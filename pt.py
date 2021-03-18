#!/usr/bin/env python

import subprocess
subprocess.call("source /users/wuxingyu/root/bin/thisroot.sh",shell=True)

import sys, os
sys.path.append("/users/wuxingyu/MG5_aMC/")
from madgraph.various.lhe_parser import *
import ROOT as R


def read_lhe(input_file):
  lhe = EventFile(input_file)


  nb_pass = 0
  data = []
  for event in lhe:
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      for particle in event:
          if particle.status == 1:
              p = FourMomentum(particle)
              pt_square = p.pt2
              pt = math.sqrt(pt_square)
              data.append(pt)
              nb_pass +=1
              if abs(pt) > ptmax_middle:
                  ptmax = abs(pt)
                  ptmax_middle = ptmax
              if abs(pt) < ptmin_middle:
                  ptmin = abs(pt)
                  ptmin_middle = ptmin



  print (data)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "pt"
  nbins, xmin, xmax = 100, ptmin, ptmax
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("pt;pt/GeV;count")
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Draw()
  
  leg = R.TLegend(0.4,0.7,0.6,0.8)
  leg.SetHeader("pt","C")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()

  myC.SaveAs("pt.png")

  tfout = R.TFile("pt.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)




