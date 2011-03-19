#!/usr/bin/env bash

crontab crontab.txt

mkdir $HOME/cache
mkdir $HOME/cache/posts


# website setup
mkdir $HOME/public_html	
function linkhtml { ln -s $HOME/repos/soul/skel/$1 $HOME/public_html/$1 ; }
linkhtml email-mcturra.png
linkhtml index.html
linkhtml feed2js.htm
