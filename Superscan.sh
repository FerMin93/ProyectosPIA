#!/bin/bash
#Script Superscan.sh
#07/03/2023 - Fer Barron
#
#Ejemplos de Menu en BASH
#
date
	echo ""
	echo "|-------------------------|"
	echo "|     Menu Principal      |"
	echo "|-------------------------|"
	echo "|1. Net Discover          |"
	echo "|2. Port scan             |"
	echo "|3. Welcome               |"
	echo "|4. Exit                  |"
	echo ""
read -p "Opcion [ 1 - 4 ] : " c
case $c in 
	1) $HOME/Escritorio/netdiscover.sh;;
	2) $HOME/Escritorio/portscanv1.sh;;
	3) $HOME/Escritorio/welcome.sh;;
	4) echo "Adios!"; exit 0;;
esac
