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
  h_CosTheta3 = rootfile.Get("CosTheta3")
  h_CosTheta4 = rootfile.Get("CosTheta4")

  h_TTCosTheta1 = rootfile.Get("TTCosTheta1")
  h_TTCosTheta2 = rootfile.Get("TTCosTheta2")
  h_TTCosTheta3 = rootfile.Get("TTCosTheta3")
  h_TTCosTheta4 = rootfile.Get("TTCosTheta4")
  h_TLCosTheta1 = rootfile.Get("TLCosTheta1")
  h_TLCosTheta2 = rootfile.Get("TLCosTheta2")
  h_TLCosTheta3 = rootfile.Get("TLCosTheta3")
  h_TLCosTheta4 = rootfile.Get("TLCosTheta4")
  h_LLCosTheta1 = rootfile.Get("LLCosTheta1")
  h_LLCosTheta2 = rootfile.Get("LLCosTheta2")
  h_LLCosTheta3 = rootfile.Get("LLCosTheta3")
  h_LLCosTheta4 = rootfile.Get("LLCosTheta4")

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
  h_CosTheta3.SetTitle("")
  h_CosTheta4.SetTitle("")

  h_TTCosTheta1.SetTitle("")
  h_TTCosTheta2.SetTitle("")
  h_TTCosTheta3.SetTitle("")
  h_TTCosTheta4.SetTitle("")
  h_TLCosTheta1.SetTitle("")
  h_TLCosTheta2.SetTitle("")
  h_TLCosTheta3.SetTitle("")
  h_TLCosTheta4.SetTitle("")
  h_LLCosTheta1.SetTitle("")
  h_LLCosTheta2.SetTitle("")
  h_LLCosTheta3.SetTitle("")
  h_LLCosTheta4.SetTitle("")

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



  """
  renormalize all the histograms, since the mass of M1 and M2 have underflow and overflow, add them to the 1st bin and last bin.
  """

  h_M1.Scale(0.02419*139*1000/20000)
  h_M1.SetBinContent(1, h_M1.GetBinContent(0)+h_M1.GetBinContent(1))
  h_M1.SetBinContent(40, h_M1.GetBinContent(40)+h_M1.GetBinContent(41))

  h_M2.Scale(0.02419*139*1000/20000)
  h_M2.SetBinContent(1, h_M2.GetBinContent(0)+h_M2.GetBinContent(1))
  h_M2.SetBinContent(40, h_M2.GetBinContent(40)+h_M2.GetBinContent(41))

  h_M1MOTHUP.Scale(0.02419*139*1000/20000)
  h_M1MOTHUP.SetBinContent(1, h_M1MOTHUP.GetBinContent(0)+h_M1MOTHUP.GetBinContent(1))
  h_M1MOTHUP.SetBinContent(40, h_M1MOTHUP.GetBinContent(40)+h_M1MOTHUP.GetBinContent(41))

  h_M2MOTHUP.Scale(0.02419*139*1000/20000)
  h_M2MOTHUP.SetBinContent(1, h_M2MOTHUP.GetBinContent(0)+h_M2MOTHUP.GetBinContent(1))
  h_M2MOTHUP.SetBinContent(40, h_M2MOTHUP.GetBinContent(40)+h_M2MOTHUP.GetBinContent(41))

  h_TTM1.Scale(0.01688*139*1000/20000)
  h_TTM1.SetBinContent(1, h_TTM1.GetBinContent(0)+h_TTM1.GetBinContent(1))
  h_TTM1.SetBinContent(40, h_TTM1.GetBinContent(40)+h_TTM1.GetBinContent(41))

  h_TTM2.Scale(0.01688*139*1000/20000)
  h_TTM2.SetBinContent(1, h_TTM2.GetBinContent(0)+h_TTM2.GetBinContent(1))
  h_TTM2.SetBinContent(40, h_TTM2.GetBinContent(40)+h_TTM2.GetBinContent(41))

  h_TLM1.Scale(0.005741*139*1000/20000)
  h_TLM1.SetBinContent(1, h_TLM1.GetBinContent(0)+h_TLM1.GetBinContent(1))
  h_TLM1.SetBinContent(40, h_TLM1.GetBinContent(40)+h_TLM1.GetBinContent(41))

  h_TLM2.Scale(0.005741*139*1000/20000)
  h_TLM2.SetBinContent(1, h_TLM2.GetBinContent(0)+h_TLM2.GetBinContent(1))
  h_TLM2.SetBinContent(40, h_TLM2.GetBinContent(40)+h_TLM2.GetBinContent(41))

  h_LLM1.Scale(0.001406*139*1000/20000)
  h_LLM1.SetBinContent(1, h_LLM1.GetBinContent(0)+h_LLM1.GetBinContent(1))
  h_LLM1.SetBinContent(40, h_LLM1.GetBinContent(40)+h_LLM1.GetBinContent(41))

  h_LLM2.Scale(0.001406*139*1000/20000)
  h_LLM2.SetBinContent(1, h_LLM2.GetBinContent(0)+h_LLM2.GetBinContent(1))
  h_LLM2.SetBinContent(40, h_LLM2.GetBinContent(40)+h_LLM2.GetBinContent(41))

  h_CosTheta1.Scale(0.02419*139*1000/20000)
  h_CosTheta2.Scale(0.02419*139*1000/20000)
  h_CosTheta3.Scale(0.02419*139*1000/20000)
  h_CosTheta4.Scale(0.02419*139*1000/20000)

  h_TTCosTheta1.Scale(0.01688*139*1000/20000)
  h_TTCosTheta2.Scale(0.01688*139*1000/20000)
  h_TTCosTheta3.Scale(0.01688*139*1000/20000)
  h_TTCosTheta4.Scale(0.01688*139*1000/20000)

  h_TLCosTheta1.Scale(0.005741*139*1000/20000)
  h_TLCosTheta2.Scale(0.005741*139*1000/20000)
  h_TLCosTheta3.Scale(0.005741*139*1000/20000)
  h_TLCosTheta4.Scale(0.005741*139*1000/20000)

  h_LLCosTheta1.Scale(0.001406*139*1000/20000)
  h_LLCosTheta2.Scale(0.001406*139*1000/20000)
  h_LLCosTheta3.Scale(0.001406*139*1000/20000)
  h_LLCosTheta4.Scale(0.001406*139*1000/20000)

  h_ThetaStar1.Scale(0.02419*139*1000/20000)
  h_ThetaStar2.Scale(0.02419*139*1000/20000)

  h_TTThetaStar1.Scale(0.01688*139*1000/20000)
  h_TTThetaStar2.Scale(0.01688*139*1000/20000)

  h_TLThetaStar1.Scale(0.005741*139*1000/20000)
  h_TLThetaStar2.Scale(0.005741*139*1000/20000)

  h_LLThetaStar1.Scale(0.001406*139*1000/20000)
  h_LLThetaStar2.Scale(0.001406*139*1000/20000)

  h_CosThetaStar1.Scale(0.02419*139*1000/20000)
  h_CosThetaStar2.Scale(0.02419*139*1000/20000)

  h_TTCosThetaStar1.Scale(0.01688*139*1000/20000)
  h_TTCosThetaStar2.Scale(0.01688*139*1000/20000)

  h_TLCosThetaStar1.Scale(0.005741*139*1000/20000)
  h_TLCosThetaStar2.Scale(0.005741*139*1000/20000)

  h_LLCosThetaStar1.Scale(0.001406*139*1000/20000)
  h_LLCosThetaStar2.Scale(0.001406*139*1000/20000)

  h_Phi.Scale(0.02419*139*1000/20000)
  h_TTPhi.Scale(0.01688*139*1000/20000)
  h_TLPhi.Scale(0.005741*139*1000/20000)
  h_LLPhi.Scale(0.001406*139*1000/20000)

  h_CosPhi.Scale(0.02419*139*1000/20000)
  h_TTCosPhi.Scale(0.01688*139*1000/20000)
  h_TLCosPhi.Scale(0.005741*139*1000/20000)
  h_LLCosPhi.Scale(0.001406*139*1000/20000)

  h_Phi1.Scale(0.02419*139*1000/20000)
  h_TTPhi1.Scale(0.01688*139*1000/20000)
  h_TLPhi1.Scale(0.005741*139*1000/20000)
  h_LLPhi1.Scale(0.001406*139*1000/20000)

  h_CosPhi1.Scale(0.02419*139*1000/20000)
  h_TTCosPhi1.Scale(0.01688*139*1000/20000)
  h_TLCosPhi1.Scale(0.005741*139*1000/20000)
  h_LLCosPhi1.Scale(0.001406*139*1000/20000)



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

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta3 = R.TH1F("TT+TL+LLCosTheta3", "", nbins, xmin, xmax)
  h_AddCosTheta3.Add(h_TTCosTheta3, 1)
  h_AddCosTheta3.Add(h_TLCosTheta3, 1)
  h_AddCosTheta3.Add(h_LLCosTheta3, 1)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta4 = R.TH1F("TT+TL+LLCosTheta4", "", nbins, xmin, xmax)
  h_AddCosTheta4.Add(h_TTCosTheta4, 1)
  h_AddCosTheta4.Add(h_TLCosTheta4, 1)
  h_AddCosTheta4.Add(h_LLCosTheta4, 1)

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

  h_CosTheta3Divide = R.TH1F("CosTheta3Divide", "", 40, -1, 1)
  h_TTCosTheta3Divide = R.TH1F("TTCosTheta3Divide", "", 40, -1, 1)
  h_TLCosTheta3Divide = R.TH1F("TLCosTheta3Divide", "", 40, -1, 1)
  h_LLCosTheta3Divide = R.TH1F("LLCosTheta3Divide", "", 40, -1, 1)
  h_AddCosTheta3Divide = R.TH1F("AddCosTheta3Divide", "", 40, -1, 1)

  h_CosTheta4Divide = R.TH1F("CosTheta4Divide", "", 40, -1, 1)
  h_TTCosTheta4Divide = R.TH1F("TTCosTheta4Divide", "", 40, -1, 1)
  h_TLCosTheta4Divide = R.TH1F("TLCosTheta4Divide", "", 40, -1, 1)
  h_LLCosTheta4Divide = R.TH1F("LLCosTheta4Divide", "", 40, -1, 1)
  h_AddCosTheta4Divide = R.TH1F("AddCosTheta4Divide", "", 40, -1, 1)

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

  h_CosTheta3DivideShape = R.TH1F("CosTheta3DivideShape", "", 40, -1, 1)
  h_TTCosTheta3DivideShape = R.TH1F("TTCosTheta3DivideShape", "", 40, -1, 1)
  h_TLCosTheta3DivideShape = R.TH1F("TLCosTheta3DivideShape", "", 40, -1, 1)
  h_LLCosTheta3DivideShape = R.TH1F("LLCosTheta3DivideShape", "", 40, -1, 1)
  h_AddCosTheta3DivideShape = R.TH1F("AddCosTheta3DivideShape", "", 40, -1, 1)

  h_CosTheta4DivideShape = R.TH1F("CosTheta4DivideShape", "", 40, -1, 1)
  h_TTCosTheta4DivideShape = R.TH1F("TTCosTheta4DivideShape", "", 40, -1, 1)
  h_TLCosTheta4DivideShape = R.TH1F("TLCosTheta4DivideShape", "", 40, -1, 1)
  h_LLCosTheta4DivideShape = R.TH1F("LLCosTheta4DivideShape", "", 40, -1, 1)
  h_AddCosTheta4DivideShape = R.TH1F("AddCosTheta4DivideShape", "", 40, -1, 1)

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

  hs_CosTheta3 = R.THStack("hs_CosTheta3", "")
  h_LLCosTheta3Clone1 = h_LLCosTheta3.Clone("h_LLCosTheta3Clone1")
  h_TLCosTheta3Clone1 = h_TLCosTheta3.Clone("h_TLCosTheta3Clone1")
  h_TTCosTheta3Clone1 = h_TTCosTheta3.Clone("h_TTCosTheta3Clone1")
  h_LLCosTheta3Clone1.SetLineWidth(0)
  h_TLCosTheta3Clone1.SetLineWidth(0)
  h_TTCosTheta3Clone1.SetLineWidth(0)
  hs_CosTheta3.Add(h_LLCosTheta3Clone1, "Hist")
  hs_CosTheta3.Add(h_TLCosTheta3Clone1, "SameHist")
  hs_CosTheta3.Add(h_TTCosTheta3Clone1, "SameHist")

  hs_CosTheta4 = R.THStack("hs_CosTheta4", "")
  h_LLCosTheta4Clone1 = h_LLCosTheta4.Clone("h_LLCosTheta4Clone1")
  h_TLCosTheta4Clone1 = h_TLCosTheta4.Clone("h_TLCosTheta4Clone1")
  h_TTCosTheta4Clone1 = h_TTCosTheta4.Clone("h_TTCosTheta4Clone1")
  h_LLCosTheta4Clone1.SetLineWidth(0)
  h_TLCosTheta4Clone1.SetLineWidth(0)
  h_TTCosTheta4Clone1.SetLineWidth(0)
  hs_CosTheta4.Add(h_LLCosTheta4Clone1, "Hist")
  hs_CosTheta4.Add(h_TLCosTheta4Clone1, "SameHist")
  hs_CosTheta4.Add(h_TTCosTheta4Clone1, "SameHist")

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

  h_CosTheta3Clone2 = h_CosTheta3.Clone("h_CosTheta3Clone2")
  h_TTCosTheta3Clone2 = h_TTCosTheta3.Clone("h_TTCosTheta3Clone2")
  h_TLCosTheta3Clone2 = h_TLCosTheta3.Clone("h_TLCosTheta3Clone2")
  h_LLCosTheta3Clone2 = h_LLCosTheta3.Clone("h_LLCosTheta3Clone2")
  h_AddCosTheta3Clone2 = h_AddCosTheta3.Clone("h_AddCosTheta3Clone2")

  h_CosTheta4Clone2 = h_CosTheta4.Clone("h_CosTheta4Clone2")
  h_TTCosTheta4Clone2 = h_TTCosTheta4.Clone("h_TTCosTheta4Clone2")
  h_TLCosTheta4Clone2 = h_TLCosTheta4.Clone("h_TLCosTheta4Clone2")
  h_LLCosTheta4Clone2 = h_LLCosTheta4.Clone("h_LLCosTheta4Clone2")
  h_AddCosTheta4Clone2 = h_AddCosTheta4.Clone("h_AddCosTheta4Clone2")

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

  h_CosTheta3Clone2.Scale(1/h_CosTheta3Clone2.Integral())
  h_TTCosTheta3Clone2.Scale(1/h_TTCosTheta3Clone2.Integral())
  h_TLCosTheta3Clone2.Scale(1/h_TLCosTheta3Clone2.Integral())
  h_LLCosTheta3Clone2.Scale(1/h_LLCosTheta3Clone2.Integral())
  h_AddCosTheta3Clone2.Scale(1/h_AddCosTheta3Clone2.Integral())

  h_CosTheta4Clone2.Scale(1/h_CosTheta4Clone2.Integral())
  h_TTCosTheta4Clone2.Scale(1/h_TTCosTheta4Clone2.Integral())
  h_TLCosTheta4Clone2.Scale(1/h_TLCosTheta4Clone2.Integral())
  h_LLCosTheta4Clone2.Scale(1/h_LLCosTheta4Clone2.Integral())
  h_AddCosTheta4Clone2.Scale(1/h_AddCosTheta4Clone2.Integral())

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
  h_M1.Draw("SameLE")
  h_TTM1.Draw("SameLE")
  h_TLM1.Draw("SameLE")
  h_LLM1.Draw("SameLE")
  h_AddM1.Draw("SameLE")

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
  leg.AddEntry(h_TTM1Clone1, "TT", "F")
  leg.AddEntry(h_TLM1Clone1, "TL", "F")
  leg.AddEntry(h_LLM1Clone1, "LL", "F")
  leg.AddEntry(h_M1,"Inclusive","LE")
  leg.AddEntry(h_TTM1,"TT","LE")
  leg.AddEntry(h_TLM1,"TL","LE")
  leg.AddEntry(h_LLM1,"LL","LE")
  leg.AddEntry(h_AddM1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_M1Divide.Draw("LE")
  h_TTM1Divide.Draw("SameLE")
  h_TLM1Divide.Draw("SameLE")
  h_LLM1Divide.Draw("SameLE")
  h_AddM1Divide.Draw("SameLE")
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
  h_M1Clone2.Draw("LE")
  h_TTM1Clone2.Draw("SameLE")
  h_TLM1Clone2.Draw("SameLE")
  h_LLM1Clone2.Draw("SameLE")
  h_AddM1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_M1DivideShape.Draw("LE")
  h_TTM1DivideShape.Draw("SameLE")
  h_TLM1DivideShape.Draw("SameLE")
  h_LLM1DivideShape.Draw("SameLE")
  h_AddM1DivideShape.Draw("SameLE")
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
  h_M2.Draw("SameLE")
  h_TTM2.Draw("SameLE")
  h_TLM2.Draw("SameLE")
  h_LLM2.Draw("SameLE")
  h_AddM2.Draw("SameLE")

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
  leg.AddEntry(h_TTM2Clone1, "TT", "F")
  leg.AddEntry(h_TLM2Clone1, "TL", "F")
  leg.AddEntry(h_LLM2Clone1, "LL", "F")
  leg.AddEntry(h_M2,"Inclusive","LE")
  leg.AddEntry(h_TTM2,"TT","LE")
  leg.AddEntry(h_TLM2,"TL","LE")
  leg.AddEntry(h_LLM2,"LL","LE")
  leg.AddEntry(h_AddM2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_M2Divide.Draw("LE")
  h_TTM2Divide.Draw("SameLE")
  h_TLM2Divide.Draw("SameLE")
  h_LLM2Divide.Draw("SameLE")
  h_AddM2Divide.Draw("SameLE")
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
  h_M2Clone2.Draw("LE")
  h_TTM2Clone2.Draw("SameLE")
  h_TLM2Clone2.Draw("SameLE")
  h_LLM2Clone2.Draw("SameLE")
  h_AddM2Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_M2DivideShape.Draw("LE")
  h_TTM2DivideShape.Draw("SameLE")
  h_TLM2DivideShape.Draw("SameLE")
  h_LLM2DivideShape.Draw("SameLE")
  h_AddM2DivideShape.Draw("SameLE")
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
  h_CosTheta1.Draw("SameLE")
  h_TTCosTheta1.Draw("SameLE")
  h_TLCosTheta1.Draw("SameLE")
  h_LLCosTheta1.Draw("SameLE")
  h_AddCosTheta1.Draw("SameLE")

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
  leg.AddEntry(h_TTCosTheta1Clone1, "TT", "F")
  leg.AddEntry(h_TLCosTheta1Clone1, "TL", "F")
  leg.AddEntry(h_LLCosTheta1Clone1, "LL", "F")
  leg.AddEntry(h_CosTheta1,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta1,"TT","LE")
  leg.AddEntry(h_TLCosTheta1,"TL","LE")
  leg.AddEntry(h_LLCosTheta1,"LL","LE")
  leg.AddEntry(h_AddCosTheta1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosTheta1Divide.Draw("LE")
  h_TTCosTheta1Divide.Draw("SameLE")
  h_TLCosTheta1Divide.Draw("SameLE")
  h_LLCosTheta1Divide.Draw("SameLE")
  h_AddCosTheta1Divide.Draw("SameLE")
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
  h_CosTheta1Clone2.Draw("LE")
  h_TTCosTheta1Clone2.Draw("SameLE")
  h_TLCosTheta1Clone2.Draw("SameLE")
  h_LLCosTheta1Clone2.Draw("SameLE")
  h_AddCosTheta1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosTheta1DivideShape.Draw("LE")
  h_TTCosTheta1DivideShape.Draw("SameLE")
  h_TLCosTheta1DivideShape.Draw("SameLE")
  h_LLCosTheta1DivideShape.Draw("SameLE")
  h_AddCosTheta1DivideShape.Draw("SameLE")
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
  h_CosTheta2.Draw("SameLE")
  h_TTCosTheta2.Draw("SameLE")
  h_TLCosTheta2.Draw("SameLE")
  h_LLCosTheta2.Draw("SameLE")
  h_AddCosTheta2.Draw("SameLE")

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
  leg.AddEntry(h_TTCosTheta2Clone1, "TT", "F")
  leg.AddEntry(h_TLCosTheta2Clone1, "TL", "F")
  leg.AddEntry(h_LLCosTheta2Clone1, "LL", "F")
  leg.AddEntry(h_CosTheta2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta2,"TT","LE")
  leg.AddEntry(h_TLCosTheta2,"TL","LE")
  leg.AddEntry(h_LLCosTheta2,"LL","LE")
  leg.AddEntry(h_AddCosTheta2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosTheta2Divide.Draw("LE")
  h_TTCosTheta2Divide.Draw("SameLE")
  h_TLCosTheta2Divide.Draw("SameLE")
  h_LLCosTheta2Divide.Draw("SameLE")
  h_AddCosTheta2Divide.Draw("SameLE")
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
  h_CosTheta2Clone2.Draw("LE")
  h_TTCosTheta2Clone2.Draw("SameLE")
  h_TLCosTheta2Clone2.Draw("SameLE")
  h_LLCosTheta2Clone2.Draw("SameLE")
  h_AddCosTheta2Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosTheta2DivideShape.Draw("LE")
  h_TTCosTheta2DivideShape.Draw("SameLE")
  h_TLCosTheta2DivideShape.Draw("SameLE")
  h_LLCosTheta2DivideShape.Draw("SameLE")
  h_AddCosTheta2DivideShape.Draw("SameLE")
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
  histogram of CosTheta3, TTCosTheta3, TLCosTheta3, LLCosTheta3, TT+TL+LLCosTheta3
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta3Sum = R.TCanvas("c_CosTheta3Sum", "CosTheta3Sum", 800, 1000)
  # set the background of this canvas
  c_CosTheta3Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosTheta3.Draw("Hist")
  h_CosTheta3.Draw("SameLE")
  h_TTCosTheta3.Draw("SameLE")
  h_TLCosTheta3.Draw("SameLE")
  h_LLCosTheta3.Draw("SameLE")
  h_AddCosTheta3.Draw("SameLE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosTheta3Clone1.SetFillColor(2)
  h_TLCosTheta3Clone1.SetFillColor(3)
  h_TTCosTheta3Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosTheta3.SetLineColor(1)
  h_TTCosTheta3.SetLineColor(7)
  h_TLCosTheta3.SetLineColor(11)
  h_LLCosTheta3.SetLineColor(5)
  h_AddCosTheta3.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta3.SetLineWidth(3)
  h_TTCosTheta3.SetLineWidth(3)
  h_TLCosTheta3.SetLineWidth(3)
  h_LLCosTheta3.SetLineWidth(3)
  h_AddCosTheta3.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosTheta3.GetXaxis().SetLabelFont(63)
  hs_CosTheta3.GetXaxis().SetLabelSize(16)
  hs_CosTheta3.GetYaxis().SetLabelFont(63)
  hs_CosTheta3.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosTheta3.GetYaxis().SetTitle("Events")
  hs_CosTheta3.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosTheta3.SetMaximum(int(hs_CosTheta3.GetMaximum())*1.2)

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
  leg.AddEntry(h_TTCosTheta3Clone1, "TT", "F")
  leg.AddEntry(h_TLCosTheta3Clone1, "TL", "F")
  leg.AddEntry(h_LLCosTheta3Clone1, "LL", "F")
  leg.AddEntry(h_CosTheta3,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta3,"TT","LE")
  leg.AddEntry(h_TLCosTheta3,"TL","LE")
  leg.AddEntry(h_LLCosTheta3,"LL","LE")
  leg.AddEntry(h_AddCosTheta3,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta3Sum.cd()


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
  h_CosTheta3Divide.Divide(h_CosTheta3, h_AddCosTheta3, 1, 1)
  h_TTCosTheta3Divide.Divide(h_TTCosTheta3, h_AddCosTheta3, 1, 1)
  h_TLCosTheta3Divide.Divide(h_TLCosTheta3, h_AddCosTheta3, 1, 1)
  h_LLCosTheta3Divide.Divide(h_LLCosTheta3, h_AddCosTheta3, 1, 1)
  h_AddCosTheta3Divide.Divide(h_AddCosTheta3, h_AddCosTheta3, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta3Divide.Draw("LE")
  h_TTCosTheta3Divide.Draw("SameLE")
  h_TLCosTheta3Divide.Draw("SameLE")
  h_LLCosTheta3Divide.Draw("SameLE")
  h_AddCosTheta3Divide.Draw("SameLE")
  # set the color of each histogram
  h_CosTheta3Divide.SetLineColor(1)
  h_TTCosTheta3Divide.SetLineColor(7)
  h_TLCosTheta3Divide.SetLineColor(11)
  h_LLCosTheta3Divide.SetLineColor(5)
  h_AddCosTheta3Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta3Divide.SetLineWidth(3)
  h_TTCosTheta3Divide.SetLineWidth(3)
  h_TLCosTheta3Divide.SetLineWidth(3)
  h_LLCosTheta3Divide.SetLineWidth(3)
  h_AddCosTheta3Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta3Divide.GetXaxis().SetLabelFont(63)
  h_CosTheta3Divide.GetXaxis().SetLabelSize(16)
  h_CosTheta3Divide.GetYaxis().SetLabelFont(63)
  h_CosTheta3Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta3Divide.GetXaxis().SetTitle("CosTheta3")
  h_CosTheta3Divide.GetXaxis().SetTitleSize(0.07)
  h_CosTheta3Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta3Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta3Divide.GetMaximum()
  Max2 = h_TTCosTheta3Divide.GetMaximum()
  Max3 = h_TLCosTheta3Divide.GetMaximum()
  Max4 = h_LLCosTheta3Divide.GetMaximum()
  Max5 = h_AddCosTheta3Divide.GetMaximum()
  Min1 = h_CosTheta3Divide.GetMinimum()
  Min2 = h_TTCosTheta3Divide.GetMinimum()
  Min3 = h_TLCosTheta3Divide.GetMinimum()
  Min4 = h_LLCosTheta3Divide.GetMinimum()
  Min5 = h_AddCosTheta3Divide.GetMinimum()
  h_CosTheta3Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta3Sum.cd()

  # save the canvas as png file
  c_CosTheta3Sum.SaveAs("CosTheta3Sum.png")
  # close the canvas
  c_CosTheta3Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta3SumShape = R.TCanvas("c_CosTheta3SumShape", "CosTheta3SumShape", 800, 1000)
  # set the background of this canvas
  c_CosTheta3SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosTheta3Clone2.Draw("LE")
  h_TTCosTheta3Clone2.Draw("SameLE")
  h_TLCosTheta3Clone2.Draw("SameLE")
  h_LLCosTheta3Clone2.Draw("SameLE")
  h_AddCosTheta3Clone2.Draw("SameLE")

  # set the line color of each histogram
  h_CosTheta3Clone2.SetLineColor(1)
  h_TTCosTheta3Clone2.SetLineColor(7)
  h_TLCosTheta3Clone2.SetLineColor(11)
  h_LLCosTheta3Clone2.SetLineColor(5)
  h_AddCosTheta3Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta3Clone2.SetLineWidth(3)
  h_TTCosTheta3Clone2.SetLineWidth(3)
  h_TLCosTheta3Clone2.SetLineWidth(3)
  h_LLCosTheta3Clone2.SetLineWidth(3)
  h_AddCosTheta3Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosTheta3Clone2.GetXaxis().SetLabelFont(63)
  h_CosTheta3Clone2.GetXaxis().SetLabelSize(16)
  h_CosTheta3Clone2.GetYaxis().SetLabelFont(63)
  h_CosTheta3Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosTheta3Clone2.GetYaxis().SetTitle("freq.")
  h_CosTheta3Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosTheta3Clone2.GetMaximum()
  Max2 = h_TTCosTheta3Clone2.GetMaximum()
  Max3 = h_TLCosTheta3Clone2.GetMaximum()
  Max4 = h_LLCosTheta3Clone2.GetMaximum()
  Max5 = h_AddCosTheta3Clone2.GetMaximum()
  h_CosTheta3Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

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
  leg.AddEntry(h_CosTheta3Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta3Clone2,"TT","LE")
  leg.AddEntry(h_TLCosTheta3Clone2,"TL","LE")
  leg.AddEntry(h_LLCosTheta3Clone2,"LL","LE")
  leg.AddEntry(h_AddCosTheta3Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta3SumShape.cd()


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
  h_CosTheta3DivideShape.Divide(h_CosTheta3Clone2, h_AddCosTheta3Clone2, 1, 1)
  h_TTCosTheta3DivideShape.Divide(h_TTCosTheta3Clone2, h_AddCosTheta3Clone2, 1, 1)
  h_TLCosTheta3DivideShape.Divide(h_TLCosTheta3Clone2, h_AddCosTheta3Clone2, 1, 1)
  h_LLCosTheta3DivideShape.Divide(h_LLCosTheta3Clone2, h_AddCosTheta3Clone2, 1, 1)
  h_AddCosTheta3DivideShape.Divide(h_AddCosTheta3Clone2, h_AddCosTheta3Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta3DivideShape.Draw("LE")
  h_TTCosTheta3DivideShape.Draw("SameLE")
  h_TLCosTheta3DivideShape.Draw("SameLE")
  h_LLCosTheta3DivideShape.Draw("SameLE")
  h_AddCosTheta3DivideShape.Draw("SameLE")
  # set the color of each histogram
  h_CosTheta3DivideShape.SetLineColor(1)
  h_TTCosTheta3DivideShape.SetLineColor(7)
  h_TLCosTheta3DivideShape.SetLineColor(11)
  h_LLCosTheta3DivideShape.SetLineColor(5)
  h_AddCosTheta3DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta3DivideShape.SetLineWidth(3)
  h_TTCosTheta3DivideShape.SetLineWidth(3)
  h_TLCosTheta3DivideShape.SetLineWidth(3)
  h_LLCosTheta3DivideShape.SetLineWidth(3)
  h_AddCosTheta3DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta3DivideShape.GetXaxis().SetLabelFont(63)
  h_CosTheta3DivideShape.GetXaxis().SetLabelSize(16)
  h_CosTheta3DivideShape.GetYaxis().SetLabelFont(63)
  h_CosTheta3DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta3DivideShape.GetXaxis().SetTitle("CosTheta3")
  h_CosTheta3DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosTheta3DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta3DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta3DivideShape.GetMaximum()
  Max2 = h_TTCosTheta3DivideShape.GetMaximum()
  Max3 = h_TLCosTheta3DivideShape.GetMaximum()
  Max4 = h_LLCosTheta3DivideShape.GetMaximum()
  Max5 = h_AddCosTheta3DivideShape.GetMaximum()
  Min1 = h_CosTheta3DivideShape.GetMinimum()
  Min2 = h_TTCosTheta3DivideShape.GetMinimum()
  Min3 = h_TLCosTheta3DivideShape.GetMinimum()
  Min4 = h_LLCosTheta3DivideShape.GetMinimum()
  Min5 = h_AddCosTheta3DivideShape.GetMinimum()
  h_CosTheta3DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta3SumShape.cd()


  # save the canvas as png file
  c_CosTheta3SumShape.SaveAs("CosTheta3ShapeOnly.png")
  # close the canvas
  c_CosTheta3SumShape.Close()



  """
  histogram of CosTheta4, TTCosTheta4, TLCosTheta4, LLCosTheta4, TT+TL+LLCosTheta4
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta4Sum = R.TCanvas("c_CosTheta4Sum", "CosTheta4Sum", 800, 1000)
  # set the background of this canvas
  c_CosTheta4Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  hs_CosTheta4.Draw("Hist")
  h_CosTheta4.Draw("SameLE")
  h_TTCosTheta4.Draw("SameLE")
  h_TLCosTheta4.Draw("SameLE")
  h_LLCosTheta4.Draw("SameLE")
  h_AddCosTheta4.Draw("SameLE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLCosTheta4Clone1.SetFillColor(2)
  h_TLCosTheta4Clone1.SetFillColor(3)
  h_TTCosTheta4Clone1.SetFillColor(9)

  # set the line color of each histogram
  h_CosTheta4.SetLineColor(1)
  h_TTCosTheta4.SetLineColor(7)
  h_TLCosTheta4.SetLineColor(11)
  h_LLCosTheta4.SetLineColor(5)
  h_AddCosTheta4.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta4.SetLineWidth(3)
  h_TTCosTheta4.SetLineWidth(3)
  h_TLCosTheta4.SetLineWidth(3)
  h_LLCosTheta4.SetLineWidth(3)
  h_AddCosTheta4.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_CosTheta4.GetXaxis().SetLabelFont(63)
  hs_CosTheta4.GetXaxis().SetLabelSize(16)
  hs_CosTheta4.GetYaxis().SetLabelFont(63)
  hs_CosTheta4.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_CosTheta4.GetYaxis().SetTitle("Events")
  hs_CosTheta4.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_M1.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_CosTheta4.SetMaximum(int(hs_CosTheta4.GetMaximum())*1.2)

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
  leg.AddEntry(h_TTCosTheta4Clone1, "TT", "F")
  leg.AddEntry(h_TLCosTheta4Clone1, "TL", "F")
  leg.AddEntry(h_LLCosTheta4Clone1, "LL", "F")
  leg.AddEntry(h_CosTheta4,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta4,"TT","LE")
  leg.AddEntry(h_TLCosTheta4,"TL","LE")
  leg.AddEntry(h_LLCosTheta4,"LL","LE")
  leg.AddEntry(h_AddCosTheta4,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta4Sum.cd()


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
  h_CosTheta4Divide.Divide(h_CosTheta4, h_AddCosTheta4, 1, 1)
  h_TTCosTheta4Divide.Divide(h_TTCosTheta4, h_AddCosTheta4, 1, 1)
  h_TLCosTheta4Divide.Divide(h_TLCosTheta4, h_AddCosTheta4, 1, 1)
  h_LLCosTheta4Divide.Divide(h_LLCosTheta4, h_AddCosTheta4, 1, 1)
  h_AddCosTheta4Divide.Divide(h_AddCosTheta4, h_AddCosTheta4, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta4Divide.Draw("LE")
  h_TTCosTheta4Divide.Draw("SameLE")
  h_TLCosTheta4Divide.Draw("SameLE")
  h_LLCosTheta4Divide.Draw("SameLE")
  h_AddCosTheta4Divide.Draw("SameLE")
  # set the color of each histogram
  h_CosTheta4Divide.SetLineColor(1)
  h_TTCosTheta4Divide.SetLineColor(7)
  h_TLCosTheta4Divide.SetLineColor(11)
  h_LLCosTheta4Divide.SetLineColor(5)
  h_AddCosTheta4Divide.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta4Divide.SetLineWidth(3)
  h_TTCosTheta4Divide.SetLineWidth(3)
  h_TLCosTheta4Divide.SetLineWidth(3)
  h_LLCosTheta4Divide.SetLineWidth(3)
  h_AddCosTheta4Divide.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta4Divide.GetXaxis().SetLabelFont(63)
  h_CosTheta4Divide.GetXaxis().SetLabelSize(16)
  h_CosTheta4Divide.GetYaxis().SetLabelFont(63)
  h_CosTheta4Divide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta4Divide.GetXaxis().SetTitle("CosTheta4")
  h_CosTheta4Divide.GetXaxis().SetTitleSize(0.07)
  h_CosTheta4Divide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta4Divide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta4Divide.GetMaximum()
  Max2 = h_TTCosTheta4Divide.GetMaximum()
  Max3 = h_TLCosTheta4Divide.GetMaximum()
  Max4 = h_LLCosTheta4Divide.GetMaximum()
  Max5 = h_AddCosTheta4Divide.GetMaximum()
  Min1 = h_CosTheta4Divide.GetMinimum()
  Min2 = h_TTCosTheta4Divide.GetMinimum()
  Min3 = h_TLCosTheta4Divide.GetMinimum()
  Min4 = h_LLCosTheta4Divide.GetMinimum()
  Min5 = h_AddCosTheta4Divide.GetMinimum()
  h_CosTheta4Divide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta4Sum.cd()

  # save the canvas as png file
  c_CosTheta4Sum.SaveAs("CosTheta4Sum.png")
  # close the canvas
  c_CosTheta4Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_CosTheta4SumShape = R.TCanvas("c_CosTheta4SumShape", "CosTheta4SumShape", 800, 1000)
  # set the background of this canvas
  c_CosTheta4SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_CosTheta4Clone2.Draw("LE")
  h_TTCosTheta4Clone2.Draw("SameLE")
  h_TLCosTheta4Clone2.Draw("SameLE")
  h_LLCosTheta4Clone2.Draw("SameLE")
  h_AddCosTheta4Clone2.Draw("SameLE")

  # set the line color of each histogram
  h_CosTheta4Clone2.SetLineColor(1)
  h_TTCosTheta4Clone2.SetLineColor(7)
  h_TLCosTheta4Clone2.SetLineColor(11)
  h_LLCosTheta4Clone2.SetLineColor(5)
  h_AddCosTheta4Clone2.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta4Clone2.SetLineWidth(3)
  h_TTCosTheta4Clone2.SetLineWidth(3)
  h_TLCosTheta4Clone2.SetLineWidth(3)
  h_LLCosTheta4Clone2.SetLineWidth(3)
  h_AddCosTheta4Clone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_CosTheta4Clone2.GetXaxis().SetLabelFont(63)
  h_CosTheta4Clone2.GetXaxis().SetLabelSize(16)
  h_CosTheta4Clone2.GetYaxis().SetLabelFont(63)
  h_CosTheta4Clone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_CosTheta4Clone2.GetYaxis().SetTitle("freq.")
  h_CosTheta4Clone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_CosTheta4Clone2.GetMaximum()
  Max2 = h_TTCosTheta4Clone2.GetMaximum()
  Max3 = h_TLCosTheta4Clone2.GetMaximum()
  Max4 = h_LLCosTheta4Clone2.GetMaximum()
  Max5 = h_AddCosTheta4Clone2.GetMaximum()
  h_CosTheta4Clone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

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
  leg.AddEntry(h_CosTheta4Clone2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta4Clone2,"TT","LE")
  leg.AddEntry(h_TLCosTheta4Clone2,"TL","LE")
  leg.AddEntry(h_LLCosTheta4Clone2,"LL","LE")
  leg.AddEntry(h_AddCosTheta4Clone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_CosTheta4SumShape.cd()


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
  h_CosTheta4DivideShape.Divide(h_CosTheta4Clone2, h_AddCosTheta4Clone2, 1, 1)
  h_TTCosTheta4DivideShape.Divide(h_TTCosTheta4Clone2, h_AddCosTheta4Clone2, 1, 1)
  h_TLCosTheta4DivideShape.Divide(h_TLCosTheta4Clone2, h_AddCosTheta4Clone2, 1, 1)
  h_LLCosTheta4DivideShape.Divide(h_LLCosTheta4Clone2, h_AddCosTheta4Clone2, 1, 1)
  h_AddCosTheta4DivideShape.Divide(h_AddCosTheta4Clone2, h_AddCosTheta4Clone2, 1 ,1)

  # draw the histograms of ratio
  h_CosTheta4DivideShape.Draw("LE")
  h_TTCosTheta4DivideShape.Draw("SameLE")
  h_TLCosTheta4DivideShape.Draw("SameLE")
  h_LLCosTheta4DivideShape.Draw("SameLE")
  h_AddCosTheta4DivideShape.Draw("SameLE")
  # set the color of each histogram
  h_CosTheta4DivideShape.SetLineColor(1)
  h_TTCosTheta4DivideShape.SetLineColor(7)
  h_TLCosTheta4DivideShape.SetLineColor(11)
  h_LLCosTheta4DivideShape.SetLineColor(5)
  h_AddCosTheta4DivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_CosTheta4DivideShape.SetLineWidth(3)
  h_TTCosTheta4DivideShape.SetLineWidth(3)
  h_TLCosTheta4DivideShape.SetLineWidth(3)
  h_LLCosTheta4DivideShape.SetLineWidth(3)
  h_AddCosTheta4DivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_CosTheta4DivideShape.GetXaxis().SetLabelFont(63)
  h_CosTheta4DivideShape.GetXaxis().SetLabelSize(16)
  h_CosTheta4DivideShape.GetYaxis().SetLabelFont(63)
  h_CosTheta4DivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_CosTheta4DivideShape.GetXaxis().SetTitle("CosTheta4")
  h_CosTheta4DivideShape.GetXaxis().SetTitleSize(0.07)
  h_CosTheta4DivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_CosTheta4DivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_CosTheta4DivideShape.GetMaximum()
  Max2 = h_TTCosTheta4DivideShape.GetMaximum()
  Max3 = h_TLCosTheta4DivideShape.GetMaximum()
  Max4 = h_LLCosTheta4DivideShape.GetMaximum()
  Max5 = h_AddCosTheta4DivideShape.GetMaximum()
  Min1 = h_CosTheta4DivideShape.GetMinimum()
  Min2 = h_TTCosTheta4DivideShape.GetMinimum()
  Min3 = h_TLCosTheta4DivideShape.GetMinimum()
  Min4 = h_LLCosTheta4DivideShape.GetMinimum()
  Min5 = h_AddCosTheta4DivideShape.GetMinimum()
  h_CosTheta4DivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4, Min5)*0.5, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_CosTheta4SumShape.cd()


  # save the canvas as png file
  c_CosTheta4SumShape.SaveAs("CosTheta4ShapeOnly.png")
  # close the canvas
  c_CosTheta4SumShape.Close()



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
  h_ThetaStar1.Draw("SameLE")
  h_TTThetaStar1.Draw("SameLE")
  h_TLThetaStar1.Draw("SameLE")
  h_LLThetaStar1.Draw("SameLE")
  h_AddThetaStar1.Draw("SameLE")

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
  leg.AddEntry(h_TTThetaStar1Clone1, "TT", "F")
  leg.AddEntry(h_TLThetaStar1Clone1, "TL", "F")
  leg.AddEntry(h_LLThetaStar1Clone1, "LL", "F")
  leg.AddEntry(h_ThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar1,"TT","LE")
  leg.AddEntry(h_TLThetaStar1,"TL","LE")
  leg.AddEntry(h_LLThetaStar1,"LL","LE")
  leg.AddEntry(h_AddThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_ThetaStar1Divide.Draw("LE")
  h_TTThetaStar1Divide.Draw("SameLE")
  h_TLThetaStar1Divide.Draw("SameLE")
  h_LLThetaStar1Divide.Draw("SameLE")
  h_AddThetaStar1Divide.Draw("SameLE")
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
  h_ThetaStar1Clone2.Draw("LE")
  h_TTThetaStar1Clone2.Draw("SameLE")
  h_TLThetaStar1Clone2.Draw("SameLE")
  h_LLThetaStar1Clone2.Draw("SameLE")
  h_AddThetaStar1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_ThetaStar1DivideShape.Draw("LE")
  h_TTThetaStar1DivideShape.Draw("SameLE")
  h_TLThetaStar1DivideShape.Draw("SameLE")
  h_LLThetaStar1DivideShape.Draw("SameLE")
  h_AddThetaStar1DivideShape.Draw("SameLE")
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
  h_ThetaStar2.Draw("SameLE")
  h_TTThetaStar2.Draw("SameLE")
  h_TLThetaStar2.Draw("SameLE")
  h_LLThetaStar2.Draw("SameLE")
  h_AddThetaStar2.Draw("SameLE")

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
  leg.AddEntry(h_TTThetaStar2Clone1, "TT", "F")
  leg.AddEntry(h_TLThetaStar2Clone1, "TL", "F")
  leg.AddEntry(h_LLThetaStar2Clone1, "LL", "F")
  leg.AddEntry(h_ThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar2,"TT","LE")
  leg.AddEntry(h_TLThetaStar2,"TL","LE")
  leg.AddEntry(h_LLThetaStar2,"LL","LE")
  leg.AddEntry(h_AddThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_ThetaStar2Divide.Draw("LE")
  h_TTThetaStar2Divide.Draw("SameLE")
  h_TLThetaStar2Divide.Draw("SameLE")
  h_LLThetaStar2Divide.Draw("SameLE")
  h_AddThetaStar2Divide.Draw("SameLE")
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
  h_ThetaStar2Clone2.Draw("LE")
  h_TTThetaStar2Clone2.Draw("SameLE")
  h_TLThetaStar2Clone2.Draw("SameLE")
  h_LLThetaStar2Clone2.Draw("SameLE")
  h_AddThetaStar2Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_ThetaStar2DivideShape.Draw("LE")
  h_TTThetaStar2DivideShape.Draw("SameLE")
  h_TLThetaStar2DivideShape.Draw("SameLE")
  h_LLThetaStar2DivideShape.Draw("SameLE")
  h_AddThetaStar2DivideShape.Draw("SameLE")
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
  h_CosThetaStar1.Draw("SameLE")
  h_TTCosThetaStar1.Draw("SameLE")
  h_TLCosThetaStar1.Draw("SameLE")
  h_LLCosThetaStar1.Draw("SameLE")
  h_AddCosThetaStar1.Draw("SameLE")

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
  leg.AddEntry(h_TTCosThetaStar1Clone1, "TT", "F")
  leg.AddEntry(h_TLCosThetaStar1Clone1, "TL", "F")
  leg.AddEntry(h_LLCosThetaStar1Clone1, "LL", "F")
  leg.AddEntry(h_CosThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar1,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar1,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar1,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosThetaStar1Divide.Draw("LE")
  h_TTCosThetaStar1Divide.Draw("SameLE")
  h_TLCosThetaStar1Divide.Draw("SameLE")
  h_LLCosThetaStar1Divide.Draw("SameLE")
  h_AddCosThetaStar1Divide.Draw("SameLE")
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
  h_CosThetaStar1Clone2.Draw("LE")
  h_TTCosThetaStar1Clone2.Draw("SameLE")
  h_TLCosThetaStar1Clone2.Draw("SameLE")
  h_LLCosThetaStar1Clone2.Draw("SameLE")
  h_AddCosThetaStar1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosThetaStar1DivideShape.Draw("LE")
  h_TTCosThetaStar1DivideShape.Draw("SameLE")
  h_TLCosThetaStar1DivideShape.Draw("SameLE")
  h_LLCosThetaStar1DivideShape.Draw("SameLE")
  h_AddCosThetaStar1DivideShape.Draw("SameLE")
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
  h_CosThetaStar2.Draw("SameLE")
  h_TTCosThetaStar2.Draw("SameLE")
  h_TLCosThetaStar2.Draw("SameLE")
  h_LLCosThetaStar2.Draw("SameLE")
  h_AddCosThetaStar2.Draw("SameLE")

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
  leg.AddEntry(h_TTCosThetaStar2Clone1, "TT", "F")
  leg.AddEntry(h_TLCosThetaStar2Clone1, "TL", "F")
  leg.AddEntry(h_LLCosThetaStar2Clone1, "LL", "F")
  leg.AddEntry(h_CosThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar2,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosThetaStar2Divide.Draw("LE")
  h_TTCosThetaStar2Divide.Draw("SameLE")
  h_TLCosThetaStar2Divide.Draw("SameLE")
  h_LLCosThetaStar2Divide.Draw("SameLE")
  h_AddCosThetaStar2Divide.Draw("SameLE")
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
  h_CosThetaStar2Clone2.Draw("LE")
  h_TTCosThetaStar2Clone2.Draw("SameLE")
  h_TLCosThetaStar2Clone2.Draw("SameLE")
  h_LLCosThetaStar2Clone2.Draw("SameLE")
  h_AddCosThetaStar2Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosThetaStar2DivideShape.Draw("LE")
  h_TTCosThetaStar2DivideShape.Draw("SameLE")
  h_TLCosThetaStar2DivideShape.Draw("SameLE")
  h_LLCosThetaStar2DivideShape.Draw("SameLE")
  h_AddCosThetaStar2DivideShape.Draw("SameLE")
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
  h_Phi.Draw("SameLE")
  h_TTPhi.Draw("SameLE")
  h_TLPhi.Draw("SameLE")
  h_LLPhi.Draw("SameLE")
  h_AddPhi.Draw("SameLE")

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
  leg.AddEntry(h_TTPhiClone1, "TT", "F")
  leg.AddEntry(h_TLPhiClone1, "TL", "F")
  leg.AddEntry(h_LLPhiClone1, "LL", "F")
  leg.AddEntry(h_Phi,"Inclusive","LE")
  leg.AddEntry(h_TTPhi,"TT","LE")
  leg.AddEntry(h_TLPhi,"TL","LE")
  leg.AddEntry(h_LLPhi,"LL","LE")
  leg.AddEntry(h_AddPhi,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_PhiDivide.Draw("LE")
  h_TTPhiDivide.Draw("SameLE")
  h_TLPhiDivide.Draw("SameLE")
  h_LLPhiDivide.Draw("SameLE")
  h_AddPhiDivide.Draw("SameLE")
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
  h_PhiClone2.Draw("LE")
  h_TTPhiClone2.Draw("SameLE")
  h_TLPhiClone2.Draw("SameLE")
  h_LLPhiClone2.Draw("SameLE")
  h_AddPhiClone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_PhiDivideShape.Draw("LE")
  h_TTPhiDivideShape.Draw("SameLE")
  h_TLPhiDivideShape.Draw("SameLE")
  h_LLPhiDivideShape.Draw("SameLE")
  h_AddPhiDivideShape.Draw("SameLE")
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
  h_CosPhi.Draw("SameLE")
  h_TTCosPhi.Draw("SameLE")
  h_TLCosPhi.Draw("SameLE")
  h_LLCosPhi.Draw("SameLE")
  h_AddCosPhi.Draw("SameLE")

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
  leg.AddEntry(h_TTCosPhiClone1, "TT", "F")
  leg.AddEntry(h_TLCosPhiClone1, "TL", "F")
  leg.AddEntry(h_LLCosPhiClone1, "LL", "F")
  leg.AddEntry(h_CosPhi,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi,"TT","LE")
  leg.AddEntry(h_TLCosPhi,"TL","LE")
  leg.AddEntry(h_LLCosPhi,"LL","LE")
  leg.AddEntry(h_AddCosPhi,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosPhiDivide.Draw("LE")
  h_TTCosPhiDivide.Draw("SameLE")
  h_TLCosPhiDivide.Draw("SameLE")
  h_LLCosPhiDivide.Draw("SameLE")
  h_AddCosPhiDivide.Draw("SameLE")
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
  h_CosPhiClone2.Draw("LE")
  h_TTCosPhiClone2.Draw("SameLE")
  h_TLCosPhiClone2.Draw("SameLE")
  h_LLCosPhiClone2.Draw("SameLE")
  h_AddCosPhiClone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosPhiDivideShape.Draw("LE")
  h_TTCosPhiDivideShape.Draw("SameLE")
  h_TLCosPhiDivideShape.Draw("SameLE")
  h_LLCosPhiDivideShape.Draw("SameLE")
  h_AddCosPhiDivideShape.Draw("SameLE")
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
  h_Phi1.Draw("SameLE")
  h_TTPhi1.Draw("SameLE")
  h_TLPhi1.Draw("SameLE")
  h_LLPhi1.Draw("SameLE")
  h_AddPhi1.Draw("SameLE")

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
  leg.AddEntry(h_TTPhi1Clone1, "TT", "F")
  leg.AddEntry(h_TLPhi1Clone1, "TL", "F")
  leg.AddEntry(h_LLPhi1Clone1, "LL", "F")
  leg.AddEntry(h_Phi1,"Inclusive","LE")
  leg.AddEntry(h_TTPhi1,"TT","LE")
  leg.AddEntry(h_TLPhi1,"TL","LE")
  leg.AddEntry(h_LLPhi1,"LL","LE")
  leg.AddEntry(h_AddPhi1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_Phi1Divide.Draw("LE")
  h_TTPhi1Divide.Draw("SameLE")
  h_TLPhi1Divide.Draw("SameLE")
  h_LLPhi1Divide.Draw("SameLE")
  h_AddPhi1Divide.Draw("SameLE")
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
  h_Phi1Clone2.Draw("LE")
  h_TTPhi1Clone2.Draw("SameLE")
  h_TLPhi1Clone2.Draw("SameLE")
  h_LLPhi1Clone2.Draw("SameLE")
  h_AddPhi1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_Phi1DivideShape.Draw("LE")
  h_TTPhi1DivideShape.Draw("SameLE")
  h_TLPhi1DivideShape.Draw("SameLE")
  h_LLPhi1DivideShape.Draw("SameLE")
  h_AddPhi1DivideShape.Draw("SameLE")
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
  h_CosPhi1.Draw("SameLE")
  h_TTCosPhi1.Draw("SameLE")
  h_TLCosPhi1.Draw("SameLE")
  h_LLCosPhi1.Draw("SameLE")
  h_AddCosPhi1.Draw("SameLE")

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
  leg.AddEntry(h_TTCosPhi1Clone1, "TT", "F")
  leg.AddEntry(h_TLCosPhi1Clone1, "TL", "F")
  leg.AddEntry(h_LLCosPhi1Clone1, "LL", "F")
  leg.AddEntry(h_CosPhi1,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi1,"TT","LE")
  leg.AddEntry(h_TLCosPhi1,"TL","LE")
  leg.AddEntry(h_LLCosPhi1,"LL","LE")
  leg.AddEntry(h_AddCosPhi1,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosPhi1Divide.Draw("LE")
  h_TTCosPhi1Divide.Draw("SameLE")
  h_TLCosPhi1Divide.Draw("SameLE")
  h_LLCosPhi1Divide.Draw("SameLE")
  h_AddCosPhi1Divide.Draw("SameLE")
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
  h_CosPhi1Clone2.Draw("LE")
  h_TTCosPhi1Clone2.Draw("SameLE")
  h_TLCosPhi1Clone2.Draw("SameLE")
  h_LLCosPhi1Clone2.Draw("SameLE")
  h_AddCosPhi1Clone2.Draw("SameLE")

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
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#it{ATLAS}} Internal")
  latex.DrawLatexNDC(0.2, 0.75, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

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
  h_CosPhi1DivideShape.Draw("LE")
  h_TTCosPhi1DivideShape.Draw("SameLE")
  h_TLCosPhi1DivideShape.Draw("SameLE")
  h_LLCosPhi1DivideShape.Draw("SameLE")
  h_AddCosPhi1DivideShape.Draw("SameLE")
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



  # close the ROOTFile
  rootfile.Close()



if __name__ == "__main__":

  InputROOTFile="Angle_v3.root"
  plot(InputROOTFile)















