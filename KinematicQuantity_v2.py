#!/usr/bin/env python

# import some modules
import sys, os
# add MG5_aMC into the path and import the lhe_parser
sys.path.append("/users/wuxingyu/MG5_aMC_v2_9_2/")
from madgraph.various.lhe_parser import *
# import ROOT, creat an alias
import ROOT as R
# import array to save the address in class Branch
from array import array



# define a function named "read_lhe", its input is "InputFileList"
def read_lhe(InputFileList):


  # define some initial values before the loop
  # define the invariant mass of Z boson, in GeV
  Zmass = 91.187621
  # define 3 initial values to count the correct pairs and the wrong pairs
  CorrectPair = 0
  WrongPair = 0
  SumPair = 0
  # define an initial value to save the accuracy
  Accuracy = 0


  """
  histogram the Zmass which is rebuilt from leptons and closest to the real Zmass. Named it as "M1"
  """
  htitle = "M1"
  nbins, xmin, xmax = 40, 80, 100
  h_M1 = R.TH1F("M1", htitle, nbins, xmin, xmax)
  h_M1.SetTitle("M1;M1/GeV;events")

  """
  histogram the Zmass which is rebuilt from the another pair leptons except M1, named it as "M2"
  """
  htitle = "M2"
  nbins, xmin, xmax = 40, 70, 110
  h_M2 = R.TH1F("M2", htitle, nbins, xmin, xmax)
  h_M2.SetTitle("M2;M2/GeV;events")

  """
  histogram the M4l, which is the mass of 4 leptons
  """
  htilte = "M4l"
  nbins, xmin, xmax = 40, 150, 550
  h_M4l = R.TH1F("M4l", htitle, nbins, xmin, xmax)
  h_M4l.SetTitle("M4l;M4l/GeV;events")

  """
  histogram the Zmass which is rebuilt from leptons using MOTHUP and closest to the real Zmass. Named it as "M1MOTHUP"
  """
  htitle = "M1MOTHUP"
  nbins, xmin, xmax = 40, 80, 100
  h_M1MOTHUP = R.TH1F("M1MOTHUP", htitle, nbins, xmin, xmax)
  h_M1MOTHUP.SetTitle("M1MOTHUP;M1/GeV;events")

  """
  histogram the Zmass which is rebuilt from the another pair leptons using MOTHUP except M1MOTHUP, named it as "M2MOTHUP"
  """
  htitle = "M2MOTHUP"
  nbins, xmin, xmax = 40, 70, 110
  h_M2MOTHUP = R.TH1F("M2MOTHUP", htitle, nbins, xmin, xmax)
  h_M2MOTHUP.SetTitle("M2MOTHUP;M2/GeV;events")

  """
  histogram the Zmass which is rebuilt from leptons and closest to the real Zmass. Named it as "M1", "TT" means the sort of polarization
  """
  htitle = "TTM1"
  nbins, xmin, xmax = 40, 80, 100
  h_TTM1 = R.TH1F("TTM1", htitle, nbins, xmin, xmax)
  h_TTM1.SetTitle("TTM1;TTM1/GeV;events")

  """
  histogram the Zmass which is rebuilt from the another pair leptons except M1, named it as "M2", "TT" means the sort of polarization
  """
  htitle = "TTM2"
  nbins, xmin, xmax = 40, 70, 110
  h_TTM2 = R.TH1F("TTM2", htitle, nbins, xmin, xmax)
  h_TTM2.SetTitle("TTM2;TTM2/GeV;events")

  """
  histogram the M4l, which is the mass of 4 leptons, "TT" means the sort of polarization
  """
  htilte = "TTM4l"
  nbins, xmin, xmax = 40, 150, 550
  h_TTM4l = R.TH1F("TTM4l", htitle, nbins, xmin, xmax)
  h_TTM4l.SetTitle("TTM4l;TTM4l/GeV;events")

  """
  histogram the Zmass which is rebuilt from leptons and closest to the real Zmass. Named it as "M1", "TL" means the sort of polarization
  """
  htitle = "TLM1"
  nbins, xmin, xmax = 40, 80, 100
  h_TLM1 = R.TH1F("TLM1", htitle, nbins, xmin, xmax)
  h_TLM1.SetTitle("TLM1;TLM1/GeV;events")

  """
  histogram the Zmass which is rebuilt from the another pair leptons except M1, named it as "M2", "TL" means the sort of polarization
  """
  htitle = "TLM2"
  nbins, xmin, xmax = 40, 70, 110
  h_TLM2 = R.TH1F("TLM2", htitle, nbins, xmin, xmax)
  h_TLM2.SetTitle("TLM2;TLM2/GeV;events")

  """
  histogram the M4l, which is the mass of 4 leptons, "TL" means the sort of polarization
  """
  htilte = "TLM4l"
  nbins, xmin, xmax = 40, 150, 550
  h_TLM4l = R.TH1F("TLM4l", htitle, nbins, xmin, xmax)
  h_TLM4l.SetTitle("TLM4l;TLM4l/GeV;events")

  """
  histogram the Zmass which is rebuilt from leptons and closest to the real Zmass. Named it as "M1", "LL" means the sort of polarization
  """
  htitle = "LLM1"
  nbins, xmin, xmax = 40, 80, 100
  h_LLM1 = R.TH1F("LLM1", htitle, nbins, xmin, xmax)
  h_LLM1.SetTitle("LLM1;LLM1/GeV;events")

  """
  histogram the Zmass which is rebuilt from the another pair leptons except M1, named it as "M2", "LL" means the sort of polarization
  """
  htitle = "LLM2"
  nbins, xmin, xmax = 40, 70, 110
  h_LLM2 = R.TH1F("LLM2", htitle, nbins, xmin, xmax)
  h_LLM2.SetTitle("LLM2;LLM2/GeV;events")

  """
  histogram the M4l, which is the mass of 4 leptons, "LL" means the sort of polarization
  """
  htilte = "LLM4l"
  nbins, xmin, xmax = 40, 150, 550
  h_LLM4l = R.TH1F("LLM4l", htitle, nbins, xmin, xmax)
  h_LLM4l.SetTitle("LLM4l;LLM4l/GeV;events")

  """
  histogram the CosTheta, "CosTheta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1
  """
  htitle = "CosTheta1"
  nbins, xmin, xmax = 40, -1, 1
  h_CosTheta1 = R.TH1F("CosTheta1", htitle, nbins, xmin, xmax)
  h_CosTheta1.SetTitle("CosTheta1;CosTheta1;events")

  """
  histogram the CosTheta, "CosTheta2" means this is the angle between Z boson which is marked as "M2" and 1 lepton in 2 leptons which rebuild the M2
  """
  htitle = "CosTheta2"
  nbins, xmin, xmax = 40, -1, 1
  h_CosTheta2 = R.TH1F("CosTheta2", htitle, nbins, xmin, xmax)
  h_CosTheta2.SetTitle("CosTheta2;CosTheta2;events")

  """
  histogram the Theta, "Theta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1
  """
  htitle = "Theta1"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_Theta1 = R.TH1F("Theta1", htitle, nbins, xmin, xmax)
  h_Theta1.SetTitle("Theta1;Theta1;events")

  """
  histogram the Theta, "Theta2" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1
  """
  htitle = "Theta2"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_Theta2 = R.TH1F("Theta2", htitle, nbins, xmin, xmax)
  h_Theta2.SetTitle("Theta2;Theta2;events")

  """
  histogram the CosTheta, "CosTheta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TT" means the sort of polarization
  """
  htitle = "TTCosTheta1"
  nbins, xmin, xmax = 40, -1, 1
  h_TTCosTheta1 = R.TH1F("TTCosTheta1", htitle, nbins, xmin, xmax)
  h_TTCosTheta1.SetTitle("TTCosTheta1;CosTheta1;events")

  """
  histogram the CosTheta, "CosTheta2" means this is the angle between Z boson which is marked as "M2" and 1 lepton in 2 leptons which rebuild the M2, "TT" means the sort of polarization
  """
  htitle = "TTCosTheta2"
  nbins, xmin, xmax = 40, -1, 1
  h_TTCosTheta2 = R.TH1F("TTCosTheta2", htitle, nbins, xmin, xmax)
  h_TTCosTheta2.SetTitle("TTCosTheta2;CosTheta2;events")

  """
  histogram the Theta, "Theta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TT" means the sort of polarization
  """
  htitle = "TTTheta1"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_TTTheta1 = R.TH1F("TTTheta1", htitle, nbins, xmin, xmax)
  h_TTTheta1.SetTitle("TTTheta1;Theta1;events")

  """
  histogram the Theta, "Theta2" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TT" means the sort of polarization
  """
  htitle = "TTTheta2"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_TTTheta2 = R.TH1F("TTTheta2", htitle, nbins, xmin, xmax)
  h_TTTheta2.SetTitle("TTTheta2;Theta2;events")

  """
  histogram the CosTheta, "CosTheta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TL" means the sort of polarization
  """
  htitle = "TLCosTheta1"
  nbins, xmin, xmax = 40, -1, 1
  h_TLCosTheta1 = R.TH1F("TLCosTheta1", htitle, nbins, xmin, xmax)
  h_TLCosTheta1.SetTitle("TLCosTheta1;CosTheta1;events")

  """
  histogram the CosTheta, "CosTheta2" means this is the angle between Z boson which is marked as "M2" and 1 lepton in 2 leptons which rebuild the M2, "TL" means the sort of polarization
  """
  htitle = "TLCosTheta2"
  nbins, xmin, xmax = 40, -1, 1
  h_TLCosTheta2 = R.TH1F("TLCosTheta2", htitle, nbins, xmin, xmax)
  h_TLCosTheta2.SetTitle("TLCosTheta2;CosTheta2;events")

  """
  histogram the Theta, "Theta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TL" means the sort of polarization
  """
  htitle = "TLTheta1"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_TLTheta1 = R.TH1F("TLTheta1", htitle, nbins, xmin, xmax)
  h_TLTheta1.SetTitle("TLTheta1;Theta1;events")

  """
  histogram the Theta, "Theta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "TL" means the sort of polarization
  """
  htitle = "TLTheta2"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_TLTheta2 = R.TH1F("TLTheta2", htitle, nbins, xmin, xmax)
  h_TLTheta2.SetTitle("TLTheta2;Theta2;events")

  """
  histogram the CosTheta, "CosTheta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "LL" means the sort of polarization
  """
  htitle = "LLCosTheta1"
  nbins, xmin, xmax = 40, -1, 1
  h_LLCosTheta1 = R.TH1F("LLCosTheta1", htitle, nbins, xmin, xmax)
  h_LLCosTheta1.SetTitle("LLCosTheta1;CosTheta1;events")

  """
  histogram the CosTheta, "CosTheta2" means this is the angle between Z boson which is marked as "M2" and 1 lepton in 2 leptons which rebuild the M2, "LL" means the sort of polarization
  """
  htitle = "LLCosTheta2"
  nbins, xmin, xmax = 40, -1, 1
  h_LLCosTheta2 = R.TH1F("LLCosTheta2", htitle, nbins, xmin, xmax)
  h_LLCosTheta2.SetTitle("LLCosTheta2;CosTheta2;events")

  """
  histogram the Theta, "Theta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "LL" means the sort of polarization
  """
  htitle = "LLTheta1"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_LLTheta1 = R.TH1F("LLTheta1", htitle, nbins, xmin, xmax)
  h_LLTheta1.SetTitle("LLTheta1;Theta1;events")

  """
  histogram the Theta, "Theta2" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1, "LL" means the sort of polarization
  """
  htitle = "LLTheta2"
  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_LLTheta2 = R.TH1F("LLTheta2", htitle, nbins, xmin, xmax)
  h_LLTheta2.SetTitle("LLTheta2;Theta2;events")

  """
  histogram the ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1
  """
  htitle = "ThetaStar1"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_ThetaStar1 = R.TH1F("ThetaStar1", htitle, nbins, xmin, xmax)
  h_ThetaStar1.SetTitle("ThetaStar1;ThetaStar1;events")

  """
  histogram the ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2
  """
  htitle = "ThetaStar2"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_ThetaStar2 = R.TH1F("ThetaStar2", htitle, nbins, xmin, xmax)
  h_ThetaStar2.SetTitle("ThetaStar2;ThetaStar2;events")

  """
  histogram the ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "TT" means the sort of polarization
  """
  htitle = "TTThetaStar1"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_TTThetaStar1 = R.TH1F("TTThetaStar1", htitle, nbins, xmin, xmax)
  h_TTThetaStar1.SetTitle("TTThetaStar1;ThetaStar1;events")

  """
  histogram the ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "TT" means the sort of polarization
  """
  htitle = "TTThetaStar2"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_TTThetaStar2 = R.TH1F("TTThetaStar2", htitle, nbins, xmin, xmax)
  h_TTThetaStar2.SetTitle("TTThetaStar2;ThetaStar2;events")

  """
  histogram the ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "TL" means the sort of polarization
  """
  htitle = "TLThetaStar1"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_TLThetaStar1 = R.TH1F("TLThetaStar1", htitle, nbins, xmin, xmax)
  h_TLThetaStar1.SetTitle("TLThetaStar1;ThetaStar1;events")

  """
  histogram the ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "TL" means the sort of polarization
  """
  htitle = "TLThetaStar2"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_TLThetaStar2 = R.TH1F("TLThetaStar2", htitle, nbins, xmin, xmax)
  h_TLThetaStar2.SetTitle("TLThetaStar2;ThetaStar2;events")

  """
  histogram the ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "LL" means the sort of polarization
  """
  htitle = "LLThetaStar1"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_LLThetaStar1 = R.TH1F("LLThetaStar1", htitle, nbins, xmin, xmax)
  h_LLThetaStar1.SetTitle("LLThetaStar1;ThetaStar1;events")

  """
  histogram the ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "LL" means the sort of polarization
  """
  htitle = "LLThetaStar2"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_LLThetaStar2 = R.TH1F("LLThetaStar2", htitle, nbins, xmin, xmax)
  h_LLThetaStar2.SetTitle("LLThetaStar2;ThetaStar2;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1
  """
  htitle = "CosThetaStar1"
  nbins, xmin, xmax = 40, -1, 1
  h_CosThetaStar1 = R.TH1F("CosThetaStar1", htitle, nbins, xmin, xmax)
  h_CosThetaStar1.SetTitle("CosThetaStar1;CosThetaStar1;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2
  """
  htitle = "CosThetaStar2"
  nbins, xmin, xmax = 40, -1, 1
  h_CosThetaStar2 = R.TH1F("CosThetaStar2", htitle, nbins, xmin, xmax)
  h_CosThetaStar2.SetTitle("CosThetaStar2;CosThetaStar2;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "TT" means the sort of polarization
  """
  htitle = "TTCosThetaStar1"
  nbins, xmin, xmax = 40, -1, 1
  h_TTCosThetaStar1 = R.TH1F("TTCosThetaStar1", htitle, nbins, xmin, xmax)
  h_TTCosThetaStar1.SetTitle("TTCosThetaStar1;CosThetaStar1;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "TT" means the sort of polarization
  """
  htitle = "TTCosThetaStar2"
  nbins, xmin, xmax = 40, -1, 1
  h_TTCosThetaStar2 = R.TH1F("TTCosThetaStar2", htitle, nbins, xmin, xmax)
  h_TTCosThetaStar2.SetTitle("TTCosThetaStar2;CosThetaStar2;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "TL" means the sort of polarization
  """
  htitle = "TLCosThetaStar1"
  nbins, xmin, xmax = 40, -1, 1
  h_TLCosThetaStar1 = R.TH1F("TLCosThetaStar1", htitle, nbins, xmin, xmax)
  h_TLCosThetaStar1.SetTitle("TLCosThetaStar1;CosThetaStar1;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "TL" means the sort of polarization
  """
  htitle = "TLCosThetaStar2"
  nbins, xmin, xmax = 40, -1, 1
  h_TLCosThetaStar2 = R.TH1F("TLCosThetaStar2", htitle, nbins, xmin, xmax)
  h_TLCosThetaStar2.SetTitle("TLCosThetaStar2;CosThetaStar2;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, "LL" means the sort of polarization
  """
  htitle = "LLCosThetaStar1"
  nbins, xmin, xmax = 40, -1, 1
  h_LLCosThetaStar1 = R.TH1F("LLCosThetaStar1", htitle, nbins, xmin, xmax)
  h_LLCosThetaStar1.SetTitle("LLCosThetaStar1;CosThetaStar1;events")

  """
  histogram the Cosin of ThetaStar, "ThetaStar2" means the ThetaStar is calculated from M2, "LL" means the sort of polarization
  """
  htitle = "LLCosThetaStar2"
  nbins, xmin, xmax = 40, -1, 1
  h_LLCosThetaStar2 = R.TH1F("LLCosThetaStar2", htitle, nbins, xmin, xmax)
  h_LLCosThetaStar2.SetTitle("LLCosThetaStar2;CosThetaStar2;events")

  """
  histogram the Phi
  """
  htitle = "Phi"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_Phi = R.TH1F("Phi", htitle, nbins, xmin, xmax)
  h_Phi.SetTitle("Phi;Phi;events")

  """
  histogram the Phi, "TT" means the sort of polarization
  """
  htitle = "TTPhi"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_TTPhi = R.TH1F("TTPhi", htitle, nbins, xmin, xmax)
  h_TTPhi.SetTitle("TTPhi;TTPhi;events")

  """
  histogram the Phi, "TL" means the sort of polarization
  """
  htitle = "TLPhi"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_TLPhi = R.TH1F("TLPhi", htitle, nbins, xmin, xmax)
  h_TLPhi.SetTitle("TLPhi;TLPhi;events")

  """
  histogram the Phi, "LL" means the sort of polarization
  """
  htitle = "LLPhi"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_LLPhi = R.TH1F("LLPhi", htitle, nbins, xmin, xmax)
  h_LLPhi.SetTitle("LLPhi;LLPhi;events")

  """
  histogram the Phi1
  """
  htitle = "Phi1"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_Phi1 = R.TH1F("Phi1", htitle, nbins, xmin, xmax)
  h_Phi1.SetTitle("Phi1;Phi1;events")

  """
  histogram the Phi1, "TT" means the sort of polarization
  """
  htitle = "TTPhi1"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_TTPhi1 = R.TH1F("TTPhi1", htitle, nbins, xmin, xmax)
  h_TTPhi1.SetTitle("TTPhi1;TTPhi1;events")

  """
  histogram the Phi1, "TL" means the sort of polarization
  """
  htitle = "TLPhi1"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_TLPhi1 = R.TH1F("TLPhi1", htitle, nbins, xmin, xmax)
  h_TLPhi1.SetTitle("TLPhi1;TLPhi1;events")

  """
  histogram the Phi1, "LL" means the sort of polarization
  """
  htitle = "LLPhi1"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_LLPhi1 = R.TH1F("LLPhi1", htitle, nbins, xmin, xmax)
  h_LLPhi1.SetTitle("LLPhi1;LLPhi1;events")

  """
  histogram the Cosin of Phi
  """
  htitle = "CosPhi"
  nbins, xmin, xmax = 40, 0, 1
  h_CosPhi = R.TH1F("CosPhi", htitle, nbins, xmin, xmax)
  h_CosPhi.SetTitle("CosPhi;CosPhi;events")

  """
  histogram the Cosin of Phi, "TT" means the sort of polarization
  """
  htitle = "TTCosPhi"
  nbins, xmin, xmax = 40, 0, 1
  h_TTCosPhi = R.TH1F("TTCosPhi", htitle, nbins, xmin, xmax)
  h_TTCosPhi.SetTitle("TTCosPhi;TTCosPhi;events")

  """
  histogram the Cosin of Phi, "TL" means the sort of polarization
  """
  htitle = "TLCosPhi"
  nbins, xmin, xmax = 40, 0, 1
  h_TLCosPhi = R.TH1F("TLCosPhi", htitle, nbins, xmin, xmax)
  h_TLCosPhi.SetTitle("TLCosPhi;TLCosPhi;events")

  """
  histogram the Cosin of Phi, "LL" means the sort of polarization
  """
  htitle = "LLCosPhi"
  nbins, xmin, xmax = 40, 0, 1
  h_LLCosPhi = R.TH1F("LLCosPhi", htitle, nbins, xmin, xmax)
  h_LLCosPhi.SetTitle("LLCosPhi;LLCosPhi;events")

  """
  histogram the Cosin of Phi1
  """
  htitle = "CosPhi1"
  nbins, xmin, xmax = 40, 0, 1
  h_CosPhi1 = R.TH1F("CosPhi1", htitle, nbins, xmin, xmax)
  h_CosPhi1.SetTitle("CosPhi1;CosPhi1;events")

  """
  histogram the Cosin of Phi1, "TT" means the sort of polarization
  """
  htitle = "TTCosPhi1"
  nbins, xmin, xmax = 40, 0, 1
  h_TTCosPhi1 = R.TH1F("TTCosPhi1", htitle, nbins, xmin, xmax)
  h_TTCosPhi1.SetTitle("TTCosPhi1;TTCosPhi1;events")

  """
  histogram the Cosin of Phi1, "TL" means the sort of polarization
  """
  htitle = "TLCosPhi1"
  nbins, xmin, xmax = 40, 0, 1
  h_TLCosPhi1 = R.TH1F("TLCosPhi1", htitle, nbins, xmin, xmax)
  h_TLCosPhi1.SetTitle("TLCosPhi1;TLCosPhi1;events")

  """
  histogram the Cosin of Phi1, "LL" means the sort of polarization
  """
  htitle = "LLCosPhi1"
  nbins, xmin, xmax = 40, 0, 1
  h_LLCosPhi1 = R.TH1F("LLCosPhi1", htitle, nbins, xmin, xmax)
  h_LLCosPhi1.SetTitle("LLCosPhi1;LLCosPhi1;events")

  """
  histogram the Eta of Z1
  """
  htitle = "Eta1"
  nbins, xmin, xmax = 40, -6, 6
  h_Eta1 = R.TH1F("Eta1", htitle, nbins, xmin, xmax)
  h_Eta1.SetTitle("Eta1;Eta1;events")

  """
  histogram the Eta of Z2
  """
  htitle = "Eta2"
  nbins, xmin, xmax = 40, -6, 6
  h_Eta2 = R.TH1F("Eta2", htitle, nbins, xmin, xmax)
  h_Eta2.SetTitle("Eta2;Eta2;events")

  """
  histogram the Eta of 4l
  """
  htitle = "Eta4l"
  nbins, xmin, xmax = 40, -6, 6
  h_Eta4l = R.TH1F("Eta4l", htitle, nbins, xmin, xmax)
  h_Eta4l.SetTitle("Eta4l;Eta4l;events")

  """
  histogram the Eta of Z1, "TT" means the sort of polarization
  """
  htitle = "TTEta1"
  nbins, xmin, xmax = 40, -6, 6
  h_TTEta1 = R.TH1F("TTEta1", htitle, nbins, xmin, xmax)
  h_TTEta1.SetTitle("TTEta1;TTEta1;events")

  """
  histogram the Eta of Z2, "TT" means the sort of polarization
  """
  htitle = "TTEta2"
  nbins, xmin, xmax = 40, -6, 6
  h_TTEta2 = R.TH1F("TTEta2", htitle, nbins, xmin, xmax)
  h_TTEta2.SetTitle("TTEta2;TTEta2;events")

  """
  histogram the Eta of 4l, "TT" means the sort of polarization
  """
  htitle = "TTEta4l"
  nbins, xmin, xmax = 40, -6, 6
  h_TTEta4l = R.TH1F("TTEta4l", htitle, nbins, xmin, xmax)
  h_TTEta4l.SetTitle("TTEta4l;TTEta4l;events")

  """  
  histogram the Eta of Z1, "TL" means the sort of polarization
  """
  htitle = "TLEta1"
  nbins, xmin, xmax = 40, -6, 6
  h_TLEta1 = R.TH1F("TLEta1", htitle, nbins, xmin, xmax)
  h_TLEta1.SetTitle("TLEta1;TLEta1;events")
  
  """
  histogram the Eta of Z2, "TL" means the sort of polarization
  """
  htitle = "TLEta2"
  nbins, xmin, xmax = 40, -6, 6
  h_TLEta2 = R.TH1F("TLEta2", htitle, nbins, xmin, xmax)
  h_TLEta2.SetTitle("TLEta2;TLEta2;events")

  """
  histogram the Eta of 4l, "TL" means the sort of polarization
  """
  htitle = "TLEta4l"
  nbins, xmin, xmax = 40, -6, 6
  h_TLEta4l = R.TH1F("TLEta4l", htitle, nbins, xmin, xmax)
  h_TLEta4l.SetTitle("TLEta4l;TLEta4l;events")

  """  
  histogram the Eta of Z1, "LL" means the sort of polarization
  """
  htitle = "LLEta1"
  nbins, xmin, xmax = 40, -6, 6
  h_LLEta1 = R.TH1F("LLEta1", htitle, nbins, xmin, xmax)
  h_LLEta1.SetTitle("LLEta1;LLEta1;events")
  
  """
  histogram the Eta of Z2, "LL" means the sort of polarization
  """
  htitle = "LLEta2"
  nbins, xmin, xmax = 40, -6, 6
  h_LLEta2 = R.TH1F("LLEta2", htitle, nbins, xmin, xmax)
  h_LLEta2.SetTitle("LLEta2;LLEta2;events")

  """
  histogram the Eta of 4l, "LL" means the sort of polarization
  """
  htitle = "LLEta4l"
  nbins, xmin, xmax = 40, -6, 6
  h_LLEta4l = R.TH1F("LLEta4l", htitle, nbins, xmin, xmax)
  h_LLEta4l.SetTitle("LLEta4l;LLEta4l;events")

  """
  histogram the Pt of Z1
  """
  htitle = "Pt1"
  nbins, xmin, xmax = 40, 0, 200
  h_Pt1 = R.TH1F("Pt1", htitle, nbins, xmin, xmax)
  h_Pt1.SetTitle("Pt1;Pt1;events")

  """
  histogram the Pt of Z2
  """
  htitle = "Pt2"
  nbins, xmin, xmax = 40, 0, 200
  h_Pt2 = R.TH1F("Pt2", htitle, nbins, xmin, xmax)
  h_Pt2.SetTitle("Pt2;Pt2;events")

  """
  histogram the Pt of 4l
  """
  htitle = "Pt4l"
  nbins, xmin, xmax = 40, 0, 200
  h_Pt4l = R.TH1F("Pt4l", htitle, nbins, xmin, xmax)
  h_Pt4l.SetTitle("Pt4l;Pt4l;events")

  """
  histogram the Pt of Z1, "TT" means the sort of polarization
  """
  htitle = "TTPt1"
  nbins, xmin, xmax = 40, 0, 200
  h_TTPt1 = R.TH1F("TTPt1", htitle, nbins, xmin, xmax)
  h_TTPt1.SetTitle("TTPt1;TTPt1;events")

  """
  histogram the Pt of Z2, "TT" means the sort of polarization
  """
  htitle = "TTPt2"
  nbins, xmin, xmax = 40, 0, 200
  h_TTPt2 = R.TH1F("TTPt2", htitle, nbins, xmin, xmax)
  h_TTPt2.SetTitle("TTPt2;TTPt2;events")
      
  """
  histogram the Pt of 4l, "TT" means the sort of polarization
  """
  htitle = "TTPt4l"
  nbins, xmin, xmax = 40, 0, 200
  h_TTPt4l = R.TH1F("TTPt4l", htitle, nbins, xmin, xmax)
  h_TTPt4l.SetTitle("TTPt4l;TTPt4l;events")

  """
  histogram the Pt of Z1, "TL" means the sort of polarization
  """
  htitle = "TLPt1"
  nbins, xmin, xmax = 40, 0, 200
  h_TLPt1 = R.TH1F("TLPt1", htitle, nbins, xmin, xmax)
  h_TLPt1.SetTitle("TLPt1;TLPt1;events")

  """
  histogram the Pt of Z2, "TL" means the sort of polarization
  """
  htitle = "TLPt2"
  nbins, xmin, xmax = 40, 0, 200
  h_TLPt2 = R.TH1F("TLPt2", htitle, nbins, xmin, xmax)
  h_TLPt2.SetTitle("TLPt2;TLPt2;events")

  """
  histogram the Pt of 4l, "TL" means the sort of polarization
  """
  htitle = "TLPt4l"
  nbins, xmin, xmax = 40, 0, 200
  h_TLPt4l = R.TH1F("TLPt4l", htitle, nbins, xmin, xmax)
  h_TLPt4l.SetTitle("TLPt4l;TLPt4l;events")

  """
  histogram the Pt of Z1, "LL" means the sort of polarization
  """
  htitle = "LLPt1"
  nbins, xmin, xmax = 40, 0, 200
  h_LLPt1 = R.TH1F("LLPt1", htitle, nbins, xmin, xmax)
  h_LLPt1.SetTitle("LLPt1;LLPt1;events")

  """
  histogram the Pt of Z2, "LL" means the sort of polarization
  """
  htitle = "LLPt2"
  nbins, xmin, xmax = 40, 0, 200
  h_LLPt2 = R.TH1F("LLPt2", htitle, nbins, xmin, xmax)
  h_LLPt2.SetTitle("LLPt2;LLPt2;events")

  """
  histogram the Pt of 4l, "LL" means the sort of polarization
  """
  htitle = "LLPt4l"
  nbins, xmin, xmax = 40, 0, 200
  h_LLPt4l = R.TH1F("LLPt4l", htitle, nbins, xmin, xmax)
  h_LLPt4l.SetTitle("LLPt4l;LLPt4l;events")



  """
  Create some trees to save the MontCarlo Events
  """

  # in order to use address in Python, create 1 dimensional float arrays as fill variables
  # in this way the float array serves as a pointer which can be passed to the branch
  # "d" means double, [0] means 1 dimensional float array, and its value is 0
  M1 = array("d", [0])
  M2 = array("d", [0])
  M4l = array("d", [0])
  M1MOTHUP = array("d", [0])
  M2MOTHUP = array("d", [0])
  CosTheta1 = array("d", [0])
  CosTheta2 = array("d", [0])
  Theta1 = array("d", [0])
  Theta2 = array("d", [0])
  ThetaStar1 = array("d", [0])
  ThetaStar2 = array("d", [0])
  CosThetaStar1 = array("d", [0])
  CosThetaStar2 = array("d", [0])
  PhiCopy = array("d", [0])
  Phi1Copy = array("d", [0])
  CosPhi = array("d", [0])
  CosPhi1 = array("d", [0])
  Eta1 = array("d", [0])
  Eta2 = array("d", [0])
  Eta4l = array("d", [0])
  Pt1 = array("d", [0])
  Pt2 = array("d", [0])
  Pt4l = array("d", [0])

  """
  Inclusive
  """
  # create a root file to save the tree
  InclusiveTreeFile = R.TFile("InclusiveTree.root", "RECREATE")
  # create a tree, define its name and title
  InclusiveTree = R.TTree("InclusiveTree", "InclusiveTree")

  # set the name, address, leaf list and variable type
  # M1 in "M1/D" means leaf, D in "M1/D" means variable type
  InclusiveTree.Branch("M1", M1, "M1/D")
  InclusiveTree.Branch("M2", M2, "M2/D")
  InclusiveTree.Branch("M4l", M4l, "M4l/D")
  InclusiveTree.Branch("M1MOTHUP", M1MOTHUP, "M1MOTHUP/D")
  InclusiveTree.Branch("M2MOTHUP", M2MOTHUP, "M2MOTHUP/D")
  InclusiveTree.Branch("CosTheta1", CosTheta1, "CosTheta1/D")
  InclusiveTree.Branch("CosTheta2", CosTheta2, "CosTheta2/D")
  InclusiveTree.Branch("Theta1", Theta1, "Theta1/D")
  InclusiveTree.Branch("Theta2", Theta2, "Theta2/D")
  InclusiveTree.Branch("ThetaStar1", ThetaStar1, "ThetaStar1/D")
  InclusiveTree.Branch("ThetaStar2", ThetaStar2, "ThetaStar2/D")
  InclusiveTree.Branch("CosThetaStar1", CosThetaStar1, "CosThetaStar1/D")
  InclusiveTree.Branch("CosThetaStar2", CosThetaStar2, "CosThetaStar2/D")
  InclusiveTree.Branch("Phi", PhiCopy, "Phi/D")
  InclusiveTree.Branch("Phi1", Phi1Copy, "Phi1/D")
  InclusiveTree.Branch("CosPhi", CosPhi, "CosPhi/D")
  InclusiveTree.Branch("CosPhi1", CosPhi1, "CosPhi1/D")
  InclusiveTree.Branch("Eta1", Eta1, "Eta1/D")
  InclusiveTree.Branch("Eta2", Eta2, "Eta2/D")
  InclusiveTree.Branch("Eta4l", Eta4l, "Eta4l/D")
  InclusiveTree.Branch("Pt1", Pt1, "Pt1/D")
  InclusiveTree.Branch("Pt2", Pt2, "Pt2/D")
  InclusiveTree.Branch("Pt4l", Pt4l, "Pt4l/D")

  """
  TT
  """
  # create a root file to save the tree
  TTTreeFile = R.TFile("TTTree.root", "RECREATE")
  # create a tree, define its name and title
  TTTree = R.TTree("TTTree", "TTTree")

  TTTree.Branch("M1", M1, "M1/D")
  TTTree.Branch("M2", M2, "M2/D")
  TTTree.Branch("M4l", M4l, "M4l/D")
  TTTree.Branch("M1MOTHUP", M1MOTHUP, "M1MOTHUP/D")
  TTTree.Branch("M2MOTHUP", M2MOTHUP, "M2MOTHUP/D")
  TTTree.Branch("CosTheta1", CosTheta1, "CosTheta1/D")
  TTTree.Branch("CosTheta2", CosTheta2, "CosTheta2/D")
  TTTree.Branch("Theta1", Theta1, "Theta1/D")
  TTTree.Branch("Theta2", Theta2, "Theta2/D")
  TTTree.Branch("ThetaStar1", ThetaStar1, "ThetaStar1/D")
  TTTree.Branch("ThetaStar2", ThetaStar2, "ThetaStar2/D")
  TTTree.Branch("CosThetaStar1", CosThetaStar1, "CosThetaStar1/D")
  TTTree.Branch("CosThetaStar2", CosThetaStar2, "CosThetaStar2/D")
  TTTree.Branch("Phi", PhiCopy, "Phi/D")
  TTTree.Branch("Phi1", Phi1Copy, "Phi1/D")
  TTTree.Branch("CosPhi", CosPhi, "CosPhi/D")
  TTTree.Branch("CosPhi1", CosPhi1, "CosPhi1/D")
  TTTree.Branch("Eta1", Eta1, "Eta1/D")
  TTTree.Branch("Eta2", Eta2, "Eta2/D")
  TTTree.Branch("Eta4l", Eta4l, "Eta4l/D")
  TTTree.Branch("Pt1", Pt1, "Pt1/D")
  TTTree.Branch("Pt2", Pt2, "Pt2/D")
  TTTree.Branch("Pt4l", Pt4l, "Pt4l/D")

  """
  TL
  """
  # create a root file to save the tree
  TLTreeFile = R.TFile("TLTree.root", "RECREATE")
  # create a tree, define its name and title
  TLTree = R.TTree("TLTree", "TLTree")

  TLTree.Branch("M1", M1, "M1/D")
  TLTree.Branch("M2", M2, "M2/D")
  TLTree.Branch("M4l", M4l, "M4l/D")
  TLTree.Branch("M1MOTHUP", M1MOTHUP, "M1MOTHUP/D")
  TLTree.Branch("M2MOTHUP", M2MOTHUP, "M2MOTHUP/D")
  TLTree.Branch("CosTheta1", CosTheta1, "CosTheta1/D")
  TLTree.Branch("CosTheta2", CosTheta2, "CosTheta2/D")
  TLTree.Branch("Theta1", Theta1, "Theta1/D")
  TLTree.Branch("Theta2", Theta2, "Theta2/D")
  TLTree.Branch("ThetaStar1", ThetaStar1, "ThetaStar1/D")
  TLTree.Branch("ThetaStar2", ThetaStar2, "ThetaStar2/D")
  TLTree.Branch("CosThetaStar1", CosThetaStar1, "CosThetaStar1/D")
  TLTree.Branch("CosThetaStar2", CosThetaStar2, "CosThetaStar2/D")
  TLTree.Branch("Phi", PhiCopy, "Phi/D")
  TLTree.Branch("Phi1", Phi1Copy, "Phi1/D")
  TLTree.Branch("CosPhi", CosPhi, "CosPhi/D")
  TLTree.Branch("CosPhi1", CosPhi1, "CosPhi1/D")
  TLTree.Branch("Eta1", Eta1, "Eta1/D")
  TLTree.Branch("Eta2", Eta2, "Eta2/D")
  TLTree.Branch("Eta4l", Eta4l, "Eta4l/D")
  TLTree.Branch("Pt1", Pt1, "Pt1/D")
  TLTree.Branch("Pt2", Pt2, "Pt2/D")
  TLTree.Branch("Pt4l", Pt4l, "Pt4l/D")

  """
  LL
  """
  # create a root file to save the tree
  LLTreeFile = R.TFile("LLTree.root", "RECREATE")
  # create a tree, define its name and title
  LLTree = R.TTree("LLTree", "LLTree")

  LLTree.Branch("M1", M1, "M1/D")
  LLTree.Branch("M2", M2, "M2/D")
  LLTree.Branch("M4l", M4l, "M4l/D")
  LLTree.Branch("M1MOTHUP", M1MOTHUP, "M1MOTHUP/D")
  LLTree.Branch("M2MOTHUP", M2MOTHUP, "M2MOTHUP/D")
  LLTree.Branch("CosTheta1", CosTheta1, "CosTheta1/D")
  LLTree.Branch("CosTheta2", CosTheta2, "CosTheta2/D")
  LLTree.Branch("Theta1", Theta1, "Theta1/D")
  LLTree.Branch("Theta2", Theta2, "Theta2/D")
  LLTree.Branch("ThetaStar1", ThetaStar1, "ThetaStar1/D")
  LLTree.Branch("ThetaStar2", ThetaStar2, "ThetaStar2/D")
  LLTree.Branch("CosThetaStar1", CosThetaStar1, "CosThetaStar1/D")
  LLTree.Branch("CosThetaStar2", CosThetaStar2, "CosThetaStar2/D")
  LLTree.Branch("Phi", PhiCopy, "Phi/D")
  LLTree.Branch("Phi1", Phi1Copy, "Phi1/D")
  LLTree.Branch("CosPhi", CosPhi, "CosPhi/D")
  LLTree.Branch("CosPhi1", CosPhi1, "CosPhi1/D")
  LLTree.Branch("Eta1", Eta1, "Eta1/D")
  LLTree.Branch("Eta2", Eta2, "Eta2/D")
  LLTree.Branch("Eta4l", Eta4l, "Eta4l/D")
  LLTree.Branch("Pt1", Pt1, "Pt1/D")
  LLTree.Branch("Pt2", Pt2, "Pt2/D")
  LLTree.Branch("Pt4l", Pt4l, "Pt4l/D")

  """
  TT+TL
  """
  # create a root file to save the tree
  TTTLTreeFile = R.TFile("TTTLTree.root", "RECREATE")
  # create a tree, define its name and title
  TTTLTree = R.TTree("TTTLTree", "TTTLTree")

  TTTLTree.Branch("M1", M1, "M1/D")
  TTTLTree.Branch("M2", M2, "M2/D")
  TTTLTree.Branch("M4l", M4l, "M4l/D")
  TTTLTree.Branch("M1MOTHUP", M1MOTHUP, "M1MOTHUP/D")
  TTTLTree.Branch("M2MOTHUP", M2MOTHUP, "M2MOTHUP/D")
  TTTLTree.Branch("CosTheta1", CosTheta1, "CosTheta1/D")
  TTTLTree.Branch("CosTheta2", CosTheta2, "CosTheta2/D")
  TTTLTree.Branch("Theta1", Theta1, "Theta1/D")
  TTTLTree.Branch("Theta2", Theta2, "Theta2/D")
  TTTLTree.Branch("ThetaStar1", ThetaStar1, "ThetaStar1/D")
  TTTLTree.Branch("ThetaStar2", ThetaStar2, "ThetaStar2/D")
  TTTLTree.Branch("CosThetaStar1", CosThetaStar1, "CosThetaStar1/D")
  TTTLTree.Branch("CosThetaStar2", CosThetaStar2, "CosThetaStar2/D")
  TTTLTree.Branch("Phi", PhiCopy, "Phi/D")
  TTTLTree.Branch("Phi1", Phi1Copy, "Phi1/D")
  TTTLTree.Branch("CosPhi", CosPhi, "CosPhi/D")
  TTTLTree.Branch("CosPhi1", CosPhi1, "CosPhi1/D")
  TTTLTree.Branch("Eta1", Eta1, "Eta1/D")
  TTTLTree.Branch("Eta2", Eta2, "Eta2/D")
  TTTLTree.Branch("Eta4l", Eta4l, "Eta4l/D")
  TTTLTree.Branch("Pt1", Pt1, "Pt1/D")
  TTTLTree.Branch("Pt2", Pt2, "Pt2/D")
  TTTLTree.Branch("Pt4l", Pt4l, "Pt4l/D")


  for InputFile in InputFileList:
      # use Class EventFile defined in the lhe_parser.py to read the usage information in the LHE files
      lhe = EventFile(InputFile)

      # loop the events
      for event in lhe:
    
          """
          4 blocks: 1st function: histogram the M1, M2 and M4l;
                    2ed function: histogram the M1MOTHUP and M2MOTHUP; 
                    3rd function: find the correct pair and the wrong pair, count it and calculate the accuracy
                    4th function: histogram the theta1 and theta2
                    5th function: histogram the ThetaStar1 and ThetaStar2
                    6th function: histogram the Phi
                    7th function: histogram the Phi1
                    8th function: histogram the eta
                    9th function: histogram the Pt1, Pt2 and Pt4l
                    10th function: fill the tree
          """

    
          """
          block of 1st function: histogram the M1 and M2
          """
    
          # define some initial values in the loop
          # define an empty list to save the particleID of final state particles
          PidList = []
          # define 4 empty lists to save the order number of each possible pair of leptons
          PidPair1, PidPair2, PidPair3, PidPair4 = [], [], [], []
          # define an empty list to save the absolute value of PidList
          AbsPidList = []
          # define 4 initial values to count the leptons in each "if" loop
          PidCount1, PidCount2, PidCount3, PidCount4 = 0, 0, 0, 0
          # define an initial value to count the particles in each event, "1" represents that it is the count of 1st function block
          ParticleCount1 = 0
          # define 4 empty lists to save the TLorentzVector for each possible pairs
          T1, T2, T3, T4 = [], [], [], []
          # define 4 initial values to save the sum of TLorentzVector for each possible pairs
          T1Sum, T2Sum, T3Sum, T4Sum = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          # define 4 empty lists to save the copy of TLorentzVector for each possible pairs
          T1Copy1, T2Copy1, T3Copy1, T4Copy1 = [], [], [], []
          # define 4 initial values to save the copy of sum of TLorentzVector for each possible pairs
          T1SumCopy1, T2SumCopy1, T3SumCopy1, T4SumCopy1 = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          # define 4 empty lists to save the copy of TLorentzVector for each possible pairs
          T1Copy2, T2Copy2, T3Copy2, T4Copy2 = [], [], [], []
          # define 4 initial values to save the copy of sum of TLorentzVector for each possible pairs
          T1SumCopy2, T2SumCopy2, T3SumCopy2, T4SumCopy2 = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          # define 4 initial values to save the deltam for each possible pairs, so that we can choose the smallest one.
          deltam1, deltam2, deltam3, deltam4 = 0, 0, 0, 0
          # define an empty list to save the 4 Zmass that rebuilt from each possible pairs
          m = []
          # define an empty list to save the 4 deltam
          deltam = []
          # define an empty list to save the sorts of deltam
          deltamSorts = []
          """
          In order to use address, change M1, M2 to M1[0], M2[0], the same as the other variables
          """
          # define 2 initial values to save the M1 and M2
          # M1, M2 = 0, 0
          # define an empty list to save the T1Sum, T2Sum, T3Sum, T4Sum
          TSum = []
          # define an empty list to save the T1SumCopy1, T2SumCopy1, T3SumCopy1, T4SumCopy1
          TSumCopy1 = []
          # define an empty list to save the T1SumCopy2, T2SumCopy2, T3SumCopy2, T4SumCopy2
          TSumCopy2 = []

          # loop the particles in each events
          for particle in event:
              # distinguish the final state particles
              if particle.status == 1:
                  # save the particle ID in a list
                  PidList.append(particle.pid)
          # calculate the absolute values of PidList
          for Pid in PidList:
              AbsPidList.append(abs(Pid))
    
          # choose the special final state which needn't 4 possibilities, [13, -13, 11, -11]
          if sorted(AbsPidList, reverse=True) == [13, 13, 11, 11]:
              # list all the possible particle pairs
              if PidList[0] == -PidList[1]:
                  PidPair1 = [0, 1]
                  PidPair2 = [2, 3]
                  PidPair3 = []
                  PidPair4 = []
              elif PidList[0] == -PidList[2]:
                  PidPair1 = [0, 2]
                  PidPair2 = [1, 3]
                  PidPair3 = []
                  PidPair4 = []
              elif PidList[0] == -PidList[3]:
                  PidPair1 = [0, 3]
                  PidPair2 = [1, 2]
                  PidPair3 = []
                  PidPair4 = []
              # calculate the TLorentzVector and their sum of each possible pairs
              for particle in event:
                  if particle.status == 1:
                      if ParticleCount1 in PidPair1:
                          p1 = FourMomentum(particle)
                          T1.append(R.TLorentzVector())
                          T1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                          T1Sum += T1[PidCount1]

                          # define some copies of T1 to use class boost
                          T1Copy1.append(R.TLorentzVector())
                          T1Copy1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                          T1SumCopy1 += T1Copy1[PidCount1]

                          T1Copy2.append(R.TLorentzVector())
                          T1Copy2[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)            
                          T1SumCopy2 += T1Copy2[PidCount1]

                          PidCount1 += 1
                          ParticleCount1 += 1
                      elif ParticleCount1 in PidPair2:
                          p2 = FourMomentum(particle)
                          T2.append(R.TLorentzVector())
                          T2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                          T2Sum += T2[PidCount2]

                          # define some copies of T2 to use class boost
                          T2Copy1.append(R.TLorentzVector())
                          T2Copy1[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)            
                          T2SumCopy1 += T2Copy1[PidCount2]
                          
                          T2Copy2.append(R.TLorentzVector())
                          T2Copy2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                          T2SumCopy2 += T2Copy2[PidCount2]

                          PidCount2 += 1
                          ParticleCount1 += 1
    
          # choose the other final states which need 4 possibilities, [11, -11, 11, -11] and [13, -13, 13, -13]
          else:
              # list all the possible particle pairs
              if PidList[0] == -PidList[1]:
                  PidPair1 = [0, 1]
                  PidPair2 = [2, 3]
                  if PidList[0] == -PidList[2]:
                      PidPair3 = [0, 2]
                      PidPair4 = [1, 3]
                  else:
                      PidPair3 = [0, 3]
                      PidPair4 = [1, 2]
              else:
                  PidPair1 = [0, 2]
                  PidPair2 = [1, 3]
                  PidPair3 = [0, 3]
                  PidPair4 = [1, 2]
              # calculate the TLorentzVector and their sum of each possible pairs
              for particle in event:
                  if particle.status == 1:
                      if ParticleCount1 in PidPair1:
                          p1 = FourMomentum(particle)
                          T1.append(R.TLorentzVector())
                          T1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                          T1Sum += T1[PidCount1]

                          # define some copies of T1 to use class boost
                          T1Copy1.append(R.TLorentzVector())
                          T1Copy1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)            
                          T1SumCopy1 += T1Copy1[PidCount1]
                          
                          T1Copy2.append(R.TLorentzVector())
                          T1Copy2[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                          T1SumCopy2 += T1Copy2[PidCount1]

                          PidCount1 += 1
                      elif ParticleCount1 in PidPair2:
                          p2 = FourMomentum(particle)
                          T2.append(R.TLorentzVector())
                          T2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                          T2Sum += T2[PidCount2]
                          
                          # define some copies of T2 to use class boost
                          T2Copy1.append(R.TLorentzVector())
                          T2Copy1[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                          T2SumCopy1 += T2Copy1[PidCount2]

                          T2Copy2.append(R.TLorentzVector())
                          T2Copy2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                          T2SumCopy2 += T2Copy2[PidCount2]

                          PidCount2 += 1
                      # since each leptons were used twice to list all the possible pairs, do the "if" loop twice, too
                      if ParticleCount1 in PidPair3:
                          p3 = FourMomentum(particle)
                          T3.append(R.TLorentzVector())
                          T3[PidCount3].SetPxPyPzE(p3.px, p3.py, p3.pz, p3.E)
                          T3Sum += T3[PidCount3]
                          
                          # define some copies of T3 to use class boost
                          T3Copy1.append(R.TLorentzVector())
                          T3Copy1[PidCount3].SetPxPyPzE(p3.px, p3.py, p3.pz, p3.E)
                          T3SumCopy1 += T3Copy1[PidCount3]

                          T3Copy2.append(R.TLorentzVector())
                          T3Copy2[PidCount3].SetPxPyPzE(p3.px, p3.py, p3.pz, p3.E)
                          T3SumCopy2 += T3Copy2[PidCount3]

                          PidCount3 += 1
                          ParticleCount1 += 1
                      elif ParticleCount1 in PidPair4:
                          p4 = FourMomentum(particle)
                          T4.append(R.TLorentzVector())
                          T4[PidCount4].SetPxPyPzE(p4.px, p4.py, p4.pz, p4.E)
                          T4Sum += T4[PidCount4]

                          # define some copies of T4 to use class boost
                          T4Copy1.append(R.TLorentzVector())
                          T4Copy1[PidCount4].SetPxPyPzE(p4.px, p4.py, p4.pz, p4.E)
                          T4SumCopy1 += T4Copy1[PidCount4]

                          T4Copy2.append(R.TLorentzVector())
                          T4Copy2[PidCount4].SetPxPyPzE(p4.px, p4.py, p4.pz, p4.E)
                          T4SumCopy2 += T4Copy2[PidCount4]

                          PidCount4 += 1
                          ParticleCount1 += 1
    
          # calculate the deltam of each possible pairs
          deltam1 = abs(T1Sum.M()-Zmass)
          deltam2 = abs(T2Sum.M()-Zmass)
          deltam3 = abs(T3Sum.M()-Zmass)
          deltam4 = abs(T4Sum.M()-Zmass)
          # calculate the Z mass and save them in a list
          m = [T1Sum.M(), T2Sum.M(), T3Sum.M(), T4Sum.M()]
          # save the deltam in a list
          deltam = [deltam1, deltam2, deltam3, deltam4]
          # save the TLorentzVector in a list
          TSum = [T1Sum, T2Sum, T3Sum, T4Sum]
          # save the copy of TLorentzVector in a list
          TSumCopy1 = [T1SumCopy1, T2SumCopy1, T3SumCopy1, T4SumCopy1]
          # save the copy of TLorentzVector in a list
          TSumCopy2 = [T1SumCopy2, T2SumCopy2, T3SumCopy2, T4SumCopy2]

          """
          take care of this code block, I have misunderstood the function named "sorted", see its explanation at https://blog.csdn.net/qq1195365047/article/details/90295660
          """
          # Sort the deltam in the list from small to large, and save the sort index values
          deltamSorts = sorted(range(len(deltam)), key=lambda k: deltam[k])
    
          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # choose the Zmass which is closest to the real Zmass, fill it in the h_M1
              if i == 0:
                  # in order to use the address, change M1 to M1[0], the same below
                  M1[0] = m[deltamSort]
                  # list all the possible M2 and fill it in the h_M2
                  if deltamSort == 0:
                      M2[0] = m[1]
                  elif deltamSort == 1:
                      M2[0] = m[0]
                  elif deltamSort == 2:
                      M2[0] = m[3]
                  elif deltamSort == 3:
                      M2[0] = m[2]

          if InputFile == InputFile_Inclusive:
              h_M1.Fill(M1[0])
              h_M2.Fill(M2[0])
          elif InputFile == InputFile_TT:
              h_TTM1.Fill(M1[0])
              h_TTM2.Fill(M2[0])
          elif InputFile == InputFile_TL:
              h_TLM1.Fill(M1[0])
              h_TLM2.Fill(M2[0])
          elif InputFile == InputFile_LL:
              h_LLM1.Fill(M1[0])
              h_LLM2.Fill(M2[0])

          """
          calculate M4l
          """
          # define some initial values
          TM4l = R.TLorentzVector()
          # M4l = 0

          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # choose the Zmass which is closest to the real Zmass
              if i == 0:
                  # list all the possibilities and fill it in the h_M4l
                  if deltamSort == 0:
                      TM4l = TSum[deltamSort] + TSum[1]
                      M4l[0] = TM4l.M()
                  elif deltamSort == 1:
                      TM4l = TSum[deltamSort] + TSum[0]
                      M4l[0] = TM4l.M()
                  elif deltamSort == 2:
                      TM4l = TSum[deltamSort] + TSum[3]
                      M4l[0] = TM4l.M()
                  elif deltamSort == 3:
                      TM4l = TSum[deltamSort] + TSum[2]
                      M4l[0] = TM4l.M()

          if InputFile == InputFile_Inclusive:
              h_M4l.Fill(M4l[0])
          elif InputFile == InputFile_TT:
              h_TTM4l.Fill(M4l[0])
          elif InputFile == InputFile_TL:
              h_TLM4l.Fill(M4l[0])
          elif InputFile == InputFile_LL:
              h_LLM4l.Fill(M4l[0])



          """
          block of 8th function: histogram the Eta1, Eta2 and Eta4l
          """

          # define some initial values
          # Eta1, Eta2, Eta4l = 0, 0, 0
          TEta4l = R.TLorentzVector()
          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # choose the Zmass which is closest to the real Zmass, fill its eta in the h_Eta1
              if i == 0:
                  Eta1[0] = TSum[deltamSort].Eta()
                  # list all the possible Eta2 and fill it in the h_Eta2
                  # also calculated Eta4l, fill it in the h_Eta4l
                  if deltamSort == 0:
                      Eta2[0] = TSum[1].Eta()
                      TEta4l = TSum[deltamSort] + TSum[1]
                      Eta4l[0] = TEta4l.Eta()
                  elif deltamSort == 1:
                      Eta2[0] = TSum[0].Eta()
                      TEta4l = TSum[deltamSort] + TSum[0]
                      Eta4l[0] = TEta4l.Eta()
                  elif deltamSort == 2:
                      Eta2[0] = TSum[3].Eta()
                      TEta4l = TSum[deltamSort] + TSum[3]
                      Eta4l[0] = TEta4l.Eta()
                  elif deltamSort == 3:
                      Eta2[0] = TSum[2].Eta()
                      TEta4l = TSum[deltamSort] + TSum[2]
                      Eta4l[0] = TEta4l.Eta()

          if InputFile == InputFile_Inclusive:
              h_Eta1.Fill(Eta1[0])
              h_Eta2.Fill(Eta2[0])
              h_Eta4l.Fill(Eta4l[0])
          elif InputFile == InputFile_TT:
              h_TTEta1.Fill(Eta1[0])
              h_TTEta2.Fill(Eta2[0])
              h_TTEta4l.Fill(Eta4l[0])
          elif InputFile == InputFile_TL:
              h_TLEta1.Fill(Eta1[0])
              h_TLEta2.Fill(Eta2[0])
              h_TLEta4l.Fill(Eta4l[0])
          elif InputFile == InputFile_LL:
              h_LLEta1.Fill(Eta1[0])
              h_LLEta2.Fill(Eta2[0])
              h_LLEta4l.Fill(Eta4l[0])



          """
          block of 9th function: histogram the Pt1, Pt2 and Pt4l
          """

          # define some initial values
          # Pt1, Pt2, Pt4l = 0, 0, 0
          TPt4l = R.TLorentzVector()
          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # choose the Zmass which is closest to the real Zmass, fill its Pt in the h_Pt1
              if i == 0:
                  Pt1[0] = TSum[deltamSort].Pt()
                  # list all the possible Pt2 and fill it in the h_Pt2
                  # also calculated Pt4l, fill it in the h_Pt4l
                  if deltamSort == 0:
                      Pt2[0] = TSum[1].Pt()
                      TPt4l = TSum[deltamSort] + TSum[1]
                      Pt4l[0] = TPt4l.Pt()
                  elif deltamSort == 1:
                      Pt2[0] = TSum[0].Pt()
                      TPt4l = TSum[deltamSort] + TSum[0]
                      Pt4l[0] = TPt4l.Pt()
                  elif deltamSort == 2:
                      Pt2[0] = TSum[3].Pt()
                      TPt4l = TSum[deltamSort] + TSum[3]
                      Pt4l[0] = TPt4l.Pt()
                  elif deltamSort == 3:
                      Pt2[0] = TSum[2].Pt()
                      TPt4l = TSum[deltamSort] + TSum[2]
                      Pt4l[0] = TPt4l.Pt()

          if InputFile == InputFile_Inclusive:
              h_Pt1.Fill(Pt1[0])
              h_Pt2.Fill(Pt2[0])
              h_Pt4l.Fill(Pt4l[0])
          elif InputFile == InputFile_TT:
              h_TTPt1.Fill(Pt1[0])
              h_TTPt2.Fill(Pt2[0])
              h_TTPt4l.Fill(Pt4l[0])
          elif InputFile == InputFile_TL:
              h_TLPt1.Fill(Pt1[0])
              h_TLPt2.Fill(Pt2[0])
              h_TLPt4l.Fill(Pt4l[0])
          elif InputFile == InputFile_LL:
              h_LLPt1.Fill(Pt1[0])
              h_LLPt2.Fill(Pt2[0])
              h_LLPt4l.Fill(Pt4l[0])



          """
          block of 6th function: histogram the Phi
          Z1, lepZ1  => n1
          Z2, lepZ2  => n2
          n1, n2     => CosPhi
          """

          # define some initial values
          VectorZ1, VectorZ2, Vector1, Vector2 = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          Vectorlep1, Vectorlep2, VectorZ1Boosted, VectorZ2Boosted = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
          n1x, n1y, n1z, n2x, n2y, n2z = 0, 0, 0, 0, 0, 0
          n1 = R.TVector3()
          n2 = R.TVector3()
          # Phi, CosPhi = 0, 0
          # PhiCopy = 0


          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # find M1, and calculate the 1st normal vector
              if i == 0:
                  # Using "if" sytax to list all the possible deltaSort
                  if deltamSort == 0:
                      # find the TLorentzVector of the Z boson relate to M1
                      VectorZ1 = TSumCopy2[0]
                      VectorZ1Boosted = VectorZ1.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M1, I select the 1st one
                      Vector1 = T1Copy2[0]
                      Vectorlep1 = Vector1
                      Vectorlep1.Boost(-VectorZ1Boosted)

                      # find the TLorentzVector of the Z boson relate to M2
                      VectorZ2 = TSumCopy2[1]
                      VectorZ2Boosted = VectorZ2.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M2, I select the 1st one
                      Vector2 = T2Copy2[0]
                      Vectorlep2 = Vector2
                      Vectorlep2.Boost(-VectorZ2Boosted)

                  elif deltamSort == 1:
                      # find the TLorentzVector of the Z boson relate to M1
                      VectorZ1 = TSumCopy2[1]
                      VectorZ1Boosted = VectorZ1.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M1, I select the 1st one
                      Vector1 = T2Copy2[0]
                      Vectorlep1 = Vector1
                      Vectorlep1.Boost(-VectorZ1Boosted)

                      # find the TLorentzVector of the Z boson relate to M2
                      VectorZ2 = TSumCopy2[0]
                      VectorZ2Boosted = VectorZ2.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M2, I select the 1st one
                      Vector2 = T1Copy2[0]
                      Vectorlep2 = Vector2
                      Vectorlep2.Boost(-VectorZ2Boosted)

                  elif deltamSort == 2:
                      # find the TLorentzVector of the Z boson relate to M1
                      VectorZ1 = TSumCopy2[2]
                      VectorZ1Boosted = VectorZ1.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M1, I select the 1st one
                      Vector1 = T3Copy2[0]
                      Vectorlep1 = Vector1
                      Vectorlep1.Boost(-VectorZ1Boosted)

                      # find the TLorentzVector of the Z boson relate to M2
                      VectorZ2 = TSumCopy2[3]
                      VectorZ2Boosted = VectorZ2.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M2, I select the 1st one
                      Vector2 = T4Copy2[0]
                      Vectorlep2 = Vector2
                      Vectorlep2.Boost(-VectorZ2Boosted)

                  elif deltamSort == 3:
                      # find the TLorentzVector of the Z boson relate to M1
                      VectorZ1 = TSumCopy2[3]
                      VectorZ1Boosted = VectorZ1.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M1, I select the 1st one
                      Vector1 = T4Copy2[0]
                      Vectorlep1 = Vector1
                      Vectorlep1.Boost(-VectorZ1Boosted)

                      # find the TLorentzVector of the Z boson relate to M2
                      VectorZ2 = TSumCopy2[2]
                      VectorZ2Boosted = VectorZ2.BoostVector()
                      # arbitrarily using one of 2 leptons which rebuilt the M2, I select the 1st one
                      Vector2 = T3Copy2[0]
                      Vectorlep2 = Vector2
                      Vectorlep2.Boost(-VectorZ2Boosted)


          # get the X, Y, Z of the TLorentzVector
          x1 = VectorZ1.X()
          y1 = VectorZ1.Y()
          z1 = VectorZ1.Z()
          x2 = Vectorlep1.X()
          y2 = Vectorlep1.Y()
          z2 = Vectorlep1.Z()
          # calculate the normal vector of the M1 plane, set the n1z = 1
          n1x = (z2*y1 - z1*y2)/(x1*y2 - x2*y1)
          n1y = (z2*x1 - z1*x2)/(x2*y1 - x1*y2)
          n1z = 1
          # Using SetXYZ to set the X, Y, Z of the normal vector
          n1.SetXYZ(n1x, n1y, n1z)
 
          # get the X, Y, Z of the TLorentzVector
          x3 = VectorZ2.X()
          y3 = VectorZ2.Y()
          z3 = VectorZ2.Z()
          x4 = Vectorlep2.X()
          y4 = Vectorlep2.Y()
          z4 = Vectorlep2.Z()
          # calculate the normal vector of the M2 plane, set the n2z = 1
          n2x = (z4*y3 - z3*y4)/(x3*y4 - x4*y3)
          n2y = (z4*x3 - z3*x4)/(x4*y3 - x3*y4)
          n2z = 1
          # Using SetXYZ to set the X, Y, Z of the normal vector
          n2.SetXYZ(n2x, n2y, n2z)

          # Calculate the Phi and CosPhi
          Phi = n1.Angle(n2)

          # Since the Phi is the angle between 2 plane, I calculate its alsolute value
          CosPhi[0] = abs(math.cos(Phi))

          if InputFile == InputFile_Inclusive:
              h_CosPhi.Fill(CosPhi[0])
          elif InputFile == InputFile_TT:
              h_TTCosPhi.Fill(CosPhi[0])
          elif InputFile == InputFile_TL:
              h_TLCosPhi.Fill(CosPhi[0])
          elif InputFile == InputFile_LL:
              h_LLCosPhi.Fill(CosPhi[0])

          # Also draw the hisgtogram of Phi, since the Phi is the angle between 2 plane, I always use the angle smaller than PiOver2
          # Since when Phi larger than PiOver2, I should change its value, I define a value named as "PhiCopy" to save it
          PhiCopy[0] = Phi
          if PhiCopy[0] > R.TMath.PiOver2():
              PhiCopy[0] = R.TMath.Pi() - PhiCopy[0]
          if InputFile == InputFile_Inclusive:
              h_Phi.Fill(PhiCopy[0])
          elif InputFile == InputFile_TT:
              h_TTPhi.Fill(PhiCopy[0])
          elif InputFile == InputFile_TL:
              h_TLPhi.Fill(PhiCopy[0])
          elif InputFile == InputFile_LL:
              h_LLPhi.Fill(PhiCopy[0])



          """
          block of 7th function: histogram the Phi1
          Z1, lep1 => n1 (already calculated in 6th block, n1 = (n1x, n1y, n1z))
          Z1, p    => n3 (Z1 = (x1, y1, z1), p = (0, 0, 1))
          n1, n3   => CosPhi1
          """

          # define some initial values
          n3x, n3y, n3z = 0, 0, 0
          n3 = R.TVector3()
          # Phi1, CosPhi1 = 0, 0

          # calculate the normal vector of the ZZ' plane
          n3x = -y1/x1
          n3y = 1
          n3z = 0
          # Using SetXYZ to set the X, Y, Z of the normal vector
          n3.SetXYZ(n3x, n3y, n3z)
          # Calculate the Phi and CosPhi
          Phi1 = n1.Angle(n3)
          # Since the Phi1 is the angle between 2 plane, I calculate its alsolute value
          CosPhi1[0] = abs(math.cos(Phi1))

          if InputFile == InputFile_Inclusive:
              h_CosPhi1.Fill(CosPhi1[0])
          elif InputFile == InputFile_TT:
              h_TTCosPhi1.Fill(CosPhi1[0])
          elif InputFile == InputFile_TL:
              h_TLCosPhi1.Fill(CosPhi1[0])
          elif InputFile == InputFile_LL:
              h_LLCosPhi1.Fill(CosPhi1[0])

          # Also draw the hisgtogram of Phi1, since the Phi1 is the angle between 2 plane, I always use the angle smaller than PiOver2
          # Since when Phi1 larger than PiOver2, I should change its value, I define a value named as "Phi1Copy" to save it
          Phi1Copy[0] = Phi1
          if Phi1Copy[0] > R.TMath.PiOver2():
              Phi1Copy[0] = R.TMath.Pi() - Phi1Copy[0]
          if InputFile == InputFile_Inclusive:
              h_Phi1.Fill(Phi1Copy[0])
          elif InputFile == InputFile_TT:
              h_TTPhi1.Fill(Phi1Copy[0])
          elif InputFile == InputFile_TL:
              h_TLPhi1.Fill(Phi1Copy[0])
          elif InputFile == InputFile_LL:
              h_LLPhi1.Fill(Phi1Copy[0])



          """
          block of 5th function: histogram the ThetaStar1 and ThetaStar2
          """
          # define some initial values
          # define 2 initial values to save the ThetaStar, "ThetaStar1" means the ThetaStar is calculated from M1, and "ThetaStar2" means the ThetaStar is calculated from M2
          # define 2 initial values to save the CosThetaStar
          # ThetaStar1, ThetaStar2, CosThetaStar1, CosThetaStar2 = 0, 0, 0, 0
          # loop the deltamSorts, find "0", which represents the closest Z mass
          for i, deltamSort in enumerate(deltamSorts):
              # find M1, and calculate the ThetaStar
              if i == 0:
                  ThetaStar1[0] = TSum[deltamSort].Phi()
                  # find M2, and calculate the ThetaStar
                  if deltamSort == 0:
                      ThetaStar2[0] = TSum[1].Phi()
                  elif deltamSort == 1:
                      ThetaStar2[0] = TSum[0].Phi()
                  elif deltamSort == 2:
                      ThetaStar2[0] = TSum[3].Phi()
                  elif deltamSort == 3:
                      ThetaStar2[0] = TSum[2].Phi()
          # calculate the Cosin of ThetaStar1 and ThetaStar2
          CosThetaStar1[0] = math.cos(ThetaStar1[0])
          CosThetaStar2[0] = math.cos(ThetaStar2[0])

          if InputFile == InputFile_Inclusive:
              h_CosThetaStar1.Fill(CosThetaStar1[0])
              h_CosThetaStar2.Fill(CosThetaStar2[0])
              h_ThetaStar1.Fill(ThetaStar1[0])
              h_ThetaStar2.Fill(ThetaStar2[0])
          elif InputFile == InputFile_TT:
              h_TTCosThetaStar1.Fill(CosThetaStar1[0])
              h_TTCosThetaStar2.Fill(CosThetaStar2[0])
              h_TTThetaStar1.Fill(ThetaStar1[0])
              h_TTThetaStar2.Fill(ThetaStar2[0])
          elif InputFile == InputFile_TL:
              h_TLCosThetaStar1.Fill(CosThetaStar1[0])
              h_TLCosThetaStar2.Fill(CosThetaStar2[0])
              h_TLThetaStar1.Fill(ThetaStar1[0])
              h_TLThetaStar2.Fill(ThetaStar2[0])
          elif InputFile == InputFile_LL:
              h_LLCosThetaStar1.Fill(CosThetaStar1[0])
              h_LLCosThetaStar2.Fill(CosThetaStar2[0])
              h_LLThetaStar1.Fill(ThetaStar1[0])
              h_LLThetaStar2.Fill(ThetaStar2[0])



          """
          block of 4th function: histogram the theta1 and theta2
          """
          # define 4 initial values to save the boosted sum TLorentzVector of 4 possible lepton pairs
          T1SumBoosted, T2SumBoosted, T3SumBoosted, T4SumBoosted = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          # define an empty list to save all the boosted sum TLorentzVectors
          TSumBoosted = []
          # define 4 initial values to save the TLorentzVector of 4 leptons in each possible final states
          TM1_1st, TM1_2ed, TM2_1st, TM2_2ed = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
          # define 4 initial values to save the TLorentzVector to calculate the final boost
          # TM1 and TM2 represent the TLorentzVector of single e and single mu in each pair leptons in 4 leptons, TM3 and TM4 represent the others
          TM1, TM2 = R.TLorentzVector(), R.TLorentzVector()
          # define 4 initial values to save the cos of each leptons, Cos1 and Cos2 represents 1 e and 1 mu, Cos3 and Cos4 represents the others
          # CosTheta1, CosTheta2 = 0, 0
          # Theta1, Theta2 = 0, 0
          # boost the TLorentzVector of 4 possible lepton pairs, which were obtained in the block of 1st function
          T1SumBoosted = T1SumCopy1.BoostVector()
          T2SumBoosted = T2SumCopy1.BoostVector()
          T3SumBoosted = T3SumCopy1.BoostVector()
          T4SumBoosted = T4SumCopy1.BoostVector()
          # save the 4 possible boosted TLorentzVector in a list named as "TSumBoosted"
          TSumBoosted = [T1SumBoosted, T2SumBoosted, T3SumBoosted, T4SumBoosted]
          # find the sorts of M1 and M2, using "deltamSorts" which is defined in the block of 1st function
          for i, deltamSort in enumerate(deltamSorts):
              # choose the Boosted TLorentzVector of M1, named it as "TSumBoostM1"
              if i == 0:
                  TSumBoostM1 = TSumBoosted[deltamSort]
                  # list all the possible sort of M1 by using "if" and "elif" first, then list all the possible pairs for each possible sort of M1
                  if deltamSort == 0:
                      # when deltamSort is 0, it represents that M1 is rebuilt from the 1st pair of leptons, so M2 would be rebuilt from the 2ed pair
                      # Name the leptons in 1st pair as "TM1_1st" and "TM1_2ed", the leptons in 2ed pair as "TM2_1st" and "TM2_2ed"
                      TM1_1st = T1Copy1[0]
                      TM1_2ed = T1Copy1[1]
                      TM2_1st = T2Copy1[0]
                      TM2_2ed = T2Copy1[1]
                  elif deltamSort == 1:
                      # when deltamSort is 1, it represents that M1 is rebuilt from the 2ed pair of leptons, so M2 would be rebuilt from the 1st pair
                      TM1_1st = T2Copy1[0]
                      TM1_2ed = T2Copy1[1]
                      TM2_1st = T1Copy1[0]
                      TM2_2ed = T1Copy1[1]
                  elif deltamSort == 2:
                      # when deltamSort is 2, it represents that M1 is rebuilt from the 3rd pair of leptons, so M2 would be rebuilt from the 4th pair
                      TM1_1st = T3Copy1[0]
                      TM1_2ed = T3Copy1[1]
                      TM2_1st = T4Copy1[0]
                      TM2_2ed = T4Copy1[1]
                  elif deltamSort == 3:
                      # when deltamSort is 3, it represents that M1 is rebuilt from the 4th pair of leptons, so M2 would be rebuilt from the 3rd pair
                      TM1_1st = T4Copy1[0]
                      TM1_2ed = T4Copy1[1]
                      TM2_1st = T3Copy1[0]
                      TM2_2ed = T3Copy1[1]
    
                  # list all the possible TSumBoostM2 for each possible M1 sort
                  if deltamSort == 0:
                      TSumBoostM2 = TSumBoosted[1]
                  elif deltamSort == 1:
                      TSumBoostM2 = TSumBoosted[0]
                  elif deltamSort == 2:
                      TSumBoostM2 = TSumBoosted[3]
                  elif deltamSort == 3:
                      TSumBoostM2 = TSumBoosted[2]
          TM1 = TM1_1st
          TM1.Boost(-TSumBoostM1)
          TM2 = TM2_1st
          TM2.Boost(-TSumBoostM2)
          CosTheta1[0] = TM1.CosTheta()
          CosTheta2[0] = TM2.CosTheta()
          Theta1[0] = R.TMath.ACos(CosTheta1[0])
          Theta2[0] = R.TMath.ACos(CosTheta2[0])

          if InputFile == InputFile_Inclusive:
              h_CosTheta1.Fill(CosTheta1[0])
              h_CosTheta2.Fill(CosTheta2[0])
              h_Theta1.Fill(Theta1[0])
              h_Theta2.Fill(Theta2[0])
          elif InputFile == InputFile_TT:
              h_TTCosTheta1.Fill(CosTheta1[0])
              h_TTCosTheta2.Fill(CosTheta2[0])
              h_TTTheta1.Fill(Theta1[0])
              h_TTTheta2.Fill(Theta2[0])
          elif InputFile == InputFile_TL:
              h_TLCosTheta1.Fill(CosTheta1[0])
              h_TLCosTheta2.Fill(CosTheta2[0])
              h_TLTheta1.Fill(Theta1[0])
              h_TLTheta2.Fill(Theta2[0])
          elif InputFile == InputFile_LL:
              h_LLCosTheta1.Fill(CosTheta1[0])
              h_LLCosTheta2.Fill(CosTheta2[0])
              h_LLTheta1.Fill(Theta1[0])
              h_LLTheta2.Fill(Theta2[0])



          """
          block of 2ed function: histogram the M1MOTHUP and M2MOTHUP
          """
    
          # define some initial values
          # define a list named as "Mother" to save the mother particles of final state particles.
          Mother = []
          # define a list named as "Mother1Index" and "Mother2Index" to save the index of 1st pair and 2ed pair of mother particles of final state particles.
          Mother1Index, Mother2Index = [], []
          # creat 2 empty lists of TLorentzVector to save the TLorentzVector of 2 pairs of leptons
          T1MOTHUP, T2MOTHUP = [], []
          # creat 2 empty TLorentzVectors of the sum of each pair of leptons
          T1MOTHUPSum, T2MOTHUPSum = R.TLorentzVector(), R.TLorentzVector()
          # define 2 initial values named as "MotherCount1" and"MotherCount2" to count the leptons in each pairs
          MotherCount1, MotherCount2 = 0, 0
          # define an initial value to count the particles in each event, "2" represents that it is the count of 2ed function block
          ParticleCount2 = 0
          # define 2 initial values named as "M1MOTHUP1", "M2MOTHUP" to save the Zmass which is rebuilt from leptons using MOTHUP. "M1" represent the closer one, "M2" is the another
          # M1MOTHUP, M2MOTHUP = 0, 0
          # loop the particles in each events
          for particle in event:
              # distinguish the final state particles
              if particle.status == 1:
                  # save the mother of each leptons in the list named "Mother"
                  Mother.append(particle.mother1)
          # find the index of the leptons which have same mother with the first lepton, regard this mother is the 1st mother, another is the 2ed.
          Mother1Index = [x for (x,m) in enumerate(Mother) if m==Mother[0] ]
          if Mother[1] == Mother[0]:
              Mother2Index = [2, 3]
          elif Mother[2] == Mother[0]:
              Mother2Index = [1, 3]
          elif Mother[3] == Mother[0]:
              Mother2Index = [1, 2]
    
          for particle in event:
              if particle.status == 1:
                  if ParticleCount2 in Mother1Index:
                      # create an empty TLorentzVector class for each selected particles
                      T1MOTHUP.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p1MOTHUP = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T1MOTHUP[MotherCount1].SetPxPyPzE(p1MOTHUP.px, p1MOTHUP.py, p1MOTHUP.pz, p1MOTHUP.E)
                      T1MOTHUPSum += T1MOTHUP[MotherCount1]
                      MotherCount1 += 1
                      ParticleCount2 += 1
                  elif ParticleCount2 in Mother2Index:
                      # create an empty TLorentzVector class for each selected particles
                      T2MOTHUP.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p2MOTHUP = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T2MOTHUP[MotherCount2].SetPxPyPzE(p2MOTHUP.px, p2MOTHUP.py, p2MOTHUP.pz, p2MOTHUP.E)
                      T2MOTHUPSum += T2MOTHUP[MotherCount2]
                      MotherCount2 += 1
                      ParticleCount2 += 1
    
    
          if abs(T1MOTHUPSum.M() - Zmass) > abs(T2MOTHUPSum.M() - Zmass):
              M1MOTHUP[0] = T2MOTHUPSum.M()
              M2MOTHUP[0] = T1MOTHUPSum.M()
          else:
              M1MOTHUP[0] = T1MOTHUPSum.M()
              M2MOTHUP[0] = T2MOTHUPSum.M()

          if InputFile == InputFile_Inclusive:
              h_M1MOTHUP.Fill(M1MOTHUP[0])
              h_M2MOTHUP.Fill(M2MOTHUP[0])



          """
          block of 3rd function: find the correct pair and the wrong pair, count it and calculate the accuracy
          """
          if M1MOTHUP == M1 and M2MOTHUP == M2:
              CorrectPair += 1
          else:
              WrongPair += 1



          """
          block of 10th function: fill the tree
          """
          if InputFile == InputFile_Inclusive:
              InclusiveTree.Fill()
          elif InputFile == InputFile_TT:
              TTTree.Fill()
              TTTLTree.Fill()
          elif InputFile == InputFile_TL:
              TLTree.Fill()
              TTTLTree.Fill()
          elif InputFile == InputFile_LL:
              LLTree.Fill()


  print("CorrectPair", CorrectPair)
  print("WrongPair", WrongPair)
  SumPair = CorrectPair + WrongPair
  # Using function float() to  make sure that the result is a decimal
  Accuracy = float(CorrectPair)/float(SumPair)
  print("Accuracy", '%.2f%%' % (Accuracy * 100))


  # write the rootfile and close it
  InclusiveTreeFile.Write()
  InclusiveTreeFile.Close()
  TTTreeFile.Write()
  TTTreeFile.Close()
  TLTreeFile.Write()
  TLTreeFile.Close()
  LLTreeFile.Write()
  LLTreeFile.Close()
  TTTLTreeFile.Write()
  TTTLTreeFile.Close()

  # creat a ROOT file to histogram
  tfout = R.TFile("KinematicQuantity_v2.root", "RECREATE")
  tfout.cd()

  h_M1.Write()
  h_M2.Write()
  h_TTM1.Write()
  h_TTM2.Write()
  h_TLM1.Write()
  h_TLM2.Write()
  h_LLM1.Write()
  h_LLM2.Write()
  h_M1MOTHUP.Write()
  h_M2MOTHUP.Write()

  h_CosTheta1.Write()
  h_CosTheta2.Write()
  h_TTCosTheta1.Write()
  h_TTCosTheta2.Write()
  h_TLCosTheta1.Write()
  h_TLCosTheta2.Write()
  h_LLCosTheta1.Write()
  h_LLCosTheta2.Write()

  h_Theta1.Write()
  h_Theta2.Write()
  h_TTTheta1.Write()
  h_TTTheta2.Write()
  h_TLTheta1.Write()
  h_TLTheta2.Write()
  h_LLTheta1.Write()
  h_LLTheta2.Write()

  h_ThetaStar1.Write()
  h_ThetaStar2.Write()
  h_TTThetaStar1.Write()
  h_TTThetaStar2.Write()
  h_TLThetaStar1.Write()
  h_TLThetaStar2.Write()
  h_LLThetaStar1.Write()
  h_LLThetaStar2.Write()

  h_CosThetaStar1.Write()
  h_CosThetaStar2.Write()
  h_TTCosThetaStar1.Write()
  h_TTCosThetaStar2.Write()
  h_TLCosThetaStar1.Write()
  h_TLCosThetaStar2.Write()
  h_LLCosThetaStar1.Write()
  h_LLCosThetaStar2.Write()

  h_Phi.Write()
  h_TTPhi.Write()
  h_TLPhi.Write()
  h_LLPhi.Write()

  h_CosPhi.Write()
  h_TTCosPhi.Write()
  h_TLCosPhi.Write()
  h_LLCosPhi.Write()

  h_Phi1.Write()
  h_TTPhi1.Write()
  h_TLPhi1.Write()
  h_LLPhi1.Write()

  h_CosPhi1.Write()
  h_TTCosPhi1.Write()
  h_TLCosPhi1.Write()
  h_LLCosPhi1.Write()

  h_Eta1.Write()
  h_Eta2.Write()
  h_Eta4l.Write()
  h_TTEta1.Write()
  h_TTEta2.Write()
  h_TTEta4l.Write()
  h_TLEta1.Write()
  h_TLEta2.Write()
  h_TLEta4l.Write()
  h_LLEta1.Write()
  h_LLEta2.Write()
  h_LLEta4l.Write()

  h_M4l.Write()
  h_TTM4l.Write()
  h_TLM4l.Write()
  h_LLM4l.Write()

  h_Pt1.Write()
  h_Pt2.Write()
  h_Pt4l.Write()
  h_TTPt1.Write()
  h_TTPt2.Write()
  h_TTPt4l.Write()
  h_TLPt1.Write()
  h_TLPt2.Write()
  h_TLPt4l.Write()
  h_LLPt1.Write()
  h_LLPt2.Write()
  h_LLPt4l.Write()

  tfout.Close()



if __name__ == "__main__":

  InputFileList = []

  InputFile_Inclusive = "/users/wuxingyu/Desktop/pp_to_ZZ_para_added/Events/run_01/unweighted_events.lhe.gz"
  InputFile_TT = "/users/wuxingyu/Desktop/pp_to_ZZ_TT/Events/run_01/unweighted_events.lhe.gz"
  InputFile_TL = "/users/wuxingyu/Desktop/pp_to_ZZ_TL/Events/run_01/unweighted_events.lhe.gz"
  InputFile_LL = "/users/wuxingyu/Desktop/pp_to_ZZ_LL/Events/run_01/unweighted_events.lhe.gz"

  InputFileList = [InputFile_Inclusive, InputFile_TT, InputFile_TL, InputFile_LL]

  read_lhe(InputFileList=InputFileList)



