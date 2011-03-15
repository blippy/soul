fname=~/soul-`date +%Y%m%d`.tar
rm $fname.gz
tar cvf $fname ~/soul
gzip $fname
