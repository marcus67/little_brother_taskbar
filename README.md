![LittleBrotherTaskbar-Logo](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/little_brother_taskbar/static/icons/little-brother-taskbar-logo_128x128.png)

# Taskbar Tray Application for `LittleBrother`

## Overview

`LittleBrotherTaskbar` is a simple application which can be installed into the tray of the window manager
to display the remaining play time of the current user.

## Contact

The taskbar does not have a homepage of its own. It is sharing `LittleBrother`'s homepage. Visit the project 
at [Facebook](https://www.facebook.com/littlebrotherdebian) or write comments to little-brother(at)web.de.

## Screenshots

The following screenshots show the display of `LittleBrotherTaskbar`.  

![Screenshot Status](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot_status_ok.png) 
![Screenshot Status](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot_status_warning.png) 

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
The taskbar client will contact the master process of `LittleBrother`. Also, some Linux packages have to be
installed to enable the compilation of the Python PIP package `wxPython`. See the installation instructions below.

In case you want to use the MP3 speech generation for notification messages you have to install the PIP package
[python-google-speak](https://pypi.org/project/python-google-speak/).

## Tested Distributions

| Distribution | Version       | Comments                                                               | Most Recent Test |
| ------------ | ------------- | ---------------------------------------------------------------------- | ---------------- |
| Debian       | testing       |                                                                        | 02.APR.2020      |

## Quick Install

This guide will take you through the steps required to install, configure, and run the `LittleBrotherTaskbar` 
application on your system. 

### Install the Software

`LittleBrotherTaskbar` is available as a Python3 [PIP package](https://pypi.org/project/little-brother-taskbar/). Make sure
you have the Debian packages

*   `libgtk-3-dev` 
*   `libpulse-dev`

installed on your system. Also, the required library `wxPython` cannot be compiled successfully with version of the
`setuptools`. Version `40.8.0` seems to work fine. Issue 

    pip install setuptools==40.8.0

to install exactly this version. Then type

    pip3 install little-brother-taskbar

to install the latest version of the taskbar. If you want to install a specific version use

    pip3 install little-brother-taskbar==[VERSION]

instead with `[VERSION]` replaced by the specific version.

**Note**: Compiling the `wxPython` library takes a LONG time. Depending on the speed of your system, compilation
times of up to 15 minutes are not unusual. So, please, be patient!

### Speech Generation and Output  

In order to use the speech generation for notification messages, issue the command

    pip3 install python-google-speak 

and use the `--speech-engine` command line option (see below). Also, install the Debian package `mpg123`:

    apt-get install mpg123

### Configure the Software

In its simplest setting the tool just needs to be started with the URL of the LittleBrother master API, e.g.

    run_little_brother_taskbar --server-url=http://[HOSTNAME]:[PORT]
    
with `[HOSTNAME]` being the host where the LittleBrother master process is running and `[PORT]` being its port.

## Extended Command Line Configuration

The tool recognizes the following extra options:

*   `--username [NAME]`: Set the username to `[NAME]`. If the option is not given the tool will try to derive the
     login name from the environment variable `USER`. If no user can be found, the tool will fail.

*   `--locale [LOCALE]`: Set the locale to `[LOCALE]`, e.g. `en_US`. Note that this locale is only used until the
     taskbar receives the first status from the LittleBrother master since status contains the locale configured for
     the user. 

*   `--config [FILENAME]`: Read the configuration file `[FILENAME]`. If this option is not given the tool
     will try to read the file `~/.config/LittleBrotherTaskbar.conf`. 
     See [this file](https://github.com/marcus67/little_brother_taskbar/blob/master/etc/LittleBrotherTaskbar.conf) 
     for an example.

*   `--loglevel [LEVEL]`: Set the log level to `DEBUG`, `INFO`, `WARNING`, or `ERROR`.

*   `--speech-engine [ENGINE]`: Activate and select the speech engine to speak messages for the monitored user.
    Possible values for `[ENGINE]` are: `google` 
    (preferred; which requires PIP package [python-google-speak](https://pypi.org/project/python-google-speak/)) or 
    `external` (which requires the Debian package [festival](https://packages.debian.org/stretch/festival) and 
    possibly some more configuration)

## Installing LittleBrotherTaskbar as a StartUp Application

Once you have succeedef starting the tool on the command line (see above) it makes sense to install the tool as
a startup application in your desktop environment. Most environments allow you to configure the applications which 
are automatically started upon logging into the desktop. Below you will find screenshots to guide you through the
installation on a 19.3 Ubuntu system using the Mate Desktop.

*   From the main menu choose the entry `Control Center`. In the upcoming window click on `Startup Applications`.

    ![Startup Applications Step 1](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-startup-applications-1.png)

*   Click on `Add` and enter your statement into the `Command` field. Chose a name and optionally set a comment.

    ![Startup Applications Step 2](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-startup-applications-2.png)
  
*   Click on `Add+` and and on `Close`.

*   Logout out of the desktop and login in again to test. If successful you should see the LittleTaskBar icon in the
    tray.
    
    ![Startup Applications Step 3](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-startup-applications-3.png)
    

### Troubleshooting

So, you went through all of the above but `LittleBrotherTaskbar` does not seem to work? Maybe this 
[troubleshooting page](https://github.com/marcus67/little_brother_taskbar/blob/master/TROUBLESHOOTING.md) can help you.

## Caveats

The application `LittleBrotherTaskbar` is far from perfect. Issues are listed on GitHub 
(see [here](https://github.com/marcus67/little_brother_taskbar/issues)). Feel free to open new issues if you have 
any trouble with installing and/or running the application.

## Internationalization

The application uses the PIP package `Flask-Babel` to provide internationalization for the web frontend, Currently, 
the following languages are supported/prepared (in the order they were made available):

| Flag                                                                                                                                    | Language      | Locale | Status         | Translation provided by |
| ----------------------------------------------------------------------------------------------------------------------------------------| ------------- | ------ | -------------- | ------------------------|
| ![Flag USA](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/united-states-of-america-flag-icon-32.png)     | English       | en     | Available      |  Marcus Rickert         |
| ![Flag Germany](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/germany-flag-icon-32.png)                  | German        | de     | Available      |  Marcus Rickert         |
| ![Flag Italy](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/italy-flag-icon-32.png)                      | Italian       | it     | Available      |  Albano Battistella     |
| ![Flag Netherlands](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/netherlands-flag-icon-32.png)          | Dutch         | nl     | Available      |  Simone & Lex           |
| ![Flag Finland](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/finland-flag-icon-32.png)                  | Finnish       | fi     | Available      |  Iisakki Kosonen        |
| ![Flag Turkey](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/turkey-flag-icon-32.png)                    | Turkish       | tr     | Available      |  Selay Dogan            |
| ![Flag Russia](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/russia-flag-icon-32.png)                    | Russian       | ru     | Available      |  J. Moldawski           |
| ![Flag Japan](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/japan-flag-icon-32.png)                      | Japanese      | ja     | Available      |  Arik M.                |
| ![Flag Bangladesh](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/bangladesh-flag-icon-32.png)            | Bangla        | bn     | Available      |  Rownak Jyoti Zaman     |
| ![Flag France](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/france-flag-icon-32.png)                    | French        | fr     | Available      |  Albano Battistella     |
| ![Flag Thailand](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/thailand-flag-icon-32.png)                | Thai          | th     | Available      |  Busaba Kramer          |
| ![Flag Spain](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/spain-flag-icon-32.png)                      | Spanish       | es     | In preparation |  N.N.                   |
| ![Flag Lithuania](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/lithuania-flag-icon-32.png)              | Lithuanian    | lt     | In preparation |  N.N.                   |
| ![Flag Croatia](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/croatia-flag-icon-32.png)                  | Croatian      | hr     | In preparation |  N.N.                   |

Note that the spoken messages are provided by the `LittleBrother` master process. Check 
[here](https://github.com/marcus67/little_brother) for the availability of desired foreign language. 
 
### Sample Screenshots

![Screenshot Status in Italian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot_status_ok_italian.png) 
![Screenshot Status in Finnish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-finnish.png) 
![Screenshot Status in Turkish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-turkish.png) 
![Screenshot Status in Russian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-russian.png) 
![Screenshot Status in Japanese](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-japanese.png) 
![Screenshot Status in Bangla](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-bangla.png) 
![Screenshot Status in French](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-french.png) 
![Screenshot Status in Thai](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/screenshot-status-ok-thai.png) 

### Sample Speech Audio Files

*   [Sample 1 in Dutch](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-nl-1.mp3)
*   [Sample 2 in Dutch](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-nl-2.mp3)
*   [Sample 1 in Italian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-it-1.mp3)
*   [Sample 2 in Italian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-it-2.mp3)
*   [Sample 1 in Finnish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-fi-1.mp3)
*   [Sample 2 in Finnish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-fi-2.mp3)
*   [Sample 1 in Turkish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-tr-1.mp3)
*   [Sample 2 in Turkish](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-tr-2.mp3)
*   [Sample 1 in Russian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-ru-1.mp3)
*   [Sample 2 in Russian](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-ru-2.mp3)
*   [Sample 1 in Japanese](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-ja-1.mp3)
*   [Sample 2 in Japanese](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-ja-2.mp3)
*   [Sample 1 in Bangla](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-bn-1.mp3)
*   [Sample 2 in Bangla](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-bn-2.mp3)
*   [Sample 1 in French](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-fr-1.mp3)
*   [Sample 2 in French](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-fr-2.mp3)
*   [Sample 1 in Thai](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-th-1.mp3)
*   [Sample 2 in Thai](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/doc/speech-sample-th-2.mp3)

Your help with translations is greatly appreciated. Please, contact the author if you are interested in providing
a translation. You do not necessarily have to clone this repository or be familiar with Python to do so.

## Credits

*   Thanks to all the people maintaining the wonderful script language [Python](https://www.python.org/) 
and the libraries on [PyPi](https://pypi.org/).
 
*   The country flags were taken from [www.countryflags.com](https://www.countryflags.com/).

*   See the section about on internalization for credits regarding the translations.

*   The site [www.mehr-schulferien.de](https://www.mehr-schulferien.de) maintains the vacation metadata for
Germany.
