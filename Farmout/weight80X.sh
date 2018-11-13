#!/bin/sh
olddirname='ztt_unweighted_Nov10'
newdirname='ztt_weighted_Nov10'
mkdir /scratch/$USER/$newdirname
cd /scratch/$USER/$newdirname

weight=1;
weightH=0;
weightW=0;
weightZ=0;

#cp /scratch/$USER/$olddirname/tauDATA.root /scratch/$USER/$newdirname/.

if [ $weightH -eq 1 ]
    then

#    for dir in ggH120.root ggH125.root ggH130.root vbfH120.root vbfH125.root vbfH130.root ttH120.root ttH125.root ttH130.root WpH120.root WpH125.root WpH130.root WmH120.root WmH125.root WmH130.root ZH120.root ZH125.root ZH130.root  
    for dir in ggH125.root vbfH125.root ttH125.root WpH125.root WmH125.root ZH125.root
    do 
	cp /scratch/$USER/$olddirname/$dir /scratch/$USER/$newdirname/. &
    done 
    wait;
    echo 'weight higgs'
    #EventWeightsIterativeGen outputFile='ggH120.root'     weight=3.644956       histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='ggH125.root'     weight=3.045965       histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='ggH130.root'     weight=2.451271       histoName='TT/results' sumHistoName='sumweights/genWeights' &
								 	   
    #EventWeightsIterativeGen outputFile='vbfH120.root'    weight=0.274663       histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='vbfH125.root'    weight=0.2371314      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='vbfH130.root'    weight=0.1967617      histoName='TT/results' sumHistoName='sumweights/genWeights' &
								 	   
    #EventWeightsIterativeGen outputFile='WpH120.root'     weight=0.0546185      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='WpH125.root'     weight=0.04304355     histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='WpH130.root'     weight=0.03270345     histoName='TT/results' sumHistoName='sumweights/genWeights' &
								 	   
    #EventWeightsIterativeGen outputFile='WmH120.root'     weight=0.0546185      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='WmH125.root'     weight=0.04304355     histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='WmH130.root'     weight=0.03270345     histoName='TT/results' sumHistoName='sumweights/genWeights' &
								 	   
    #EventWeightsIterativeGen outputFile='ZH120.root'      weight=0.0693812      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='ZH125.root'      weight=0.0554268      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='ZH130.root'      weight=0.042739       histoName='TT/results' sumHistoName='sumweights/genWeights' &
								 	   
    #EventWeightsIterativeGen outputFile='ttH120.root'     weight=0.040128       histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen outputFile='ttH125.root'     weight=0.0320424      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='ttH130.root'     weight=0.024743       histoName='TT/results' sumHistoName='sumweights/genWeights' &
    wait;
fi

if [ $weightZ -eq 1 ]
    then
    for dir in ZJets.root Z1Jets.root Z2Jets.root Z3Jets.root Z4Jets.root
    do 
	cp /scratch/$USER/$olddirname/$dir /scratch/$USER/$newdirname/.
    done 
    #make sure Zpt root file is around!!!
    cp /scratch/ojalvo/zpt_weights_2016.root /scratch/$USER/$newdirname/.
    EventWeightsIterativeZJets    weight=1    histoName='TT/results' 
    hadd -f ZJETS.root ZJets_ext1.root Z1Jets.root Z2Jets.root Z3Jets.root Z4Jets.root
     
fi

if [ $weightW -eq 1 ]
    then
    for dir in WJets.root W1Jets.root W2Jets.root W3Jets.root W4Jets.root
    do 
	cp /scratch/$USER/$olddirname/$dir /scratch/$USER/$newdirname/. &
    done 
    wait;
    #EventWeightsIterativeGen outputFile='WJets.root'      weight=61526.7   histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeWJets    weight=1    histoName='TT/results' 
    #hadd WJETS.root WJetsMLM.root W1Jets.root W2Jets.root W3Jets.root W4Jets.root
    hadd -f WJETS.root WJets.root W1Jets.root W2Jets.root W3Jets.root W4Jets.root
 
fi

if [ $weight -eq 1 ]
    then

#removed from copy list:
#WZTo2L2Q.root
    for dir in TT_DL.root TT_SL.root TT_had.root WZTo1L3Nu.root WZTo1L1Nu2Q.root WZTo2L2Q.root WZTo3L1Nu.root tBar_tW.root t_tW.root St_tBar.root St_t.root WWTo1L1Nu2Q.root WWTo2L2Nu.root WWTo4Q.root ZZTo2L2Q.root ZZTo2L2Nu.root ZZTo4L.root EWKWm2j.root EWKWp2j.root EWKZ2Nu.root EWKZ2l.root 
    do 
	cp /scratch/$USER/$olddirname/$dir /scratch/$USER/$newdirname/.
    done

    #EventWeightsIterativeGen outputFile='TT.root'  weight=831.76     histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight TT'
    EventWeightsIterativeGen  outputFile='TT_DL.root'             weight=88.29      histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen  outputFile='TT_SL.root'             weight=365.35     histoName='TT/results' sumHistoName='sumweights/genWeights' &
    EventWeightsIterativeGen  outputFile='TT_had.root'            weight=377.96     histoName='TT/results' sumHistoName='sumweights/genWeights' &

    echo 'Weight WZ 1L3Nu'
    EventWeightsIterativeGen outputFile='WZTo1L3Nu.root'      weight=3.293   histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight WZ 1L1NuQQ'
    EventWeightsIterativeGen outputFile='WZTo1L1Nu2Q.root'    weight=11.66   histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight WZ 2L2Q'
    EventWeightsIterativeGen outputFile='WZTo2L2Q.root'       weight=6.331   histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight WZ 3L1Nu'
    EventWeightsIterativeGen outputFile='WZTo3L1Nu.root'      weight=5.052   histoName='TT/results' sumHistoName='sumweights/genWeights' &


    echo 'Weight tBar_tW'
    EventWeightsIterativeGen outputFile='tBar_tW.root'      weight=36.0    histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight t_tW'
    EventWeightsIterativeGen outputFile='t_tW.root'         weight=36.0    histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight St_antitop'
    EventWeightsIterativeGen outputFile='St_tBar.root'      weight=80.95    histoName='TT/results' sumHistoName='sumweights/genWeights' & #80.59 pb * 3*.108
    echo 'Weight St_top'
    EventWeightsIterativeGen outputFile='St_t.root'         weight=136.02    histoName='TT/results' sumHistoName='sumweights/genWeights' & #136 * 3*.108

    echo 'Weight WW to 1L1Nu QQ'
    EventWeightsIterativeGen outputFile='WWTo1L1Nu2Q.root'  weight=45.997    histoName='TT/results' sumHistoName='sumweights/genWeights' &

    echo 'Weight WW To 2L 2Nu'
    EventWeightsIterativeGen outputFile='WWTo2L2Nu.root'    weight=11.08    histoName='TT/results' sumHistoName='sumweights/genWeights' &

    echo 'Weight WW To To 4Q'
    EventWeightsIterativeGen outputFile='WWTo4Q.root'       weight=47.73    histoName='TT/results' sumHistoName='sumweights/genWeights' &

    echo 'Weight ZZ 2L2Q'
    EventWeightsIterativeGen outputFile='ZZTo2L2Q.root'     weight=3.688  histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight ZZ 2L2Nu'
    EventWeightsIterativeGen outputFile='ZZTo2L2Nu.root'    weight=0.6008  histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight ZZTo4L'
    EventWeightsIterativeGen outputFile='ZZTo4L.root'       weight=1.325  histoName='TT/results' sumHistoName='sumweights/genWeights' &

    echo 'Weight EWK Wm2j'
    EventWeightsIterativeGen outputFile='EWKWm2j.root'       weight=  histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight EWK Wp2j'
    EventWeightsIterativeGen outputFile='EWKWp2j.root'       weight=  histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight EWK Z2Nu'
    EventWeightsIterativeGen outputFile='EWKZ2Nu.root'       weight=  histoName='TT/results' sumHistoName='sumweights/genWeights' &
    echo 'Weight EWK Z2l'
    EventWeightsIterativeGen outputFile='EWKZ2l.root'       weight=  histoName='TT/results' sumHistoName='sumweights/genWeights' &

    #echo 'Weight VV to 2L2Nu'
    #EventWeightsIterativeGen outputFile='VVTo2L2Nu.root'    weight=11.95    histoName='TT/results' sumHistoName='sumweights/genWeights' &

    #echo 'Weight TriBoson WWW'
    #EventWeightsIterativeGen outputFile='WWW.root'          weight=0.2086     histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #echo 'Weight TriBoson ZZZ'
    #EventWeightsIterativeGen outputFile='ZZZ.root'          weight=0.01398      histoName='TT/results' sumHistoName='sumweights/genWeights' &

    #EventWeightsIterativeGen outputFile='WZJTo1L3Nu.root'      weight=4.708   histoName='TT/results' sumHistoName='sumweights/genWeights' &
#add m_ll>30

    #echo 'Weight WW to L1Nu QQ'
    #EventWeightsIterativeGen outputFile='WWToLNuQQ.root'     weight=49.997    histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeGen outputFile='WWTo2L2Q.root'     weight=49.997    histoName='TT/results' sumHistoName='sumweights/genWeights' &

    wait;

    hadd -f DiBoson.root WWTo*root WZTo*root ZZTo*.root St_*.root t*tW.root EWK*.root
    hadd -f TT.root TT_*.root
fi


#now doing some cleanup
mv St_t* ../unneededZTT/.
mv WW*.root ../unneededZTT/.
mv Z*Jets.root ../unneededZTT/.
mv W*Jets.root ../unneededZTT/.
mv WJets.root ../unneededZTT/.
mv ZJets_* ../unneededZTT/.
mv WZ*.root ../unneededZTT/.
mv t* ../unneededZTT/.
mv ZZ*.root ../unneededZTT/.
mv EWK*.root ../unneededZTT/.


