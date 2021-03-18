#!/usr/bin/env python

# import some modules
import sys, os
# add MG5_aMC into the path and import the lhe_parser
sys.path.append("/users/wuxingyu/MG5_aMC_v2_9_2/")
from madgraph.various.lhe_parser import *
# import ROOT, creat an alias
import ROOT as R


# define a function named "read_lhe", its input is "input_file"
def read_lhe(input_file):
  # use Class EventFile defined in the lhe_parser.py to read the usage information in the LHE files
  lhe = EventFile(input_file)


  """
  histogram of invariant mass
  """
  # define htitle = "invariant_mass", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "invariant_mass"
  nbins, xmin, xmax = 100, 0, 2000
  # "invariant_mass" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_invariant_mass = R.TH1F("invariant_mass", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_invariant_mass.SetTitle("invariant_mass;invariant_mass/Gev;count")


  """
  histogram of Pt
  """
  # define htitle = "Pt", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "Pt"
  nbins, xmin, xmax = 100, -10, 10
  h_Pt = R.TH1F("Pt", htitle, nbins, xmin, xmax)
  h_Pt.SetTitle("Pt of tt~ system;Pt/GeV;count")


  """
  histogram of E
  """
  # define htitle = "E of tt~ system", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "E of tt~ system"
  nbins, xmin, xmax = 100, 0, 4000
  h_E = R.TH1F("E", htitle, nbins, xmin, xmax)
  h_E.SetTitle("E of tt~ system;E of tt~ system/GeV;count")


  """
  histogram of the maximum pseudorapidity
  """
  # define htitle = "the maximum pseudorapidity", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "the maximum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_eta_max = R.TH1F("eta_max", htitle, nbins, xmin, xmax)
  h_eta_max.SetTitle("the maximum pseudorapidity;the maximum pseudorapidity;count")


  """
  histogram of the minimum pseudorapidity
  """
  # define htitle = "the minimum pseudorapidity", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "the minimum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_eta_min = R.TH1F("eta_min", htitle, nbins, xmin, xmax)
  h_eta_min.SetTitle("the minimum pseudorapidity;the minimum pseudorapidity;count")


  """
  histogram of the maximum rapidity
  """
  # define htitle = "the maximum rapidity", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "the maximum rapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_rap_max = R.TH1F("rap_max", htitle, nbins, xmin, xmax)
  h_rap_max.SetTitle("the maximum rapidity;the maximum rapidity;count")


  """
  histogram of the minimum rapidity
  """
  # define htitle = "the minimum rapidity", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "the minimum rapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_rap_min = R.TH1F("rap_min", htitle, nbins, xmin, xmax)
  h_rap_min.SetTitle("the minimum rapidity;the minimum rapidity;count")


  """
  histogram of the rapidity of the particle which has maximum pseudorapidity
  """
  htitle = "rapidity of the particle which has maximum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_rap_of_eta_max = R.TH1F("rap_of_eta_max", htitle, nbins, xmin, xmax)
  h_rap_of_eta_max.SetTitle("rap_of_eta_max;rap;count")
  h_rap_of_eta_max.SetLineColor(3)


  """
  histogram of the rapidity of the particle which has minimum pseudorapidity
  """
  htitle = "rapidity of the particle which has minimum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h_rap_of_eta_min = R.TH1F("rap_of_eta_min", htitle, nbins, xmin, xmax)
  h_rap_of_eta_min.SetTitle("rap_of_eta_min;rap;count")
  h_rap_of_eta_min.SetLineColor(3)



  # loop the events
  for event in lhe:

      #define some initial values in the loop

      # define an initial value to save the sum of TLorentzVector
      T_sum = R.TLorentzVector()
      # define an empty list to save the TLorentzVector of each particles
      # it can't be defined out of the event, or its member will add up to 2, 4, ...etc
      T = []
      # define an empty list to save the pseudorapidity of each particles
      eta = []
      # define an initial value to save the maximum pseudorapidity
      eta_max = 0
      # define an initial value to save the minimum pseudorapidity
      eta_min = 0
      # define an empty list to save the rapidity of each particles
      rap = []
      # define an initial value to save the maximum rapidity
      rap_max = 0
      # define an initial value to save the minimum rapidity
      rap_min = 0
      # define an initial value to save the rapidity of the maximum pseudorapidity particle
      rap_of_eta_max  = 0
      # define an initial value to save the rapidity of the minimum pseudorapidity particle
      rap_of_eta_min = 0


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
              T_sum += T[particle_count]

              # define an initial value to save the pseudorapidity
              eta.append(0)
              # pick out the pseudorapidity using TLorentzVector
              eta[particle_count] = T[particle_count].PseudoRapidity()
              # define an initial value to save the rapidity
              rap.append(0)
              # pick out the rapidity using TLorentzVector
              rap[particle_count] = T[particle_count].Rapidity()

              # find the maximum pseudorapidity
              eta_max = max(eta)
              # find the minimum pseudorapidity
              eta_min = min(eta)
              # find the maximum rapidity
              rap_max = max(rap)
              # find the minimum rapidity
              rap_min = min(rap)
              """
              here the "max(eta)" in the "eta.index (max(eta))" can't be changed to "eta_max"
              """
              # find the rapidity of the maximum pseudorapidity particle
              rap_of_eta_max = rap[eta.index (max(eta))]
              # find the rapidity of the minimum pseudorapidity particle
              rap_of_eta_min = rap[eta.index (min(eta))]

              # prepare to the next loop
              particle_count += 1



      # Fill the histogram in the loop, so that you needn't to define another loop to fill
      h_invariant_mass.Fill(T_sum.M())
      h_Pt.Fill(T_sum.Pt())
      h_E.Fill(T_sum.E())
      h_eta_max.Fill(eta_max)
      h_eta_min.Fill(eta_min)
      h_rap_max.Fill(rap_max)
      h_rap_min.Fill(rap_min)
      h_rap_of_eta_max.Fill(rap_of_eta_max)
      h_rap_of_eta_min.Fill(rap_of_eta_min)

  # creat a root file to histogram
  tfout = R.TFile("sum_v2.root", "RECREATE")
  tfout.cd()
  h_invariant_mass.Write()
  h_Pt.Write()
  h_E.Write()
  h_eta_max.Write()
  h_eta_min.Write()
  h_rap_max.Write()
  h_rap_min.Write()
  h_rap_of_eta_max.Write()
  h_rap_of_eta_min.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)

