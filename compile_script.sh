#!/bin/bash
gcc ".temp.c"  &> ".compile.log"
if [ $? -ne 0 ] 
then
sed -i "s/‘/\"/g" ".compile.log"
sed -i "s/’/\"/g" ".compile.log"
else
echo "compilation successful" > .compile.log
fi
