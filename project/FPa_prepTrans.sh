#!/bin/bash

###############################################################################
# Task a: FPa_prepTrans.sh (Section 4.1) (25%)
################
#
# Implement the body of this script:
#
#	Parse all the transcription files (trans/*.trans), generate a file "sentences.txt and a file "words.txt"
#
#	Refer to Section 4.1 in "../LING402_FP.pdf" for other requirements
#
###############################################################################


if [ $# -ne 3 ]; then
    echo "Usage: $0 dir_trans file_sentences file_words"
    exit 1
fi



### INSERT YOUR CODE BELOW THIS LINE ###



for file in $1/*
do
    b=$(cat $file)
    d="${b%%|*}"
    file=${file##*/}
    a=${file%.*}
    c="${a}|${d}"
    cd etc/
    echo ${c} >> $2
    cd ..
done


for file in $1/*;
do
    a=$(cat $file | cut -d'|' -f 1 |head -n 1 | tr -cd ' \t' | wc -c)
    for word in $(seq 1 $(($a + 1)))
    do
        echo "$(cat $file | cut -d'|' -f 1 | cut -d ' ' -f $word)|$(cat $file | cut -d'|' -f 2 | tr -s " " | sed -e 's, \,,\,,g' | sed -e 's,\, ,\,,g' | cut -d ',' -f $word)" >> temp
        done
done

sort -u temp >> etc/$3
rm temp
