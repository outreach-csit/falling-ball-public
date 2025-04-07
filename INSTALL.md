# Install

This provides installation instructions for the software requirements for Windows and Mac.

In a nutshell, we need to have the following installed:

* [Python](https://www.python.org/) 3.10+: the programming language to be used.
* [pygame](https://www.pygame.org/wiki/about) library: a toolkit to write games.
* [VSCode](https://code.visualstudio.com/): the IDE (Integrated Development Environment) where will code, basically a tool to write code in a nice way! 😉

## Windows Instructions

Windows installation instructions for

1. [Download VSCode from for Windows][1] from the website.
2. Follow the installer and use all default options.
3. Open VSCode.
4. Open a terminal (Menu Terminal -> New Terminal, or `Control+J`).
5. Type `python` and hit `Enter`. Windows will not find it, but will pop up a window in the Microsoft Store to get it. Hit the button `Get` to install Python in your machine.
6. Once installed, go back to the terminal in VSCode and type `python --version`. It should now say the version of Python installed in your machine.
7. Finally, install the `pygame` module by running `pip install pygame`.
   * Pip is a package manager for Python, to install available modules. Pip is installed by default in the windows installer, so it's not required.

> [!WARNING]
>  VSCode may open a pop-up about creating a virtual container. Say 'no' or decline this message.


>[!NOTE]
> The first time that you open a Python file in VSCode, VSCode will recognise that and ask you if you want to install its Python extension. Say YES/ISNTALL to get it installed. This way VSCode gets all the features to develop in Python.

## Mac Instructions

1. [Download Python3 for Mac][2] from the website.
2. Follow the installer and use all default options.
3. [Download VSCode from for Mac][1] from the website.
4. Follow the installer and use all default options.
5. Open VSCode
6. Open a terminal (Menu Terminal -> New Terminal, or `Control+J`)
7. Run the following command to install Pygame module:

    ```shell
    python3 -m pip install -U pygame --user
    ```

> [!NOTE]
> Some newer systems may use `python` rather than `python3`. Also, this setup uses the easiest to setup approach, using available installers. More advanced users may use brew.


[1]: https://code.visualstudio.com/download
[2]: https://www.python.org/downloads/
