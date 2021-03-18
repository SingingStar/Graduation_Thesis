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

  # define an empty list to save the data of Pt_sort in each event
  data_Pt_sorts = []
  # define an empty list to save the data of Leading_Pt
  data_Leading_Pt = []
  # define an empty list to save the data of SubLeading_Pt
  data_SubLeading_Pt = []
  # define an empty list to save the data of ThirdLeading_Pt
  data_ThirdLeading_Pt = []
  # define an empty list to save the data of ForthLeading_Pt
  data_ForthLeading_Pt = []
  # define an empty list to save the data of eta_of_Leading_Pt
  data_eta_of_Leading_Pt = []
  # define an empty list to save the data of eta_of_SubLeading_Pt
  data_eta_of_SubLeading_Pt = []
  # define an empty list to save the data of eta_of_ThirdLeading_Pt
  data_eta_of_ThirdLeading_Pt = []
  # define an empty list to save the data of eta_of_ForthLeading_Pt
  data_eta_of_ForthLeading_Pt = []


  # loop the events
  for event in lhe:
      #define some initial values in the loop
      # define an empty list to save the TLorentzVector of each particles
      # it can't be defined out of the event, or its member will add up to 2, 4, ...etc
      T = []
      # define "particle_count" to count the particles, so that we can draw the histograms when particle_counts beyond 2.
      particle_count = 0
      # define an empty list to save the data of Pt, the number of Pt equals to the number of final state particles
      data_Pt = []
      # define an initial value to save the sort of Pt
      Pt_sorts = []
      # define an initial value to save the Leading_Pt
      Leading_Pt = 0
      # define an initial value to save the SubLeading_Pt
      SubLeading_Pt = 0
      # define an initial value to save the ThirdLeading_Pt
      ThirdLeading_Pt = 0
      # define an initial value to save the ForthLeading_Pt
      ForthLeading_Pt = 0
      # define an initial value to save the eta_of_Leading_Pt
      eta_of_Leading_Pt = 0
      # define an initial value to save the eta_of_SubLeading_Pt
      eta_of_SubLeading_Pt = 0
      # define an initial value to save the eta_of_ThirdLeading_Pt
      eta_of_ThirdLeading_Pt = 0
      # define an initial value to save the eta_of_ForthLeading_Pt
      eta_of_ForthLeading_Pt = 0


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


              # calculate the Pt of each final status particles and save them
              data_Pt.append(T[particle_count].Pt())

              # prepare to the next loop
              particle_count += 1


      """
      take care of this code block, I have misunderstood the function named "sorted", see its explanation at https://blog.csdn.net/qq1195365047/article/details/90295660
      """
      # Sort the Pt in the list from small to large, and save the sort index values
      Pt_sorts = sorted(range(len(data_Pt)), key=lambda k: data_Pt[k])
      data_Pt_sorts.append(Pt_sorts)

      # loop the Pt_sorts to save the data of each Pt(Leading, SubLeading, ThirdLeading, ForthLeading)
      for i, Pt_sort in enumerate(Pt_sorts):
          # take care that the Pt behind is larger than the front, that would influence how to define the value of i in sytax if and elif
          if i == 3:
              Leading_Pt = data_Pt[Pt_sort]
              data_Leading_Pt.append(Leading_Pt)
              eta_of_Leading_Pt = T[Pt_sort].PseudoRapidity()
              data_eta_of_Leading_Pt.append(eta_of_Leading_Pt)
          elif i == 2:
              SubLeading_Pt = data_Pt[Pt_sort]
              data_SubLeading_Pt.append(SubLeading_Pt)
              eta_of_SubLeading_Pt = T[Pt_sort].PseudoRapidity()
              data_eta_of_SubLeading_Pt.append(eta_of_SubLeading_Pt)
          elif i == 1:
              ThirdLeading_Pt = data_Pt[Pt_sort]
              data_ThirdLeading_Pt.append(ThirdLeading_Pt)
              eta_of_ThirdLeading_Pt = T[Pt_sort].PseudoRapidity()
              data_eta_of_ThirdLeading_Pt.append(eta_of_ThirdLeading_Pt)
          elif i == 0:
              ForthLeading_Pt = data_Pt[Pt_sort]
              data_ForthLeading_Pt.append(ForthLeading_Pt)
              eta_of_ForthLeading_Pt = T[Pt_sort].PseudoRapidity()
              data_eta_of_ForthLeading_Pt.append(eta_of_ForthLeading_Pt)





  # print out the data in the terminal
  print ("**********data_Pt_sorts**********")
  print (data_Pt_sorts)
  print ("\n\n\n")
  print ("**********data_Leading_Pt**********")
  print (data_Leading_Pt)
  print ("\n\n\n")
  print ("**********data_SubLeading_Pt**********")
  print (data_SubLeading_Pt)
  print ("\n\n\n")
  print ("**********data_ThirdLeading_Pt**********")
  print (data_ThirdLeading_Pt)
  print ("\n\n\n")
  print ("**********data_ForthLeading_Pt**********")
  print (data_ForthLeading_Pt)
  print ("\n\n\n")
  print ("**********data_eta_of_Leading_Pt**********")
  print (data_eta_of_Leading_Pt)
  print ("\n\n\n")
  print ("**********data_eta_of_SubLeading_Pt**********")
  print (data_eta_of_SubLeading_Pt)
  print ("\n\n\n")
  print ("**********data_eta_of_ThirdLeading_Pt**********")
  print (data_eta_of_ThirdLeading_Pt)
  print ("\n\n\n")
  print ("**********data_eta_of_ForthLeading_Pt**********")
  print (data_eta_of_ForthLeading_Pt)
  print ("\n\n\n")




  """
  draw the histogram of 4_Pt, including Leading_Pt, SubLeading_Pt, ThirdLeading_Pt, ForthLeading_Pt
  """
  # creat a new canvas named "myC1", sign it with "C1"
  myC1 = R.TCanvas("C1")
  # enter this canvas
  myC1.cd()

  hname = "4_Pt"
  nbins, xmin, xmax = 100, 0, 200
  h11 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h12 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h13 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h14 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h11.SetTitle("4_Pt;Pt/GeV;count")
  h12.SetTitle("4_Pt;Pt/GeV;count")
  h13.SetTitle("4_Pt;Pt/GeV;count")
  h14.SetTitle("4_Pt;Pt/GeV;count")
  h11.SetLineColor(2)
  h12.SetLineColor(3)
  h13.SetLineColor(4)
  h14.SetLineColor(5)



  for i, d in enumerate(data_ForthLeading_Pt):
    h11.Fill(d)
  h11.Draw("LE")
  for i, d in enumerate(data_ThirdLeading_Pt):
    h12.Fill(d)
  h12.Draw("SameLE")
  for i, d in enumerate(data_SubLeading_Pt):
    h13.Fill(d)
  h13.Draw("SameLE")
  for i, d in enumerate(data_Leading_Pt):
    h14.Fill(d)
  h14.Draw("SameLE")

  R.gStyle.SetOptStat(0)


  leg = R.TLegend(0.4,0.6,0.8,0.9)
  leg.SetHeader("4_Pt","C1")
  leg.AddEntry(h11,"ForthLeading_Pt","f")
  leg.AddEntry(h12,"THirdLeading_Pt","f")
  leg.AddEntry(h13,"SubLeading_Pt","f")
  leg.AddEntry(h14,"Leading_Pt","f")
  leg.Draw()

  myC1.SaveAs("4_Pt.png")



  """
  draw the histogram of eta_of_4_Pt, including eta_of_Leading_Pt, eta_of_SubLeading_Pt, eta_of_ThirdLeading_Pt, eta_of_ForthLeading_Pt
  """
  # creat a new canvas named "myC2", sign it with "C2"
  myC2 = R.TCanvas("C2")
  # enter this canvas
  myC2.cd()

  hname = "eta_of_4_Pt"
  nbins, xmin, xmax = 100, -10, 10
  h21 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h22 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h23 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h24 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h21.SetTitle("eta_of_4_Pt;eta;count")
  h22.SetTitle("eta_of_4_Pt;eta;count")
  h23.SetTitle("eta_of_4_Pt;eta;count")
  h24.SetTitle("eta_of_4_Pt;eta;count")
  h21.SetLineColor(2)
  h22.SetLineColor(3)
  h23.SetLineColor(4)
  h24.SetLineColor(5)



  for i, d in enumerate(data_eta_of_ForthLeading_Pt):
    h21.Fill(d)
  h21.Draw("LE")
  for i, d in enumerate(data_eta_of_ThirdLeading_Pt):
    h22.Fill(d)
  h22.Draw("SameLE")
  for i, d in enumerate(data_eta_of_SubLeading_Pt):
    h23.Fill(d)
  h23.Draw("SameLE")
  for i, d in enumerate(data_eta_of_Leading_Pt):
    h24.Fill(d)
  h24.Draw("SameLE")

  R.gStyle.SetOptStat(0)


  leg = R.TLegend(0.1,0.7,0.4,0.9)
  leg.SetHeader("eta_of_4_Pt","C2")
  leg.AddEntry(h21,"eta_of_ForthLeading_Pt","f")
  leg.AddEntry(h22,"eta_of_THirdLeading_Pt","f")
  leg.AddEntry(h23,"eta_of_SubLeading_Pt","f")
  leg.AddEntry(h24,"eta_of_Leading_Pt","f")
  leg.Draw()

  myC2.SaveAs("eta_of_4_Pt.png")





  tfout = R.TFile("4_Pt_and_eta.root", "RECREATE")
  tfout.cd()
  """
  h1.Write() #what's the meaning?
  """
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/pp_to_ZZ/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)
