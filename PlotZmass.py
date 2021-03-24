#!/usr/bin/env python

# import some modules
import sys, os
# import ROOT, creat an alias
import ROOT as R

def plot(input_root_file):

  rootfile=R.TFile.Open(input_root_file)

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
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_M1.SetLineColor(1)
  # save the histogram as png
  c_M1.SaveAs("M1.png")
  # close the Canvas
  c_M1.Close()


  # histogram of M2
  c_M2 = R.TCanvas()
  c_M2.cd()
  c_M2.SetFillColor(0)
  h_M2.Draw("LE")
  h_M2.SetLineColor(1)
  c_M2.SaveAs("M2.png")
  c_M2.Close()


  # histogram of M1MOTHUP
  c_M1MOTHUP = R.TCanvas()
  c_M1MOTHUP.cd()
  c_M1MOTHUP.SetFillColor(0)
  h_M1MOTHUP.Draw("LE")
  h_M1MOTHUP.SetLineColor(1)
  c_M1MOTHUP.SaveAs("M1MOTHUP.png")
  c_M1MOTHUP.Close()


  # histogram of M2MOTHUP
  c_M2MOTHUP = R.TCanvas()
  c_M2MOTHUP.cd()
  c_M2MOTHUP.SetFillColor(0)
  h_M2MOTHUP.Draw("LE")
  h_M2MOTHUP.SetLineColor(1)
  c_M2MOTHUP.SaveAs("M2MOTHUP.png")
  c_M2MOTHUP.Close()


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
  h_M1.SetTitle("Compare M1 and M1MOTHUP; ZMass/GeV; Count")
  h_M1MOTHUP.SetTitle("Compare M1 and M1MOTHUP; ZMass/GeV; Count")

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.8, 0.95, 0.95)
  # set the header of the legend
  leg.SetHeader("M1 and M1MOTHUP", "c_M1_M1MOTHUP")
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_M1,"M1","l")
  leg.AddEntry(h_M1MOTHUP,"M1MOTHUP","l")
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
  h_M2.SetTitle("Compare M2 and M2MOTHUP; ZMass/GeV; Count")
  h_M2MOTHUP.SetTitle("Compare M2 and M2MOTHUP; ZMass/GeV; Count")

  leg = R.TLegend(0.7, 0.8, 0.95, 0.95)
  leg.SetHeader("M2 and M2MOTHUP", "c_M2_M2MOTHUP")
  leg.AddEntry(h_M2,"M2","l")
  leg.AddEntry(h_M2MOTHUP,"M2MOTHUP","l")
  leg.Draw()

  c_M2_M2MOTHUP.SaveAs("M2_M2MOTHUP.png")
  c_M2_M2MOTHUP.Close()

  rootfile.Close()


if __name__ == "__main__":

  input_root_file="Zmass.root"
  plot(input_root_file)

