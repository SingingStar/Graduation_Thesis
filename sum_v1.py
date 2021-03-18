#!/usr/bin/env python

# import some modules
import sys, os
sys.path.append("/users/wuxingyu/MG5_aMC_v2_9_2/")
from madgraph.various.lhe_parser import *
import ROOT as R


# define a function named "read_lhe", its input is "input_file"
def read_lhe(input_file):
  # use Class EventFile defined in the lhe_parser.py to read the usage information in the LHE files
  lhe = EventFile(input_file)

  # define some initial values before the loop
  # define an empty list to save the data of invariant mass
  data_invariant_mass = []
  # define an empty list to save the data of Pt of tt~ system, so each event only have 1 Pt
  data_Pt = []
  # define an empty list to save the data of E of tt~ system, so each event only have 1 E
  data_E = []
  # define an empty list to save the data of the maximum pseudorapidity
  data_eta_max = []
  # define an empty list to save the data of the minimum pseudorapidity
  data_eta_min = []
  # define an empty list to save the data of the maximum rapidity, use "rap" to represent rapidity
  data_rap_max = []
  # define an empty list to save the data of the minimum rapidity
  data_rap_min = []
  # define an empty list to save the data of the rapidity of the maximum pseudorapidity
  data_rap_of_max_eta = []
  # define an empty list to save the data of the rapidity of the minimum pseudorapidity
  data_rap_of_min_eta = []
  # define an empty list to save the data of the pseudorapidity of 1st final state particle
  data_eta_1st = []
  # define an empty list to save the data of the rapidity of the 1st final state particle
  data_rap_1st = []
  # define an initial value to count the number of positive-rapidity of the 1st final state particle
  num_positive_rap_1st = 0
  # define an initial value to count the number of positive-pseudorapidity of the 1st final state particle
  num_positive_eta_1st = 0




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
      # define an initial value to save the index of maximum pseudorapidity
      eta_max_index = 0
      # define an initial value to save the index of minimum pseudorapidity
      eta_min_index = 0
      # define an empty list to save the rapidity of each particles
      rap = []
      # define an initial value to save the maximum rapidity
      rap_max = 0
      # define an initial value to save the rapidity of the maximum pseudorapidity particle
      rap_of_max_eta  = 0
      # define an initial value to save the rapidity of the minimum pseudorapidity particle
      rap_of_min_eta = 0
      # define an initial value to save the pseudorapidity of 1st final state particle
      eta_1st = 0
      # define an initial value to save the rapidity of 1st final state particle
      rap_1st = 0


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

              # pick out the pseudorapidity using TLorentzVector
              eta[particle_count] = R.TLorentzVector.PseudoRapidity(T[particle_count])


              """
              there's a question or maybe a bug which still haven't found the answer, if I use pseudorapidity and rapidity defined in the madgraph, the data is not corresponded.
              # pick out the pseudorapidity using madgraph
              eta[particle_count] = p.pseudorapidity
              print("pseudorapidity", particle_count, p.pseudorapidity)
              """

              # find the maximum pseudorapidity
              eta_max = max(eta)
              # find the index of maximum pseudorapidity
              eta_max_index = eta.index (max(eta))
              # find the minimum pseudorapidity
              eta_min = min(eta)
              # find the index of minimum pseudorapidity
              eta_min_index = eta.index (min(eta))


              """
              calculate both the maximum rapidity and the minimum rapidity in the final state particles
              """

              # define an initial value to save the rapidity
              rap.append(0)


              # pick out the rapidity using TLorentzVector
              rap[particle_count] = R.TLorentzVector.Rapidity(T[particle_count])


              """
              there's a question or maybe a bug which still haven't found the answer, if I use pseudorapidity and rapidity defined in the madgraph, the data is not corresponded.
              # pick out the rapidity using madgraph
              rap[particle_count] = p.rapidity
              print ("rapidity", particle_count, p.rapidity)
              """

              # find the maximum rapidity
              rap_max = max(rap)
              # find the minimum rapidity
              rap_min = min(rap)
              # find the rapidity of the maximum pseudorapidity particle
              rap_of_max_eta = rap[eta_max_index]
              # find the rapidity of the minimum pseudorapidity particle
              rap_of_min_eta = rap[eta_min_index]


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
      calculate the E of the sum of final status particles
      """
      energy = T_sum.E()
      # save the data
      data_E.append(energy)


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


      """
      save the rapidity of the maximum pseudorapidity particle
      """
      data_rap_of_max_eta.append(rap_of_max_eta)


      """
      save the rapidity of the minimum pseudorapidity particle
      """
      data_rap_of_min_eta.append(rap_of_min_eta)


      """
      save the pseudorapidity of 1st final state particle
      """
      eta_1st = eta[0]
      data_eta_1st.append(eta_1st)


      """
      save the rapidity of 1st final state particle
      """
      rap_1st = rap[0]
      data_rap_1st.append(rap_1st)


  # count the number of positive-rapidity of the 1st final state particle
  for i in data_rap_1st:
      if i > 0:
          num_positive_rap_1st += 1
  print ("positive_rap_1st", num_positive_rap_1st)


  # count the number of positive-pseudorapidity of the 1st final state particle
  for i in data_eta_1st:
      if i > 0:
          num_positive_eta_1st += 1
  print ("positive_eta_1st", num_positive_eta_1st)



  # print out the data in the terminal
  print ("**********data_invariant_mass**********")
  print (data_invariant_mass)
  print ("\n\n\n")
  print ("**********data_Pt**********")
  print (data_Pt)
  print ("\n\n\n")
  print ("**********data_E**********")
  print (data_E)
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
  print ("\n\n\n")
  print ("**********data_rap_of_max_eta**********")
  print (data_rap_of_max_eta)
  print ("\n\n\n")
  print ("**********data_rap_of_min_eta**********")
  print (data_rap_of_min_eta)
  print ("\n\n\n")
  print ("**********data_eta_1st**********")
  print (data_eta_1st)
  print ("\n\n\n")
  print ("**********data_rap_1st**********")
  print (data_rap_1st)



  """
  draw the histogram of invariant_mass
  """
  # creat a new canvas named "myC1", sign it with "C1"
  myC1 = R.TCanvas("C1")
  # enter this canvas
  myC1.cd()

  hname = "invariant_mass"
  nbins, xmin, xmax = 100, 0, 2000
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h1.SetTitle("invariant_mass;invariant_mass/Gev;count")
  for i, d in enumerate(data_invariant_mass):
    h1.Fill(d)
  h1.Draw("LE")


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
  # enter this canvas
  myC2.cd()


  hname = "Pt"
  nbins, xmin, xmax = 100, -10, 10
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h2.SetTitle("Pt of tt~ system;Pt/GeV;count")
  for i, d in enumerate(data_Pt):
    h2.Fill(d)
  h2.Draw("LE")


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("Pt of tt~ system","C2")
  leg.AddEntry(h2,"t and t~","f")
  leg.Draw()


  myC2.SaveAs("Pt.png")


  """
  draw the histogram of E
  """
  # creat a new canvas named "myC3", sign it with "C3"
  myC3 = R.TCanvas("C3")
  # enter this canvas
  myC3.cd()


  hname = "E of tt~ system"
  nbins, xmin, xmax = 100, 0, 4000
  h3 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h3.SetTitle("E of tt~ system;E of tt~ system/GeV;count")
  for i, d in enumerate(data_E):
    h3.Fill(d)
  h3.Draw("LE")

  
  leg = R.TLegend(0.5,0.7,0.7,0.8)
  leg.SetHeader("E of tt~ system","C3")
  leg.AddEntry(h3,"t and t~","f")
  leg.Draw()


  myC3.SaveAs("E.png")


  """
  draw the histogram of the maximum pseudorapidity
  """
  # creat a new canvas named "myC4", sign it with "C4"
  myC4 = R.TCanvas("C4")
  # enter this canvas
  myC4.cd()


  hname = "the maximum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h4 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h4.SetTitle("the maximum pseudorapidity;the maximum pseudorapidity;count")
  for i, d in enumerate(data_eta_max):
    h4.Fill(d)
  h4.Draw("LE")

  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the maximum pseudorapidity","C4")
  leg.AddEntry(h4,"t and t~","f")
  leg.Draw()


  myC4.SaveAs("eta_max.png")


  """
  draw the histogram of the minumum pseudorapidity
  """
  # creat a new canvas named "myC5", sign it with "C5"
  myC5 = R.TCanvas("C5")
  # enter this canvas
  myC5.cd()


  hname = "the minimum pseudorapidity"
  nbins, xmin, xmax = 100, -10, 10
  h5 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h5.SetTitle("the minimum pseudorapidity;the minimum pseudorapidity;count")
  for i, d in enumerate(data_eta_min):
    h5.Fill(d)
  h5.Draw("LE")

  
  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the minimum pseudorapidity","C5")
  leg.AddEntry(h5,"t and t~","f")
  leg.Draw()


  myC5.SaveAs("eta_min.png")

  """
  draw the histogram of the maximum rapidity
  """
  # creat a new canvas named "myC6", sign it with "C6"
  myC6 = R.TCanvas("C6")
  # enter this canvas
  myC6.cd()


  hname = "the maximum rapidity"
  nbins, xmin, xmax = 100, -10, 10
  h6 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h6.SetTitle("the maximum rapidity;the maximum rapidity;count")
  for i, d in enumerate(data_rap_max):
    h6.Fill(d)
  h6.Draw("LE")


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the maximum rapidity","C6")
  leg.AddEntry(h6,"t and t~","f")
  leg.Draw()


  myC6.SaveAs("rap_max.png")


  """
  draw the histogram of the minimum rapidity
  """
  # creat a new canvas named "myC7", sign it with "C7"
  myC7 = R.TCanvas("C7")
  # enter this canvas
  myC7.cd()


  hname = "the minimum rapidity"
  nbins, xmin, xmax = 100, -10, 10
  h7 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h7.SetTitle("the minimum rapidity;the minimum rapidity;count")
  for i, d in enumerate(data_rap_min):
    h7.Fill(d)
  h7.Draw("LE")


  leg = R.TLegend(0.2,0.7,0.4,0.8)
  leg.SetHeader("the minimum rapidity","C7")
  leg.AddEntry(h7,"t and t~","f")
  leg.Draw()


  myC7.SaveAs("rap_min.png")


  """
  draw the histogram of the maximum pseudorapidity and this particle's rapidity
  """
  # creat a new canvas named "myC8", sign it with "C8"
  myC8 = R.TCanvas("C8")
  # enter this canvas
  myC8.cd()


  hname = "compare eta_max & its rap"
  nbins, xmin, xmax = 100, -10, 10
  h81 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h82 = R.TH1F(hname, hname, nbins, xmin, xmax)

  h81.SetTitle("compare eta_max & its rap;eta_max/rap;count")
  h82.SetTitle("compare eta_max & its rap;eta_max/rap;count")
  h81.SetLineColor(2)
  h82.SetLineColor(3)

  for i, d in enumerate(data_rap_of_max_eta):
    h81.Fill(d)
  h81.Draw("LE")
  for i, d in enumerate(data_eta_max):
    h82.Fill(d)
  h82.Draw("SameLE")


  leg = R.TLegend(0.2,0.6,0.4,0.8)
  leg.SetHeader("eta_max & its rap","C8")
  leg.AddEntry(h81,"rap","f")
  leg.AddEntry(h82,"eta_max","f")
  leg.Draw()

  R.gStyle.SetOptStat(0)


  myC8.SaveAs("eta_max & its rap.png")


  """
  draw the histogram of the minimum pseudorapidity and this particle's rapidity
  """
  # creat a new canvas named "myC9", sign it with "C9"
  myC9 = R.TCanvas("C9")
  # enter this canvas
  myC9.cd()


  hname = "compare eta_min & its rap"
  nbins, xmin, xmax = 100, -10, 10
  h91 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h92 = R.TH1F(hname, hname, nbins, xmin, xmax)

  h91.SetTitle("compare eta_min & its rap;eta_min/rap;count")
  h92.SetTitle("compare eta_min & its rap;eta_min/rap;count")
  h91.SetLineColor(2)
  h92.SetLineColor(3)

  for i, d in enumerate(data_rap_of_min_eta):
    h91.Fill(d)
  h91.Draw("LE")
  for i, d in enumerate(data_eta_min):
    h92.Fill(d)
  h92.Draw("SameLE")

  leg = R.TLegend(0.2,0.6,0.4,0.8)
  leg.SetHeader("eta_min & its rap","C9")
  leg.AddEntry(h91,"rap","f")
  leg.AddEntry(h92,"eta_min","f")
  leg.Draw()

  R.gStyle.SetOptStat(0)


  myC9.SaveAs("eta_min & its rap.png")


  """
  draw the histogram of pseudorapidity and rapidity of 1st final state particle
  """
  # creat a new canvas named "myC10", sign it with "C10"
  myC10 = R.TCanvas("C10")
  # enter this canvas
  myC10.cd()

  hname = "compare 1st rap & eta"
  nbins, xmin, xmax = 100, -10, 10
  h101 = R.TH1F(hname, hname, nbins, xmin, xmax)
  h102 = R.TH1F(hname, hname, nbins, xmin, xmax)

  h101.SetTitle("compare 1st eta & rap;eta/rap;count")
  h102.SetTitle("compare 1st eta & rap;eta/rap;count")
  h101.SetLineColor(2)
  h102.SetLineColor(3)

  for i, d in enumerate(data_rap_1st):
    h101.Fill(d)
  h101.Draw("LE")
  for i, d in enumerate(data_eta_1st):
    h102.Fill(d)
  h102.Draw("SameLE")

  leg = R.TLegend(0.2,0.6,0.4,0.8)
  leg.SetHeader("1st eta & rap","C10")
  leg.AddEntry(h101,"rap_1st","f")
  leg.AddEntry(h102,"eta_1st","f")
  leg.Draw()

  R.gStyle.SetOptStat(0)


  myC10.SaveAs("1st eta & rap.png")




  tfout = R.TFile("sum.root", "RECREATE")
  tfout.cd()
  """
  h1.Write() #what's the meaning?
  """
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/MY_FIRST_MG5_RUN/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)



