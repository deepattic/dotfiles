from libqtile import bar, layout, qtile, widget
from libqtile.config import Match, Screen
from libqtile.config import EzKey as Key
from libqtile.config import EzClick, EzDrag
from libqtile.lazy import lazy
from libqtile.config import Group

from colors import default_theme as colors

menu = "dmenu_run -p \"Run:\" -b"
file_manager = "thunar"
wezterm = "wezterm --config-file=.config/wezterm/wezterm.lua"
terminal = wezterm 

keys = [
    Key("M-h", lazy.layout.left(), desc="Move focus to left"),
    Key("M-l", lazy.layout.right(), desc="Move focus to right"),
    Key("M-j", lazy.layout.down(), desc="Move focus down"),
    Key("M-k", lazy.layout.up(), desc="Move focus up"),
    Key("M-n", lazy.layout.next(), desc="Move window focus to other window"),
    Key("M-<space>", lazy.spawn(menu), desc="Move window focus to other window"),
    Key("M-S-h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key("M-S-l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key("M-S-j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key("M-S-k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key("M-C-h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key("M-C-l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key("M-C-j", lazy.layout.grow_down(), desc="Grow window down"),
    Key("M-C-k", lazy.layout.grow_up(), desc="Grow window up"),
    Key("M-C-n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        "M-S-<return>",
        lazy.spawn(file_manager),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key("M-<return>", lazy.spawn(terminal), desc="Launch terminal"),
    Key("M-<tab>", lazy.next_layout(), desc="Toggle between layouts"),
    Key("M-S-w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        "M-f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key("M-t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key("M-C-r", lazy.reload_config(), desc="Reload the config"),
    Key("M-C-q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key("M-r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

mpv_group = {
    "label": "mpv",
    "layouts": [layout.Max()],
    "matches": [
        Match(wm_class="mpv"),
    ],
}
web_group = {
    "label": "www",
    "matches":[Match(wm_class="Firefox")],
}
define_groups = [{}, {**web_group}, {}, {}, {}, {}, {}, {**mpv_group}, {}]
groups = [
    Group(name=str(idx), **group)
    for idx, group in enumerate(define_groups, start=1)
]

for i in groups:
    keys.extend(
        [
            Key(
                f"M-{i.name}",
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.label),
            ),
            Key(
                f"M-S-{i.name}",
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.label),
            ),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 3,
    "border_focus": colors["pine"],
    "border_normal": colors["base"]
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Roboto",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/python-logo-only.svg',
                    margin=3
                ),
                # widget.CurrentLayout(),
                widget.GroupBox(
                    active=colors["foam"],
                    inactive=colors["muted"],
                    highlight_method='line',
                    highlight_color=colors["overlay"],
                    this_screen_border = colors["love"],
                    this_current_screen_border = colors["foam"],
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            background = colors["surface"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    EzDrag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    EzDrag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    EzClick("M-2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Auto start applications
import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
