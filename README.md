# Sublime Text - edit in new tab plugin
My first Sublime Text plugin.

## Motivation
[<img src="https://raw.github.com/borjacampina/sublimetext-edit_in_new_tab-plugin/master/tweet.png" width="590" />](https://twitter.com/Wakkos/status/807287658925948928)

## Demo
<img src="https://raw.github.com/borjacampina/sublimetext-edit_in_new_tab-plugin/master/example.gif" width="590" />

## Changes
- Dec 10: support for multiple selection
- Dec 9: first version

## Install

Clone this repository in your Sublime Text Packages directory:

- Linux: `~/.config/sublime-text-3/Packages/`
- OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
- Windows: `%APPDATA%/Sublime Text 3/Packages/`

Mac installation example:
```bash
git clone https://github.com/borjacampina/sublimetext-edit_in_new_tab-plugin "$HOME/Library/Application Support/Sublime Text 3/Packages/EditInNewTab"
```

## Adding a keyboard shortcut
`Sublime Text 3` > `Preferences` > `Key Bindings`
```json
[
  { "keys": ["super+shift+w"], "command": "edit_in_new_tab" }
]
```
