#!/usr/bin/env python

# import some modules
import sys, os
# import ROOT, creat an alias
import ROOT as R


def PlotDistribution(KinematicsName, InputROOTFile_Inclusive, InputROOTFile_TT, InputROOTFile_TL, InputROOTFile_LL):

  # Load each input ROOT file and open them
  ROOTFile_Inclusive = R.TFile.Open(InputROOTFile_Inclusive)
  ROOTFile_TT = R.TFile.Open(InputROOTFile_TT)
  ROOTFile_TL = R.TFile.Open(InputROOTFile_TL)
  ROOTFile_LL = R.TFile.Open(InputROOTFile_LL)

  # Get histograms in each ROOT file
  h_Inclusive = ROOTFile_Inclusive.Get("h_Inclusive")
  h_TT = ROOTFile_TT.Get("h_TT")
  h_TL = ROOTFile_TL.Get("h_TL")
  h_LL = ROOTFile_LL.Get("h_LL")
  #h_Inclusive = ROOTFile_Inclusive.Get("h_{KinematicsName}".format(KinematicsName = KinematicsName))
  #h_TT = ROOTFile_TT.Get("h_TT{KinematicsName}".format(KinematicsName = KinematicsName))
  #h_TL = ROOTFile_TL.Get("h_TL{KinematicsName}".format(KinematicsName = KinematicsName))
  #h_LL = ROOTFile_LL.Get("h_LL{KinematicsName}".format(KinematicsName = KinematicsName))

  # Remove the title in each histogram
  h_Inclusive.SetTitle("")
  h_TT.SetTitle("")
  h_TL.SetTitle("")
  h_LL.SetTitle("")

  # Get the entries of the 1st histogram, use it for scaling
  Entries = h_Inclusive.GetEntries()
  
  # scale all the histograms to yield
  h_Inclusive.Scale(0.02419*139*1000/Entries)
  h_TT.Scale(0.01688*139*1000/Entries)
  h_TL.Scale(0.005741*139*1000/Entries)
  h_LL.Scale(0.001406*139*1000/Entries)

  # Get the number of bins and the maximum and minimum of the x range
  nbins = h_Inclusive.GetNbinsX()
  xmax = h_Inclusive.GetXaxis().GetXmax()
  xmin = h_Inclusive.GetXaxis().GetXmin()

  # create a histogram to save the sum of TT,TL and LL
  h_Add = R.TH1F("TT+TL+LL", "", nbins, xmin, xmax)
  h_Add.Add(h_TT, 1)
  h_Add.Add(h_TL, 1)
  h_Add.Add(h_LL, 1)

  # create a series of histograms to save the histograms after dividing
  h_InclusiveDivide = R.TH1F("Divide", "", nbins, xmin, xmax)
  h_TTDivide = R.TH1F("TTDivide", "", nbins, xmin, xmax)
  h_TLDivide = R.TH1F("TLDivide", "", nbins, xmin, xmax)
  h_LLDivide = R.TH1F("LLDivide", "", nbins, xmin, xmax)
  h_AddDivide = R.TH1F("AddDivide", "", nbins, xmin, xmax)

  # create a series of histograms to save the histograms after dividing in ShapeOnly histograms
  h_InclusiveDivideShape = R.TH1F("DivideShape", "", nbins, xmin, xmax)
  h_TTDivideShape = R.TH1F("TTDivideShape", "", nbins, xmin, xmax)
  h_TLDivideShape = R.TH1F("TLDivideShape", "", nbins, xmin, xmax)
  h_LLDivideShape = R.TH1F("LLDivideShape", "", nbins, xmin, xmax)
  h_AddDivideShape = R.TH1F("AddDivideShape", "", nbins, xmin, xmax)

  # creat a THStack to stack the histogram of TT, TL and LL, set its name and title
  hs = R.THStack("hs", "")
  # since we should remove the line of histogram when stack them, I create a series of copied histograms in order to avoid changing the initial histogram.
  h_LLClone1 = h_LL.Clone("h_LLClone1")
  h_TLClone1 = h_TL.Clone("h_TLClone1")
  h_TTClone1 = h_TT.Clone("h_TTClone1")
  # set the width of histogram to zero
  h_LLClone1.SetLineWidth(0)
  h_TLClone1.SetLineWidth(0)
  h_TTClone1.SetLineWidth(0)
  # add these histograms to the THStack
  hs.Add(h_LLClone1, "Hist")
  hs.Add(h_TLClone1, "SameHist")
  hs.Add(h_TTClone1, "SameHist")

  # since we should renormalize all the histograms to 1 to see their shapes, I create a series of copied histograms in order to avoid changing the initial histogram.
  h_InclusiveClone2 = h_Inclusive.Clone("h_InclusiveClone2")
  h_TTClone2 = h_TT.Clone("h_TTClone2")
  h_TLClone2 = h_TL.Clone("h_TLClone2")
  h_LLClone2 = h_LL.Clone("h_LLClone2")
  h_AddClone2 = h_Add.Clone("h_AddClone2")

  # renormalize all the histograms to 1 to see their shapes
  h_InclusiveClone2.Scale(1/h_InclusiveClone2.Integral())
  h_TTClone2.Scale(1/h_TTClone2.Integral())
  h_TLClone2.Scale(1/h_TLClone2.Integral())
  h_LLClone2.Scale(1/h_LLClone2.Integral())
  h_AddClone2.Scale(1/h_AddClone2.Integral())

  # remove the Standard Deviation at upper right corner in each histogram
  R.gStyle.SetOptStat(0)



  """
  histogram of Inclusive, TT, TL, LL, TT+TL+LL
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_Sum = R.TCanvas("c_Sum", "Sum", 800, 1000)
  # set the background of this canvas
  c_Sum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs.Draw("Hist")
  h_Inclusive.Draw("SameHE")
  h_TT.Draw("SameHE")
  h_TL.Draw("SameHE")
  h_LL.Draw("SameHE")
  h_Add.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLClone1.SetFillColor(2)
  h_TLClone1.SetFillColor(3)
  h_TTClone1.SetFillColor(9)

  # set the line color of each histogram
  h_Inclusive.SetLineColor(1)
  h_TT.SetLineColor(7)
  h_TL.SetLineColor(11)
  h_LL.SetLineColor(5)
  h_Add.SetLineColor(46)
  # set the width of each histogram's line
  h_Inclusive.SetLineWidth(3)
  h_TT.SetLineWidth(3)
  h_TL.SetLineWidth(3)
  h_LL.SetLineWidth(3)
  h_Add.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs.GetXaxis().SetLabelFont(63)
  hs.GetXaxis().SetLabelSize(16)
  hs.GetYaxis().SetLabelFont(63)
  hs.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs.GetYaxis().SetTitle("Events")
  hs.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs.SetMaximum(int(hs.GetMaximum())*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.5, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_TTClone1, "TTStack", "F")
  leg.AddEntry(h_TLClone1, "TLStack", "F")
  leg.AddEntry(h_LLClone1, "LLStack", "F")
  leg.AddEntry(h_Inclusive,"Inclusive","LE")
  leg.AddEntry(h_TT,"TT","LE")
  leg.AddEntry(h_TL,"TL","LE")
  leg.AddEntry(h_LL,"LL","LE")
  leg.AddEntry(h_Add,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_Sum.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_InclusiveDivide.Divide(h_Inclusive, h_Add, 1, 1)
  h_TTDivide.Divide(h_TT, h_Add, 1, 1)
  h_TLDivide.Divide(h_TL, h_Add, 1, 1)
  h_LLDivide.Divide(h_LL, h_Add, 1, 1)
  h_AddDivide.Divide(h_Add, h_Add, 1 ,1)

  # draw the histograms of ratio
  h_InclusiveDivide.Draw("HE")
  h_TTDivide.Draw("SameHE")
  h_TLDivide.Draw("SameHE")
  h_LLDivide.Draw("SameHE")
  h_AddDivide.Draw("SameHE")
  # set the color of each histogram
  h_InclusiveDivide.SetLineColor(1)
  h_TTDivide.SetLineColor(7)
  h_TLDivide.SetLineColor(11)
  h_LLDivide.SetLineColor(5)
  h_AddDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_InclusiveDivide.SetLineWidth(3)
  h_TTDivide.SetLineWidth(3)
  h_TLDivide.SetLineWidth(3)
  h_LLDivide.SetLineWidth(3)
  h_AddDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_InclusiveDivide.GetXaxis().SetLabelFont(63)
  h_InclusiveDivide.GetXaxis().SetLabelSize(16)
  h_InclusiveDivide.GetYaxis().SetLabelFont(63)
  h_InclusiveDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis

  print("********************************************************************************************************")
  print("I'm going to plot the distribution of {KinematicsName}".format(KinematicsName = KinematicsName))
  print("-------------------------------Please select the unit of your Kinematics!-------------------------------")
  print("(1) If you want to choose 'GeV', please press 'g'")
  print("(2) If your Kinematics has no unit, please press 'n'")
  print("Since this script is python2, You must add '' to g or n, like 'g' or 'n', Don't say I didn't remind you!")
  print("********************************************************************************************************")
  UnitSelect = input("^_^ Please press:")
  if UnitSelect == "g":
      print(":D Well Done! You have already chosen 'GeV'!")
      h_InclusiveDivide.GetXaxis().SetTitle("{KinematicsName}/GeV".format(KinematicsName = KinematicsName))
  elif UnitSelect == "n":
      print(":D Well Done! You have already chosen 'no-unit'!")
      h_InclusiveDivide.GetXaxis().SetTitle("{KinematicsName}".format(KinematicsName = KinematicsName))
  else:
      print("O_o Oh my God, You stupid little boy! please press the correct button!!!")
      print("-_- You have only just one last chance, take care of it!")
      UnitSelect = input("Please press:")
      if UnitSelect == "g":
          print(":D Well Done! You have already chosen 'GeV'!")
          h_InclusiveDivide.GetXaxis().SetTitle("{KinematicsName}/GeV".format(KinematicsName = KinematicsName))
      elif UnitSelect == "n":
          print(":D Well Done! You have already chosen 'no-unit'!")
          h_InclusiveDivide.GetXaxis().SetTitle("{KinematicsName}".format(KinematicsName = KinematicsName))
      else:
          print("O_o Why are you make the same mistake again?! GoodBye!")

  h_InclusiveDivide.GetXaxis().SetTitleSize(0.07)
  h_InclusiveDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_InclusiveDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_InclusiveDivide.GetMaximum()
  Max2 = h_TTDivide.GetMaximum()
  Max3 = h_TLDivide.GetMaximum()
  Max4 = h_LLDivide.GetMaximum()
  Max5 = h_AddDivide.GetMaximum()
  Min1 = h_InclusiveDivide.GetMinimum()
  Min2 = h_TTDivide.GetMinimum()
  Min3 = h_TLDivide.GetMinimum()
  Min4 = h_LLDivide.GetMinimum()
  Min5 = h_AddDivide.GetMinimum()
  h_InclusiveDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_Sum.cd()

  # save the canvas as png file
  c_Sum.SaveAs("{KinematicsName}Sum.png".format(KinematicsName=KinematicsName))
  # close the canvas
  c_Sum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_SumShape = R.TCanvas("c_SumShape", "SumShape", 800, 1000)
  # set the background of this canvas
  c_SumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_InclusiveClone2.Draw("HE")
  h_TTClone2.Draw("SameHE")
  h_TLClone2.Draw("SameHE")
  h_LLClone2.Draw("SameHE")
  h_AddClone2.Draw("SameHE")

  # set the line color of each histogram
  h_InclusiveClone2.SetLineColor(1)
  h_TTClone2.SetLineColor(7)
  h_TLClone2.SetLineColor(11)
  h_LLClone2.SetLineColor(5)
  h_AddClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_InclusiveClone2.SetLineWidth(3)
  h_TTClone2.SetLineWidth(3)
  h_TLClone2.SetLineWidth(3)
  h_LLClone2.SetLineWidth(3)
  h_AddClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_InclusiveClone2.GetXaxis().SetLabelFont(63)
  h_InclusiveClone2.GetXaxis().SetLabelSize(16)
  h_InclusiveClone2.GetYaxis().SetLabelFont(63)
  h_InclusiveClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_InclusiveClone2.GetYaxis().SetTitle("freq.")
  h_InclusiveClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_InclusiveClone2.GetMaximum()
  Max2 = h_TTClone2.GetMaximum()
  Max3 = h_TLClone2.GetMaximum()
  Max4 = h_LLClone2.GetMaximum()
  Max5 = h_AddClone2.GetMaximum()
  h_InclusiveClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

  # add a legend at upper right corner
  # set the position of the legend
  leg = R.TLegend(0.7, 0.7, 0.9, 0.9)
  # draw legend without box
  leg.SetBorderSize(0)
  # remove the white background of the legend box
  leg.SetFillStyle(0)
  # add the content in the legend
  """
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
  """
  leg.AddEntry(h_InclusiveClone2,"Inclusive","LE")
  leg.AddEntry(h_TTClone2,"TT","LE")
  leg.AddEntry(h_TLClone2,"TL","LE")
  leg.AddEntry(h_LLClone2,"LL","LE")
  leg.AddEntry(h_AddClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_SumShape.cd()


  # create the 2ed pad, set name, title, xlow, ylow, xup, yup
  pad2 = R.TPad("pad2", "pad2", 0, 0, 1, 0.3)
  # set the margin between pad1 and pad2
  pad2.SetTopMargin(0)
  # set the margin below the pad2, so that it can print the legend of x axis
  pad2.SetBottomMargin(0.3)
  # draw the 2ed pad
  pad2.Draw()
  # enter this pad
  pad2.cd()

  # draw the histogram in this pad
  # use class Divide to calculate the ratio to TT+TL+LL, set the weight of 2 histograms
  h_InclusiveDivideShape.Divide(h_InclusiveClone2, h_AddClone2, 1, 1)
  h_TTDivideShape.Divide(h_TTClone2, h_AddClone2, 1, 1)
  h_TLDivideShape.Divide(h_TLClone2, h_AddClone2, 1, 1)
  h_LLDivideShape.Divide(h_LLClone2, h_AddClone2, 1, 1)
  h_AddDivideShape.Divide(h_AddClone2, h_AddClone2, 1 ,1)

  # draw the histograms of ratio
  h_InclusiveDivideShape.Draw("HE")
  h_TTDivideShape.Draw("SameHE")
  h_TLDivideShape.Draw("SameHE")
  h_LLDivideShape.Draw("SameHE")
  h_AddDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_InclusiveDivideShape.SetLineColor(1)
  h_TTDivideShape.SetLineColor(7)
  h_TLDivideShape.SetLineColor(11)
  h_LLDivideShape.SetLineColor(5)
  h_AddDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_InclusiveDivideShape.SetLineWidth(3)
  h_TTDivideShape.SetLineWidth(3)
  h_TLDivideShape.SetLineWidth(3)
  h_LLDivideShape.SetLineWidth(3)
  h_AddDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_InclusiveDivideShape.GetXaxis().SetLabelFont(63)
  h_InclusiveDivideShape.GetXaxis().SetLabelSize(16)
  h_InclusiveDivideShape.GetYaxis().SetLabelFont(63)
  h_InclusiveDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  if UnitSelect == "g":
      h_InclusiveDivideShape.GetXaxis().SetTitle("{KinematicsName}/GeV".format(KinematicsName = KinematicsName))
  elif UnitSelect == "n":
      h_InclusiveDivideShape.GetXaxis().SetTitle("{KinematicsName}".format(KinematicsName = KinematicsName))
  h_InclusiveDivideShape.GetXaxis().SetTitleSize(0.07)
  h_InclusiveDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_InclusiveDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_InclusiveDivideShape.GetMaximum()
  Max2 = h_TTDivideShape.GetMaximum()
  Max3 = h_TLDivideShape.GetMaximum()
  Max4 = h_LLDivideShape.GetMaximum()
  Max5 = h_AddDivideShape.GetMaximum()
  Min1 = h_InclusiveDivideShape.GetMinimum()
  Min2 = h_TTDivideShape.GetMinimum()
  Min3 = h_TLDivideShape.GetMinimum()
  Min4 = h_LLDivideShape.GetMinimum()
  Min5 = h_AddDivideShape.GetMinimum()
  h_InclusiveDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_SumShape.cd()


  # save the canvas as png file
  c_SumShape.SaveAs("{KinematicsName}ShapeOnly.png".format(KinematicsName = KinematicsName))
  # close the canvas
  c_SumShape.Close()

  # close the ROOT file
  ROOTFile_Inclusive.Close()
  ROOTFile_TT.Close()
  ROOTFile_TL.Close()
  ROOTFile_LL.Close()

if __name__ == "__main__":

  KinematicsName = "BDT"
  InputROOTFile_Inclusive = "/users/wuxingyu/desktop/WorkingSpace/h_Inclusive.root"
  InputROOTFile_TT = "/users/wuxingyu/desktop/WorkingSpace/h_TT.root"
  InputROOTFile_TL = "/users/wuxingyu/desktop/WorkingSpace/h_TL.root"
  InputROOTFile_LL = "/users/wuxingyu/desktop/WorkingSpace/h_LL.root"

PlotDistribution(KinematicsName, InputROOTFile_Inclusive, InputROOTFile_TT, InputROOTFile_TL, InputROOTFile_LL)



