#!/usr/bin/env python

# import some modules
import sys, os
# import ROOT, creat an alias
import ROOT as R

def plot(InputROOTFile):

  rootfile = R.TFile.Open(InputROOTFile)

  # loop all objects of the root file and print them
  for key in rootfile.GetListOfKeys():
    key.Print()



  """
  Get all the histogram in the root file
  """

  h_M1 = rootfile.Get("M1")
  h_M2 = rootfile.Get("M2")
  h_M1MOTHUP = rootfile.Get("M1MOTHUP")
  h_M2MOTHUP = rootfile.Get("M2MOTHUP")

  h_TTM1 = rootfile.Get("TTM1")
  h_TTM2 = rootfile.Get("TTM2")
  h_TLM1 = rootfile.Get("TLM1")
  h_TLM2 = rootfile.Get("TLM2")
  h_LLM1 = rootfile.Get("LLM1")
  h_LLM2 = rootfile.Get("LLM2")

  h_CosTheta1 = rootfile.Get("CosTheta1")
  h_CosTheta2 = rootfile.Get("CosTheta2")

  h_TTCosTheta1 = rootfile.Get("TTCosTheta1")
  h_TTCosTheta2 = rootfile.Get("TTCosTheta2")
  h_TLCosTheta1 = rootfile.Get("TLCosTheta1")
  h_TLCosTheta2 = rootfile.Get("TLCosTheta2")
  h_LLCosTheta1 = rootfile.Get("LLCosTheta1")
  h_LLCosTheta2 = rootfile.Get("LLCosTheta2")

  h_Theta1 = rootfile.Get("Theta1")
  h_Theta2 = rootfile.Get("Theta2")

  h_TTTheta1 = rootfile.Get("TTTheta1")
  h_TTTheta2 = rootfile.Get("TTTheta2")
  h_TLTheta1 = rootfile.Get("TLTheta1")
  h_TLTheta2 = rootfile.Get("TLTheta2")
  h_LLTheta1 = rootfile.Get("LLTheta1")
  h_LLTheta2 = rootfile.Get("LLTheta2")

  h_ThetaStar1 = rootfile.Get("ThetaStar1")
  h_ThetaStar2 = rootfile.Get("ThetaStar2")
  h_TTThetaStar1 = rootfile.Get("TTThetaStar1")
  h_TTThetaStar2 = rootfile.Get("TTThetaStar2")
  h_TLThetaStar1 = rootfile.Get("TLThetaStar1")
  h_TLThetaStar2 = rootfile.Get("TLThetaStar2")
  h_LLThetaStar1 = rootfile.Get("LLThetaStar1")
  h_LLThetaStar2 = rootfile.Get("LLThetaStar2")

  h_CosThetaStar1 = rootfile.Get("CosThetaStar1")
  h_CosThetaStar2 = rootfile.Get("CosThetaStar2")
  h_TTCosThetaStar1 = rootfile.Get("TTCosThetaStar1")
  h_TTCosThetaStar2 = rootfile.Get("TTCosThetaStar2")
  h_TLCosThetaStar1 = rootfile.Get("TLCosThetaStar1")
  h_TLCosThetaStar2 = rootfile.Get("TLCosThetaStar2")
  h_LLCosThetaStar1 = rootfile.Get("LLCosThetaStar1")
  h_LLCosThetaStar2 = rootfile.Get("LLCosThetaStar2")

  h_Phi = rootfile.Get("Phi")
  h_TTPhi = rootfile.Get("TTPhi")
  h_TLPhi = rootfile.Get("TLPhi")
  h_LLPhi = rootfile.Get("LLPhi")

  h_CosPhi = rootfile.Get("CosPhi")
  h_TTCosPhi = rootfile.Get("TTCosPhi")
  h_TLCosPhi = rootfile.Get("TLCosPhi")
  h_LLCosPhi = rootfile.Get("LLCosPhi")

  h_Phi1 = rootfile.Get("Phi1")
  h_TTPhi1 = rootfile.Get("TTPhi1")
  h_TLPhi1 = rootfile.Get("TLPhi1")
  h_LLPhi1 = rootfile.Get("LLPhi1")

  h_CosPhi1 = rootfile.Get("CosPhi1")
  h_TTCosPhi1 = rootfile.Get("TTCosPhi1")
  h_TLCosPhi1 = rootfile.Get("TLCosPhi1")
  h_LLCosPhi1 = rootfile.Get("LLCosPhi1")

  h_M4l = rootfile.Get("M4l")
  h_TTM4l = rootfile.Get("TTM4l")
  h_TLM4l = rootfile.Get("TLM4l")
  h_LLM4l = rootfile.Get("LLM4l")

  h_Eta1 = rootfile.Get("Eta1")
  h_Eta2 = rootfile.Get("Eta2")
  h_Eta4l = rootfile.Get("Eta4l")
  h_TTEta1 = rootfile.Get("TTEta1")
  h_TTEta2 = rootfile.Get("TTEta2")
  h_TTEta4l = rootfile.Get("TTEta4l")
  h_TLEta1 = rootfile.Get("TLEta1")
  h_TLEta2 = rootfile.Get("TLEta2")
  h_TLEta4l = rootfile.Get("TLEta4l")
  h_LLEta1 = rootfile.Get("LLEta1")
  h_LLEta2 = rootfile.Get("LLEta2")
  h_LLEta4l = rootfile.Get("LLEta4l")

  h_Pt1 = rootfile.Get("Pt1")
  h_Pt2 = rootfile.Get("Pt2")
  h_Pt4l = rootfile.Get("Pt4l")
  h_TTPt1 = rootfile.Get("TTPt1")
  h_TTPt2 = rootfile.Get("TTPt2")
  h_TTPt4l = rootfile.Get("TTPt4l")
  h_TLPt1 = rootfile.Get("TLPt1")
  h_TLPt2 = rootfile.Get("TLPt2")
  h_TLPt4l = rootfile.Get("TLPt4l")
  h_LLPt1 = rootfile.Get("LLPt1")
  h_LLPt2 = rootfile.Get("LLPt2")
  h_LLPt4l = rootfile.Get("LLPt4l")


  """
  Remove the title of all histograms
  """

  h_M1.SetTitle("")
  h_M2.SetTitle("")
  h_M1MOTHUP.SetTitle("")
  h_M2MOTHUP.SetTitle("")

  h_TTM1.SetTitle("")
  h_TTM2.SetTitle("")
  h_TLM1.SetTitle("")
  h_TLM2.SetTitle("")
  h_LLM1.SetTitle("")
  h_LLM2.SetTitle("")

  h_CosTheta1.SetTitle("")
  h_CosTheta2.SetTitle("")

  h_TTCosTheta1.SetTitle("")
  h_TTCosTheta2.SetTitle("")
  h_TLCosTheta1.SetTitle("")
  h_TLCosTheta2.SetTitle("")
  h_LLCosTheta1.SetTitle("")
  h_LLCosTheta2.SetTitle("")

  h_Theta1.SetTitle("")
  h_Theta2.SetTitle("")

  h_TTTheta1.SetTitle("")
  h_TTTheta2.SetTitle("")
  h_TLTheta1.SetTitle("")
  h_TLTheta2.SetTitle("")
  h_LLTheta1.SetTitle("")
  h_LLTheta2.SetTitle("")

  h_ThetaStar1.SetTitle("")
  h_ThetaStar2.SetTitle("")
  h_TTThetaStar1.SetTitle("")
  h_TTThetaStar2.SetTitle("")
  h_TLThetaStar1.SetTitle("")
  h_TLThetaStar2.SetTitle("")
  h_LLThetaStar1.SetTitle("")
  h_LLThetaStar2.SetTitle("")

  h_CosThetaStar1.SetTitle("")
  h_CosThetaStar2.SetTitle("")
  h_TTCosThetaStar1.SetTitle("")
  h_TTCosThetaStar2.SetTitle("")
  h_TLCosThetaStar1.SetTitle("")
  h_TLCosThetaStar2.SetTitle("")
  h_LLCosThetaStar1.SetTitle("")
  h_LLCosThetaStar2.SetTitle("")

  h_Phi.SetTitle("")
  h_TTPhi.SetTitle("")
  h_TLPhi.SetTitle("")
  h_LLPhi.SetTitle("")

  h_CosPhi.SetTitle("")
  h_TTCosPhi.SetTitle("")
  h_TLCosPhi.SetTitle("")
  h_LLCosPhi.SetTitle("")

  h_Phi1.SetTitle("")
  h_TTPhi1.SetTitle("")
  h_TLPhi1.SetTitle("")
  h_LLPhi1.SetTitle("")
  
  h_CosPhi1.SetTitle("")
  h_TTCosPhi1.SetTitle("")
  h_TLCosPhi1.SetTitle("")
  h_LLCosPhi1.SetTitle("")

  h_M4l.SetTitle("")
  h_TTM4l.SetTitle("")
  h_TLM4l.SetTitle("")
  h_LLM4l.SetTitle("")

  h_Eta1.SetTitle("")
  h_Eta2.SetTitle("")
  h_Eta4l.SetTitle("")
  h_TTEta1.SetTitle("")
  h_TTEta2.SetTitle("")
  h_TTEta4l.SetTitle("")
  h_TLEta1.SetTitle("")
  h_TLEta2.SetTitle("")
  h_TLEta4l.SetTitle("")
  h_LLEta1.SetTitle("")
  h_LLEta2.SetTitle("")
  h_LLEta4l.SetTitle("")

  h_Pt1.SetTitle("")
  h_Pt2.SetTitle("")
  h_Pt4l.SetTitle("")
  h_TTPt1.SetTitle("")
  h_TTPt2.SetTitle("")
  h_TTPt4l.SetTitle("")
  h_TLPt1.SetTitle("")
  h_TLPt2.SetTitle("")
  h_TLPt4l.SetTitle("")
  h_LLPt1.SetTitle("")
  h_LLPt2.SetTitle("")
  h_LLPt4l.SetTitle("")


  """
  renormalize all the histograms, since the mass of M1 and M2 have underflow and overflow, add them to the 1st bin and last bin.
  """

  h_M1.Scale(0.02419*139*1000/1000000)
  h_M1.SetBinContent(1, h_M1.GetBinContent(0)+h_M1.GetBinContent(1))
  h_M1.SetBinContent(40, h_M1.GetBinContent(40)+h_M1.GetBinContent(41))

  h_M2.Scale(0.02419*139*1000/1000000)
  h_M2.SetBinContent(1, h_M2.GetBinContent(0)+h_M2.GetBinContent(1))
  h_M2.SetBinContent(40, h_M2.GetBinContent(40)+h_M2.GetBinContent(41))

  h_M1MOTHUP.Scale(0.02419*139*1000/1000000)
  h_M1MOTHUP.SetBinContent(1, h_M1MOTHUP.GetBinContent(0)+h_M1MOTHUP.GetBinContent(1))
  h_M1MOTHUP.SetBinContent(40, h_M1MOTHUP.GetBinContent(40)+h_M1MOTHUP.GetBinContent(41))

  h_M2MOTHUP.Scale(0.02419*139*1000/1000000)
  h_M2MOTHUP.SetBinContent(1, h_M2MOTHUP.GetBinContent(0)+h_M2MOTHUP.GetBinContent(1))
  h_M2MOTHUP.SetBinContent(40, h_M2MOTHUP.GetBinContent(40)+h_M2MOTHUP.GetBinContent(41))

  h_TTM1.Scale(0.01688*139*1000/1000000)
  h_TTM1.SetBinContent(1, h_TTM1.GetBinContent(0)+h_TTM1.GetBinContent(1))
  h_TTM1.SetBinContent(40, h_TTM1.GetBinContent(40)+h_TTM1.GetBinContent(41))

  h_TTM2.Scale(0.01688*139*1000/1000000)
  h_TTM2.SetBinContent(1, h_TTM2.GetBinContent(0)+h_TTM2.GetBinContent(1))
  h_TTM2.SetBinContent(40, h_TTM2.GetBinContent(40)+h_TTM2.GetBinContent(41))

  h_TLM1.Scale(0.005741*139*1000/1000000)
  h_TLM1.SetBinContent(1, h_TLM1.GetBinContent(0)+h_TLM1.GetBinContent(1))
  h_TLM1.SetBinContent(40, h_TLM1.GetBinContent(40)+h_TLM1.GetBinContent(41))

  h_TLM2.Scale(0.005741*139*1000/1000000)
  h_TLM2.SetBinContent(1, h_TLM2.GetBinContent(0)+h_TLM2.GetBinContent(1))
  h_TLM2.SetBinContent(40, h_TLM2.GetBinContent(40)+h_TLM2.GetBinContent(41))

  h_LLM1.Scale(0.001406*139*1000/1000000)
  h_LLM1.SetBinContent(1, h_LLM1.GetBinContent(0)+h_LLM1.GetBinContent(1))
  h_LLM1.SetBinContent(40, h_LLM1.GetBinContent(40)+h_LLM1.GetBinContent(41))

  h_LLM2.Scale(0.001406*139*1000/1000000)
  h_LLM2.SetBinContent(1, h_LLM2.GetBinContent(0)+h_LLM2.GetBinContent(1))
  h_LLM2.SetBinContent(40, h_LLM2.GetBinContent(40)+h_LLM2.GetBinContent(41))

  h_CosTheta1.Scale(0.02419*139*1000/1000000)
  h_CosTheta2.Scale(0.02419*139*1000/1000000)

  h_TTCosTheta1.Scale(0.01688*139*1000/1000000)
  h_TTCosTheta2.Scale(0.01688*139*1000/1000000)

  h_TLCosTheta1.Scale(0.005741*139*1000/1000000)
  h_TLCosTheta2.Scale(0.005741*139*1000/1000000)

  h_LLCosTheta1.Scale(0.001406*139*1000/1000000)
  h_LLCosTheta2.Scale(0.001406*139*1000/1000000)

  h_Theta1.Scale(0.02419*139*1000/1000000)
  h_Theta2.Scale(0.02419*139*1000/1000000)

  h_TTTheta1.Scale(0.01688*139*1000/1000000)
  h_TTTheta2.Scale(0.01688*139*1000/1000000)

  h_TLTheta1.Scale(0.005741*139*1000/1000000)
  h_TLTheta2.Scale(0.005741*139*1000/1000000)

  h_LLTheta1.Scale(0.001406*139*1000/1000000)
  h_LLTheta2.Scale(0.001406*139*1000/1000000)

  h_ThetaStar1.Scale(0.02419*139*1000/1000000)
  h_ThetaStar2.Scale(0.02419*139*1000/1000000)

  h_TTThetaStar1.Scale(0.01688*139*1000/1000000)
  h_TTThetaStar2.Scale(0.01688*139*1000/1000000)

  h_TLThetaStar1.Scale(0.005741*139*1000/1000000)
  h_TLThetaStar2.Scale(0.005741*139*1000/1000000)

  h_LLThetaStar1.Scale(0.001406*139*1000/1000000)
  h_LLThetaStar2.Scale(0.001406*139*1000/1000000)

  h_CosThetaStar1.Scale(0.02419*139*1000/1000000)
  h_CosThetaStar2.Scale(0.02419*139*1000/1000000)

  h_TTCosThetaStar1.Scale(0.01688*139*1000/1000000)
  h_TTCosThetaStar2.Scale(0.01688*139*1000/1000000)

  h_TLCosThetaStar1.Scale(0.005741*139*1000/1000000)
  h_TLCosThetaStar2.Scale(0.005741*139*1000/1000000)

  h_LLCosThetaStar1.Scale(0.001406*139*1000/1000000)
  h_LLCosThetaStar2.Scale(0.001406*139*1000/1000000)

  h_Phi.Scale(0.02419*139*1000/1000000)
  h_TTPhi.Scale(0.01688*139*1000/1000000)
  h_TLPhi.Scale(0.005741*139*1000/1000000)
  h_LLPhi.Scale(0.001406*139*1000/1000000)

  h_CosPhi.Scale(0.02419*139*1000/1000000)
  h_TTCosPhi.Scale(0.01688*139*1000/1000000)
  h_TLCosPhi.Scale(0.005741*139*1000/1000000)
  h_LLCosPhi.Scale(0.001406*139*1000/1000000)

  h_Phi1.Scale(0.02419*139*1000/1000000)
  h_TTPhi1.Scale(0.01688*139*1000/1000000)
  h_TLPhi1.Scale(0.005741*139*1000/1000000)
  h_LLPhi1.Scale(0.001406*139*1000/1000000)

  h_CosPhi1.Scale(0.02419*139*1000/1000000)
  h_TTCosPhi1.Scale(0.01688*139*1000/1000000)
  h_TLCosPhi1.Scale(0.005741*139*1000/1000000)
  h_LLCosPhi1.Scale(0.001406*139*1000/1000000)

  h_M4l.Scale(0.02419*139*1000/1000000)
  h_M4l.SetBinContent(1, h_M4l.GetBinContent(0)+h_M4l.GetBinContent(1))
  h_M4l.SetBinContent(40, h_M4l.GetBinContent(40)+h_M4l.GetBinContent(41))

  h_TTM4l.Scale(0.01688*139*1000/1000000)
  h_TTM4l.SetBinContent(1, h_TTM4l.GetBinContent(0)+h_TTM4l.GetBinContent(1))
  h_TTM4l.SetBinContent(40, h_TTM4l.GetBinContent(40)+h_TTM4l.GetBinContent(41))

  h_TLM4l.Scale(0.005741*139*1000/1000000)
  h_TLM4l.SetBinContent(1, h_TLM4l.GetBinContent(0)+h_TLM4l.GetBinContent(1))
  h_TLM4l.SetBinContent(40, h_TLM4l.GetBinContent(40)+h_TLM4l.GetBinContent(41))

  h_LLM4l.Scale(0.001406*139*1000/1000000)
  h_LLM4l.SetBinContent(1, h_LLM4l.GetBinContent(0)+h_LLM4l.GetBinContent(1))
  h_LLM4l.SetBinContent(40, h_LLM4l.GetBinContent(40)+h_LLM4l.GetBinContent(41))

  h_Eta1.Scale(0.02419*139*1000/1000000)
  h_Eta1.SetBinContent(1, h_Eta1.GetBinContent(0)+h_Eta1.GetBinContent(1))
  h_Eta1.SetBinContent(40, h_Eta1.GetBinContent(40)+h_Eta1.GetBinContent(41))

  h_TTEta1.Scale(0.01688*139*1000/1000000)
  h_TTEta1.SetBinContent(1, h_TTEta1.GetBinContent(0)+h_TTEta1.GetBinContent(1))
  h_TTEta1.SetBinContent(40, h_TTEta1.GetBinContent(40)+h_TTEta1.GetBinContent(41))

  h_TLEta1.Scale(0.005741*139*1000/1000000)
  h_TLEta1.SetBinContent(1, h_TLEta1.GetBinContent(0)+h_TLEta1.GetBinContent(1))
  h_TLEta1.SetBinContent(40, h_TLEta1.GetBinContent(40)+h_TLEta1.GetBinContent(41))

  h_LLEta1.Scale(0.001406*139*1000/1000000)
  h_LLEta1.SetBinContent(1, h_LLEta1.GetBinContent(0)+h_LLEta1.GetBinContent(1))
  h_LLEta1.SetBinContent(40, h_LLEta1.GetBinContent(40)+h_LLEta1.GetBinContent(41))

  h_Eta2.Scale(0.02419*139*1000/1000000)
  h_Eta2.SetBinContent(1, h_Eta2.GetBinContent(0)+h_Eta2.GetBinContent(1))
  h_Eta2.SetBinContent(40, h_Eta2.GetBinContent(40)+h_Eta2.GetBinContent(41))

  h_TTEta2.Scale(0.01688*139*1000/1000000)
  h_TTEta2.SetBinContent(1, h_TTEta2.GetBinContent(0)+h_TTEta2.GetBinContent(1))
  h_TTEta2.SetBinContent(40, h_TTEta2.GetBinContent(40)+h_TTEta2.GetBinContent(41))

  h_TLEta2.Scale(0.005741*139*1000/1000000)
  h_TLEta2.SetBinContent(1, h_TLEta2.GetBinContent(0)+h_TLEta2.GetBinContent(1))
  h_TLEta2.SetBinContent(40, h_TLEta2.GetBinContent(40)+h_TLEta2.GetBinContent(41))

  h_LLEta2.Scale(0.001406*139*1000/1000000)
  h_LLEta2.SetBinContent(1, h_LLEta2.GetBinContent(0)+h_LLEta2.GetBinContent(1))
  h_LLEta2.SetBinContent(40, h_LLEta2.GetBinContent(40)+h_LLEta2.GetBinContent(41))

  h_Eta4l.Scale(0.02419*139*1000/1000000)
  h_Eta4l.SetBinContent(1, h_Eta4l.GetBinContent(0)+h_Eta4l.GetBinContent(1))
  h_Eta4l.SetBinContent(40, h_Eta4l.GetBinContent(40)+h_Eta4l.GetBinContent(41))

  h_TTEta4l.Scale(0.01688*139*1000/1000000)
  h_TTEta4l.SetBinContent(1, h_TTEta4l.GetBinContent(0)+h_TTEta4l.GetBinContent(1))
  h_TTEta4l.SetBinContent(40, h_TTEta4l.GetBinContent(40)+h_TTEta4l.GetBinContent(41))

  h_TLEta4l.Scale(0.005741*139*1000/1000000)
  h_TLEta4l.SetBinContent(1, h_TLEta4l.GetBinContent(0)+h_TLEta4l.GetBinContent(1))
  h_TLEta4l.SetBinContent(40, h_TLEta4l.GetBinContent(40)+h_TLEta4l.GetBinContent(41))

  h_LLEta4l.Scale(0.001406*139*1000/1000000)
  h_LLEta4l.SetBinContent(1, h_LLEta4l.GetBinContent(0)+h_LLEta4l.GetBinContent(1))
  h_LLEta4l.SetBinContent(40, h_LLEta4l.GetBinContent(40)+h_LLEta4l.GetBinContent(41))

  h_Pt1.Scale(0.02419*139*1000/1000000)
  h_Pt1.SetBinContent(1, h_Pt1.GetBinContent(0)+h_Pt1.GetBinContent(1))
  h_Pt1.SetBinContent(40, h_Pt1.GetBinContent(40)+h_Pt1.GetBinContent(41))

  h_TTPt1.Scale(0.01688*139*1000/1000000)
  h_TTPt1.SetBinContent(1, h_TTPt1.GetBinContent(0)+h_TTPt1.GetBinContent(1))
  h_TTPt1.SetBinContent(40, h_TTPt1.GetBinContent(40)+h_TTPt1.GetBinContent(41))

  h_TLPt1.Scale(0.005741*139*1000/1000000)
  h_TLPt1.SetBinContent(1, h_TLPt1.GetBinContent(0)+h_TLPt1.GetBinContent(1))
  h_TLPt1.SetBinContent(40, h_TLPt1.GetBinContent(40)+h_TLPt1.GetBinContent(41))

  h_LLPt1.Scale(0.001406*139*1000/1000000)
  h_LLPt1.SetBinContent(1, h_LLPt1.GetBinContent(0)+h_LLPt1.GetBinContent(1))
  h_LLPt1.SetBinContent(40, h_LLPt1.GetBinContent(40)+h_LLPt1.GetBinContent(41))

  h_Pt2.Scale(0.02419*139*1000/1000000)
  h_Pt2.SetBinContent(1, h_Pt2.GetBinContent(0)+h_Pt2.GetBinContent(1))
  h_Pt2.SetBinContent(40, h_Pt2.GetBinContent(40)+h_Pt2.GetBinContent(41))

  h_TTPt2.Scale(0.01688*139*1000/1000000)
  h_TTPt2.SetBinContent(1, h_TTPt2.GetBinContent(0)+h_TTPt2.GetBinContent(1))
  h_TTPt2.SetBinContent(40, h_TTPt2.GetBinContent(40)+h_TTPt2.GetBinContent(41))

  h_TLPt2.Scale(0.005741*139*1000/1000000)
  h_TLPt2.SetBinContent(1, h_TLPt2.GetBinContent(0)+h_TLPt2.GetBinContent(1))
  h_TLPt2.SetBinContent(40, h_TLPt2.GetBinContent(40)+h_TLPt2.GetBinContent(41))

  h_LLPt2.Scale(0.001406*139*1000/1000000)
  h_LLPt2.SetBinContent(1, h_LLPt2.GetBinContent(0)+h_LLPt2.GetBinContent(1))
  h_LLPt2.SetBinContent(40, h_LLPt2.GetBinContent(40)+h_LLPt2.GetBinContent(41))

  h_Pt4l.Scale(0.02419*139*1000/1000000)
  h_Pt4l.SetBinContent(1, h_Pt4l.GetBinContent(0)+h_Pt4l.GetBinContent(1))
  h_Pt4l.SetBinContent(40, h_Pt4l.GetBinContent(40)+h_Pt4l.GetBinContent(41))

  h_TTPt4l.Scale(0.01688*139*1000/1000000)
  h_TTPt4l.SetBinContent(1, h_TTPt4l.GetBinContent(0)+h_TTPt4l.GetBinContent(1))
  h_TTPt4l.SetBinContent(40, h_TTPt4l.GetBinContent(40)+h_TTPt4l.GetBinContent(41))

  h_TLPt4l.Scale(0.005741*139*1000/1000000)
  h_TLPt4l.SetBinContent(1, h_TLPt4l.GetBinContent(0)+h_TLPt4l.GetBinContent(1))
  h_TLPt4l.SetBinContent(40, h_TLPt4l.GetBinContent(40)+h_TLPt4l.GetBinContent(41))

  h_LLPt4l.Scale(0.001406*139*1000/1000000)
  h_LLPt4l.SetBinContent(1, h_LLPt4l.GetBinContent(0)+h_LLPt4l.GetBinContent(1))
  h_LLPt4l.SetBinContent(40, h_LLPt4l.GetBinContent(40)+h_LLPt4l.GetBinContent(41))

  """
  Create h_AddXX to save the histogram of TT+TL+LL
  """

  nbins, xmin, xmax = 40, 80, 100
  h_AddM1 = R.TH1F("TT+TL+LLM1", "", nbins, xmin, xmax)
  h_AddM1.Add(h_TTM1, 1)
  h_AddM1.Add(h_TLM1, 1)
  h_AddM1.Add(h_LLM1, 1)

  nbins, xmin, xmax = 40, 70, 110
  h_AddM2 = R.TH1F("TT+TL+LLM2", "", nbins, xmin, xmax)
  h_AddM2.Add(h_TTM2, 1)
  h_AddM2.Add(h_TLM2, 1)
  h_AddM2.Add(h_LLM2, 1)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta1 = R.TH1F("TT+TL+LLCosTheta1", "", nbins, xmin, xmax)
  h_AddCosTheta1.Add(h_TTCosTheta1, 1)
  h_AddCosTheta1.Add(h_TLCosTheta1, 1)
  h_AddCosTheta1.Add(h_LLCosTheta1, 1)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta2 = R.TH1F("TT+TL+LLCosTheta2", "", nbins, xmin, xmax)
  h_AddCosTheta2.Add(h_TTCosTheta2, 1)
  h_AddCosTheta2.Add(h_TLCosTheta2, 1)
  h_AddCosTheta2.Add(h_LLCosTheta2, 1)

  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_AddTheta1 = R.TH1F("TT+TL+LLTheta1", "", nbins, xmin, xmax)
  h_AddTheta1.Add(h_TTTheta1, 1)
  h_AddTheta1.Add(h_TLTheta1, 1)
  h_AddTheta1.Add(h_LLTheta1, 1)

  nbins, xmin, xmax = 40, 0, R.TMath.Pi()
  h_AddTheta2 = R.TH1F("TT+TL+LLTheta2", "", nbins, xmin, xmax)
  h_AddTheta2.Add(h_TTTheta2, 1)
  h_AddTheta2.Add(h_TLTheta2, 1)
  h_AddTheta2.Add(h_LLTheta2, 1)

  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_AddThetaStar1 = R.TH1F("TT+TL+LLThetaStar1", "", nbins, xmin, xmax)
  h_AddThetaStar1.Add(h_TTThetaStar1, 1)
  h_AddThetaStar1.Add(h_TLThetaStar1, 1)
  h_AddThetaStar1.Add(h_LLThetaStar1, 1)

  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_AddThetaStar2 = R.TH1F("TT+TL+LLThetaStar2", "", nbins, xmin, xmax)
  h_AddThetaStar2.Add(h_TTThetaStar2, 1)
  h_AddThetaStar2.Add(h_TLThetaStar2, 1)
  h_AddThetaStar2.Add(h_LLThetaStar2, 1)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosThetaStar1 = R.TH1F("TT+TL+LLCosThetaStar1", "", nbins, xmin, xmax)
  h_AddCosThetaStar1.Add(h_TTCosThetaStar1, 1)
  h_AddCosThetaStar1.Add(h_TLCosThetaStar1, 1)
  h_AddCosThetaStar1.Add(h_LLCosThetaStar1, 1)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosThetaStar2 = R.TH1F("TT+TL+LLCosThetaStar2", "", nbins, xmin, xmax)
  h_AddCosThetaStar2.Add(h_TTCosThetaStar2, 1)
  h_AddCosThetaStar2.Add(h_TLCosThetaStar2, 1)
  h_AddCosThetaStar2.Add(h_LLCosThetaStar2, 1)

  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_AddPhi = R.TH1F("TT+TL+LLPhi", "", nbins, xmin, xmax)
  h_AddPhi.Add(h_TTPhi, 1)
  h_AddPhi.Add(h_TLPhi, 1)
  h_AddPhi.Add(h_LLPhi, 1)

  nbins, xmin, xmax = 40, 0, 1
  h_AddCosPhi = R.TH1F("TT+TL+LLCosPhi", "", nbins, xmin, xmax)
  h_AddCosPhi.Add(h_TTCosPhi, 1)
  h_AddCosPhi.Add(h_TLCosPhi, 1)
  h_AddCosPhi.Add(h_LLCosPhi, 1)

  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_AddPhi1 = R.TH1F("TT+TL+LLPhi1", "", nbins, xmin, xmax)
  h_AddPhi1.Add(h_TTPhi1, 1)
  h_AddPhi1.Add(h_TLPhi1, 1)
  h_AddPhi1.Add(h_LLPhi1, 1)

  nbins, xmin, xmax = 40, 0, 1
  h_AddCosPhi1 = R.TH1F("TT+TL+LLCosPhi1", "", nbins, xmin, xmax)
  h_AddCosPhi1.Add(h_TTCosPhi1, 1)
  h_AddCosPhi1.Add(h_TLCosPhi1, 1)
  h_AddCosPhi1.Add(h_LLCosPhi1, 1)

  nbins, xmin, xmax = 40, 150, 550
  h_AddM4l = R.TH1F("TT+TL+LLM4l", "", nbins, xmin, xmax)
  h_AddM4l.Add(h_TTM4l, 1)
  h_AddM4l.Add(h_TLM4l, 1)
  h_AddM4l.Add(h_LLM4l, 1)

  nbins, xmin, xmax = 40, -6, 6
  h_AddEta1 = R.TH1F("TT+TL+LLEta1", "", nbins, xmin, xmax)
  h_AddEta1.Add(h_TTEta1, 1)
  h_AddEta1.Add(h_TLEta1, 1)
  h_AddEta1.Add(h_LLEta1, 1)

  nbins, xmin, xmax = 40, -6, 6
  h_AddEta2 = R.TH1F("TT+TL+LLEta2", "", nbins, xmin, xmax)
  h_AddEta2.Add(h_TTEta2, 1)
  h_AddEta2.Add(h_TLEta2, 1)
  h_AddEta2.Add(h_LLEta2, 1)

  nbins, xmin, xmax = 40, -6, 6
  h_AddEta4l = R.TH1F("TT+TL+LLEta4l", "", nbins, xmin, xmax)
  h_AddEta4l.Add(h_TTEta4l, 1)
  h_AddEta4l.Add(h_TLEta4l, 1)
  h_AddEta4l.Add(h_LLEta4l, 1)

  nbins, xmin, xmax = 40, 0, 200
  h_AddPt1 = R.TH1F("TT+TL+LLPt1", "", nbins, xmin, xmax)
  h_AddPt1.Add(h_TTPt1, 1)
  h_AddPt1.Add(h_TLPt1, 1)
  h_AddPt1.Add(h_LLPt1, 1)

  nbins, xmin, xmax = 40, 0, 200
  h_AddPt2 = R.TH1F("TT+TL+LLPt2", "", nbins, xmin, xmax)
  h_AddPt2.Add(h_TTPt2, 1)
  h_AddPt2.Add(h_TLPt2, 1)
  h_AddPt2.Add(h_LLPt2, 1)

  nbins, xmin, xmax = 40, 0, 200
  h_AddPt4l = R.TH1F("TT+TL+LLPt4l", "", nbins, xmin, xmax)
  h_AddPt4l.Add(h_TTPt4l, 1)
  h_AddPt4l.Add(h_TLPt4l, 1)
  h_AddPt4l.Add(h_LLPt4l, 1)



  """
  In order to calculate the ratio between each histogram and h_AddXX, create a series of histograms to save the results of ratio
  """

  h_M1Divide = R.TH1F("M1Divide", "", 40, 80, 100)
  h_TTM1Divide = R.TH1F("TTM1Divide", "", 40, 80, 100)
  h_TLM1Divide = R.TH1F("TLM1Divide", "", 40, 80, 100)
  h_LLM1Divide = R.TH1F("LLM1Divide", "", 40, 80, 100)
  h_AddM1Divide = R.TH1F("AddM1Divide", "", 40, 80, 100)

  h_M2Divide = R.TH1F("M2Divide", "", 40, 70, 110)
  h_TTM2Divide = R.TH1F("TTM2Divide", "", 40, 70, 110)
  h_TLM2Divide = R.TH1F("TLM2Divide", "", 40, 70, 110)
  h_LLM2Divide = R.TH1F("LLM2Divide", "", 40, 70, 110)
  h_AddM2Divide = R.TH1F("AddM2Divide", "", 40, 70, 110)

  h_CosTheta1Divide = R.TH1F("CosTheta1Divide", "", 40, -1, 1)
  h_TTCosTheta1Divide = R.TH1F("TTCosTheta1Divide", "", 40, -1, 1)
  h_TLCosTheta1Divide = R.TH1F("TLCosTheta1Divide", "", 40, -1, 1)
  h_LLCosTheta1Divide = R.TH1F("LLCosTheta1Divide", "", 40, -1, 1)
  h_AddCosTheta1Divide = R.TH1F("AddCosTheta1Divide", "", 40, -1, 1)

  h_CosTheta2Divide = R.TH1F("CosTheta2Divide", "", 40, -1, 1)
  h_TTCosTheta2Divide = R.TH1F("TTCosTheta2Divide", "", 40, -1, 1)
  h_TLCosTheta2Divide = R.TH1F("TLCosTheta2Divide", "", 40, -1, 1)
  h_LLCosTheta2Divide = R.TH1F("LLCosTheta2Divide", "", 40, -1, 1)
  h_AddCosTheta2Divide = R.TH1F("AddCosTheta2Divide", "", 40, -1, 1)

  h_Theta1Divide = R.TH1F("Theta1Divide", "", 40, 0, R.TMath.Pi())
  h_TTTheta1Divide = R.TH1F("TTTheta1Divide", "", 40, 0, R.TMath.Pi())
  h_TLTheta1Divide = R.TH1F("TLTheta1Divide", "", 40, 0, R.TMath.Pi())
  h_LLTheta1Divide = R.TH1F("LLTheta1Divide", "", 40, 0, R.TMath.Pi())
  h_AddTheta1Divide = R.TH1F("AddTheta1Divide", "", 40, 0, R.TMath.Pi())

  h_Theta2Divide = R.TH1F("Theta2Divide", "", 40, 0, R.TMath.Pi())
  h_TTTheta2Divide = R.TH1F("TTTheta2Divide", "", 40, 0, R.TMath.Pi())
  h_TLTheta2Divide = R.TH1F("TLTheta2Divide", "", 40, 0, R.TMath.Pi())
  h_LLTheta2Divide = R.TH1F("LLTheta2Divide", "", 40, 0, R.TMath.Pi())
  h_AddTheta2Divide = R.TH1F("AddTheta2Divide", "", 40, 0, R.TMath.Pi())

  h_ThetaStar1Divide = R.TH1F("ThetaStar1Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TTThetaStar1Divide = R.TH1F("TTThetaStar1Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TLThetaStar1Divide = R.TH1F("TLThetaStar1Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_LLThetaStar1Divide = R.TH1F("LLThetaStar1Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_AddThetaStar1Divide = R.TH1F("AddThetaStar1Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())

  h_ThetaStar2Divide = R.TH1F("ThetaStar2Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TTThetaStar2Divide = R.TH1F("TTThetaStar2Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TLThetaStar2Divide = R.TH1F("TLThetaStar2Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_LLThetaStar2Divide = R.TH1F("LLThetaStar2Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_AddThetaStar2Divide = R.TH1F("AddThetaStar2Divide", "", 40, -R.TMath.Pi(), R.TMath.Pi())

  h_CosThetaStar1Divide = R.TH1F("CosThetaStar1Divide", "", 40, -1, 1)
  h_TTCosThetaStar1Divide = R.TH1F("TTCosThetaStar1Divide", "", 40, -1, 1)
  h_TLCosThetaStar1Divide = R.TH1F("TLCosThetaStar1Divide", "", 40, -1, 1)
  h_LLCosThetaStar1Divide = R.TH1F("LLCosThetaStar1Divide", "", 40, -1, 1)
  h_AddCosThetaStar1Divide = R.TH1F("AddCosThetaStar1Divide", "", 40, -1, 1)

  h_CosThetaStar2Divide = R.TH1F("CosThetaStar2Divide", "", 40, -1, 1)
  h_TTCosThetaStar2Divide = R.TH1F("TTCosThetaStar2Divide", "", 40, -1, 1)
  h_TLCosThetaStar2Divide = R.TH1F("TLCosThetaStar2Divide", "", 40, -1, 1)
  h_LLCosThetaStar2Divide = R.TH1F("LLCosThetaStar2Divide", "", 40, -1, 1)
  h_AddCosThetaStar2Divide = R.TH1F("AddCosThetaStar2Divide", "", 40, -1, 1)

  h_PhiDivide = R.TH1F("PhiDivide", "", 40, 0, R.TMath.PiOver2())
  h_TTPhiDivide = R.TH1F("TTPhiDivide", "", 40, 0, R.TMath.PiOver2())
  h_TLPhiDivide = R.TH1F("TLPhiDivide", "", 40, 0, R.TMath.PiOver2())
  h_LLPhiDivide = R.TH1F("LLPhiDivide", "", 40, 0, R.TMath.PiOver2())
  h_AddPhiDivide = R.TH1F("AddPhiDivide", "", 40, 0, R.TMath.PiOver2())

  h_CosPhiDivide = R.TH1F("CosPhiDivide", "", 40, 0, 1)
  h_TTCosPhiDivide = R.TH1F("TTCosPhiDivide", "", 40, 0, 1)
  h_TLCosPhiDivide = R.TH1F("TLCosPhiDivide", "", 40, 0, 1)
  h_LLCosPhiDivide = R.TH1F("LLCosPhiDivide", "", 40, 0, 1)
  h_AddCosPhiDivide = R.TH1F("AddCosPhiDivide", "", 40, 0, 1)

  h_Phi1Divide = R.TH1F("Phi1Divide", "", 40, 0, R.TMath.PiOver2())
  h_TTPhi1Divide = R.TH1F("TTPhi1Divide", "", 40, 0, R.TMath.PiOver2())
  h_TLPhi1Divide = R.TH1F("TLPhi1Divide", "", 40, 0, R.TMath.PiOver2())
  h_LLPhi1Divide = R.TH1F("LLPhi1Divide", "", 40, 0, R.TMath.PiOver2())
  h_AddPhi1Divide = R.TH1F("AddPhi1Divide", "", 40, 0, R.TMath.PiOver2())

  h_CosPhi1Divide = R.TH1F("CosPhi1Divide", "", 40, 0, 1)
  h_TTCosPhi1Divide = R.TH1F("TTCosPhi1Divide", "", 40, 0, 1)
  h_TLCosPhi1Divide = R.TH1F("TLCosPhi1Divide", "", 40, 0, 1)
  h_LLCosPhi1Divide = R.TH1F("LLCosPhi1Divide", "", 40, 0, 1)
  h_AddCosPhi1Divide = R.TH1F("AddCosPhi1Divide", "", 40, 0, 1)

  h_M4lDivide = R.TH1F("M4lDivide", "", 40, 150, 550)
  h_TTM4lDivide = R.TH1F("TTM4lDivide", "", 40, 150, 550)
  h_TLM4lDivide = R.TH1F("TLM4lDivide", "", 40, 150, 550)
  h_LLM4lDivide = R.TH1F("LLM4lDivide", "", 40, 150, 550)
  h_AddM4lDivide = R.TH1F("AddM4lDivide", "", 40, 150, 550)

  h_Eta1Divide = R.TH1F("Eta1Divide", "", 40, -6, 6)
  h_TTEta1Divide = R.TH1F("TTEta1Divide", "", 40, -6, 6)
  h_TLEta1Divide = R.TH1F("TLEta1Divide", "", 40, -6, 6)
  h_LLEta1Divide = R.TH1F("LLEta1Divide", "", 40, -6, 6)
  h_AddEta1Divide = R.TH1F("AddEta1Divide", "", 40, -6, 6)

  h_Eta2Divide = R.TH1F("Eta2Divide", "", 40, -6, 6)
  h_TTEta2Divide = R.TH1F("TTEta2Divide", "", 40, -6, 6)
  h_TLEta2Divide = R.TH1F("TLEta2Divide", "", 40, -6, 6)
  h_LLEta2Divide = R.TH1F("LLEta2Divide", "", 40, -6, 6)
  h_AddEta2Divide = R.TH1F("AddEta2Divide", "", 40, -6, 6)

  h_Eta4lDivide = R.TH1F("Eta4lDivide", "", 40, -6, 6)
  h_TTEta4lDivide = R.TH1F("TTEta4lDivide", "", 40, -6, 6)
  h_TLEta4lDivide = R.TH1F("TLEta4lDivide", "", 40, -6, 6)
  h_LLEta4lDivide = R.TH1F("LLEta4lDivide", "", 40, -6, 6)
  h_AddEta4lDivide = R.TH1F("AddEta4lDivide", "", 40, -6, 6)

  h_Pt1Divide = R.TH1F("Pt1Divide", "", 40, 0, 200)
  h_TTPt1Divide = R.TH1F("TTPt1Divide", "", 40, 0, 200)
  h_TLPt1Divide = R.TH1F("TLPt1Divide", "", 40, 0, 200)
  h_LLPt1Divide = R.TH1F("LLPt1Divide", "", 40, 0, 200)
  h_AddPt1Divide = R.TH1F("AddPt1Divide", "", 40, 0, 200)

  h_Pt2Divide = R.TH1F("Pt2Divide", "", 40, 0, 200)
  h_TTPt2Divide = R.TH1F("TTPt2Divide", "", 40, 0, 200)
  h_TLPt2Divide = R.TH1F("TLPt2Divide", "", 40, 0, 200)
  h_LLPt2Divide = R.TH1F("LLPt2Divide", "", 40, 0, 200)
  h_AddPt2Divide = R.TH1F("AddPt2Divide", "", 40, 0, 200)

  h_Pt4lDivide = R.TH1F("Pt4lDivide", "", 40, 0, 200)
  h_TTPt4lDivide = R.TH1F("TTPt4lDivide", "", 40, 0, 200)
  h_TLPt4lDivide = R.TH1F("TLPt4lDivide", "", 40, 0, 200)
  h_LLPt4lDivide = R.TH1F("LLPt4lDivide", "", 40, 0, 200)
  h_AddPt4lDivide = R.TH1F("AddPt4lDivide", "", 40, 0, 200)



  """
  When draw the shape-only histograms, I need to calculate the ratio between each shape-only histogram and h_AddXXShape, so I create a series of histograms to save the results of ratio
  """

  h_M1DivideShape = R.TH1F("M1DivideShape", "", 40, 80, 100)
  h_TTM1DivideShape = R.TH1F("TTM1DivideShape", "", 40, 80, 100)
  h_TLM1DivideShape = R.TH1F("TLM1DivideShape", "", 40, 80, 100)
  h_LLM1DivideShape = R.TH1F("LLM1DivideShape", "", 40, 80, 100)
  h_AddM1DivideShape = R.TH1F("AddM1DivideShape", "", 40, 80, 100)

  h_M2DivideShape = R.TH1F("M2DivideShape", "", 40, 70, 110)
  h_TTM2DivideShape = R.TH1F("TTM2DivideShape", "", 40, 70, 110)
  h_TLM2DivideShape = R.TH1F("TLM2DivideShape", "", 40, 70, 110)
  h_LLM2DivideShape = R.TH1F("LLM2DivideShape", "", 40, 70, 110)
  h_AddM2DivideShape = R.TH1F("AddM2DivideShape", "", 40, 70, 110)

  h_CosTheta1DivideShape = R.TH1F("CosTheta1DivideShape", "", 40, -1, 1)
  h_TTCosTheta1DivideShape = R.TH1F("TTCosTheta1DivideShape", "", 40, -1, 1)
  h_TLCosTheta1DivideShape = R.TH1F("TLCosTheta1DivideShape", "", 40, -1, 1)
  h_LLCosTheta1DivideShape = R.TH1F("LLCosTheta1DivideShape", "", 40, -1, 1)
  h_AddCosTheta1DivideShape = R.TH1F("AddCosTheta1DivideShape", "", 40, -1, 1)

  h_CosTheta2DivideShape = R.TH1F("CosTheta2DivideShape", "", 40, -1, 1)
  h_TTCosTheta2DivideShape = R.TH1F("TTCosTheta2DivideShape", "", 40, -1, 1)
  h_TLCosTheta2DivideShape = R.TH1F("TLCosTheta2DivideShape", "", 40, -1, 1)
  h_LLCosTheta2DivideShape = R.TH1F("LLCosTheta2DivideShape", "", 40, -1, 1)
  h_AddCosTheta2DivideShape = R.TH1F("AddCosTheta2DivideShape", "", 40, -1, 1)

  h_Theta1DivideShape = R.TH1F("Theta1DivideShape", "", 40, 0, R.TMath.Pi())
  h_TTTheta1DivideShape = R.TH1F("TTTheta1DivideShape", "", 40, 0, R.TMath.Pi())
  h_TLTheta1DivideShape = R.TH1F("TLTheta1DivideShape", "", 40, 0, R.TMath.Pi())
  h_LLTheta1DivideShape = R.TH1F("LLTheta1DivideShape", "", 40, 0, R.TMath.Pi())
  h_AddTheta1DivideShape = R.TH1F("AddTheta1DivideShape", "", 40, 0, R.TMath.Pi())

  h_Theta2DivideShape = R.TH1F("Theta2DivideShape", "", 40, 0, R.TMath.Pi())
  h_TTTheta2DivideShape = R.TH1F("TTTheta2DivideShape", "", 40, 0, R.TMath.Pi())
  h_TLTheta2DivideShape = R.TH1F("TLTheta2DivideShape", "", 40, 0, R.TMath.Pi())
  h_LLTheta2DivideShape = R.TH1F("LLTheta2DivideShape", "", 40, 0, R.TMath.Pi())
  h_AddTheta2DivideShape = R.TH1F("AddTheta2DivideShape", "", 40, 0, R.TMath.Pi())

  h_ThetaStar1DivideShape = R.TH1F("ThetaStar1DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TTThetaStar1DivideShape = R.TH1F("TTThetaStar1DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TLThetaStar1DivideShape = R.TH1F("TLThetaStar1DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_LLThetaStar1DivideShape = R.TH1F("LLThetaStar1DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_AddThetaStar1DivideShape = R.TH1F("AddThetaStar1DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())

  h_ThetaStar2DivideShape = R.TH1F("ThetaStar2DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TTThetaStar2DivideShape = R.TH1F("TTThetaStar2DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_TLThetaStar2DivideShape = R.TH1F("TLThetaStar2DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_LLThetaStar2DivideShape = R.TH1F("LLThetaStar2DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())
  h_AddThetaStar2DivideShape = R.TH1F("AddThetaStar2DivideShape", "", 40, -R.TMath.Pi(), R.TMath.Pi())

  h_CosThetaStar1DivideShape = R.TH1F("CosThetaStar1DivideShape", "", 40, -1, 1)
  h_TTCosThetaStar1DivideShape = R.TH1F("TTCosThetaStar1DivideShape", "", 40, -1, 1)
  h_TLCosThetaStar1DivideShape = R.TH1F("TLCosThetaStar1DivideShape", "", 40, -1, 1)
  h_LLCosThetaStar1DivideShape = R.TH1F("LLCosThetaStar1DivideShape", "", 40, -1, 1)
  h_AddCosThetaStar1DivideShape = R.TH1F("AddCosThetaStar1DivideShape", "", 40, -1, 1)

  h_CosThetaStar2DivideShape = R.TH1F("CosThetaStar2DivideShape", "", 40, -1, 1)
  h_TTCosThetaStar2DivideShape = R.TH1F("TTCosThetaStar2DivideShape", "", 40, -1, 1)
  h_TLCosThetaStar2DivideShape = R.TH1F("TLCosThetaStar2DivideShape", "", 40, -1, 1)
  h_LLCosThetaStar2DivideShape = R.TH1F("LLCosThetaStar2DivideShape", "", 40, -1, 1)
  h_AddCosThetaStar2DivideShape = R.TH1F("AddCosThetaStar2DivideShape", "", 40, -1, 1)

  h_PhiDivideShape = R.TH1F("PhiDivideShape", "", 40, 0, R.TMath.PiOver2())
  h_TTPhiDivideShape = R.TH1F("TTPhiDivideShape", "", 40, 0, R.TMath.PiOver2())
  h_TLPhiDivideShape = R.TH1F("TLPhiDivideShape", "", 40, 0, R.TMath.PiOver2())
  h_LLPhiDivideShape = R.TH1F("LLPhiDivideShape", "", 40, 0, R.TMath.PiOver2())
  h_AddPhiDivideShape = R.TH1F("AddPhiDivideShape", "", 40, 0, R.TMath.PiOver2())

  h_CosPhiDivideShape = R.TH1F("CosPhiDivideShape", "", 40, 0, 1)
  h_TTCosPhiDivideShape = R.TH1F("TTCosPhiDivideShape", "", 40, 0, 1)
  h_TLCosPhiDivideShape = R.TH1F("TLCosPhiDivideShape", "", 40, 0, 1)
  h_LLCosPhiDivideShape = R.TH1F("LLCosPhiDivideShape", "", 40, 0, 1)
  h_AddCosPhiDivideShape = R.TH1F("AddCosPhiDivideShape", "", 40, 0, 1)

  h_Phi1DivideShape = R.TH1F("Phi1DivideShape", "", 40, 0, R.TMath.PiOver2())
  h_TTPhi1DivideShape = R.TH1F("TTPhi1DivideShape", "", 40, 0, R.TMath.PiOver2())
  h_TLPhi1DivideShape = R.TH1F("TLPhi1DivideShape", "", 40, 0, R.TMath.PiOver2())
  h_LLPhi1DivideShape = R.TH1F("LLPhi1DivideShape", "", 40, 0, R.TMath.PiOver2())
  h_AddPhi1DivideShape = R.TH1F("AddPhi1DivideShape", "", 40, 0, R.TMath.PiOver2())

  h_CosPhi1DivideShape = R.TH1F("CosPhi1DivideShape", "", 40, 0, 1)
  h_TTCosPhi1DivideShape = R.TH1F("TTCosPhi1DivideShape", "", 40, 0, 1)
  h_TLCosPhi1DivideShape = R.TH1F("TLCosPhi1DivideShape", "", 40, 0, 1)
  h_LLCosPhi1DivideShape = R.TH1F("LLCosPhi1DivideShape", "", 40, 0, 1)
  h_AddCosPhi1DivideShape = R.TH1F("AddCosPhi1DivideShape", "", 40, 0, 1)

  h_M4lDivideShape = R.TH1F("M4lDivideShape", "", 40, 150, 550)
  h_TTM4lDivideShape = R.TH1F("TTM4lDivideShape", "", 40, 150, 550)
  h_TLM4lDivideShape = R.TH1F("TLM4lDivideShape", "", 40, 150, 550)
  h_LLM4lDivideShape = R.TH1F("LLM4lDivideShape", "", 40, 150, 550)
  h_AddM4lDivideShape = R.TH1F("AddM14lDivideShape", "", 40, 150, 550)

  h_Eta1DivideShape = R.TH1F("Eta1DivideShape", "", 40, -6, 6)
  h_TTEta1DivideShape = R.TH1F("TTEta1DivideShape", "", 40, -6, 6)
  h_TLEta1DivideShape = R.TH1F("TLEta1DivideShape", "", 40, -6, 6)
  h_LLEta1DivideShape = R.TH1F("LLEta1DivideShape", "", 40, -6, 6)
  h_AddEta1DivideShape = R.TH1F("AddEta1DivideShape", "", 40, -6, 6)

  h_Eta2DivideShape = R.TH1F("Eta2DivideShape", "", 40, -6, 6)
  h_TTEta2DivideShape = R.TH1F("TTEta2DivideShape", "", 40, -6, 6)
  h_TLEta2DivideShape = R.TH1F("TLEta2DivideShape", "", 40, -6, 6)
  h_LLEta2DivideShape = R.TH1F("LLEta2DivideShape", "", 40, -6, 6)
  h_AddEta2DivideShape = R.TH1F("AddEta2DivideShape", "", 40, -6, 6)

  h_Eta4lDivideShape = R.TH1F("Eta4lDivideShape", "", 40, -6, 6)
  h_TTEta4lDivideShape = R.TH1F("TTEta4lDivideShape", "", 40, -6, 6)
  h_TLEta4lDivideShape = R.TH1F("TLEta4lDivideShape", "", 40, -6, 6)
  h_LLEta4lDivideShape = R.TH1F("LLEta4lDivideShape", "", 40, -6, 6)
  h_AddEta4lDivideShape = R.TH1F("AddEta4lDivideShape", "", 40, -6, 6)

  h_Pt1DivideShape = R.TH1F("Pt1DivideShape", "", 40, 0, 200)
  h_TTPt1DivideShape = R.TH1F("TTPt1DivideShape", "", 40, 0, 200)
  h_TLPt1DivideShape = R.TH1F("TLPt1DivideShape", "", 40, 0, 200)
  h_LLPt1DivideShape = R.TH1F("LLPt1DivideShape", "", 40, 0, 200)
  h_AddPt1DivideShape = R.TH1F("AddPt1DivideShape", "", 40, 0, 200)

  h_Pt2DivideShape = R.TH1F("Pt2DivideShape", "", 40, 0, 200)
  h_TTPt2DivideShape = R.TH1F("TTPt2DivideShape", "", 40, 0, 200)
  h_TLPt2DivideShape = R.TH1F("TLPt2DivideShape", "", 40, 0, 200)
  h_LLPt2DivideShape = R.TH1F("LLPt2DivideShape", "", 40, 0, 200)
  h_AddPt2DivideShape = R.TH1F("AddPt2DivideShape", "", 40, 0, 200)

  h_Pt4lDivideShape = R.TH1F("Pt4lDivideShape", "", 40, 0, 200)
  h_TTPt4lDivideShape = R.TH1F("TTPt4lDivideShape", "", 40, 0, 200)
  h_TLPt4lDivideShape = R.TH1F("TLPt4lDivideShape", "", 40, 0, 200)
  h_LLPt4lDivideShape = R.TH1F("LLPt4lDivideShape", "", 40, 0, 200)
  h_AddPt4lDivideShape = R.TH1F("AddPt4lDivideShape", "", 40, 0, 200)



  """
  In order to draw the stacked histogram of TT, TL and LL, create a series of histograms to save the results of stacking
  """

  # creat a THStack to stack the histogram of TT, TL and LL, set its name and title
  hs_M1 = R.THStack("hs_M1", "")
  # since we should remove the line of histogram when stack them, I create a series of copied histograms in order to avoid changing the initial histogram.
  h_LLM1Clone1 = h_LLM1.Clone("h_LLM1Clone1")
  h_TLM1Clone1 = h_TLM1.Clone("h_TLM1Clone1")
  h_TTM1Clone1 = h_TTM1.Clone("h_TTM1Clone1")
  # set the width of histogram to zero
  h_LLM1Clone1.SetLineWidth(0)
  h_TLM1Clone1.SetLineWidth(0)
  h_TTM1Clone1.SetLineWidth(0)
  # add these histograms to the THStack
  hs_M1.Add(h_LLM1Clone1, "Hist")
  hs_M1.Add(h_TLM1Clone1, "SameHist")
  hs_M1.Add(h_TTM1Clone1, "SameHist")

  hs_M2 = R.THStack("hs_M2", "")
  h_LLM2Clone1 = h_LLM2.Clone("h_LLM2Clone1")
  h_TLM2Clone1 = h_TLM2.Clone("h_TLM2Clone1")
  h_TTM2Clone1 = h_TTM2.Clone("h_TTM2Clone1")
  h_LLM2Clone1.SetLineWidth(0)
  h_TLM2Clone1.SetLineWidth(0)
  h_TTM2Clone1.SetLineWidth(0)
  hs_M2.Add(h_LLM2Clone1, "Hist")
  hs_M2.Add(h_TLM2Clone1, "SameHist")
  hs_M2.Add(h_TTM2Clone1, "SameHist")

  hs_CosTheta1 = R.THStack("hs_CosTheta1", "")
  h_LLCosTheta1Clone1 = h_LLCosTheta1.Clone("h_LLCosTheta1Clone1")
  h_TLCosTheta1Clone1 = h_TLCosTheta1.Clone("h_TLCosTheta1Clone1")
  h_TTCosTheta1Clone1 = h_TTCosTheta1.Clone("h_TTCosTheta1Clone1")
  h_LLCosTheta1Clone1.SetLineWidth(0)
  h_TLCosTheta1Clone1.SetLineWidth(0)
  h_TTCosTheta1Clone1.SetLineWidth(0)
  hs_CosTheta1.Add(h_LLCosTheta1Clone1, "Hist")
  hs_CosTheta1.Add(h_TLCosTheta1Clone1, "SameHist")
  hs_CosTheta1.Add(h_TTCosTheta1Clone1, "SameHist")

  hs_CosTheta2 = R.THStack("hs_CosTheta2", "")
  h_LLCosTheta2Clone1 = h_LLCosTheta2.Clone("h_LLCosTheta2Clone1")
  h_TLCosTheta2Clone1 = h_TLCosTheta2.Clone("h_TLCosTheta2Clone1")
  h_TTCosTheta2Clone1 = h_TTCosTheta2.Clone("h_TTCosTheta2Clone1")
  h_LLCosTheta2Clone1.SetLineWidth(0)
  h_TLCosTheta2Clone1.SetLineWidth(0)
  h_TTCosTheta2Clone1.SetLineWidth(0)
  hs_CosTheta2.Add(h_LLCosTheta2Clone1, "Hist")
  hs_CosTheta2.Add(h_TLCosTheta2Clone1, "SameHist")
  hs_CosTheta2.Add(h_TTCosTheta2Clone1, "SameHist")

  hs_Theta1 = R.THStack("hs_Theta1", "")
  h_LLTheta1Clone1 = h_LLTheta1.Clone("h_LLTheta1Clone1")
  h_TLTheta1Clone1 = h_TLTheta1.Clone("h_TLTheta1Clone1")
  h_TTTheta1Clone1 = h_TTTheta1.Clone("h_TTTheta1Clone1")
  h_LLTheta1Clone1.SetLineWidth(0)
  h_TLTheta1Clone1.SetLineWidth(0)
  h_TTTheta1Clone1.SetLineWidth(0)
  hs_Theta1.Add(h_LLTheta1Clone1, "Hist")
  hs_Theta1.Add(h_TLTheta1Clone1, "SameHist")
  hs_Theta1.Add(h_TTTheta1Clone1, "SameHist")

  hs_Theta2 = R.THStack("hs_Theta2", "")
  h_LLTheta2Clone1 = h_LLTheta2.Clone("h_LLTheta2Clone1")
  h_TLTheta2Clone1 = h_TLTheta2.Clone("h_TLTheta2Clone1")
  h_TTTheta2Clone1 = h_TTTheta2.Clone("h_TTTheta2Clone1")
  h_LLTheta2Clone1.SetLineWidth(0)
  h_TLTheta2Clone1.SetLineWidth(0)
  h_TTTheta2Clone1.SetLineWidth(0)
  hs_Theta2.Add(h_LLTheta2Clone1, "Hist")
  hs_Theta2.Add(h_TLTheta2Clone1, "SameHist")
  hs_Theta2.Add(h_TTTheta2Clone1, "SameHist")

  hs_ThetaStar1 = R.THStack("hs_ThetaStar1", "")
  h_LLThetaStar1Clone1 = h_LLThetaStar1.Clone("h_LLThetaStar1Clone1")
  h_TLThetaStar1Clone1 = h_TLThetaStar1.Clone("h_TLThetaStar1Clone1")
  h_TTThetaStar1Clone1 = h_TTThetaStar1.Clone("h_TTThetaStar1Clone1")
  h_LLThetaStar1Clone1.SetLineWidth(0)
  h_TLThetaStar1Clone1.SetLineWidth(0)
  h_TTThetaStar1Clone1.SetLineWidth(0)
  hs_ThetaStar1.Add(h_LLThetaStar1Clone1, "Hist")
  hs_ThetaStar1.Add(h_TLThetaStar1Clone1, "SameHist")
  hs_ThetaStar1.Add(h_TTThetaStar1Clone1, "SameHist")

  hs_ThetaStar2 = R.THStack("hs_ThetaStar2", "")
  h_LLThetaStar2Clone1 = h_LLThetaStar2.Clone("h_LLThetaStar2Clone1")
  h_TLThetaStar2Clone1 = h_TLThetaStar2.Clone("h_TLThetaStar2Clone1")
  h_TTThetaStar2Clone1 = h_TTThetaStar2.Clone("h_TTThetaStar2Clone1")
  h_LLThetaStar2Clone1.SetLineWidth(0)
  h_TLThetaStar2Clone1.SetLineWidth(0)
  h_TTThetaStar2Clone1.SetLineWidth(0)
  hs_ThetaStar2.Add(h_LLThetaStar2Clone1, "Hist")
  hs_ThetaStar2.Add(h_TLThetaStar2Clone1, "SameHist")
  hs_ThetaStar2.Add(h_TTThetaStar2Clone1, "SameHist")

  hs_CosThetaStar1 = R.THStack("hs_CosThetaStar1", "")
  h_LLCosThetaStar1Clone1 = h_LLCosThetaStar1.Clone("h_LLCosThetaStar1Clone1")
  h_TLCosThetaStar1Clone1 = h_TLCosThetaStar1.Clone("h_TLCosThetaStar1Clone1")
  h_TTCosThetaStar1Clone1 = h_TTCosThetaStar1.Clone("h_TTCosThetaStar1Clone1")
  h_LLCosThetaStar1Clone1.SetLineWidth(0)
  h_TLCosThetaStar1Clone1.SetLineWidth(0)
  h_TTCosThetaStar1Clone1.SetLineWidth(0)
  hs_CosThetaStar1.Add(h_LLCosThetaStar1Clone1, "Hist")
  hs_CosThetaStar1.Add(h_TLCosThetaStar1Clone1, "SameHist")
  hs_CosThetaStar1.Add(h_TTCosThetaStar1Clone1, "SameHist")

  hs_CosThetaStar2 = R.THStack("hs_CosThetaStar2", "")
  h_LLCosThetaStar2Clone1 = h_LLCosThetaStar2.Clone("h_LLCosThetaStar2Clone1")
  h_TLCosThetaStar2Clone1 = h_TLCosThetaStar2.Clone("h_TLCosThetaStar2Clone1")
  h_TTCosThetaStar2Clone1 = h_TTCosThetaStar2.Clone("h_TTCosThetaStar2Clone1")
  h_LLCosThetaStar2Clone1.SetLineWidth(0)
  h_TLCosThetaStar2Clone1.SetLineWidth(0)
  h_TTCosThetaStar2Clone1.SetLineWidth(0)
  hs_CosThetaStar2.Add(h_LLCosThetaStar2Clone1, "Hist")
  hs_CosThetaStar2.Add(h_TLCosThetaStar2Clone1, "SameHist")
  hs_CosThetaStar2.Add(h_TTCosThetaStar2Clone1, "SameHist")

  hs_Phi = R.THStack("hs_Phi", "")
  h_LLPhiClone1 = h_LLPhi.Clone("h_LLPhiClone1")
  h_TLPhiClone1 = h_TLPhi.Clone("h_TLPhiClone1")
  h_TTPhiClone1 = h_TTPhi.Clone("h_TTPhiClone1")
  h_LLPhiClone1.SetLineWidth(0)
  h_TLPhiClone1.SetLineWidth(0)
  h_TTPhiClone1.SetLineWidth(0)
  hs_Phi.Add(h_LLPhiClone1, "Hist")
  hs_Phi.Add(h_TLPhiClone1, "SameHist")
  hs_Phi.Add(h_TTPhiClone1, "SameHist")

  hs_CosPhi = R.THStack("hs_CosPhi", "")
  h_LLCosPhiClone1 = h_LLCosPhi.Clone("h_LLCosPhiClone1")
  h_TLCosPhiClone1 = h_TLCosPhi.Clone("h_TLCosPhiClone1")
  h_TTCosPhiClone1 = h_TTCosPhi.Clone("h_TTCosPhiClone1")
  h_LLCosPhiClone1.SetLineWidth(0)
  h_TLCosPhiClone1.SetLineWidth(0)
  h_TTCosPhiClone1.SetLineWidth(0)
  hs_CosPhi.Add(h_LLCosPhiClone1, "Hist")
  hs_CosPhi.Add(h_TLCosPhiClone1, "SameHist")
  hs_CosPhi.Add(h_TTCosPhiClone1, "SameHist")

  hs_Phi1 = R.THStack("hs_Phi1", "")
  h_LLPhi1Clone1 = h_LLPhi1.Clone("h_LLPhi1Clone1")
  h_TLPhi1Clone1 = h_TLPhi1.Clone("h_TLPhi1Clone1")
  h_TTPhi1Clone1 = h_TTPhi1.Clone("h_TTPhi1Clone1")
  h_LLPhi1Clone1.SetLineWidth(0)
  h_TLPhi1Clone1.SetLineWidth(0)
  h_TTPhi1Clone1.SetLineWidth(0)
  hs_Phi1.Add(h_LLPhi1Clone1, "Hist")
  hs_Phi1.Add(h_TLPhi1Clone1, "SameHist")
  hs_Phi1.Add(h_TTPhi1Clone1, "SameHist")

  hs_CosPhi1 = R.THStack("hs_CosPhi1", "")
  h_LLCosPhi1Clone1 = h_LLCosPhi1.Clone("h_LLCosPhi1Clone1")
  h_TLCosPhi1Clone1 = h_TLCosPhi1.Clone("h_TLCosPhi1Clone1")
  h_TTCosPhi1Clone1 = h_TTCosPhi1.Clone("h_TTCosPhi1Clone1")
  h_LLCosPhi1Clone1.SetLineWidth(0)
  h_TLCosPhi1Clone1.SetLineWidth(0)
  h_TTCosPhi1Clone1.SetLineWidth(0)
  hs_CosPhi1.Add(h_LLCosPhi1Clone1, "Hist")
  hs_CosPhi1.Add(h_TLCosPhi1Clone1, "SameHist")
  hs_CosPhi1.Add(h_TTCosPhi1Clone1, "SameHist")

  hs_M4l = R.THStack("hs_M4l", "")
  h_LLM4lClone1 = h_LLM4l.Clone("h_LLM4lClone1")
  h_TLM4lClone1 = h_TLM4l.Clone("h_TLM4lClone1")
  h_TTM4lClone1 = h_TTM4l.Clone("h_TTM4lClone1")
  h_LLM4lClone1.SetLineWidth(0)
  h_TLM4lClone1.SetLineWidth(0)
  h_TTM4lClone1.SetLineWidth(0)
  hs_M4l.Add(h_LLM4lClone1, "Hist")
  hs_M4l.Add(h_TLM4lClone1, "SameHist")
  hs_M4l.Add(h_TTM4lClone1, "SameHist")

  hs_Eta1 = R.THStack("hs_Eta1", "")
  h_LLEta1Clone1 = h_LLEta1.Clone("h_LLEta1Clone1")
  h_TLEta1Clone1 = h_TLEta1.Clone("h_TLEta1Clone1")
  h_TTEta1Clone1 = h_TTEta1.Clone("h_TTEta1Clone1")
  h_LLEta1Clone1.SetLineWidth(0)
  h_TLEta1Clone1.SetLineWidth(0)
  h_TTEta1Clone1.SetLineWidth(0)
  hs_Eta1.Add(h_LLEta1Clone1, "Hist")
  hs_Eta1.Add(h_TLEta1Clone1, "SameHist")
  hs_Eta1.Add(h_TTEta1Clone1, "SameHist")

  hs_Eta2 = R.THStack("hs_Eta2", "")
  h_LLEta2Clone1 = h_LLEta2.Clone("h_LLEta2Clone1")
  h_TLEta2Clone1 = h_TLEta2.Clone("h_TLEta2Clone1")
  h_TTEta2Clone1 = h_TTEta2.Clone("h_TTEta2Clone1")
  h_LLEta2Clone1.SetLineWidth(0)
  h_TLEta2Clone1.SetLineWidth(0)
  h_TTEta2Clone1.SetLineWidth(0)
  hs_Eta2.Add(h_LLEta2Clone1, "Hist")
  hs_Eta2.Add(h_TLEta2Clone1, "SameHist")
  hs_Eta2.Add(h_TTEta2Clone1, "SameHist")

  hs_Eta4l = R.THStack("hs_Eta4l", "")
  h_LLEta4lClone1 = h_LLEta4l.Clone("h_LLEta4lClone1")
  h_TLEta4lClone1 = h_TLEta4l.Clone("h_TLEta4lClone1")
  h_TTEta4lClone1 = h_TTEta4l.Clone("h_TTEta4lClone1")
  h_LLEta4lClone1.SetLineWidth(0)
  h_TLEta4lClone1.SetLineWidth(0)
  h_TTEta4lClone1.SetLineWidth(0)
  hs_Eta4l.Add(h_LLEta4lClone1, "Hist")
  hs_Eta4l.Add(h_TLEta4lClone1, "SameHist")
  hs_Eta4l.Add(h_TTEta4lClone1, "SameHist")

  hs_Pt1 = R.THStack("hs_Pt1", "")
  h_LLPt1Clone1 = h_LLPt1.Clone("h_LLPt1Clone1")
  h_TLPt1Clone1 = h_TLPt1.Clone("h_TLPt1Clone1")
  h_TTPt1Clone1 = h_TTPt1.Clone("h_TTPt1Clone1")
  h_LLPt1Clone1.SetLineWidth(0)
  h_TLPt1Clone1.SetLineWidth(0)
  h_TTPt1Clone1.SetLineWidth(0)
  hs_Pt1.Add(h_LLPt1Clone1, "Hist")
  hs_Pt1.Add(h_TLPt1Clone1, "SameHist")
  hs_Pt1.Add(h_TTPt1Clone1, "SameHist")

  hs_Pt2 = R.THStack("hs_Eta2", "")
  h_LLPt2Clone1 = h_LLPt2.Clone("h_LLPt2Clone1")
  h_TLPt2Clone1 = h_TLPt2.Clone("h_TLPt2Clone1")
  h_TTPt2Clone1 = h_TTPt2.Clone("h_TTPt2Clone1")
  h_LLPt2Clone1.SetLineWidth(0)
  h_TLPt2Clone1.SetLineWidth(0)
  h_TTPt2Clone1.SetLineWidth(0)
  hs_Pt2.Add(h_LLPt2Clone1, "Hist")
  hs_Pt2.Add(h_TLPt2Clone1, "SameHist")
  hs_Pt2.Add(h_TTPt2Clone1, "SameHist")

  hs_Pt4l = R.THStack("hs_Pt4l", "")
  h_LLPt4lClone1 = h_LLPt4l.Clone("h_LLPt4lClone1")
  h_TLPt4lClone1 = h_TLPt4l.Clone("h_TLPt4lClone1")
  h_TTPt4lClone1 = h_TTPt4l.Clone("h_TTPt4lClone1")
  h_LLPt4lClone1.SetLineWidth(0)
  h_TLPt4lClone1.SetLineWidth(0)
  h_TTPt4lClone1.SetLineWidth(0)
  hs_Pt4l.Add(h_LLPt4lClone1, "Hist")
  hs_Pt4l.Add(h_TLPt4lClone1, "SameHist")
  hs_Pt4l.Add(h_TTPt4lClone1, "SameHist")



  """
  In order to draw the shape-only histograms, all the histogram of Inclusive, TT, TL, LL and TT+TL+LL need to be renormalized to 1, create a series of copied histograms to save them
  """

  h_M1Clone2 = h_M1.Clone("h_M1Clone2")
  h_TTM1Clone2 = h_TTM1.Clone("h_TTM1Clone2")
  h_TLM1Clone2 = h_TLM1.Clone("h_TLM1Clone2")
  h_LLM1Clone2 = h_LLM1.Clone("h_LLM1Clone2")
  h_AddM1Clone2 = h_AddM1.Clone("h_AddM1Clone2")

  h_M2Clone2 = h_M2.Clone("h_M2Clone2")
  h_TTM2Clone2 = h_TTM2.Clone("h_TTM2Clone2")
  h_TLM2Clone2 = h_TLM2.Clone("h_TLM2Clone2")
  h_LLM2Clone2 = h_LLM2.Clone("h_LLM2Clone2")
  h_AddM2Clone2 = h_AddM2.Clone("h_AddM2Clone2")

  h_CosTheta1Clone2 = h_CosTheta1.Clone("h_CosTheta1Clone2")
  h_TTCosTheta1Clone2 = h_TTCosTheta1.Clone("h_TTCosTheta1Clone2")
  h_TLCosTheta1Clone2 = h_TLCosTheta1.Clone("h_TLCosTheta1Clone2")
  h_LLCosTheta1Clone2 = h_LLCosTheta1.Clone("h_LLCosTheta1Clone2")
  h_AddCosTheta1Clone2 = h_AddCosTheta1.Clone("h_AddCosTheta1Clone2")

  h_CosTheta2Clone2 = h_CosTheta2.Clone("h_CosTheta2Clone2")
  h_TTCosTheta2Clone2 = h_TTCosTheta2.Clone("h_TTCosTheta2Clone2")
  h_TLCosTheta2Clone2 = h_TLCosTheta2.Clone("h_TLCosTheta2Clone2")
  h_LLCosTheta2Clone2 = h_LLCosTheta2.Clone("h_LLCosTheta2Clone2")
  h_AddCosTheta2Clone2 = h_AddCosTheta2.Clone("h_AddCosTheta2Clone2")

  h_Theta1Clone2 = h_Theta1.Clone("h_Theta1Clone2")
  h_TTTheta1Clone2 = h_TTTheta1.Clone("h_TTTheta1Clone2")
  h_TLTheta1Clone2 = h_TLTheta1.Clone("h_TLTheta1Clone2")
  h_LLTheta1Clone2 = h_LLTheta1.Clone("h_LLTheta1Clone2")
  h_AddTheta1Clone2 = h_AddTheta1.Clone("h_AddTheta1Clone2")

  h_Theta2Clone2 = h_Theta2.Clone("h_Theta2Clone2")
  h_TTTheta2Clone2 = h_TTTheta2.Clone("h_TTTheta2Clone2")
  h_TLTheta2Clone2 = h_TLTheta2.Clone("h_TLTheta2Clone2")
  h_LLTheta2Clone2 = h_LLTheta2.Clone("h_LLTheta2Clone2")
  h_AddTheta2Clone2 = h_AddTheta2.Clone("h_AddTheta2Clone2")

  h_ThetaStar1Clone2 = h_ThetaStar1.Clone("h_ThetaStar1Clone2")
  h_TTThetaStar1Clone2 = h_TTThetaStar1.Clone("h_TTThetaStar1Clone2")
  h_TLThetaStar1Clone2 = h_TLThetaStar1.Clone("h_TLThetaStar1Clone2")
  h_LLThetaStar1Clone2 = h_LLThetaStar1.Clone("h_LLThetaStar1Clone2")
  h_AddThetaStar1Clone2 = h_AddThetaStar1.Clone("h_AddThetaStar1Clone2")

  h_ThetaStar2Clone2 = h_ThetaStar2.Clone("h_ThetaStar2Clone2")
  h_TTThetaStar2Clone2 = h_TTThetaStar2.Clone("h_TTThetaStar2Clone2")
  h_TLThetaStar2Clone2 = h_TLThetaStar2.Clone("h_TLThetaStar2Clone2")
  h_LLThetaStar2Clone2 = h_LLThetaStar2.Clone("h_LLThetaStar2Clone2")
  h_AddThetaStar2Clone2 = h_AddThetaStar2.Clone("h_AddThetaStar2Clone2")

  h_CosThetaStar1Clone2 = h_CosThetaStar1.Clone("h_CosThetaStar1Clone2")
  h_TTCosThetaStar1Clone2 = h_TTCosThetaStar1.Clone("h_TTCosThetaStar1Clone2")
  h_TLCosThetaStar1Clone2 = h_TLCosThetaStar1.Clone("h_TLCosThetaStar1Clone2")
  h_LLCosThetaStar1Clone2 = h_LLCosThetaStar1.Clone("h_LLCosThetaStar1Clone2")
  h_AddCosThetaStar1Clone2 = h_AddCosThetaStar1.Clone("h_AddCosThetaStar1Clone2")

  h_CosThetaStar2Clone2 = h_CosThetaStar2.Clone("h_CosThetaStar2Clone2")
  h_TTCosThetaStar2Clone2 = h_TTCosThetaStar2.Clone("h_TTCosThetaStar2Clone2")
  h_TLCosThetaStar2Clone2 = h_TLCosThetaStar2.Clone("h_TLCosThetaStar2Clone2")
  h_LLCosThetaStar2Clone2 = h_LLCosThetaStar2.Clone("h_LLCosThetaStar2Clone2")
  h_AddCosThetaStar2Clone2 = h_AddCosThetaStar2.Clone("h_AddCosThetaStar2Clone2")

  h_PhiClone2 = h_Phi.Clone("h_PhiClone2")
  h_TTPhiClone2 = h_TTPhi.Clone("h_TTPhiClone2")
  h_TLPhiClone2 = h_TLPhi.Clone("h_TLPhiClone2")
  h_LLPhiClone2 = h_LLPhi.Clone("h_LLPhiClone2")
  h_AddPhiClone2 = h_AddPhi.Clone("h_AddPhiClone2")

  h_CosPhiClone2 = h_CosPhi.Clone("h_CosPhiClone2")
  h_TTCosPhiClone2 = h_TTCosPhi.Clone("h_TTCosPhiClone2")
  h_TLCosPhiClone2 = h_TLCosPhi.Clone("h_TLCosPhiClone2")
  h_LLCosPhiClone2 = h_LLCosPhi.Clone("h_LLCosPhiClone2")
  h_AddCosPhiClone2 = h_AddCosPhi.Clone("h_AddCosPhiClone2")

  h_Phi1Clone2 = h_Phi1.Clone("h_Phi1Clone2")
  h_TTPhi1Clone2 = h_TTPhi1.Clone("h_TTPhi1Clone2")
  h_TLPhi1Clone2 = h_TLPhi1.Clone("h_TLPhi1Clone2")
  h_LLPhi1Clone2 = h_LLPhi1.Clone("h_LLPhi1Clone2")
  h_AddPhi1Clone2 = h_AddPhi1.Clone("h_AddPhi1Clone2")

  h_CosPhi1Clone2 = h_CosPhi1.Clone("h_CosPhi1Clone2")
  h_TTCosPhi1Clone2 = h_TTCosPhi1.Clone("h_TTCosPhi1Clone2")
  h_TLCosPhi1Clone2 = h_TLCosPhi1.Clone("h_TLCosPhi1Clone2")
  h_LLCosPhi1Clone2 = h_LLCosPhi1.Clone("h_LLCosPhi1Clone2")
  h_AddCosPhi1Clone2 = h_AddCosPhi1.Clone("h_AddCosPhi1Clone2")

  h_M4lClone2 = h_M4l.Clone("h_M4lClone2")
  h_TTM4lClone2 = h_TTM4l.Clone("h_TTM4lClone2")
  h_TLM4lClone2 = h_TLM4l.Clone("h_TLM4lClone2")
  h_LLM4lClone2 = h_LLM4l.Clone("h_LLM4lClone2")
  h_AddM4lClone2 = h_AddM4l.Clone("h_AddM4lClone2")

  h_Eta1Clone2 = h_Eta1.Clone("h_Eta1Clone2")
  h_TTEta1Clone2 = h_TTEta1.Clone("h_TTEta1Clone2")
  h_TLEta1Clone2 = h_TLEta1.Clone("h_TLEta1Clone2")
  h_LLEta1Clone2 = h_LLEta1.Clone("h_LLEta1Clone2")
  h_AddEta1Clone2 = h_AddEta1.Clone("h_AddEta1Clone2")

  h_Eta2Clone2 = h_Eta2.Clone("h_Eta2Clone2")
  h_TTEta2Clone2 = h_TTEta2.Clone("h_TTEta2Clone2")
  h_TLEta2Clone2 = h_TLEta2.Clone("h_TLEta2Clone2")
  h_LLEta2Clone2 = h_LLEta2.Clone("h_LLEta2Clone2")
  h_AddEta2Clone2 = h_AddEta2.Clone("h_AddEta2Clone2")

  h_Eta4lClone2 = h_Eta4l.Clone("h_Eta4lClone2")
  h_TTEta4lClone2 = h_TTEta4l.Clone("h_TTEta4lClone2")
  h_TLEta4lClone2 = h_TLEta4l.Clone("h_TLEta4lClone2")
  h_LLEta4lClone2 = h_LLEta4l.Clone("h_LLEta4lClone2")
  h_AddEta4lClone2 = h_AddEta4l.Clone("h_AddEta4lClone2")

  h_Pt1Clone2 = h_Pt1.Clone("h_Pt1Clone2")
  h_TTPt1Clone2 = h_TTPt1.Clone("h_TTPt1Clone2")
  h_TLPt1Clone2 = h_TLPt1.Clone("h_TLPt1Clone2")
  h_LLPt1Clone2 = h_LLPt1.Clone("h_LLPt1Clone2")
  h_AddPt1Clone2 = h_AddPt1.Clone("h_AddPt1Clone2")

  h_Pt2Clone2 = h_Pt2.Clone("h_Pt2Clone2")
  h_TTPt2Clone2 = h_TTPt2.Clone("h_TTPt2Clone2")
  h_TLPt2Clone2 = h_TLPt2.Clone("h_TLPt2Clone2")
  h_LLPt2Clone2 = h_LLPt2.Clone("h_LLPt2Clone2")
  h_AddPt2Clone2 = h_AddPt2.Clone("h_AddPt2Clone2")

  h_Pt4lClone2 = h_Pt4l.Clone("h_Pt4lClone2")
  h_TTPt4lClone2 = h_TTPt4l.Clone("h_TTPt4lClone2")
  h_TLPt4lClone2 = h_TLPt4l.Clone("h_TLPt4lClone2")
  h_LLPt4lClone2 = h_LLPt4l.Clone("h_LLPt4lClone2")
  h_AddPt4lClone2 = h_AddPt4l.Clone("h_AddPt4lClone2")



  """
  Renormalize all the histograms whose name has "Clone2" to 1
  """

  h_M1Clone2.Scale(1/h_M1Clone2.Integral())
  h_TTM1Clone2.Scale(1/h_TTM1Clone2.Integral())
  h_TLM1Clone2.Scale(1/h_TLM1Clone2.Integral())
  h_LLM1Clone2.Scale(1/h_LLM1Clone2.Integral())
  h_AddM1Clone2.Scale(1/h_AddM1Clone2.Integral())


  h_M2Clone2.Scale(1/h_M2Clone2.Integral())
  h_TTM2Clone2.Scale(1/h_TTM2Clone2.Integral())
  h_TLM2Clone2.Scale(1/h_TLM2Clone2.Integral())
  h_LLM2Clone2.Scale(1/h_LLM2Clone2.Integral())
  h_AddM2Clone2.Scale(1/h_AddM2Clone2.Integral())

  h_CosTheta1Clone2.Scale(1/h_CosTheta1Clone2.Integral())
  h_TTCosTheta1Clone2.Scale(1/h_TTCosTheta1Clone2.Integral())
  h_TLCosTheta1Clone2.Scale(1/h_TLCosTheta1Clone2.Integral())
  h_LLCosTheta1Clone2.Scale(1/h_LLCosTheta1Clone2.Integral())
  h_AddCosTheta1Clone2.Scale(1/h_AddCosTheta1Clone2.Integral())

  h_CosTheta2Clone2.Scale(1/h_CosTheta2Clone2.Integral())
  h_TTCosTheta2Clone2.Scale(1/h_TTCosTheta2Clone2.Integral())
  h_TLCosTheta2Clone2.Scale(1/h_TLCosTheta2Clone2.Integral())
  h_LLCosTheta2Clone2.Scale(1/h_LLCosTheta2Clone2.Integral())
  h_AddCosTheta2Clone2.Scale(1/h_AddCosTheta2Clone2.Integral())

  h_Theta1Clone2.Scale(1/h_Theta1Clone2.Integral())
  h_TTTheta1Clone2.Scale(1/h_TTTheta1Clone2.Integral())
  h_TLTheta1Clone2.Scale(1/h_TLTheta1Clone2.Integral())
  h_LLTheta1Clone2.Scale(1/h_LLTheta1Clone2.Integral())
  h_AddTheta1Clone2.Scale(1/h_AddTheta1Clone2.Integral())

  h_Theta2Clone2.Scale(1/h_Theta2Clone2.Integral())
  h_TTTheta2Clone2.Scale(1/h_TTTheta2Clone2.Integral())
  h_TLTheta2Clone2.Scale(1/h_TLTheta2Clone2.Integral())
  h_LLTheta2Clone2.Scale(1/h_LLTheta2Clone2.Integral())
  h_AddTheta2Clone2.Scale(1/h_AddTheta2Clone2.Integral())

  h_ThetaStar1Clone2.Scale(1/h_ThetaStar1Clone2.Integral())
  h_TTThetaStar1Clone2.Scale(1/h_TTThetaStar1Clone2.Integral())
  h_TLThetaStar1Clone2.Scale(1/h_TLThetaStar1Clone2.Integral())
  h_LLThetaStar1Clone2.Scale(1/h_LLThetaStar1Clone2.Integral())
  h_AddThetaStar1Clone2.Scale(1/h_AddThetaStar1Clone2.Integral())

  h_ThetaStar2Clone2.Scale(1/h_ThetaStar2Clone2.Integral())
  h_TTThetaStar2Clone2.Scale(1/h_TTThetaStar2Clone2.Integral())
  h_TLThetaStar2Clone2.Scale(1/h_TLThetaStar2Clone2.Integral())
  h_LLThetaStar2Clone2.Scale(1/h_LLThetaStar2Clone2.Integral())
  h_AddThetaStar2Clone2.Scale(1/h_AddThetaStar2Clone2.Integral())

  h_CosThetaStar1Clone2.Scale(1/h_CosThetaStar1Clone2.Integral())
  h_TTCosThetaStar1Clone2.Scale(1/h_TTCosThetaStar1Clone2.Integral())
  h_TLCosThetaStar1Clone2.Scale(1/h_TLCosThetaStar1Clone2.Integral())
  h_LLCosThetaStar1Clone2.Scale(1/h_LLCosThetaStar1Clone2.Integral())
  h_AddCosThetaStar1Clone2.Scale(1/h_AddCosThetaStar1Clone2.Integral())

  h_CosThetaStar2Clone2.Scale(1/h_CosThetaStar2Clone2.Integral())
  h_TTCosThetaStar2Clone2.Scale(1/h_TTCosThetaStar2Clone2.Integral())
  h_TLCosThetaStar2Clone2.Scale(1/h_TLCosThetaStar2Clone2.Integral())
  h_LLCosThetaStar2Clone2.Scale(1/h_LLCosThetaStar2Clone2.Integral())
  h_AddCosThetaStar2Clone2.Scale(1/h_AddCosThetaStar2Clone2.Integral())

  h_PhiClone2.Scale(1/h_PhiClone2.Integral())
  h_TTPhiClone2.Scale(1/h_TTPhiClone2.Integral())
  h_TLPhiClone2.Scale(1/h_TLPhiClone2.Integral())
  h_LLPhiClone2.Scale(1/h_LLPhiClone2.Integral())
  h_AddPhiClone2.Scale(1/h_AddPhiClone2.Integral())

  h_CosPhiClone2.Scale(1/h_CosPhiClone2.Integral())
  h_TTCosPhiClone2.Scale(1/h_TTCosPhiClone2.Integral())
  h_TLCosPhiClone2.Scale(1/h_TLCosPhiClone2.Integral())
  h_LLCosPhiClone2.Scale(1/h_LLCosPhiClone2.Integral())
  h_AddCosPhiClone2.Scale(1/h_AddCosPhiClone2.Integral())

  h_Phi1Clone2.Scale(1/h_Phi1Clone2.Integral())
  h_TTPhi1Clone2.Scale(1/h_TTPhi1Clone2.Integral())
  h_TLPhi1Clone2.Scale(1/h_TLPhi1Clone2.Integral())
  h_LLPhi1Clone2.Scale(1/h_LLPhi1Clone2.Integral())
  h_AddPhi1Clone2.Scale(1/h_AddPhi1Clone2.Integral())

  h_CosPhi1Clone2.Scale(1/h_CosPhi1Clone2.Integral())
  h_TTCosPhi1Clone2.Scale(1/h_TTCosPhi1Clone2.Integral())
  h_TLCosPhi1Clone2.Scale(1/h_TLCosPhi1Clone2.Integral())
  h_LLCosPhi1Clone2.Scale(1/h_LLCosPhi1Clone2.Integral())
  h_AddCosPhi1Clone2.Scale(1/h_AddCosPhi1Clone2.Integral())

  h_M4lClone2.Scale(1/h_M4lClone2.Integral())
  h_TTM4lClone2.Scale(1/h_TTM4lClone2.Integral())
  h_TLM4lClone2.Scale(1/h_TLM4lClone2.Integral())
  h_LLM4lClone2.Scale(1/h_LLM4lClone2.Integral())
  h_AddM4lClone2.Scale(1/h_AddM4lClone2.Integral())

  h_Eta1Clone2.Scale(1/h_Eta1Clone2.Integral())
  h_TTEta1Clone2.Scale(1/h_TTEta1Clone2.Integral())
  h_TLEta1Clone2.Scale(1/h_TLEta1Clone2.Integral())
  h_LLEta1Clone2.Scale(1/h_LLEta1Clone2.Integral())
  h_AddEta1Clone2.Scale(1/h_AddEta1Clone2.Integral())

  h_Eta2Clone2.Scale(1/h_Eta2Clone2.Integral())
  h_TTEta2Clone2.Scale(1/h_TTEta2Clone2.Integral())
  h_TLEta2Clone2.Scale(1/h_TLEta2Clone2.Integral())
  h_LLEta2Clone2.Scale(1/h_LLEta2Clone2.Integral())
  h_AddEta2Clone2.Scale(1/h_AddEta2Clone2.Integral())

  h_Eta4lClone2.Scale(1/h_Eta4lClone2.Integral())
  h_TTEta4lClone2.Scale(1/h_TTEta4lClone2.Integral())
  h_TLEta4lClone2.Scale(1/h_TLEta4lClone2.Integral())
  h_LLEta4lClone2.Scale(1/h_LLEta4lClone2.Integral())
  h_AddEta4lClone2.Scale(1/h_AddEta4lClone2.Integral())

  h_Pt1Clone2.Scale(1/h_Pt1Clone2.Integral())
  h_TTPt1Clone2.Scale(1/h_TTPt1Clone2.Integral())
  h_TLPt1Clone2.Scale(1/h_TLPt1Clone2.Integral())
  h_LLPt1Clone2.Scale(1/h_LLPt1Clone2.Integral())
  h_AddPt1Clone2.Scale(1/h_AddPt1Clone2.Integral())

  h_Pt2Clone2.Scale(1/h_Pt2Clone2.Integral())
  h_TTPt2Clone2.Scale(1/h_TTPt2Clone2.Integral())
  h_TLPt2Clone2.Scale(1/h_TLPt2Clone2.Integral())
  h_LLPt2Clone2.Scale(1/h_LLPt2Clone2.Integral())
  h_AddPt2Clone2.Scale(1/h_AddPt2Clone2.Integral())

  h_Pt4lClone2.Scale(1/h_Pt4lClone2.Integral())
  h_TTPt4lClone2.Scale(1/h_TTPt4lClone2.Integral())
  h_TLPt4lClone2.Scale(1/h_TLPt4lClone2.Integral())
  h_LLPt4lClone2.Scale(1/h_LLPt4lClone2.Integral())
  h_AddPt4lClone2.Scale(1/h_AddPt4lClone2.Integral())



  """
  Put Inclusive, TT, TL, LL, TT+TL+LL in a single histogram
  """

  # remove the Standard Deviation at upper right corner in each histogram
  R.gStyle.SetOptStat(0)



  """
  histogram of M1, TTM1, TLM1, LLM1, TT+TL+LLM1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M1Sum = R.TCanvas("c_M1Sum", "M1Sum", 800, 1000)
  # set the background of this canvas
  c_M1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_M1.Draw("Hist")
  h_M1.Draw("SameHE")
  h_TTM1.Draw("SameHE")
  h_TLM1.Draw("SameHE")
  h_LLM1.Draw("SameHE")
  h_AddM1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLM1Clone1.SetFillColor(2)
  h_TLM1Clone1.SetFillColor(3)
  h_TTM1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_M1.SetLineColor(1)
  h_TTM1.SetLineColor(7)
  h_TLM1.SetLineColor(11)
  h_LLM1.SetLineColor(5)
  h_AddM1.SetLineColor(46)
  # set the width of each histogram's line
  h_M1.SetLineWidth(3)
  h_TTM1.SetLineWidth(3)
  h_TLM1.SetLineWidth(3)
  h_LLM1.SetLineWidth(3)
  h_AddM1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_M1.GetXaxis().SetLabelFont(63)
  hs_M1.GetXaxis().SetLabelSize(16)
  hs_M1.GetYaxis().SetLabelFont(63)
  hs_M1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_M1.GetYaxis().SetTitle("Events")
  hs_M1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_M1.SetMaximum(int(hs_M1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTM1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLM1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLM1Clone1, "LLStack", "F")
  leg.AddEntry(h_M1,"Inclusive","LE")
  leg.AddEntry(h_TTM1,"TT","LE")
  leg.AddEntry(h_TLM1,"TL","LE")
  leg.AddEntry(h_LLM1,"LL","LE")
  leg.AddEntry(h_AddM1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M1Divide.Divide(h_M1, h_AddM1, 1, 1)
  h_TTM1Divide.Divide(h_TTM1, h_AddM1, 1, 1)
  h_TLM1Divide.Divide(h_TLM1, h_AddM1, 1, 1)
  h_LLM1Divide.Divide(h_LLM1, h_AddM1, 1, 1)
  h_AddM1Divide.Divide(h_AddM1, h_AddM1, 1 ,1)

  # draw the histograms of ratio
  h_M1Divide.Draw("HE")
  h_TTM1Divide.Draw("SameHE")
  h_TLM1Divide.Draw("SameHE")
  h_LLM1Divide.Draw("SameHE")
  h_AddM1Divide.Draw("SameHE")
  # set the color of each histogram
  h_M1Divide.SetLineColor(1)
  h_TTM1Divide.SetLineColor(7)
  h_TLM1Divide.SetLineColor(11)
  h_LLM1Divide.SetLineColor(5)
  h_AddM1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_M1Divide.SetLineWidth(3)
  h_TTM1Divide.SetLineWidth(3)
  h_TLM1Divide.SetLineWidth(3)
  h_LLM1Divide.SetLineWidth(3)
  h_AddM1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_M1Divide.GetXaxis().SetLabelFont(63)
  h_M1Divide.GetXaxis().SetLabelSize(16)
  h_M1Divide.GetYaxis().SetLabelFont(63)
  h_M1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M1Divide.GetXaxis().SetTitle("M1/GeV")
  h_M1Divide.GetXaxis().SetTitleSize(0.07)
  h_M1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M1Divide.GetMaximum()
  Max2 = h_TTM1Divide.GetMaximum()
  Max3 = h_TLM1Divide.GetMaximum()
  Max4 = h_LLM1Divide.GetMaximum()
  Max5 = h_AddM1Divide.GetMaximum()
  Min1 = h_M1Divide.GetMinimum()
  Min2 = h_TTM1Divide.GetMinimum()
  Min3 = h_TLM1Divide.GetMinimum()
  Min4 = h_LLM1Divide.GetMinimum()
  Min5 = h_AddM1Divide.GetMinimum()
  h_M1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M1Sum.cd()

  # save the canvas as png file
  c_M1Sum.SaveAs("M1Sum.png")
  # close the canvas
  c_M1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M1SumShape = R.TCanvas("c_M1SumShape", "M1SumShape", 800, 1000)
  # set the background of this canvas
  c_M1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_M1Clone2.Draw("HE")
  h_TTM1Clone2.Draw("SameHE")
  h_TLM1Clone2.Draw("SameHE")
  h_LLM1Clone2.Draw("SameHE")
  h_AddM1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_M1Clone2.SetLineColor(1)
  h_TTM1Clone2.SetLineColor(7)
  h_TLM1Clone2.SetLineColor(11)
  h_LLM1Clone2.SetLineColor(5)
  h_AddM1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_M1Clone2.SetLineWidth(3)
  h_TTM1Clone2.SetLineWidth(3)
  h_TLM1Clone2.SetLineWidth(3)
  h_LLM1Clone2.SetLineWidth(3)
  h_AddM1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_M1Clone2.GetXaxis().SetLabelFont(63)
  h_M1Clone2.GetXaxis().SetLabelSize(16)
  h_M1Clone2.GetYaxis().SetLabelFont(63)
  h_M1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_M1Clone2.GetYaxis().SetTitle("freq.")
  h_M1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_M1Clone2.GetMaximum()
  Max2 = h_TTM1Clone2.GetMaximum()
  Max3 = h_TLM1Clone2.GetMaximum()
  Max4 = h_LLM1Clone2.GetMaximum()
  Max5 = h_AddM1Clone2.GetMaximum()
  h_M1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_M1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTM1Clone2,"TT","LE")
  leg.AddEntry(h_TLM1Clone2,"TL","LE")
  leg.AddEntry(h_LLM1Clone2,"LL","LE")
  leg.AddEntry(h_AddM1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M1DivideShape.Divide(h_M1Clone2, h_AddM1Clone2, 1, 1)
  h_TTM1DivideShape.Divide(h_TTM1Clone2, h_AddM1Clone2, 1, 1)
  h_TLM1DivideShape.Divide(h_TLM1Clone2, h_AddM1Clone2, 1, 1)
  h_LLM1DivideShape.Divide(h_LLM1Clone2, h_AddM1Clone2, 1, 1)
  h_AddM1DivideShape.Divide(h_AddM1Clone2, h_AddM1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_M1DivideShape.Draw("HE")
  h_TTM1DivideShape.Draw("SameHE")
  h_TLM1DivideShape.Draw("SameHE")
  h_LLM1DivideShape.Draw("SameHE")
  h_AddM1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_M1DivideShape.SetLineColor(1)
  h_TTM1DivideShape.SetLineColor(7)
  h_TLM1DivideShape.SetLineColor(11)
  h_LLM1DivideShape.SetLineColor(5)
  h_AddM1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_M1DivideShape.SetLineWidth(3)
  h_TTM1DivideShape.SetLineWidth(3)
  h_TLM1DivideShape.SetLineWidth(3)
  h_LLM1DivideShape.SetLineWidth(3)
  h_AddM1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_M1DivideShape.GetXaxis().SetLabelFont(63)
  h_M1DivideShape.GetXaxis().SetLabelSize(16)
  h_M1DivideShape.GetYaxis().SetLabelFont(63)
  h_M1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M1DivideShape.GetXaxis().SetTitle("M1/GeV")
  h_M1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_M1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M1DivideShape.GetMaximum()
  Max2 = h_TTM1DivideShape.GetMaximum()
  Max3 = h_TLM1DivideShape.GetMaximum()
  Max4 = h_LLM1DivideShape.GetMaximum()
  Max5 = h_AddM1DivideShape.GetMaximum()
  Min1 = h_M1DivideShape.GetMinimum()
  Min2 = h_TTM1DivideShape.GetMinimum()
  Min3 = h_TLM1DivideShape.GetMinimum()
  Min4 = h_LLM1DivideShape.GetMinimum()
  Min5 = h_AddM1DivideShape.GetMinimum()
  h_M1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M1SumShape.cd()


  # save the canvas as png file
  c_M1SumShape.SaveAs("M1ShapeOnly.png")
  # close the canvas
  c_M1SumShape.Close()



  """
  histogram of M2, TTM2, TLM2, LLM2, TT+TL+LLM2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M2Sum = R.TCanvas("c_M2Sum", "M2Sum", 800, 1000)
  # set the background of this canvas
  c_M2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_M2.Draw("Hist")
  h_M2.Draw("SameHE")
  h_TTM2.Draw("SameHE")
  h_TLM2.Draw("SameHE")
  h_LLM2.Draw("SameHE")
  h_AddM2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLM2Clone1.SetFillColor(2)
  h_TLM2Clone1.SetFillColor(3)
  h_TTM2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_M2.SetLineColor(1)
  h_TTM2.SetLineColor(7)
  h_TLM2.SetLineColor(11)
  h_LLM2.SetLineColor(5)
  h_AddM2.SetLineColor(46)
  # set the width of each histogram's line
  h_M2.SetLineWidth(3)
  h_TTM2.SetLineWidth(3)
  h_TLM2.SetLineWidth(3)
  h_LLM2.SetLineWidth(3)
  h_AddM2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_M2.GetXaxis().SetLabelFont(63)
  hs_M2.GetXaxis().SetLabelSize(16)
  hs_M2.GetYaxis().SetLabelFont(63)
  hs_M2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_M2.GetYaxis().SetTitle("Events")
  hs_M2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_M2.SetMaximum(int(hs_M2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTM2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLM2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLM2Clone1, "LLStack", "F")
  leg.AddEntry(h_M2,"Inclusive","LE")
  leg.AddEntry(h_TTM2,"TT","LE")
  leg.AddEntry(h_TLM2,"TL","LE")
  leg.AddEntry(h_LLM2,"LL","LE")
  leg.AddEntry(h_AddM2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M2Divide.Divide(h_M2, h_AddM2, 1, 1)
  h_TTM2Divide.Divide(h_TTM2, h_AddM2, 1, 1)
  h_TLM2Divide.Divide(h_TLM2, h_AddM2, 1, 1)
  h_LLM2Divide.Divide(h_LLM2, h_AddM2, 1, 1)
  h_AddM2Divide.Divide(h_AddM2, h_AddM2, 1 ,1)

  # draw the histograms of ratio
  h_M2Divide.Draw("HE")
  h_TTM2Divide.Draw("SameHE")
  h_TLM2Divide.Draw("SameHE")
  h_LLM2Divide.Draw("SameHE")
  h_AddM2Divide.Draw("SameHE")
  # set the color of each histogram
  h_M2Divide.SetLineColor(1)
  h_TTM2Divide.SetLineColor(7)
  h_TLM2Divide.SetLineColor(11)
  h_LLM2Divide.SetLineColor(5)
  h_AddM2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_M2Divide.SetLineWidth(3)
  h_TTM2Divide.SetLineWidth(3)
  h_TLM2Divide.SetLineWidth(3)
  h_LLM2Divide.SetLineWidth(3)
  h_AddM2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_M2Divide.GetXaxis().SetLabelFont(63)
  h_M2Divide.GetXaxis().SetLabelSize(16)
  h_M2Divide.GetYaxis().SetLabelFont(63)
  h_M2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M2Divide.GetXaxis().SetTitle("M2/GeV")
  h_M2Divide.GetXaxis().SetTitleSize(0.07)
  h_M2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M2Divide.GetMaximum()
  Max2 = h_TTM2Divide.GetMaximum()
  Max3 = h_TLM2Divide.GetMaximum()
  Max4 = h_LLM2Divide.GetMaximum()
  Max5 = h_AddM2Divide.GetMaximum()
  Min1 = h_M2Divide.GetMinimum()
  Min2 = h_TTM2Divide.GetMinimum()
  Min3 = h_TLM2Divide.GetMinimum()
  Min4 = h_LLM2Divide.GetMinimum()
  Min5 = h_AddM2Divide.GetMinimum()
  h_M2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M2Sum.cd()

  # save the canvas as png file
  c_M2Sum.SaveAs("M2Sum.png")
  # close the canvas
  c_M2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M2SumShape = R.TCanvas("c_M2SumShape", "M2SumShape", 800, 1000)
  # set the background of this canvas
  c_M2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_M2Clone2.Draw("HE")
  h_TTM2Clone2.Draw("SameHE")
  h_TLM2Clone2.Draw("SameHE")
  h_LLM2Clone2.Draw("SameHE")
  h_AddM2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_M2Clone2.SetLineColor(1)
  h_TTM2Clone2.SetLineColor(7)
  h_TLM2Clone2.SetLineColor(11)
  h_LLM2Clone2.SetLineColor(5)
  h_AddM2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_M2Clone2.SetLineWidth(3)
  h_TTM2Clone2.SetLineWidth(3)
  h_TLM2Clone2.SetLineWidth(3)
  h_LLM2Clone2.SetLineWidth(3)
  h_AddM2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_M2Clone2.GetXaxis().SetLabelFont(63)
  h_M2Clone2.GetXaxis().SetLabelSize(16)
  h_M2Clone2.GetYaxis().SetLabelFont(63)
  h_M2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_M2Clone2.GetYaxis().SetTitle("freq.")
  h_M2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_M2Clone2.GetMaximum()
  Max2 = h_TTM2Clone2.GetMaximum()
  Max3 = h_TLM2Clone2.GetMaximum()
  Max4 = h_LLM2Clone2.GetMaximum()
  Max5 = h_AddM2Clone2.GetMaximum()
  h_M2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_M2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTM2Clone2,"TT","LE")
  leg.AddEntry(h_TLM2Clone2,"TL","LE")
  leg.AddEntry(h_LLM2Clone2,"LL","LE")
  leg.AddEntry(h_AddM2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M2DivideShape.Divide(h_M2Clone2, h_AddM2Clone2, 1, 1)
  h_TTM2DivideShape.Divide(h_TTM2Clone2, h_AddM2Clone2, 1, 1)
  h_TLM2DivideShape.Divide(h_TLM2Clone2, h_AddM2Clone2, 1, 1)
  h_LLM2DivideShape.Divide(h_LLM2Clone2, h_AddM2Clone2, 1, 1)
  h_AddM2DivideShape.Divide(h_AddM2Clone2, h_AddM2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_M2DivideShape.Draw("HE")
  h_TTM2DivideShape.Draw("SameHE")
  h_TLM2DivideShape.Draw("SameHE")
  h_LLM2DivideShape.Draw("SameHE")
  h_AddM2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_M2DivideShape.SetLineColor(1)
  h_TTM2DivideShape.SetLineColor(7)
  h_TLM2DivideShape.SetLineColor(11)
  h_LLM2DivideShape.SetLineColor(5)
  h_AddM2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_M2DivideShape.SetLineWidth(3)
  h_TTM2DivideShape.SetLineWidth(3)
  h_TLM2DivideShape.SetLineWidth(3)
  h_LLM2DivideShape.SetLineWidth(3)
  h_AddM2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_M2DivideShape.GetXaxis().SetLabelFont(63)
  h_M2DivideShape.GetXaxis().SetLabelSize(16)
  h_M2DivideShape.GetYaxis().SetLabelFont(63)
  h_M2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M2DivideShape.GetXaxis().SetTitle("M2/GeV")
  h_M2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_M2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M2DivideShape.GetMaximum()
  Max2 = h_TTM2DivideShape.GetMaximum()
  Max3 = h_TLM2DivideShape.GetMaximum()
  Max4 = h_LLM2DivideShape.GetMaximum()
  Max5 = h_AddM2DivideShape.GetMaximum()
  Min1 = h_M2DivideShape.GetMinimum()
  Min3 = h_TLM2DivideShape.GetMinimum()
  Min4 = h_LLM2DivideShape.GetMinimum()
  Min5 = h_AddM2DivideShape.GetMinimum()
  h_M2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M2SumShape.cd()

  # save the canvas as png file
  c_M2SumShape.SaveAs("M2ShapeOnly.png")
  # close the canvas
  c_M2SumShape.Close()



  """
  histogram of CosTheta1, TTCosTheta1, TLCosTheta1, LLCosTheta1, TT+TL+LLCosTheta1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta1Sum = R.TCanvas("c_CosTheta1Sum", "CosTheta1Sum", 800, 1000)
  # set the background of this canvas
  c_CosTheta1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosTheta1.Draw("Hist")
  h_CosTheta1.Draw("SameHE")
  h_TTCosTheta1.Draw("SameHE")
  h_TLCosTheta1.Draw("SameHE")
  h_LLCosTheta1.Draw("SameHE")
  h_AddCosTheta1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosTheta1Clone1.SetFillColor(2)
  h_TLCosTheta1Clone1.SetFillColor(3)
  h_TTCosTheta1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosTheta1.SetLineColor(1)
  h_TTCosTheta1.SetLineColor(7)
  h_TLCosTheta1.SetLineColor(11)
  h_LLCosTheta1.SetLineColor(5)
  h_AddCosTheta1.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta1.SetLineWidth(3)
  h_TTCosTheta1.SetLineWidth(3)
  h_TLCosTheta1.SetLineWidth(3)
  h_LLCosTheta1.SetLineWidth(3)
  h_AddCosTheta1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosTheta1.GetXaxis().SetLabelFont(63)
  hs_CosTheta1.GetXaxis().SetLabelSize(16)
  hs_CosTheta1.GetYaxis().SetLabelFont(63)
  hs_CosTheta1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosTheta1.GetYaxis().SetTitle("Events")
  hs_CosTheta1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosTheta1.SetMaximum(int(hs_CosTheta1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosTheta1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLCosTheta1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLCosTheta1Clone1, "LLStack", "F")
  leg.AddEntry(h_CosTheta1,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta1,"TT","LE")
  leg.AddEntry(h_TLCosTheta1,"TL","LE")
  leg.AddEntry(h_LLCosTheta1,"LL","LE")
  leg.AddEntry(h_AddCosTheta1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosTheta1Divide.Divide(h_CosTheta1, h_AddCosTheta1, 1, 1)
  h_TTCosTheta1Divide.Divide(h_TTCosTheta1, h_AddCosTheta1, 1, 1)
  h_TLCosTheta1Divide.Divide(h_TLCosTheta1, h_AddCosTheta1, 1, 1)
  h_LLCosTheta1Divide.Divide(h_LLCosTheta1, h_AddCosTheta1, 1, 1)
  h_AddCosTheta1Divide.Divide(h_AddCosTheta1, h_AddCosTheta1, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta1Divide.Draw("HE")
  h_TTCosTheta1Divide.Draw("SameHE")
  h_TLCosTheta1Divide.Draw("SameHE")
  h_LLCosTheta1Divide.Draw("SameHE")
  h_AddCosTheta1Divide.Draw("SameHE")
  # set the color of each histogram
  h_CosTheta1Divide.SetLineColor(1)
  h_TTCosTheta1Divide.SetLineColor(7)
  h_TLCosTheta1Divide.SetLineColor(11)
  h_LLCosTheta1Divide.SetLineColor(5)
  h_AddCosTheta1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta1Divide.SetLineWidth(3)
  h_TTCosTheta1Divide.SetLineWidth(3)
  h_TLCosTheta1Divide.SetLineWidth(3)
  h_LLCosTheta1Divide.SetLineWidth(3)
  h_AddCosTheta1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta1Divide.GetXaxis().SetLabelFont(63)
  h_CosTheta1Divide.GetXaxis().SetLabelSize(16)
  h_CosTheta1Divide.GetYaxis().SetLabelFont(63)
  h_CosTheta1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta1Divide.GetXaxis().SetTitle("CosTheta1")
  h_CosTheta1Divide.GetXaxis().SetTitleSize(0.07)
  h_CosTheta1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta1Divide.GetMaximum()
  Max2 = h_TTCosTheta1Divide.GetMaximum()
  Max3 = h_TLCosTheta1Divide.GetMaximum()
  Max4 = h_LLCosTheta1Divide.GetMaximum()
  Max5 = h_AddCosTheta1Divide.GetMaximum()
  Min1 = h_CosTheta1Divide.GetMinimum()
  Min2 = h_TTCosTheta1Divide.GetMinimum()
  Min3 = h_TLCosTheta1Divide.GetMinimum()
  Min4 = h_LLCosTheta1Divide.GetMinimum()
  Min5 = h_AddCosTheta1Divide.GetMinimum()
  h_CosTheta1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta1Sum.cd()

  # save the canvas as png file
  c_CosTheta1Sum.SaveAs("CosTheta1Sum.png")
  # close the canvas
  c_CosTheta1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta1SumShape = R.TCanvas("c_CosTheta1SumShape", "CosTheta1SumShape", 800, 1000)
  # set the background of this canvas
  c_CosTheta1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosTheta1Clone2.Draw("HE")
  h_TTCosTheta1Clone2.Draw("SameHE")
  h_TLCosTheta1Clone2.Draw("SameHE")
  h_LLCosTheta1Clone2.Draw("SameHE")
  h_AddCosTheta1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosTheta1Clone2.SetLineColor(1)
  h_TTCosTheta1Clone2.SetLineColor(7)
  h_TLCosTheta1Clone2.SetLineColor(11)
  h_LLCosTheta1Clone2.SetLineColor(5)
  h_AddCosTheta1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta1Clone2.SetLineWidth(3)
  h_TTCosTheta1Clone2.SetLineWidth(3)
  h_TLCosTheta1Clone2.SetLineWidth(3)
  h_LLCosTheta1Clone2.SetLineWidth(3)
  h_AddCosTheta1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosTheta1Clone2.GetXaxis().SetLabelFont(63)
  h_CosTheta1Clone2.GetXaxis().SetLabelSize(16)
  h_CosTheta1Clone2.GetYaxis().SetLabelFont(63)
  h_CosTheta1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosTheta1Clone2.GetYaxis().SetTitle("freq.")
  h_CosTheta1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosTheta1Clone2.GetMaximum()
  Max2 = h_TTCosTheta1Clone2.GetMaximum()
  Max3 = h_TLCosTheta1Clone2.GetMaximum()
  Max4 = h_LLCosTheta1Clone2.GetMaximum()
  Max5 = h_AddCosTheta1Clone2.GetMaximum()
  h_CosTheta1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosTheta1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta1Clone2,"TT","LE")
  leg.AddEntry(h_TLCosTheta1Clone2,"TL","LE")
  leg.AddEntry(h_LLCosTheta1Clone2,"LL","LE")
  leg.AddEntry(h_AddCosTheta1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosTheta1DivideShape.Divide(h_CosTheta1Clone2, h_AddCosTheta1Clone2, 1, 1)
  h_TTCosTheta1DivideShape.Divide(h_TTCosTheta1Clone2, h_AddCosTheta1Clone2, 1, 1)
  h_TLCosTheta1DivideShape.Divide(h_TLCosTheta1Clone2, h_AddCosTheta1Clone2, 1, 1)
  h_LLCosTheta1DivideShape.Divide(h_LLCosTheta1Clone2, h_AddCosTheta1Clone2, 1, 1)
  h_AddCosTheta1DivideShape.Divide(h_AddCosTheta1Clone2, h_AddCosTheta1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta1DivideShape.Draw("HE")
  h_TTCosTheta1DivideShape.Draw("SameHE")
  h_TLCosTheta1DivideShape.Draw("SameHE")
  h_LLCosTheta1DivideShape.Draw("SameHE")
  h_AddCosTheta1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosTheta1DivideShape.SetLineColor(1)
  h_TTCosTheta1DivideShape.SetLineColor(7)
  h_TLCosTheta1DivideShape.SetLineColor(11)
  h_LLCosTheta1DivideShape.SetLineColor(5)
  h_AddCosTheta1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta1DivideShape.SetLineWidth(3)
  h_TTCosTheta1DivideShape.SetLineWidth(3)
  h_TLCosTheta1DivideShape.SetLineWidth(3)
  h_LLCosTheta1DivideShape.SetLineWidth(3)
  h_AddCosTheta1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta1DivideShape.GetXaxis().SetLabelFont(63)
  h_CosTheta1DivideShape.GetXaxis().SetLabelSize(16)
  h_CosTheta1DivideShape.GetYaxis().SetLabelFont(63)
  h_CosTheta1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta1DivideShape.GetXaxis().SetTitle("CosTheta1")
  h_CosTheta1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosTheta1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta1DivideShape.GetMaximum()
  Max2 = h_TTCosTheta1DivideShape.GetMaximum()
  Max3 = h_TLCosTheta1DivideShape.GetMaximum()
  Max4 = h_LLCosTheta1DivideShape.GetMaximum()
  Max5 = h_AddCosTheta1DivideShape.GetMaximum()
  Min1 = h_CosTheta1DivideShape.GetMinimum()
  Min2 = h_TTCosTheta1DivideShape.GetMinimum()
  Min3 = h_TLCosTheta1DivideShape.GetMinimum()
  Min4 = h_LLCosTheta1DivideShape.GetMinimum()
  Min5 = h_AddCosTheta1DivideShape.GetMinimum()
  h_CosTheta1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta1SumShape.cd()


  # save the canvas as png file
  c_CosTheta1SumShape.SaveAs("CosTheta1ShapeOnly.png")
  # close the canvas
  c_CosTheta1SumShape.Close()



  """
  histogram of CosTheta2, TTCosTheta2, TLCosTheta2, LLCosTheta2, TT+TL+LLCosTheta2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta2Sum = R.TCanvas("c_CosTheta2Sum", "CosTheta2Sum", 800, 1000)
  # set the background of this canvas
  c_CosTheta2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosTheta2.Draw("Hist")
  h_CosTheta2.Draw("SameHE")
  h_TTCosTheta2.Draw("SameHE")
  h_TLCosTheta2.Draw("SameHE")
  h_LLCosTheta2.Draw("SameHE")
  h_AddCosTheta2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosTheta2Clone1.SetFillColor(2)
  h_TLCosTheta2Clone1.SetFillColor(3)
  h_TTCosTheta2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosTheta2.SetLineColor(1)
  h_TTCosTheta2.SetLineColor(7)
  h_TLCosTheta2.SetLineColor(11)
  h_LLCosTheta2.SetLineColor(5)
  h_AddCosTheta2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta2.SetLineWidth(3)
  h_TTCosTheta2.SetLineWidth(3)
  h_TLCosTheta2.SetLineWidth(3)
  h_LLCosTheta2.SetLineWidth(3)
  h_AddCosTheta2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosTheta2.GetXaxis().SetLabelFont(63)
  hs_CosTheta2.GetXaxis().SetLabelSize(16)
  hs_CosTheta2.GetYaxis().SetLabelFont(63)
  hs_CosTheta2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosTheta2.GetYaxis().SetTitle("Events")
  hs_CosTheta2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosTheta2.SetMaximum(int(hs_CosTheta2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosTheta2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLCosTheta2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLCosTheta2Clone1, "LLStack", "F")
  leg.AddEntry(h_CosTheta2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta2,"TT","LE")
  leg.AddEntry(h_TLCosTheta2,"TL","LE")
  leg.AddEntry(h_LLCosTheta2,"LL","LE")
  leg.AddEntry(h_AddCosTheta2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosTheta2Divide.Divide(h_CosTheta2, h_AddCosTheta2, 1, 1)
  h_TTCosTheta2Divide.Divide(h_TTCosTheta2, h_AddCosTheta2, 1, 1)
  h_TLCosTheta2Divide.Divide(h_TLCosTheta2, h_AddCosTheta2, 1, 1)
  h_LLCosTheta2Divide.Divide(h_LLCosTheta2, h_AddCosTheta2, 1, 1)
  h_AddCosTheta2Divide.Divide(h_AddCosTheta2, h_AddCosTheta2, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta2Divide.Draw("HE")
  h_TTCosTheta2Divide.Draw("SameHE")
  h_TLCosTheta2Divide.Draw("SameHE")
  h_LLCosTheta2Divide.Draw("SameHE")
  h_AddCosTheta2Divide.Draw("SameHE")
  # set the color of each histogram
  h_CosTheta2Divide.SetLineColor(1)
  h_TTCosTheta2Divide.SetLineColor(7)
  h_TLCosTheta2Divide.SetLineColor(11)
  h_LLCosTheta2Divide.SetLineColor(5)
  h_AddCosTheta2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta2Divide.SetLineWidth(3)
  h_TTCosTheta2Divide.SetLineWidth(3)
  h_TLCosTheta2Divide.SetLineWidth(3)
  h_LLCosTheta2Divide.SetLineWidth(3)
  h_AddCosTheta2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta2Divide.GetXaxis().SetLabelFont(63)
  h_CosTheta2Divide.GetXaxis().SetLabelSize(16)
  h_CosTheta2Divide.GetYaxis().SetLabelFont(63)
  h_CosTheta2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta2Divide.GetXaxis().SetTitle("CosTheta2")
  h_CosTheta2Divide.GetXaxis().SetTitleSize(0.07)
  h_CosTheta2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta2Divide.GetMaximum()
  Max2 = h_TTCosTheta2Divide.GetMaximum()
  Max3 = h_TLCosTheta2Divide.GetMaximum()
  Max4 = h_LLCosTheta2Divide.GetMaximum()
  Max5 = h_AddCosTheta2Divide.GetMaximum()
  Min1 = h_CosTheta2Divide.GetMinimum()
  Min2 = h_TTCosTheta2Divide.GetMinimum()
  Min3 = h_TLCosTheta2Divide.GetMinimum()
  Min4 = h_LLCosTheta2Divide.GetMinimum()
  Min5 = h_AddCosTheta2Divide.GetMinimum()
  h_CosTheta2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta2Sum.cd()

  # save the canvas as png file
  c_CosTheta2Sum.SaveAs("CosTheta2Sum.png")
  # close the canvas
  c_CosTheta2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta2SumShape = R.TCanvas("c_CosTheta2SumShape", "CosTheta2SumShape", 800, 1000)
  # set the background of this canvas
  c_CosTheta2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosTheta2Clone2.Draw("HE")
  h_TTCosTheta2Clone2.Draw("SameHE")
  h_TLCosTheta2Clone2.Draw("SameHE")
  h_LLCosTheta2Clone2.Draw("SameHE")
  h_AddCosTheta2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosTheta2Clone2.SetLineColor(1)
  h_TTCosTheta2Clone2.SetLineColor(7)
  h_TLCosTheta2Clone2.SetLineColor(11)
  h_LLCosTheta2Clone2.SetLineColor(5)
  h_AddCosTheta2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta2Clone2.SetLineWidth(3)
  h_TTCosTheta2Clone2.SetLineWidth(3)
  h_TLCosTheta2Clone2.SetLineWidth(3)
  h_LLCosTheta2Clone2.SetLineWidth(3)
  h_AddCosTheta2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosTheta2Clone2.GetXaxis().SetLabelFont(63)
  h_CosTheta2Clone2.GetXaxis().SetLabelSize(16)
  h_CosTheta2Clone2.GetYaxis().SetLabelFont(63)
  h_CosTheta2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosTheta2Clone2.GetYaxis().SetTitle("freq.")
  h_CosTheta2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosTheta2Clone2.GetMaximum()
  Max2 = h_TTCosTheta2Clone2.GetMaximum()
  Max3 = h_TLCosTheta2Clone2.GetMaximum()
  Max4 = h_LLCosTheta2Clone2.GetMaximum()
  Max5 = h_AddCosTheta2Clone2.GetMaximum()
  h_CosTheta2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosTheta2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta2Clone2,"TT","LE")
  leg.AddEntry(h_TLCosTheta2Clone2,"TL","LE")
  leg.AddEntry(h_LLCosTheta2Clone2,"LL","LE")
  leg.AddEntry(h_AddCosTheta2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosTheta2DivideShape.Divide(h_CosTheta2Clone2, h_AddCosTheta2Clone2, 1, 1)
  h_TTCosTheta2DivideShape.Divide(h_TTCosTheta2Clone2, h_AddCosTheta2Clone2, 1, 1)
  h_TLCosTheta2DivideShape.Divide(h_TLCosTheta2Clone2, h_AddCosTheta2Clone2, 1, 1)
  h_LLCosTheta2DivideShape.Divide(h_LLCosTheta2Clone2, h_AddCosTheta2Clone2, 1, 1)
  h_AddCosTheta2DivideShape.Divide(h_AddCosTheta2Clone2, h_AddCosTheta2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta2DivideShape.Draw("HE")
  h_TTCosTheta2DivideShape.Draw("SameHE")
  h_TLCosTheta2DivideShape.Draw("SameHE")
  h_LLCosTheta2DivideShape.Draw("SameHE")
  h_AddCosTheta2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosTheta2DivideShape.SetLineColor(1)
  h_TTCosTheta2DivideShape.SetLineColor(7)
  h_TLCosTheta2DivideShape.SetLineColor(11)
  h_LLCosTheta2DivideShape.SetLineColor(5)
  h_AddCosTheta2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta2DivideShape.SetLineWidth(3)
  h_TTCosTheta2DivideShape.SetLineWidth(3)
  h_TLCosTheta2DivideShape.SetLineWidth(3)
  h_LLCosTheta2DivideShape.SetLineWidth(3)
  h_AddCosTheta2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta2DivideShape.GetXaxis().SetLabelFont(63)
  h_CosTheta2DivideShape.GetXaxis().SetLabelSize(16)
  h_CosTheta2DivideShape.GetYaxis().SetLabelFont(63)
  h_CosTheta2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta2DivideShape.GetXaxis().SetTitle("CosTheta2")
  h_CosTheta2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosTheta2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta2DivideShape.GetMaximum()
  Max2 = h_TTCosTheta2DivideShape.GetMaximum()
  Max3 = h_TLCosTheta2DivideShape.GetMaximum()
  Max4 = h_LLCosTheta2DivideShape.GetMaximum()
  Max5 = h_AddCosTheta2DivideShape.GetMaximum()
  Min1 = h_CosTheta2DivideShape.GetMinimum()
  Min2 = h_TTCosTheta2DivideShape.GetMinimum()
  Min3 = h_TLCosTheta2DivideShape.GetMinimum()
  Min4 = h_LLCosTheta2DivideShape.GetMinimum()
  Min5 = h_AddCosTheta2DivideShape.GetMinimum()
  h_CosTheta2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta2SumShape.cd()


  # save the canvas as png file
  c_CosTheta2SumShape.SaveAs("CosTheta2ShapeOnly.png")
  # close the canvas
  c_CosTheta2SumShape.Close()



  """
  histogram of Theta1, TTTheta1, TLTheta1, LLTheta1, TT+TL+LLTheta1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Theta1Sum = R.TCanvas("c_Theta1Sum", "Theta1Sum", 800, 1000)
  # set the background of this canvas
  c_Theta1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_Theta1.Draw("Hist")
  h_Theta1.Draw("SameHE")
  h_TTTheta1.Draw("SameHE")
  h_TLTheta1.Draw("SameHE")
  h_LLTheta1.Draw("SameHE")
  h_AddTheta1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLTheta1Clone1.SetFillColor(2)
  h_TLTheta1Clone1.SetFillColor(3)
  h_TTTheta1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Theta1.SetLineColor(1)
  h_TTTheta1.SetLineColor(7)
  h_TLTheta1.SetLineColor(11)
  h_LLTheta1.SetLineColor(5)
  h_AddTheta1.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta1.SetLineWidth(3)
  h_TTTheta1.SetLineWidth(3)
  h_TLTheta1.SetLineWidth(3)
  h_LLTheta1.SetLineWidth(3)
  h_AddTheta1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Theta1.GetXaxis().SetLabelFont(63)
  hs_Theta1.GetXaxis().SetLabelSize(16)
  hs_Theta1.GetYaxis().SetLabelFont(63)
  hs_Theta1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Theta1.GetYaxis().SetTitle("Events")
  hs_Theta1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Theta1.SetMaximum(int(hs_Theta1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTTheta1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLTheta1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLTheta1Clone1, "LLStack", "F")
  leg.AddEntry(h_Theta1,"Inclusive","LE")
  leg.AddEntry(h_TTTheta1,"TT","LE")
  leg.AddEntry(h_TLTheta1,"TL","LE")
  leg.AddEntry(h_LLTheta1,"LL","LE")
  leg.AddEntry(h_AddTheta1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Theta1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Theta1Divide.Divide(h_Theta1, h_AddTheta1, 1, 1)
  h_TTTheta1Divide.Divide(h_TTTheta1, h_AddTheta1, 1, 1)
  h_TLTheta1Divide.Divide(h_TLTheta1, h_AddTheta1, 1, 1)
  h_LLTheta1Divide.Divide(h_LLTheta1, h_AddTheta1, 1, 1)
  h_AddTheta1Divide.Divide(h_AddTheta1, h_AddTheta1, 1 ,1)

  # draw the histograms of ratio
  h_Theta1Divide.Draw("HE")
  h_TTTheta1Divide.Draw("SameHE")
  h_TLTheta1Divide.Draw("SameHE")
  h_LLTheta1Divide.Draw("SameHE")
  h_AddTheta1Divide.Draw("SameHE")
  # set the color of each histogram
  h_Theta1Divide.SetLineColor(1)
  h_TTTheta1Divide.SetLineColor(7)
  h_TLTheta1Divide.SetLineColor(11)
  h_LLTheta1Divide.SetLineColor(5)
  h_AddTheta1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta1Divide.SetLineWidth(3)
  h_TTTheta1Divide.SetLineWidth(3)
  h_TLTheta1Divide.SetLineWidth(3)
  h_LLTheta1Divide.SetLineWidth(3)
  h_AddTheta1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Theta1Divide.GetXaxis().SetLabelFont(63)
  h_Theta1Divide.GetXaxis().SetLabelSize(16)
  h_Theta1Divide.GetYaxis().SetLabelFont(63)
  h_Theta1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Theta1Divide.GetXaxis().SetTitle("Theta1")
  h_Theta1Divide.GetXaxis().SetTitleSize(0.07)
  h_Theta1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Theta1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Theta1Divide.GetMaximum()
  Max2 = h_TTTheta1Divide.GetMaximum()
  Max3 = h_TLTheta1Divide.GetMaximum()
  Max4 = h_LLTheta1Divide.GetMaximum()
  Max5 = h_AddTheta1Divide.GetMaximum()
  Min1 = h_Theta1Divide.GetMinimum()
  Min2 = h_TTTheta1Divide.GetMinimum()
  Min3 = h_TLTheta1Divide.GetMinimum()
  Min4 = h_LLTheta1Divide.GetMinimum()
  Min5 = h_AddTheta1Divide.GetMinimum()
  h_Theta1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Theta1Sum.cd()

  # save the canvas as png file
  c_Theta1Sum.SaveAs("Theta1Sum.png")
  # close the canvas
  c_Theta1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Theta1SumShape = R.TCanvas("c_Theta1SumShape", "Theta1SumShape", 800, 1000)
  # set the background of this canvas
  c_Theta1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Theta1Clone2.Draw("HE")
  h_TTTheta1Clone2.Draw("SameHE")
  h_TLTheta1Clone2.Draw("SameHE")
  h_LLTheta1Clone2.Draw("SameHE")
  h_AddTheta1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Theta1Clone2.SetLineColor(1)
  h_TTTheta1Clone2.SetLineColor(7)
  h_TLTheta1Clone2.SetLineColor(11)
  h_LLTheta1Clone2.SetLineColor(5)
  h_AddTheta1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta1Clone2.SetLineWidth(3)
  h_TTTheta1Clone2.SetLineWidth(3)
  h_TLTheta1Clone2.SetLineWidth(3)
  h_LLTheta1Clone2.SetLineWidth(3)
  h_AddTheta1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Theta1Clone2.GetXaxis().SetLabelFont(63)
  h_Theta1Clone2.GetXaxis().SetLabelSize(16)
  h_Theta1Clone2.GetYaxis().SetLabelFont(63)
  h_Theta1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Theta1Clone2.GetYaxis().SetTitle("freq.")
  h_Theta1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Theta1Clone2.GetMaximum()
  Max2 = h_TTTheta1Clone2.GetMaximum()
  Max3 = h_TLTheta1Clone2.GetMaximum()
  Max4 = h_LLTheta1Clone2.GetMaximum()
  Max5 = h_AddTheta1Clone2.GetMaximum()
  h_Theta1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Theta1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTTheta1Clone2,"TT","LE")
  leg.AddEntry(h_TLTheta1Clone2,"TL","LE")
  leg.AddEntry(h_LLTheta1Clone2,"LL","LE")
  leg.AddEntry(h_AddTheta1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Theta1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Theta1DivideShape.Divide(h_Theta1Clone2, h_AddTheta1Clone2, 1, 1)
  h_TTTheta1DivideShape.Divide(h_TTTheta1Clone2, h_AddTheta1Clone2, 1, 1)
  h_TLTheta1DivideShape.Divide(h_TLTheta1Clone2, h_AddTheta1Clone2, 1, 1)
  h_LLTheta1DivideShape.Divide(h_LLTheta1Clone2, h_AddTheta1Clone2, 1, 1)
  h_AddTheta1DivideShape.Divide(h_AddTheta1Clone2, h_AddTheta1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Theta1DivideShape.Draw("HE")
  h_TTTheta1DivideShape.Draw("SameHE")
  h_TLTheta1DivideShape.Draw("SameHE")
  h_LLTheta1DivideShape.Draw("SameHE")
  h_AddTheta1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Theta1DivideShape.SetLineColor(1)
  h_TTTheta1DivideShape.SetLineColor(7)
  h_TLTheta1DivideShape.SetLineColor(11)
  h_LLTheta1DivideShape.SetLineColor(5)
  h_AddTheta1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta1DivideShape.SetLineWidth(3)
  h_TTTheta1DivideShape.SetLineWidth(3)
  h_TLTheta1DivideShape.SetLineWidth(3)
  h_LLTheta1DivideShape.SetLineWidth(3)
  h_AddTheta1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Theta1DivideShape.GetXaxis().SetLabelFont(63)
  h_Theta1DivideShape.GetXaxis().SetLabelSize(16)
  h_Theta1DivideShape.GetYaxis().SetLabelFont(63)
  h_Theta1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Theta1DivideShape.GetXaxis().SetTitle("Theta1")
  h_Theta1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Theta1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Theta1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Theta1DivideShape.GetMaximum()
  Max2 = h_TTTheta1DivideShape.GetMaximum()
  Max3 = h_TLTheta1DivideShape.GetMaximum()
  Max4 = h_LLTheta1DivideShape.GetMaximum()
  Max5 = h_AddTheta1DivideShape.GetMaximum()
  Min1 = h_Theta1DivideShape.GetMinimum()
  Min2 = h_TTTheta1DivideShape.GetMinimum()
  Min3 = h_TLTheta1DivideShape.GetMinimum()
  Min4 = h_LLTheta1DivideShape.GetMinimum()
  Min5 = h_AddTheta1DivideShape.GetMinimum()
  h_Theta1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Theta1SumShape.cd()


  # save the canvas as png file
  c_Theta1SumShape.SaveAs("Theta1ShapeOnly.png")
  # close the canvas
  c_Theta1SumShape.Close()



  """
  histogram of Theta2, TTTheta2, TLTheta2, LLTheta2, TT+TL+LLTheta2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Theta2Sum = R.TCanvas("c_Theta2Sum", "Theta2Sum", 800, 1000)
  # set the background of this canvas
  c_Theta2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_Theta2.Draw("Hist")
  h_Theta2.Draw("SameHE")
  h_TTTheta2.Draw("SameHE")
  h_TLTheta2.Draw("SameHE")
  h_LLTheta2.Draw("SameHE")
  h_AddTheta2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLTheta2Clone1.SetFillColor(2)
  h_TLTheta2Clone1.SetFillColor(3)
  h_TTTheta2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Theta2.SetLineColor(1)
  h_TTTheta2.SetLineColor(7)
  h_TLTheta2.SetLineColor(11)
  h_LLTheta2.SetLineColor(5)
  h_AddTheta2.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta2.SetLineWidth(3)
  h_TTTheta2.SetLineWidth(3)
  h_TLTheta2.SetLineWidth(3)
  h_LLTheta2.SetLineWidth(3)
  h_AddTheta2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Theta2.GetXaxis().SetLabelFont(63)
  hs_Theta2.GetXaxis().SetLabelSize(16)
  hs_Theta2.GetYaxis().SetLabelFont(63)
  hs_Theta2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Theta2.GetYaxis().SetTitle("Events")
  hs_Theta2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Theta2.SetMaximum(int(hs_Theta2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTTheta2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLTheta2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLTheta2Clone1, "LLStack", "F")
  leg.AddEntry(h_Theta2,"Inclusive","LE")
  leg.AddEntry(h_TTTheta2,"TT","LE")
  leg.AddEntry(h_TLTheta2,"TL","LE")
  leg.AddEntry(h_LLTheta2,"LL","LE")
  leg.AddEntry(h_AddTheta2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Theta2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Theta2Divide.Divide(h_Theta2, h_AddTheta2, 1, 1)
  h_TTTheta2Divide.Divide(h_TTTheta2, h_AddTheta2, 1, 1)
  h_TLTheta2Divide.Divide(h_TLTheta2, h_AddTheta2, 1, 1)
  h_LLTheta2Divide.Divide(h_LLTheta2, h_AddTheta2, 1, 1)
  h_AddTheta2Divide.Divide(h_AddTheta2, h_AddTheta2, 1 ,1)

  # draw the histograms of ratio
  h_Theta2Divide.Draw("HE")
  h_TTTheta2Divide.Draw("SameHE")
  h_TLTheta2Divide.Draw("SameHE")
  h_LLTheta2Divide.Draw("SameHE")
  h_AddTheta2Divide.Draw("SameHE")
  # set the color of each histogram
  h_Theta2Divide.SetLineColor(1)
  h_TTTheta2Divide.SetLineColor(7)
  h_TLTheta2Divide.SetLineColor(11)
  h_LLTheta2Divide.SetLineColor(5)
  h_AddTheta2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta2Divide.SetLineWidth(3)
  h_TTTheta2Divide.SetLineWidth(3)
  h_TLTheta2Divide.SetLineWidth(3)
  h_LLTheta2Divide.SetLineWidth(3)
  h_AddTheta2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Theta2Divide.GetXaxis().SetLabelFont(63)
  h_Theta2Divide.GetXaxis().SetLabelSize(16)
  h_Theta2Divide.GetYaxis().SetLabelFont(63)
  h_Theta2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Theta2Divide.GetXaxis().SetTitle("Theta2")
  h_Theta2Divide.GetXaxis().SetTitleSize(0.07)
  h_Theta2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Theta2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Theta2Divide.GetMaximum()
  Max2 = h_TTTheta2Divide.GetMaximum()
  Max3 = h_TLTheta2Divide.GetMaximum()
  Max4 = h_LLTheta2Divide.GetMaximum()
  Max5 = h_AddTheta2Divide.GetMaximum()
  Min1 = h_Theta2Divide.GetMinimum()
  Min2 = h_TTTheta2Divide.GetMinimum()
  Min3 = h_TLTheta2Divide.GetMinimum()
  Min4 = h_LLTheta2Divide.GetMinimum()
  Min5 = h_AddTheta2Divide.GetMinimum()
  h_Theta2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Theta2Sum.cd()

  # save the canvas as png file
  c_Theta2Sum.SaveAs("Theta2Sum.png")
  # close the canvas
  c_Theta2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Theta2SumShape = R.TCanvas("c_Theta2SumShape", "Theta2SumShape", 800, 1000)
  # set the background of this canvas
  c_Theta2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Theta2Clone2.Draw("HE")
  h_TTTheta2Clone2.Draw("SameHE")
  h_TLTheta2Clone2.Draw("SameHE")
  h_LLTheta2Clone2.Draw("SameHE")
  h_AddTheta2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Theta2Clone2.SetLineColor(1)
  h_TTTheta2Clone2.SetLineColor(7)
  h_TLTheta2Clone2.SetLineColor(11)
  h_LLTheta2Clone2.SetLineColor(5)
  h_AddTheta2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta2Clone2.SetLineWidth(3)
  h_TTTheta2Clone2.SetLineWidth(3)
  h_TLTheta2Clone2.SetLineWidth(3)
  h_LLTheta2Clone2.SetLineWidth(3)
  h_AddTheta2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Theta2Clone2.GetXaxis().SetLabelFont(63)
  h_Theta2Clone2.GetXaxis().SetLabelSize(16)
  h_Theta2Clone2.GetYaxis().SetLabelFont(63)
  h_Theta2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Theta2Clone2.GetYaxis().SetTitle("freq.")
  h_Theta2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Theta2Clone2.GetMaximum()
  Max2 = h_TTTheta2Clone2.GetMaximum()
  Max3 = h_TLTheta2Clone2.GetMaximum()
  Max4 = h_LLTheta2Clone2.GetMaximum()
  Max5 = h_AddTheta2Clone2.GetMaximum()
  h_Theta2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Theta2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTTheta2Clone2,"TT","LE")
  leg.AddEntry(h_TLTheta2Clone2,"TL","LE")
  leg.AddEntry(h_LLTheta2Clone2,"LL","LE")
  leg.AddEntry(h_AddTheta2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Theta2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Theta2DivideShape.Divide(h_Theta2Clone2, h_AddTheta2Clone2, 1, 1)
  h_TTTheta2DivideShape.Divide(h_TTTheta2Clone2, h_AddTheta2Clone2, 1, 1)
  h_TLTheta2DivideShape.Divide(h_TLTheta2Clone2, h_AddTheta2Clone2, 1, 1)
  h_LLTheta2DivideShape.Divide(h_LLTheta2Clone2, h_AddTheta2Clone2, 1, 1)
  h_AddTheta2DivideShape.Divide(h_AddTheta2Clone2, h_AddTheta2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Theta2DivideShape.Draw("HE")
  h_TTTheta2DivideShape.Draw("SameHE")
  h_TLTheta2DivideShape.Draw("SameHE")
  h_LLTheta2DivideShape.Draw("SameHE")
  h_AddTheta2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Theta2DivideShape.SetLineColor(1)
  h_TTTheta2DivideShape.SetLineColor(7)
  h_TLTheta2DivideShape.SetLineColor(11)
  h_LLTheta2DivideShape.SetLineColor(5)
  h_AddTheta2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Theta2DivideShape.SetLineWidth(3)
  h_TTTheta2DivideShape.SetLineWidth(3)
  h_TLTheta2DivideShape.SetLineWidth(3)
  h_LLTheta2DivideShape.SetLineWidth(3)
  h_AddTheta2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Theta2DivideShape.GetXaxis().SetLabelFont(63)
  h_Theta2DivideShape.GetXaxis().SetLabelSize(16)
  h_Theta2DivideShape.GetYaxis().SetLabelFont(63)
  h_Theta2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Theta2DivideShape.GetXaxis().SetTitle("Theta2")
  h_Theta2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Theta2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Theta2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Theta2DivideShape.GetMaximum()
  Max2 = h_TTTheta2DivideShape.GetMaximum()
  Max3 = h_TLTheta2DivideShape.GetMaximum()
  Max4 = h_LLTheta2DivideShape.GetMaximum()
  Max5 = h_AddTheta2DivideShape.GetMaximum()
  Min1 = h_Theta2DivideShape.GetMinimum()
  Min2 = h_TTTheta2DivideShape.GetMinimum()
  Min3 = h_TLTheta2DivideShape.GetMinimum()
  Min4 = h_LLTheta2DivideShape.GetMinimum()
  Min5 = h_AddTheta2DivideShape.GetMinimum()
  h_Theta2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Theta2SumShape.cd()


  # save the canvas as png file
  c_Theta2SumShape.SaveAs("Theta2ShapeOnly.png")
  # close the canvas
  c_Theta2SumShape.Close()



  """
  histogram of ThetaStar1, TTThetaStar1, TLThetaStar1, LLThetaStar1, TT+TL+LLThetaStar1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_ThetaStar1Sum = R.TCanvas("c_ThetaStar1Sum", "ThetaStar1Sum", 800, 1000)
  # set the background of this canvas
  c_ThetaStar1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_ThetaStar1.Draw("Hist")
  h_ThetaStar1.Draw("SameHE")
  h_TTThetaStar1.Draw("SameHE")
  h_TLThetaStar1.Draw("SameHE")
  h_LLThetaStar1.Draw("SameHE")
  h_AddThetaStar1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLThetaStar1Clone1.SetFillColor(2)
  h_TLThetaStar1Clone1.SetFillColor(3)
  h_TTThetaStar1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_ThetaStar1.SetLineColor(1)
  h_TTThetaStar1.SetLineColor(7)
  h_TLThetaStar1.SetLineColor(11)
  h_LLThetaStar1.SetLineColor(5)
  h_AddThetaStar1.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar1.SetLineWidth(3)
  h_TTThetaStar1.SetLineWidth(3)
  h_TLThetaStar1.SetLineWidth(3)
  h_LLThetaStar1.SetLineWidth(3)
  h_AddThetaStar1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_ThetaStar1.GetXaxis().SetLabelFont(63)
  hs_ThetaStar1.GetXaxis().SetLabelSize(16)
  hs_ThetaStar1.GetYaxis().SetLabelFont(63)
  hs_ThetaStar1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_ThetaStar1.GetYaxis().SetTitle("Events")
  hs_ThetaStar1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_ThetaStar1.SetMaximum(int(hs_ThetaStar1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTThetaStar1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLThetaStar1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLThetaStar1Clone1, "LLStack", "F")
  leg.AddEntry(h_ThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar1,"TT","LE")
  leg.AddEntry(h_TLThetaStar1,"TL","LE")
  leg.AddEntry(h_LLThetaStar1,"LL","LE")
  leg.AddEntry(h_AddThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_ThetaStar1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_ThetaStar1Divide.Divide(h_ThetaStar1, h_AddThetaStar1, 1, 1)
  h_TTThetaStar1Divide.Divide(h_TTThetaStar1, h_AddThetaStar1, 1, 1)
  h_TLThetaStar1Divide.Divide(h_TLThetaStar1, h_AddThetaStar1, 1, 1)
  h_LLThetaStar1Divide.Divide(h_LLThetaStar1, h_AddThetaStar1, 1, 1)
  h_AddThetaStar1Divide.Divide(h_AddThetaStar1, h_AddThetaStar1, 1 ,1)

  # draw the histograms of ratio
  h_ThetaStar1Divide.Draw("HE")
  h_TTThetaStar1Divide.Draw("SameHE")
  h_TLThetaStar1Divide.Draw("SameHE")
  h_LLThetaStar1Divide.Draw("SameHE")
  h_AddThetaStar1Divide.Draw("SameHE")
  # set the color of each histogram
  h_ThetaStar1Divide.SetLineColor(1)
  h_TTThetaStar1Divide.SetLineColor(7)
  h_TLThetaStar1Divide.SetLineColor(11)
  h_LLThetaStar1Divide.SetLineColor(5)
  h_AddThetaStar1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar1Divide.SetLineWidth(3)
  h_TTThetaStar1Divide.SetLineWidth(3)
  h_TLThetaStar1Divide.SetLineWidth(3)
  h_LLThetaStar1Divide.SetLineWidth(3)
  h_AddThetaStar1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_ThetaStar1Divide.GetXaxis().SetLabelFont(63)
  h_ThetaStar1Divide.GetXaxis().SetLabelSize(16)
  h_ThetaStar1Divide.GetYaxis().SetLabelFont(63)
  h_ThetaStar1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_ThetaStar1Divide.GetXaxis().SetTitle("ThetaStar1")
  h_ThetaStar1Divide.GetXaxis().SetTitleSize(0.07)
  h_ThetaStar1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_ThetaStar1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_ThetaStar1Divide.GetMaximum()
  Max2 = h_TTThetaStar1Divide.GetMaximum()
  Max3 = h_TLThetaStar1Divide.GetMaximum()
  Max4 = h_LLThetaStar1Divide.GetMaximum()
  Max5 = h_AddThetaStar1Divide.GetMaximum()
  Min1 = h_ThetaStar1Divide.GetMinimum()
  Min2 = h_TTThetaStar1Divide.GetMinimum()
  Min3 = h_TLThetaStar1Divide.GetMinimum()
  Min4 = h_LLThetaStar1Divide.GetMinimum()
  Min5 = h_AddThetaStar1Divide.GetMinimum()
  h_ThetaStar1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_ThetaStar1Sum.cd()

  # save the canvas as png file
  c_ThetaStar1Sum.SaveAs("ThetaStar1Sum.png")
  # close the canvas
  c_ThetaStar1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_ThetaStar1SumShape = R.TCanvas("c_ThetaStar1SumShape", "ThetaStar1SumShape", 800, 1000)
  # set the background of this canvas
  c_ThetaStar1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_ThetaStar1Clone2.Draw("HE")
  h_TTThetaStar1Clone2.Draw("SameHE")
  h_TLThetaStar1Clone2.Draw("SameHE")
  h_LLThetaStar1Clone2.Draw("SameHE")
  h_AddThetaStar1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_ThetaStar1Clone2.SetLineColor(1)
  h_TTThetaStar1Clone2.SetLineColor(7)
  h_TLThetaStar1Clone2.SetLineColor(11)
  h_LLThetaStar1Clone2.SetLineColor(5)
  h_AddThetaStar1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar1Clone2.SetLineWidth(3)
  h_TTThetaStar1Clone2.SetLineWidth(3)
  h_TLThetaStar1Clone2.SetLineWidth(3)
  h_LLThetaStar1Clone2.SetLineWidth(3)
  h_AddThetaStar1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_ThetaStar1Clone2.GetXaxis().SetLabelFont(63)
  h_ThetaStar1Clone2.GetXaxis().SetLabelSize(16)
  h_ThetaStar1Clone2.GetYaxis().SetLabelFont(63)
  h_ThetaStar1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_ThetaStar1Clone2.GetYaxis().SetTitle("freq.")
  h_ThetaStar1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_ThetaStar1Clone2.GetMaximum()
  Max2 = h_TTThetaStar1Clone2.GetMaximum()
  Max3 = h_TLThetaStar1Clone2.GetMaximum()
  Max4 = h_LLThetaStar1Clone2.GetMaximum()
  Max5 = h_AddThetaStar1Clone2.GetMaximum()
  h_ThetaStar1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_ThetaStar1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar1Clone2,"TT","LE")
  leg.AddEntry(h_TLThetaStar1Clone2,"TL","LE")
  leg.AddEntry(h_LLThetaStar1Clone2,"LL","LE")
  leg.AddEntry(h_AddThetaStar1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_ThetaStar1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_ThetaStar1DivideShape.Divide(h_ThetaStar1Clone2, h_AddThetaStar1Clone2, 1, 1)
  h_TTThetaStar1DivideShape.Divide(h_TTThetaStar1Clone2, h_AddThetaStar1Clone2, 1, 1)
  h_TLThetaStar1DivideShape.Divide(h_TLThetaStar1Clone2, h_AddThetaStar1Clone2, 1, 1)
  h_LLThetaStar1DivideShape.Divide(h_LLThetaStar1Clone2, h_AddThetaStar1Clone2, 1, 1)
  h_AddThetaStar1DivideShape.Divide(h_AddThetaStar1Clone2, h_AddThetaStar1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_ThetaStar1DivideShape.Draw("HE")
  h_TTThetaStar1DivideShape.Draw("SameHE")
  h_TLThetaStar1DivideShape.Draw("SameHE")
  h_LLThetaStar1DivideShape.Draw("SameHE")
  h_AddThetaStar1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_ThetaStar1DivideShape.SetLineColor(1)
  h_TTThetaStar1DivideShape.SetLineColor(7)
  h_TLThetaStar1DivideShape.SetLineColor(11)
  h_LLThetaStar1DivideShape.SetLineColor(5)
  h_AddThetaStar1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar1DivideShape.SetLineWidth(3)
  h_TTThetaStar1DivideShape.SetLineWidth(3)
  h_TLThetaStar1DivideShape.SetLineWidth(3)
  h_LLThetaStar1DivideShape.SetLineWidth(3)
  h_AddThetaStar1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_ThetaStar1DivideShape.GetXaxis().SetLabelFont(63)
  h_ThetaStar1DivideShape.GetXaxis().SetLabelSize(16)
  h_ThetaStar1DivideShape.GetYaxis().SetLabelFont(63)
  h_ThetaStar1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_ThetaStar1DivideShape.GetXaxis().SetTitle("ThetaStar1")
  h_ThetaStar1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_ThetaStar1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_ThetaStar1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_ThetaStar1DivideShape.GetMaximum()
  Max2 = h_TTThetaStar1DivideShape.GetMaximum()
  Max3 = h_TLThetaStar1DivideShape.GetMaximum()
  Max4 = h_LLThetaStar1DivideShape.GetMaximum()
  Max5 = h_AddThetaStar1DivideShape.GetMaximum()
  Min1 = h_ThetaStar1DivideShape.GetMinimum()
  Min2 = h_TTThetaStar1DivideShape.GetMinimum()
  Min3 = h_TLThetaStar1DivideShape.GetMinimum()
  Min4 = h_LLThetaStar1DivideShape.GetMinimum()
  Min5 = h_AddThetaStar1DivideShape.GetMinimum()
  h_ThetaStar1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_ThetaStar1SumShape.cd()


  # save the canvas as png file
  c_ThetaStar1SumShape.SaveAs("ThetaStar1ShapeOnly.png")
  # close the canvas
  c_ThetaStar1SumShape.Close()



  """
  histogram of ThetaStar2, TTThetaStar2, TLThetaStar2, LLThetaStar2, TT+TL+LLThetaStar2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_ThetaStar2Sum = R.TCanvas("c_ThetaStar2Sum", "ThetaStar2Sum", 800, 1000)
  # set the background of this canvas
  c_ThetaStar2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_ThetaStar2.Draw("Hist")
  h_ThetaStar2.Draw("SameHE")
  h_TTThetaStar2.Draw("SameHE")
  h_TLThetaStar2.Draw("SameHE")
  h_LLThetaStar2.Draw("SameHE")
  h_AddThetaStar2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLThetaStar2Clone1.SetFillColor(2)
  h_TLThetaStar2Clone1.SetFillColor(3)
  h_TTThetaStar2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_ThetaStar2.SetLineColor(1)
  h_TTThetaStar2.SetLineColor(7)
  h_TLThetaStar2.SetLineColor(11)
  h_LLThetaStar2.SetLineColor(5)
  h_AddThetaStar2.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar2.SetLineWidth(3)
  h_TTThetaStar2.SetLineWidth(3)
  h_TLThetaStar2.SetLineWidth(3)
  h_LLThetaStar2.SetLineWidth(3)
  h_AddThetaStar2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_ThetaStar2.GetXaxis().SetLabelFont(63)
  hs_ThetaStar2.GetXaxis().SetLabelSize(16)
  hs_ThetaStar2.GetYaxis().SetLabelFont(63)
  hs_ThetaStar2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_ThetaStar2.GetYaxis().SetTitle("Events")
  hs_ThetaStar2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_ThetaStar2.SetMaximum(int(hs_ThetaStar2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTThetaStar2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLThetaStar2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLThetaStar2Clone1, "LLStack", "F")
  leg.AddEntry(h_ThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar2,"TT","LE")
  leg.AddEntry(h_TLThetaStar2,"TL","LE")
  leg.AddEntry(h_LLThetaStar2,"LL","LE")
  leg.AddEntry(h_AddThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_ThetaStar2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_ThetaStar2Divide.Divide(h_ThetaStar2, h_AddThetaStar2, 1, 1)
  h_TTThetaStar2Divide.Divide(h_TTThetaStar2, h_AddThetaStar2, 1, 1)
  h_TLThetaStar2Divide.Divide(h_TLThetaStar2, h_AddThetaStar2, 1, 1)
  h_LLThetaStar2Divide.Divide(h_LLThetaStar2, h_AddThetaStar2, 1, 1)
  h_AddThetaStar2Divide.Divide(h_AddThetaStar2, h_AddThetaStar2, 1 ,1)

  # draw the histograms of ratio
  h_ThetaStar2Divide.Draw("HE")
  h_TTThetaStar2Divide.Draw("SameHE")
  h_TLThetaStar2Divide.Draw("SameHE")
  h_LLThetaStar2Divide.Draw("SameHE")
  h_AddThetaStar2Divide.Draw("SameHE")
  # set the color of each histogram
  h_ThetaStar2Divide.SetLineColor(1)
  h_TTThetaStar2Divide.SetLineColor(7)
  h_TLThetaStar2Divide.SetLineColor(11)
  h_LLThetaStar2Divide.SetLineColor(5)
  h_AddThetaStar2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar2Divide.SetLineWidth(3)
  h_TTThetaStar2Divide.SetLineWidth(3)
  h_TLThetaStar2Divide.SetLineWidth(3)
  h_LLThetaStar2Divide.SetLineWidth(3)
  h_AddThetaStar2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_ThetaStar2Divide.GetXaxis().SetLabelFont(63)
  h_ThetaStar2Divide.GetXaxis().SetLabelSize(16)
  h_ThetaStar2Divide.GetYaxis().SetLabelFont(63)
  h_ThetaStar2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_ThetaStar2Divide.GetXaxis().SetTitle("ThetaStar2")
  h_ThetaStar2Divide.GetXaxis().SetTitleSize(0.07)
  h_ThetaStar2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_ThetaStar2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_ThetaStar2Divide.GetMaximum()
  Max2 = h_TTThetaStar2Divide.GetMaximum()
  Max3 = h_TLThetaStar2Divide.GetMaximum()
  Max4 = h_LLThetaStar2Divide.GetMaximum()
  Max5 = h_AddThetaStar2Divide.GetMaximum()
  Min1 = h_ThetaStar2Divide.GetMinimum()
  Min2 = h_TTThetaStar2Divide.GetMinimum()
  Min3 = h_TLThetaStar2Divide.GetMinimum()
  Min4 = h_LLThetaStar2Divide.GetMinimum()
  Min5 = h_AddThetaStar2Divide.GetMinimum()
  h_ThetaStar2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_ThetaStar2Sum.cd()

  # save the canvas as png file
  c_ThetaStar2Sum.SaveAs("ThetaStar2Sum.png")
  # close the canvas
  c_ThetaStar2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_ThetaStar2SumShape = R.TCanvas("c_ThetaStar2SumShape", "ThetaStar2SumShape", 800, 1000)
  # set the background of this canvas
  c_ThetaStar2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_ThetaStar2Clone2.Draw("HE")
  h_TTThetaStar2Clone2.Draw("SameHE")
  h_TLThetaStar2Clone2.Draw("SameHE")
  h_LLThetaStar2Clone2.Draw("SameHE")
  h_AddThetaStar2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_ThetaStar2Clone2.SetLineColor(1)
  h_TTThetaStar2Clone2.SetLineColor(7)
  h_TLThetaStar2Clone2.SetLineColor(11)
  h_LLThetaStar2Clone2.SetLineColor(5)
  h_AddThetaStar2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar2Clone2.SetLineWidth(3)
  h_TTThetaStar2Clone2.SetLineWidth(3)
  h_TLThetaStar2Clone2.SetLineWidth(3)
  h_LLThetaStar2Clone2.SetLineWidth(3)
  h_AddThetaStar2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_ThetaStar2Clone2.GetXaxis().SetLabelFont(63)
  h_ThetaStar2Clone2.GetXaxis().SetLabelSize(16)
  h_ThetaStar2Clone2.GetYaxis().SetLabelFont(63)
  h_ThetaStar2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_ThetaStar2Clone2.GetYaxis().SetTitle("freq.")
  h_ThetaStar2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_ThetaStar2Clone2.GetMaximum()
  Max2 = h_TTThetaStar2Clone2.GetMaximum()
  Max3 = h_TLThetaStar2Clone2.GetMaximum()
  Max4 = h_LLThetaStar2Clone2.GetMaximum()
  Max5 = h_AddThetaStar2Clone2.GetMaximum()
  h_ThetaStar2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_ThetaStar2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar2Clone2,"TT","LE")
  leg.AddEntry(h_TLThetaStar2Clone2,"TL","LE")
  leg.AddEntry(h_LLThetaStar2Clone2,"LL","LE")
  leg.AddEntry(h_AddThetaStar2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_ThetaStar2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_ThetaStar2DivideShape.Divide(h_ThetaStar2Clone2, h_AddThetaStar2Clone2, 1, 1)
  h_TTThetaStar2DivideShape.Divide(h_TTThetaStar2Clone2, h_AddThetaStar2Clone2, 1, 1)
  h_TLThetaStar2DivideShape.Divide(h_TLThetaStar2Clone2, h_AddThetaStar2Clone2, 1, 1)
  h_LLThetaStar2DivideShape.Divide(h_LLThetaStar2Clone2, h_AddThetaStar2Clone2, 1, 1)
  h_AddThetaStar2DivideShape.Divide(h_AddThetaStar2Clone2, h_AddThetaStar2Clone2,1 ,1)

  # draw the histograms of ratio
  h_ThetaStar2DivideShape.Draw("HE")
  h_TTThetaStar2DivideShape.Draw("SameHE")
  h_TLThetaStar2DivideShape.Draw("SameHE")
  h_LLThetaStar2DivideShape.Draw("SameHE")
  h_AddThetaStar2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_ThetaStar2DivideShape.SetLineColor(1)
  h_TTThetaStar2DivideShape.SetLineColor(7)
  h_TLThetaStar2DivideShape.SetLineColor(11)
  h_LLThetaStar2DivideShape.SetLineColor(5)
  h_AddThetaStar2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_ThetaStar2DivideShape.SetLineWidth(3)
  h_TTThetaStar2DivideShape.SetLineWidth(3)
  h_TLThetaStar2DivideShape.SetLineWidth(3)
  h_LLThetaStar2DivideShape.SetLineWidth(3)
  h_AddThetaStar2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_ThetaStar2DivideShape.GetXaxis().SetLabelFont(63)
  h_ThetaStar2DivideShape.GetXaxis().SetLabelSize(16)
  h_ThetaStar2DivideShape.GetYaxis().SetLabelFont(63)
  h_ThetaStar2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_ThetaStar2DivideShape.GetXaxis().SetTitle("ThetaStar2")
  h_ThetaStar2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_ThetaStar2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_ThetaStar2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_ThetaStar2DivideShape.GetMaximum()
  Max2 = h_TTThetaStar2DivideShape.GetMaximum()
  Max3 = h_TLThetaStar2DivideShape.GetMaximum()
  Max4 = h_LLThetaStar2DivideShape.GetMaximum()
  Max5 = h_AddThetaStar2DivideShape.GetMaximum()
  Min1 = h_ThetaStar2DivideShape.GetMinimum()
  Min2 = h_TTThetaStar2DivideShape.GetMinimum()
  Min3 = h_TLThetaStar2DivideShape.GetMinimum()
  Min4 = h_LLThetaStar2DivideShape.GetMinimum()
  Min5 = h_AddThetaStar2DivideShape.GetMinimum()
  h_ThetaStar2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_ThetaStar2SumShape.cd()


  # save the canvas as png file
  c_ThetaStar2SumShape.SaveAs("ThetaStar2ShapeOnly.png")
  # close the canvas
  c_ThetaStar2SumShape.Close()



  """
  histogram of CosThetaStar1, TTCosThetaStar1, TLCosThetaStar1, LLCosThetaStar1, TT+TL+LLCosThetaStar1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosThetaStar1Sum = R.TCanvas("c_CosThetaStar1Sum", "CosThetaStar1Sum", 800, 1000)
  # set the background of this canvas
  c_CosThetaStar1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosThetaStar1.Draw("Hist")
  h_CosThetaStar1.Draw("SameHE")
  h_TTCosThetaStar1.Draw("SameHE")
  h_TLCosThetaStar1.Draw("SameHE")
  h_LLCosThetaStar1.Draw("SameHE")
  h_AddCosThetaStar1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosThetaStar1Clone1.SetFillColor(2)
  h_TLCosThetaStar1Clone1.SetFillColor(3)
  h_TTCosThetaStar1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosThetaStar1.SetLineColor(1)
  h_TTCosThetaStar1.SetLineColor(7)
  h_TLCosThetaStar1.SetLineColor(11)
  h_LLCosThetaStar1.SetLineColor(5)
  h_AddCosThetaStar1.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar1.SetLineWidth(3)
  h_TTCosThetaStar1.SetLineWidth(3)
  h_TLCosThetaStar1.SetLineWidth(3)
  h_LLCosThetaStar1.SetLineWidth(3)
  h_AddCosThetaStar1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosThetaStar1.GetXaxis().SetLabelFont(63)
  hs_CosThetaStar1.GetXaxis().SetLabelSize(16)
  hs_CosThetaStar1.GetYaxis().SetLabelFont(63)
  hs_CosThetaStar1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosThetaStar1.GetYaxis().SetTitle("Events")
  hs_CosThetaStar1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosThetaStar1.SetMaximum(int(hs_CosThetaStar1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosThetaStar1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLCosThetaStar1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLCosThetaStar1Clone1, "LLStack", "F")
  leg.AddEntry(h_CosThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar1,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar1,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar1,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosThetaStar1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosThetaStar1Divide.Divide(h_CosThetaStar1, h_AddCosThetaStar1, 1, 1)
  h_TTCosThetaStar1Divide.Divide(h_TTCosThetaStar1, h_AddCosThetaStar1, 1, 1)
  h_TLCosThetaStar1Divide.Divide(h_TLCosThetaStar1, h_AddCosThetaStar1, 1, 1)
  h_LLCosThetaStar1Divide.Divide(h_LLCosThetaStar1, h_AddCosThetaStar1, 1, 1)
  h_AddCosThetaStar1Divide.Divide(h_AddCosThetaStar1, h_AddCosThetaStar1, 1 ,1)

  # draw the histograms of ratio
  h_CosThetaStar1Divide.Draw("HE")
  h_TTCosThetaStar1Divide.Draw("SameHE")
  h_TLCosThetaStar1Divide.Draw("SameHE")
  h_LLCosThetaStar1Divide.Draw("SameHE")
  h_AddCosThetaStar1Divide.Draw("SameHE")
  # set the color of each histogram
  h_CosThetaStar1Divide.SetLineColor(1)
  h_TTCosThetaStar1Divide.SetLineColor(7)
  h_TLCosThetaStar1Divide.SetLineColor(11)
  h_LLCosThetaStar1Divide.SetLineColor(5)
  h_AddCosThetaStar1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar1Divide.SetLineWidth(3)
  h_TTCosThetaStar1Divide.SetLineWidth(3)
  h_TLCosThetaStar1Divide.SetLineWidth(3)
  h_LLCosThetaStar1Divide.SetLineWidth(3)
  h_AddCosThetaStar1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosThetaStar1Divide.GetXaxis().SetLabelFont(63)
  h_CosThetaStar1Divide.GetXaxis().SetLabelSize(16)
  h_CosThetaStar1Divide.GetYaxis().SetLabelFont(63)
  h_CosThetaStar1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosThetaStar1Divide.GetXaxis().SetTitle("CosThetaStar1")
  h_CosThetaStar1Divide.GetXaxis().SetTitleSize(0.07)
  h_CosThetaStar1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosThetaStar1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosThetaStar1Divide.GetMaximum()
  Max2 = h_TTCosThetaStar1Divide.GetMaximum()
  Max3 = h_TLCosThetaStar1Divide.GetMaximum()
  Max4 = h_LLCosThetaStar1Divide.GetMaximum()
  Max5 = h_AddCosThetaStar1Divide.GetMaximum()
  Min1 = h_CosThetaStar1Divide.GetMinimum()
  Min2 = h_TTCosThetaStar1Divide.GetMinimum()
  Min3 = h_TLCosThetaStar1Divide.GetMinimum()
  Min4 = h_LLCosThetaStar1Divide.GetMinimum()
  Min5 = h_AddCosThetaStar1Divide.GetMinimum()
  h_CosThetaStar1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosThetaStar1Sum.cd()

  # save the canvas as png file
  c_CosThetaStar1Sum.SaveAs("CosThetaStar1Sum.png")
  # close the canvas
  c_CosThetaStar1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosThetaStar1SumShape = R.TCanvas("c_CosThetaStar1SumShape", "CosThetaStar1SumShape", 800, 1000)
  # set the background of this canvas
  c_CosThetaStar1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosThetaStar1Clone2.Draw("HE")
  h_TTCosThetaStar1Clone2.Draw("SameHE")
  h_TLCosThetaStar1Clone2.Draw("SameHE")
  h_LLCosThetaStar1Clone2.Draw("SameHE")
  h_AddCosThetaStar1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosThetaStar1Clone2.SetLineColor(1)
  h_TTCosThetaStar1Clone2.SetLineColor(7)
  h_TLCosThetaStar1Clone2.SetLineColor(11)
  h_LLCosThetaStar1Clone2.SetLineColor(5)
  h_AddCosThetaStar1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar1Clone2.SetLineWidth(3)
  h_TTCosThetaStar1Clone2.SetLineWidth(3)
  h_TLCosThetaStar1Clone2.SetLineWidth(3)
  h_LLCosThetaStar1Clone2.SetLineWidth(3)
  h_AddCosThetaStar1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosThetaStar1Clone2.GetXaxis().SetLabelFont(63)
  h_CosThetaStar1Clone2.GetXaxis().SetLabelSize(16)
  h_CosThetaStar1Clone2.GetYaxis().SetLabelFont(63)
  h_CosThetaStar1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosThetaStar1Clone2.GetYaxis().SetTitle("freq.")
  h_CosThetaStar1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosThetaStar1Clone2.GetMaximum()
  Max2 = h_TTCosThetaStar1Clone2.GetMaximum()
  Max3 = h_TLCosThetaStar1Clone2.GetMaximum()
  Max4 = h_LLCosThetaStar1Clone2.GetMaximum()
  Max5 = h_AddCosThetaStar1Clone2.GetMaximum()
  h_CosThetaStar1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosThetaStar1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar1Clone2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar1Clone2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar1Clone2,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosThetaStar1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosThetaStar1DivideShape.Divide(h_CosThetaStar1Clone2, h_AddCosThetaStar1Clone2, 1, 1)
  h_TTCosThetaStar1DivideShape.Divide(h_TTCosThetaStar1Clone2, h_AddCosThetaStar1Clone2, 1, 1)
  h_TLCosThetaStar1DivideShape.Divide(h_TLCosThetaStar1Clone2, h_AddCosThetaStar1Clone2, 1, 1)
  h_LLCosThetaStar1DivideShape.Divide(h_LLCosThetaStar1Clone2, h_AddCosThetaStar1Clone2, 1, 1)
  h_AddCosThetaStar1DivideShape.Divide(h_AddCosThetaStar1Clone2, h_AddCosThetaStar1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosThetaStar1DivideShape.Draw("HE")
  h_TTCosThetaStar1DivideShape.Draw("SameHE")
  h_TLCosThetaStar1DivideShape.Draw("SameHE")
  h_LLCosThetaStar1DivideShape.Draw("SameHE")
  h_AddCosThetaStar1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosThetaStar1DivideShape.SetLineColor(1)
  h_TTCosThetaStar1DivideShape.SetLineColor(7)
  h_TLCosThetaStar1DivideShape.SetLineColor(11)
  h_LLCosThetaStar1DivideShape.SetLineColor(5)
  h_AddCosThetaStar1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar1DivideShape.SetLineWidth(3)
  h_TTCosThetaStar1DivideShape.SetLineWidth(3)
  h_TLCosThetaStar1DivideShape.SetLineWidth(3)
  h_LLCosThetaStar1DivideShape.SetLineWidth(3)
  h_AddCosThetaStar1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosThetaStar1DivideShape.GetXaxis().SetLabelFont(63)
  h_CosThetaStar1DivideShape.GetXaxis().SetLabelSize(16)
  h_CosThetaStar1DivideShape.GetYaxis().SetLabelFont(63)
  h_CosThetaStar1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosThetaStar1DivideShape.GetXaxis().SetTitle("CosThetaStar1")
  h_CosThetaStar1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosThetaStar1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosThetaStar1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosThetaStar1DivideShape.GetMaximum()
  Max2 = h_TTCosThetaStar1DivideShape.GetMaximum()
  Max3 = h_TLCosThetaStar1DivideShape.GetMaximum()
  Max4 = h_LLCosThetaStar1DivideShape.GetMaximum()
  Max5 = h_AddCosThetaStar1DivideShape.GetMaximum()
  Min1 = h_CosThetaStar1DivideShape.GetMinimum()
  Min2 = h_TTCosThetaStar1DivideShape.GetMinimum()
  Min3 = h_TLCosThetaStar1DivideShape.GetMinimum()
  Min4 = h_LLCosThetaStar1DivideShape.GetMinimum()
  Min5 = h_AddCosThetaStar1DivideShape.GetMinimum()
  h_CosThetaStar1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosThetaStar1SumShape.cd()


  # save the canvas as png file
  c_CosThetaStar1SumShape.SaveAs("CosThetaStar1ShapeOnly.png")
  # close the canvas
  c_CosThetaStar1SumShape.Close()



  """
  histogram of CosThetaStar2, TTCosThetaStar2, TLCosThetaStar2, LLCosThetaStar2, TT+TL+LLCosThetaStar2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosThetaStar2Sum = R.TCanvas("c_CosThetaStar2Sum", "CosThetaStar2Sum", 800, 1000)
  # set the background of this canvas
  c_CosThetaStar2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosThetaStar2.Draw("Hist")
  h_CosThetaStar2.Draw("SameHE")
  h_TTCosThetaStar2.Draw("SameHE")
  h_TLCosThetaStar2.Draw("SameHE")
  h_LLCosThetaStar2.Draw("SameHE")
  h_AddCosThetaStar2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosThetaStar2Clone1.SetFillColor(2)
  h_TLCosThetaStar2Clone1.SetFillColor(3)
  h_TTCosThetaStar2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosThetaStar2.SetLineColor(1)
  h_TTCosThetaStar2.SetLineColor(7)
  h_TLCosThetaStar2.SetLineColor(11)
  h_LLCosThetaStar2.SetLineColor(5)
  h_AddCosThetaStar2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar2.SetLineWidth(3)
  h_TTCosThetaStar2.SetLineWidth(3)
  h_TLCosThetaStar2.SetLineWidth(3)
  h_LLCosThetaStar2.SetLineWidth(3)
  h_AddCosThetaStar2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosThetaStar2.GetXaxis().SetLabelFont(63)
  hs_CosThetaStar2.GetXaxis().SetLabelSize(16)
  hs_CosThetaStar2.GetYaxis().SetLabelFont(63)
  hs_CosThetaStar2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosThetaStar2.GetYaxis().SetTitle("Events")
  hs_CosThetaStar2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosThetaStar2.SetMaximum(int(hs_CosThetaStar2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosThetaStar2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLCosThetaStar2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLCosThetaStar2Clone1, "LLStack", "F")
  leg.AddEntry(h_CosThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar2,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosThetaStar2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosThetaStar2Divide.Divide(h_CosThetaStar2, h_AddCosThetaStar2, 1, 1)
  h_TTCosThetaStar2Divide.Divide(h_TTCosThetaStar2, h_AddCosThetaStar2, 1, 1)
  h_TLCosThetaStar2Divide.Divide(h_TLCosThetaStar2, h_AddCosThetaStar2, 1, 1)
  h_LLCosThetaStar2Divide.Divide(h_LLCosThetaStar2, h_AddCosThetaStar2, 1, 1)
  h_AddCosThetaStar2Divide.Divide(h_AddCosThetaStar2, h_AddCosThetaStar2, 1 ,1)

  # draw the histograms of ratio
  h_CosThetaStar2Divide.Draw("HE")
  h_TTCosThetaStar2Divide.Draw("SameHE")
  h_TLCosThetaStar2Divide.Draw("SameHE")
  h_LLCosThetaStar2Divide.Draw("SameHE")
  h_AddCosThetaStar2Divide.Draw("SameHE")
  # set the color of each histogram
  h_CosThetaStar2Divide.SetLineColor(1)
  h_TTCosThetaStar2Divide.SetLineColor(7)
  h_TLCosThetaStar2Divide.SetLineColor(11)
  h_LLCosThetaStar2Divide.SetLineColor(5)
  h_AddCosThetaStar2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar2Divide.SetLineWidth(3)
  h_TTCosThetaStar2Divide.SetLineWidth(3)
  h_TLCosThetaStar2Divide.SetLineWidth(3)
  h_LLCosThetaStar2Divide.SetLineWidth(3)
  h_AddCosThetaStar2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosThetaStar2Divide.GetXaxis().SetLabelFont(63)
  h_CosThetaStar2Divide.GetXaxis().SetLabelSize(16)
  h_CosThetaStar2Divide.GetYaxis().SetLabelFont(63)
  h_CosThetaStar2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosThetaStar2Divide.GetXaxis().SetTitle("CosThetaStar2")
  h_CosThetaStar2Divide.GetXaxis().SetTitleSize(0.07)
  h_CosThetaStar2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosThetaStar2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosThetaStar2Divide.GetMaximum()
  Max2 = h_TTCosThetaStar2Divide.GetMaximum()
  Max3 = h_TLCosThetaStar2Divide.GetMaximum()
  Max4 = h_LLCosThetaStar2Divide.GetMaximum()
  Max5 = h_AddCosThetaStar2Divide.GetMaximum()
  Min1 = h_CosThetaStar2Divide.GetMinimum()
  Min2 = h_TTCosThetaStar2Divide.GetMinimum()
  Min3 = h_TLCosThetaStar2Divide.GetMinimum()
  Min4 = h_LLCosThetaStar2Divide.GetMinimum()
  Min5 = h_AddCosThetaStar2Divide.GetMinimum()
  h_CosThetaStar2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosThetaStar2Sum.cd()

  # save the canvas as png file
  c_CosThetaStar2Sum.SaveAs("CosThetaStar2Sum.png")
  # close the canvas
  c_CosThetaStar2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosThetaStar2SumShape = R.TCanvas("c_CosThetaStar2SumShape", "CosThetaStar2SumShape", 800, 1000)
  # set the background of this canvas
  c_CosThetaStar2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosThetaStar2Clone2.Draw("HE")
  h_TTCosThetaStar2Clone2.Draw("SameHE")
  h_TLCosThetaStar2Clone2.Draw("SameHE")
  h_LLCosThetaStar2Clone2.Draw("SameHE")
  h_AddCosThetaStar2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosThetaStar2Clone2.SetLineColor(1)
  h_TTCosThetaStar2Clone2.SetLineColor(7)
  h_TLCosThetaStar2Clone2.SetLineColor(11)
  h_LLCosThetaStar2Clone2.SetLineColor(5)
  h_AddCosThetaStar2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar2Clone2.SetLineWidth(3)
  h_TTCosThetaStar2Clone2.SetLineWidth(3)
  h_TLCosThetaStar2Clone2.SetLineWidth(3)
  h_LLCosThetaStar2Clone2.SetLineWidth(3)
  h_AddCosThetaStar2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosThetaStar2Clone2.GetXaxis().SetLabelFont(63)
  h_CosThetaStar2Clone2.GetXaxis().SetLabelSize(16)
  h_CosThetaStar2Clone2.GetYaxis().SetLabelFont(63)
  h_CosThetaStar2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosThetaStar2Clone2.GetYaxis().SetTitle("freq.")
  h_CosThetaStar2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosThetaStar2Clone2.GetMaximum()
  Max2 = h_TTCosThetaStar2Clone2.GetMaximum()
  Max3 = h_TLCosThetaStar2Clone2.GetMaximum()
  Max4 = h_LLCosThetaStar2Clone2.GetMaximum()
  Max5 = h_AddCosThetaStar2Clone2.GetMaximum()
  h_CosThetaStar2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosThetaStar2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar2Clone2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar2Clone2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar2Clone2,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosThetaStar2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosThetaStar2DivideShape.Divide(h_CosThetaStar2Clone2, h_AddCosThetaStar2Clone2, 1, 1)
  h_TTCosThetaStar2DivideShape.Divide(h_TTCosThetaStar2Clone2, h_AddCosThetaStar2Clone2, 1, 1)
  h_TLCosThetaStar2DivideShape.Divide(h_TLCosThetaStar2Clone2, h_AddCosThetaStar2Clone2, 1, 1)
  h_LLCosThetaStar2DivideShape.Divide(h_LLCosThetaStar2Clone2, h_AddCosThetaStar2Clone2, 1, 1)
  h_AddCosThetaStar2DivideShape.Divide(h_AddCosThetaStar2Clone2, h_AddCosThetaStar2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosThetaStar2DivideShape.Draw("HE")
  h_TTCosThetaStar2DivideShape.Draw("SameHE")
  h_TLCosThetaStar2DivideShape.Draw("SameHE")
  h_LLCosThetaStar2DivideShape.Draw("SameHE")
  h_AddCosThetaStar2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosThetaStar2DivideShape.SetLineColor(1)
  h_TTCosThetaStar2DivideShape.SetLineColor(7)
  h_TLCosThetaStar2DivideShape.SetLineColor(11)
  h_LLCosThetaStar2DivideShape.SetLineColor(5)
  h_AddCosThetaStar2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosThetaStar2DivideShape.SetLineWidth(3)
  h_TTCosThetaStar2DivideShape.SetLineWidth(3)
  h_TLCosThetaStar2DivideShape.SetLineWidth(3)
  h_LLCosThetaStar2DivideShape.SetLineWidth(3)
  h_AddCosThetaStar2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosThetaStar2DivideShape.GetXaxis().SetLabelFont(63)
  h_CosThetaStar2DivideShape.GetXaxis().SetLabelSize(16)
  h_CosThetaStar2DivideShape.GetYaxis().SetLabelFont(63)
  h_CosThetaStar2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosThetaStar2DivideShape.GetXaxis().SetTitle("CosThetaStar2")
  h_CosThetaStar2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosThetaStar2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosThetaStar2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosThetaStar2DivideShape.GetMaximum()
  Max2 = h_TTCosThetaStar2DivideShape.GetMaximum()
  Max3 = h_TLCosThetaStar2DivideShape.GetMaximum()
  Max4 = h_LLCosThetaStar2DivideShape.GetMaximum()
  Max5 = h_AddCosThetaStar2DivideShape.GetMaximum()
  Min1 = h_CosThetaStar2DivideShape.GetMinimum()
  Min2 = h_TTCosThetaStar2DivideShape.GetMinimum()
  Min3 = h_TLCosThetaStar2DivideShape.GetMinimum()
  Min4 = h_LLCosThetaStar2DivideShape.GetMinimum()
  Min5 = h_AddCosThetaStar2DivideShape.GetMinimum()
  h_CosThetaStar2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosThetaStar2SumShape.cd()


  # save the canvas as png file
  c_CosThetaStar2SumShape.SaveAs("CosThetaStar2ShapeOnly.png")
  # close the canvas
  c_CosThetaStar2SumShape.Close()



  """
  histogram of Phi, TTPhi, TLPhi, LLPhi, TT+TL+LLPhi
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_PhiSum = R.TCanvas("c_PhiSum", "PhiSum", 800, 1000)
  # set the background of this canvas
  c_PhiSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_Phi.Draw("Hist")
  h_Phi.Draw("SameHE")
  h_TTPhi.Draw("SameHE")
  h_TLPhi.Draw("SameHE")
  h_LLPhi.Draw("SameHE")
  h_AddPhi.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLPhiClone1.SetFillColor(2)
  h_TLPhiClone1.SetFillColor(3)
  h_TTPhiClone1.SetFillColor(9)

  # set the line color of each histogram
  h_Phi.SetLineColor(1)
  h_TTPhi.SetLineColor(7)
  h_TLPhi.SetLineColor(11)
  h_LLPhi.SetLineColor(5)
  h_AddPhi.SetLineColor(46)
  # set the width of each histogram's line
  h_Phi.SetLineWidth(3)
  h_TTPhi.SetLineWidth(3)
  h_TLPhi.SetLineWidth(3)
  h_LLPhi.SetLineWidth(3)
  h_AddPhi.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Phi.GetXaxis().SetLabelFont(63)
  hs_Phi.GetXaxis().SetLabelSize(16)
  hs_Phi.GetYaxis().SetLabelFont(63)
  hs_Phi.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Phi.GetYaxis().SetTitle("Events")
  hs_Phi.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Phi.SetMaximum(int(hs_Phi.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTPhiClone1, "TTStack", "F")
  leg.AddEntry(h_TLPhiClone1, "TLStack", "F")
  leg.AddEntry(h_LLPhiClone1, "LLStack", "F")
  leg.AddEntry(h_Phi,"Inclusive","LE")
  leg.AddEntry(h_TTPhi,"TT","LE")
  leg.AddEntry(h_TLPhi,"TL","LE")
  leg.AddEntry(h_LLPhi,"LL","LE")
  leg.AddEntry(h_AddPhi,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_PhiSum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_PhiDivide.Divide(h_Phi, h_AddPhi, 1, 1)
  h_TTPhiDivide.Divide(h_TTPhi, h_AddPhi, 1, 1)
  h_TLPhiDivide.Divide(h_TLPhi, h_AddPhi, 1, 1)
  h_LLPhiDivide.Divide(h_LLPhi, h_AddPhi, 1, 1)
  h_AddPhiDivide.Divide(h_AddPhi, h_AddPhi, 1 ,1)

  # draw the histograms of ratio
  h_PhiDivide.Draw("HE")
  h_TTPhiDivide.Draw("SameHE")
  h_TLPhiDivide.Draw("SameHE")
  h_LLPhiDivide.Draw("SameHE")
  h_AddPhiDivide.Draw("SameHE")
  # set the color of each histogram
  h_PhiDivide.SetLineColor(1)
  h_TTPhiDivide.SetLineColor(7)
  h_TLPhiDivide.SetLineColor(11)
  h_LLPhiDivide.SetLineColor(5)
  h_AddPhiDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_PhiDivide.SetLineWidth(3)
  h_TTPhiDivide.SetLineWidth(3)
  h_TLPhiDivide.SetLineWidth(3)
  h_LLPhiDivide.SetLineWidth(3)
  h_AddPhiDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_PhiDivide.GetXaxis().SetLabelFont(63)
  h_PhiDivide.GetXaxis().SetLabelSize(16)
  h_PhiDivide.GetYaxis().SetLabelFont(63)
  h_PhiDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_PhiDivide.GetXaxis().SetTitle("Phi")
  h_PhiDivide.GetXaxis().SetTitleSize(0.07)
  h_PhiDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_PhiDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_PhiDivide.GetMaximum()
  Max2 = h_TTPhiDivide.GetMaximum()
  Max3 = h_TLPhiDivide.GetMaximum()
  Max4 = h_LLPhiDivide.GetMaximum()
  Max5 = h_AddPhiDivide.GetMaximum()
  Min1 = h_PhiDivide.GetMinimum()
  Min2 = h_TTPhiDivide.GetMinimum()
  Min3 = h_TLPhiDivide.GetMinimum()
  Min4 = h_LLPhiDivide.GetMinimum()
  Min5 = h_AddPhiDivide.GetMinimum()
  h_PhiDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_PhiSum.cd()

  # save the canvas as png file
  c_PhiSum.SaveAs("PhiSum.png")
  # close the canvas
  c_PhiSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_PhiSumShape = R.TCanvas("c_PhiSumShape", "PhiSumShape", 800, 1000)
  # set the background of this canvas
  c_PhiSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_PhiClone2.Draw("HE")
  h_TTPhiClone2.Draw("SameHE")
  h_TLPhiClone2.Draw("SameHE")
  h_LLPhiClone2.Draw("SameHE")
  h_AddPhiClone2.Draw("SameHE")

  # set the line color of each histogram
  h_PhiClone2.SetLineColor(1)
  h_TTPhiClone2.SetLineColor(7)
  h_TLPhiClone2.SetLineColor(11)
  h_LLPhiClone2.SetLineColor(5)
  h_AddPhiClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_PhiClone2.SetLineWidth(3)
  h_TTPhiClone2.SetLineWidth(3)
  h_TLPhiClone2.SetLineWidth(3)
  h_LLPhiClone2.SetLineWidth(3)
  h_AddPhiClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_PhiClone2.GetXaxis().SetLabelFont(63)
  h_PhiClone2.GetXaxis().SetLabelSize(16)
  h_PhiClone2.GetYaxis().SetLabelFont(63)
  h_PhiClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_PhiClone2.GetYaxis().SetTitle("freq.")
  h_PhiClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_PhiClone2.GetMaximum()
  Max2 = h_TTPhiClone2.GetMaximum()
  Max3 = h_TLPhiClone2.GetMaximum()
  Max4 = h_LLPhiClone2.GetMaximum()
  Max5 = h_AddPhiClone2.GetMaximum()
  h_PhiClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_PhiClone2,"Inclusive","LE")
  leg.AddEntry(h_TTPhiClone2,"TT","LE")
  leg.AddEntry(h_TLPhiClone2,"TL","LE")
  leg.AddEntry(h_LLPhiClone2,"LL","LE")
  leg.AddEntry(h_AddPhiClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_PhiSumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_PhiDivideShape.Divide(h_PhiClone2, h_AddPhiClone2, 1, 1)
  h_TTPhiDivideShape.Divide(h_TTPhiClone2, h_AddPhiClone2, 1, 1)
  h_TLPhiDivideShape.Divide(h_TLPhiClone2, h_AddPhiClone2, 1, 1)
  h_LLPhiDivideShape.Divide(h_LLPhiClone2, h_AddPhiClone2, 1, 1)
  h_AddPhiDivideShape.Divide(h_AddPhiClone2, h_AddPhiClone2, 1 ,1)

  # draw the histograms of ratio
  h_PhiDivideShape.Draw("HE")
  h_TTPhiDivideShape.Draw("SameHE")
  h_TLPhiDivideShape.Draw("SameHE")
  h_LLPhiDivideShape.Draw("SameHE")
  h_AddPhiDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_PhiDivideShape.SetLineColor(1)
  h_TTPhiDivideShape.SetLineColor(7)
  h_TLPhiDivideShape.SetLineColor(11)
  h_LLPhiDivideShape.SetLineColor(5)
  h_AddPhiDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_PhiDivideShape.SetLineWidth(3)
  h_TTPhiDivideShape.SetLineWidth(3)
  h_TLPhiDivideShape.SetLineWidth(3)
  h_LLPhiDivideShape.SetLineWidth(3)
  h_AddPhiDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_PhiDivideShape.GetXaxis().SetLabelFont(63)
  h_PhiDivideShape.GetXaxis().SetLabelSize(16)
  h_PhiDivideShape.GetYaxis().SetLabelFont(63)
  h_PhiDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_PhiDivideShape.GetXaxis().SetTitle("Phi")
  h_PhiDivideShape.GetXaxis().SetTitleSize(0.07)
  h_PhiDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_PhiDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_PhiDivideShape.GetMaximum()
  Max2 = h_TTPhiDivideShape.GetMaximum()
  Max3 = h_TLPhiDivideShape.GetMaximum()
  Max4 = h_LLPhiDivideShape.GetMaximum()
  Max5 = h_AddPhiDivideShape.GetMaximum()
  Min1 = h_PhiDivideShape.GetMinimum()
  Min2 = h_TTPhiDivideShape.GetMinimum()
  Min3 = h_TLPhiDivideShape.GetMinimum()
  Min4 = h_LLPhiDivideShape.GetMinimum()
  Min5 = h_AddPhiDivideShape.GetMinimum()
  h_PhiDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_PhiSumShape.cd()


  # save the canvas as png file
  c_PhiSumShape.SaveAs("PhiShapeOnly.png")
  # close the canvas
  c_PhiSumShape.Close()



  """
  histogram of CosPhi, TTCosPhi, TLCosPhi, LLCosPhi, TT+TL+LLCosPhi
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosPhiSum = R.TCanvas("c_CosPhiSum", "CosPhiSum", 800, 1000)
  # set the background of this canvas
  c_CosPhiSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosPhi.Draw("Hist")
  h_CosPhi.Draw("SameHE")
  h_TTCosPhi.Draw("SameHE")
  h_TLCosPhi.Draw("SameHE")
  h_LLCosPhi.Draw("SameHE")
  h_AddCosPhi.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosPhiClone1.SetFillColor(2)
  h_TLCosPhiClone1.SetFillColor(3)
  h_TTCosPhiClone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosPhi.SetLineColor(1)
  h_TTCosPhi.SetLineColor(7)
  h_TLCosPhi.SetLineColor(11)
  h_LLCosPhi.SetLineColor(5)
  h_AddCosPhi.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhi.SetLineWidth(3)
  h_TTCosPhi.SetLineWidth(3)
  h_TLCosPhi.SetLineWidth(3)
  h_LLCosPhi.SetLineWidth(3)
  h_AddCosPhi.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosPhi.GetXaxis().SetLabelFont(63)
  hs_CosPhi.GetXaxis().SetLabelSize(16)
  hs_CosPhi.GetYaxis().SetLabelFont(63)
  hs_CosPhi.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosPhi.GetYaxis().SetTitle("Events")
  hs_CosPhi.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosPhi.SetMaximum(int(hs_CosPhi.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosPhiClone1, "TTStack", "F")
  leg.AddEntry(h_TLCosPhiClone1, "TLStack", "F")
  leg.AddEntry(h_LLCosPhiClone1, "LLStack", "F")
  leg.AddEntry(h_CosPhi,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi,"TT","LE")
  leg.AddEntry(h_TLCosPhi,"TL","LE")
  leg.AddEntry(h_LLCosPhi,"LL","LE")
  leg.AddEntry(h_AddCosPhi,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosPhiSum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosPhiDivide.Divide(h_CosPhi, h_AddCosPhi, 1, 1)
  h_TTCosPhiDivide.Divide(h_TTCosPhi, h_AddCosPhi, 1, 1)
  h_TLCosPhiDivide.Divide(h_TLCosPhi, h_AddCosPhi, 1, 1)
  h_LLCosPhiDivide.Divide(h_LLCosPhi, h_AddCosPhi, 1, 1)
  h_AddCosPhiDivide.Divide(h_AddCosPhi, h_AddCosPhi, 1 ,1)

  # draw the histograms of ratio
  h_CosPhiDivide.Draw("HE")
  h_TTCosPhiDivide.Draw("SameHE")
  h_TLCosPhiDivide.Draw("SameHE")
  h_LLCosPhiDivide.Draw("SameHE")
  h_AddCosPhiDivide.Draw("SameHE")
  # set the color of each histogram
  h_CosPhiDivide.SetLineColor(1)
  h_TTCosPhiDivide.SetLineColor(7)
  h_TLCosPhiDivide.SetLineColor(11)
  h_LLCosPhiDivide.SetLineColor(5)
  h_AddCosPhiDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhiDivide.SetLineWidth(3)
  h_TTCosPhiDivide.SetLineWidth(3)
  h_TLCosPhiDivide.SetLineWidth(3)
  h_LLCosPhiDivide.SetLineWidth(3)
  h_AddCosPhiDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosPhiDivide.GetXaxis().SetLabelFont(63)
  h_CosPhiDivide.GetXaxis().SetLabelSize(16)
  h_CosPhiDivide.GetYaxis().SetLabelFont(63)
  h_CosPhiDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosPhiDivide.GetXaxis().SetTitle("CosPhi")
  h_CosPhiDivide.GetXaxis().SetTitleSize(0.07)
  h_CosPhiDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosPhiDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosPhiDivide.GetMaximum()
  Max2 = h_TTCosPhiDivide.GetMaximum()
  Max3 = h_TLCosPhiDivide.GetMaximum()
  Max4 = h_LLCosPhiDivide.GetMaximum()
  Max5 = h_AddCosPhiDivide.GetMaximum()
  Min1 = h_CosPhiDivide.GetMinimum()
  Min2 = h_TTCosPhiDivide.GetMinimum()
  Min3 = h_TLCosPhiDivide.GetMinimum()
  Min4 = h_LLCosPhiDivide.GetMinimum()
  Min5 = h_AddCosPhiDivide.GetMinimum()
  h_CosPhiDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosPhiSum.cd()

  # save the canvas as png file
  c_CosPhiSum.SaveAs("CosPhiSum.png")
  # close the canvas
  c_CosPhiSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosPhiSumShape = R.TCanvas("c_CosPhiSumShape", "CosPhiSumShape", 800, 1000)
  # set the background of this canvas
  c_CosPhiSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosPhiClone2.Draw("HE")
  h_TTCosPhiClone2.Draw("SameHE")
  h_TLCosPhiClone2.Draw("SameHE")
  h_LLCosPhiClone2.Draw("SameHE")
  h_AddCosPhiClone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosPhiClone2.SetLineColor(1)
  h_TTCosPhiClone2.SetLineColor(7)
  h_TLCosPhiClone2.SetLineColor(11)
  h_LLCosPhiClone2.SetLineColor(5)
  h_AddCosPhiClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhiClone2.SetLineWidth(3)
  h_TTCosPhiClone2.SetLineWidth(3)
  h_TLCosPhiClone2.SetLineWidth(3)
  h_LLCosPhiClone2.SetLineWidth(3)
  h_AddCosPhiClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosPhiClone2.GetXaxis().SetLabelFont(63)
  h_CosPhiClone2.GetXaxis().SetLabelSize(16)
  h_CosPhiClone2.GetYaxis().SetLabelFont(63)
  h_CosPhiClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosPhiClone2.GetYaxis().SetTitle("freq.")
  h_CosPhiClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosPhiClone2.GetMaximum()
  Max2 = h_TTCosPhiClone2.GetMaximum()
  Max3 = h_TLCosPhiClone2.GetMaximum()
  Max4 = h_LLCosPhiClone2.GetMaximum()
  Max5 = h_AddCosPhiClone2.GetMaximum()
  h_CosPhiClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosPhiClone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhiClone2,"TT","LE")
  leg.AddEntry(h_TLCosPhiClone2,"TL","LE")
  leg.AddEntry(h_LLCosPhiClone2,"LL","LE")
  leg.AddEntry(h_AddCosPhiClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosPhiSumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosPhiDivideShape.Divide(h_CosPhiClone2, h_AddCosPhiClone2, 1, 1)
  h_TTCosPhiDivideShape.Divide(h_TTCosPhiClone2, h_AddCosPhiClone2, 1, 1)
  h_TLCosPhiDivideShape.Divide(h_TLCosPhiClone2, h_AddCosPhiClone2, 1, 1)
  h_LLCosPhiDivideShape.Divide(h_LLCosPhiClone2, h_AddCosPhiClone2, 1, 1)
  h_AddCosPhiDivideShape.Divide(h_AddCosPhiClone2, h_AddCosPhiClone2, 1 ,1)

  # draw the histograms of ratio
  h_CosPhiDivideShape.Draw("HE")
  h_TTCosPhiDivideShape.Draw("SameHE")
  h_TLCosPhiDivideShape.Draw("SameHE")
  h_LLCosPhiDivideShape.Draw("SameHE")
  h_AddCosPhiDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosPhiDivideShape.SetLineColor(1)
  h_TTCosPhiDivideShape.SetLineColor(7)
  h_TLCosPhiDivideShape.SetLineColor(11)
  h_LLCosPhiDivideShape.SetLineColor(5)
  h_AddCosPhiDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhiDivideShape.SetLineWidth(3)
  h_TTCosPhiDivideShape.SetLineWidth(3)
  h_TLCosPhiDivideShape.SetLineWidth(3)
  h_LLCosPhiDivideShape.SetLineWidth(3)
  h_AddCosPhiDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosPhiDivideShape.GetXaxis().SetLabelFont(63)
  h_CosPhiDivideShape.GetXaxis().SetLabelSize(16)
  h_CosPhiDivideShape.GetYaxis().SetLabelFont(63)
  h_CosPhiDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosPhiDivideShape.GetXaxis().SetTitle("CosPhi")
  h_CosPhiDivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosPhiDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosPhiDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosPhiDivideShape.GetMaximum()
  Max2 = h_TTCosPhiDivideShape.GetMaximum()
  Max3 = h_TLCosPhiDivideShape.GetMaximum()
  Max4 = h_LLCosPhiDivideShape.GetMaximum()
  Max5 = h_AddCosPhiDivideShape.GetMaximum()
  Min1 = h_CosPhiDivideShape.GetMinimum()
  Min2 = h_TTCosPhiDivideShape.GetMinimum()
  Min3 = h_TLCosPhiDivideShape.GetMinimum()
  Min4 = h_LLCosPhiDivideShape.GetMinimum()
  Min5 = h_AddCosPhiDivideShape.GetMinimum()
  h_CosPhiDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosPhiSumShape.cd()


  # save the canvas as png file
  c_CosPhiSumShape.SaveAs("CosPhiShapeOnly.png")
  # close the canvas
  c_CosPhiSumShape.Close()



  """
  histogram of Phi1, TTPhi1, TLPhi1, LLPhi1, TT+TL+LLPhi1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Phi1Sum = R.TCanvas("c_Phi1Sum", "Phi1Sum", 800, 1000)
  # set the background of this canvas
  c_Phi1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_Phi1.Draw("Hist")
  h_Phi1.Draw("SameHE")
  h_TTPhi1.Draw("SameHE")
  h_TLPhi1.Draw("SameHE")
  h_LLPhi1.Draw("SameHE")
  h_AddPhi1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLPhi1Clone1.SetFillColor(2)
  h_TLPhi1Clone1.SetFillColor(3)
  h_TTPhi1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Phi1.SetLineColor(1)
  h_TTPhi1.SetLineColor(7)
  h_TLPhi1.SetLineColor(11)
  h_LLPhi1.SetLineColor(5)
  h_AddPhi1.SetLineColor(46)
  # set the width of each histogram's line
  h_Phi1.SetLineWidth(3)
  h_TTPhi1.SetLineWidth(3)
  h_TLPhi1.SetLineWidth(3)
  h_LLPhi1.SetLineWidth(3)
  h_AddPhi1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Phi1.GetXaxis().SetLabelFont(63)
  hs_Phi1.GetXaxis().SetLabelSize(16)
  hs_Phi1.GetYaxis().SetLabelFont(63)
  hs_Phi1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Phi1.GetYaxis().SetTitle("Events")
  hs_Phi1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Phi1.SetMaximum(int(hs_Phi1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTPhi1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLPhi1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLPhi1Clone1, "LLStack", "F")
  leg.AddEntry(h_Phi1,"Inclusive","LE")
  leg.AddEntry(h_TTPhi1,"TT","LE")
  leg.AddEntry(h_TLPhi1,"TL","LE")
  leg.AddEntry(h_LLPhi1,"LL","LE")
  leg.AddEntry(h_AddPhi1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Phi1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Phi1Divide.Divide(h_Phi1, h_AddPhi1, 1, 1)
  h_TTPhi1Divide.Divide(h_TTPhi1, h_AddPhi1, 1, 1)
  h_TLPhi1Divide.Divide(h_TLPhi1, h_AddPhi1, 1, 1)
  h_LLPhi1Divide.Divide(h_LLPhi1, h_AddPhi1, 1, 1)
  h_AddPhi1Divide.Divide(h_AddPhi1, h_AddPhi1, 1 ,1)

  # draw the histograms of ratio
  h_Phi1Divide.Draw("HE")
  h_TTPhi1Divide.Draw("SameHE")
  h_TLPhi1Divide.Draw("SameHE")
  h_LLPhi1Divide.Draw("SameHE")
  h_AddPhi1Divide.Draw("SameHE")
  # set the color of each histogram
  h_Phi1Divide.SetLineColor(1)
  h_TTPhi1Divide.SetLineColor(7)
  h_TLPhi1Divide.SetLineColor(11)
  h_LLPhi1Divide.SetLineColor(5)
  h_AddPhi1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Phi1Divide.SetLineWidth(3)
  h_TTPhi1Divide.SetLineWidth(3)
  h_TLPhi1Divide.SetLineWidth(3)
  h_LLPhi1Divide.SetLineWidth(3)
  h_AddPhi1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Phi1Divide.GetXaxis().SetLabelFont(63)
  h_Phi1Divide.GetXaxis().SetLabelSize(16)
  h_Phi1Divide.GetYaxis().SetLabelFont(63)
  h_Phi1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Phi1Divide.GetXaxis().SetTitle("Phi1")
  h_Phi1Divide.GetXaxis().SetTitleSize(0.07)
  h_Phi1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Phi1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Phi1Divide.GetMaximum()
  Max2 = h_TTPhi1Divide.GetMaximum()
  Max3 = h_TLPhi1Divide.GetMaximum()
  Max4 = h_LLPhi1Divide.GetMaximum()
  Max5 = h_AddPhi1Divide.GetMaximum()
  Min1 = h_Phi1Divide.GetMinimum()
  Min2 = h_TTPhi1Divide.GetMinimum()
  Min3 = h_TLPhi1Divide.GetMinimum()
  Min4 = h_LLPhi1Divide.GetMinimum()
  Min5 = h_AddPhi1Divide.GetMinimum()
  h_Phi1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Phi1Sum.cd()

  # save the canvas as png file
  c_Phi1Sum.SaveAs("Phi1Sum.png")
  # close the canvas
  c_Phi1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Phi1SumShape = R.TCanvas("c_Phi1SumShape", "Phi1SumShape", 800, 1000)
  # set the background of this canvas
  c_Phi1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Phi1Clone2.Draw("HE")
  h_TTPhi1Clone2.Draw("SameHE")
  h_TLPhi1Clone2.Draw("SameHE")
  h_LLPhi1Clone2.Draw("SameHE")
  h_AddPhi1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Phi1Clone2.SetLineColor(1)
  h_TTPhi1Clone2.SetLineColor(7)
  h_TLPhi1Clone2.SetLineColor(11)
  h_LLPhi1Clone2.SetLineColor(5)
  h_AddPhi1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Phi1Clone2.SetLineWidth(3)
  h_TTPhi1Clone2.SetLineWidth(3)
  h_TLPhi1Clone2.SetLineWidth(3)
  h_LLPhi1Clone2.SetLineWidth(3)
  h_AddPhi1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Phi1Clone2.GetXaxis().SetLabelFont(63)
  h_Phi1Clone2.GetXaxis().SetLabelSize(16)
  h_Phi1Clone2.GetYaxis().SetLabelFont(63)
  h_Phi1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Phi1Clone2.GetYaxis().SetTitle("freq.")
  h_Phi1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Phi1Clone2.GetMaximum()
  Max2 = h_TTPhi1Clone2.GetMaximum()
  Max3 = h_TLPhi1Clone2.GetMaximum()
  Max4 = h_LLPhi1Clone2.GetMaximum()
  Max5 = h_AddPhi1Clone2.GetMaximum()
  h_Phi1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Phi1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTPhi1Clone2,"TT","LE")
  leg.AddEntry(h_TLPhi1Clone2,"TL","LE")
  leg.AddEntry(h_LLPhi1Clone2,"LL","LE")
  leg.AddEntry(h_AddPhi1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Phi1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Phi1DivideShape.Divide(h_Phi1Clone2, h_AddPhi1Clone2, 1, 1)
  h_TTPhi1DivideShape.Divide(h_TTPhi1Clone2, h_AddPhi1Clone2, 1, 1)
  h_TLPhi1DivideShape.Divide(h_TLPhi1Clone2, h_AddPhi1Clone2, 1, 1)
  h_LLPhi1DivideShape.Divide(h_LLPhi1Clone2, h_AddPhi1Clone2, 1, 1)
  h_AddPhi1DivideShape.Divide(h_AddPhi1Clone2, h_AddPhi1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Phi1DivideShape.Draw("HE")
  h_TTPhi1DivideShape.Draw("SameHE")
  h_TLPhi1DivideShape.Draw("SameHE")
  h_LLPhi1DivideShape.Draw("SameHE")
  h_AddPhi1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Phi1DivideShape.SetLineColor(1)
  h_TTPhi1DivideShape.SetLineColor(7)
  h_TLPhi1DivideShape.SetLineColor(11)
  h_LLPhi1DivideShape.SetLineColor(5)
  h_AddPhi1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Phi1DivideShape.SetLineWidth(3)
  h_TTPhi1DivideShape.SetLineWidth(3)
  h_TLPhi1DivideShape.SetLineWidth(3)
  h_LLPhi1DivideShape.SetLineWidth(3)
  h_AddPhi1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Phi1DivideShape.GetXaxis().SetLabelFont(63)
  h_Phi1DivideShape.GetXaxis().SetLabelSize(16)
  h_Phi1DivideShape.GetYaxis().SetLabelFont(63)
  h_Phi1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Phi1DivideShape.GetXaxis().SetTitle("Phi1")
  h_Phi1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Phi1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Phi1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Phi1DivideShape.GetMaximum()
  Max2 = h_TTPhi1DivideShape.GetMaximum()
  Max3 = h_TLPhi1DivideShape.GetMaximum()
  Max4 = h_LLPhi1DivideShape.GetMaximum()
  Max5 = h_AddPhi1DivideShape.GetMaximum()
  Min1 = h_Phi1DivideShape.GetMinimum()
  Min2 = h_TTPhi1DivideShape.GetMinimum()
  Min3 = h_TLPhi1DivideShape.GetMinimum()
  Min4 = h_LLPhi1DivideShape.GetMinimum()
  Min5 = h_AddPhi1DivideShape.GetMinimum()
  h_Phi1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Phi1SumShape.cd()


  # save the canvas as png file
  c_Phi1SumShape.SaveAs("Phi1ShapeOnly.png")
  # close the canvas
  c_Phi1SumShape.Close()



  """
  histogram of CosPhi1, TTCosPhi1, TLCosPhi1, LLCosPhi1, TT+TL+LLCosPhi1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosPhi1Sum = R.TCanvas("c_CosPhi1Sum", "CosPhi1Sum", 800, 1000)
  # set the background of this canvas
  c_CosPhi1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosPhi1.Draw("Hist")
  h_CosPhi1.Draw("SameHE")
  h_TTCosPhi1.Draw("SameHE")
  h_TLCosPhi1.Draw("SameHE")
  h_LLCosPhi1.Draw("SameHE")
  h_AddCosPhi1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosPhi1Clone1.SetFillColor(2)
  h_TLCosPhi1Clone1.SetFillColor(3)
  h_TTCosPhi1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosPhi1.SetLineColor(1)
  h_TTCosPhi1.SetLineColor(7)
  h_TLCosPhi1.SetLineColor(11)
  h_LLCosPhi1.SetLineColor(5)
  h_AddCosPhi1.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhi1.SetLineWidth(3)
  h_TTCosPhi1.SetLineWidth(3)
  h_TLCosPhi1.SetLineWidth(3)
  h_LLCosPhi1.SetLineWidth(3)
  h_AddCosPhi1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosPhi1.GetXaxis().SetLabelFont(63)
  hs_CosPhi1.GetXaxis().SetLabelSize(16)
  hs_CosPhi1.GetYaxis().SetLabelFont(63)
  hs_CosPhi1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosPhi1.GetYaxis().SetTitle("Events")
  hs_CosPhi1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosPhi1.SetMaximum(int(hs_CosPhi1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTCosPhi1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLCosPhi1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLCosPhi1Clone1, "LLStack", "F")
  leg.AddEntry(h_CosPhi1,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi1,"TT","LE")
  leg.AddEntry(h_TLCosPhi1,"TL","LE")
  leg.AddEntry(h_LLCosPhi1,"LL","LE")
  leg.AddEntry(h_AddCosPhi1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosPhi1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosPhi1Divide.Divide(h_CosPhi1, h_AddCosPhi1, 1, 1)
  h_TTCosPhi1Divide.Divide(h_TTCosPhi1, h_AddCosPhi1, 1, 1)
  h_TLCosPhi1Divide.Divide(h_TLCosPhi1, h_AddCosPhi1, 1, 1)
  h_LLCosPhi1Divide.Divide(h_LLCosPhi1, h_AddCosPhi1, 1, 1)
  h_AddCosPhi1Divide.Divide(h_AddCosPhi1, h_AddCosPhi1, 1 ,1)

  # draw the histograms of ratio
  h_CosPhi1Divide.Draw("HE")
  h_TTCosPhi1Divide.Draw("SameHE")
  h_TLCosPhi1Divide.Draw("SameHE")
  h_LLCosPhi1Divide.Draw("SameHE")
  h_AddCosPhi1Divide.Draw("SameHE")
  # set the color of each histogram
  h_CosPhi1Divide.SetLineColor(1)
  h_TTCosPhi1Divide.SetLineColor(7)
  h_TLCosPhi1Divide.SetLineColor(11)
  h_LLCosPhi1Divide.SetLineColor(5)
  h_AddCosPhi1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhi1Divide.SetLineWidth(3)
  h_TTCosPhi1Divide.SetLineWidth(3)
  h_TLCosPhi1Divide.SetLineWidth(3)
  h_LLCosPhi1Divide.SetLineWidth(3)
  h_AddCosPhi1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosPhi1Divide.GetXaxis().SetLabelFont(63)
  h_CosPhi1Divide.GetXaxis().SetLabelSize(16)
  h_CosPhi1Divide.GetYaxis().SetLabelFont(63)
  h_CosPhi1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosPhi1Divide.GetXaxis().SetTitle("CosPhi1")
  h_CosPhi1Divide.GetXaxis().SetTitleSize(0.07)
  h_CosPhi1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosPhi1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosPhi1Divide.GetMaximum()
  Max2 = h_TTCosPhi1Divide.GetMaximum()
  Max3 = h_TLCosPhi1Divide.GetMaximum()
  Max4 = h_LLCosPhi1Divide.GetMaximum()
  Max5 = h_AddCosPhi1Divide.GetMaximum()
  Min1 = h_CosPhi1Divide.GetMinimum()
  Min2 = h_TTCosPhi1Divide.GetMinimum()
  Min3 = h_TLCosPhi1Divide.GetMinimum()
  Min4 = h_LLCosPhi1Divide.GetMinimum()
  Min5 = h_AddCosPhi1Divide.GetMinimum()
  h_CosPhi1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosPhi1Sum.cd()

  # save the canvas as png file
  c_CosPhi1Sum.SaveAs("CosPhi1Sum.png")
  # close the canvas
  c_CosPhi1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosPhi1SumShape = R.TCanvas("c_CosPhi1SumShape", "CosPhi1SumShape", 800, 1000)
  # set the background of this canvas
  c_CosPhi1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosPhi1Clone2.Draw("HE")
  h_TTCosPhi1Clone2.Draw("SameHE")
  h_TLCosPhi1Clone2.Draw("SameHE")
  h_LLCosPhi1Clone2.Draw("SameHE")
  h_AddCosPhi1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_CosPhi1Clone2.SetLineColor(1)
  h_TTCosPhi1Clone2.SetLineColor(7)
  h_TLCosPhi1Clone2.SetLineColor(11)
  h_LLCosPhi1Clone2.SetLineColor(5)
  h_AddCosPhi1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhi1Clone2.SetLineWidth(3)
  h_TTCosPhi1Clone2.SetLineWidth(3)
  h_TLCosPhi1Clone2.SetLineWidth(3)
  h_LLCosPhi1Clone2.SetLineWidth(3)
  h_AddCosPhi1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosPhi1Clone2.GetXaxis().SetLabelFont(63)
  h_CosPhi1Clone2.GetXaxis().SetLabelSize(16)
  h_CosPhi1Clone2.GetYaxis().SetLabelFont(63)
  h_CosPhi1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosPhi1Clone2.GetYaxis().SetTitle("freq.")
  h_CosPhi1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosPhi1Clone2.GetMaximum()
  Max2 = h_TTCosPhi1Clone2.GetMaximum()
  Max3 = h_TLCosPhi1Clone2.GetMaximum()
  Max4 = h_LLCosPhi1Clone2.GetMaximum()
  Max5 = h_AddCosPhi1Clone2.GetMaximum()
  h_CosPhi1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_CosPhi1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi1Clone2,"TT","LE")
  leg.AddEntry(h_TLCosPhi1Clone2,"TL","LE")
  leg.AddEntry(h_LLCosPhi1Clone2,"LL","LE")
  leg.AddEntry(h_AddCosPhi1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosPhi1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_CosPhi1DivideShape.Divide(h_CosPhi1Clone2, h_AddCosPhi1Clone2, 1, 1)
  h_TTCosPhi1DivideShape.Divide(h_TTCosPhi1Clone2, h_AddCosPhi1Clone2, 1, 1)
  h_TLCosPhi1DivideShape.Divide(h_TLCosPhi1Clone2, h_AddCosPhi1Clone2, 1, 1)
  h_LLCosPhi1DivideShape.Divide(h_LLCosPhi1Clone2, h_AddCosPhi1Clone2, 1, 1)
  h_AddCosPhi1DivideShape.Divide(h_AddCosPhi1Clone2, h_AddCosPhi1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosPhi1DivideShape.Draw("HE")
  h_TTCosPhi1DivideShape.Draw("SameHE")
  h_TLCosPhi1DivideShape.Draw("SameHE")
  h_LLCosPhi1DivideShape.Draw("SameHE")
  h_AddCosPhi1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_CosPhi1DivideShape.SetLineColor(1)
  h_TTCosPhi1DivideShape.SetLineColor(7)
  h_TLCosPhi1DivideShape.SetLineColor(11)
  h_LLCosPhi1DivideShape.SetLineColor(5)
  h_AddCosPhi1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosPhi1DivideShape.SetLineWidth(3)
  h_TTCosPhi1DivideShape.SetLineWidth(3)
  h_TLCosPhi1DivideShape.SetLineWidth(3)
  h_LLCosPhi1DivideShape.SetLineWidth(3)
  h_AddCosPhi1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosPhi1DivideShape.GetXaxis().SetLabelFont(63)
  h_CosPhi1DivideShape.GetXaxis().SetLabelSize(16)
  h_CosPhi1DivideShape.GetYaxis().SetLabelFont(63)
  h_CosPhi1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosPhi1DivideShape.GetXaxis().SetTitle("CosPhi1")
  h_CosPhi1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosPhi1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosPhi1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosPhi1DivideShape.GetMaximum()
  Max2 = h_TTCosPhi1DivideShape.GetMaximum()
  Max3 = h_TLCosPhi1DivideShape.GetMaximum()
  Max4 = h_LLCosPhi1DivideShape.GetMaximum()
  Max5 = h_AddCosPhi1DivideShape.GetMaximum()
  Min1 = h_CosPhi1DivideShape.GetMinimum()
  Min2 = h_TTCosPhi1DivideShape.GetMinimum()
  Min3 = h_TLCosPhi1DivideShape.GetMinimum()
  Min4 = h_LLCosPhi1DivideShape.GetMinimum()
  Min5 = h_AddCosPhi1DivideShape.GetMinimum()
  h_CosPhi1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosPhi1SumShape.cd()


  # save the canvas as png file
  c_CosPhi1SumShape.SaveAs("CosPhi1ShapeOnly.png")
  # close the canvas
  c_CosPhi1SumShape.Close()



  """
  histogram of M4l, TTM4l, TLM4l, LLM4l, TT+TL+LLM4l
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M4lSum = R.TCanvas("c_M4lSum", "M4lSum", 800, 1000)
  # set the background of this canvas
  c_M4lSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_M4l.Draw("Hist")
  h_M4l.Draw("SameHE")
  h_TTM4l.Draw("SameHE")
  h_TLM4l.Draw("SameHE")
  h_LLM4l.Draw("SameHE")
  h_AddM4l.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLM4lClone1.SetFillColor(2)
  h_TLM4lClone1.SetFillColor(3)
  h_TTM4lClone1.SetFillColor(9)

  # set the line color of each histogram
  h_M4l.SetLineColor(1)
  h_TTM4l.SetLineColor(7)
  h_TLM4l.SetLineColor(11)
  h_LLM4l.SetLineColor(5)
  h_AddM4l.SetLineColor(46)
  # set the width of each histogram's line
  h_M4l.SetLineWidth(3)
  h_TTM4l.SetLineWidth(3)
  h_TLM4l.SetLineWidth(3)
  h_LLM4l.SetLineWidth(3)
  h_AddM4l.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_M4l.GetXaxis().SetLabelFont(63)
  hs_M4l.GetXaxis().SetLabelSize(16)
  hs_M4l.GetYaxis().SetLabelFont(63)
  hs_M4l.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_M4l.GetYaxis().SetTitle("Events")
  hs_M4l.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_M4l.SetMaximum(int(hs_M4l.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTM4lClone1, "TTStack", "F")
  leg.AddEntry(h_TLM4lClone1, "TLStack", "F")
  leg.AddEntry(h_LLM4lClone1, "LLStack", "F")
  leg.AddEntry(h_M4l,"Inclusive","LE")
  leg.AddEntry(h_TTM4l,"TT","LE")
  leg.AddEntry(h_TLM4l,"TL","LE")
  leg.AddEntry(h_LLM4l,"LL","LE")
  leg.AddEntry(h_AddM4l,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M4lSum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M4lDivide.Divide(h_M4l, h_AddM4l, 1, 1)
  h_TTM4lDivide.Divide(h_TTM4l, h_AddM4l, 1, 1)
  h_TLM4lDivide.Divide(h_TLM4l, h_AddM4l, 1, 1)
  h_LLM4lDivide.Divide(h_LLM4l, h_AddM4l, 1, 1)
  h_AddM4lDivide.Divide(h_AddM4l, h_AddM4l, 1 ,1)

  # draw the histograms of ratio
  h_M4lDivide.Draw("HE")
  h_TTM4lDivide.Draw("SameHE")
  h_TLM4lDivide.Draw("SameHE")
  h_LLM4lDivide.Draw("SameHE")
  h_AddM4lDivide.Draw("SameHE")
  # set the color of each histogram
  h_M4lDivide.SetLineColor(1)
  h_TTM4lDivide.SetLineColor(7)
  h_TLM4lDivide.SetLineColor(11)
  h_LLM4lDivide.SetLineColor(5)
  h_AddM4lDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_M4lDivide.SetLineWidth(3)
  h_TTM4lDivide.SetLineWidth(3)
  h_TLM4lDivide.SetLineWidth(3)
  h_LLM4lDivide.SetLineWidth(3)
  h_AddM4lDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_M4lDivide.GetXaxis().SetLabelFont(63)
  h_M4lDivide.GetXaxis().SetLabelSize(16)
  h_M4lDivide.GetYaxis().SetLabelFont(63)
  h_M4lDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M4lDivide.GetXaxis().SetTitle("M4l/GeV")
  h_M4lDivide.GetXaxis().SetTitleSize(0.07)
  h_M1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M4lDivide.GetMaximum()
  Max2 = h_TTM4lDivide.GetMaximum()
  Max3 = h_TLM4lDivide.GetMaximum()
  Max4 = h_LLM4lDivide.GetMaximum()
  Max5 = h_AddM4lDivide.GetMaximum()
  Min1 = h_M4lDivide.GetMinimum()
  Min2 = h_TTM4lDivide.GetMinimum()
  Min3 = h_TLM4lDivide.GetMinimum()
  Min4 = h_LLM4lDivide.GetMinimum()
  Min5 = h_AddM4lDivide.GetMinimum()
  h_M4lDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M4lSum.cd()

  # save the canvas as png file
  c_M4lSum.SaveAs("M4lSum.png")
  # close the canvas
  c_M4lSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_M4lSumShape = R.TCanvas("c_M4lSumShape", "M4lSumShape", 800, 1000)
  # set the background of this canvas
  c_M4lSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_M4lClone2.Draw("HE")
  h_TTM4lClone2.Draw("SameHE")
  h_TLM4lClone2.Draw("SameHE")
  h_LLM4lClone2.Draw("SameHE")
  h_AddM4lClone2.Draw("SameHE")

  # set the line color of each histogram
  h_M4lClone2.SetLineColor(1)
  h_TTM4lClone2.SetLineColor(7)
  h_TLM4lClone2.SetLineColor(11)
  h_LLM4lClone2.SetLineColor(5)
  h_AddM4lClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_M4lClone2.SetLineWidth(3)
  h_TTM4lClone2.SetLineWidth(3)
  h_TLM4lClone2.SetLineWidth(3)
  h_LLM4lClone2.SetLineWidth(3)
  h_AddM4lClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_M4lClone2.GetXaxis().SetLabelFont(63)
  h_M4lClone2.GetXaxis().SetLabelSize(16)
  h_M4lClone2.GetYaxis().SetLabelFont(63)
  h_M4lClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_M4lClone2.GetYaxis().SetTitle("freq.")
  h_M4lClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_M4lClone2.GetMaximum()
  Max2 = h_TTM4lClone2.GetMaximum()
  Max3 = h_TLM4lClone2.GetMaximum()
  Max4 = h_LLM4lClone2.GetMaximum()
  Max5 = h_AddM4lClone2.GetMaximum()
  h_M4lClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_M4lClone2,"Inclusive","LE")
  leg.AddEntry(h_TTM4lClone2,"TT","LE")
  leg.AddEntry(h_TLM4lClone2,"TL","LE")
  leg.AddEntry(h_LLM4lClone2,"LL","LE")
  leg.AddEntry(h_AddM4lClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_M4lSumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_M4lDivideShape.Divide(h_M4lClone2, h_AddM4lClone2, 1, 1)
  h_TTM4lDivideShape.Divide(h_TTM4lClone2, h_AddM4lClone2, 1, 1)
  h_TLM4lDivideShape.Divide(h_TLM4lClone2, h_AddM4lClone2, 1, 1)
  h_LLM4lDivideShape.Divide(h_LLM4lClone2, h_AddM4lClone2, 1, 1)
  h_AddM4lDivideShape.Divide(h_AddM4lClone2, h_AddM4lClone2, 1 ,1)

  # draw the histograms of ratio
  h_M4lDivideShape.Draw("HE")
  h_TTM4lDivideShape.Draw("SameHE")
  h_TLM4lDivideShape.Draw("SameHE")
  h_LLM4lDivideShape.Draw("SameHE")
  h_AddM4lDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_M4lDivideShape.SetLineColor(1)
  h_TTM4lDivideShape.SetLineColor(7)
  h_TLM4lDivideShape.SetLineColor(11)
  h_LLM4lDivideShape.SetLineColor(5)
  h_AddM4lDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_M4lDivideShape.SetLineWidth(3)
  h_TTM4lDivideShape.SetLineWidth(3)
  h_TLM4lDivideShape.SetLineWidth(3)
  h_LLM4lDivideShape.SetLineWidth(3)
  h_AddM4lDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_M4lDivideShape.GetXaxis().SetLabelFont(63)
  h_M4lDivideShape.GetXaxis().SetLabelSize(16)
  h_M4lDivideShape.GetYaxis().SetLabelFont(63)
  h_M4lDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_M4lDivideShape.GetXaxis().SetTitle("M4l/GeV")
  h_M4lDivideShape.GetXaxis().SetTitleSize(0.07)
  h_M4lDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_M4lDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_M4lDivideShape.GetMaximum()
  Max2 = h_TTM4lDivideShape.GetMaximum()
  Max3 = h_TLM4lDivideShape.GetMaximum()
  Max4 = h_LLM4lDivideShape.GetMaximum()
  Max5 = h_AddM4lDivideShape.GetMaximum()
  Min1 = h_M4lDivideShape.GetMinimum()
  Min2 = h_TTM4lDivideShape.GetMinimum()
  Min3 = h_TLM4lDivideShape.GetMinimum()
  Min4 = h_LLM4lDivideShape.GetMinimum()
  Min5 = h_AddM4lDivideShape.GetMinimum()
  h_M4lDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_M4lSumShape.cd()


  # save the canvas as png file
  c_M4lSumShape.SaveAs("M4lShapeOnly.png")
  # close the canvas
  c_M4lSumShape.Close()



  """
  histogram of Eta1, TTEta1, TLEta1, LLEta1, TT+TL+LLEta1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta1Sum = R.TCanvas("c_Eta1Sum", "Eta1Sum", 800, 1000)
  # set the background of this canvas
  c_Eta1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Eta1.Draw("Hist")
  h_Eta1.Draw("SameHE")
  h_TTEta1.Draw("SameHE")
  h_TLEta1.Draw("SameHE")
  h_LLEta1.Draw("SameHE")
  h_AddEta1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLEta1Clone1.SetFillColor(2)
  h_TLEta1Clone1.SetFillColor(3)
  h_TTEta1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Eta1.SetLineColor(1)
  h_TTEta1.SetLineColor(7)
  h_TLEta1.SetLineColor(11)
  h_LLEta1.SetLineColor(5)
  h_AddEta1.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta1.SetLineWidth(3)
  h_TTEta1.SetLineWidth(3)
  h_TLEta1.SetLineWidth(3)
  h_LLEta1.SetLineWidth(3)
  h_AddEta1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Eta1.GetXaxis().SetLabelFont(63)
  hs_Eta1.GetXaxis().SetLabelSize(16)
  hs_Eta1.GetYaxis().SetLabelFont(63)
  hs_Eta1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Eta1.GetYaxis().SetTitle("Events")
  hs_Eta1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Eta1.SetMaximum(int(hs_Eta1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTEta1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLEta1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLEta1Clone1, "LLStack", "F")
  leg.AddEntry(h_Eta1,"Inclusive","LE")
  leg.AddEntry(h_TTEta1,"TT","LE")
  leg.AddEntry(h_TLEta1,"TL","LE")
  leg.AddEntry(h_LLEta1,"LL","LE")
  leg.AddEntry(h_AddEta1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta1Divide.Divide(h_Eta1, h_AddEta1, 1, 1)
  h_TTEta1Divide.Divide(h_TTEta1, h_AddEta1, 1, 1)
  h_TLEta1Divide.Divide(h_TLEta1, h_AddEta1, 1, 1)
  h_LLEta1Divide.Divide(h_LLEta1, h_AddEta1, 1, 1)
  h_AddEta1Divide.Divide(h_AddEta1, h_AddEta1, 1 ,1)

  # draw the histograms of ratio
  h_Eta1Divide.Draw("HE")
  h_TTEta1Divide.Draw("SameHE")
  h_TLEta1Divide.Draw("SameHE")
  h_LLEta1Divide.Draw("SameHE")
  h_AddEta1Divide.Draw("SameHE")
  # set the color of each histogram
  h_Eta1Divide.SetLineColor(1)
  h_TTEta1Divide.SetLineColor(7)
  h_TLEta1Divide.SetLineColor(11)
  h_LLEta1Divide.SetLineColor(5)
  h_AddEta1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta1Divide.SetLineWidth(3)
  h_TTEta1Divide.SetLineWidth(3)
  h_TLEta1Divide.SetLineWidth(3)
  h_LLEta1Divide.SetLineWidth(3)
  h_AddEta1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta1Divide.GetXaxis().SetLabelFont(63)
  h_Eta1Divide.GetXaxis().SetLabelSize(16)
  h_Eta1Divide.GetYaxis().SetLabelFont(63)
  h_Eta1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta1Divide.GetXaxis().SetTitle("Eta1")
  h_Eta1Divide.GetXaxis().SetTitleSize(0.07)
  h_Eta1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta1Divide.GetMaximum()
  Max2 = h_TTEta1Divide.GetMaximum()
  Max3 = h_TLEta1Divide.GetMaximum()
  Max4 = h_LLEta1Divide.GetMaximum()
  Max5 = h_AddEta1Divide.GetMaximum()
  Min1 = h_Eta1Divide.GetMinimum()
  Min2 = h_TTEta1Divide.GetMinimum()
  Min3 = h_TLEta1Divide.GetMinimum()
  Min4 = h_LLEta1Divide.GetMinimum()
  Min5 = h_AddEta1Divide.GetMinimum()
  h_Eta1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta1Sum.cd()

  # save the canvas as png file
  c_Eta1Sum.SaveAs("Eta1Sum.png")
  # close the canvas
  c_Eta1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta1SumShape = R.TCanvas("c_Eta1SumShape", "Eta1SumShape", 800, 1000)
  # set the background of this canvas
  c_Eta1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Eta1Clone2.Draw("HE")
  h_TTEta1Clone2.Draw("SameHE")
  h_TLEta1Clone2.Draw("SameHE")
  h_LLEta1Clone2.Draw("SameHE")
  h_AddEta1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Eta1Clone2.SetLineColor(1)
  h_TTEta1Clone2.SetLineColor(7)
  h_TLEta1Clone2.SetLineColor(11)
  h_LLEta1Clone2.SetLineColor(5)
  h_AddEta1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta1Clone2.SetLineWidth(3)
  h_TTEta1Clone2.SetLineWidth(3)
  h_TLEta1Clone2.SetLineWidth(3)
  h_LLEta1Clone2.SetLineWidth(3)
  h_AddEta1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Eta1Clone2.GetXaxis().SetLabelFont(63)
  h_Eta1Clone2.GetXaxis().SetLabelSize(16)
  h_Eta1Clone2.GetYaxis().SetLabelFont(63)
  h_Eta1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Eta1Clone2.GetYaxis().SetTitle("freq.")
  h_Eta1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Eta1Clone2.GetMaximum()
  Max2 = h_TTEta1Clone2.GetMaximum()
  Max3 = h_TLEta1Clone2.GetMaximum()
  Max4 = h_LLEta1Clone2.GetMaximum()
  Max5 = h_AddEta1Clone2.GetMaximum()
  h_Eta1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Eta1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTEta1Clone2,"TT","LE")
  leg.AddEntry(h_TLEta1Clone2,"TL","LE")
  leg.AddEntry(h_LLEta1Clone2,"LL","LE")
  leg.AddEntry(h_AddEta1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta1DivideShape.Divide(h_Eta1Clone2, h_AddEta1Clone2, 1, 1)
  h_TTEta1DivideShape.Divide(h_TTEta1Clone2, h_AddEta1Clone2, 1, 1)
  h_TLEta1DivideShape.Divide(h_TLEta1Clone2, h_AddEta1Clone2, 1, 1)
  h_LLEta1DivideShape.Divide(h_LLEta1Clone2, h_AddEta1Clone2, 1, 1)
  h_AddEta1DivideShape.Divide(h_AddEta1Clone2, h_AddEta1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Eta1DivideShape.Draw("HE")
  h_TTEta1DivideShape.Draw("SameHE")
  h_TLEta1DivideShape.Draw("SameHE")
  h_LLEta1DivideShape.Draw("SameHE")
  h_AddEta1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Eta1DivideShape.SetLineColor(1)
  h_TTEta1DivideShape.SetLineColor(7)
  h_TLEta1DivideShape.SetLineColor(11)
  h_LLEta1DivideShape.SetLineColor(5)
  h_AddEta1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta1DivideShape.SetLineWidth(3)
  h_TTEta1DivideShape.SetLineWidth(3)
  h_TLEta1DivideShape.SetLineWidth(3)
  h_LLEta1DivideShape.SetLineWidth(3)
  h_AddEta1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta1DivideShape.GetXaxis().SetLabelFont(63)
  h_Eta1DivideShape.GetXaxis().SetLabelSize(16)
  h_Eta1DivideShape.GetYaxis().SetLabelFont(63)
  h_Eta1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta1DivideShape.GetXaxis().SetTitle("Eta1")
  h_Eta1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Eta1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta1DivideShape.GetMaximum()
  Max2 = h_TTEta1DivideShape.GetMaximum()
  Max3 = h_TLEta1DivideShape.GetMaximum()
  Max4 = h_LLEta1DivideShape.GetMaximum()
  Max5 = h_AddEta1DivideShape.GetMaximum()
  Min1 = h_Eta1DivideShape.GetMinimum()
  Min2 = h_TTEta1DivideShape.GetMinimum()
  Min3 = h_TLEta1DivideShape.GetMinimum()
  Min4 = h_LLEta1DivideShape.GetMinimum()
  Min5 = h_AddEta1DivideShape.GetMinimum()
  h_Eta1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta1SumShape.cd()


  # save the canvas as png file
  c_Eta1SumShape.SaveAs("Eta1ShapeOnly.png")
  # close the canvas
  c_Eta1SumShape.Close()



  """
  histogram of Eta2, TTEta2, TLEta2, LLEta2, TT+TL+LLEta2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta2Sum = R.TCanvas("c_Eta2Sum", "Eta2Sum", 800, 1000)
  # set the background of this canvas
  c_Eta2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Eta2.Draw("Hist")
  h_Eta2.Draw("SameHE")
  h_TTEta2.Draw("SameHE")
  h_TLEta2.Draw("SameHE")
  h_LLEta2.Draw("SameHE")
  h_AddEta2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLEta2Clone1.SetFillColor(2)
  h_TLEta2Clone1.SetFillColor(3)
  h_TTEta2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Eta2.SetLineColor(1)
  h_TTEta2.SetLineColor(7)
  h_TLEta2.SetLineColor(11)
  h_LLEta2.SetLineColor(5)
  h_AddEta2.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta2.SetLineWidth(3)
  h_TTEta2.SetLineWidth(3)
  h_TLEta2.SetLineWidth(3)
  h_LLEta2.SetLineWidth(3)
  h_AddEta2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Eta2.GetXaxis().SetLabelFont(63)
  hs_Eta2.GetXaxis().SetLabelSize(16)
  hs_Eta2.GetYaxis().SetLabelFont(63)
  hs_Eta2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Eta2.GetYaxis().SetTitle("Events")
  hs_Eta2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Eta2.SetMaximum(int(hs_Eta2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTEta2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLEta2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLEta2Clone1, "LLStack", "F")
  leg.AddEntry(h_Eta2,"Inclusive","LE")
  leg.AddEntry(h_TTEta2,"TT","LE")
  leg.AddEntry(h_TLEta2,"TL","LE")
  leg.AddEntry(h_LLEta2,"LL","LE")
  leg.AddEntry(h_AddEta2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta2Divide.Divide(h_Eta2, h_AddEta2, 1, 1)
  h_TTEta2Divide.Divide(h_TTEta2, h_AddEta2, 1, 1)
  h_TLEta2Divide.Divide(h_TLEta2, h_AddEta2, 1, 1)
  h_LLEta2Divide.Divide(h_LLEta2, h_AddEta2, 1, 1)
  h_AddEta2Divide.Divide(h_AddEta2, h_AddEta2, 1 ,1)

  # draw the histograms of ratio
  h_Eta2Divide.Draw("HE")
  h_TTEta2Divide.Draw("SameHE")
  h_TLEta2Divide.Draw("SameHE")
  h_LLEta2Divide.Draw("SameHE")
  h_AddEta2Divide.Draw("SameHE")
  # set the color of each histogram
  h_Eta2Divide.SetLineColor(1)
  h_TTEta2Divide.SetLineColor(7)
  h_TLEta2Divide.SetLineColor(11)
  h_LLEta2Divide.SetLineColor(5)
  h_AddEta2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta2Divide.SetLineWidth(3)
  h_TTEta2Divide.SetLineWidth(3)
  h_TLEta2Divide.SetLineWidth(3)
  h_LLEta2Divide.SetLineWidth(3)
  h_AddEta2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta2Divide.GetXaxis().SetLabelFont(63)
  h_Eta2Divide.GetXaxis().SetLabelSize(16)
  h_Eta2Divide.GetYaxis().SetLabelFont(63)
  h_Eta2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta2Divide.GetXaxis().SetTitle("Eta2")
  h_Eta2Divide.GetXaxis().SetTitleSize(0.07)
  h_Eta2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta2Divide.GetMaximum()
  Max2 = h_TTEta2Divide.GetMaximum()
  Max3 = h_TLEta2Divide.GetMaximum()
  Max4 = h_LLEta2Divide.GetMaximum()
  Max5 = h_AddEta2Divide.GetMaximum()
  Min1 = h_Eta2Divide.GetMinimum()
  Min2 = h_TTEta2Divide.GetMinimum()
  Min3 = h_TLEta2Divide.GetMinimum()
  Min4 = h_LLEta2Divide.GetMinimum()
  Min5 = h_AddEta2Divide.GetMinimum()
  h_Eta2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta2Sum.cd()

  # save the canvas as png file
  c_Eta2Sum.SaveAs("Eta2Sum.png")
  # close the canvas
  c_Eta2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta2SumShape = R.TCanvas("c_Eta2SumShape", "Eta2SumShape", 800, 1000)
  # set the background of this canvas
  c_Eta2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Eta2Clone2.Draw("HE")
  h_TTEta2Clone2.Draw("SameHE")
  h_TLEta2Clone2.Draw("SameHE")
  h_LLEta2Clone2.Draw("SameHE")
  h_AddEta2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Eta2Clone2.SetLineColor(1)
  h_TTEta2Clone2.SetLineColor(7)
  h_TLEta2Clone2.SetLineColor(11)
  h_LLEta2Clone2.SetLineColor(5)
  h_AddEta2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta2Clone2.SetLineWidth(3)
  h_TTEta2Clone2.SetLineWidth(3)
  h_TLEta2Clone2.SetLineWidth(3)
  h_LLEta2Clone2.SetLineWidth(3)
  h_AddEta2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Eta2Clone2.GetXaxis().SetLabelFont(63)
  h_Eta2Clone2.GetXaxis().SetLabelSize(16)
  h_Eta2Clone2.GetYaxis().SetLabelFont(63)
  h_Eta2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Eta2Clone2.GetYaxis().SetTitle("freq.")
  h_Eta2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Eta2Clone2.GetMaximum()
  Max2 = h_TTEta2Clone2.GetMaximum()
  Max3 = h_TLEta2Clone2.GetMaximum()
  Max4 = h_LLEta2Clone2.GetMaximum()
  Max5 = h_AddEta2Clone2.GetMaximum()
  h_Eta2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Eta2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTEta2Clone2,"TT","LE")
  leg.AddEntry(h_TLEta2Clone2,"TL","LE")
  leg.AddEntry(h_LLEta2Clone2,"LL","LE")
  leg.AddEntry(h_AddEta2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta2DivideShape.Divide(h_Eta2Clone2, h_AddEta2Clone2, 1, 1)
  h_TTEta2DivideShape.Divide(h_TTEta2Clone2, h_AddEta2Clone2, 1, 1)
  h_TLEta2DivideShape.Divide(h_TLEta2Clone2, h_AddEta2Clone2, 1, 1)
  h_LLEta2DivideShape.Divide(h_LLEta2Clone2, h_AddEta2Clone2, 1, 1)
  h_AddEta2DivideShape.Divide(h_AddEta2Clone2, h_AddEta2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Eta2DivideShape.Draw("HE")
  h_TTEta2DivideShape.Draw("SameHE")
  h_TLEta2DivideShape.Draw("SameHE")
  h_LLEta2DivideShape.Draw("SameHE")
  h_AddEta2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Eta2DivideShape.SetLineColor(1)
  h_TTEta2DivideShape.SetLineColor(7)
  h_TLEta2DivideShape.SetLineColor(11)
  h_LLEta2DivideShape.SetLineColor(5)
  h_AddEta2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta2DivideShape.SetLineWidth(3)
  h_TTEta2DivideShape.SetLineWidth(3)
  h_TLEta2DivideShape.SetLineWidth(3)
  h_LLEta2DivideShape.SetLineWidth(3)
  h_AddEta2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta2DivideShape.GetXaxis().SetLabelFont(63)
  h_Eta2DivideShape.GetXaxis().SetLabelSize(16)
  h_Eta2DivideShape.GetYaxis().SetLabelFont(63)
  h_Eta2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta2DivideShape.GetXaxis().SetTitle("Eta2")
  h_Eta2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Eta2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta2DivideShape.GetMaximum()
  Max2 = h_TTEta2DivideShape.GetMaximum()
  Max3 = h_TLEta2DivideShape.GetMaximum()
  Max4 = h_LLEta2DivideShape.GetMaximum()
  Max5 = h_AddEta2DivideShape.GetMaximum()
  Min1 = h_Eta2DivideShape.GetMinimum()
  Min2 = h_TTEta2DivideShape.GetMinimum()
  Min3 = h_TLEta2DivideShape.GetMinimum()
  Min4 = h_LLEta2DivideShape.GetMinimum()
  Min5 = h_AddEta2DivideShape.GetMinimum()
  h_Eta2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta2SumShape.cd()


  # save the canvas as png file
  c_Eta2SumShape.SaveAs("Eta2ShapeOnly.png")
  # close the canvas
  c_Eta2SumShape.Close()



  """
  histogram of Eta4l, TTEta4l, TLEta4l, LLEta4l, TT+TL+LLEta4l
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta4lSum = R.TCanvas("c_Eta4lSum", "Eta4lSum", 800, 1000)
  # set the background of this canvas
  c_Eta4lSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Eta4l.Draw("Hist")
  h_Eta4l.Draw("SameHE")
  h_TTEta4l.Draw("SameHE")
  h_TLEta4l.Draw("SameHE")
  h_LLEta4l.Draw("SameHE")
  h_AddEta4l.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLEta4lClone1.SetFillColor(2)
  h_TLEta4lClone1.SetFillColor(3)
  h_TTEta4lClone1.SetFillColor(9)

  # set the line color of each histogram
  h_Eta4l.SetLineColor(1)
  h_TTEta4l.SetLineColor(7)
  h_TLEta4l.SetLineColor(11)
  h_LLEta4l.SetLineColor(5)
  h_AddEta4l.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta4l.SetLineWidth(3)
  h_TTEta4l.SetLineWidth(3)
  h_TLEta4l.SetLineWidth(3)
  h_LLEta4l.SetLineWidth(3)
  h_AddEta4l.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Eta4l.GetXaxis().SetLabelFont(63)
  hs_Eta4l.GetXaxis().SetLabelSize(16)
  hs_Eta4l.GetYaxis().SetLabelFont(63)
  hs_Eta4l.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Eta4l.GetYaxis().SetTitle("Events")
  hs_Eta4l.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Eta4l.SetMaximum(int(hs_Eta4l.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTEta4lClone1, "TTStack", "F")
  leg.AddEntry(h_TLEta4lClone1, "TLStack", "F")
  leg.AddEntry(h_LLEta4lClone1, "LLStack", "F")
  leg.AddEntry(h_Eta4l,"Inclusive","LE")
  leg.AddEntry(h_TTEta4l,"TT","LE")
  leg.AddEntry(h_TLEta4l,"TL","LE")
  leg.AddEntry(h_LLEta4l,"LL","LE")
  leg.AddEntry(h_AddEta4l,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta4lSum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta4lDivide.Divide(h_Eta4l, h_AddEta4l, 1, 1)
  h_TTEta4lDivide.Divide(h_TTEta4l, h_AddEta4l, 1, 1)
  h_TLEta4lDivide.Divide(h_TLEta4l, h_AddEta4l, 1, 1)
  h_LLEta4lDivide.Divide(h_LLEta4l, h_AddEta4l, 1, 1)
  h_AddEta4lDivide.Divide(h_AddEta4l, h_AddEta4l, 1 ,1)

  # draw the histograms of ratio
  h_Eta4lDivide.Draw("HE")
  h_TTEta4lDivide.Draw("SameHE")
  h_TLEta4lDivide.Draw("SameHE")
  h_LLEta4lDivide.Draw("SameHE")
  h_AddEta4lDivide.Draw("SameHE")
  # set the color of each histogram
  h_Eta4lDivide.SetLineColor(1)
  h_TTEta4lDivide.SetLineColor(7)
  h_TLEta4lDivide.SetLineColor(11)
  h_LLEta4lDivide.SetLineColor(5)
  h_AddEta4lDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta4lDivide.SetLineWidth(3)
  h_TTEta4lDivide.SetLineWidth(3)
  h_TLEta4lDivide.SetLineWidth(3)
  h_LLEta4lDivide.SetLineWidth(3)
  h_AddEta4lDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta4lDivide.GetXaxis().SetLabelFont(63)
  h_Eta4lDivide.GetXaxis().SetLabelSize(16)
  h_Eta4lDivide.GetYaxis().SetLabelFont(63)
  h_Eta4lDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta4lDivide.GetXaxis().SetTitle("Eta4l")
  h_Eta4lDivide.GetXaxis().SetTitleSize(0.07)
  h_Eta4lDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta4lDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta4lDivide.GetMaximum()
  Max2 = h_TTEta4lDivide.GetMaximum()
  Max3 = h_TLEta4lDivide.GetMaximum()
  Max4 = h_LLEta4lDivide.GetMaximum()
  Max5 = h_AddEta4lDivide.GetMaximum()
  Min1 = h_Eta4lDivide.GetMinimum()
  Min2 = h_TTEta4lDivide.GetMinimum()
  Min3 = h_TLEta4lDivide.GetMinimum()
  Min4 = h_LLEta4lDivide.GetMinimum()
  Min5 = h_AddEta4lDivide.GetMinimum()
  h_Eta4lDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta4lSum.cd()

  # save the canvas as png file
  c_Eta4lSum.SaveAs("Eta4lSum.png")
  # close the canvas
  c_Eta4lSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Eta4lSumShape = R.TCanvas("c_Eta4lSumShape", "Eta4lSumShape", 800, 1000)
  # set the background of this canvas
  c_Eta4lSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Eta4lClone2.Draw("HE")
  h_TTEta4lClone2.Draw("SameHE")
  h_TLEta4lClone2.Draw("SameHE")
  h_LLEta4lClone2.Draw("SameHE")
  h_AddEta4lClone2.Draw("SameHE")

  # set the line color of each histogram
  h_Eta4lClone2.SetLineColor(1)
  h_TTEta4lClone2.SetLineColor(7)
  h_TLEta4lClone2.SetLineColor(11)
  h_LLEta4lClone2.SetLineColor(5)
  h_AddEta4lClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta4lClone2.SetLineWidth(3)
  h_TTEta4lClone2.SetLineWidth(3)
  h_TLEta4lClone2.SetLineWidth(3)
  h_LLEta4lClone2.SetLineWidth(3)
  h_AddEta4lClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Eta4lClone2.GetXaxis().SetLabelFont(63)
  h_Eta4lClone2.GetXaxis().SetLabelSize(16)
  h_Eta4lClone2.GetYaxis().SetLabelFont(63)
  h_Eta4lClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Eta4lClone2.GetYaxis().SetTitle("freq.")
  h_Eta4lClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Eta4lClone2.GetMaximum()
  Max2 = h_TTEta4lClone2.GetMaximum()
  Max3 = h_TLEta4lClone2.GetMaximum()
  Max4 = h_LLEta4lClone2.GetMaximum()
  Max5 = h_AddEta4lClone2.GetMaximum()
  h_Eta4lClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Eta4lClone2,"Inclusive","LE")
  leg.AddEntry(h_TTEta4lClone2,"TT","LE")
  leg.AddEntry(h_TLEta4lClone2,"TL","LE")
  leg.AddEntry(h_LLEta4lClone2,"LL","LE")
  leg.AddEntry(h_AddEta4lClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Eta4lSumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Eta4lDivideShape.Divide(h_Eta4lClone2, h_AddEta4lClone2, 1, 1)
  h_TTEta4lDivideShape.Divide(h_TTEta4lClone2, h_AddEta4lClone2, 1, 1)
  h_TLEta4lDivideShape.Divide(h_TLEta4lClone2, h_AddEta4lClone2, 1, 1)
  h_LLEta4lDivideShape.Divide(h_LLEta4lClone2, h_AddEta4lClone2, 1, 1)
  h_AddEta4lDivideShape.Divide(h_AddEta4lClone2, h_AddEta4lClone2, 1 ,1)

  # draw the histograms of ratio
  h_Eta4lDivideShape.Draw("HE")
  h_TTEta4lDivideShape.Draw("SameHE")
  h_TLEta4lDivideShape.Draw("SameHE")
  h_LLEta4lDivideShape.Draw("SameHE")
  h_AddEta4lDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Eta4lDivideShape.SetLineColor(1)
  h_TTEta4lDivideShape.SetLineColor(7)
  h_TLEta4lDivideShape.SetLineColor(11)
  h_LLEta4lDivideShape.SetLineColor(5)
  h_AddEta4lDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Eta4lDivideShape.SetLineWidth(3)
  h_TTEta4lDivideShape.SetLineWidth(3)
  h_TLEta4lDivideShape.SetLineWidth(3)
  h_LLEta4lDivideShape.SetLineWidth(3)
  h_AddEta4lDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Eta4lDivideShape.GetXaxis().SetLabelFont(63)
  h_Eta4lDivideShape.GetXaxis().SetLabelSize(16)
  h_Eta4lDivideShape.GetYaxis().SetLabelFont(63)
  h_Eta4lDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Eta4lDivideShape.GetXaxis().SetTitle("Eta4l")
  h_Eta4lDivideShape.GetXaxis().SetTitleSize(0.07)
  h_Eta4lDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Eta4lDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Eta4lDivideShape.GetMaximum()
  Max2 = h_TTEta4lDivideShape.GetMaximum()
  Max3 = h_TLEta4lDivideShape.GetMaximum()
  Max4 = h_LLEta4lDivideShape.GetMaximum()
  Max5 = h_AddEta4lDivideShape.GetMaximum()
  Min1 = h_Eta4lDivideShape.GetMinimum()
  Min2 = h_TTEta4lDivideShape.GetMinimum()
  Min3 = h_TLEta4lDivideShape.GetMinimum()
  Min4 = h_LLEta4lDivideShape.GetMinimum()
  Min5 = h_AddEta4lDivideShape.GetMinimum()
  h_Eta4lDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Eta4lSumShape.cd()


  # save the canvas as png file
  c_Eta4lSumShape.SaveAs("Eta4lShapeOnly.png")
  # close the canvas
  c_Eta4lSumShape.Close()



  """
  histogram of Pt1, TTPt1, TLPt1, LLPt1, TT+TL+LLPt1
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt1Sum = R.TCanvas("c_Pt1Sum", "Pt1Sum", 800, 1000)
  # set the background of this canvas
  c_Pt1Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Pt1.Draw("Hist")
  h_Pt1.Draw("SameHE")
  h_TTPt1.Draw("SameHE")
  h_TLPt1.Draw("SameHE")
  h_LLPt1.Draw("SameHE")
  h_AddPt1.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLPt1Clone1.SetFillColor(2)
  h_TLPt1Clone1.SetFillColor(3)
  h_TTPt1Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Pt1.SetLineColor(1)
  h_TTPt1.SetLineColor(7)
  h_TLPt1.SetLineColor(11)
  h_LLPt1.SetLineColor(5)
  h_AddPt1.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt1.SetLineWidth(3)
  h_TTPt1.SetLineWidth(3)
  h_TLPt1.SetLineWidth(3)
  h_LLPt1.SetLineWidth(3)
  h_AddPt1.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Pt1.GetXaxis().SetLabelFont(63)
  hs_Pt1.GetXaxis().SetLabelSize(16)
  hs_Pt1.GetYaxis().SetLabelFont(63)
  hs_Pt1.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Pt1.GetYaxis().SetTitle("Events")
  hs_Pt1.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Pt1.SetMaximum(int(hs_Pt1.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTPt1Clone1, "TTStack", "F")
  leg.AddEntry(h_TLPt1Clone1, "TLStack", "F")
  leg.AddEntry(h_LLPt1Clone1, "LLStack", "F")
  leg.AddEntry(h_Pt1,"Inclusive","LE")
  leg.AddEntry(h_TTPt1,"TT","LE")
  leg.AddEntry(h_TLPt1,"TL","LE")
  leg.AddEntry(h_LLPt1,"LL","LE")
  leg.AddEntry(h_AddPt1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt1Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt1Divide.Divide(h_Pt1, h_AddPt1, 1, 1)
  h_TTPt1Divide.Divide(h_TTPt1, h_AddPt1, 1, 1)
  h_TLPt1Divide.Divide(h_TLPt1, h_AddPt1, 1, 1)
  h_LLPt1Divide.Divide(h_LLPt1, h_AddPt1, 1, 1)
  h_AddPt1Divide.Divide(h_AddPt1, h_AddPt1, 1 ,1)

  # draw the histograms of ratio
  h_Pt1Divide.Draw("HE")
  h_TTPt1Divide.Draw("SameHE")
  h_TLPt1Divide.Draw("SameHE")
  h_LLPt1Divide.Draw("SameHE")
  h_AddPt1Divide.Draw("SameHE")
  # set the color of each histogram
  h_Pt1Divide.SetLineColor(1)
  h_TTPt1Divide.SetLineColor(7)
  h_TLPt1Divide.SetLineColor(11)
  h_LLPt1Divide.SetLineColor(5)
  h_AddPt1Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt1Divide.SetLineWidth(3)
  h_TTPt1Divide.SetLineWidth(3)
  h_TLPt1Divide.SetLineWidth(3)
  h_LLPt1Divide.SetLineWidth(3)
  h_AddPt1Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt1Divide.GetXaxis().SetLabelFont(63)
  h_Pt1Divide.GetXaxis().SetLabelSize(16)
  h_Pt1Divide.GetYaxis().SetLabelFont(63)
  h_Pt1Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt1Divide.GetXaxis().SetTitle("Pt1/GeV")
  h_Pt1Divide.GetXaxis().SetTitleSize(0.07)
  h_Pt1Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt1Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt1Divide.GetMaximum()
  Max2 = h_TTPt1Divide.GetMaximum()
  Max3 = h_TLPt1Divide.GetMaximum()
  Max4 = h_LLPt1Divide.GetMaximum()
  Max5 = h_AddPt1Divide.GetMaximum()
  Min1 = h_Pt1Divide.GetMinimum()
  Min2 = h_TTPt1Divide.GetMinimum()
  Min3 = h_TLPt1Divide.GetMinimum()
  Min4 = h_LLPt1Divide.GetMinimum()
  Min5 = h_AddPt1Divide.GetMinimum()
  h_Pt1Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt1Sum.cd()

  # save the canvas as png file
  c_Pt1Sum.SaveAs("Pt1Sum.png")
  # close the canvas
  c_Pt1Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt1SumShape = R.TCanvas("c_Pt1SumShape", "Pt1SumShape", 800, 1000)
  # set the background of this canvas
  c_Pt1SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Pt1Clone2.Draw("HE")
  h_TTPt1Clone2.Draw("SameHE")
  h_TLPt1Clone2.Draw("SameHE")
  h_LLPt1Clone2.Draw("SameHE")
  h_AddPt1Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Pt1Clone2.SetLineColor(1)
  h_TTPt1Clone2.SetLineColor(7)
  h_TLPt1Clone2.SetLineColor(11)
  h_LLPt1Clone2.SetLineColor(5)
  h_AddPt1Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt1Clone2.SetLineWidth(3)
  h_TTPt1Clone2.SetLineWidth(3)
  h_TLPt1Clone2.SetLineWidth(3)
  h_LLPt1Clone2.SetLineWidth(3)
  h_AddPt1Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Pt1Clone2.GetXaxis().SetLabelFont(63)
  h_Pt1Clone2.GetXaxis().SetLabelSize(16)
  h_Pt1Clone2.GetYaxis().SetLabelFont(63)
  h_Pt1Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Pt1Clone2.GetYaxis().SetTitle("freq.")
  h_Pt1Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Pt1Clone2.GetMaximum()
  Max2 = h_TTPt1Clone2.GetMaximum()
  Max3 = h_TLPt1Clone2.GetMaximum()
  Max4 = h_LLPt1Clone2.GetMaximum()
  Max5 = h_AddPt1Clone2.GetMaximum()
  h_Pt1Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Pt1Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTPt1Clone2,"TT","LE")
  leg.AddEntry(h_TLPt1Clone2,"TL","LE")
  leg.AddEntry(h_LLPt1Clone2,"LL","LE")
  leg.AddEntry(h_AddPt1Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt1SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt1DivideShape.Divide(h_Pt1Clone2, h_AddPt1Clone2, 1, 1)
  h_TTPt1DivideShape.Divide(h_TTPt1Clone2, h_AddPt1Clone2, 1, 1)
  h_TLPt1DivideShape.Divide(h_TLPt1Clone2, h_AddPt1Clone2, 1, 1)
  h_LLPt1DivideShape.Divide(h_LLPt1Clone2, h_AddPt1Clone2, 1, 1)
  h_AddPt1DivideShape.Divide(h_AddPt1Clone2, h_AddPt1Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Pt1DivideShape.Draw("HE")
  h_TTPt1DivideShape.Draw("SameHE")
  h_TLPt1DivideShape.Draw("SameHE")
  h_LLPt1DivideShape.Draw("SameHE")
  h_AddPt1DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Pt1DivideShape.SetLineColor(1)
  h_TTPt1DivideShape.SetLineColor(7)
  h_TLPt1DivideShape.SetLineColor(11)
  h_LLPt1DivideShape.SetLineColor(5)
  h_AddPt1DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt1DivideShape.SetLineWidth(3)
  h_TTPt1DivideShape.SetLineWidth(3)
  h_TLPt1DivideShape.SetLineWidth(3)
  h_LLPt1DivideShape.SetLineWidth(3)
  h_AddPt1DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt1DivideShape.GetXaxis().SetLabelFont(63)
  h_Pt1DivideShape.GetXaxis().SetLabelSize(16)
  h_Pt1DivideShape.GetYaxis().SetLabelFont(63)
  h_Pt1DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt1DivideShape.GetXaxis().SetTitle("Pt1/GeV")
  h_Pt1DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Pt1DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt1DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt1DivideShape.GetMaximum()
  Max2 = h_TTPt1DivideShape.GetMaximum()
  Max3 = h_TLPt1DivideShape.GetMaximum()
  Max4 = h_LLPt1DivideShape.GetMaximum()
  Max5 = h_AddPt1DivideShape.GetMaximum()
  Min1 = h_Pt1DivideShape.GetMinimum()
  Min2 = h_TTPt1DivideShape.GetMinimum()
  Min3 = h_TLPt1DivideShape.GetMinimum()
  Min4 = h_LLPt1DivideShape.GetMinimum()
  Min5 = h_AddPt1DivideShape.GetMinimum()
  h_Pt1DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt1SumShape.cd()


  # save the canvas as png file
  c_Pt1SumShape.SaveAs("Pt1ShapeOnly.png")
  # close the canvas
  c_Pt1SumShape.Close()



  """
  histogram of Pt2, TTPt2, TLPt2, LLPt2, TT+TL+LLPt2
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt2Sum = R.TCanvas("c_Pt2Sum", "Pt2Sum", 800, 1000)
  # set the background of this canvas
  c_Pt2Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Pt2.Draw("Hist")
  h_Pt2.Draw("SameHE")
  h_TTPt2.Draw("SameHE")
  h_TLPt2.Draw("SameHE")
  h_LLPt2.Draw("SameHE")
  h_AddPt2.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLPt2Clone1.SetFillColor(2)
  h_TLPt2Clone1.SetFillColor(3)
  h_TTPt2Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_Pt2.SetLineColor(1)
  h_TTPt2.SetLineColor(7)
  h_TLPt2.SetLineColor(11)
  h_LLPt2.SetLineColor(5)
  h_AddPt2.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt2.SetLineWidth(3)
  h_TTPt2.SetLineWidth(3)
  h_TLPt2.SetLineWidth(3)
  h_LLPt2.SetLineWidth(3)
  h_AddPt2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Pt2.GetXaxis().SetLabelFont(63)
  hs_Pt2.GetXaxis().SetLabelSize(16)
  hs_Pt2.GetYaxis().SetLabelFont(63)
  hs_Pt2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Pt2.GetYaxis().SetTitle("Events")
  hs_Pt2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Pt2.SetMaximum(int(hs_Pt2.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTPt2Clone1, "TTStack", "F")
  leg.AddEntry(h_TLPt2Clone1, "TLStack", "F")
  leg.AddEntry(h_LLPt2Clone1, "LLStack", "F")
  leg.AddEntry(h_Pt2,"Inclusive","LE")
  leg.AddEntry(h_TTPt2,"TT","LE")
  leg.AddEntry(h_TLPt2,"TL","LE")
  leg.AddEntry(h_LLPt2,"LL","LE")
  leg.AddEntry(h_AddPt2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt2Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt2Divide.Divide(h_Pt2, h_AddPt2, 1, 1)
  h_TTPt2Divide.Divide(h_TTPt2, h_AddPt2, 1, 1)
  h_TLPt2Divide.Divide(h_TLPt2, h_AddPt2, 1, 1)
  h_LLPt2Divide.Divide(h_LLPt2, h_AddPt2, 1, 1)
  h_AddPt2Divide.Divide(h_AddPt2, h_AddPt2, 1 ,1)

  # draw the histograms of ratio
  h_Pt2Divide.Draw("HE")
  h_TTPt2Divide.Draw("SameHE")
  h_TLPt2Divide.Draw("SameHE")
  h_LLPt2Divide.Draw("SameHE")
  h_AddPt2Divide.Draw("SameHE")
  # set the color of each histogram
  h_Pt2Divide.SetLineColor(1)
  h_TTPt2Divide.SetLineColor(7)
  h_TLPt2Divide.SetLineColor(11)
  h_LLPt2Divide.SetLineColor(5)
  h_AddPt2Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt2Divide.SetLineWidth(3)
  h_TTPt2Divide.SetLineWidth(3)
  h_TLPt2Divide.SetLineWidth(3)
  h_LLPt2Divide.SetLineWidth(3)
  h_AddPt2Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt2Divide.GetXaxis().SetLabelFont(63)
  h_Pt2Divide.GetXaxis().SetLabelSize(16)
  h_Pt2Divide.GetYaxis().SetLabelFont(63)
  h_Pt2Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt2Divide.GetXaxis().SetTitle("Pt2/GeV")
  h_Pt2Divide.GetXaxis().SetTitleSize(0.07)
  h_Pt2Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt2Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt2Divide.GetMaximum()
  Max2 = h_TTPt2Divide.GetMaximum()
  Max3 = h_TLPt2Divide.GetMaximum()
  Max4 = h_LLPt2Divide.GetMaximum()
  Max5 = h_AddPt2Divide.GetMaximum()
  Min1 = h_Pt2Divide.GetMinimum()
  Min2 = h_TTPt2Divide.GetMinimum()
  Min3 = h_TLPt2Divide.GetMinimum()
  Min4 = h_LLPt2Divide.GetMinimum()
  Min5 = h_AddPt2Divide.GetMinimum()
  h_Pt2Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt2Sum.cd()

  # save the canvas as png file
  c_Pt2Sum.SaveAs("Pt2Sum.png")
  # close the canvas
  c_Pt2Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt2SumShape = R.TCanvas("c_Pt2SumShape", "Pt2SumShape", 800, 1000)
  # set the background of this canvas
  c_Pt2SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Pt2Clone2.Draw("HE")
  h_TTPt2Clone2.Draw("SameHE")
  h_TLPt2Clone2.Draw("SameHE")
  h_LLPt2Clone2.Draw("SameHE")
  h_AddPt2Clone2.Draw("SameHE")

  # set the line color of each histogram
  h_Pt2Clone2.SetLineColor(1)
  h_TTPt2Clone2.SetLineColor(7)
  h_TLPt2Clone2.SetLineColor(11)
  h_LLPt2Clone2.SetLineColor(5)
  h_AddPt2Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt2Clone2.SetLineWidth(3)
  h_TTPt2Clone2.SetLineWidth(3)
  h_TLPt2Clone2.SetLineWidth(3)
  h_LLPt2Clone2.SetLineWidth(3)
  h_AddPt2Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Pt2Clone2.GetXaxis().SetLabelFont(63)
  h_Pt2Clone2.GetXaxis().SetLabelSize(16)
  h_Pt2Clone2.GetYaxis().SetLabelFont(63)
  h_Pt2Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Pt2Clone2.GetYaxis().SetTitle("freq.")
  h_Pt2Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Pt2Clone2.GetMaximum()
  Max2 = h_TTPt2Clone2.GetMaximum()
  Max3 = h_TLPt2Clone2.GetMaximum()
  Max4 = h_LLPt2Clone2.GetMaximum()
  Max5 = h_AddPt2Clone2.GetMaximum()
  h_Pt2Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Pt2Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTPt2Clone2,"TT","LE")
  leg.AddEntry(h_TLPt2Clone2,"TL","LE")
  leg.AddEntry(h_LLPt2Clone2,"LL","LE")
  leg.AddEntry(h_AddPt2Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt2SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt2DivideShape.Divide(h_Pt2Clone2, h_AddPt2Clone2, 1, 1)
  h_TTPt2DivideShape.Divide(h_TTPt2Clone2, h_AddPt2Clone2, 1, 1)
  h_TLPt2DivideShape.Divide(h_TLPt2Clone2, h_AddPt2Clone2, 1, 1)
  h_LLPt2DivideShape.Divide(h_LLPt2Clone2, h_AddPt2Clone2, 1, 1)
  h_AddPt2DivideShape.Divide(h_AddPt2Clone2, h_AddPt2Clone2, 1 ,1)

  # draw the histograms of ratio
  h_Pt2DivideShape.Draw("HE")
  h_TTPt2DivideShape.Draw("SameHE")
  h_TLPt2DivideShape.Draw("SameHE")
  h_LLPt2DivideShape.Draw("SameHE")
  h_AddPt2DivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Pt2DivideShape.SetLineColor(1)
  h_TTPt2DivideShape.SetLineColor(7)
  h_TLPt2DivideShape.SetLineColor(11)
  h_LLPt2DivideShape.SetLineColor(5)
  h_AddPt2DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt2DivideShape.SetLineWidth(3)
  h_TTPt2DivideShape.SetLineWidth(3)
  h_TLPt2DivideShape.SetLineWidth(3)
  h_LLPt2DivideShape.SetLineWidth(3)
  h_AddPt2DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt2DivideShape.GetXaxis().SetLabelFont(63)
  h_Pt2DivideShape.GetXaxis().SetLabelSize(16)
  h_Pt2DivideShape.GetYaxis().SetLabelFont(63)
  h_Pt2DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt2DivideShape.GetXaxis().SetTitle("Pt2/GeV")
  h_Pt2DivideShape.GetXaxis().SetTitleSize(0.07)
  h_Pt2DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt2DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt2DivideShape.GetMaximum()
  Max2 = h_TTPt2DivideShape.GetMaximum()
  Max3 = h_TLPt2DivideShape.GetMaximum()
  Max4 = h_LLPt2DivideShape.GetMaximum()
  Max5 = h_AddPt2DivideShape.GetMaximum()
  Min1 = h_Pt2DivideShape.GetMinimum()
  Min2 = h_TTPt2DivideShape.GetMinimum()
  Min3 = h_TLPt2DivideShape.GetMinimum()
  Min4 = h_LLPt2DivideShape.GetMinimum()
  Min5 = h_AddPt2DivideShape.GetMinimum()
  h_Pt2DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt2SumShape.cd()


  # save the canvas as png file
  c_Pt2SumShape.SaveAs("Pt2ShapeOnly.png")
  # close the canvas
  c_Pt2SumShape.Close()



  """
  histogram of Pt4l, TTPt4l, TLPt4l, LLPt4l, TT+TL+LLPt4l
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt4lSum = R.TCanvas("c_Pt4lSum", "Pt4lSum", 800, 1000)
  # set the background of this canvas
  c_Pt4lSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_Pt4l.Draw("Hist")
  h_Pt4l.Draw("SameHE")
  h_TTPt4l.Draw("SameHE")
  h_TLPt4l.Draw("SameHE")
  h_LLPt4l.Draw("SameHE")
  h_AddPt4l.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLPt4lClone1.SetFillColor(2)
  h_TLPt4lClone1.SetFillColor(3)
  h_TTPt4lClone1.SetFillColor(9)

  # set the line color of each histogram
  h_Pt4l.SetLineColor(1)
  h_TTPt4l.SetLineColor(7)
  h_TLPt4l.SetLineColor(11)
  h_LLPt4l.SetLineColor(5)
  h_AddPt4l.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt4l.SetLineWidth(3)
  h_TTPt4l.SetLineWidth(3)
  h_TLPt4l.SetLineWidth(3)
  h_LLPt4l.SetLineWidth(3)
  h_AddPt4l.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_Pt4l.GetXaxis().SetLabelFont(63)
  hs_Pt4l.GetXaxis().SetLabelSize(16)
  hs_Pt4l.GetYaxis().SetLabelFont(63)
  hs_Pt4l.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_Pt4l.GetYaxis().SetTitle("Events")
  hs_Pt4l.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_Pt4l.SetMaximum(int(hs_Pt4l.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTPt4lClone1, "TTStack", "F")
  leg.AddEntry(h_TLPt4lClone1, "TLStack", "F")
  leg.AddEntry(h_LLPt4lClone1, "LLStack", "F")
  leg.AddEntry(h_Pt4l,"Inclusive","LE")
  leg.AddEntry(h_TTPt4l,"TT","LE")
  leg.AddEntry(h_TLPt4l,"TL","LE")
  leg.AddEntry(h_LLPt4l,"LL","LE")
  leg.AddEntry(h_AddPt4l,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt4lSum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt4lDivide.Divide(h_Pt4l, h_AddPt4l, 1, 1)
  h_TTPt4lDivide.Divide(h_TTPt4l, h_AddPt4l, 1, 1)
  h_TLPt4lDivide.Divide(h_TLPt4l, h_AddPt4l, 1, 1)
  h_LLPt4lDivide.Divide(h_LLPt4l, h_AddPt4l, 1, 1)
  h_AddPt4lDivide.Divide(h_AddPt4l, h_AddPt4l, 1 ,1)

  # draw the histograms of ratio
  h_Pt4lDivide.Draw("HE")
  h_TTPt4lDivide.Draw("SameHE")
  h_TLPt4lDivide.Draw("SameHE")
  h_LLPt4lDivide.Draw("SameHE")
  h_AddPt4lDivide.Draw("SameHE")
  # set the color of each histogram
  h_Pt4lDivide.SetLineColor(1)
  h_TTPt4lDivide.SetLineColor(7)
  h_TLPt4lDivide.SetLineColor(11)
  h_LLPt4lDivide.SetLineColor(5)
  h_AddPt4lDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt4lDivide.SetLineWidth(3)
  h_TTPt4lDivide.SetLineWidth(3)
  h_TLPt4lDivide.SetLineWidth(3)
  h_LLPt4lDivide.SetLineWidth(3)
  h_AddPt4lDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt4lDivide.GetXaxis().SetLabelFont(63)
  h_Pt4lDivide.GetXaxis().SetLabelSize(16)
  h_Pt4lDivide.GetYaxis().SetLabelFont(63)
  h_Pt4lDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt4lDivide.GetXaxis().SetTitle("Pt4l/GeV")
  h_Pt4lDivide.GetXaxis().SetTitleSize(0.07)
  h_Pt4lDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt4lDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt4lDivide.GetMaximum()
  Max2 = h_TTPt4lDivide.GetMaximum()
  Max3 = h_TLPt4lDivide.GetMaximum()
  Max4 = h_LLPt4lDivide.GetMaximum()
  Max5 = h_AddPt4lDivide.GetMaximum()
  Min1 = h_Pt4lDivide.GetMinimum()
  Min2 = h_TTPt4lDivide.GetMinimum()
  Min3 = h_TLPt4lDivide.GetMinimum()
  Min4 = h_LLPt4lDivide.GetMinimum()
  Min5 = h_AddPt4lDivide.GetMinimum()
  h_Pt4lDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt4lSum.cd()

  # save the canvas as png file
  c_Pt4lSum.SaveAs("Pt4lSum.png")
  # close the canvas
  c_Pt4lSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Pt4lSumShape = R.TCanvas("c_Pt4lSumShape", "Pt4lSumShape", 800, 1000)
  # set the background of this canvas
  c_Pt4lSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_Pt4lClone2.Draw("HE")
  h_TTPt4lClone2.Draw("SameHE")
  h_TLPt4lClone2.Draw("SameHE")
  h_LLPt4lClone2.Draw("SameHE")
  h_AddPt4lClone2.Draw("SameHE")

  # set the line color of each histogram
  h_Pt4lClone2.SetLineColor(1)
  h_TTPt4lClone2.SetLineColor(7)
  h_TLPt4lClone2.SetLineColor(11)
  h_LLPt4lClone2.SetLineColor(5)
  h_AddPt4lClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt4lClone2.SetLineWidth(3)
  h_TTPt4lClone2.SetLineWidth(3)
  h_TLPt4lClone2.SetLineWidth(3)
  h_LLPt4lClone2.SetLineWidth(3)
  h_AddPt4lClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_Pt4lClone2.GetXaxis().SetLabelFont(63)
  h_Pt4lClone2.GetXaxis().SetLabelSize(16)
  h_Pt4lClone2.GetYaxis().SetLabelFont(63)
  h_Pt4lClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_Pt4lClone2.GetYaxis().SetTitle("freq.")
  h_Pt4lClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_Pt4lClone2.GetMaximum()
  Max2 = h_TTPt4lClone2.GetMaximum()
  Max3 = h_TLPt4lClone2.GetMaximum()
  Max4 = h_LLPt4lClone2.GetMaximum()
  Max5 = h_AddPt4lClone2.GetMaximum()
  h_Pt4lClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_Pt4lClone2,"Inclusive","LE")
  leg.AddEntry(h_TTPt4lClone2,"TT","LE")
  leg.AddEntry(h_TLPt4lClone2,"TL","LE")
  leg.AddEntry(h_LLPt4lClone2,"LL","LE")
  leg.AddEntry(h_AddPt4lClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Pt4lSumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_Pt4lDivideShape.Divide(h_Pt4lClone2, h_AddPt4lClone2, 1, 1)
  h_TTPt4lDivideShape.Divide(h_TTPt4lClone2, h_AddPt4lClone2, 1, 1)
  h_TLPt4lDivideShape.Divide(h_TLPt4lClone2, h_AddPt4lClone2, 1, 1)
  h_LLPt4lDivideShape.Divide(h_LLPt4lClone2, h_AddPt4lClone2, 1, 1)
  h_AddPt4lDivideShape.Divide(h_AddPt4lClone2, h_AddPt4lClone2, 1 ,1)

  # draw the histograms of ratio
  h_Pt4lDivideShape.Draw("HE")
  h_TTPt4lDivideShape.Draw("SameHE")
  h_TLPt4lDivideShape.Draw("SameHE")
  h_LLPt4lDivideShape.Draw("SameHE")
  h_AddPt4lDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_Pt4lDivideShape.SetLineColor(1)
  h_TTPt4lDivideShape.SetLineColor(7)
  h_TLPt4lDivideShape.SetLineColor(11)
  h_LLPt4lDivideShape.SetLineColor(5)
  h_AddPt4lDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_Pt4lDivideShape.SetLineWidth(3)
  h_TTPt4lDivideShape.SetLineWidth(3)
  h_TLPt4lDivideShape.SetLineWidth(3)
  h_LLPt4lDivideShape.SetLineWidth(3)
  h_AddPt4lDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_Pt4lDivideShape.GetXaxis().SetLabelFont(63)
  h_Pt4lDivideShape.GetXaxis().SetLabelSize(16)
  h_Pt4lDivideShape.GetYaxis().SetLabelFont(63)
  h_Pt4lDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_Pt4lDivideShape.GetXaxis().SetTitle("Pt4l/GeV")
  h_Pt4lDivideShape.GetXaxis().SetTitleSize(0.07)
  h_Pt4lDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_Pt4lDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_Pt4lDivideShape.GetMaximum()
  Max2 = h_TTPt4lDivideShape.GetMaximum()
  Max3 = h_TLPt4lDivideShape.GetMaximum()
  Max4 = h_LLPt4lDivideShape.GetMaximum()
  Max5 = h_AddPt4lDivideShape.GetMaximum()
  Min1 = h_Pt4lDivideShape.GetMinimum()
  Min2 = h_TTPt4lDivideShape.GetMinimum()
  Min3 = h_TLPt4lDivideShape.GetMinimum()
  Min4 = h_LLPt4lDivideShape.GetMinimum()
  Min5 = h_AddPt4lDivideShape.GetMinimum()
  h_Pt4lDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Pt4lSumShape.cd()


  # save the canvas as png file
  c_Pt4lSumShape.SaveAs("Pt4lShapeOnly.png")
  # close the canvas
  c_Pt4lSumShape.Close()





  # close the ROOTFile
  rootfile.Close()



if __name__ == "__main__":

  InputROOTFile="KinematicQuantity_ssh.root"
  plot(InputROOTFile)















