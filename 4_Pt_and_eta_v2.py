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
  When histograming, be careful that every histogram has the same name of parameters, such as "hname", "nbins", "xmin", "xmax". Although because every time when you use them they have already change to the new value and the past job have already finished and wouldn't be changed. Maybe sometimes it would cause to errors.
  """



  """
  histogram of 4_Pt, including Leading_Pt, SubLeading_Pt, ThirdLeading_Pt, ForthLeading_Pt
  """
  # define hname = "4_Pt", and use it to fill in the 2ed parameter in the class TH1F, so that every histogram have the same title.
  hname = "4_Pt"
  nbins, xmin, xmax = 100, 0, 200
  # h_FLP represents histogram of Forthleading Pt, the others are the same.
  # "Leading_Pt" represents that the name of the 1st histogram, it's different from the title, the others are the same.
  h_LP = R.TH1F("Leading_Pt", hname, nbins, xmin, xmax)
  h_SLP = R.TH1F("SubLeading_Pt", hname, nbins, xmin, xmax)
  h_TLP = R.TH1F("ThirdLeading_Pt", hname, nbins, xmin, xmax)
  h_FLP = R.TH1F("Fortheading_Pt", hname, nbins, xmin, xmax)
  # set the title of each histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_LP.SetTitle("Leading_Pt;Pt/GeV;count")
  h_SLP.SetTitle("SubLeading_Pt;Pt/GeV;count")
  h_TLP.SetTitle("ThirdLeading_Pt;Pt/GeV;count")
  h_FLP.SetTitle("ForthLeading_Pt;Pt/GeV;count")
  # set the color of each histogram
  h_LP.SetLineColor(5)
  h_SLP.SetLineColor(4)
  h_TLP.SetLineColor(3)
  h_FLP.SetLineColor(2)


  """
  histogram of eta_of_4_Pt, including eta_of_Leading_Pt, eta_of_SubLeading_Pt, eta_of_ThirdLeading_Pt, eta_of_ForthLeading_Pt
  """
  # define hname = "eta_of_4_Pt", and use it in the class TH1F, so that every histogram have the same title.
  hname = "eta_of_4_Pt"
  nbins, xmin, xmax = 100, -10, 10
  # h_eLP represents histogram of eta of Leading Pt, the others are the same.
  h_eLP = R.TH1F("eta_of_Leading_Pt", hname, nbins, xmin, xmax)
  h_eSLP = R.TH1F("eta_of_SubLeading_Pt", hname, nbins, xmin, xmax)
  h_eTLP = R.TH1F("eta_of_ThirdLeading_Pt", hname, nbins, xmin, xmax)
  h_eFLP = R.TH1F("eta_of_ForthLeading_Pt", hname, nbins, xmin, xmax)
  # set the title of each histogram
  h_eLP.SetTitle("eta_of_Leading_Pt;eta;count")
  h_eSLP.SetTitle("eta_of_SubLeading_Pt;eta;count")
  h_eTLP.SetTitle("eta_of_ThirdLeading_Pt;eta;count")
  h_eFLP.SetTitle("eta_of_ForthLeading_Pt;eta;count")
  # set the color of each histogram
  h_eLP.SetLineColor(2)
  h_eSLP.SetLineColor(3)
  h_eTLP.SetLineColor(4)
  h_eFLP.SetLineColor(5)


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

      # loop the Pt_sorts to save the data of each Pt(Leading, SubLeading, ThirdLeading, ForthLeading)
      for i, Pt_sort in enumerate(Pt_sorts):
          # take care that the Pt behind is larger than the front, that would influence how to define the value of i in sytax if and elif
          if i == 3:
              # data_Pt[Pt_sort] = Leading_Pt
              h_LP.Fill(data_Pt[Pt_sort])
              # T[Pt_sort].PseudoRapidity() = eta_of_Leading_Pt
              h_eLP.Fill(T[Pt_sort].PseudoRapidity())
          elif i == 2:
              # data_Pt[Pt_sort] = SubLeading_Pt
              h_SLP.Fill(data_Pt[Pt_sort])
              # T[Pt_sort].PseudoRapidity() = eta_of_SubLeading_Pt
              h_eSLP.Fill(T[Pt_sort].PseudoRapidity())
          elif i == 1:
              # data_Pt[Pt_sort] = ThirdLeading_Pt
              h_TLP.Fill(data_Pt[Pt_sort])
              # T[Pt_sort].PseudoRapidity() = eta_of_ThirdLeading_Pt
              h_eTLP.Fill(T[Pt_sort].PseudoRapidity())
          elif i == 0:
              # data_Pt[Pt_sort] = ForthLeading_Pt
              h_eFLP.Fill(data_Pt[Pt_sort])
              # T[Pt_sort].PseudoRapidity() = eta_of_ForthLeading_Pt
              h_eFLP.Fill(T[Pt_sort].PseudoRapidity())



  tfout = R.TFile("4_Pt_and_eta.root", "RECREATE")
  tfout.cd()
  h_LP.Write()
  h_SLP.Write()
  h_TLP.Write()
  h_FLP.Write()
  h_eLP.Write()
  h_eSLP.Write()
  h_eTLP.Write()
  h_eFLP.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/pp_to_ZZ/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)
