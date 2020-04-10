![LittleBrotherTaskbar-Logo](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/little_brother_taskbar/static/icons/little-brother-taskbar-logo_128x128.png)

# Taskbar Tray Application for `LittleBrother`

## Overview

`LittleBrotherTaskbar` is a simple application which can be installed into the tray of the window manager
to display the remaining play time of the current user.

## Contact

The taskbar does not have a homepage of its own. It sharing `LittleBrother`'s homepage. Visit the project 
at [Facebook](https://www.facebook.com/littlebrotherdebian) or write comments to little-brother(at)web.de.

## Screenshots

The following screenshots show the display of `LittleBrotherTaskbar`.  

![Screenshot Status](doc/screenshot_status_ok.png) 
![Screenshot Status](doc/screenshot_status_warning.png) 

## Change History 

See [here](https://github.com/marcus67/little_brother_taskbar/blob/master/CHANGES.md)

## GitHub Status

<A HREF="https://github.com/marcus67/little_brother_taskbar">
<IMG SRC="https://img.shields.io/github/forks/marcus67/little_brother_taskbar.svg?label=forks"></A> 
<A HREF="https://github.com/marcus67/little_brother_taskbar/stargazers">
<IMG SRC="https://img.shields.io/github/stars/marcus67/little_brother_taskbar.svg?label=stars"></A> 
<A HREF="https://github.com/marcus67/little_brother_taskbar/watchers">
<IMG SRC="https://img.shields.io/github/watchers/marcus67/little_brother_taskbar.svg?label=watchers"></A> 
<A HREF="https://github.com/marcus67/little_brother_taskbar/issues">
<IMG SRC="https://img.shields.io/github/issues/marcus67/little_brother_taskbar.svg"></A> 
<A HREF="https://github.com/marcus67/little_brother_taskbar/pulls">
<IMG SRC="https://img.shields.io/github/issues-pr/marcus67/little_brother_taskbar.svg"></A>

## Continuous Integration Status Overview

| Status              | Master                                                                                                                                                                                                                                                                                                                                                                               | Release                                                                                                                                                                                                 |
|:------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CircleCI            | <A HREF="https://circleci.com/gh/marcus67/little_brother_taskbar/tree/master"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/little_brother_taskbar/master.svg?label=master"></A>                                                                                                                                                                                 | <A HREF="https://circleci.com/gh/marcus67/little_brother_taskbar/tree/release"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/little_brother_taskbar/release.svg?label=release"></A> |
| Test Coverage       | <A HREF="https://codecov.io/gh/marcus67/little_brother_taskbar/branch/master"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/little_brother_taskbar.svg?label=master"></A>                                                                                                                                                                                               | <A HREF="https://codecov.io/gh/marcus67/little_brother_taskbar/branch/release"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/little_brother_taskbar/release.svg?label=release"></A>        |
| Snyk Vulnerability  | <a href="https://snyk.io/test/github/marcus67/little_brother_taskbar?targetFile=requirements.txt"><img src="https://snyk.io/test/github/marcus67/little_brother_taskbar/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/marcus67/little_brother_taskbar?targetFile=requirements.txt" style="max-width:100%;"></a> | not available                                                                                                                                                                                           |
| Codacy Code Quality | <a href="https://www.codacy.com/app/marcus67/little_brother_taskbar?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcus67/little_brother_taskbar&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/f1fc3b113b95438189da9032ecf03b34"/></a>                                                                                         | not available                                                                                                                                                                                           |

Note: The vulnerability status is derived from the Python PIP packages found in `requirements.txt`.

## Features

`LittleBrotherTaskbar` has the following features:

*   Shows the status of a user monitored by [LittleBrother](https://github.com/marcus67/little_brother)
*   More to come

## Prerequisites

`LittleBrotherTask` requires an active installation of [LittleBrother](https://github.com/marcus67/little_brother).
The taskbar client will contact the master process of `LittleBrother`.   


## Tested Distributions

| Distribution | Version       | Comments                                                               | Most Recent Test |
| ------------ | ------------- | ---------------------------------------------------------------------- | ---------------- |
| Debian       | testing       |                                                                        | 02.APR.2020      |

## Quick Install (Debian Package)

This guide will take you through the steps required to install, configure, and run the `LittleBrotherTaskbar` 
application on your system. 

### Install the Software

`LittleBrotherTaskbar` will be available as a [PIP package](https://pypi.org/project/little-brother-taskbar/).

### Configure the Software

In its simplest setting the tool just needs to be started with the URL of the LittleBrother master API, e.g.

    run_little_brother_taskbar --server-url=http://[HOSTNAME]:[PORT]
    
with `[HOSTNAME]` being the host where the LittleBrother master process is running and `[PORT ]` being its port.

## Extended Command Line Configuration

The tool recognizes the following extra options:

*   `--username [NAME]`: Set the username to `[NAME]`. If the option is not given the tool will try to derive the
     login name from the environment variable `USER`. If no user can be found, the tool will fail.

*   `--locale [LOCALE]`: Set the locale to `[LOCALE]`, e.g. `en_US`. 

*   `--config [FILENAME]`: Read the configuration file `[FILENAME]`. If this option is not given the tool
     will try to read the file `~/.config/LittleBrotherTaskbar.conf`. 
     See [this file](https://github.com/marcus67/little_brother_taskbar/blob/master/etc/LittleBrotherTaskbar.conf) 
     for an example.
 
*   `--loglevel [LEVEL]`: Set the log level to `DEBUG`, `INFO`, `WARNING`, or `ERROR`.  
  
### Troubleshooting

So, you went through all of the above but `LittleBrotherTaskbar` does not seem to work? Maybe this 
[troubleshooting page](https://github.com/marcus67/little_brother_taskbar/blob/master/TROUBLESHOOTING.md) can help you.

## Caveats

The application `LittleBrotherTaskbar` is far from perfect. Issues are listed on GitHub 
(see [here](https://github.com/marcus67/little_brother_taskbar/issues)). Feel free to open new issues if you have 
any trouble with installing and/or running the application.

## Internationalization

The application uses the PIP package `Flask-Babel` to provide internationalization for the web frontend, Currently, 
the following languages are supported/prepared:

| Language | Locale | Status    | Translation provided by |
| -------- | ------ | --------- | ------------------------|
| English  | en     | Available |  Marcus Rickert         |
| German   | de     | Available |  Marcus Rickert         |
| Italian  | it     | Prepared  |  N.N.                   |
| French   | fr     | Prepared  |  N.N.                   |

Your help with translations is greatly appreciated. Please, contact the author if you are interested in providing
a translation. You do not necessarily have to clone this repository or be familiar with Python to do so.
