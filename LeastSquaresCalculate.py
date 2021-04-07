#!/usr/bin/env python

# import some modules
import sys, os, math
# import ROOT, creat an alias
import ROOT as R

def plot(InputROOTFile):

  rootfile = R.TFile.Open(InputROOTFile)

  # loop all objects of the root file and print them
  for key in rootfile.GetListOfKeys():
    key.Print()

  h_CosTheta1 = rootfile.Get("CosTheta1")
  h_TTCosTheta1 = rootfile.Get("TTCosTheta1")
  h_TLCosTheta1 = rootfile.Get("TLCosTheta1")
  h_LLCosTheta1 = rootfile.Get("LLCosTheta1")

  h_CosTheta1.Scale(0.02419*139*1000/20000)
  h_TTCosTheta1.Scale(0.01688*139*1000/20000)
  h_TLCosTheta1.Scale(0.005741*139*1000/20000)
  h_LLCosTheta1.Scale(0.001406*139*1000/20000)

  nbins, xmin, xmax = 40, -1, 1
  h_AddCosTheta1 = R.TH1F("TT+TL+LLCosTheta1", "", nbins, xmin, xmax)
  h_AddCosTheta1.Add(h_TTCosTheta1, 1)
  h_AddCosTheta1.Add(h_TLCosTheta1, 1)
  h_AddCosTheta1.Add(h_LLCosTheta1, 1)

  # XT and YT means these X and Y are calculated by theory.
  ListYT = []
  ListXT = []
  ListX = []
  ListY = []
  ListInclusive = []
  XT2sum = 0
  XTYTsum = 0
  YminusYbar2sum = 0

  for i in range(1, 41):
      N_LL = h_LLCosTheta1.GetBinContent(i)
      N_Add = h_AddCosTheta1.GetBinContent(i)
      XT = N_LL/N_Add
      YT = N_Add
      ListXT.append(XT)
      ListYT.append(YT)

  # Least Squares Method
  XTbar = sum(ListXT)/40
  YTbar = sum(ListYT)/40
  for XT in ListXT:
      XT2sum += XT*XT
  XT2bar = XT2sum/40
  for i in range(0, 40):
      XTYTsum += ListXT[i]*ListYT[i]
  XTYTbar = XTYTsum/40

  k = (XTYTbar - XTbar*YTbar)/(XT2bar - XTbar*XTbar)
  b = YTbar - k*XTbar
  print("k", k)
  print("b", b)
  print("XTbar", XTbar)

  for i in range(1, 41):
      Y = h_CosTheta1.GetBinContent(i)
      ListY.append(Y)
      X = (Y - b)/k
      ListX.append(X)
  Ybar = sum(ListY)/40
  for i in range(0, 40):
      YminusYbar2sum += (ListY[i] - Ybar)*(ListY[i] - Ybar)
  uY = math.sqrt(YminusYbar2sum/(40*39))
  X = (Ybar - b)/k
  uX = uY/k
  print("X", X)
  print("uX", uX)






  # close the ROOTFile
  rootfile.Close()



if __name__ == "__main__":

  InputROOTFile="Angle_v3.root"
  plot(InputROOTFile)

