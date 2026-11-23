#!/usr/bin/env bash
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#
#  Builds the Ugly side on the build machine in Google's cloud, so this
#  PC does not have to, and brings the built library back.
#
#    bin/cloud_build.sh
#
#  What it does, in this order:
#  1. Starts the machine when it is stopped, and waits until it takes
#     a login.
#  2. Makes sure the dead hand runs there, and builds nothing when it
#     does not. The machine is set up once, with 'bin/cloud_setup.sh',
#     and its disk keeps that.
#  3. Copies up what a build needs: the package, the Qt of THIS PC
#     (its headers, its shared objects and its 'mkspecs', found by
#     asking 'qmake6' here), and worktoy as the Python here has it.
#     That Qt lies there at the very paths it has here, so what
#     'clang++' is told is the same on both.
#  4. Builds there, with 'Rituals.build()', the way a build runs here.
#     While it builds, '/run/deadhand' on the machine is touched from
#     here once a minute.
#  5. Copies the built library back, to where a build here puts it,
#     and opens it here.
#  When the connection drops, it begins again at 1, five times at
#  most. A build the compiler refuses is no dropped connection: that
#  ends it at once, with what the compiler said.
#
#  It never stops the machine. A timer on the machine, the dead hand,
#  powers it off when '/run/deadhand' went untouched for 15 minutes.
#
#  The library has to run on this PC, so it is built against this PC's
#  Qt and with what 'Build' tells the compiler here, nothing more. The
#  'clang++' it meets on the machine is a small script written below:
#  it runs the real one through ccache, and refuses '-march=native'.
#
#  You provide, when the defaults do not fit:
#    PYTHON               the Python that has worktoy; 'python3'
#    CUTIENATOR_INSTANCE  the name of the machine; 'cutienator'
#    CUTIENATOR_KEY       the key to log in with;
#                         '~/.config/cutienator-gcp/id_ed25519'
#  The project and the zone are those 'gcloud' is set to.
set -u -o pipefail

REPO=$(cd "$(dirname "$0")/.." && pwd)
PYTHON=${PYTHON:-python3}
INSTANCE=${CUTIENATOR_INSTANCE:-cutienator}
KEY=${CUTIENATOR_KEY:-$HOME/.config/cutienator-gcp/id_ed25519}
LOGIN=builder
THERE=cutienator-build
KEPT=$REPO/tmp/cloud_build
ATTEMPTS=5
DROPPED=75
ADDRESS=
KEEPER=

say() {
  printf '%s  %s\n' "$(date +%H:%M:%S)" "$*"
}

fail() {
  say "FAILED: $*" >&2
  exit 1
}

#  Runs a command on the machine. The address changes at every start,
#  so the key of the machine is kept under one name of our own.
onMachine() {
  ssh -F /dev/null -i "$KEY" -o IdentitiesOnly=yes -o BatchMode=yes \
    -o UserKnownHostsFile="$KEPT/known_hosts" \
    -o HostKeyAlias="$INSTANCE-build-machine" \
    -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 \
    -o ServerAliveInterval=15 -o ServerAliveCountMax=4 \
    -o LogLevel=ERROR "$@"
}

#  Copies with rsync, logging in the same way.
copy() {
  rsync -e "ssh -F /dev/null -i '$KEY' -o IdentitiesOnly=yes \
-o BatchMode=yes -o UserKnownHostsFile='$KEPT/known_hosts' \
-o HostKeyAlias='$INSTANCE-build-machine' \
-o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 \
-o ServerAliveInterval=15 -o ServerAliveCountMax=4 \
-o LogLevel=ERROR" "$@"
}

#  Says whether an exit code means the connection dropped: 255 is how
#  ssh says so, and the others are rsync's words for the same.
isDropped() {
  case "$1" in
    255|10|12|30|35) return 0;;
  esac
  return 1
}

#  Ends one try: a dropped connection is tried again, anything else
#  ends the whole run.
endTry() {
  local code=$1
  shift
  if isDropped "$code"; then
    say "the connection dropped while $* (code $code)"
    return $DROPPED
  fi
  fail "$* (code $code)"
}

askState() {
  gcloud compute instances describe "$INSTANCE" --format='get(status)'
}

#  Starts the machine when it is stopped, and finds its address.
startMachine() {
  local state waited=0
  state=$(askState) || fail "gcloud could not say how '$INSTANCE' is"
  while [ "$state" != RUNNING ]; do
    case "$state" in
      TERMINATED)
        say "the machine is stopped: starting it"
        gcloud compute instances start "$INSTANCE" --quiet \
          || fail "gcloud could not start '$INSTANCE'"
        ;;
      STOPPING|PROVISIONING|STAGING)
        say "the machine is $state: waiting"
        sleep 10
        ;;
      *)
        fail "the machine is '$state', which this script does not mend"
        ;;
    esac
    waited=$((waited + 1))
    [ "$waited" -lt 60 ] || fail "the machine never came to run"
    state=$(askState) || fail "gcloud could not say how '$INSTANCE' is"
  done
  ADDRESS=$(gcloud compute instances describe "$INSTANCE" \
    --format='get(networkInterfaces[0].accessConfigs[0].natIP)') \
    || fail "gcloud could not give the address of '$INSTANCE'"
  [ -n "$ADDRESS" ] || fail "the machine runs and has no address"
}

#  Waits until the machine takes a login, and touches the file the
#  dead hand watches.
waitForLogin() {
  local tries=0
  until onMachine "$LOGIN@$ADDRESS" 'touch /run/deadhand' 2> /dev/null
  do
    tries=$((tries + 1))
    [ "$tries" -lt 30 ] || return 255
    sleep 6
  done
}

#  Touches the file the dead hand watches, once a minute, from here:
#  when this PC goes away, the touching ends with it.
keepAwake() {
  while :; do
    onMachine "$LOGIN@$ADDRESS" 'touch /run/deadhand' 2> /dev/null
    sleep 60
  done
}

stopKeeper() {
  if [ -n "$KEEPER" ]; then
    kill "$KEEPER" 2> /dev/null
    wait "$KEEPER" 2> /dev/null
    KEEPER=
  fi
}

#  Makes sure the dead hand is on the machine and running, before
#  anything is copied or built: without it the machine would run, and
#  cost, until someone stops it by hand.
checkDeadHand() {
  local answer code
  answer=$(onMachine "$LOGIN@$ADDRESS" \
    'systemctl is-enabled deadhand.timer; systemctl is-active \
deadhand.timer' 2> /dev/null)
  code=$?
  if isDropped "$code"; then
    endTry "$code" "asking for the dead hand"
    return
  fi
  [ "$(echo $answer)" = "enabled active" ] \
    || fail "the dead hand does not run on the machine: set the \
machine up with bin/cloud_setup.sh, as its heading says"
}

#  Copies with rsync as the machine's root, for this PC's Qt, which
#  lies there where it lies here. The files become root's own there.
copyAsRoot() {
  copy --rsync-path='sudo -n rsync' -rlpt --chmod=a+rX "$@"
}

#  Copies up the package, this PC's Qt and worktoy, and writes the two
#  small programs the build meets on the machine.
copyUp() {
  local headers libs bins data answers worktoy part code name
  local sharedObjects=()
  headers=$(qmake6 -query QT_INSTALL_HEADERS) \
    && libs=$(qmake6 -query QT_INSTALL_LIBS) \
    && bins=$(qmake6 -query QT_INSTALL_BINS) \
    && data=$(qmake6 -query QT_HOST_DATA) \
    && answers=$(qmake6 -query) \
    || fail "'qmake6' did not answer here"
  worktoy=$("$PYTHON" -B -c \
    'import os, worktoy; print(os.path.dirname(worktoy.__file__))') \
    || fail "'$PYTHON' has no worktoy; set PYTHON to the one that has"
  #  One shared object of Qt for each part that has ritual files, as
  #  'libQt6Core.so' for the folder 'QtCoreRituals', with the names
  #  that point at it.
  for part in "$REPO"/src/cutienator/occult/rituals/Qt*Rituals; do
    name=$(basename "$part")
    name=${name%Rituals}
    sharedObjects+=("$libs"/libQt6"${name#Qt}".so*)
  done
  #  This PC's Qt goes where it lies here. A Qt the machine has of its
  #  own at one of those places is not written over.
  onMachine "$LOGIN@$ADDRESS" "mkdir -p $THERE/tree/src/cutienator \
$THERE/pydeps/worktoy $THERE/shims || exit 1
for place in '$headers' '$data' ${sharedObjects[*]}; do
  if dpkg -S \"\$place\" > /dev/null 2>&1; then
    echo \"a package of the machine owns '\$place'\" >&2
    exit 3
  fi
done
sudo -n mkdir -p '$headers' '$data/mkspecs' '$bins' '$libs'"
  code=$?
  [ $code -eq 0 ] || { endTry $code "readying the folders"; return; }
  #  What is built there stays there: the object files and the library
  #  are left out, which also keeps '--delete' off them.
  copy -a --delete --exclude '__pycache__/' --exclude '*.py[cod]' \
    --exclude '/occult/demons/' --exclude '*.so' --exclude '*.dll' \
    --exclude '*.dylib' "$REPO/src/cutienator/" \
    "$LOGIN@$ADDRESS:$THERE/tree/src/cutienator/"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying the package up"; return; }
  copyAsRoot --delete "$headers/" "$LOGIN@$ADDRESS:$headers/"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying Qt's headers up"; return; }
  copyAsRoot --delete "$data/mkspecs/" \
    "$LOGIN@$ADDRESS:$data/mkspecs/"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying Qt's mkspecs up"; return; }
  copyAsRoot "${sharedObjects[@]}" "$LOGIN@$ADDRESS:$libs/"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying Qt's libraries up"; return; }
  copy -a --delete --exclude '__pycache__/' "$worktoy/" \
    "$LOGIN@$ADDRESS:$THERE/pydeps/worktoy/"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying worktoy up"; return; }
  #  'qmake6' there answers what 'qmake6' answers here. 'clang++'
  #  there runs the real one through ccache. It makes a precompiled
  #  header without the times of the files it is made of, or ccache
  #  would take every header made anew for a new one. And it refuses
  #  '-march=native': what is built has to run on this PC.
  onMachine "$LOGIN@$ADDRESS" "cat > $THERE/shims/qmake6 <<'EOF'
#!/bin/sh
#  Written by bin/cloud_build.sh. Changes made here are lost.
#  Answers 'qmake6 -query NAME' as the PC does that the library is
#  built for: the table below is what its 'qmake6 -query' prints.
[ \"\$1\" = -query ] || { echo 'only -query is answered' >&2; exit 1; }
while IFS=: read -r name answer; do
  if [ \"\$name\" = \"\$2\" ]; then
    echo \"\$answer\"
    exit 0
  fi
done <<'TABLE'
$answers
TABLE
echo \"no answer for '\$2'\" >&2
exit 1
EOF
cat > $THERE/shims/clang++ <<'EOF'
#!/bin/sh
#  Written by bin/cloud_build.sh. Changes made here are lost.
header=
for one in \"\$@\"; do
  case \"\$one\" in
    -march=native|-mtune=native|-mcpu=native)
      echo \"refused: '\$one' would not run on the PC\" >&2
      exit 1;;
    c++-header) header=yes;;
  esac
done
if [ -n \"\$header\" ]; then
  exec ccache /usr/bin/clang++ -Xclang -fno-pch-timestamp \"\$@\"
fi
exec ccache /usr/bin/clang++ \"\$@\"
EOF
chmod 755 $THERE/shims/qmake6 $THERE/shims/clang++"
  code=$?
  [ $code -eq 0 ] || { endTry $code "writing the two programs"; return; }
}

#  Builds on the machine, and says where the library lies there. One
#  build at a time: a build left over from a dropped connection is
#  waited for.
buildThere() {
  local code
  onMachine -tt "$LOGIN@$ADDRESS" "touch /run/deadhand
cd $THERE/tree || exit 1
export PATH=\"\$HOME/$THERE/shims:\$PATH\"
export PYTHONPATH=\"src:\$HOME/$THERE/pydeps\"
export CCACHE_SLOPPINESS=pch_defines,time_macros
ccache --zero-stats > /dev/null
flock ../lock python3 -B -c 'from cutienator.occult import Rituals
print(Rituals.build())' > ../build.log 2>&1
code=\$?
tail -n 12 ../build.log
ccache --show-stats | grep -E '^ *(Hits|Misses)' | head -n 2
exit \$code" | tr -d '\r' | tee "$KEPT/build.log"
  code=${PIPESTATUS[0]}
  if [ "$code" -ne 0 ]; then
    if isDropped "$code"; then
      endTry "$code" "building"
      return
    fi
    fail "the build on the machine was refused (code $code): see above"
  fi
}

#  Copies the library back to where a build here puts it. Its time is
#  kept, so 'Rituals.isStale()' sees it is newer than the ritual files.
copyBack() {
  local target relative code
  target=$(grep -E "/$THERE/tree/src/cutienator/.+" "$KEPT/build.log" \
    | grep -vE '[[:space:]]' | tail -n 1)
  [ -n "$target" ] || fail "the build did not say where the library is"
  relative=${target#*/"$THERE"/tree/}
  case "$relative" in
    src/cutienator/*) ;;
    *) fail "the library lies at '$target', outside the package";;
  esac
  copy -t "$LOGIN@$ADDRESS:$THERE/tree/$relative" "$REPO/$relative"
  code=$?
  [ $code -eq 0 ] || { endTry $code "copying the library back"; return; }
  say "the library is at $relative"
}

#  One try, from starting the machine to the library lying here.
tryOnce() {
  local code
  startMachine
  say "the machine runs; waiting for it to take a login"
  waitForLogin || { endTry 255 "logging in"; return; }
  keepAwake > /dev/null 2>&1 &
  KEEPER=$!
  checkDeadHand
  code=$?
  [ $code -eq 0 ] || { stopKeeper; return $code; }
  say "copying up the package, Qt and worktoy"
  copyUp
  code=$?
  [ $code -eq 0 ] || { stopKeeper; return $code; }
  say "building on the machine"
  buildThere
  code=$?
  [ $code -eq 0 ] || { stopKeeper; return $code; }
  copyBack
  code=$?
  stopKeeper
  return $code
}

trap stopKeeper EXIT
command -v gcloud > /dev/null || fail "'gcloud' is not installed"
command -v rsync > /dev/null || fail "'rsync' is not installed"
command -v qmake6 > /dev/null || fail "'qmake6' is not installed"
[ -r "$KEY" ] || fail "there is no key to log in with at '$KEY'"
mkdir -p "$KEPT" || fail "'$KEPT' cannot be made"
began=$(date +%s)
try=1
while :; do
  say "try $try of $ATTEMPTS"
  tryOnce
  code=$?
  [ $code -eq 0 ] && break
  [ $code -eq $DROPPED ] || fail "a try ended with code $code"
  [ "$try" -lt "$ATTEMPTS" ] \
    || fail "the connection dropped in each of $ATTEMPTS tries"
  try=$((try + 1))
  sleep 10
done
#  The library has to open on this PC, against this PC's Qt.
PYTHONPATH="$REPO/src" "$PYTHON" -B -c '
from cutienator.occult import Rituals
if Rituals.isStale():
  raise SystemExit("the library is older than a ritual file")
Rituals.getOpened()
print("opened here: %s, with %d rituals" % (
    Rituals.getTargetFile(), len(Rituals.getRitualNames())))
' || fail "the library does not open on this PC"
say "done in $(( $(date +%s) - began )) s; the dead hand will power \
the machine off after 15 idle minutes"
