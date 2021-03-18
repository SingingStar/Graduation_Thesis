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

  """
  定义初始化的T1，T2时应该在它所在的循环定义,use english
  """


  T1 = (0, 0, 0, 0)
  T2 = (0, 0, 0, 0)
  for event in lhe:
      for particle in event:
          TLorentzVector = R.TLorentzVector()
          if particle.status == 1:
              if particle.color1 == 0:
                  p = FourMomentum(particle)
                  px = p.px
                  py = p.py
                  pz = p.pz
                  E = p.E
                  T1 = TLorentzVector(px, py, pz, E)
              else:
                  p=FourMomentum(particle)
                  px = p.px
                  py = p.py
                  pz = p.pz
                  E = p.E
                  T2 = TLorentzVector(px, py, pz, E)
          d = T1.TLorentzVector.DeltaR(T2)
      data.append(d)
      nb_pass +=1



  print (data)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "deltaR"
  nbins, xmin, xmax = 100, -100, 100
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("deltaR;deltaR;count")
  for i, d in enumerate(data):
    h1.Fill(d)
  h1.Draw()
  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("deltaR","C")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()

  myC.SaveAs("deltaR.png")

  tfout = R.TFile("deltaR.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)
