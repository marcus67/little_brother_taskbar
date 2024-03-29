![LittleBrotherTaskbar-Logo](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/little_brother_taskbar/static/icons/little-brother-taskbar-logo_128x128.png)

# Change History 

This document lists all changes of `LittleBrotherTaskbar` with the most recent changes at the top.

## Version 0.1.23 (release, March 5th, 2024)

* Upgrade `python_base_app` to 0.2.50

## Version 0.1.22 (release, June 5th, 2022)

* Support Windows
* Upgrade `python_base_app` to 0.2.40 (eliminate dependency on PIP package `python-ldap`)
* Call `MainLoop` of `wxpython` in main thread
* Derive path of temporary directory in a platform independent way 
* Added some debugging output
* Build URLs in a platform independent way 

## Version 0.1.21 (release, March 12th, 2022)

* Merge Snyk security fix

## Version 0.1.20 (release, March 12th, 2022)

* Add CODE_OF_CONDUCT.md and CONTRIBUTING.md
* Add Snyk package health indicator in README.md
* Upgrade `python_base_app` to 0.2.36

## Version 0.1.19 (release, August 15th, 2021)

* Describe workaround for modern Gnome desktops. See [README](README.md).  
* Closes #33, see [here](https://github.com/marcus67/little_brother_taskbar/issues/33)  

## Version 0.1.18 (release, August 15th, 2021)

*   Add [CodeClimate](https://codeclimate.com/github/marcus67/little_brother_taskbar) rating to README.md
*   Handle status window using `wxglade`
*   Use `HtmlWindow` for displaying message    
*   Remove resize hack
*   Upgrade `python_base_app` to 0.2.23
*   Closes #30, see [here](https://github.com/marcus67/little_brother_taskbar/issues/30)
*   Update Italian localization
*   Add tabs to configuration dialog

## Version 0.1.17 (release, June 6th, 2021)

*   Closes #25, see [here](https://github.com/marcus67/little_brother_taskbar/issues/25)
*   Closes #26, see [here](https://github.com/marcus67/little_brother_taskbar/issues/26)
*   Closes #27, see [here](https://github.com/marcus67/little_brother_taskbar/issues/27)
*   Add class `StatusFrame`
*   Add script `run_little_brother_taskbar_test_suite_no_env.py` 
*   Activate Sonarcube analysis

## Version 0.1.16 (release, February 24, 2021)

*   Accepts [pull request regarding Italian localization](https://github.com/marcus67/little_brother_taskbar/pull/23)
*   Accepts [pull request regarding French localization](https://github.com/marcus67/little_brother_taskbar/pull/24)
*   Beautified tray logo

## Version 0.1.15 (release, January 31st, 2021)

*   Upgrade to `python_base_app` 0.2.13 (fix CircleCI CPU limit issue)

## Version 0.1.14 (release, January 26th, 2021)

*   Fix wrong release branch (some changes from master branch were missing)

## Version 0.1.13 (release, January 26th, 2021)

*   Update `wxPython` to 4.1.1 (this solves problem with compilation error of `wxPython` for current `setuptools`)
*   Upgrade to `python_base_app` 0.2.10
*   Correct URLs for test.pypi.org and pypi.org

## Version 0.1.12 (release, September 7th, 2020)

*   Closes #17, see [here](https://github.com/marcus67/little_brother_taskbar/issues/17)
*   Closes #18, see [here](https://github.com/marcus67/little_brother_taskbar/issues/18)
*   Add icon in window header to show whether spoken notifications are enabled
*   Update Italian localization

## Version 0.1.11 (release, August 27th, 2020)

*   Use LocaleHelper
*   More consistent naming of configurations options and variables
*   Closes #1, see [here](https://github.com/marcus67/little_brother_taskbar/issues/1)
*   Closes #2, see [here](https://github.com/marcus67/little_brother_taskbar/issues/2)
*   Closes #5, see [here](https://github.com/marcus67/little_brother_taskbar/issues/5)
*   Closes #12, see [here](https://github.com/marcus67/little_brother_taskbar/issues/12)
*   Closes #14, see [here](https://github.com/marcus67/little_brother_taskbar/issues/14)
*   Upgrade to `python_base_app` 0.2.1

## Version 0.1.10 (release, August 8th, 2020)

*   Set default locale to "en" 
*   Add YouTube video

## Version 0.1.9 (release, August 4th, 2020)

*   Upgrade to `python_base_app` 0.2.0

## Version 0.1.8 (release, June 8th, 2020)

*   Add Danish localization (locale 'da')
*   Add Spanish localization (locale 'es')
*   Upgrade to `python_base_app` 0.1.11

## Version 0.1.7 (release, May 7th, 2020)

*   Add Finnish localization (locale 'fi')
*   Add Turkish localization (locale 'tr')
*   Add Japanese localization (locale 'ja')
*   Add Bangla localization (locale 'bn')
*   Add French localization (locale 'fr')
*   Add Thai localization (locale 'th')
*   Add license file
*   Suppress old spoken notifications upon login
*   Upgrade to `python_base_app` 0.1.9
*   Remove translations of `python_base_app` from Babel files
*   Add README.md section on installation as desktop startup application 

## Version 0.1.6 (release, April 18th, 2020)

*   Add Dutch localization (locale 'nl')
*   Upgrade to `python_base_app` 0.1.8

## Version 0.1.5 (release, April 12th, 2020)

*   Optionally provide speech generation for notification messages
*   Upgrade to `python_base_app` 0.1.6

## Version 0.1.4 (release, April 10th, 2020)

*   Activate the Italian translations
*   Increase default width of window to allow for Italian texts to be fully displayed 

## Version 0.1.3 (April 10th, 2020)

*   Upgrade to python_base_app 0.1.5
*   Read long_description of `setup.py` from `README.md`
*   Provide new icon showing panda in tray
*   Provide empty test suite for CI
*   Align version of PIP package `Jinja2` to that of `python-base-app`
*   Remove some Codacy smells

## Version 0.1 Revision 02 (April 2nd, 2020)

*   Automatic loading of user configuration file
*   Provide sample configuration file**
*   Provide default English translations for Italian and French

## Version 0.1 Revision 01 (March 28th, 2020)

*   Initial version
