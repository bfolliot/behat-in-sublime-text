Run Behat in Sublime text
===============

This plugin allows you the run the Behat tests using the Sublime Text interface, without having to open and use the command line.

It's a fork of [Simple PHPUnit](https://github.com/evgeny-golubev/SimplePHPUnit-for-Sublime-Text).

### Available commands:

- `Behat: Run`
- `Behat: Run with params`

### Installation:

Use Package Controller ("Run Behat") or clone this repository in your Sublime Text Packages directory, and you're ready to go.

### Usage:

Press Cmd + Shift + P for the dropdown command list, search for `Behat: `, and pick your command. Also you can use `Tools/Behat...` menu item

### Keybinding:

You can use command `run_behat` for your keybinding.

Example:

```json
{ "keys": ["super+ctrl+alt+t"], "command": "run_behat" }
```

### Notes:

- Behat config file needs to been in the root folder of your structure in the sidebar or in the a folder `config` in the root folder.
- You need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.
