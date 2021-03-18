#!/usr/bin/env python

# import some modules
import sys, os
sys.path.append("/users/wuxingyu/MG5_aMC/")
from madgraph.various.lhe_parser import *
import ROOT as R


# define a function named "read_lhe", its input is "input_file"
def read_lhe(input_file):
  # use Class EventFile defined in the lhe_parser.py to read the usage information in the LHE files
  lhe = EventFile(input_file)

  # define some initial values before the loop
  # define a empty list to save data
  data_invariant_mass = []

  # loop the events
  for event in lhe:
      #define some initial values in the loop

      # define a initial value to save the total TLorentzVector
      T_total = R.TLorentzVector()
      # define a empty list to save the TLorentzVector of each particles
      # it can't be defined out of the event, or it's member will add up to 2, 4, ...etc
      T = []
      # define "particle_count" to count the particles, so that we can draw the histograms when particle_counts beyond 2.
      particle_count = 0


      # loop the particles in each events
      for particle in event:
          # distinguish the final state particles
          if particle.status == 1:
              # create an empty TLorentzVector class for each selected particles
              T.append(R.TLorentzVector())
              # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
              p = FourMomentum(particle)
              # pick out the px, py, pz and E
              px = p.px
              py = p.py
              pz = p.pz
              E = p.E
              # assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
              T[particle_count].SetPxPyPzE(px, py, pz, E)
              # sum the TLorentzVector
              T_total += T[particle_count]
              # prepare to the next loop
              particle_count += 1


      """
      calculate the invariant mass of the sum of final status particles
      """
      m = T_total.M()
      # save the data
      data_invariant_mass.append(m)


  # print out the data in the terminal
  print (data_invariant_mass)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "invariant_mass"
  nbins, xmin, xmax = 1000, 0, 10000
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("invariant_mass;invariant_mass;count")
  for i, d in enumerate(data_invariant_mass):
    h1.Fill(d)
  h1.Draw()

  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("invariant_mass","C")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()


  myC.SaveAs("invariant_mass.png")


  tfout = R.TFile("sum.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)



