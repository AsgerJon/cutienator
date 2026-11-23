#!/usr/bin/env bash
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#
#  Sets the build machine in Google's cloud up for our work. It runs
#  ON the machine, as a user that has 'sudo' without a password, once:
#  the disk of the machine keeps what it does. From the PC:
#
#    ssh builder@ADDRESS 'bash -s' < bin/cloud_setup.sh
#
#  It is the record of how the machine was set up, for the day its
#  disk is made anew. It may run any number of times: what is in place
#  already is left as it is.
#
#  In this order:
#  1. The dead hand: a timer that powers the machine off when
#     '/run/deadhand' went untouched for 15 minutes. A missing file
#     counts as fresh, so a boot gets its 15 minutes. It is checked to
#     be enabled and running, and nothing else is done before it is.
#  2. The packages named below, each with who needs it. Only those
#     that are missing are fetched.
#  3. A look that every program the build and the generators call is
#     there.
#
#  Nothing of Qt is installed here: the Qt of the PC the library is
#  built for is copied up by 'bin/cloud_build.sh'.
set -u -o pipefail

PACKAGES=(
  #  The compiler the build calls, 'clang++'.
  clang
  #  The headers of the C++ library 'clang++' compiles against, and
  #  with them the linker.
  g++
  #  'readelf', 'objcopy', 'nm' and 'c++filt', which the generators
  #  call themselves.
  binutils
  #  Keeps what was compiled, so a file that did not change is not
  #  compiled again.
  ccache
  #  Copies the sources up and the library back.
  rsync
  #  Runs 'Rituals.build()' and the generators.
  python3
  #  'flock': one build at a time.
  util-linux
  #  Headers that Qt's own headers pull in: OpenGL for QtGui, and for
  #  the headers Qt calls private ICU and double-conversion.
  libgl-dev
  libicu-dev
  libdouble-conversion-dev
  #  For the rehearsal of the test job. The linker of the build for
  #  Windows.
  lld
  #  Runs the Windows Pythons and the library built for Windows.
  wine
  #  What Qt's own package for Linux wants at hand when the tests run
  #  against it.
  libegl1
  libfontconfig1
)
PROGRAMS=(
  clang++ ccache rsync python3 flock readelf objcopy nm c++filt
  ld.lld wine
)

say() {
  printf 'setup: %s\n' "$*"
}

fail() {
  say "FAILED: $*" >&2
  exit 1
}

#  Writes what comes in to a file of the system, when the file is not
#  that already, and says so by its exit code: 0 when it wrote.
writeFile() {
  local path=$1 mode=$2 fresh
  fresh=$(mktemp) || fail "no temporary file could be made"
  cat > "$fresh"
  if sudo -n cmp -s "$fresh" "$path"; then
    rm "$fresh"
    return 1
  fi
  sudo -n install -m "$mode" "$fresh" "$path" \
    || fail "'$path' could not be written"
  rm "$fresh"
  return 0
}

sudo -n true 2> /dev/null \
  || fail "this user has no 'sudo' without a password"

#  1. The dead hand.
wrote=
writeFile /usr/local/sbin/deadhand 755 <<'EOF' && wrote=yes
#!/bin/sh
# The dead hand: powers the machine off when nobody has touched
# /run/deadhand for 15 minutes. A missing file counts as fresh: it is
# made here, so after a boot the clock starts at the first look.
FILE="${DEADHAND_FILE:-/run/deadhand}"
LIMIT="${DEADHAND_SECONDS:-900}"
if [ ! -e "$FILE" ]; then
  touch "$FILE"
  chmod 666 "$FILE"
fi
AGE=$(( $(date +%s) - $(stat -c %Y "$FILE") ))
if [ "$AGE" -lt "$LIMIT" ]; then
  [ -n "$DEADHAND_DRY" ] && echo "stays on: touched $AGE s ago"
  exit 0
fi
if [ -n "$DEADHAND_DRY" ]; then
  echo "would power off: untouched for $AGE s"
  exit 0
fi
logger -t deadhand "untouched for $AGE s: powering off"
systemctl poweroff
EOF
writeFile /etc/systemd/system/deadhand.service 644 <<'EOF' && wrote=yes
[Unit]
Description=Powers off when /run/deadhand went untouched for 15 minutes

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/deadhand
EOF
writeFile /etc/systemd/system/deadhand.timer 644 <<'EOF' && wrote=yes
[Unit]
Description=Looks every minute whether the machine is still in use

[Timer]
OnBootSec=1min
OnUnitActiveSec=1min
AccuracySec=5s

[Install]
WantedBy=timers.target
EOF
if [ -n "$wrote" ]; then
  sudo -n systemctl daemon-reload || fail "systemd did not take the timer"
fi
if [ "$(systemctl is-enabled deadhand.timer 2> /dev/null)" != enabled ] \
  || [ "$(systemctl is-active deadhand.timer 2> /dev/null)" != active ]
then
  sudo -n systemctl enable --now deadhand.timer \
    || fail "the dead hand could not be switched on"
  wrote=yes
fi
[ "$(systemctl is-enabled deadhand.timer)" = enabled ] \
  || fail "the dead hand is not enabled"
[ "$(systemctl is-active deadhand.timer)" = active ] \
  || fail "the dead hand is not running"
missingFile=$(mktemp -u)
answer=$(DEADHAND_FILE=$missingFile DEADHAND_DRY=1 /usr/local/sbin/deadhand)
rm -f "$missingFile"
case "$answer" in
  "stays on"*) ;;
  *) fail "the dead hand does not take a missing file for fresh";;
esac
if [ -n "$wrote" ]; then
  say "the dead hand was put in place: enabled and running"
else
  say "the dead hand is in place: enabled and running"
fi

#  2. The packages.
missing=()
for package in "${PACKAGES[@]}"; do
  dpkg -s "$package" > /dev/null 2>&1 || missing+=("$package")
done
if [ "${#missing[@]}" -gt 0 ]; then
  say "fetching ${missing[*]}"
  export DEBIAN_FRONTEND=noninteractive
  sudo -n apt-get update -qq > /dev/null \
    || fail "'apt-get update' did not go through"
  sudo -n DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
    --no-install-recommends "${missing[@]}" > /tmp/cloud_setup_apt.log \
    2>&1 || fail "'apt-get install' did not go through: \
$(tail -n 3 /tmp/cloud_setup_apt.log)"
else
  say "all ${#PACKAGES[@]} packages are there"
fi

#  3. The programs.
for program in "${PROGRAMS[@]}"; do
  command -v "$program" > /dev/null \
    || fail "the program '$program' is not there"
done
say "ready: $(clang++ --version | head -n 1), $(nproc) processors"
