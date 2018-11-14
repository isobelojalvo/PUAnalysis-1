#!/bin/sh

#nohup bash ./merge.sh >merge.log & 
#to see if finished running check 'top' and tail below
#tail -f merge.log

mkdir /scratch/$USER/ztt_unweighted_Nov13
cd /scratch/$USER/ztt_unweighted_Nov13
jobID='2018_Nov13_data_tau'

user=ojalvo
mergedata=0;
mergemc=0;
mergeW=1;
mergeZ=1;
mergehiggs=0;

if [ $mergedata -eq 1 ]
    then
    hadd -f tauDATA-B.root 	/hdfs/store/user/$user/${jobID}_B_tautau-SUB_Data/* &
    hadd -f tauDATA-C.root 	/hdfs/store/user/$user/${jobID}_C_tautau-SUB_Data/* &
    hadd -f tauDATA-D.root 	/hdfs/store/user/$user/${jobID}_D_tautau-SUB_Data/* &
    hadd -f tauDATA-E.root 	/hdfs/store/user/$user/${jobID}_E_tautau-SUB_Data/* &
    hadd -f tauDATA-F.root 	/hdfs/store/user/$user/${jobID}_F_tautau-SUB_Data/* &
    wait;
    hadd -f tauDATA.root tauDATA-B.root tauDATA-C.root tauDATA-D.root tauDATA-E.root tauDATA-F.root
fi

jobID='2018_Nov12_tautau'
#2018_Oct_2017MC_ggH_ggHtautau_125-SUB/
if [ $mergehiggs -eq 1 ]
    then #ggHtautau_125
    #hadd -f  ggH110.root /hdfs/store/user/$user/${jobID}_ggHtautau_110-SUB-TT/* &
    #hadd -f  ggH120.root /hdfs/store/user/$user/${jobID}_ggHtautau_120-SUB-TT/* &
    hadd -f  ggH125.root /hdfs/store/user/$user/${jobID}_ggH125_ext-SUB_MC/* &
    #hadd -f  ggH130.root /hdfs/store/user/$user/${jobID}_ggHtautau_130-SUB-TT/* &
    #hadd -f  ggH140.root /hdfs/store/user/$user/${jobID}_ggHtautau_140-SUB-TT/* &

    #hadd -f  vbfH120.root /hdfs/store/user/$user/${jobID}_vbfHtautau_110-SUB-TT/* &
    #hadd -f  vbfH120.root /hdfs/store/user/$user/${jobID}_vbfHtautau_120-SUB-TT/* &
    hadd -f  vbfH125.root /hdfs/store/user/$user/${jobID}_vbfH125-SUB_MC/* &
    #hadd -f  vbfH130.root /hdfs/store/user/$user/${jobID}_vbfHtautau_130-SUB-TT/* &
    #hadd -f  vbfH130.root /hdfs/store/user/$user/${jobID}_vbfHtautau_140-SUB-TT/* &

    #hadd -f  WpH120.root /hdfs/store/user/$user/${jobID}_WpHtautau_120-SUB-TT/* &
    hadd -f  WpH125.root /hdfs/store/user/$user/${jobID}_WHplus-SUB_MC/* &
    #hadd -f  WpH130.root /hdfs/store/user/$user/${jobID}_WpHtautau_130-SUB-TT/* &

    #hadd -f  WmH120.root /hdfs/store/user/$user/${jobID}_WmHtautau_120-SUB-TT/* &
    hadd -f  WmH125.root /hdfs/store/user/$user/${jobID}_WHminus-SUB_MC/* &
    #hadd -f  WmH130.root /hdfs/store/user/$user/${jobID}_WmHtautau_130-SUB-TT/* &

    #hadd -f  ZH120.root /hdfs/store/user/$user/${jobID}_ZHtautau_120-SUB-TT/* &
    hadd -f  ZH125.root /hdfs/store/user/$user/${jobID}_ZH-SUB_MC/* &
    #hadd -f  ZH130.root /hdfs/store/user/$user/${jobID}_ZHtautau_130-SUB-TT/* &

    #hadd -f  ttH120.root /hdfs/store/user/$user/${jobID}_ttHtautau_120-SUB-TT/* &
    hadd -f  ttH125.root /hdfs/store/user/$user/${jobID}_ttH-SUB_MC/* &
    #hadd -f  ttH130.root /hdfs/store/user/$user/${jobID}_ttHtautau_130-SUB-TT/* &
    wait;
fi 

if [ $mergeW -eq 1 ]
    then
    hadd -f  W1Jets.root /hdfs/store/user/$user/${jobID}i_W1J_lnu-SUB_MC/* & 
    hadd -f  W2Jets.root /hdfs/store/user/$user/${jobID}_W2J_lnu-SUB_MC/* & 
    hadd -f  W3Jets.root /hdfs/store/user/$user/${jobID}_W3J_lnu-SUB_MC/* & 
    hadd -f  W4Jets.root /hdfs/store/user/$user/${jobID}_W4J_lnu-SUB_MC/* & 
    hadd -f  WJets.root /hdfs/store/user/$user/${jobID}_WJ_lnu*-SUB_MC/* & 
    wait;
fi 

if [ $mergeZ -eq 1 ]
    then
    ##merge nominal and extension at the same time
    hadd -f  ZJets.root  /hdfs/store/user/$user/${jobID}_DYJ*-SUB_MC/* & 
    hadd -f  Z1Jets.root /hdfs/store/user/$user/${jobID}_DY1*-SUB_MC/* & 
    hadd -f  Z2Jets.root /hdfs/store/user/$user/${jobID}_DY2*-SUB_MC/* & 
    hadd -f  Z3Jets.root /hdfs/store/user/$user/${jobID}_DY3*-SUB_MC/* & 
    hadd -f  Z4Jets.root /hdfs/store/user/$user/${jobID}_DY4-SUB_MC/* & 
    wait;
fi 

if [ $mergemc -eq 1 ]
    then

   #uncomment below for SM Backgorund sample 2016_Sep23_TT-SUB-TT
    hadd -f   TT_had.root 	/hdfs/store/user/$user/${jobID}_TT_had-SUB_MC/*  
    hadd -f   TT_SL.root 	/hdfs/store/user/$user/${jobID}_TT_sl-SUB_MC/*  
    hadd -f   TT_DL.root 	/hdfs/store/user/$user/${jobID}_TT_2l2nu-SUB_MC/*  

    hadd -f   WZTo1L3Nu.root    /hdfs/store/user/$user/${jobID}_WZ_1l3nu-SUB_MC/* & 
    hadd -f   WZTo1L1Nu2Q.root  /hdfs/store/user/$user/${jobID}_WZ_lnu2q-SUB_MC/* & 
    hadd -f   WZTo2L2Q.root     /hdfs/store/user/$user/${jobID}_WZ_2l2q-SUB_MC/* & 
    hadd -f   WZTo3L1Nu.root    /hdfs/store/user/$user/${jobID}_WZ_3lnu-SUB_MC/* & 

    hadd -f   tBar_tW.root 	/hdfs/store/user/$user/${jobID}_ST_tw_at-SUB_MC/* &
    hadd -f   t_tW.root 	/hdfs/store/user/$user/${jobID}_ST_tW_t-SUB_MC/* & 
    hadd -f   St_tBar.root 	/hdfs/store/user/$user/${jobID}_ST_t_at-SUB_MC/* &
    hadd -f   St_t.root 	/hdfs/store/user/$user/${jobID}_ST_t_t-SUB_MC/* & 

    hadd -f   WWTo1L1Nu2Q.root  /hdfs/store/user/$user/${jobID}_WW_lnu2q*-SUB_MC/* & 
    hadd -f   WWTo4Q.root       /hdfs/store/user/$user/${jobID}_WW_4q-SUB_MC/* & 
    hadd -f   WWTo2L2Nu.root    /hdfs/store/user/$user/${jobID}_WW_2l2nu-SUB_MC/* & 

    hadd -f   ZZTo2L2Q.root     /hdfs/store/user/$user/${jobID}_ZZ_2l2q-SUB_MC/* & 
    hadd -f   ZZTo2L2Nu.root    /hdfs/store/user/$user/${jobID}_ZZ_2l2nu-SUB_MC/* & 
    hadd -f   ZZTo4L.root       /hdfs/store/user/$user/${jobID}_ZZ_4l*-SUB_MC/* & 

    hadd -f   EWKWp2j.root      /hdfs/store/user/$user/${jobID}_EWKWPlus2j-SUB_MC/* &
    hadd -f   EWKWm2j.root      /hdfs/store/user/$user/${jobID}_EWKWminus2j-SUB_MC/* &
    hadd -f   EWKZ2l.root       /hdfs/store/user/$user/${jobID}_EWKZ2j_2l-SUB_MC/* &
    hadd -f   EWKZ2Nu.root      /hdfs/store/user/$user/${jobID}_EWKZ2j_2nu-SUB_MC* &

    wait;
    #hadd     	--reuse-cache-files ZJets1050.root	/hdfs/store/user/$user/${jobID}_ZJets1050-SUB-MC 
    #hadd 	--reuse-cache-files WWTo2L2Nu.root 	/hdfs/store/user/$user/${jobID}_WWTo2L2Nu-SUB-MC 
    #hadd 	--reuse-cache-files WWTo4Q.root 	/hdfs/store/user/$user/${jobID}_WWTo4Q-SUB-MC 
    #hadd 	--reuse-cache-files WWToLNuQQ.root 	/hdfs/store/user/$user/${jobID}_WWToLNuQQ-SUB-MC 
    #hadd 	--reuse-cache-files ZZTo2L2Q.root 	/hdfs/store/user/$user/${jobID}_ZZTo2L2Q-SUB-MC 
    #hadd 	--reuse-cache-files ZZTo4Q.root 	/hdfs/store/user/$user/${jobID}_ZZTo4Q-SUB-MC 
    #hadd 	--reuse-cache-files TT.root 	        /hdfs/store/user/$user/${jobID}_TT-SUB-MC  
    #hadd 	--reuse-cache-files WJetsMLM.root 	/hdfs/store/user/$user/${jobID}_WJetsMLM-SUB-MC 
    #hadd 	--reuse-cache-files t_s.root 	        /hdfs/store/user/$user/${jobID}_t_s-SUB-MC 
    #hadd 	--reuse-cache-files t_s_Ext.root 	/hdfs/store/user/$user/${jobID}_t_Ext-SUB-MC 
    #hadd -f   VVTo2L2Nu.root       /hdfs/store/user/$user/${jobID}_VVTo2L2Nu*/* & 
    #hadd -f   WWW.root          /hdfs/store/user/$user/${jobID}_WWW-SUB-TT/* &
    #hadd -f   ZZZ.root          /hdfs/store/user/$user/${jobID}_ZZZ-SUB-TT/* &

fi

