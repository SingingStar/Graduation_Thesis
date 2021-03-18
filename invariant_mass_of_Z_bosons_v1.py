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
  # define an initial value to count 4e events, "fe" represents four electrons
  fe_count = 0
  # define an initial value to count 4mu events, "fm" represents four muons
  fmu_count = 0
  # define an initial value to count 2e2mu events, "tetmu" represents two electrons and two muons
  tetmu_count = 0

  # define a list named as "fe_event" to save the events whose final state has 4 electrons, so that we can distinguish the 3 types of final states.
  fe_event = []
  # define a list named as "T_fe" to save the TLorentzVectors of each electrons in 4 electrons.
  T_fe = []
  # define a list named as "fmu_event" to save the events whose final state has 4 muons, so that we can distinguish the 3 types of final states.
  fmu_event = []
  # define a list named as "T_fmu" to save the TLorentzVectors of each muons in 4 muons.
  T_fmu = []
  # define a list named as "tetmu_event" to save the events whose final state has 2 electrons and 2 muons, so that we can distinguish the 3 types of final states.
  tetmu_event = []
  # define a list named as "T_tetmu" to save the TLorentzVectors of 2 electrons and 2 muons.
  T_tetmu = []

  """
  histogram of the closer invariant mass of Z bosons whose final state has 4 electrons, using particleID to distinguish the Z boson
  """
  # define htitle = "closer_Zmass_fe_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "closer_Zmass_fe_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_fe_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_fe_pid = R.TH1F("closer_Zmass_fe_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_fe_pid.SetTitle("closer_Zmass_fe_pid;closer_Zmass/Gev;count")

  """
  histogram of the further invariant mass of Z bosons whose final state has 4 electrons, using particleID to distinguish the Z boson
  """
  # define htitle = "further_Zmass_fe_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "further_Zmass_fe_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_fe_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_fe_pid = R.TH1F("further_Zmass_fe_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_fe_pid.SetTitle("further_Zmass_fe_pid;futher_Zmass/Gev;count")

  """
  histogram of the closer invariant mass of Z bosons whose final state has 4 electrons
  """
  # define htitle = "closer_Zmass_fe", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "closer_Zmass_fe"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_fe" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_fe = R.TH1F("closer_Zmass_fe", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_fe.SetTitle("closer_Zmass_fe;closer_Zmass/Gev;count")

  """
  histogram of the further invariant mass of Z bosons whose final state has 4 electrons
  """
  # define htitle = "further_Zmass_fe", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "further_Zmass_fe"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_fe" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_fe = R.TH1F("further_Zmass_fe", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_fe.SetTitle("further_Zmass_fe;further_Zmass/Gev;count")

  """
  histogram of the closer invariant mass of Z bosons whose final state has 4 muons, using particleID to distinguish the Z boson
  """
  # define htitle = "closer_Zmass_fmu_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "closer_Zmass_fmu_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_fmu_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_fmu_pid = R.TH1F("closer_Zmass_fmu_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_fmu_pid.SetTitle("closer_Zmass_fmu_pid;closer_Zmass/Gev;count")

  """
  histogram of the further invariant mass of Z bosons whose final state has 4 muons, using particleID to distinguish the Z boson
  """
  # define htitle = "further_Zmass_fmu_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "further_Zmass_fmu_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_fmu_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_fmu_pid = R.TH1F("further_Zmass_fmu_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_fmu_pid.SetTitle("further_Zmass_fmu_pid;futher_Zmass/Gev;count")

  """
  histogram of the closer invariant mass of Z bosons whose final state has 4 muons
  """
  # define htitle = "closer_Zmass_fmu", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "closer_Zmass_fmu"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_fmu" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_fmu = R.TH1F("closer_Zmass_fmu", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_fmu.SetTitle("closer_Zmass_fmu;closer_Zmass/Gev;count")


  """
  histogram of the further invariant mass of Z bosons whose final state has 4 muons
  """
  # define htitle = "further_Zmass_fmu", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "further_Zmass_fmu"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_fmu" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_fmu = R.TH1F("further_Zmass_fmu", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_fmu.SetTitle("further_Zmass_fmu;further_Zmass/Gev;count")

  """
  histogram of the closer invariant mass of Z bosons whose final state has 2 electrons and 2 muons, using particleID to distinguish the Z boson
  """
  # define htitle = "closer_Zmass_tetmu_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "closer_Zmass_tetmu_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_tetmu_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_tetmu_pid = R.TH1F("closer_Zmass_tetmu_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_tetmu_pid.SetTitle("closer_Zmass_tetmu_pid;closer_Zmass/Gev;count")

  """
  histogram of the further invariant mass of Z bosons whose final state has 2 electrons and 2 muons, using particleID to distinguish the Z boson
  """
  # define htitle = "further_Zmass_tetmu_pid", and use it to fill in the 2ed parameter in the class TH1F, the "pid" in the title means using particleID = 23 to distinguish the Z boson
  htitle = "further_Zmass_tetmu_pid"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_tetmu_pid" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_tetmu_pid = R.TH1F("further_Zmass_tetmu_pid", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_tetmu_pid.SetTitle("further_Zmass_tetmu_pid;futher_Zmass/Gev;count")

  """
  histogram of the closer invariant mass of Z bosons whose final state has 2 electrons and 2 muons
  """
  # define htitle = "closer_Zmass_tetmu", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "closer_Zmass_tetmu"
  nbins, xmin, xmax = 100, 0, 200
  # "closer_Zmass_tetmu" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_closer_Zmass_tetmu = R.TH1F("closer_Zmass_tetmu", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_closer_Zmass_tetmu.SetTitle("closer_Zmass_tetmu;closer_Zmass/Gev;count")

  """
  histogram of the further invariant mass of Z bosons whose final state has 2 electrons and 2 muons
  """
  # define htitle = "further_Zmass_tetmu", and use it to fill in the 2ed parameter in the class TH1F
  htitle = "further_Zmass_tetmu"
  nbins, xmin, xmax = 100, 0, 200
  # "further_Zmass_tetmu" represents the name of the histogram, it's different from the title, which is the 2ed parameter in the TH1F
  h_further_Zmass_tetmu = R.TH1F("further_Zmass_tetmu", htitle, nbins, xmin, xmax)
  # set the title of the histogram
  # the first parameter of function SetTitle is the title of the histogram, the 2ed is the name of x, the 3rd is the name of y
  h_further_Zmass_tetmu.SetTitle("further_Zmass_tetmu;further_Zmass/Gev;count")


  # loop the events
  for event in lhe:
      # define a list named as "particle_ID" to save the ID of each final state particles in each events.
      particle_ID = []
      """
      Due to the reason refer to the lhe_parser's notes that "mother1/mother2 will be modified by the Event parse function to replace the integer by a pointer to actual particle object
      when I type "particle.mother", it means the whole particle information.
      So it's necessary to define a list to save the mother particles of final state particles and finally disitinguish the particles which have the same mother.
      """
      # define a list named as "mother" to save the mother particles of final state particles.
      mother = []
      # define a list named as "index_1st_mother" to save the index of 1st mother particles of final state particles.
      index_1st_mother = []
      # define a list named as "index_2ed_mother" to save the index of 2ed mother particles of final state particles.
      index_2ed_mother = []

      # loop the particles in each events
      for particle in event:

          # distinguish the final state particles
          if particle.status == 1:
              # save the particle_ID of the particle, so that you can distinguish the 3 different final states.
              particle_ID.append(abs(particle.pid))
              mother.append(particle.mother1)
      # find the index of the final state particles which have same mother with the first particle, regard this mother is the 1st mother, another is the 2ed.
      index_1st_mother = [x for (x,m) in enumerate(mother) if m==mother[0] ]
      if mother[1] == mother[0]:
          index_2ed_mother = [2, 3]
      elif mother[2] == mother[0]:
          index_2ed_mother = [1, 3]
      elif mother[3] == mother[0]:
          index_2ed_mother = [1, 2]

      """
      distinguish the 3 different final states and save the different types of event.
      """

      # first type of final states: 4 electrons
      if particle_ID == [11, 11, 11, 11]:
          fe_event.append(event)
          # define a list named as "T_fe_pid" to save the TLorentzVectors of 2 Z bosons when using particleID to distinguish the Z bosons.
          T_fe_pid = []
          # define a list named as "T_fe1" to save the TLorentzVectors of first two electrons
          T_fe1 = []
          # define a list named as "T_fe2" to save the TLorentzVectors of second two electrons
          T_fe2 = []
          # create an empty TLorentzVector class for the sum of 1st 4e
          T_sum_1st_fe = R.TLorentzVector()
          # create an empty TLorentzVector class for the sum of 2ed 4e
          T_sum_2ed_fe = R.TLorentzVector()
          # define a list named as "invariant_mass_fe_pid" to save the invariant mass of 2 Z bosons when using particleID to distinguish the Z bosons.
          invariant_mass_fe_pid = []
          # define an initial value to count 4e events when using particleID to distinguish the Z bosons, "fe" represents four electrons
          fe_count_pid = 0
          # define an initial value to count 4e events, "fe" represents four electrons
          fe_count1 = 0
          # define an initial value to count 4e events, "fe" represents four electrons
          fe_count2 = 0
          # define an initial value named as "particle_count" to save the paritcle count
          particle_count = 0

          """
          histogram the 2 Z mass of 4 electrons using particleID pid = 23
          """
          for particle in event:
              if particle.pid == 23:
                  T_fe_pid.append(R.TLorentzVector())
                  p_fe_pid = FourMomentum(particle)
                  T_fe_pid[fe_count_pid].SetPxPyPzE(p_fe_pid.px, p_fe_pid.py, p_fe_pid.pz, p_fe_pid.E)
                  invariant_mass_fe_pid.append(T_fe_pid[fe_count_pid].M())
                  fe_count_pid += 1
          if abs(invariant_mass_fe_pid[0] - Zmass) > abs(invariant_mass_fe_pid[1] - Zmass):
              h_closer_Zmass_fe_pid.Fill(invariant_mass_fe_pid[1])
              h_further_Zmass_fe_pid.Fill(invariant_mass_fe_pid[0])
          else:
              h_closer_Zmass_fe_pid.Fill(invariant_mass_fe_pid[0])
              h_further_Zmass_fe_pid.Fill(invariant_mass_fe_pid[1])

          """
          histogram the 2 Z mass of 4 electrons using MOTHUP
          """
          for particle in event:
              if particle.status == 1:
                  if particle_count in index_1st_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_fe1.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_fe = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_fe1[fe_count1].SetPxPyPzE(p_fe.px, p_fe.py, p_fe.pz, p_fe.E)
                      T_sum_1st_fe += T_fe1[fe_count1]
                      fe_count1 += 1
                      particle_count += 1
                  elif particle_count in index_2ed_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_fe2.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_fe = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_fe2[fe_count2].SetPxPyPzE(p_fe.px, p_fe.py, p_fe.pz, p_fe.E)
                      T_sum_2ed_fe += T_fe2[fe_count2]
                      fe_count2 += 1
                      particle_count += 1

          # invariant_mass_1st_fe = T_sum_1st_fe.M()
          # invariant_mass_2ed_fe = T_sum_2ed_fe.M()
          if abs(T_sum_1st_fe.M() - Zmass) > abs(T_sum_2ed_fe.M() - Zmass):
              h_closer_Zmass_fe.Fill(T_sum_2ed_fe.M())
              h_further_Zmass_fe.Fill(T_sum_1st_fe.M())
          else:
              h_closer_Zmass_fe.Fill(T_sum_1st_fe.M())
              h_further_Zmass_fe.Fill(T_sum_2ed_fe.M())
          fe_count += 1


      # second type of final states: 4 muons
      elif particle_ID == [13, 13, 13, 13]:
          fmu_event.append(event)
          # define a list named as "T_fmu_pid" to save the TLorentzVectors of 2 Z bosons when using particleID to distinguish the Z bosons.
          T_fmu_pid = []
          # define a list named as "T_fmu1" to save the TLorentzVectors of first two muons
          T_fmu1 = []
          # define a list named as "T_fmu2" to save the TLorentzVectors of second two muons
          T_fmu2 = []
          # create an empty TLorentzVector class for the sum of 1st 4mu
          T_sum_1st_fmu = R.TLorentzVector()
          # create an empty TLorentzVector class for the sum of 2ed 4mu
          T_sum_2ed_fmu = R.TLorentzVector()
          # define a list named as "invariant_mass_fmu_pid" to save the invariant mass of 2 Z bosons when using particleID to distinguish the Z bosons.
          invariant_mass_fmu_pid = []
          # define an initial value to count 4mu events when using particleID to distinguish the Z bosons, "fmu" represents four electrons
          fmu_count_pid = 0
          # define an initial value to count 4mu events, "fmu" represents four muons
          fmu_count1 = 0
          # define an initial value to count 4mu events, "fmu" represents four muons
          fmu_count2 = 0
          # define an initial value named as "particle_count" to save the paritcle count
          particle_count = 0

          """
          histogram the 2 Z mass of 4 muons using particleID pid = 23
          """
          for particle in event:
              if particle.pid == 23:
                  T_fmu_pid.append(R.TLorentzVector())
                  p_fmu_pid = FourMomentum(particle)
                  T_fmu_pid[fmu_count_pid].SetPxPyPzE(p_fmu_pid.px, p_fmu_pid.py, p_fmu_pid.pz, p_fmu_pid.E)
                  invariant_mass_fmu_pid.append(T_fmu_pid[fmu_count_pid].M())
                  fmu_count_pid += 1
          if abs(invariant_mass_fmu_pid[0] - Zmass) > abs(invariant_mass_fmu_pid[1] - Zmass):
              h_closer_Zmass_fmu_pid.Fill(invariant_mass_fmu_pid[1])
              h_further_Zmass_fmu_pid.Fill(invariant_mass_fmu_pid[0])
          else:
              h_closer_Zmass_fmu_pid.Fill(invariant_mass_fmu_pid[0])
              h_further_Zmass_fmu_pid.Fill(invariant_mass_fmu_pid[1])

          """
          histogram the 2 Z mass of 4 muons using MOTHUP
          """
          for particle in event:
              if particle.status == 1:
                  if particle_count in index_1st_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_fmu1.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_fmu = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_fmu1[fmu_count1].SetPxPyPzE(p_fmu.px, p_fmu.py, p_fmu.pz, p_fmu.E)
                      T_sum_1st_fmu += T_fmu1[fmu_count1]
                      fmu_count1 += 1
                      particle_count += 1
                  elif particle_count in index_2ed_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_fmu2.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_fmu = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_fmu2[fmu_count2].SetPxPyPzE(p_fmu.px, p_fmu.py, p_fmu.pz, p_fmu.E)
                      T_sum_2ed_fmu += T_fmu2[fmu_count2]
                      fmu_count2 += 1
                      particle_count += 1

          # invariant_mass_1st_fmu = T_sum_1st_fmu.M()
          # invariant_mass_2ed_fmu = T_sum_2ed_fmu.M()
          if abs(T_sum_1st_fmu.M() - Zmass) > abs(T_sum_2ed_fmu.M() - Zmass):
              h_closer_Zmass_fmu.Fill(T_sum_2ed_fmu.M())
              h_further_Zmass_fmu.Fill(T_sum_1st_fmu.M())
          else:
              h_closer_Zmass_fmu.Fill(T_sum_1st_fmu.M())
              h_further_Zmass_fmu.Fill(T_sum_2ed_fmu.M())
          fmu_count += 1


      # third type of final states: 2 electrons and 2 muons
      elif sorted(particle_ID, reverse=True) == [13, 13, 11, 11]:
          tetmu_event.append(event)
          # define a list named as "T_tetmu_pid" to save the TLorentzVectors of 2 Z bosons when using particleID to distinguish the Z bosons.
          T_tetmu_pid = []
          # define a list named as "T_tetmu1" to save the TLorentzVectors of first two leptons
          T_tetmu1 = []
          # define a list named as "T_tetmu2" to save the TLorentzVectors of second two leptons
          T_tetmu2 = []
          # create an empty TLorentzVector class for the sum of 1st two leptons
          T_sum_1st_tetmu = R.TLorentzVector()
          # create an empty TLorentzVector class for the sum of 2ed two leptons
          T_sum_2ed_tetmu = R.TLorentzVector()
          # define a list named as "invariant_mass_tetmu_pid" to save the invariant mass of 2 Z bosons when using particleID to distinguish the Z bosons.
          invariant_mass_tetmu_pid = []
          # define an initial value to count 2e2mu events when using particleID to distinguish the Z bosons, "tetmu" represents two electrons and two muons
          tetmu_count_pid = 0
          # define an initial value to count 2e2mu events, "tetmu" represents two electrons and two muons
          tetmu_count1 = 0
          # define an initial value to count 2e2mu events, "tetmu" represents two electrons and two muons
          tetmu_count2 = 0
          # define an initial value named as "particle_count" to save the paritcle count
          particle_count = 0

          """
          histogram the 2 Z mass of 2 electrons and 2 muons using particleID pid = 23
          """
          for particle in event:
              if particle.pid == 23:
                  T_tetmu_pid.append(R.TLorentzVector())
                  p_tetmu_pid = FourMomentum(particle)
                  T_tetmu_pid[tetmu_count_pid].SetPxPyPzE(p_tetmu_pid.px, p_tetmu_pid.py, p_tetmu_pid.pz, p_tetmu_pid.E)
                  invariant_mass_tetmu_pid.append(T_tetmu_pid[tetmu_count_pid].M())
                  tetmu_count_pid += 1
          if abs(invariant_mass_tetmu_pid[0] - Zmass) > abs(invariant_mass_tetmu_pid[1] - Zmass):
              h_closer_Zmass_tetmu_pid.Fill(invariant_mass_tetmu_pid[1])
              h_further_Zmass_tetmu_pid.Fill(invariant_mass_tetmu_pid[0])
          else:
              h_closer_Zmass_tetmu_pid.Fill(invariant_mass_tetmu_pid[0])
              h_further_Zmass_tetmu_pid.Fill(invariant_mass_tetmu_pid[1])

          """
          histogram the 2 Z mass of 2 electrons and 2 muons using MOTHUP
          """
          for particle in event:
              if particle.status == 1:
                  if particle_count in index_1st_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_tetmu1.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_tetmu = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_tetmu1[tetmu_count1].SetPxPyPzE(p_tetmu.px, p_tetmu.py, p_tetmu.pz, p_tetmu.E)
                      T_sum_1st_tetmu += T_tetmu1[tetmu_count1]
                      tetmu_count1 += 1
                      particle_count += 1
                  elif particle_count in index_2ed_mother:
                      # create an empty TLorentzVector class for each selected particles
                      T_tetmu2.append(R.TLorentzVector())
                      # use class FourMomentum which is defined in the lhe_parser.py to read the fourmomentum of the particle
                      p_tetmu = FourMomentum(particle)
                      # pick out the px, py, pz and E, assign a value to the previously created empty function R.TLorentzVector(), which is listed in the list T
                      T_tetmu2[tetmu_count2].SetPxPyPzE(p_tetmu.px, p_tetmu.py, p_tetmu.pz, p_tetmu.E)
                      T_sum_2ed_tetmu += T_tetmu2[tetmu_count2]
                      tetmu_count2 += 1
                      particle_count += 1

          # invariant_mass_1st_tetmu = T_sum_1st_tetmu.M()
          # invariant_mass_2ed_tetmu = T_sum_2ed_tetmu.M()
          if abs(T_sum_1st_tetmu.M() - Zmass) > abs(T_sum_2ed_tetmu.M() - Zmass):
              h_closer_Zmass_tetmu.Fill(T_sum_2ed_tetmu.M())
              h_further_Zmass_tetmu.Fill(T_sum_1st_tetmu.M())
          else:
              h_closer_Zmass_tetmu.Fill(T_sum_1st_tetmu.M())
              h_further_Zmass_tetmu.Fill(T_sum_2ed_tetmu.M())
          tetmu_count += 1

  # print out the number of 3 types of final states
  print("fe_count", fe_count)
  print("fmu_count", fmu_count)
  print("tetmu_count", tetmu_count)


  #creat a ROOT file to histogram
  tfout = R.TFile("invariant_mass_of_Z_bosons_v1.root", "RECREATE")
  tfout.cd()
  h_closer_Zmass_fe_pid.Write()
  h_further_Zmass_fe_pid.Write()
  h_closer_Zmass_fe.Write()
  h_further_Zmass_fe.Write()
  h_closer_Zmass_fmu_pid.Write()
  h_further_Zmass_fmu_pid.Write()
  h_closer_Zmass_fmu.Write()
  h_further_Zmass_fmu.Write()
  h_closer_Zmass_tetmu_pid.Write()
  h_further_Zmass_tetmu_pid.Write()
  h_closer_Zmass_tetmu.Write()
  h_further_Zmass_tetmu.Write()
  tfout.Close()


if __name__ == "__main__":

  input_file="/users/wuxingyu/Desktop/pp_to_ZZ_para_added/Events/run_01/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)


