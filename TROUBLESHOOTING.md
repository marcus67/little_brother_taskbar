![LittleBrotherTaskbar-Logo](https://raw.githubusercontent.com/marcus67/little_brother_taskbar/master/little_brother_taskbar/static/icons/little-brother-taskbar-logo_128x128.png)

# Troubleshooting `LittleBrotherTaskbar`

This page tries to help you with troubleshooting the most common problems with running `LittleBrotherTaskbar`. 

## Trouble finding the GTK development files

If you run into any complaints about not being able to find GTK components, make sure you have the following packages
installed

*   `libgtk-3-dev` 
*   `libpulse-dev`

On a Debian based system issue

    apt-get install libgtk-3-dev libpulse-dev
    
and then try to re-install `LittleBrotherTaskbar`.

## Trouble finding the library `libwx_baseu-3.0.so` 

Unfortunately, there seems to be some incompatibility between some versions of the Python `setuptools` and the
way that `wxPython` builds its libraries. In this case the following error will occur when installing the `wxPython`
PIP package:

    copying symlink wx/libwx_baseu-3.0.so -> build/lib.linux-x86_64-3.5/wx/libwx_baseu-3.0.so
    error: [Errno 2] No such file or directory: 'build/lib.linux-x86_64-3.5/wx/libwx_baseu-3.0.so'

One way to tackle this is to explicitly downgrade the `setuptools` package. In the current CI setup, using version
`51.1.2` worked successfully:

    pip install setuptools==51.1.2
    
After that try to re-install the `LittleBrotherTaskbar`.
