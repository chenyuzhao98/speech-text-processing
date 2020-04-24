#!/bin/bash

###############################################################################
# Task f: FPf_run.sh (Section 4.6) (10%)
################
#
# Implement the body of this script:
#	Run "FPa_prepTrans.sh", "FPb_buildDict.py", "FPd_genWhiteNoise.py" and "FPe_genStimuli.py" in this script in sequence.
#
#	Refer to Section 4.6 in "../LING402_FP.pdf" for requirements
#
###############################################################################


### INSERT YOUR CODE BELOW THIS LINE ###

if [ -d "./stimuli" ]
then
    rm -r stimuli
    mkdir stimuli
else
    mkdir stimuli
fi

if [ -d "./etc" ]
then
    rm -r etc
    mkdir etc
else
    mkdir etc
fi

if [ -d "./noise" ]
then
    rm -r noise
    mkdir noise
else
    mkdir noise
fi


echo Running FPa_prepTrans
./FPa_prepTrans.sh trans sentences.txt words.txt
echo Completed FPa_prepTrans and moving on to FPb_buildDict
python3 FPb_buildDict.py ./etc/sentences.txt ./etc/dict.txt
echo Completed FPb_buildDict and moving on to FPd_genWhiteNoise
python3 FPd_genWhiteNoise.py 60 16000 ./noise/wn.wav ./etc/spect_wn.pdf
echo Completed FPd_genWhiteNoise and moving on to FPe_genStimuli
echo This part may take a while please be patient
python3 FPe_genStimuli.py ./wavs/ ./stimuli/ ./resources/wn.wav ./etc/wn_idx.txt
echo Finished running all scripts

