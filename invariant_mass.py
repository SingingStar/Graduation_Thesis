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
      massmax = 0
      massmin = 200
      massmax_middle = 0
      massmin_middle = 0
      for particle in event:
          if particle.status == 1:
              p = FourMomentum(particle)
              m = p.mass
              data.append(m)
              nb_pass +=1
              if abs(m) > massmax_middle:
                  massmax = abs(m)
                  massmax_middle = massmax
              if abs(m) < massmin_middle:
                  massmin = abs(m)
                  massmin_middle = massmin


  print (data)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "invariant_mass"
  nbins, xmin, xmax = 100, massmin, massmax
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("invariant_mass;invariant_mass/GeV;count")
  for i, m in enumerate(data):
    h1.Fill(m)

  # set plotting range
  h1.GetXaxis().SetRangeUser(168, 179)
  h1.Draw()
  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("invariant_mass","C")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()

  myC.SaveAs("invariant_mass.png")

  tfout = R.TFile("invariant_mass.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)


