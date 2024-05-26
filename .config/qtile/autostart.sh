#!/bin/sh
pipewire &
nm-applet &
sleep 12 && volumeicon &
xdg-user-dirs-update &
/usr/libexec/xfce-polkit &
setxkbmap us -variant colemak_dh &
nitrogen --restore &
