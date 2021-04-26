#!/usr/bin/env python

# import some modules
import sys, os
# add MG5_aMC into the path and import the lhe_parser
sys.path.append("/users/wuxingyu/MG5_aMC_v2_9_2/")
from madgraph.various.lhe_parser import *
# import ROOT, creat an alias
import ROOT as R
# import array to save the address in class Branch
from array import array

def TMVAApply(InputFile):

  InputFile = R.TFile.Open("/users/wuxingyu/Desktop/WorkingSpace/KinematicQuantity_v4_Output/InclusiveTree.root")

  data = InputFile.Get("InclusiveTree")

  M1 = array("f", [0])
  M2 = array("f", [0])
  M4l = array("f", [0])
  CosTheta1 = array("f", [0])
  CosTheta2 = array("f", [0])
  Theta1 = array("f", [0])
  Theta2 = array("f", [0])
  ThetaStar1 = array("f", [0])
  ThetaStar2 = array("f", [0])
  CosThetaStar1 = array("f", [0])
  CosThetaStar2 = array("f", [0])
  Phi = array("f", [0])
  Phi1 = array("f", [0])
  CosPhi = array("f", [0])
  CosPhi1 = array("f", [0])
  Eta1 = array("f", [0])
  Eta2 = array("f", [0])
  Eta4l = array("f", [0])
  Pt1 = array("f", [0])
  Pt2 = array("f", [0])
  Pt4l = array("f", [0])
  deltaR1 = array("f", [0])
  deltaR2 = array("f", [0])
  MindeltaR = array("f", [0])
  Y1 = array("f", [0])
  Y2 = array("f", [0])
  deltaY = array("f", [0])



  data.SetBranchAddress("M1", M1)
  data.SetBranchAddress("M2", M2)
  data.SetBranchAddress("M4l", M4l)
  data.SetBranchAddress("CosTheta1", CosTheta1)
  data.SetBranchAddress("CosTheta2", CosTheta2)
  data.SetBranchAddress("Theta1", Theta1)
  data.SetBranchAddress("Theta2", Theta2)
  data.SetBranchAddress("ThetaStar1", ThetaStar1)
  data.SetBranchAddress("ThetaStar2", ThetaStar2)
  data.SetBranchAddress("CosThetaStar1", CosThetaStar1)
  data.SetBranchAddress("CosThetaStar2", CosThetaStar2)
  data.SetBranchAddress("Phi", Phi)
  data.SetBranchAddress("Phi1", Phi1)
  data.SetBranchAddress("CosPhi", CosPhi)
  data.SetBranchAddress("CosPhi1", CosPhi1)
  data.SetBranchAddress("Eta1", Eta1)
  data.SetBranchAddress("Eta2", Eta2)
  data.SetBranchAddress("Eta4l", Eta4l)
  data.SetBranchAddress("Pt1", Pt1)
  data.SetBranchAddress("Pt2", Pt2)
  data.SetBranchAddress("Pt4l", Pt4l)
  data.SetBranchAddress("deltaR1", deltaR1)
  data.SetBranchAddress("deltaR2", deltaR2)
  data.SetBranchAddress("MindeltaR", MindeltaR)
  data.SetBranchAddress("Y1", Y1)
  data.SetBranchAddress("Y2", Y2)
  data.SetBranchAddress("deltaY", deltaY)

  reader = R.TMVA.Reader("!Color:!Silent")
  reader.AddVariable("M1", M1)
  reader.AddVariable("M2", M2)
  reader.AddVariable("M4l", M4l)
  reader.AddVariable("CosTheta1", CosTheta1)
  reader.AddVariable("CosTheta2", CosTheta2)
  reader.AddVariable("Theta1", Theta1)
  reader.AddVariable("Theta2", Theta2)
  reader.AddVariable("ThetaStar1", ThetaStar1)
  reader.AddVariable("ThetaStar2", ThetaStar2)
  reader.AddVariable("CosThetaStar1", CosThetaStar1)
  reader.AddVariable("CosThetaStar2", CosThetaStar2)
  reader.AddVariable("Phi", Phi)
  reader.AddVariable("Phi1", Phi1)
  reader.AddVariable("CosPhi", CosPhi)
  reader.AddVariable("CosPhi1", CosPhi1)
  reader.AddVariable("Eta1", Eta1)
  reader.AddVariable("Eta2", Eta2)
  reader.AddVariable("Eta4l", Eta4l)
  reader.AddVariable("Pt1", Pt1)
  reader.AddVariable("Pt2", Pt2)
  reader.AddVariable("Pt4l", Pt4l)
  reader.AddVariable("deltaR1", deltaR1)
  reader.AddVariable("deltaR2", deltaR2)
  reader.AddVariable("MindeltaR", MindeltaR)
  reader.AddVariable("Y1", Y1)
  reader.AddVariable("Y2", Y2)
  reader.AddVariable("deltaY", deltaY)

  reader.BookMVA("BDT Method", "dataset/weights/TMVAClassification_BDT.weights.xml")

  h_Inclusive = R.TH1F("h_Inclusive", "h_Inclusive", 40, -1, 1)
  for i in range(0, data.GetEntries()):
      data.GetEntry(i)
      h_Inclusive.Fill(reader.EvaluateMVA("BDT Method"))

  tfout = R.TFile("h_Inclusive.root", "RECREATE")
  tfout.cd()
  
  h_Inclusive.Write()
  tfout.Close()
  InputFile.Close()

if __name__ == "__main__":

  InputFile = R.TFile("/users/wuxingyu/Desktop/WorkingSpace/KinematicQuantity_v5_Output/InclusiveTree.root")
  TMVAApply(InputFile=InputFile)
