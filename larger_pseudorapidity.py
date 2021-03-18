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
      etaabs = 0 
      etalarger = 0

      for particle in event:
          if particle.status == 1:
              p = FourMomentum(particle)
              eta = p.pseudorapidity
              if abs(eta) > etaabs:
                  etalarger = eta
                  etaabs = abs(eta)
      nb_pass +=1

      data.append(etalarger)

  print (data)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "larger_pseudorapidity"
  nbins, xmin, xmax = 100, -5, 5
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("larger_pseudorapidity between 2 final state particles;pseudorapidity;count")
  for i, eta in enumerate(data):
    h1.Fill(eta)
  h1.Draw()

  leg = R.TLegend(0.1,0.7,0.29,0.9)
  leg.SetHeader("larger_pseudorapidity","C")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()


  myC.SaveAs("larger_pseudorapidity.png")

  tfout = R.TFile("larger_pseudorapidity.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)


