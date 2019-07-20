# pylightning-qt
*groestlcoin-qt for C-Lightning, as simple as : `lightning-cli gui`*

## What is it ?
lightning-qt is a Python plugin for [C-lightning](https://github.com/groestlcoin/lightning), a [Lightning Network](https://github.com/groestlcoin/groestlcoin/tree/master/src/qt) daemon. It enables the use of a [groestlcoin-qt](https://github.com/groestlcoin/groestlcoin/tree/master/src/qt)-like Graphical User Interface (actually, part of the icons and forms have been taken from groestlcoin-qt and modified) via the RPC interface.  

## Why ?
Currently lightning does not have a GUI, and I think that having one which looks like groestlcoin-qt is great for people coming from [groestlcoin-core](https://github.com/groestlcoin/groestlcoin), which most of the C-Lightning users do (or have at least ever used groestlcoin-qt). Having it directly available from the RPC is also quite convenient.  

## How to install it ?
For more informations about plugins and their installations you can checkout the [lightningd/plugins](https://github.com/lightningd/plugins) repository (which has a great list of plugins too). For a quick solution :  
```shell
git clone https://github.com/groestlcoin/pylightning-qt && cd pylightning-qt
pip3 install -r requirements.txt
chmod a+x lightning-qt.py
# And just start lightningd like
lightningd --plugin=lightning-qt.py
```

## How to use it ?
Just launch `lightning-cli gui` :D.  
You can now also use lightning-qt in standalone mode. It will connect to a socket which path can be given as a command line option (and defaults to $HOME/.lightning/lightning-rpc) : this can be useful to use lightning-qt as a remote control for your lightning node hosted on another computer, you could for example share a socket through ssh and start lightning-qt listening on this socket i.e.  
```bash
python3 lightning-qt --socket-path /path/to/unixdomain/socket
```


## Contributing
Any contribution (issue, PR) is welcome.
We use [forms](forms/)(ui files) to design pages : these are handled by PyQt5 with the `pyuic5` command line tool (installed with `pip install PyQt5`). If you modify a ui file (you may want to use [QDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html)), you can regenerate the Python code like :
```shell
pyuic5 forms/channelspage.ui -o forms/ui_channelsPage.py
```
Images are handled in the [qrc](gui.qrc) file : if you modify this resource file (for instance to add an image/icon), you can regenerate the Python code with :
```shell
pyrcc5 gui.qrc -o resources.py
```
Also, if you help me on this project you may want to use the very handy [auto-reload plugin](https://github.com/lightningd/plugins/tree/master/autoreload). Please also note that PyQt5 has *__a very bad__* way to handle exception in slots : in short you cannot `except` a raised exception in a [slot](https://doc.qt.io/qt-5/signalsandslots.html), so be carefull and happy debuging ;).  

## Licence
BSD 3-clauses clear
