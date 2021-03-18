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
  # define a empty list to save the data of invariant mass
  data_invariant_mass = []
  # define a empty list to save the data of Pt of tt~ system, so each event only have 1 Pt
  data_Pt = []
  # define a empty list to save the data of the maximum pseudorapidity
  data_eta_max = []
  # define a empty list to save the data of the minimum pseudorapidity
  data_eta_min = []
  # define a empty list to save the data of the maximum rapidity, use "rap" to represent rapidity
  data_rap_max = []
  # define a empty list to save the data of the minimum rapidity
  data_rap_min = []


  # loop the events
  for event in lhe:
      #define some initial values in the loop

      # define an initial value to save the sum of TLorentzVector
      T_sum = R.TLorentzVector()
      # define an empty list to save the TLorentzVector of each particles
      # it can't be defined out of the event, or it's member will add up to 2, 4, ...etc
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


              """
              calculate both the maximum pseudorapidity and the minimum pseudorapidity in the final state particles
              """

              # define an initial value to save the pseudorapidity
              eta.append(0)
              # pick out the pseudorapidity
              eta[particle_count] = p.pseudorapidity
              # find the maximum pseudorapidity
              eta_max = max(eta)
              # find the minimum pseudorapidity
              eta_min = min(eta)


              """
              calculate both the maximum rapidity and the minimum rapidity in the final state particles
              """

              # define an initial value to save the rapidity
              rap.append(0)
              # pick out the rapidity
              rap[particle_count] = p.rapidity
              # find the maximum rapidity
              rap_max = max(rap)
              # find the minimum rapidity
              rap_min = min(rap)


              # prepare to the next loop
              particle_count += 1


      """
      calculate the invariant mass of the sum of final status particles
      """
      m = T_sum.M()
      # save the data
      data_invariant_mass.append(m)


      """
      calculate the Pt of the sum of final status particles
      """
      pt = T_sum.Pt()
      # save the data
      data_Pt.append(pt)


      """
      save the maximum pseudorapidity and the minimum pseudorapidity
      """
      data_eta_max.append(eta_max)
      data_eta_min.append(eta_min)


      """
      save the maximum rapidity and the minimum rapidity
      """
      data_rap_max.append(rap_max)
      data_rap_min.append(rap_min)

  # print out the data in the terminal
  print ("**********data_invariant_mass**********")
  print (data_invariant_mass)
  print ("\n\n\n")
  print ("**********data_Pt**********")
  print (data_Pt)
  print ("\n\n\n")
  print ("**********data_eta_max***********")
  print (data_eta_max)
  print ("\n\n\n")
  print ("**********data_eta_min***********")
  print (data_eta_min)
  print ("\n\n\n")
  print ("**********data_rap_max**********")
  print (data_rap_max)
  print ("\n\n\n")
  print ("**********data_rap_min**********")
  print (data_rap_min)



  """
  draw the histogram of invariant_mass
  """
  # creat a new canvas named "myC1", sign it with "C1"
  myC1 = R.TCanvas("C1")
  # enter this canvas
  myC1.cd()

  hname = "invariant_mass"
  nbins, xmin, xmax = 1000, 0, 2000
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("invariant_mass;invariant_mass/Gev;count")
  for i, d in enumerate(data_invariant_mass):
    h1.Fill(d)
  h1.Draw()


  leg = R.TLegend(0.5,0.7,0.7,0.8)
  leg.SetHeader("invariant_mass","C1")
  leg.AddEntry(h1,"t and t~","f")
  leg.Draw()

  myC1.SaveAs("invariant_mass.png")


  """
  draw the histogram of Pt
  """
  # creat a new canvas named "myC2", sign it with "C2"
  myC2 = R.TCanvas("C2")
  myC2.cd()


  hname = "Pt"
  nbins, xmin, xmax = 1000, -1000, 1000
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h2.SetTitle("Pt;Pt/GeV;count")
  for i, d in enumerate(data_Pt):
    h2.Fill(d)
  h2.Draw()


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("Pt","C2")
  leg.AddEntry(h2,"t and t~","f")
  leg.Draw()


  myC2.SaveAs("Pt.png")


  """
  draw the histogram of the maximum pseudorapidity
  """
  # creat a new canvas named "myC3", sign it with "C3"
  myC3 = R.TCanvas("C3")
  myC3.cd()


  hname = "the maximum pseudorapidity"
  nbins, xmin, xmax = 1000, -10, 10
  h3 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h3.SetTitle("the maximum pseudorapidity;the maximum pseudorapidity;count")
  for i, d in enumerate(data_eta_max):
    h3.Fill(d)
  h3.Draw()

  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the maximum pseudorapidity","C3")
  leg.AddEntry(h3,"t and t~","f")
  leg.Draw()


  myC3.SaveAs("eta_max.png")


  """
  draw the histogram of the minumum pseudorapidity
  """
  # creat a new canvas named "myC4", sign it with "C4"
  myC4 = R.TCanvas("C4")
  myC4.cd()


  hname = "the minimum pseudorapidity"
  nbins, xmin, xmax = 1000, -10, 10
  h4 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h4.SetTitle("the minimum pseudorapidity;the minimum pseudorapidity;count")
  for i, d in enumerate(data_eta_min):
    h4.Fill(d)
  h4.Draw()

  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the minimum pseudorapidity","C4")
  leg.AddEntry(h4,"t and t~","f")
  leg.Draw()


  myC4.SaveAs("eta_min.png")

  """
  draw the histogram of the maximum rapidity
  """
  # creat a new canvas named "myC5", sign it with "C5"
  myC5 = R.TCanvas("C5")
  myC5.cd()


  hname = "the maximum rapidity"
  nbins, xmin, xmax = 1000, -10, 10
  h5 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h5.SetTitle("the maximum rapidity;the maximum rapidity;count")
  for i, d in enumerate(data_rap_max):
    h5.Fill(d)
  h5.Draw()


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the maximum rapidity","C5")
  leg.AddEntry(h5,"t and t~","f")
  leg.Draw()


  myC5.SaveAs("rap_max.png")


  """
  draw the histogram of the minimum rapidity
  """
  # creat a new canvas named "myC6", sign it with "C6"
  myC6 = R.TCanvas("C6")
  myC6.cd()


  hname = "the minimum rapidity"
  nbins, xmin, xmax = 1000, -10, 10
  h6 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h6.SetTitle("the minimum rapidity;the minimum rapidity;count")
  for i, d in enumerate(data_rap_min):
    h6.Fill(d)
  h6.Draw()


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the minimum rapidity","C6")
  leg.AddEntry(h6,"t and t~","f")
  leg.Draw()


  myC6.SaveAs("rap_min.png")



  tfout = R.TFile("sum.root", "RECREATE")
  tfout.cd()
  h1.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)



