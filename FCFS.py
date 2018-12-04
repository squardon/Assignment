{\rtf1\ansi\ansicpg1252\cocoartf1671
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;\f1\fmodern\fcharset0 CourierNewPS-BoldMT;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red10\green82\blue135;
\red251\green0\blue129;\red0\green0\blue255;\red18\green139\blue2;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c40000\c60000;
\cssrgb\c100000\c7843\c57647;\cssrgb\c0\c0\c100000;\cssrgb\c0\c60000\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl330\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 bt
\f1\b \cf4 \strokec4 =
\f0\b0 \cf2 \strokec2 []\
\pard\pardeftab720\sl330\partightenfactor0
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "Enter the number of process: "\cf2 \strokec2 )\
n
\f1\b \cf4 \strokec4 =
\f0\b0 \cf5 \strokec5 int\cf2 \strokec2 (\cf5 \strokec5 input\cf2 \strokec2 ())\
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "Enter the burst time of the processes: \\n"\cf2 \strokec2 )\
bt
\f1\b \cf4 \strokec4 =
\f0\b0 \cf5 \strokec5 list\cf2 \strokec2 (\cf5 \strokec5 map\cf2 \strokec2 (\cf5 \strokec5 int\cf2 \strokec2 , \cf5 \strokec5 raw_input\cf2 \strokec2 ().split()))\
wt
\f1\b \cf4 \strokec4 =
\f0\b0 \cf2 \strokec2 []\
avgwt
\f1\b \cf4 \strokec4 =
\f0\b0 \cf7 \strokec7 0\cf2 \strokec2 \
tat
\f1\b \cf4 \strokec4 =
\f0\b0 \cf2 \strokec2 []\
avgtat
\f1\b \cf4 \strokec4 =
\f0\b0 \cf7 \strokec7 0\cf2 \strokec2 \
wt.insert(\cf7 \strokec7 0\cf2 \strokec2 ,\cf7 \strokec7 0\cf2 \strokec2 )\
tat.insert(\cf7 \strokec7 0\cf2 \strokec2 ,bt[\cf7 \strokec7 0\cf2 \strokec2 ])\
\pard\pardeftab720\sl330\partightenfactor0

\f1\b \cf4 \strokec4 for
\f0\b0 \cf2 \strokec2  i 
\f1\b \cf4 \strokec4 in
\f0\b0 \cf2 \strokec2  \cf5 \strokec5 range\cf2 \strokec2 (\cf7 \strokec7 1\cf2 \strokec2 ,\cf5 \strokec5 len\cf2 \strokec2 (bt)):\
\'a0wt.insert(i,wt[i
\f1\b \cf4 \strokec4 -
\f0\b0 \cf7 \strokec7 1\cf2 \strokec2 ]
\f1\b \cf4 \strokec4 +
\f0\b0 \cf2 \strokec2 bt[i
\f1\b \cf4 \strokec4 -
\f0\b0 \cf7 \strokec7 1\cf2 \strokec2 ])\
\'a0tat.insert(i,wt[i]
\f1\b \cf4 \strokec4 +
\f0\b0 \cf2 \strokec2 bt[i])\
\'a0avgwt
\f1\b \cf4 \strokec4 +=
\f0\b0 \cf2 \strokec2 wt[i]\
\'a0avgtat
\f1\b \cf4 \strokec4 +=
\f0\b0 \cf2 \strokec2 tat[i]\
avgwt
\f1\b \cf4 \strokec4 =
\f0\b0 \cf5 \strokec5 float\cf2 \strokec2 (avgwt)
\f1\b \cf4 \strokec4 /
\f0\b0 \cf2 \strokec2 n\
avgtat
\f1\b \cf4 \strokec4 =
\f0\b0 \cf5 \strokec5 float\cf2 \strokec2 (avgtat)
\f1\b \cf4 \strokec4 /
\f0\b0 \cf2 \strokec2 n\
\pard\pardeftab720\sl330\partightenfactor0
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "\\n"\cf2 \strokec2 )\
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "Process\\t\'a0 Burst Time\\t\'a0 Waiting Time\\t\'a0 Turn Around Time"\cf2 \strokec2 )\
\pard\pardeftab720\sl330\partightenfactor0

\f1\b \cf4 \strokec4 for
\f0\b0 \cf2 \strokec2  i 
\f1\b \cf4 \strokec4 in
\f0\b0 \cf2 \strokec2  \cf5 \strokec5 range\cf2 \strokec2 (\cf7 \strokec7 0\cf2 \strokec2 ,n):\
\'a0\cf5 \strokec5 print\cf2 \strokec2 (\cf5 \strokec5 str\cf2 \strokec2 (i)
\f1\b \cf4 \strokec4 +
\f0\b0 \cf6 \strokec6 "\\t\\t"
\f1\b \cf4 \strokec4 +
\f0\b0 \cf5 \strokec5 str\cf2 \strokec2 (bt[i])
\f1\b \cf4 \strokec4 +
\f0\b0 \cf6 \strokec6 "\\t\\t"
\f1\b \cf4 \strokec4 +
\f0\b0 \cf5 \strokec5 str\cf2 \strokec2 (wt[i])
\f1\b \cf4 \strokec4 +
\f0\b0 \cf6 \strokec6 "\\t\\t"
\f1\b \cf4 \strokec4 +
\f0\b0 \cf5 \strokec5 str\cf2 \strokec2 (tat[i]))\
\'a0\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "\\n"\cf2 \strokec2 )\
\pard\pardeftab720\sl330\partightenfactor0
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "Average Waiting time is: "
\f1\b \cf4 \strokec4 +
\f0\b0 \cf5 \strokec5 str\cf2 \strokec2 (avgwt))\
\cf5 \strokec5 print\cf2 \strokec2 (\cf6 \strokec6 "Average Turn Arount Time is: "
\f1\b \cf4 \strokec4 +
\f0\b0 \cf5 \strokec5 str\cf2 \strokec2 (avgtat))\
}