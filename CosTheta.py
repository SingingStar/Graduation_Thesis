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

  # define some initial values before the loop
  # define the invariant mass of Z boson, in GeV
  Zmass = 91.187621
  # define 2 initial values to count the correct pairs and the wrong pairs
  CorrectPair = 0
  WrongPair = 0
  # define an initial value to save the accuracy
  Accuracy = 0


  """
  histogram the Zmass which is rebuilt from leptons and closest to the real Zmass. Named it as "M1"
  """
  htitle = "M1"
  nbins, xmin, xmax = 100, 40, 140
  h_M1 = R.TH1F("M1", htitle, nbins, xmin, xmax)
  h_M1.SetTitle("M1;M1/GeV;count")

  """
  histogram the Zmass which is rebuilt from the another pair leptons except M1, named it as "M2"
  """
  htitle = "M2"
  nbins, xmin, xmax = 100, 40, 140
  h_M2 = R.TH1F("M2", htitle, nbins, xmin, xmax)
  h_M2.SetTitle("M2;M2/GeV;count")

  """
  histogram the Zmass which is rebuilt from leptons using MOTHUP and closest to the real Zmass. Named it as "M1MOTHUP"
  """
  htitle = "M1MOTHUP"
  nbins, xmin, xmax = 100, 40, 140
  h_M1MOTHUP = R.TH1F("M1MOTHUP", htitle, nbins, xmin, xmax)
  h_M1MOTHUP.SetTitle("M1MOTHUP;M1/GeV;count")

  """
  histogram the Zmass which is rebuilt from the another pair leptons using MOTHUP except M1MOTHUP, named it as "M2MOTHUP"
  """
  htitle = "M2MOTHUP"
  nbins, xmin, xmax = 100, 40, 140
  h_M2MOTHUP = R.TH1F("M2MOTHUP", htitle, nbins, xmin, xmax)
  h_M2MOTHUP.SetTitle("M2MOTHUP;M2/GeV;count")

  """
  histogram the CosTheta, "CosTheta1" means this is the angle between Z boson which is marked as "M1" and 1 lepton in 2 leptons which rebuild the M1
  """
  htitle = "CosTheta1"
  nbins, xmin, xmax = 50, -1, 1
  h_CosTheta1 = R.TH1F("CosTheta1", htitle, nbins, xmin, xmax)
  h_CosTheta1.SetTitle("CosTheta1;CosTheta1;count")

  """
  histogram the CosTheta, "CosTheta2" means this is the angle between Z boson which is marked as "M2" and 1 lepton in 2 leptons which rebuild the M2
  """
  htitle = "CosTheta2"
  nbins, xmin, xmax = 50, -1, 1
  h_CosTheta2 = R.TH1F("CosTheta2", htitle, nbins, xmin, xmax)
  h_CosTheta2.SetTitle("CosTheta2;CosTheta2;count")

  """
  histogram the CosTheta, "CosTheta3" means this is the angle between Z boson which is marked as "M1" and another lepton different from CosTheta1 which rebuild the M1
  """
  htitle = "CosTheta3"
  nbins, xmin, xmax = 50, -1, 1
  h_CosTheta3 = R.TH1F("CosTheta3", htitle, nbins, xmin, xmax)
  h_CosTheta3.SetTitle("CosTheta3;CosTheta3;count")

  """
  histogram the CosTheta, "CosTheta4" means this is the angle between Z boson which is marked as "M2" and another lepton different from CosTheta1 which rebuild the M2
  """
  htitle = "CosTheta4"
  nbins, xmin, xmax = 50, -1, 1
  h_CosTheta4 = R.TH1F("CosTheta4", htitle, nbins, xmin, xmax)
  h_CosTheta4.SetTitle("CosTheta4;CosTheta4;count")


  # loop the events
  for event in lhe:

      """
      4 blocks: 1st function:histogram the M1 and M2;
                2ed function: histogram the M1MOTHUP and M2MOTHUP; 
                3rd function: find the correct pair and the wrong pair, count it and calculate the accuracy
                4th function: histogram the theta1 and theta2
      """

      """
      block of 1st function: histogram the M1 and M2
      """

      # define some initial values in the loop
      # define an empty list to save the particleID of final state particles
      PidList = []
      # define 4 empty lists to save the order number of each possible pair of leptons
      PidPair1, PidPair2, PidPair3, PidPair4 = [], [], [], []
      # define an empty list to save the absolute value of PidList
      AbsPidList = []
      # define 4 initial values to count the leptons in each "if" loop
      PidCount1, PidCount2, PidCount3, PidCount4 = 0, 0, 0, 0
      # define an initial value to count the particles in each event, "1" represents that it is the count of 1st function block
      ParticleCount1 = 0
      # define 4 empty lists to save the TLorentzVector for each possible pairs
      T1, T2, T3, T4 = [], [], [], []
      # define 4 initial values to save the sum of TLorentzVector for each possible pairs
      T1Sum, T2Sum, T3Sum, T4Sum = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
      # define 4 initial values to save the deltam for each possible pairs, so that we can choose the smallest one.
      deltam1, deltam2, deltam3, deltam4 = 0, 0, 0, 0
      # define an empty list to save the 4 Zmass that rebuilt from each possible pairs
      m = []
      # define an empty list to save the 4 deltam
      deltam = []
      # define an empty list to save the sorts of deltam
      deltamSorts = []
      # define 2 initial values to save the M1 and M2
      M1, M2 = 0, 0

      # loop the particles in each events
      for particle in event:
          # distinguish the final state particles
          if particle.status == 1:
              # save the particle ID in a list
              PidList.append(particle.pid)
      # calculate the absolute values of PidList
      for Pid in PidList:
          AbsPidList.append(abs(Pid))

      # choose the special final state which needn't 4 possibilities, [13, -13, 11, -11]
      if sorted(AbsPidList, reverse=True) == [13, 13, 11, 11]:
          # list all the possible particle pairs
          if PidList[0] == -PidList[1]:
              PidPair1 = [0, 1]
              PidPair2 = [2, 3]
              PidPair3 = []
              PidPair4 = []
          elif PidList[0] == -PidList[2]:
              PidPair1 = [0, 2]
              PidPair2 = [1, 3]
              PidPair3 = []
              PidPair4 = []
          elif PidList[0] == -PidList[3]:
              PidPair1 = [0, 3]
              PidPair2 = [1, 2]
              PidPair3 = []
              PidPair4 = []
          # calculate the TLorentzVector and their sum of each possible pairs
          for particle in event:
              if particle.status == 1:
                  if ParticleCount1 in PidPair1:
                      p1 = FourMomentum(particle)
                      T1.append(R.TLorentzVector())
                      T1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                      T1Sum += T1[PidCount1]
                      PidCount1 += 1
                      ParticleCount1 += 1
                  elif ParticleCount1 in PidPair2:
                      p2 = FourMomentum(particle)
                      T2.append(R.TLorentzVector())
                      T2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                      T2Sum += T2[PidCount2]
                      PidCount2 += 1
                      ParticleCount1 += 1

      # choose the other final states which need 4 possibilities, [11, -11, 11, -11] and [13, -13, 13, -13]
      else:
          # list all the possible particle pairs
          if PidList[0] == -PidList[1]:
              PidPair1 = [0, 1]
              PidPair2 = [2, 3]
              if PidList[0] == -PidList[2]:
                  PidPair3 = [0, 2]
                  PidPair4 = [1, 3]
              else:
                  PidPair3 = [0, 3]
                  PidPair4 = [1, 2]
          else:
              PidPair1 = [0, 2]
              PidPair2 = [1, 3]
              PidPair3 = [0, 3]
              PidPair4 = [1, 2]
          # calculate the TLorentzVector and their sum of each possible pairs
          for particle in event:
              if particle.status == 1:
                  if ParticleCount1 in PidPair1:
                      p1 = FourMomentum(particle)
                      T1.append(R.TLorentzVector())
                      T1[PidCount1].SetPxPyPzE(p1.px, p1.py, p1.pz, p1.E)
                      T1Sum += T1[PidCount1]
                      PidCount1 += 1
                  elif ParticleCount1 in PidPair2:
                      p2 = FourMomentum(particle)
                      T2.append(R.TLorentzVector())
                      T2[PidCount2].SetPxPyPzE(p2.px, p2.py, p2.pz, p2.E)
                      T2Sum += T2[PidCount2]
                      PidCount2 += 1
                  # since each leptons were used twice to list all the possible pairs, do the "if" loop twice, too
                  if ParticleCount1 in PidPair3:
                      p3 = FourMomentum(particle)
                      T3.append(R.TLorentzVector())
                      T3[PidCount3].SetPxPyPzE(p3.px, p3.py, p3.pz, p3.E)
                      T3Sum += T3[PidCount3]
                      PidCount3 += 1
                      ParticleCount1 += 1
                  elif ParticleCount1 in PidPair4:
                      p4 = FourMomentum(particle)
                      T4.append(R.TLorentzVector())
                      T4[PidCount4].SetPxPyPzE(p4.px, p4.py, p4.pz, p4.E)
                      T4Sum += T4[PidCount4]
                      PidCount4 += 1
                      ParticleCount1 += 1

      # calculate the deltam of each possible pairs
      deltam1 = abs(T1Sum.M()-Zmass)
      deltam2 = abs(T2Sum.M()-Zmass)
      deltam3 = abs(T3Sum.M()-Zmass)
      deltam4 = abs(T4Sum.M()-Zmass)
      # calculate the Z mass and save them in a list
      m = [T1Sum.M(), T2Sum.M(), T3Sum.M(), T4Sum.M()]
      # save the deltam in a list
      deltam = [deltam1, deltam2, deltam3, deltam4]

      """
      take care of this code block, I have misunderstood the function named "sorted", see its explanation at https://blog.csdn.net/qq1195365047/article/details/90295660
      """
      # Sort the deltam in the list from small to large, and save the sort index values
      deltamSorts = sorted(range(len(deltam)), key=lambda k: deltam[k])

      # loop the deltamSorts, find "0", which represents the closest Z mass
      for i, deltamSort in enumerate(deltamSorts):
          # choose the Zmass which is closest to the real Zmass, fill it in the h_M1
          if i == 0:
              M1 = m[deltamSort]
              # list all the possible M2 and fill it in the h_M2
              if deltamSort == 0:
                  M2 = m[1]
              elif deltamSort == 1:
                  M2 = m[0]
              elif deltamSort == 2:
                  M2 = m[3]
              elif deltamSort == 3:
                  M2 = m[2]
      h_M1.Fill(M1)
      h_M2.Fill(M2)



      """
      block of 4th function: histogram the theta1 and theta2
      """
      # define 4 initial values to save the boosted sum TLorentzVector of 4 possible lepton pairs
      T1SumBoosted, T2SumBoosted, T3SumBoosted, T4SumBoosted = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
      # define an empty list to save all the boosted sum TLorentzVectors
      TSumBoosted = []
      # define 4 initial values to save the TLorentzVector of 4 leptons in each possible final states
      TM1_1st, TM1_2ed, TM2_1st, TM2_2ed = R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector(), R.TLorentzVector()
      # define 4 initial values to save the TLorentzVector to calculate the final boost
      # TM1 and TM2 represent the TLorentzVector of single e and single mu in each pair leptons in 4 leptons, TM3 and TM4 represent the others
      TM1, TM2 = R.TLorentzVector(), R.TLorentzVector()
      TM3, TM4 = R.TLorentzVector(), R.TLorentzVector()
      # define 4 initial values to save the cos of each leptons, Cos1 and Cos2 represents 1 e and 1 mu, Cos3 and Cos4 represents the others
      CosTheta1, CosTheta2 = 0, 0
      CosTheta3, CosTheta4 = 0, 0

      # boost the TLorentzVector of 4 possible lepton pairs, which were obtained in the block of 1st function
      T1SumBoosted = T1Sum.BoostVector()
      T2SumBoosted = T2Sum.BoostVector()
      T3SumBoosted = T3Sum.BoostVector()
      T4SumBoosted = T4Sum.BoostVector()
      # save the 4 possible boosted TLorentzVector in a list named as "TSumBoosted"
      TSumBoosted = [T1SumBoosted, T2SumBoosted, T3SumBoosted, T4SumBoosted]
      # find the sorts of M1 and M2, using "deltamSorts" which is defined in the block of 1st function
      for i, deltamSort in enumerate(deltamSorts):
          # choose the Boosted TLorentzVector of M1, named it as "TSumBoostM1"
          if i == 0:
              TSumBoostM1 = TSumBoosted[deltamSort]
              # list all the possible sort of M1 by using "if" and "elif" first, then list all the possible pairs for each possible sort of M1
              if deltamSort == 0:
                  # when deltamSort is 0, it represents that M1 is rebuilt from the 1st pair of leptons, so M2 would be rebuilt from the 2ed pair
                  # Name the leptons in 1st pair as "TM1_1st" and "TM1_2ed", the leptons in 2ed pair as "TM2_1st" and "TM2_2ed"
                  TM1_1st = T1[0]
                  TM1_2ed = T1[1]
                  TM2_1st = T2[0]
                  TM2_2ed = T2[1]
              elif deltamSort == 1:
                  # when deltamSort is 1, it represents that M1 is rebuilt from the 2ed pair of leptons, so M2 would be rebuilt from the 1st pair
                  TM1_1st = T2[0]
                  TM1_2ed = T2[1]
                  TM2_1st = T1[0]
                  TM2_2ed = T1[1]
              elif deltamSort == 2:
                  # when deltamSort is 2, it represents that M1 is rebuilt from the 3rd pair of leptons, so M2 would be rebuilt from the 4th pair
                  TM1_1st = T3[0]
                  TM1_2ed = T3[1]
                  TM2_1st = T4[0]
                  TM2_2ed = T4[1]
              elif deltamSort == 3:
                  # when deltamSort is 3, it represents that M1 is rebuilt from the 4th pair of leptons, so M2 would be rebuilt from the 3rd pair
                  TM1_1st = T4[0]
                  TM1_2ed = T4[1]
                  TM2_1st = T3[0]
                  TM2_2ed = T3[1]

              # list all the possible TSumBoostM2 for each possible M1 sort
              if deltamSort == 0:
                  TSumBoostM2 = TSumBoosted[1]
              elif deltamSort == 1:
                  TSumBoostM2 = TSumBoosted[0]
              elif deltamSort == 2:
                  TSumBoostM2 = TSumBoosted[3]
              elif deltamSort == 3:
                  TSumBoostM2 = TSumBoosted[2]
      TM1 = TM1_1st
      TM1.Boost(-TSumBoostM1)
      TM2 = TM2_1st
      TM2.Boost(-TSumBoostM2)
      CosTheta1 = TM1.CosTheta()
      CosTheta2 = TM2.CosTheta()
      h_CosTheta1.Fill(CosTheta1)
      h_CosTheta2.Fill(CosTheta2)

      TM3 = TM1_2ed
      TM3.Boost(-TSumBoostM1)
      TM4 = TM2_2ed
      TM4.Boost(-TSumBoostM2)
      CosTheta3 = TM3.CosTheta()
      CosTheta4 = TM4.CosTheta()
      h_CosTheta3.Fill(CosTheta3)
      h_CosTheta4.Fill(CosTheta4)


      """
      block of 2ed function: histogram the M1MOTHUP and M2MOTHUP
      """

      # define some initial values
      # define a list named as "Mother" to save the mother particles of final state particles.
      Mother = []
      # define a list named as "Mother1Index" and "Mother2Index" to save the index of 1st pair and 2ed pair of mother particles of final state particles.
      Mother1Index, Mother2Index = [], []
      # creat 2 empty lists of TLorentzVector to save the TLorentzVector of 2 pairs of leptons
      T1MOTHUP, T2MOTHUP = [], []
      # creat 2 empty TLorentzVectors of the sum of each pair of leptons
      T1MOTHUPSum, T2MOTHUPSum = R.TLorentzVector(), R.TLorentzVector()
      # define 2 initial values named as "MotherCount1" and"MotherCount2" to count the leptons in each pairs
      MotherCount1, MotherCount2 = 0, 0
      # define an initial value to count the particles in each event, "2" represents that it is the count of 2ed function block
      ParticleCount2 = 0
      # define 2 initial values named as "M1MOTHUP1", "M2MOTHUP" to save the Zmass which is rebuilt from leptons using MOTHUP. "M1" represent the closer one, "M2" is the another
      M1MOTHUP, M2MOTHUP = 0, 0
      # loop the particles in each events
      for particle in event:
          # distinguish the final state particles
          if particle.status == 1:
              # save the mother of each leptons in the list named "Mother"
              Mother.append(particle.mother1)
      # find the index of the leptons which have same mother with the first lepton, regard this mother is the 1st mother, another is the 2ed.
      Mother1Index = [x for (x,m) in enumerate(Mother) if m==Mother[0] ]
      if Mother[1] == Mother[0]:
          Mother2Index = [2, 3]
      elif Mother[2] == Mother[0]:
          Mother2Index = [1, 3]
      elif Mother[3] == Mother[0]:
          Mother2Index = [1, 2]

      for particle in event:
          if particle.status == 1:
              if ParticleCount2 in Mother1Index:
                  # create an empty TLorentzVector class for each selected particles
                  T1MOTHUP.append(R.TLorentzVector())
                  # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                  p1MOTHUP = FourMomentum(particle)
                  # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                  T1MOTHUP[MotherCount1].SetPxPyPzE(p1MOTHUP.px, p1MOTHUP.py, p1MOTHUP.pz, p1MOTHUP.E)
                  T1MOTHUPSum += T1MOTHUP[MotherCount1]
                  MotherCount1 += 1
                  ParticleCount2 += 1
              elif ParticleCount2 in Mother2Index:
                  # create an empty TLorentzVector class for each selected particles
                  T2MOTHUP.append(R.TLorentzVector())
                  # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                  p2MOTHUP = FourMomentum(particle)
                  # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                  T2MOTHUP[MotherCount2].SetPxPyPzE(p2MOTHUP.px, p2MOTHUP.py, p2MOTHUP.pz, p2MOTHUP.E)
                  T2MOTHUPSum += T2MOTHUP[MotherCount2]
                  MotherCount2 += 1
                  ParticleCount2 += 1


      if abs(T1MOTHUPSum.M() - Zmass) > abs(T2MOTHUPSum.M() - Zmass):
          M1MOTHUP = T2MOTHUPSum.M()
          M2MOTHUP = T1MOTHUPSum.M()
      else:
          M1MOTHUP = T1MOTHUPSum.M()
          M2MOTHUP = T2MOTHUPSum.M()
      h_M1MOTHUP.Fill(M1MOTHUP)
      h_M2MOTHUP.Fill(M2MOTHUP)



      """
      block of 3rd function: find the correct pair and the wrong pair, count it and calculate the accuracy
      """
      if M1MOTHUP == M1 and M2MOTHUP == M2:
          CorrectPair += 1
      else:
          WrongPair += 1

  print("CorrectPair", CorrectPair)
  print("WrongPair", WrongPair)
  # add ".0" to make sure that the result is a decimal
  Accuracy = CorrectPair/20000.0
  print("Accuracy", '%.2f%%' % (Accuracy * 100))

  # creat a ROOT file to histogram
  tfout = R.TFile("CosTheta.root", "RECREATE")
  tfout.cd()
  h_M1.Write()
  h_M2.Write()
  h_M1MOTHUP.Write()
  h_M2MOTHUP.Write()
  h_CosTheta1.Write()
  h_CosTheta2.Write()
  h_CosTheta3.Write()
  h_CosTheta4.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/pp_to_ZZ_para_added/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)

