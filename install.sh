#!/bin/bash

# Constants
localname="pyso.py"
installPath="/usr/bin/"
filename="sosearch"

print_help(){
    echo "Please make sure the script is ran as root."
    echo $0 + " -i "
    echo "            Will install pyso."
    echo $0 + " -r"
    echo "            Will remove pyso."
    exit
}

install_pyso(){
    cp $localname $installPath$filename
    if [ $? -eq 0 ]; then
        echo Installed.
        echo "You can execute it via "$filename
    else
        echo "Installation Failed!"
    fi
    exit
}

remove_pyso(){
    rm $installPath$filename
    if [ $? -eq 0 ]; then
        echo "Uninstallation successful"
    else
        echo "Removal failed!"
        echo "Try to remove via 'rm /usr/bin/sosearch'."
    fi
    exit
}

# Check if root
if [ "$EUID" -ne 0 ]
  then print_help
fi

# Check for arguments
if [ $# -eq 0 ]; then
    print_help
fi

if [ $1 = "-r" ]; then
    remove_pyso
fi

if [ $1 = "-i" ]; then
    install_pyso
else
    print_help
fi
