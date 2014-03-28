#!/bin/bash
exec 2> logfile
timeout 1 ./a.out < ".input" > /dev/null
if [ $? -eq 124 ] 
then
echo "TLE" > "logfile"
exit 0
fi
exec 2> logfile
time ./a.out <".input" > ".output"
grep "Segmentation fault" "logfile"
if [ $? -eq 0 ]
then
echo "Segmentation fault" > "logfile"
exit 0
fi
grep "Floating" "logfile"
if [ $? -eq 0 ]
then
echo "Floating point exception" > "logfile"
exit 0
fi
tail "logfile" -c 9 > "logfile1"
rm "logfile"
mv "logfile1" "logfile"
