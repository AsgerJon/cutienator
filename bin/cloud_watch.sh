#!/usr/bin/env bash
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#
#  Shows the graphical session of the build machine in Google's cloud
#  on this PC, through ssh alone: the wayvnc socket on the machine,
#  which 'bin/cloud_display_setup.sh' sets up, is forwarded to a port
#  on this PC's own loopback, and a VNC viewer opens that. No port is
#  opened on the machine or in the cloud.
#
#    bin/cloud_watch.sh
#
#  It starts the machine when it is stopped. While it runs,
#  '/run/deadhand' on the machine is touched once a minute, as during a
#  build: the machine stays on while it is watched, and powers off 15
#  minutes after this ends. Closing the viewer, or Ctrl-C, ends it.
#
#  You provide, when the defaults do not fit:
#    CUTIENATOR_INSTANCE  the name of the machine; 'cutienator'
#    CUTIENATOR_KEY       the key to log in with;
#                         '~/.config/cutienator-gcp/id_ed25519'
#    CUTIENATOR_PORT      the port on this PC's loopback; 5901
#    VIEWER               the VNC viewer, given 'vnc://HOST:PORT'; 'krdc'
#    CUTIENATOR_LOGIN     the user whose session is watched, the one
#                         'bin/cloud_display_setup.sh' was run for;
#                         'builder'
set -u -o pipefail

REPO=$(cd "$(dirname "$0")/.." && pwd)
INSTANCE=${CUTIENATOR_INSTANCE:-cutienator}
KEY=${CUTIENATOR_KEY:-$HOME/.config/cutienator-gcp/id_ed25519}
PORT=${CUTIENATOR_PORT:-5901}
VIEWER=${VIEWER:-krdc}
LOGIN=${CUTIENATOR_LOGIN:-builder}
KEPT=$REPO/tmp/cloud_build
KEEPER=
TUNNEL=

fail() {
  echo "FAILED: $*" >&2
  exit 1
}

#  Logs in as 'bin/cloud_build.sh' does, under the same name of the key.
onMachine() {
  ssh -F /dev/null -i "$KEY" -o IdentitiesOnly=yes -o BatchMode=yes \
    -o UserKnownHostsFile="$KEPT/known_hosts" \
    -o HostKeyAlias="$INSTANCE-build-machine" \
    -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 \
    -o ServerAliveInterval=15 -o ServerAliveCountMax=4 \
    -o LogLevel=ERROR "$@"
}

#  Ends the tunnel and the touching. Each runs in a subshell of its
#  own, so the ssh and the sleep inside are ended first.
stopAll() {
  local pid
  for pid in $KEEPER $TUNNEL; do
    pkill -P "$pid" 2> /dev/null
    kill "$pid" 2> /dev/null
  done
}
trap stopAll EXIT

command -v gcloud > /dev/null || fail "'gcloud' is not installed"
command -v "$VIEWER" > /dev/null || fail "there is no viewer '$VIEWER'"
state=$(gcloud compute instances describe "$INSTANCE" \
  --format='get(status)') || fail "gcloud could not say how it is"
if [ "$state" = TERMINATED ]; then
  echo "the machine is stopped: starting it"
  gcloud compute instances start "$INSTANCE" --quiet \
    || fail "gcloud could not start '$INSTANCE'"
fi
ADDRESS=$(gcloud compute instances describe "$INSTANCE" \
  --format='get(networkInterfaces[0].accessConfigs[0].natIP)')
[ -n "$ADDRESS" ] || fail "the machine has no address"
tries=0
until uid=$(onMachine "$LOGIN@$ADDRESS" 'touch /run/deadhand; id -u' \
    2> /dev/null); do
  tries=$((tries + 1))
  [ "$tries" -lt 30 ] || fail "the machine takes no login"
  sleep 6
done
socket=/run/user/$uid/wayvnc.sock
#  A session that started at boot has its socket after a few seconds.
tries=0
until onMachine "$LOGIN@$ADDRESS" "test -S $socket"; do
  tries=$((tries + 1))
  [ "$tries" -lt 20 ] || fail "no '$socket': the session does not run \
there; see bin/cloud_display_setup.sh"
  sleep 3
done
( while :; do
    onMachine "$LOGIN@$ADDRESS" 'touch /run/deadhand' 2> /dev/null
    sleep 60
  done ) > /dev/null 2>&1 &
KEEPER=$!
onMachine -N -o ExitOnForwardFailure=yes \
  -L "127.0.0.1:$PORT:$socket" "$LOGIN@$ADDRESS" &
TUNNEL=$!
sleep 2
kill -0 "$TUNNEL" 2> /dev/null || fail "the tunnel did not open"
echo "watching through 127.0.0.1:$PORT; close the viewer to end"
"$VIEWER" "vnc://127.0.0.1:$PORT"
