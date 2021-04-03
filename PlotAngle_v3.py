#!/usr/bin/env python

# import some modules
import sys, os
# import ROOT, creat an alias
import ROOT as R

def plot(InputROOTFile):

  rootfile=R.TFile.Open(InputROOTFile)

  # loop all objects of the root file
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
  Plotting
  """

  # remove the Standard Deviation at upper right corner in each histogram
  R.gStyle.SetOptStat(0)


  # histogram of M1
  c_M1 = R.TCanvas()
  c_M1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_M1.SetFillColor(0)
  h_M1.Draw("LE")

  # renormalize the histogram, the cross section of inclusive event is 0.02419pb, ATLAS luminosity is 139 fb-1
  h_M1.Scale(0.02419*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_M1.SetLineColor(2)

  # Since the range of bin is smaller than the whole distribution, it's necessary to add the overflow and underflow in the 1st bin and last bin.
  h_M1.SetBinContent(1, h_M1.GetBinContent(0)+h_M1.GetBinContent(1))
  h_M1.SetBinContent(40, h_M1.GetBinContent(40)+h_M1.GetBinContent(41))

  # save the histogram as png
  c_M1.SaveAs("M1.png")
  # close the Canvas
  c_M1.Close()

  # histogram of M2
  c_M2 = R.TCanvas()
  c_M2.cd()
  c_M2.SetFillColor(0)
  h_M2.Draw("LE")
  h_M2.Scale(0.02419*139*1000/20000)
  h_M2.SetLineColor(2)
  h_M2.SetBinContent(1, h_M2.GetBinContent(0)+h_M2.GetBinContent(1))
  h_M2.SetBinContent(40, h_M2.GetBinContent(40)+h_M2.GetBinContent(41))
  c_M2.SaveAs("M2.png")
  c_M2.Close()

  # histogram of M1MOTHUP
  c_M1MOTHUP = R.TCanvas()
  c_M1MOTHUP.cd()
  c_M1MOTHUP.SetFillColor(0)
  h_M1MOTHUP.Draw("LE")
  h_M1MOTHUP.Scale(0.02419*139*1000/20000)
  h_M1MOTHUP.SetLineColor(2)
  h_M1MOTHUP.SetBinContent(1, h_M1MOTHUP.GetBinContent(0)+h_M1MOTHUP.GetBinContent(1))
  h_M1MOTHUP.SetBinContent(40, h_M1MOTHUP.GetBinContent(40)+h_M1MOTHUP.GetBinContent(41))
  c_M1MOTHUP.SaveAs("M1MOTHUP.png")
  c_M1MOTHUP.Close()

  # histogram of M2MOTHUP
  c_M2MOTHUP = R.TCanvas()
  c_M2MOTHUP.cd()
  c_M2MOTHUP.SetFillColor(0)
  h_M2MOTHUP.Draw("LE")
  h_M2MOTHUP.Scale(0.02419*139*1000/20000)
  h_M2MOTHUP.SetLineColor(2)
  h_M2MOTHUP.SetBinContent(1, h_M2MOTHUP.GetBinContent(0)+h_M2MOTHUP.GetBinContent(1))
  h_M2MOTHUP.SetBinContent(40, h_M2MOTHUP.GetBinContent(40)+h_M2MOTHUP.GetBinContent(41))
  c_M2MOTHUP.SaveAs("M2MOTHUP.png")
  c_M2MOTHUP.Close()


  # histogram of TTM1
  c_TTM1 = R.TCanvas()
  c_TTM1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_TTM1.SetFillColor(0)
  h_TTM1.Draw("LE")
  # renormalize the histogram, the cross section of TT event is 0.01688pb, ATLAS luminosity is 139 fb-1
  h_TTM1.Scale(0.01688*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_TTM1.SetLineColor(2)

  # Since the range of bin is smaller than the whole distribution, it's necessary to add the overflow and underflow in the 1st bin and last bin.
  h_TTM1.SetBinContent(1, h_TTM1.GetBinContent(0)+h_TTM1.GetBinContent(1))
  h_TTM1.SetBinContent(40, h_TTM1.GetBinContent(40)+h_TTM1.GetBinContent(41))

  # save the histogram as png
  c_TTM1.SaveAs("TTM1.png")
  # close the Canvas
  c_TTM1.Close()

  # histogram of TTM2
  c_TTM2 = R.TCanvas()
  c_TTM2.cd()
  c_TTM2.SetFillColor(0)
  h_TTM2.Draw("LE")
  h_TTM2.Scale(0.01688*139*1000/20000)
  h_TTM2.SetLineColor(2)
  h_TTM2.SetBinContent(1, h_TTM2.GetBinContent(0)+h_TTM2.GetBinContent(1))
  h_TTM2.SetBinContent(40, h_TTM2.GetBinContent(40)+h_TTM2.GetBinContent(41))
  c_TTM2.SaveAs("TTM2.png")
  c_TTM2.Close()

  # histogram of TLM1
  c_TLM1 = R.TCanvas()
  c_TLM1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_TLM1.SetFillColor(0)
  h_TLM1.Draw("LE")
  # renormalize the histogram, the cross section of TL event is 0.005741pb, ATLAS luminosity is 139 fb-1
  h_TLM1.Scale(0.005741*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_TLM1.SetLineColor(2)

  # Since the range of bin is smaller than the whole distribution, it's necessary to add the overflow and underflow in the 1st bin and last bin.
  h_TLM1.SetBinContent(1, h_TLM1.GetBinContent(0)+h_TLM1.GetBinContent(1))
  h_TLM1.SetBinContent(40, h_TLM1.GetBinContent(40)+h_TLM1.GetBinContent(41))

  # save the histogram as png
  c_TLM1.SaveAs("TLM1.png")
  # close the Canvas
  c_TLM1.Close()

  # histogram of TLM2
  c_TLM2 = R.TCanvas()
  c_TLM2.cd()
  c_TLM2.SetFillColor(0)
  h_TLM2.Draw("LE")
  h_TLM2.Scale(0.005741*139*1000/20000)
  h_TLM2.SetLineColor(2)
  h_TLM2.SetBinContent(1, h_TLM2.GetBinContent(0)+h_TLM2.GetBinContent(1))
  h_TLM2.SetBinContent(40, h_TLM2.GetBinContent(40)+h_TLM2.GetBinContent(41))
  c_TLM2.SaveAs("TLM2.png")
  c_TLM2.Close()

  # histogram of LLM1
  c_LLM1 = R.TCanvas()
  c_LLM1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_LLM1.SetFillColor(0)
  h_LLM1.Draw("LE")
  # renormalize the histogram, the cross section of LL event is 0.001406pb, ATLAS luminosity is 139 fb-1
  h_LLM1.Scale(0.001406*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_LLM1.SetLineColor(2)

  # Since the range of bin is smaller than the whole distribution, it's necessary to add the overflow and underflow in the 1st bin and last bin.
  h_LLM1.SetBinContent(1, h_LLM1.GetBinContent(0)+h_LLM1.GetBinContent(1))
  h_LLM1.SetBinContent(40, h_LLM1.GetBinContent(40)+h_LLM1.GetBinContent(41))

  # save the histogram as png
  c_LLM1.SaveAs("LLM1.png")
  # close the Canvas
  c_LLM1.Close()

  # histogram of LLM2
  c_LLM2 = R.TCanvas()
  c_LLM2.cd()
  c_LLM2.SetFillColor(0)
  h_LLM2.Draw("LE")
  h_LLM2.Scale(0.001406*139*1000/20000)
  h_LLM2.SetLineColor(2)
  h_LLM2.SetBinContent(1, h_LLM2.GetBinContent(0)+h_LLM2.GetBinContent(1))
  h_LLM2.SetBinContent(40, h_LLM2.GetBinContent(40)+h_LLM2.GetBinContent(41))
  c_LLM2.SaveAs("LLM2.png")
  c_LLM2.Close()


  # histogram of CosTheta1
  c_CosTheta1 = R.TCanvas()
  c_CosTheta1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_CosTheta1.SetFillColor(0)
  h_CosTheta1.Draw("LE")
  # renormalize the histogram, the cross section of inclusive event is 0.02419pb, ATLAS luminosity is 139 fb-1
  h_CosTheta1.Scale(0.02419*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_CosTheta1.SetLineColor(2)
  # save the histogram as png
  c_CosTheta1.SaveAs("CosTheta1.png")

  # histogram of CosTheta2
  c_CosTheta2 = R.TCanvas()
  c_CosTheta2.cd()
  c_CosTheta2.SetFillColor(0)
  h_CosTheta2.Draw("LE")
  h_CosTheta2.Scale(0.02419*139*1000/20000)
  h_CosTheta2.SetLineColor(2)
  c_CosTheta2.SaveAs("CosTheta2.png")

  # histogram of CosTheta3
  c_CosTheta3 = R.TCanvas()
  c_CosTheta3.cd()
  c_CosTheta3.SetFillColor(0)
  h_CosTheta3.Draw("LE")
  h_CosTheta3.Scale(0.02419*139*1000/20000)
  h_CosTheta3.SetLineColor(2)
  c_CosTheta3.SaveAs("CosTheta3.png")

  # histogram of CosTheta4
  c_CosTheta4 = R.TCanvas()
  c_CosTheta4.cd()
  c_CosTheta4.SetFillColor(0)
  h_CosTheta4.Draw("LE")
  h_CosTheta4.Scale(0.02419*139*1000/20000)
  h_CosTheta4.SetLineColor(2)
  c_CosTheta4.SaveAs("CosTheta4.png")


  # histogram of TTCosTheta1
  c_TTCosTheta1 = R.TCanvas()
  c_TTCosTheta1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_TTCosTheta1.SetFillColor(0)
  h_TTCosTheta1.Draw("LE")
  # renormalize the histogram, the cross section of TT event is 0.01688pb, ATLAS luminosity is 139 fb-1
  h_TTCosTheta1.Scale(0.01688*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_TTCosTheta1.SetLineColor(2)
  # save the histogram as png
  c_TTCosTheta1.SaveAs("TTCosTheta1.png")

  # histogram of TTCosTheta2
  c_TTCosTheta2 = R.TCanvas()
  c_TTCosTheta2.cd()
  c_TTCosTheta2.SetFillColor(0)
  h_TTCosTheta2.Draw("LE")
  h_TTCosTheta2.Scale(0.01688*139*1000/20000)
  h_TTCosTheta2.SetLineColor(2)
  c_TTCosTheta2.SaveAs("TTCosTheta2.png")

  # histogram of TTCosTheta3
  c_TTCosTheta3 = R.TCanvas()
  c_TTCosTheta3.cd()
  c_TTCosTheta3.SetFillColor(0)
  h_TTCosTheta3.Draw("LE")
  h_TTCosTheta3.Scale(0.01688*139*1000/20000)
  h_TTCosTheta3.SetLineColor(2)
  c_TTCosTheta3.SaveAs("TTCosTheta3.png")

  # histogram of TTCosTheta4
  c_TTCosTheta4 = R.TCanvas()
  c_TTCosTheta4.cd()
  c_TTCosTheta4.SetFillColor(0)
  h_TTCosTheta4.Draw("LE")
  h_TTCosTheta4.Scale(0.01688*139*1000/20000)
  h_TTCosTheta4.SetLineColor(2)
  c_TTCosTheta4.SaveAs("TTCosTheta4.png")

  # histogram of TLCosTheta1
  c_TLCosTheta1 = R.TCanvas()
  c_TLCosTheta1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_TLCosTheta1.SetFillColor(0)
  h_TLCosTheta1.Draw("LE")
  # renormalize the histogram, the cross section of TL event is 0.005741pb, ATLAS luminosity is 139 fb-1
  h_TLCosTheta1.Scale(0.005741*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_TLCosTheta1.SetLineColor(2)
  # save the histogram as png
  c_TLCosTheta1.SaveAs("TLCosTheta1.png")

  # histogram of TLCosTheta2
  c_TLCosTheta2 = R.TCanvas()
  c_TLCosTheta2.cd()
  c_TLCosTheta2.SetFillColor(0)
  h_TLCosTheta2.Draw("LE")
  h_TLCosTheta2.Scale(0.005741*139*1000/20000)
  h_TLCosTheta2.SetLineColor(2)
  c_TLCosTheta2.SaveAs("TLCosTheta2.png")

  # histogram of TLCosTheta3
  c_TLCosTheta3 = R.TCanvas()
  c_TLCosTheta3.cd()
  c_TLCosTheta3.SetFillColor(0)
  h_TLCosTheta3.Draw("LE")
  h_TLCosTheta3.Scale(0.005741*139*1000/20000)
  h_TLCosTheta3.SetLineColor(2)
  c_TLCosTheta3.SaveAs("TLCosTheta3.png")

  # histogram of TLCosTheta4
  c_TLCosTheta4 = R.TCanvas()
  c_TLCosTheta4.cd()
  c_TLCosTheta4.SetFillColor(0)
  h_TLCosTheta4.Draw("LE")
  h_TLCosTheta4.Scale(0.005741*139*1000/20000)
  h_TLCosTheta4.SetLineColor(2)
  c_TLCosTheta4.SaveAs("TLCosTheta4.png")

  # histogram of LLCosTheta1
  c_LLCosTheta1 = R.TCanvas()
  c_LLCosTheta1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_LLCosTheta1.SetFillColor(0)
  h_LLCosTheta1.Draw("LE")
  # renormalize the histogram, the cross section of LL event is 0.001406pb, ATLAS luminosity is 139 fb-1
  h_LLCosTheta1.Scale(0.001406*139*1000/20000)
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_LLCosTheta1.SetLineColor(2)
  # save the histogram as png
  c_LLCosTheta1.SaveAs("LLCosTheta1.png")

  # histogram of LLCosTheta2
  c_LLCosTheta2 = R.TCanvas()
  c_LLCosTheta2.cd()
  c_LLCosTheta2.SetFillColor(0)
  h_LLCosTheta2.Draw("LE")
  h_LLCosTheta2.Scale(0.001406*139*1000/20000)
  h_LLCosTheta2.SetLineColor(2)
  c_LLCosTheta2.SaveAs("LLCosTheta2.png")

  # histogram of LLCosTheta3
  c_LLCosTheta3 = R.TCanvas()
  c_LLCosTheta3.cd()
  c_LLCosTheta3.SetFillColor(0)
  h_LLCosTheta3.Draw("LE")
  h_LLCosTheta3.Scale(0.001406*139*1000/20000)
  h_LLCosTheta3.SetLineColor(2)
  c_LLCosTheta3.SaveAs("LLCosTheta3.png")

  # histogram of LLCosTheta4
  c_LLCosTheta4 = R.TCanvas()
  c_LLCosTheta4.cd()
  c_LLCosTheta4.SetFillColor(0)
  h_LLCosTheta4.Draw("LE")
  h_LLCosTheta4.Scale(0.001406*139*1000/20000)
  h_LLCosTheta4.SetLineColor(2)
  c_LLCosTheta4.SaveAs("LLCosTheta4.png")


  # histogram of ThetaStar1
  c_ThetaStar1 = R.TCanvas()
  c_ThetaStar1.cd()
  c_ThetaStar1.SetFillColor(0)
  h_ThetaStar1.Draw("LE")
  h_ThetaStar1.Scale(0.02419*139*1000/20000)
  h_ThetaStar1.SetLineColor(2)
  c_ThetaStar1.SaveAs("ThetaStar1.png")

  # histogram of ThetaStar2
  c_ThetaStar2 = R.TCanvas()
  c_ThetaStar2.cd()
  c_ThetaStar2.SetFillColor(0)
  h_ThetaStar2.Draw("LE")
  h_ThetaStar2.Scale(0.02419*139*1000/20000)
  h_ThetaStar2.SetLineColor(2)
  c_ThetaStar2.SaveAs("ThetaStar2.png")

  # histogram of TTThetaStar1
  c_TTThetaStar1 = R.TCanvas()
  c_TTThetaStar1.cd()
  c_TTThetaStar1.SetFillColor(0)
  h_TTThetaStar1.Draw("LE")
  h_TTThetaStar1.SetLineColor(2)
  h_TTThetaStar1.Scale(0.01688*139*1000/20000)
  c_TTThetaStar1.SaveAs("TTThetaStar1.png")

  # histogram of TTThetaStar2
  c_TTThetaStar2 = R.TCanvas()
  c_TTThetaStar2.cd()
  c_TTThetaStar2.SetFillColor(0)
  h_TTThetaStar2.Draw("LE")
  h_TTThetaStar2.Scale(0.01688*139*1000/20000)
  h_TTThetaStar2.SetLineColor(2)
  c_TTThetaStar2.SaveAs("TTThetaStar2.png")

  # histogram of TLThetaStar1
  c_TLThetaStar1 = R.TCanvas()
  c_TLThetaStar1.cd()
  c_TLThetaStar1.SetFillColor(0)
  h_TLThetaStar1.Draw("LE")
  h_TLThetaStar1.Scale(0.005741*139*1000/20000)
  h_TLThetaStar1.SetLineColor(2)
  c_TLThetaStar1.SaveAs("TLThetaStar1.png")

  # histogram of TLThetaStar2
  c_TLThetaStar2 = R.TCanvas()
  c_TLThetaStar2.cd()
  c_TLThetaStar2.SetFillColor(0)
  h_TLThetaStar2.Draw("LE")
  h_TLThetaStar2.Scale(0.005741*139*1000/20000)
  h_TLThetaStar2.SetLineColor(2)
  c_TLThetaStar2.SaveAs("TLThetaStar2.png")

  # histogram of LLThetaStar1
  c_LLThetaStar1 = R.TCanvas()
  c_LLThetaStar1.cd()
  c_LLThetaStar1.SetFillColor(0)
  h_LLThetaStar1.Draw("LE")
  h_LLThetaStar1.Scale(0.001406*139*1000/20000)
  h_LLThetaStar1.SetLineColor(2)
  c_LLThetaStar1.SaveAs("LLThetaStar1.png")

  # histogram of LLThetaStar2
  c_LLThetaStar2 = R.TCanvas()
  c_LLThetaStar2.cd()
  c_LLThetaStar2.SetFillColor(0)
  h_LLThetaStar2.Draw("LE")
  h_LLThetaStar2.Scale(0.001406*139*1000/20000)
  h_LLThetaStar2.SetLineColor(2)
  c_LLThetaStar2.SaveAs("LLThetaStar2.png")

  # histogram of CosThetaStar1
  c_CosThetaStar1 = R.TCanvas()
  c_CosThetaStar1.cd()
  c_CosThetaStar1.SetFillColor(0)
  h_CosThetaStar1.Draw("LE")
  h_CosThetaStar1.Scale(0.02419*139*1000/20000)
  h_CosThetaStar1.SetLineColor(2)
  c_CosThetaStar1.SaveAs("CosThetaStar1.png")

  # histogram of CosThetaStar2
  c_CosThetaStar2 = R.TCanvas()
  c_CosThetaStar2.cd()
  c_CosThetaStar2.SetFillColor(0)
  h_CosThetaStar2.Draw("LE")
  h_CosThetaStar2.Scale(0.02419*139*1000/20000)
  h_CosThetaStar2.SetLineColor(2)
  c_CosThetaStar2.SaveAs("CosThetaStar2.png")

  # histogram of TTCosThetaStar1
  c_TTCosThetaStar1 = R.TCanvas()
  c_TTCosThetaStar1.cd()
  c_TTCosThetaStar1.SetFillColor(0)
  h_TTCosThetaStar1.Draw("LE")
  h_TTCosThetaStar1.SetLineColor(2)
  h_TTCosThetaStar1.Scale(0.01688*139*1000/20000)
  c_TTCosThetaStar1.SaveAs("TTCosThetaStar1.png")
  
  # histogram of TTCosThetaStar2
  c_TTCosThetaStar2 = R.TCanvas()
  c_TTCosThetaStar2.cd()
  c_TTCosThetaStar2.SetFillColor(0)
  h_TTCosThetaStar2.Draw("LE")
  h_TTCosThetaStar2.Scale(0.01688*139*1000/20000)
  h_TTCosThetaStar2.SetLineColor(2)
  c_TTCosThetaStar2.SaveAs("TTCosThetaStar2.png")

  # histogram of TLCosThetaStar1
  c_TLCosThetaStar1 = R.TCanvas()
  c_TLCosThetaStar1.cd()
  c_TLCosThetaStar1.SetFillColor(0)
  h_TLCosThetaStar1.Draw("LE")
  h_TLCosThetaStar1.Scale(0.005741*139*1000/20000)
  h_TLCosThetaStar1.SetLineColor(2)
  c_TLCosThetaStar1.SaveAs("TLCosThetaStar1.png")
  
  # histogram of TLCosThetaStar2
  c_TLCosThetaStar2 = R.TCanvas()
  c_TLCosThetaStar2.cd()
  c_TLCosThetaStar2.SetFillColor(0)
  h_TLCosThetaStar2.Draw("LE")
  h_TLCosThetaStar2.Scale(0.005741*139*1000/20000)
  h_TLCosThetaStar2.SetLineColor(2)
  c_TLCosThetaStar2.SaveAs("TLCosThetaStar2.png")

  # histogram of LLCosThetaStar1
  c_LLCosThetaStar1 = R.TCanvas()
  c_LLCosThetaStar1.cd()
  c_LLCosThetaStar1.SetFillColor(0)
  h_LLCosThetaStar1.Draw("LE")
  h_LLCosThetaStar1.Scale(0.001406*139*1000/20000)
  h_LLCosThetaStar1.SetLineColor(2)
  c_LLCosThetaStar1.SaveAs("LLCosThetaStar1.png")
  
  # histogram of LLCosThetaStar2
  c_LLCosThetaStar2 = R.TCanvas()
  c_LLCosThetaStar2.cd()
  c_LLCosThetaStar2.SetFillColor(0)
  h_LLCosThetaStar2.Draw("LE")
  h_LLCosThetaStar2.Scale(0.001406*139*1000/20000)
  h_LLCosThetaStar2.SetLineColor(2)
  c_LLCosThetaStar2.SaveAs("LLCosThetaStar2.png")


  # histogram of Phi
  c_Phi = R.TCanvas()
  c_Phi.cd()
  c_Phi.SetFillColor(0)
  h_Phi.Draw("LE")
  h_Phi.Scale(0.02419*139*1000/20000)
  h_Phi.SetLineColor(2)
  c_Phi.SaveAs("Phi.png")

  # histogram of TTPhi
  c_TTPhi = R.TCanvas()
  c_TTPhi.cd()
  c_TTPhi.SetFillColor(0)
  h_TTPhi.Draw("LE")
  h_TTPhi.Scale(0.01688*139*1000/20000)
  h_TTPhi.SetLineColor(2)
  c_TTPhi.SaveAs("TTPhi.png")

  # histogram of TLPhi
  c_TLPhi = R.TCanvas()
  c_TLPhi.cd()
  c_TLPhi.SetFillColor(0)
  h_TLPhi.Draw("LE")
  h_TLPhi.Scale(0.005741*139*1000/20000)
  h_TLPhi.SetLineColor(2)
  c_TLPhi.SaveAs("TLPhi.png")

  # histogram of LLPhi
  c_LLPhi = R.TCanvas()
  c_LLPhi.cd()
  c_LLPhi.SetFillColor(0)
  h_LLPhi.Draw("LE")
  h_LLPhi.Scale(0.001406*139*1000/20000)
  h_LLPhi.SetLineColor(2)
  c_LLPhi.SaveAs("LLPhi.png")


  # histogram of CosPhi
  c_CosPhi = R.TCanvas()
  c_CosPhi.cd()
  c_CosPhi.SetFillColor(0)
  h_CosPhi.Draw("LE")
  h_CosPhi.Scale(0.02419*139*1000/20000)
  h_CosPhi.SetLineColor(2)
  c_CosPhi.SaveAs("CosPhi.png")

  # histogram of TTCosPhi
  c_TTCosPhi = R.TCanvas()
  c_TTCosPhi.cd()
  c_TTCosPhi.SetFillColor(0)
  h_TTCosPhi.Draw("LE")
  h_TTCosPhi.Scale(0.01688*139*1000/20000)
  h_TTCosPhi.SetLineColor(2)
  c_TTCosPhi.SaveAs("TTCosPhi.png")

  # histogram of TLCosPhi
  c_TLCosPhi = R.TCanvas()
  c_TLCosPhi.cd()
  c_TLCosPhi.SetFillColor(0)
  h_TLCosPhi.Draw("LE")
  h_TLCosPhi.Scale(0.005741*139*1000/20000)
  h_TLCosPhi.SetLineColor(2)
  c_TLCosPhi.SaveAs("TLCosPhi.png")

  # histogram of LLCosPhi
  c_LLCosPhi = R.TCanvas()
  c_LLCosPhi.cd()
  c_LLCosPhi.SetFillColor(0)
  h_LLCosPhi.Draw("LE")
  h_LLCosPhi.Scale(0.001406*139*1000/20000)
  h_LLCosPhi.SetLineColor(2)
  c_LLCosPhi.SaveAs("LLCosPhi.png")


  # histogram of Phi1
  c_Phi1 = R.TCanvas()
  c_Phi1.cd()
  c_Phi1.SetFillColor(0)
  h_Phi1.Draw("LE")
  h_Phi1.Scale(0.02419*139*1000/20000)
  h_Phi1.SetLineColor(2)
  c_Phi1.SaveAs("Phi1.png")

  # histogram of TTPhi1
  c_TTPhi1 = R.TCanvas()
  c_TTPhi1.cd()
  c_TTPhi1.SetFillColor(0)
  h_TTPhi1.Draw("LE")
  h_TTPhi1.Scale(0.01688*139*1000/20000)
  h_TTPhi1.SetLineColor(2)
  c_TTPhi1.SaveAs("TTPhi1.png")

  # histogram of TLPhi1
  c_TLPhi1 = R.TCanvas()
  c_TLPhi1.cd()
  c_TLPhi1.SetFillColor(0)
  h_TLPhi1.Draw("LE")
  h_TLPhi1.Scale(0.005741*139*1000/20000)
  h_TLPhi1.SetLineColor(2)
  c_TLPhi1.SaveAs("TLPhi1.png")

  # histogram of LLPhi1
  c_LLPhi1 = R.TCanvas()
  c_LLPhi1.cd()
  c_LLPhi1.SetFillColor(0)
  h_LLPhi1.Draw("LE")
  h_LLPhi1.Scale(0.001406*139*1000/20000)
  h_LLPhi1.SetLineColor(2)
  c_LLPhi1.SaveAs("LLPhi1.png")


  # histogram of CosPhi1
  c_CosPhi1 = R.TCanvas()
  c_CosPhi1.cd()
  c_CosPhi1.SetFillColor(0)
  h_CosPhi1.Draw("LE")
  h_CosPhi1.Scale(0.02419*139*1000/20000)
  h_CosPhi1.SetLineColor(2)
  c_CosPhi1.SaveAs("CosPhi1.png")
  
  # histogram of TTCosPhi1
  c_TTCosPhi1 = R.TCanvas()
  c_TTCosPhi1.cd()
  c_TTCosPhi1.SetFillColor(0)
  h_TTCosPhi1.Draw("LE")
  h_TTCosPhi1.Scale(0.01688*139*1000/20000)
  h_TTCosPhi1.SetLineColor(2)
  c_TTCosPhi1.SaveAs("TTCosPhi1.png")

  # histogram of TLCosPhi1
  c_TLCosPhi1 = R.TCanvas()
  c_TLCosPhi1.cd()
  c_TLCosPhi1.SetFillColor(0)
  h_TLCosPhi1.Draw("LE")
  h_TLCosPhi1.Scale(0.005741*139*1000/20000)
  h_TLCosPhi1.SetLineColor(2)
  c_TLCosPhi1.SaveAs("TLCosPhi1.png")

  # histogram of LLCosPhi1
  c_LLCosPhi1 = R.TCanvas()
  c_LLCosPhi1.cd()
  c_LLCosPhi1.SetFillColor(0)
  h_LLCosPhi1.Draw("LE")
  h_LLCosPhi1.Scale(0.001406*139*1000/20000)
  h_LLCosPhi1.SetLineColor(2)
  c_LLCosPhi1.SaveAs("LLCosPhi1.png")



  """
  several histograms in a Canvas
  Since class Scale has already been used to renormalize all the histogram above, I needn't renormalize it below
  """

  # histogram of M1 and M1MOTHUP
  c_M1_M1MOTHUP = R.TCanvas()
  c_M1_M1MOTHUP.cd()
  c_M1_M1MOTHUP.SetFillColor(0)
  h_M1.Draw("LE")
  # plot the 2ed histogram in the same Canvas
  h_M1MOTHUP.Draw("SameLE")
  h_M1.SetLineColor(3)
  h_M1MOTHUP.SetLineColor(2)
  # set the title of these 2 histograms
  h_M1.SetTitle("Compare M1 and M1MOTHUP; ZMass/GeV; events")
  h_M1MOTHUP.SetTitle("Compare M1 and M1MOTHUP; ZMass/GeV; events")
  # set the range of the axis
  Max1 = h_M1.GetMaximum()
  Max2 = h_M1MOTHUP.GetMaximum()
  Max = max(Max1, Max2)
  h_M1.SetMaximum(Max*1.2)
  h_M1MOTHUP.SetMaximum(Max*1.2)
  h_M1.SetMinimum(0)
  h_M1MOTHUP.SetMinimum(0)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.8, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_M1,"M1","LE")
  leg.AddEntry(h_M1MOTHUP,"M1MOTHUP","LE")
  leg.Draw()

  c_M1_M1MOTHUP.SaveAs("M1_M1MOTHUP.png")
  c_M1_M1MOTHUP.Close()



  # histogram of M2 and M2MOTHUP
  c_M2_M2MOTHUP = R.TCanvas()
  c_M2_M2MOTHUP.cd()
  c_M2_M2MOTHUP.SetFillColor(0)
  h_M2.Draw("LE")
  h_M2MOTHUP.Draw("SameLE")
  h_M2.SetLineColor(3)
  h_M2MOTHUP.SetLineColor(2)
  h_M2.SetTitle("Compare M2 and M2MOTHUP; ZMass/GeV; events")
  h_M2MOTHUP.SetTitle("Compare M2 and M2MOTHUP; ZMass/GeV; events")

  # set the range of the axis
  Max1 = h_M2.GetMaximum()
  Max2 = h_M2MOTHUP.GetMaximum()
  Max = max(Max1, Max2)
  h_M2.SetMaximum(Max*1.2)
  h_M2MOTHUP.SetMaximum(Max*1.2)
  h_M2.SetMinimum(0)
  h_M2MOTHUP.SetMinimum(0)

  leg = R.TLegend(0.7, 0.8, 0.9, 0.9)
  leg.SetBorderSize(0)
  leg.SetFillStyle(0)
  leg.AddEntry(h_M2,"M2","LE")
  leg.AddEntry(h_M2MOTHUP,"M2MOTHUP","LE")
  leg.Draw()

  c_M2_M2MOTHUP.SaveAs("M2_M2MOTHUP.png")
  c_M2_M2MOTHUP.Close()



  # histogram of M1, TTM1, TLM1, LLM1
  c_M1Sum = R.TCanvas()
  c_M1Sum.cd()
  c_M1Sum.SetFillColor(0)
  h_M1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTM1.Draw("SameLE")
  h_TLM1.Draw("SameLE")
  h_LLM1.Draw("SameLE")

  h_M1.SetLineColor(1)
  h_TTM1.SetLineColor(2)
  h_TLM1.SetLineColor(3)
  h_LLM1.SetLineColor(4)

  # set the title of these 4 histograms
  h_M1.SetTitle("Compare M1; ZMass/GeV; events")
  h_TTM1.SetTitle("Compare M1; ZMass/GeV; events")
  h_TLM1.SetTitle("Compare M1; ZMass/GeV; events")
  h_LLM1.SetTitle("Compare M1; ZMass/GeV; events")

  # set the range of the axis
  Max1 = h_M1.GetMaximum()
  Max2 = h_TTM1.GetMaximum()
  Max3 = h_TLM1.GetMaximum()
  Max4 = h_LLM1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_M1.SetMaximum(Max*1.2)
  h_TTM1.SetMaximum(Max*1.2)
  h_TLM1.SetMaximum(Max*1.2)
  h_LLM1.SetMaximum(Max*1.2)
  h_M1.SetMinimum(0)
  h_TTM1.SetMinimum(0)
  h_TLM1.SetMinimum(0)
  h_LLM1.SetMinimum(0)

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
  leg.AddEntry(h_M1,"Inclusive","LE")
  leg.AddEntry(h_TTM1,"TT","LE")
  leg.AddEntry(h_TLM1,"TL","LE")
  leg.AddEntry(h_LLM1,"LL","LE")
  leg.Draw()

  c_M1Sum.SaveAs("M1Sum.png")
  c_M1Sum.Close()



  # histogram of M2, TTM2, TLM2, LLM2
  c_M2Sum = R.TCanvas()
  c_M2Sum.cd()
  c_M2Sum.SetFillColor(0)
  h_M2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTM2.Draw("SameLE")
  h_TLM2.Draw("SameLE")
  h_LLM2.Draw("SameLE")

  h_M2.SetLineColor(1)
  h_TTM2.SetLineColor(2)
  h_TLM2.SetLineColor(3)
  h_LLM2.SetLineColor(4)

  # set the title of these 4 histograms
  h_M2.SetTitle("Compare M2; ZMass/GeV; events")
  h_TTM2.SetTitle("Compare M2; ZMass/GeV; events")
  h_TLM2.SetTitle("Compare M2; ZMass/GeV; events")
  h_LLM2.SetTitle("Compare M2; ZMass/GeV; events")

  # set the range of the axis
  Max1 = h_M2.GetMaximum()
  Max2 = h_TTM2.GetMaximum()
  Max3 = h_TLM2.GetMaximum()
  Max4 = h_LLM2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_M2.SetMaximum(Max*1.2)
  h_TTM2.SetMaximum(Max*1.2)
  h_TLM2.SetMaximum(Max*1.2)
  h_LLM2.SetMaximum(Max*1.2)
  h_M2.SetMinimum(0)
  h_TTM2.SetMinimum(0)
  h_TLM2.SetMinimum(0)
  h_LLM2.SetMinimum(0)

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
  leg.AddEntry(h_M2,"Inclusive","LE")
  leg.AddEntry(h_TTM2,"TT","LE")
  leg.AddEntry(h_TLM2,"TL","LE")
  leg.AddEntry(h_LLM2,"LL","LE")
  leg.Draw()

  c_M2Sum.SaveAs("M2Sum.png")
  c_M2Sum.Close()



  # histogram of CosTheta1, TTCosTheta1, TLCosTheta1, LLCosTheta1
  c_CosTheta1Sum = R.TCanvas()
  c_CosTheta1Sum.cd()
  c_CosTheta1Sum.SetFillColor(0)
  h_CosTheta1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta1.Draw("SameLE")
  h_TLCosTheta1.Draw("SameLE")
  h_LLCosTheta1.Draw("SameLE")

  h_CosTheta1.SetLineColor(1)
  h_TTCosTheta1.SetLineColor(2)
  h_TLCosTheta1.SetLineColor(3)
  h_LLCosTheta1.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_TTCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_TLCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_LLCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")

  # set the range of the axis
  Max1 = h_CosTheta1.GetMaximum()
  Max2 = h_TTCosTheta1.GetMaximum()
  Max3 = h_TLCosTheta1.GetMaximum()
  Max4 = h_LLCosTheta1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosTheta1.SetMaximum(Max*1.2)
  h_TTCosTheta1.SetMaximum(Max*1.2)
  h_TLCosTheta1.SetMaximum(Max*1.2)
  h_LLCosTheta1.SetMaximum(Max*1.2)
  h_CosTheta1.SetMinimum(0)
  h_TTCosTheta1.SetMinimum(0)
  h_TLCosTheta1.SetMinimum(0)
  h_LLCosTheta1.SetMinimum(0)

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
  leg.AddEntry(h_CosTheta1,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta1,"TT","LE")
  leg.AddEntry(h_TLCosTheta1,"TL","LE")
  leg.AddEntry(h_LLCosTheta1,"LL","LE")
  leg.Draw()

  c_CosTheta1Sum.SaveAs("CosTheta1Sum.png")
  c_CosTheta1Sum.Close()



  # histogram of CosTheta2, TTCosTheta2, TLCosTheta2, LLCosTheta2
  c_CosTheta2Sum = R.TCanvas()
  c_CosTheta2Sum.cd()
  c_CosTheta2Sum.SetFillColor(0)
  h_CosTheta2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta2.Draw("SameLE")
  h_TLCosTheta2.Draw("SameLE")
  h_LLCosTheta2.Draw("SameLE")

  h_CosTheta2.SetLineColor(1)
  h_TTCosTheta2.SetLineColor(2)
  h_TLCosTheta2.SetLineColor(3)
  h_LLCosTheta2.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_TTCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_TLCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_LLCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")

  # set the range of the axis
  Max1 = h_CosTheta2.GetMaximum()
  Max2 = h_TTCosTheta2.GetMaximum()
  Max3 = h_TLCosTheta2.GetMaximum()
  Max4 = h_LLCosTheta2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosTheta2.SetMaximum(Max*1.2)
  h_TTCosTheta2.SetMaximum(Max*1.2)
  h_TLCosTheta2.SetMaximum(Max*1.2)
  h_LLCosTheta2.SetMaximum(Max*1.2)
  h_CosTheta2.SetMinimum(0)
  h_TTCosTheta2.SetMinimum(0)
  h_TLCosTheta2.SetMinimum(0)
  h_LLCosTheta2.SetMinimum(0)

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
  leg.AddEntry(h_CosTheta2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta2,"TT","LE")
  leg.AddEntry(h_TLCosTheta2,"TL","LE")
  leg.AddEntry(h_LLCosTheta2,"LL","LE")
  leg.Draw()

  c_CosTheta2Sum.SaveAs("CosTheta2Sum.png")
  c_CosTheta2Sum.Close()



  # histogram of CosTheta3, TTCosTheta3, TLCosTheta3, LLCosTheta3
  c_CosTheta3Sum = R.TCanvas()
  c_CosTheta3Sum.cd()
  c_CosTheta3Sum.SetFillColor(0)
  h_CosTheta3.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta3.Draw("SameLE")
  h_TLCosTheta3.Draw("SameLE")
  h_LLCosTheta3.Draw("SameLE")

  h_CosTheta3.SetLineColor(1)
  h_TTCosTheta3.SetLineColor(2)
  h_TLCosTheta3.SetLineColor(3)
  h_LLCosTheta3.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_TTCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_TLCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_LLCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")

  # set the range of the axis
  Max1 = h_CosTheta3.GetMaximum()
  Max2 = h_TTCosTheta3.GetMaximum()
  Max3 = h_TLCosTheta3.GetMaximum()
  Max4 = h_LLCosTheta3.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosTheta3.SetMaximum(Max*1.2)
  h_TTCosTheta3.SetMaximum(Max*1.2)
  h_TLCosTheta3.SetMaximum(Max*1.2)
  h_LLCosTheta3.SetMaximum(Max*1.2)
  h_CosTheta3.SetMinimum(0)
  h_TTCosTheta3.SetMinimum(0)
  h_TLCosTheta3.SetMinimum(0)
  h_LLCosTheta3.SetMinimum(0)

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
  leg.AddEntry(h_CosTheta3,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta3,"TT","LE")
  leg.AddEntry(h_TLCosTheta3,"TL","LE")
  leg.AddEntry(h_LLCosTheta3,"LL","LE")
  leg.Draw()

  c_CosTheta3Sum.SaveAs("CosTheta3Sum.png")
  c_CosTheta3Sum.Close()



  # histogram of CosTheta4, TTCosTheta4, TLCosTheta4, LLCosTheta4
  c_CosTheta4Sum = R.TCanvas()
  c_CosTheta4Sum.cd()
  c_CosTheta4Sum.SetFillColor(0)
  h_CosTheta4.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta4.Draw("SameLE")
  h_TLCosTheta4.Draw("SameLE")
  h_LLCosTheta4.Draw("SameLE")

  h_CosTheta4.SetLineColor(1)
  h_TTCosTheta4.SetLineColor(2)
  h_TLCosTheta4.SetLineColor(3)
  h_LLCosTheta4.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_TTCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_TLCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_LLCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")

  # set the range of the axis
  Max1 = h_CosTheta4.GetMaximum()
  Max2 = h_TTCosTheta4.GetMaximum()
  Max3 = h_TLCosTheta4.GetMaximum()
  Max4 = h_LLCosTheta4.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosTheta4.SetMaximum(Max*1.2)
  h_TTCosTheta4.SetMaximum(Max*1.2)
  h_TLCosTheta4.SetMaximum(Max*1.2)
  h_LLCosTheta4.SetMaximum(Max*1.2)
  h_CosTheta4.SetMinimum(0)
  h_TTCosTheta4.SetMinimum(0)
  h_TLCosTheta4.SetMinimum(0)
  h_LLCosTheta4.SetMinimum(0)

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
  leg.AddEntry(h_CosTheta4,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta4,"TT","LE")
  leg.AddEntry(h_TLCosTheta4,"TL","LE")
  leg.AddEntry(h_LLCosTheta4,"LL","LE")
  leg.Draw()

  c_CosTheta4Sum.SaveAs("CosTheta4Sum.png")
  c_CosTheta4Sum.Close()


  # histogram of ThetaStar1, TTThetaStar1, TLThetaStar1, LLThetaStar1
  c_ThetaStar1Sum = R.TCanvas()
  c_ThetaStar1Sum.cd()
  c_ThetaStar1Sum.SetFillColor(0)
  h_ThetaStar1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTThetaStar1.Draw("SameLE")
  h_TLThetaStar1.Draw("SameLE")
  h_LLThetaStar1.Draw("SameLE")

  h_ThetaStar1.SetLineColor(1)
  h_TTThetaStar1.SetLineColor(2)
  h_TLThetaStar1.SetLineColor(3)
  h_LLThetaStar1.SetLineColor(4)

  # set the title of these 4 histograms
  h_ThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_TTThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_TLThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_LLThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")

  # set the range of the axis
  Max1 = h_ThetaStar1.GetMaximum()
  Max2 = h_TTThetaStar1.GetMaximum()
  Max3 = h_TLThetaStar1.GetMaximum()
  Max4 = h_LLThetaStar1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_ThetaStar1.SetMaximum(Max*1.2)
  h_TTThetaStar1.SetMaximum(Max*1.2)
  h_TLThetaStar1.SetMaximum(Max*1.2)
  h_LLThetaStar1.SetMaximum(Max*1.2)
  h_ThetaStar1.SetMinimum(0)
  h_TTThetaStar1.SetMinimum(0)
  h_TLThetaStar1.SetMinimum(0)
  h_LLThetaStar1.SetMinimum(0)

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
  leg.AddEntry(h_ThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar1,"TT","LE")
  leg.AddEntry(h_TLThetaStar1,"TL","LE")
  leg.AddEntry(h_LLThetaStar1,"LL","LE")
  leg.Draw()

  c_ThetaStar1Sum.SaveAs("ThetaStar1Sum.png")
  c_ThetaStar1Sum.Close()



  # histogram of ThetaStar2, TTThetaStar2, TLThetaStar2, LLThetaStar2
  c_ThetaStar2Sum = R.TCanvas()
  c_ThetaStar2Sum.cd()
  c_ThetaStar2Sum.SetFillColor(0)
  h_ThetaStar2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTThetaStar2.Draw("SameLE")
  h_TLThetaStar2.Draw("SameLE")
  h_LLThetaStar2.Draw("SameLE")

  h_ThetaStar2.SetLineColor(1)
  h_TTThetaStar2.SetLineColor(2)
  h_TLThetaStar2.SetLineColor(3)
  h_LLThetaStar2.SetLineColor(4)

  # set the title of these 4 histograms
  h_ThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_TTThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_TLThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_LLThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")

  # set the range of the axis
  Max1 = h_ThetaStar2.GetMaximum()
  Max2 = h_TTThetaStar2.GetMaximum()
  Max3 = h_TLThetaStar2.GetMaximum()
  Max4 = h_LLThetaStar2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_ThetaStar2.SetMaximum(Max*1.2)
  h_TTThetaStar2.SetMaximum(Max*1.2)
  h_TLThetaStar2.SetMaximum(Max*1.2)
  h_LLThetaStar2.SetMaximum(Max*1.2)
  h_ThetaStar2.SetMinimum(0)
  h_TTThetaStar2.SetMinimum(0)
  h_TLThetaStar2.SetMinimum(0)
  h_LLThetaStar2.SetMinimum(0)

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
  leg.AddEntry(h_ThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar2,"TT","LE")
  leg.AddEntry(h_TLThetaStar2,"TL","LE")
  leg.AddEntry(h_LLThetaStar2,"LL","LE")
  leg.Draw()

  c_ThetaStar2Sum.SaveAs("ThetaStar2Sum.png")
  c_ThetaStar2Sum.Close()



  # histogram of CosThetaStar1, TTCosThetaStar1, TLCosThetaStar1, LLCosThetaStar1
  c_CosThetaStar1Sum = R.TCanvas()
  c_CosThetaStar1Sum.cd()
  c_CosThetaStar1Sum.SetFillColor(0)
  h_CosThetaStar1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosThetaStar1.Draw("SameLE")
  h_TLCosThetaStar1.Draw("SameLE")
  h_LLCosThetaStar1.Draw("SameLE")

  h_CosThetaStar1.SetLineColor(1)
  h_TTCosThetaStar1.SetLineColor(2)
  h_TLCosThetaStar1.SetLineColor(3)
  h_LLCosThetaStar1.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_TTCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_TLCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_LLCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")

  # set the range of the axis
  Max1 = h_CosThetaStar1.GetMaximum()
  Max2 = h_TTCosThetaStar1.GetMaximum()
  Max3 = h_TLCosThetaStar1.GetMaximum()
  Max4 = h_LLCosThetaStar1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosThetaStar1.SetMaximum(Max*1.2)
  h_TTCosThetaStar1.SetMaximum(Max*1.2)
  h_TLCosThetaStar1.SetMaximum(Max*1.2)
  h_LLCosThetaStar1.SetMaximum(Max*1.2)
  h_CosThetaStar1.SetMinimum(0)
  h_TTCosThetaStar1.SetMinimum(0)
  h_TLCosThetaStar1.SetMinimum(0)
  h_LLCosThetaStar1.SetMinimum(0)

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
  leg.AddEntry(h_CosThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar1,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar1,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar1,"LL","LE")
  leg.Draw()

  c_CosThetaStar1Sum.SaveAs("CosThetaStar1Sum.png")
  c_CosThetaStar1Sum.Close()



  # histogram of CosThetaStar2, TTCosThetaStar2, TLCosThetaStar2, LLCosThetaStar2
  c_CosThetaStar2Sum = R.TCanvas()
  c_CosThetaStar2Sum.cd()
  c_CosThetaStar2Sum.SetFillColor(0)
  h_CosThetaStar2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosThetaStar2.Draw("SameLE")
  h_TLCosThetaStar2.Draw("SameLE")
  h_LLCosThetaStar2.Draw("SameLE")

  h_CosThetaStar2.SetLineColor(1)
  h_TTCosThetaStar2.SetLineColor(2)
  h_TLCosThetaStar2.SetLineColor(3)
  h_LLCosThetaStar2.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_TTCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_TLCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_LLCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")

  # set the range of the axis
  Max1 = h_CosThetaStar2.GetMaximum()
  Max2 = h_TTCosThetaStar2.GetMaximum()
  Max3 = h_TLCosThetaStar2.GetMaximum()
  Max4 = h_LLCosThetaStar2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosThetaStar2.SetMaximum(Max*1.2)
  h_TTCosThetaStar2.SetMaximum(Max*1.2)
  h_TLCosThetaStar2.SetMaximum(Max*1.2)
  h_LLCosThetaStar2.SetMaximum(Max*1.2)
  h_CosThetaStar2.SetMinimum(0)
  h_TTCosThetaStar2.SetMinimum(0)
  h_TLCosThetaStar2.SetMinimum(0)
  h_LLCosThetaStar2.SetMinimum(0)

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
  leg.AddEntry(h_CosThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar2,"LL","LE")
  leg.Draw()

  c_CosThetaStar2Sum.SaveAs("CosThetaStar2Sum.png")
  c_CosThetaStar2Sum.Close()



  # histogram of Phi, TTPhi, TLPhi, LLPhi
  c_PhiSum = R.TCanvas()
  c_PhiSum.cd()
  c_PhiSum.SetFillColor(0)

  h_Phi.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTPhi.Draw("SameLE")
  h_TLPhi.Draw("SameLE")
  h_LLPhi.Draw("SameLE")

  h_Phi.SetLineColor(1)
  h_TTPhi.SetLineColor(2)
  h_TLPhi.SetLineColor(3)
  h_LLPhi.SetLineColor(4)

  # set the title of these 4 histograms
  h_Phi.SetTitle("Compare Phi; Phi; events")
  h_TTPhi.SetTitle("Compare Phi; Phi; events")
  h_TLPhi.SetTitle("Compare Phi; Phi; events")
  h_LLPhi.SetTitle("Compare Phi; Phi; events")

  # set the range of the axis
  Max1 = h_Phi.GetMaximum()
  Max2 = h_TTPhi.GetMaximum()
  Max3 = h_TLPhi.GetMaximum()
  Max4 = h_LLPhi.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_Phi.SetMaximum(Max*1.2)
  h_TTPhi.SetMaximum(Max*1.2)
  h_TLPhi.SetMaximum(Max*1.2)
  h_LLPhi.SetMaximum(Max*1.2)
  h_Phi.SetMinimum(0)
  h_TTPhi.SetMinimum(0)
  h_TLPhi.SetMinimum(0)
  h_LLPhi.SetMinimum(0)

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
  leg.AddEntry(h_Phi,"Inclusive","LE")
  leg.AddEntry(h_TTPhi,"TT","LE")
  leg.AddEntry(h_TLPhi,"TL","LE")
  leg.AddEntry(h_LLPhi,"LL","LE")
  leg.Draw()

  c_PhiSum.SaveAs("PhiSum.png")
  c_PhiSum.Close()



  # histogram of CosPhi, TTCosPhi, TLCosPhi, LLCosPhi
  c_CosPhiSum = R.TCanvas()
  c_CosPhiSum.cd()
  c_CosPhiSum.SetFillColor(0)

  h_CosPhi.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosPhi.Draw("SameLE")
  h_TLCosPhi.Draw("SameLE")
  h_LLCosPhi.Draw("SameLE")

  h_CosPhi.SetLineColor(1)
  h_TTCosPhi.SetLineColor(2)
  h_TLCosPhi.SetLineColor(3)
  h_LLCosPhi.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_TTCosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_TLCosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_LLCosPhi.SetTitle("Compare CosPhi; CosPhi; events")

  # set the range of the axis
  Max1 = h_CosPhi.GetMaximum()
  Max2 = h_TTCosPhi.GetMaximum()
  Max3 = h_TLCosPhi.GetMaximum()
  Max4 = h_LLCosPhi.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosPhi.SetMaximum(Max*1.2)
  h_TTCosPhi.SetMaximum(Max*1.2)
  h_TLCosPhi.SetMaximum(Max*1.2)
  h_LLCosPhi.SetMaximum(Max*1.2)
  h_CosPhi.SetMinimum(0)
  h_TTCosPhi.SetMinimum(0)
  h_TLCosPhi.SetMinimum(0)
  h_LLCosPhi.SetMinimum(0)

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
  leg.AddEntry(h_CosPhi,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi,"TT","LE")
  leg.AddEntry(h_TLCosPhi,"TL","LE")
  leg.AddEntry(h_LLCosPhi,"LL","LE")
  leg.Draw()

  c_CosPhiSum.SaveAs("CosPhiSum.png")
  c_CosPhiSum.Close()



  # histogram of Phi1, TTPhi1, TLPhi1, LLPhi1
  c_Phi1Sum = R.TCanvas()
  c_Phi1Sum.cd()
  c_Phi1Sum.SetFillColor(0)

  h_Phi1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTPhi1.Draw("SameLE")
  h_TLPhi1.Draw("SameLE")
  h_LLPhi1.Draw("SameLE")

  h_Phi1.SetLineColor(1)
  h_TTPhi1.SetLineColor(2)
  h_TLPhi1.SetLineColor(3)
  h_LLPhi1.SetLineColor(4)

  # set the title of these 4 histograms
  h_Phi1.SetTitle("Compare Phi1; Phi1; events")
  h_TTPhi1.SetTitle("Compare Phi1; Phi1; events")
  h_TLPhi1.SetTitle("Compare Phi1; Phi1; events")
  h_LLPhi1.SetTitle("Compare Phi1; Phi1; events")

  # set the range of the axis
  Max1 = h_Phi1.GetMaximum()
  Max2 = h_TTPhi1.GetMaximum()
  Max3 = h_TLPhi1.GetMaximum()
  Max4 = h_LLPhi1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_Phi1.SetMaximum(Max*1.2)
  h_TTPhi1.SetMaximum(Max*1.2)
  h_TLPhi1.SetMaximum(Max*1.2)
  h_LLPhi1.SetMaximum(Max*1.2)
  h_Phi1.SetMinimum(0)
  h_TTPhi1.SetMinimum(0)
  h_TLPhi1.SetMinimum(0)
  h_LLPhi1.SetMinimum(0)

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
  leg.AddEntry(h_Phi1,"Inclusive","LE")
  leg.AddEntry(h_TTPhi1,"TT","LE")
  leg.AddEntry(h_TLPhi1,"TL","LE")
  leg.AddEntry(h_LLPhi1,"LL","LE")
  leg.Draw()

  c_Phi1Sum.SaveAs("Phi1Sum.png")
  c_Phi1Sum.Close()



  # histogram of CosPhi1, TTCosPhi1, TLCosPhi1, LLCosPhi1
  c_CosPhi1Sum = R.TCanvas()
  c_CosPhi1Sum.cd()
  c_CosPhi1Sum.SetFillColor(0)
  h_CosPhi1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosPhi1.Draw("SameLE")
  h_TLCosPhi1.Draw("SameLE")
  h_LLCosPhi1.Draw("SameLE")

  h_CosPhi1.SetLineColor(1)
  h_TTCosPhi1.SetLineColor(2)
  h_TLCosPhi1.SetLineColor(3)
  h_LLCosPhi1.SetLineColor(4)

  # set the title of these 4 histograms
  h_CosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_TTCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_TLCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_LLCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")

  # set the range of the axis
  Max1 = h_CosPhi1.GetMaximum()
  Max2 = h_TTCosPhi1.GetMaximum()
  Max3 = h_TLCosPhi1.GetMaximum()
  Max4 = h_LLCosPhi1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4)
  h_CosPhi1.SetMaximum(Max*1.2)
  h_TTCosPhi1.SetMaximum(Max*1.2)
  h_TLCosPhi1.SetMaximum(Max*1.2)
  h_LLCosPhi1.SetMaximum(Max*1.2)
  h_CosPhi1.SetMinimum(0)
  h_TTCosPhi1.SetMinimum(0)
  h_TLCosPhi1.SetMinimum(0)
  h_LLCosPhi1.SetMinimum(0)

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
  leg.AddEntry(h_CosPhi1,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi1,"TT","LE")
  leg.AddEntry(h_TLCosPhi1,"TL","LE")
  leg.AddEntry(h_LLCosPhi1,"LL","LE")
  leg.Draw()

  c_CosPhi1Sum.SaveAs("CosPhi1Sum.png")
  c_CosPhi1Sum.Close()



  """
  Add the histogram of TT, TL and LL, name it as TT+TL+LL, put it in a single histogram with TT, TL, LL and inclusive.
  """

  # histogram of M1, TTM1, TLM1, LLM1, TT+TL+LLM1
  c_M1SumAdd = R.TCanvas()
  c_M1SumAdd.cd()
  c_M1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLM1"
  nbins, xmin, xmax = 40, 80, 100
  h_AddM1 = R.TH1F("TT+TL+LLM1", htitle, nbins, xmin, xmax)
  h_AddM1.Add(h_TTM1, 1)
  h_AddM1.Add(h_TLM1, 1)
  h_AddM1.Add(h_LLM1, 1)

  h_M1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTM1.Draw("SameLE")
  h_TLM1.Draw("SameLE")
  h_LLM1.Draw("SameLE")
  h_AddM1.Draw("SameLE")

  h_M1.SetLineColor(1)
  h_TTM1.SetLineColor(2)
  h_TLM1.SetLineColor(3)
  h_LLM1.SetLineColor(4)
  h_AddM1.SetLineColor(5)

  # set the title of these 4 histograms
  h_M1.SetTitle("Compare M1; ZMass/GeV; events")
  h_TTM1.SetTitle("Compare M1; ZMass/GeV; events")
  h_TLM1.SetTitle("Compare M1; ZMass/GeV; events")
  h_LLM1.SetTitle("Compare M1; ZMass/GeV; events")
  h_AddM1.SetTitle("Compare M1; ZMass/GeV; events")

  # set the range of the axis
  Max1 = h_M1.GetMaximum()
  Max2 = h_TTM1.GetMaximum()
  Max3 = h_TLM1.GetMaximum()
  Max4 = h_LLM1.GetMaximum()
  Max5 = h_AddM1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_M1.SetMaximum(Max*1.2)
  h_TTM1.SetMaximum(Max*1.2)
  h_TLM1.SetMaximum(Max*1.2)
  h_LLM1.SetMaximum(Max*1.2)
  h_AddM1.SetMaximum(Max*1.2)
  h_M1.SetMinimum(0)
  h_TTM1.SetMinimum(0)
  h_TLM1.SetMinimum(0)
  h_LLM1.SetMinimum(0)
  h_AddM1.SetMinimum(0)


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
  leg.AddEntry(h_M1,"Inclusive","LE")
  leg.AddEntry(h_TTM1,"TT","LE")
  leg.AddEntry(h_TLM1,"TL","LE")
  leg.AddEntry(h_LLM1,"LL","LE")
  leg.AddEntry(h_AddM1,"TT+TL+LL","LE")
  leg.Draw()


  c_M1SumAdd.SaveAs("M1SumAdd.png")
  c_M1SumAdd.Close()


  # histogram of M2, TTM2, TLM2, LLM2, TT+TL+LLM2
  c_M2SumAdd = R.TCanvas()
  c_M2SumAdd.cd()
  c_M2SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLM2"
  nbins, xmin, xmax = 40, 70, 110
  h_AddM2 = R.TH1F("TT+TL+LLM2", htitle, nbins, xmin, xmax)
  h_AddM2.Add(h_TTM2, 1)
  h_AddM2.Add(h_TLM2, 1)
  h_AddM2.Add(h_LLM2, 1)

  h_M2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTM2.Draw("SameLE")
  h_TLM2.Draw("SameLE")
  h_LLM2.Draw("SameLE")
  h_AddM2.Draw("SameLE")

  h_M2.SetLineColor(1)
  h_TTM2.SetLineColor(2)
  h_TLM2.SetLineColor(3)
  h_LLM2.SetLineColor(4)
  h_AddM2.SetLineColor(5)

  # set the title of these 4 histograms
  h_M2.SetTitle("Compare M2; ZMass/GeV; events")
  h_TTM2.SetTitle("Compare M2; ZMass/GeV; events")
  h_TLM2.SetTitle("Compare M2; ZMass/GeV; events")
  h_LLM2.SetTitle("Compare M2; ZMass/GeV; events")
  h_AddM2.SetTitle("Compare M2; ZMass/GeV; events")

  # set the range of the axis
  Max1 = h_M2.GetMaximum()
  Max2 = h_TTM2.GetMaximum()
  Max3 = h_TLM2.GetMaximum()
  Max4 = h_LLM2.GetMaximum()
  Max5 = h_AddM2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_M2.SetMaximum(Max*1.2)
  h_TTM2.SetMaximum(Max*1.2)
  h_TLM2.SetMaximum(Max*1.2)
  h_LLM2.SetMaximum(Max*1.2)
  h_AddM2.SetMaximum(Max*1.2)
  h_M2.SetMinimum(0)
  h_TTM2.SetMinimum(0)
  h_TLM2.SetMinimum(0)
  h_LLM2.SetMinimum(0)
  h_AddM2.SetMinimum(0)


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
  leg.AddEntry(h_M2,"Inclusive","LE")
  leg.AddEntry(h_TTM2,"TT","LE")
  leg.AddEntry(h_TLM2,"TL","LE")
  leg.AddEntry(h_LLM2,"LL","LE")
  leg.AddEntry(h_AddM2,"TT+TL+LL","LE")
  leg.Draw()

  c_M2SumAdd.SaveAs("M2SumAdd.png")
  c_M2SumAdd.Close()


  # histogram of CosTheta1, TTCosTheta1, TLCosTheta1, LLCosTheta1, TT+TL+LLCosTheta1
  c_CosTheta1SumAdd = R.TCanvas()
  c_CosTheta1SumAdd.cd()
  c_CosTheta1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosTheta1"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta1 = R.TH1F("TT+TL+LLCosTheta1", htitle, nbins, xmin, xmax)
  h_AddCosTheta1.Add(h_TTCosTheta1, 1)
  h_AddCosTheta1.Add(h_TLCosTheta1, 1)
  h_AddCosTheta1.Add(h_LLCosTheta1, 1)

  h_CosTheta1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta1.Draw("SameLE")
  h_TLCosTheta1.Draw("SameLE")
  h_LLCosTheta1.Draw("SameLE")
  h_AddCosTheta1.Draw("SameLE")

  h_CosTheta1.SetLineColor(1)
  h_TTCosTheta1.SetLineColor(2)
  h_TLCosTheta1.SetLineColor(3)
  h_LLCosTheta1.SetLineColor(4)
  h_AddCosTheta1.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_TTCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_TLCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_LLCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")
  h_AddCosTheta1.SetTitle("Compare CosTheta1; CosTheta1; events")

  # set the range of the axis
  Max1 = h_CosTheta1.GetMaximum()
  Max2 = h_TTCosTheta1.GetMaximum()
  Max3 = h_TLCosTheta1.GetMaximum()
  Max4 = h_LLCosTheta1.GetMaximum()
  Max5 = h_AddCosTheta1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosTheta1.SetMaximum(Max*1.2)
  h_TTCosTheta1.SetMaximum(Max*1.2)
  h_TLCosTheta1.SetMaximum(Max*1.2)
  h_LLCosTheta1.SetMaximum(Max*1.2)
  h_AddCosTheta1.SetMaximum(Max*1.2)
  h_CosTheta1.SetMinimum(0)
  h_TTCosTheta1.SetMinimum(0)
  h_TLCosTheta1.SetMinimum(0)
  h_LLCosTheta1.SetMinimum(0)
  h_AddCosTheta1.SetMinimum(0)


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
  leg.AddEntry(h_CosTheta1,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta1,"TT","LE")
  leg.AddEntry(h_TLCosTheta1,"TL","LE")
  leg.AddEntry(h_LLCosTheta1,"LL","LE")
  leg.AddEntry(h_AddCosTheta1,"TT+TL+LL","LE")
  leg.Draw()

  c_CosTheta1SumAdd.SaveAs("CosTheta1SumAdd.png")
  c_CosTheta1SumAdd.Close()


  # histogram of CosTheta2, TTCosTheta2, TLCosTheta2, LLCosTheta2, TT+TL+LLCosTheta2
  c_CosTheta2SumAdd = R.TCanvas()
  c_CosTheta2SumAdd.cd()
  c_CosTheta2SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosTheta2"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta2 = R.TH1F("TT+TL+LLCosTheta2", htitle, nbins, xmin, xmax)
  h_AddCosTheta2.Add(h_TTCosTheta2, 1)
  h_AddCosTheta2.Add(h_TLCosTheta2, 1)
  h_AddCosTheta2.Add(h_LLCosTheta2, 1)

  h_CosTheta2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta2.Draw("SameLE")
  h_TLCosTheta2.Draw("SameLE")
  h_LLCosTheta2.Draw("SameLE")
  h_AddCosTheta2.Draw("SameLE")

  h_CosTheta2.SetLineColor(1)
  h_TTCosTheta2.SetLineColor(2)
  h_TLCosTheta2.SetLineColor(3)
  h_LLCosTheta2.SetLineColor(4)
  h_AddCosTheta2.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_TTCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_TLCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_LLCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")
  h_AddCosTheta2.SetTitle("Compare CosTheta2; CosTheta2; events")

  # set the range of the axis
  Max1 = h_CosTheta2.GetMaximum()
  Max2 = h_TTCosTheta2.GetMaximum()
  Max3 = h_TLCosTheta2.GetMaximum()
  Max4 = h_LLCosTheta2.GetMaximum()
  Max5 = h_AddCosTheta2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosTheta2.SetMaximum(Max*1.2)
  h_TTCosTheta2.SetMaximum(Max*1.2)
  h_TLCosTheta2.SetMaximum(Max*1.2)
  h_LLCosTheta2.SetMaximum(Max*1.2)
  h_AddCosTheta2.SetMaximum(Max*1.2)
  h_CosTheta2.SetMinimum(0)
  h_TTCosTheta2.SetMinimum(0)
  h_TLCosTheta2.SetMinimum(0)
  h_LLCosTheta2.SetMinimum(0)
  h_AddCosTheta2.SetMinimum(0)


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
  leg.AddEntry(h_CosTheta2,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta2,"TT","LE")
  leg.AddEntry(h_TLCosTheta2,"TL","LE")
  leg.AddEntry(h_LLCosTheta2,"LL","LE")
  leg.AddEntry(h_AddCosTheta2,"TT+TL+LL","LE")
  leg.Draw()

  c_CosTheta2SumAdd.SaveAs("CosTheta2SumAdd.png")
  c_CosTheta2SumAdd.Close()


  # histogram of CosTheta3, TTCosTheta3, TLCosTheta3, LLCosTheta3, TT+TL+LLCosTheta3
  c_CosTheta3SumAdd = R.TCanvas()
  c_CosTheta3SumAdd.cd()
  c_CosTheta3SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosTheta3"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta3 = R.TH1F("TT+TL+LLCosTheta3", htitle, nbins, xmin, xmax)
  h_AddCosTheta3.Add(h_TTCosTheta3, 1)
  h_AddCosTheta3.Add(h_TLCosTheta3, 1)
  h_AddCosTheta3.Add(h_LLCosTheta3, 1)

  h_CosTheta3.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta3.Draw("SameLE")
  h_TLCosTheta3.Draw("SameLE")
  h_LLCosTheta3.Draw("SameLE")
  h_AddCosTheta3.Draw("SameLE")

  h_CosTheta3.SetLineColor(1)
  h_TTCosTheta3.SetLineColor(2)
  h_TLCosTheta3.SetLineColor(3)
  h_LLCosTheta3.SetLineColor(4)
  h_AddCosTheta3.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_TTCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_TLCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_LLCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")
  h_AddCosTheta3.SetTitle("Compare CosTheta3; CosTheta3; events")

  # set the range of the axis
  Max1 = h_CosTheta3.GetMaximum()
  Max2 = h_TTCosTheta3.GetMaximum()
  Max3 = h_TLCosTheta3.GetMaximum()
  Max4 = h_LLCosTheta3.GetMaximum()
  Max5 = h_AddCosTheta3.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosTheta3.SetMaximum(Max*1.2)
  h_TTCosTheta3.SetMaximum(Max*1.2)
  h_TLCosTheta3.SetMaximum(Max*1.2)
  h_LLCosTheta3.SetMaximum(Max*1.2)
  h_AddCosTheta3.SetMaximum(Max*1.2)
  h_CosTheta3.SetMinimum(0)
  h_TTCosTheta3.SetMinimum(0)
  h_TLCosTheta3.SetMinimum(0)
  h_LLCosTheta3.SetMinimum(0)
  h_AddCosTheta3.SetMinimum(0)


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
  leg.AddEntry(h_CosTheta3,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta3,"TT","LE")
  leg.AddEntry(h_TLCosTheta3,"TL","LE")
  leg.AddEntry(h_LLCosTheta3,"LL","LE")
  leg.AddEntry(h_AddCosTheta3,"TT+TL+LL","LE")
  leg.Draw()

  c_CosTheta3SumAdd.SaveAs("CosTheta3SumAdd.png")
  c_CosTheta3SumAdd.Close()


  # histogram of CosTheta4, TTCosTheta4, TLCosTheta4, LLCosTheta4, TT+TL+LLCosTheta4
  c_CosTheta4SumAdd = R.TCanvas()
  c_CosTheta4SumAdd.cd()
  c_CosTheta4SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosTheta4"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta4 = R.TH1F("TT+TL+LLCosTheta4", htitle, nbins, xmin, xmax)
  h_AddCosTheta4.Add(h_TTCosTheta4, 1)
  h_AddCosTheta4.Add(h_TLCosTheta4, 1)
  h_AddCosTheta4.Add(h_LLCosTheta4, 1)

  h_CosTheta4.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosTheta4.Draw("SameLE")
  h_TLCosTheta4.Draw("SameLE")
  h_LLCosTheta4.Draw("SameLE")
  h_AddCosTheta4.Draw("SameLE")

  h_CosTheta4.SetLineColor(1)
  h_TTCosTheta4.SetLineColor(2)
  h_TLCosTheta4.SetLineColor(3)
  h_LLCosTheta4.SetLineColor(4)
  h_AddCosTheta4.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_TTCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_TLCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_LLCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")
  h_AddCosTheta4.SetTitle("Compare CosTheta4; CosTheta4; events")

  # set the range of the axis
  Max1 = h_CosTheta4.GetMaximum()
  Max2 = h_TTCosTheta4.GetMaximum()
  Max3 = h_TLCosTheta4.GetMaximum()
  Max4 = h_LLCosTheta4.GetMaximum()
  Max5 = h_AddCosTheta4.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosTheta4.SetMaximum(Max*1.2)
  h_TTCosTheta4.SetMaximum(Max*1.2)
  h_TLCosTheta4.SetMaximum(Max*1.2)
  h_LLCosTheta4.SetMaximum(Max*1.2)
  h_AddCosTheta4.SetMaximum(Max*1.2)
  h_CosTheta4.SetMinimum(0)
  h_TTCosTheta4.SetMinimum(0)
  h_TLCosTheta4.SetMinimum(0)
  h_LLCosTheta4.SetMinimum(0)
  h_AddCosTheta4.SetMinimum(0)


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
  leg.AddEntry(h_CosTheta4,"Inclusive","LE")
  leg.AddEntry(h_TTCosTheta4,"TT","LE")
  leg.AddEntry(h_TLCosTheta4,"TL","LE")
  leg.AddEntry(h_LLCosTheta4,"LL","LE")
  leg.AddEntry(h_AddCosTheta4,"TT+TL+LL","LE")
  leg.Draw()

  c_CosTheta4SumAdd.SaveAs("CosTheta4SumAdd.png")
  c_CosTheta4SumAdd.Close()



  # histogram of ThetaStar1, TTThetaStar1, TLThetaStar1, LLThetaStar1, TT+TL+LLThetaStar1
  c_ThetaStar1SumAdd = R.TCanvas()
  c_ThetaStar1SumAdd.cd()
  c_ThetaStar1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLThetaStar1"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_AddThetaStar1 = R.TH1F("TT+TL+LLThetaStar1", htitle, nbins, xmin, xmax)
  h_AddThetaStar1.Add(h_TTThetaStar1, 1)
  h_AddThetaStar1.Add(h_TLThetaStar1, 1)
  h_AddThetaStar1.Add(h_LLThetaStar1, 1)

  h_ThetaStar1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTThetaStar1.Draw("SameLE")
  h_TLThetaStar1.Draw("SameLE")
  h_LLThetaStar1.Draw("SameLE")
  h_AddThetaStar1.Draw("SameLE")

  h_ThetaStar1.SetLineColor(1)
  h_TTThetaStar1.SetLineColor(2)
  h_TLThetaStar1.SetLineColor(3)
  h_LLThetaStar1.SetLineColor(4)
  h_AddThetaStar1.SetLineColor(5)

  # set the title of these 4 histograms
  h_ThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_TTThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_TLThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_LLThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")
  h_AddThetaStar1.SetTitle("Compare ThetaStar1; ThetaStar1; events")

  # set the range of the axis
  Max1 = h_ThetaStar1.GetMaximum()
  Max2 = h_TTThetaStar1.GetMaximum()
  Max3 = h_TLThetaStar1.GetMaximum()
  Max4 = h_LLThetaStar1.GetMaximum()
  Max5 = h_AddThetaStar1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_ThetaStar1.SetMaximum(Max*1.2)
  h_TTThetaStar1.SetMaximum(Max*1.2)
  h_TLThetaStar1.SetMaximum(Max*1.2)
  h_LLThetaStar1.SetMaximum(Max*1.2)
  h_AddThetaStar1.SetMaximum(Max*1.2)
  h_ThetaStar1.SetMinimum(0)
  h_TTThetaStar1.SetMinimum(0)
  h_TLThetaStar1.SetMinimum(0)
  h_LLThetaStar1.SetMinimum(0)
  h_AddThetaStar1.SetMinimum(0)


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
  leg.AddEntry(h_ThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar1,"TT","LE")
  leg.AddEntry(h_TLThetaStar1,"TL","LE")
  leg.AddEntry(h_LLThetaStar1,"LL","LE")
  leg.AddEntry(h_AddThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  c_ThetaStar1SumAdd.SaveAs("ThetaStar1SumAdd.png")
  c_ThetaStar1SumAdd.Close()


  # histogram of ThetaStar2, TTThetaStar2, TLThetaStar2, LLThetaStar2, TT+TL+LLThetaStar2
  c_ThetaStar2SumAdd = R.TCanvas()
  c_ThetaStar2SumAdd.cd()
  c_ThetaStar2SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLThetaStar2"
  nbins, xmin, xmax = 40, -R.TMath.Pi(), R.TMath.Pi()
  h_AddThetaStar2 = R.TH1F("TT+TL+LLThetaStar2", htitle, nbins, xmin, xmax)
  h_AddThetaStar2.Add(h_TTThetaStar2, 1)
  h_AddThetaStar2.Add(h_TLThetaStar2, 1)
  h_AddThetaStar2.Add(h_LLThetaStar2, 1)

  h_ThetaStar2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTThetaStar2.Draw("SameLE")
  h_TLThetaStar2.Draw("SameLE")
  h_LLThetaStar2.Draw("SameLE")
  h_AddThetaStar2.Draw("SameLE")

  h_ThetaStar2.SetLineColor(1)
  h_TTThetaStar2.SetLineColor(2)
  h_TLThetaStar2.SetLineColor(3)
  h_LLThetaStar2.SetLineColor(4)
  h_AddThetaStar2.SetLineColor(5)

  # set the title of these 4 histograms
  h_ThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_TTThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_TLThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_LLThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")
  h_AddThetaStar2.SetTitle("Compare ThetaStar2; ThetaStar2; events")

  # set the range of the axis
  Max1 = h_ThetaStar2.GetMaximum()
  Max2 = h_TTThetaStar2.GetMaximum()
  Max3 = h_TLThetaStar2.GetMaximum()
  Max4 = h_LLThetaStar2.GetMaximum()
  Max5 = h_AddThetaStar2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_ThetaStar2.SetMaximum(Max*1.2)
  h_TTThetaStar2.SetMaximum(Max*1.2)
  h_TLThetaStar2.SetMaximum(Max*1.2)
  h_LLThetaStar2.SetMaximum(Max*1.2)
  h_AddThetaStar2.SetMaximum(Max*1.2)
  h_ThetaStar2.SetMinimum(0)
  h_TTThetaStar2.SetMinimum(0)
  h_TLThetaStar2.SetMinimum(0)
  h_LLThetaStar2.SetMinimum(0)
  h_AddThetaStar2.SetMinimum(0)


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
  leg.AddEntry(h_ThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTThetaStar2,"TT","LE")
  leg.AddEntry(h_TLThetaStar2,"TL","LE")
  leg.AddEntry(h_LLThetaStar2,"LL","LE")
  leg.AddEntry(h_AddThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  c_ThetaStar2SumAdd.SaveAs("ThetaStar2SumAdd.png")
  c_ThetaStar2SumAdd.Close()



  # histogram of CosThetaStar1, TTCosThetaStar1, TLCosThetaStar1, LLCosThetaStar1, TT+TL+LLCosThetaStar1
  c_CosThetaStar1SumAdd = R.TCanvas()
  c_CosThetaStar1SumAdd.cd()
  c_CosThetaStar1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosThetaStar1"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosThetaStar1 = R.TH1F("TT+TL+LLCosThetaStar1", htitle, nbins, xmin, xmax)
  h_AddCosThetaStar1.Add(h_TTCosThetaStar1, 1)
  h_AddCosThetaStar1.Add(h_TLCosThetaStar1, 1)
  h_AddCosThetaStar1.Add(h_LLCosThetaStar1, 1)

  h_CosThetaStar1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosThetaStar1.Draw("SameLE")
  h_TLCosThetaStar1.Draw("SameLE")
  h_LLCosThetaStar1.Draw("SameLE")
  h_AddCosThetaStar1.Draw("SameLE")

  h_CosThetaStar1.SetLineColor(1)
  h_TTCosThetaStar1.SetLineColor(2)
  h_TLCosThetaStar1.SetLineColor(3)
  h_LLCosThetaStar1.SetLineColor(4)
  h_AddCosThetaStar1.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_TTCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_TLCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_LLCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")
  h_AddCosThetaStar1.SetTitle("Compare CosThetaStar1; CosThetaStar1; events")

  # set the range of the axis
  Max1 = h_CosThetaStar1.GetMaximum()
  Max2 = h_TTCosThetaStar1.GetMaximum()
  Max3 = h_TLCosThetaStar1.GetMaximum()
  Max4 = h_LLCosThetaStar1.GetMaximum()
  Max5 = h_AddCosThetaStar1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosThetaStar1.SetMaximum(Max*1.2)
  h_TTCosThetaStar1.SetMaximum(Max*1.2)
  h_TLCosThetaStar1.SetMaximum(Max*1.2)
  h_LLCosThetaStar1.SetMaximum(Max*1.2)
  h_AddCosThetaStar1.SetMaximum(Max*1.2)
  h_CosThetaStar1.SetMinimum(0)
  h_TTCosThetaStar1.SetMinimum(0)
  h_TLCosThetaStar1.SetMinimum(0)
  h_LLCosThetaStar1.SetMinimum(0)
  h_AddCosThetaStar1.SetMinimum(0)


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
  leg.AddEntry(h_CosThetaStar1,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar1,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar1,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar1,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar1,"TT+TL+LL","LE")
  leg.Draw()

  c_CosThetaStar1SumAdd.SaveAs("CosThetaStar1SumAdd.png")
  c_CosThetaStar1SumAdd.Close()


  # histogram of CosThetaStar2, TTCosThetaStar2, TLCosThetaStar2, LLCosThetaStar2, TT+TL+LLCosThetaStar2
  c_CosThetaStar2SumAdd = R.TCanvas()
  c_CosThetaStar2SumAdd.cd()
  c_CosThetaStar2SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosThetaStar2"
  nbins, xmin, xmax = 40, -1, 1
  h_AddCosThetaStar2 = R.TH1F("TT+TL+LLCosThetaStar2", htitle, nbins, xmin, xmax)
  h_AddCosThetaStar2.Add(h_TTCosThetaStar2, 1)
  h_AddCosThetaStar2.Add(h_TLCosThetaStar2, 1)
  h_AddCosThetaStar2.Add(h_LLCosThetaStar2, 1)

  h_CosThetaStar2.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosThetaStar2.Draw("SameLE")
  h_TLCosThetaStar2.Draw("SameLE")
  h_LLCosThetaStar2.Draw("SameLE")
  h_AddCosThetaStar2.Draw("SameLE")

  h_CosThetaStar2.SetLineColor(1)
  h_TTCosThetaStar2.SetLineColor(2)
  h_TLCosThetaStar2.SetLineColor(3)
  h_LLCosThetaStar2.SetLineColor(4)
  h_AddCosThetaStar2.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_TTCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_TLCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_LLCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")
  h_AddCosThetaStar2.SetTitle("Compare CosThetaStar2; CosThetaStar2; events")

  # set the range of the axis
  Max1 = h_CosThetaStar2.GetMaximum()
  Max2 = h_TTCosThetaStar2.GetMaximum()
  Max3 = h_TLCosThetaStar2.GetMaximum()
  Max4 = h_LLCosThetaStar2.GetMaximum()
  Max5 = h_AddCosThetaStar2.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosThetaStar2.SetMaximum(Max*1.2)
  h_TTCosThetaStar2.SetMaximum(Max*1.2)
  h_TLCosThetaStar2.SetMaximum(Max*1.2)
  h_LLCosThetaStar2.SetMaximum(Max*1.2)
  h_AddCosThetaStar2.SetMaximum(Max*1.2)
  h_CosThetaStar2.SetMinimum(0)
  h_TTCosThetaStar2.SetMinimum(0)
  h_TLCosThetaStar2.SetMinimum(0)
  h_LLCosThetaStar2.SetMinimum(0)
  h_AddCosThetaStar2.SetMinimum(0)


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
  leg.AddEntry(h_CosThetaStar2,"Inclusive","LE")
  leg.AddEntry(h_TTCosThetaStar2,"TT","LE")
  leg.AddEntry(h_TLCosThetaStar2,"TL","LE")
  leg.AddEntry(h_LLCosThetaStar2,"LL","LE")
  leg.AddEntry(h_AddCosThetaStar2,"TT+TL+LL","LE")
  leg.Draw()

  c_CosThetaStar2SumAdd.SaveAs("CosThetaStar2SumAdd.png")
  c_CosThetaStar2SumAdd.Close()


  # histogram of Phi, TTPhi, TLPhi, LLPhi, TT+TL+LLPhi
  c_PhiSumAdd = R.TCanvas()
  c_PhiSumAdd.cd()
  c_PhiSumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLPhi"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_AddPhi = R.TH1F("TT+TL+LLPhi", htitle, nbins, xmin, xmax)
  h_AddPhi.Add(h_TTPhi, 1)
  h_AddPhi.Add(h_TLPhi, 1)
  h_AddPhi.Add(h_LLPhi, 1)

  h_Phi.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTPhi.Draw("SameLE")
  h_TLPhi.Draw("SameLE")
  h_LLPhi.Draw("SameLE")
  h_AddPhi.Draw("SameLE")

  h_Phi.SetLineColor(1)
  h_TTPhi.SetLineColor(2)
  h_TLPhi.SetLineColor(3)
  h_LLPhi.SetLineColor(4)
  h_AddPhi.SetLineColor(5)

  # set the title of these 4 histograms
  h_Phi.SetTitle("Compare Phi; Phi; events")
  h_TTPhi.SetTitle("Compare Phi; Phi; events")
  h_TLPhi.SetTitle("Compare Phi; Phi; events")
  h_LLPhi.SetTitle("Compare Phi; Phi; events")
  h_AddPhi.SetTitle("Compare Phi; Phi; events")

  # set the range of the axis
  Max1 = h_Phi.GetMaximum()
  Max2 = h_TTPhi.GetMaximum()
  Max3 = h_TLPhi.GetMaximum()
  Max4 = h_LLPhi.GetMaximum()
  Max5 = h_AddPhi.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_Phi.SetMaximum(Max*1.2)
  h_TTPhi.SetMaximum(Max*1.2)
  h_TLPhi.SetMaximum(Max*1.2)
  h_LLPhi.SetMaximum(Max*1.2)
  h_AddPhi.SetMaximum(Max*1.2)
  h_Phi.SetMinimum(0)
  h_TTPhi.SetMinimum(0)
  h_TLPhi.SetMinimum(0)
  h_LLPhi.SetMinimum(0)
  h_AddPhi.SetMinimum(0)

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
  leg.AddEntry(h_Phi,"Inclusive","LE")
  leg.AddEntry(h_TTPhi,"TT","LE")
  leg.AddEntry(h_TLPhi,"TL","LE")
  leg.AddEntry(h_LLPhi,"LL","LE")
  leg.AddEntry(h_AddPhi,"TT+TL+LL","LE")
  leg.Draw()

  c_PhiSumAdd.SaveAs("PhiSumAdd.png")
  c_PhiSumAdd.Close()


  # histogram of CosPhi, TTCosPhi, TLCosPhi, LLCosPhi, TT+TL+LLCosPhi
  c_CosPhiSumAdd = R.TCanvas()
  c_CosPhiSumAdd.cd()
  c_CosPhiSumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosPhi"
  nbins, xmin, xmax = 40, 0, 1
  h_AddCosPhi = R.TH1F("TT+TL+LLCosPhi", htitle, nbins, xmin, xmax)
  h_AddCosPhi.Add(h_TTCosPhi, 1)
  h_AddCosPhi.Add(h_TLCosPhi, 1)
  h_AddCosPhi.Add(h_LLCosPhi, 1)

  h_CosPhi.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosPhi.Draw("SameLE")
  h_TLCosPhi.Draw("SameLE")
  h_LLCosPhi.Draw("SameLE")
  h_AddCosPhi.Draw("SameLE")

  h_CosPhi.SetLineColor(1)
  h_TTCosPhi.SetLineColor(2)
  h_TLCosPhi.SetLineColor(3)
  h_LLCosPhi.SetLineColor(4)
  h_AddCosPhi.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_TTCosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_TLCosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_LLCosPhi.SetTitle("Compare CosPhi; CosPhi; events")
  h_AddCosPhi.SetTitle("Compare CosPhi; CosPhi; events")

  # set the range of the axis
  Max1 = h_CosPhi.GetMaximum()
  Max2 = h_TTCosPhi.GetMaximum()
  Max3 = h_TLCosPhi.GetMaximum()
  Max4 = h_LLCosPhi.GetMaximum()
  Max5 = h_AddCosPhi.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosPhi.SetMaximum(Max*1.2)
  h_TTCosPhi.SetMaximum(Max*1.2)
  h_TLCosPhi.SetMaximum(Max*1.2)
  h_LLCosPhi.SetMaximum(Max*1.2)
  h_AddCosPhi.SetMaximum(Max*1.2)
  h_CosPhi.SetMinimum(0)
  h_TTCosPhi.SetMinimum(0)
  h_TLCosPhi.SetMinimum(0)
  h_LLCosPhi.SetMinimum(0)
  h_AddCosPhi.SetMinimum(0)

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
  leg.AddEntry(h_CosPhi,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi,"TT","LE")
  leg.AddEntry(h_TLCosPhi,"TL","LE")
  leg.AddEntry(h_LLCosPhi,"LL","LE")
  leg.AddEntry(h_AddCosPhi,"TT+TL+LL","LE")
  leg.Draw()

  c_CosPhiSumAdd.SaveAs("CosPhiSumAdd.png")
  c_CosPhiSumAdd.Close()


  # histogram of Phi1, TTPhi1, TLPhi1, LLPhi1, TT+TL+LLPhi1
  c_Phi1SumAdd = R.TCanvas()
  c_Phi1SumAdd.cd()
  c_Phi1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLPhi1"
  nbins, xmin, xmax = 40, 0, R.TMath.PiOver2()
  h_AddPhi1 = R.TH1F("TT+TL+LLPhi1", htitle, nbins, xmin, xmax)
  h_AddPhi1.Add(h_TTPhi1, 1)
  h_AddPhi1.Add(h_TLPhi1, 1)
  h_AddPhi1.Add(h_LLPhi1, 1)

  h_Phi1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTPhi1.Draw("SameLE")
  h_TLPhi1.Draw("SameLE")
  h_LLPhi1.Draw("SameLE")
  h_AddPhi1.Draw("SameLE")

  h_Phi1.SetLineColor(1)
  h_TTPhi1.SetLineColor(2)
  h_TLPhi1.SetLineColor(3)
  h_LLPhi1.SetLineColor(4)
  h_AddPhi1.SetLineColor(5)

  # set the title of these 4 histograms
  h_Phi1.SetTitle("Compare Phi1; Phi1; events")
  h_TTPhi1.SetTitle("Compare Phi1; Phi1; events")
  h_TLPhi1.SetTitle("Compare Phi1; Phi1; events")
  h_LLPhi1.SetTitle("Compare Phi1; Phi1; events")
  h_AddPhi1.SetTitle("Compare Phi1; Phi1; events")

  # set the range of the axis
  Max1 = h_Phi1.GetMaximum()
  Max2 = h_TTPhi1.GetMaximum()
  Max3 = h_TLPhi1.GetMaximum()
  Max4 = h_LLPhi1.GetMaximum()
  Max5 = h_AddPhi1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_Phi1.SetMaximum(Max*1.2)
  h_TTPhi1.SetMaximum(Max*1.2)
  h_TLPhi1.SetMaximum(Max*1.2)
  h_LLPhi1.SetMaximum(Max*1.2)
  h_AddPhi1.SetMaximum(Max*1.2)
  h_Phi1.SetMinimum(0)
  h_TTPhi1.SetMinimum(0)
  h_TLPhi1.SetMinimum(0)
  h_LLPhi1.SetMinimum(0)
  h_AddPhi1.SetMinimum(0)

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
  leg.AddEntry(h_Phi1,"Inclusive","LE")
  leg.AddEntry(h_TTPhi1,"TT","LE")
  leg.AddEntry(h_TLPhi1,"TL","LE")
  leg.AddEntry(h_LLPhi1,"LL","LE")
  leg.AddEntry(h_AddPhi1,"TT+TL+LL","LE")
  leg.Draw()

  c_Phi1SumAdd.SaveAs("Phi1SumAdd.png")
  c_Phi1SumAdd.Close()


  # histogram of CosPhi1, TTCosPhi1, TLCosPhi1, LLCosPhi1, TT+TL+LLCosPhi1
  c_CosPhi1SumAdd = R.TCanvas()
  c_CosPhi1SumAdd.cd()
  c_CosPhi1SumAdd.SetFillColor(0)
  # create a histogram to save the TT+TL+LL
  htitle = "TT+TL+LLCosPhi1"
  nbins, xmin, xmax = 40, 0, 1
  h_AddCosPhi1 = R.TH1F("TT+TL+LLCosPhi1", htitle, nbins, xmin, xmax)
  h_AddCosPhi1.Add(h_TTCosPhi1, 1)
  h_AddCosPhi1.Add(h_TLCosPhi1, 1)
  h_AddCosPhi1.Add(h_LLCosPhi1, 1)

  h_CosPhi1.Draw("LE")
  # plot the other histogram in the same Canvas
  h_TTCosPhi1.Draw("SameLE")
  h_TLCosPhi1.Draw("SameLE")
  h_LLCosPhi1.Draw("SameLE")
  h_AddCosPhi1.Draw("SameLE")

  h_CosPhi1.SetLineColor(1)
  h_TTCosPhi1.SetLineColor(2)
  h_TLCosPhi1.SetLineColor(3)
  h_LLCosPhi1.SetLineColor(4)
  h_AddCosPhi1.SetLineColor(5)

  # set the title of these 4 histograms
  h_CosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_TTCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_TLCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_LLCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")
  h_AddCosPhi1.SetTitle("Compare CosPhi1; CosPhi1; events")

  # set the range of the axis
  Max1 = h_CosPhi1.GetMaximum()
  Max2 = h_TTCosPhi1.GetMaximum()
  Max3 = h_TLCosPhi1.GetMaximum()
  Max4 = h_LLCosPhi1.GetMaximum()
  Max5 = h_AddCosPhi1.GetMaximum()
  Max = max(Max1, Max2, Max3, Max4, Max5)
  h_CosPhi1.SetMaximum(Max*1.2)
  h_TTCosPhi1.SetMaximum(Max*1.2)
  h_TLCosPhi1.SetMaximum(Max*1.2)
  h_LLCosPhi1.SetMaximum(Max*1.2)
  h_AddCosPhi1.SetMaximum(Max*1.2)
  h_CosPhi1.SetMinimum(0)
  h_TTCosPhi1.SetMinimum(0)
  h_TLCosPhi1.SetMinimum(0)
  h_LLCosPhi1.SetMinimum(0)
  h_AddCosPhi1.SetMinimum(0)

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
  leg.AddEntry(h_CosPhi1,"Inclusive","LE")
  leg.AddEntry(h_TTCosPhi1,"TT","LE")
  leg.AddEntry(h_TLCosPhi1,"TL","LE")
  leg.AddEntry(h_LLCosPhi1,"LL","LE")
  leg.AddEntry(h_AddCosPhi1,"TT+TL+LL","LE")
  leg.Draw()

  c_CosPhi1SumAdd.SaveAs("CosPhi1SumAdd.png")
  c_CosPhi1SumAdd.Close()

  rootfile.Close()



if __name__ == "__main__":

  InputROOTFile="Angle_v3.root"
  plot(InputROOTFile)

