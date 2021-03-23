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
  h_CosTheta1 = rootfile.Get("CosTheta1")
  h_CosTheta2 = rootfile.Get("CosTheta2")
  h_CosTheta3 = rootfile.Get("CosTheta3")
  h_CosTheta4 = rootfile.Get("CosTheta4")

  """
  Plotting
  """

  # histogram of CosTheta1
  c_CosTheta1 = R.TCanvas()
  c_CosTheta1.cd()
  # function SetFillColor is used to set the color of background, "0" represents white, "1" represents black, "2" represents red, "3" represents green.
  c_CosTheta1.SetFillColor(0)
  h_CosTheta1.Draw()
  # set the color of line, "0", "1", "2", "3" have the same meaning as SetFillColor.
  h_CosTheta1.SetLineColor(1)
  # save the histogram as png
  c_CosTheta1.SaveAs("CosTheta1.png")

  # histogram of CosTheta2
  c_CosTheta2 = R.TCanvas()
  c_CosTheta2.cd()
  c_CosTheta2.SetFillColor(0)
  h_CosTheta2.Draw()
  h_CosTheta2.SetLineColor(1)
  c_CosTheta2.SaveAs("CosTheta2.png")

  # histogram of CosTheta3
  c_CosTheta3 = R.TCanvas()
  c_CosTheta3.cd()
  c_CosTheta3.SetFillColor(0)
  h_CosTheta3.Draw()
  h_CosTheta3.SetLineColor(1)
  c_CosTheta3.SaveAs("CosTheta3.png")

  # histogram of CosTheta4
  c_CosTheta4 = R.TCanvas()
  c_CosTheta4.cd()
  c_CosTheta4.SetFillColor(0)
  h_CosTheta4.Draw()
  h_CosTheta4.SetLineColor(1)
  c_CosTheta4.SaveAs("CosTheta4.png")


  rootfile.Close()

if __name__ == "__main__":

  input_root_file="CosTheta.root"
  plot(input_root_file)

