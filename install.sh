#!/bin/sh

sudo pacman -S tk --needed --noconfirm || sudo apt install python-tk -y || echo "Warning: Couldn't install tkinter. Manual installation required!"
mkdir $HOME/.tkinter_saqib
cp ./*.py $HOME/.tkinter_saqib

echo "installing calculator"

cat <<EOT >> $HOME/.local/share/applications/calculator.desktop
[Desktop Entry]
Version=1.0
Exec=/home/$USER/.tkinter_saqib/calculator.py
#Icon=/path/to/icon
Name=Calculator
Type=Application
EOT

echo "installing text editor"
cat <<EOT >> $HOME/.local/share/applications/text_editor.desktop
[Desktop Entry]
Version=1.0
Exec=/home/$USER/.tkinter_saqib/text_editor.py
#Icon=/path/to/icon
Name=Text Editor
Type=Application
EOT

echo "installing system info"
cat <<EOT >> $HOME/.local/share/applications/system_info.desktop
[Desktop Entry]
Version=1.0
Exec=/home/$USER/.tkinter_saqib/system_info.py
#Icon=/path/to/icon
Name=System Info
Type=Application
EOT

echo "Installation Finished"
