#! /usr/bin/bash
. $HOME/.bashrc
cd $HOME/soul
alias x=/opt/webstack/bin/python

function activate {
    /opt/webstack/bin/python $1.py 2>$HOME/soul-cache/$1.err
}
	
activate filter
activate summarise
activate email
activate post

activate shtm
activate latest
activate archives
activate feed
