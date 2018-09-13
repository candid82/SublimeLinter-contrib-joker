SublimeLinter-contrib-joker
================================

[![Build Status](https://travis-ci.org/candid82/SublimeLinter-contrib-joker.svg?branch=master)](https://travis-ci.org/candid82/SublimeLinter-contrib-joker)

This linter plugin for [SublimeLinter][docs] provides an interface to [joker](https://github.com/candid82/joker). It will be used with files that have the “__clojure__” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `joker` is installed on your system. Refer to [joker's docs](https://github.com/candid82/joker#getting-started) for installation instructions.


**Note:** This plugin requires `joker` __0.9.7__ or later.

### Linter configuration
In order for `joker` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Please read about [Joker's linter mode](https://github.com/candid82/joker#linter-mode) to understand its capabilities and limitations. Specifically, it's important to [configure Joker](https://github.com/candid82/joker#reducing-false-positives) to reduce false positives.

Once you have installed and configured `joker`, you can proceed to install the SublimeLinter-contrib-joker plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `joker`. Among the entries you should see `SublimeLinter-contrib-joker`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Examples

### Reader errors

![image](https://cloud.githubusercontent.com/assets/882970/22320933/6da69702-e345-11e6-876b-3182df8bd85e.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320909/27a242d8-e345-11e6-9722-b0e6867f195b.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320877/f69fbbca-e344-11e6-84e4-0fa5968397ec.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320929/562e60be-e345-11e6-8231-c42f661f94db.png)

### Parser errors

![image](https://cloud.githubusercontent.com/assets/882970/22320956/a6491292-e345-11e6-9787-7550a56907fd.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320767/0f9f3fa2-e344-11e6-8c49-f5f4c32a5b96.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320815/71017418-e344-11e6-98ff-dff980497ca2.png)

### Built-in macros errors

![image](https://cloud.githubusercontent.com/assets/882970/22320945/851cc8c0-e345-11e6-81f6-3b32c389de1c.png)

### Speculative warnings

![image](https://cloud.githubusercontent.com/assets/882970/22320971/cebea638-e345-11e6-9dac-a32e5afd4293.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320868/d6318ada-e344-11e6-9be4-388723b69b7c.png)

![image](https://cloud.githubusercontent.com/assets/882970/22320695/6e1b7d4e-e343-11e6-84b5-4f0121ba2da1.png)

### Unused namespaces, vars and let bindings

![image](https://cloud.githubusercontent.com/assets/882970/24892779/f0de32aa-1e33-11e7-9f28-f7759b5572f0.jpg)



## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
