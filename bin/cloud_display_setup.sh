#!/usr/bin/env bash
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#
#  Sets up a graphical session on the build machine in Google's cloud:
#  LXQt on Wayland, with labwc as the compositor, on Google's virtual
#  display device. The machine runs Arch Linux and has that device
#  switched on. Run it there as root; running it again changes nothing
#  that is so already:
#
#    ssh ... 'sudo bash -s' < bin/cloud_display_setup.sh
#
#  What it does:
#  1. Installs from pacman: LXQt, its Wayland session, labwc, greetd,
#     wayvnc and grim. Qt's Wayland platform comes with 'qt6-base';
#     'qt6-wayland' is Qt's Wayland compositor, which nothing here uses,
#     and is not installed: the machine's Qt stays the PC's.
#  2. Has greetd log SESSION_USER ('builder' unless set) into the LXQt
#     Wayland session at boot, on the virtual display, with no one at a
#     screen. When that session ends, greetd shows its plain login
#     prompt there instead.
#  3. Sets labwc up for a display with no 3D: it draws in software
#     ('pixman') and draws the pointer itself. Nothing turns the
#     display off or locks it for being idle, so it can be watched and
#     photographed at any time: neither labwc's idle timer, nor LXQt's
#     power management, nor its screensaver.
#  4. Starts wayvnc with the session, on a unix socket in the user's
#     runtime folder: no port is opened, and only that user reaches it.
#     The session is watched through ssh, as 'bin/cloud_watch.sh' does
#     from the PC.
#  5. Writes '/usr/local/bin/ondisplay': 'ondisplay COMMAND...' runs a
#     command inside the session as that user, as a Qt window of
#     cutienator, or 'ondisplay grim shot.png' for a screenshot.
#
#  The dead hand is not touched. The session does not keep the machine
#  awake: it powers off 15 minutes after '/run/deadhand' was last
#  touched, as it did before.
set -eu -o pipefail

SESSION_USER=${SESSION_USER:-builder}
[ "$(id -u)" -eq 0 ] || { echo "run it as root" >&2; exit 1; }
home=$(getent passwd "$SESSION_USER" | cut -d: -f6)
[ -n "$home" ] || { echo "there is no user '$SESSION_USER'" >&2; exit 1; }
uid=$(id -u "$SESSION_USER")
MARK='Written by bin/cloud_display_setup.sh'

#  Runs a command as the session user, so what it writes is theirs.
asUser() {
  runuser -u "$SESSION_USER" -- "$@"
}

#  Adds a line to a file of the session user, when it is not there.
ensureLine() {
  local file=$1 line=$2
  asUser touch "$file"
  grep -qxF -- "$line" "$file" || printf '%s\n' "$line" \
    | asUser tee -a "$file" > /dev/null
}

echo "1. packages"
pacman -S --needed --noconfirm lxqt lxqt-wayland-session labwc greetd \
  wayvnc grim

echo "2. greetd logs $SESSION_USER into the session at boot"
if [ -f /etc/greetd/config.toml ] && [ ! -e /etc/greetd/config.toml.orig ] \
    && ! grep -qF "$MARK" /etc/greetd/config.toml; then
  cp /etc/greetd/config.toml /etc/greetd/config.toml.orig
fi
cat > /etc/greetd/config.toml <<EOF
#  $MARK. The package's own file is
#  beside it as config.toml.orig.
[terminal]
vt = 1

#  After the first session ends: a plain login prompt on the display.
[default_session]
command = "agreety --cmd startlxqtwayland"
user = "greeter"

#  At boot: $SESSION_USER, straight into LXQt on Wayland.
[initial_session]
command = "startlxqtwayland"
user = "$SESSION_USER"
EOF
systemctl enable greetd.service
systemctl set-default graphical.target

echo "3. LXQt with labwc, for a display with no 3D"
config=$home/.config
asUser mkdir -p "$config/lxqt"
session=$config/lxqt/session.conf
asUser touch "$session"
if grep -q '^compositor[[:space:]]*=' "$session"; then
  asUser sed -i 's/^compositor[[:space:]]*=.*/compositor=labwc/' "$session"
elif grep -q '^\[General\]' "$session"; then
  asUser sed -i '/^\[General\]/a compositor=labwc' "$session"
else
  printf '[General]\ncompositor=labwc\n' | asUser tee -a "$session" \
    > /dev/null
fi
#  The settings startlxqtwayland would copy at the first login.
if [ ! -d "$config/labwc" ]; then
  asUser cp -r /usr/share/lxqt/wayland/labwc "$config/labwc"
fi
environment=$config/labwc/environment
ensureLine "$environment" "#  $MARK: no 3D on the display."
ensureLine "$environment" 'WLR_RENDERER=pixman'
ensureLine "$environment" 'WLR_NO_HARDWARE_CURSORS=1'
autostart=$config/labwc/autostart
asUser touch "$autostart"
#  The display stays on: no idle timer of labwc turns it off, and
#  LXQt's power management and screensaver are not started for the
#  user, as the autostart rules have it for an entry marked hidden.
asUser sed -i 's/^\(swayidle .*wlopm --off.*\)$/# \1/' "$autostart"
asUser mkdir -p "$config/autostart"
for entry in lxqt-powermanagement lxqt-xscreensaver-autostart; do
  printf '[Desktop Entry]\n#  %s.\nHidden=true\n' "$MARK" \
    | asUser tee "$config/autostart/$entry.desktop" > /dev/null
done

echo "4. wayvnc with the session, on a unix socket"
ensureLine "$autostart" "#  $MARK: the session is watched"
ensureLine "$autostart" "#  through ssh, on a socket only its user reaches."
ensureLine "$autostart" \
  'wayvnc --unix-socket "$XDG_RUNTIME_DIR/wayvnc.sock" > /dev/null 2>&1 &'

echo "5. /usr/local/bin/ondisplay"
cat > /usr/local/bin/ondisplay <<EOF
#!/bin/sh
#  $MARK. Runs a command inside the
#  graphical session of $SESSION_USER, as that user:
#    ondisplay grim /tmp/shot.png
#    ondisplay python3 -m some.qt.program
runtime=/run/user/$uid
socket=\$(ls "\$runtime" 2> /dev/null | grep -E '^wayland-[0-9]+\$' \\
  | head -n 1)
if [ -z "\$socket" ]; then
  echo "no Wayland session of $SESSION_USER runs" >&2
  exit 1
fi
export XDG_RUNTIME_DIR="\$runtime" WAYLAND_DISPLAY="\$socket"
export QT_QPA_PLATFORM=wayland XDG_SESSION_TYPE=wayland
export DBUS_SESSION_BUS_ADDRESS="unix:path=\$runtime/bus"
if [ "\$(id -u)" -eq $uid ]; then
  exec "\$@"
fi
exec sudo -u $SESSION_USER --preserve-env=XDG_RUNTIME_DIR,WAYLAND_DISPLAY\\
,QT_QPA_PLATFORM,XDG_SESSION_TYPE,DBUS_SESSION_BUS_ADDRESS -- "\$@"
EOF
chmod 755 /usr/local/bin/ondisplay

echo "done: the session starts at the next boot, or now with"
echo "  systemctl start greetd"
