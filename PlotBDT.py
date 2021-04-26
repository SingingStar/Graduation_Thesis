#!/usr/bin/env python

# import some modules
import sys, os
# import ROOT, creat an alias
import ROOT as R

def plot(InputROOTFile_Inclusive, InputROOTFile_TT, InputROOTFile_TL, InputROOTFile_LL):

  rootfile_Inclusive = R.TFile.Open(InputROOTFile_Inclusive)
  rootfile_TT = R.TFile.Open(InputROOTFile_TT)
  rootfile_TL = R.TFile.Open(InputROOTFile_TL)
  rootfile_LL = R.TFile.Open(InputROOTFile_LL)


  h_BDT = rootfile_Inclusive.Get("h_Inclusive")
  h_TTBDT = rootfile_TT.Get("h_TT")
  h_TLBDT = rootfile_TL.Get("h_TL")
  h_LLBDT = rootfile_LL.Get("h_LL")

  h_BDT.SetTitle("")
  h_TTBDT.SetTitle("")
  h_TLBDT.SetTitle("")
  h_LLBDT.SetTitle("")

  h_BDT.Scale(0.02419*139*1000/20000)
  h_TTBDT.Scale(0.01688*139*1000/20000)
  h_TLBDT.Scale(0.005741*139*1000/20000)
  h_LLBDT.Scale(0.001406*139*1000/20000)

  nbins, xmin, xmax = 40, -1, 1
  h_AddBDT = R.TH1F("TT+TL+LLBDT", "", nbins, xmin, xmax)
  h_AddBDT.Add(h_TTBDT, 1)
  h_AddBDT.Add(h_TLBDT, 1)
  h_AddBDT.Add(h_LLBDT, 1)

  h_BDTDivide = R.TH1F("BDTDivide", "", 40, -1, 1)
  h_TTBDTDivide = R.TH1F("TTBDTDivide", "", 40, -1, 1)
  h_TLBDTDivide = R.TH1F("TLBDTDivide", "", 40, -1, 1)
  h_LLBDTDivide = R.TH1F("LLBDTDivide", "", 40, -1, 1)
  h_AddBDTDivide = R.TH1F("AddBDTDivide", "", 40, -1, 1)

  h_BDTDivideShape = R.TH1F("BDTDivideShape", "", 40, -1, 1)
  h_TTBDTDivideShape = R.TH1F("TTBDTDivideShape", "", 40, -1, 1)
  h_TLBDTDivideShape = R.TH1F("TLBDTDivideShape", "", 40, -1, 1)
  h_LLBDTDivideShape = R.TH1F("LLBDTDivideShape", "", 40, -1, 1)
  h_AddBDTDivideShape = R.TH1F("AddBDTDivideShape", "", 40, -1, 1)

  # creat a THStack to stack the histogram of TT, TL and LL, set its name and title
  hs_BDT = R.THStack("hs_BDT", "")
  # since we should remove the line of histogram when stack them, I create a series of copied histograms in order to avoid changing the initial histogram.
  h_LLBDTClone1 = h_LLBDT.Clone("h_LLBDTClone1")
  h_TLBDTClone1 = h_TLBDT.Clone("h_TLBDTClone1")
  h_TTBDTClone1 = h_TTBDT.Clone("h_TTBDTClone1")
  # set the width of histogram to zero
  h_LLBDTClone1.SetLineWidth(0)
  h_TLBDTClone1.SetLineWidth(0)
  h_TTBDTClone1.SetLineWidth(0)
  # add these histograms to the THStack
  hs_BDT.Add(h_LLBDTClone1, "Hist")
  hs_BDT.Add(h_TLBDTClone1, "SameHist")
  hs_BDT.Add(h_TTBDTClone1, "SameHist")

  h_BDTClone2 = h_BDT.Clone("h_BDTClone2")
  h_TTBDTClone2 = h_TTBDT.Clone("h_TTBDTClone2")
  h_TLBDTClone2 = h_TLBDT.Clone("h_TLBDTClone2")
  h_LLBDTClone2 = h_LLBDT.Clone("h_LLBDTClone2")
  h_AddBDTClone2 = h_AddBDT.Clone("h_AddBDTClone2")

  h_BDTClone2.Scale(1/h_BDTClone2.Integral())
  h_TTBDTClone2.Scale(1/h_TTBDTClone2.Integral())
  h_TLBDTClone2.Scale(1/h_TLBDTClone2.Integral())
  h_LLBDTClone2.Scale(1/h_LLBDTClone2.Integral())
  h_AddBDTClone2.Scale(1/h_AddBDTClone2.Integral())

  # remove the Standard Deviation at upper right corner in each histogram
  R.gStyle.SetOptStat(0)



  """
  histogram of BDT, TTBDT, TLBDT, LLBDT, TT+TL+LLBDT
  """

  # create a canvas, set the name, title, pixels of x, pixels of y
  c_BDTSum = R.TCanvas("c_BDTSum", "BDTSum", 800, 1000)
  # set the background of this canvas
  c_BDTSum.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()


  # draw histograms in this pad
  hs_BDT.Draw("Hist")
  h_BDT.Draw("SameHE")
  h_TTBDT.Draw("SameHE")
  h_TLBDT.Draw("SameHE")
  h_LLBDT.Draw("SameHE")
  h_AddBDT.Draw("SameHE")

  # set the fill color of histogram TTClone, TLClone and LLClone, since it will be used in THStack
  h_LLBDTClone1.SetFillColor(2)
  h_TLBDTClone1.SetFillColor(3)
  h_TTBDTClone1.SetFillColor(9)

  # set the line color of each histogram
  h_BDT.SetLineColor(1)
  h_TTBDT.SetLineColor(7)
  h_TLBDT.SetLineColor(11)
  h_LLBDT.SetLineColor(5)
  h_AddBDT.SetLineColor(46)
  # set the width of each histogram's line
  h_BDT.SetLineWidth(3)
  h_TTBDT.SetLineWidth(3)
  h_TLBDT.SetLineWidth(3)
  h_LLBDT.SetLineWidth(3)
  h_AddBDT.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  hs_BDT.GetXaxis().SetLabelFont(63)
  hs_BDT.GetXaxis().SetLabelSize(16)
  hs_BDT.GetYaxis().SetLabelFont(63)
  hs_BDT.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  hs_BDT.GetYaxis().SetTitle("Events")
  hs_BDT.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  """
  A problem: hs_BDT.GetYaxis().SetRangeUser(0, 1000) seems not valid when the object is THStack, so I use SetMaximum
  """
  hs_BDT.SetMaximum(int(hs_BDT.GetMaximum())*1.2)

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
  leg.AddEntry(h_TTBDTClone1, "TTStack", "F")
  leg.AddEntry(h_TLBDTClone1, "TLStack", "F")
  leg.AddEntry(h_LLBDTClone1, "LLStack", "F")
  leg.AddEntry(h_BDT,"Inclusive","LE")
  leg.AddEntry(h_TTBDT,"TT","LE")
  leg.AddEntry(h_TLBDT,"TL","LE")
  leg.AddEntry(h_LLBDT,"LL","LE")
  leg.AddEntry(h_AddBDT,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_BDTSum.cd()


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
  h_BDTDivide.Divide(h_BDT, h_AddBDT, 1, 1)
  h_TTBDTDivide.Divide(h_TTBDT, h_AddBDT, 1, 1)
  h_TLBDTDivide.Divide(h_TLBDT, h_AddBDT, 1, 1)
  h_LLBDTDivide.Divide(h_LLBDT, h_AddBDT, 1, 1)
  h_AddBDTDivide.Divide(h_AddBDT, h_AddBDT, 1 ,1)

  # draw the histograms of ratio
  h_BDTDivide.Draw("HE")
  h_TTBDTDivide.Draw("SameHE")
  h_TLBDTDivide.Draw("SameHE")
  h_LLBDTDivide.Draw("SameHE")
  h_AddBDTDivide.Draw("SameHE")
  # set the color of each histogram
  h_BDTDivide.SetLineColor(1)
  h_TTBDTDivide.SetLineColor(7)
  h_TLBDTDivide.SetLineColor(11)
  h_LLBDTDivide.SetLineColor(5)
  h_AddBDTDivide.SetLineColor(46)
  # set the width of each histogram's line
  h_BDTDivide.SetLineWidth(3)
  h_TTBDTDivide.SetLineWidth(3)
  h_TLBDTDivide.SetLineWidth(3)
  h_LLBDTDivide.SetLineWidth(3)
  h_AddBDTDivide.SetLineWidth(3)
  # set the font and size of each axis
  h_BDTDivide.GetXaxis().SetLabelFont(63)
  h_BDTDivide.GetXaxis().SetLabelSize(16)
  h_BDTDivide.GetYaxis().SetLabelFont(63)
  h_BDTDivide.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_BDTDivide.GetXaxis().SetTitle("BDT/GeV")
  h_BDTDivide.GetXaxis().SetTitleSize(0.07)
  h_BDTDivide.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_BDTDivide.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_BDTDivide.GetMaximum()
  Max2 = h_TTBDTDivide.GetMaximum()
  Max3 = h_TLBDTDivide.GetMaximum()
  Max4 = h_LLBDTDivide.GetMaximum()
  Max5 = h_AddBDTDivide.GetMaximum()
  Min1 = h_BDTDivide.GetMinimum()
  Min2 = h_TTBDTDivide.GetMinimum()
  Min3 = h_TLBDTDivide.GetMinimum()
  Min4 = h_LLBDTDivide.GetMinimum()
  Min5 = h_AddBDTDivide.GetMinimum()
  h_BDTDivide.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_BDTSum.cd()

  # save the canvas as png file
  c_BDTSum.SaveAs("BDTSum.png")
  # close the canvas
  c_BDTSum.Close()


  # create a canvas, set the name, title, pixels of x, pixels of y
  c_BDTSumShape = R.TCanvas("c_BDTSumShape", "BDTSumShape", 800, 1000)
  # set the background of this canvas
  c_BDTSumShape.SetFillColor(0)

  # create the 1st pad, set name, title, xlow, ylow, xup, yup
  pad1 = R.TPad("pad1", "pad1", 0, 0.3, 1, 1)
  # set the margin below the pad1
  pad1.SetBottomMargin(0.01)
  # draw this pad
  pad1.Draw()
  # enter this pad
  pad1.cd()

  # draw histograms in this pad
  h_BDTClone2.Draw("HE")
  h_TTBDTClone2.Draw("SameHE")
  h_TLBDTClone2.Draw("SameHE")
  h_LLBDTClone2.Draw("SameHE")
  h_AddBDTClone2.Draw("SameHE")

  # set the line color of each histogram
  h_BDTClone2.SetLineColor(1)
  h_TTBDTClone2.SetLineColor(7)
  h_TLBDTClone2.SetLineColor(11)
  h_LLBDTClone2.SetLineColor(5)
  h_AddBDTClone2.SetLineColor(46)
  # set the width of each histogram's line
  h_BDTClone2.SetLineWidth(3)
  h_TTBDTClone2.SetLineWidth(3)
  h_TLBDTClone2.SetLineWidth(3)
  h_LLBDTClone2.SetLineWidth(3)
  h_AddBDTClone2.SetLineWidth(3)

  # Since we draw the THStack first, so we just need to change the range of THStack to make the Canvas suitable
  # set the font and size of each axis
  h_BDTClone2.GetXaxis().SetLabelFont(63)
  h_BDTClone2.GetXaxis().SetLabelSize(16)
  h_BDTClone2.GetYaxis().SetLabelFont(63)
  h_BDTClone2.GetYaxis().SetLabelSize(16)
  # set the size of y axis's title
  h_BDTClone2.GetYaxis().SetTitle("freq.")
  h_BDTClone2.GetYaxis().SetTitleSize(0.035)
  # set the range of y axis
  Max1 = h_BDTClone2.GetMaximum()
  Max2 = h_TTBDTClone2.GetMaximum()
  Max3 = h_TLBDTClone2.GetMaximum()
  Max4 = h_LLBDTClone2.GetMaximum()
  Max5 = h_AddBDTClone2.GetMaximum()
  h_BDTClone2.GetYaxis().SetRangeUser(0, max(Max1, Max2, Max3, Max4, Max5)*1.2)

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
  leg.AddEntry(h_BDTClone2,"Inclusive","LE")
  leg.AddEntry(h_TTBDTClone2,"TT","LE")
  leg.AddEntry(h_TLBDTClone2,"TL","LE")
  leg.AddEntry(h_LLBDTClone2,"LL","LE")
  leg.AddEntry(h_AddBDTClone2,"TT+TL+LL","LE")
  leg.Draw()

  # add another legend at upper left corner
  latex = R.TLatex()
  latex.SetTextSize(0.05)
  latex.DrawLatexNDC(0.2, 0.8, "#bf{#bf{#sqrt{s} = 13TeV, 139 fb^{-1}}}")

  # After finishing drawing histogram in 1st pad, enter the canvas
  c_BDTSumShape.cd()


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
  h_BDTDivideShape.Divide(h_BDTClone2, h_AddBDTClone2, 1, 1)
  h_TTBDTDivideShape.Divide(h_TTBDTClone2, h_AddBDTClone2, 1, 1)
  h_TLBDTDivideShape.Divide(h_TLBDTClone2, h_AddBDTClone2, 1, 1)
  h_LLBDTDivideShape.Divide(h_LLBDTClone2, h_AddBDTClone2, 1, 1)
  h_AddBDTDivideShape.Divide(h_AddBDTClone2, h_AddBDTClone2, 1 ,1)

  # draw the histograms of ratio
  h_BDTDivideShape.Draw("HE")
  h_TTBDTDivideShape.Draw("SameHE")
  h_TLBDTDivideShape.Draw("SameHE")
  h_LLBDTDivideShape.Draw("SameHE")
  h_AddBDTDivideShape.Draw("SameHE")
  # set the color of each histogram
  h_BDTDivideShape.SetLineColor(1)
  h_TTBDTDivideShape.SetLineColor(7)
  h_TLBDTDivideShape.SetLineColor(11)
  h_LLBDTDivideShape.SetLineColor(5)
  h_AddBDTDivideShape.SetLineColor(46)
  # set the width of each histogram's line
  h_BDTDivideShape.SetLineWidth(3)
  h_TTBDTDivideShape.SetLineWidth(3)
  h_TLBDTDivideShape.SetLineWidth(3)
  h_LLBDTDivideShape.SetLineWidth(3)
  h_AddBDTDivideShape.SetLineWidth(3)
  # set the font and size of each axis
  h_BDTDivideShape.GetXaxis().SetLabelFont(63)
  h_BDTDivideShape.GetXaxis().SetLabelSize(16)
  h_BDTDivideShape.GetYaxis().SetLabelFont(63)
  h_BDTDivideShape.GetYaxis().SetLabelSize(16)
  # set the title and title size of x axis and y axis
  h_BDTDivideShape.GetXaxis().SetTitle("BDT/GeV")
  h_BDTDivideShape.GetXaxis().SetTitleSize(0.07)
  h_BDTDivideShape.GetYaxis().SetTitle("Ratio to TT+TL+LL")
  h_BDTDivideShape.GetYaxis().SetTitleSize(0.07)
  # set the range of y axis
  Max1 = h_BDTDivideShape.GetMaximum()
  Max2 = h_TTBDTDivideShape.GetMaximum()
  Max3 = h_TLBDTDivideShape.GetMaximum()
  Max4 = h_LLBDTDivideShape.GetMaximum()
  Max5 = h_AddBDTDivideShape.GetMaximum()
  Min1 = h_BDTDivideShape.GetMinimum()
  Min2 = h_TTBDTDivideShape.GetMinimum()
  Min3 = h_TLBDTDivideShape.GetMinimum()
  Min4 = h_LLBDTDivideShape.GetMinimum()
  Min5 = h_AddBDTDivideShape.GetMinimum()
  h_BDTDivideShape.GetYaxis().SetRangeUser(min(Min1, Min2, Min3, Min4,Min5)*0.1, max(Max1, Max2, Max3, Max4, Max5)*1.2)
  # After finishing drawing histogram in 2ed pad, enter the canvas
  c_BDTSumShape.cd()


  # save the canvas as png file
  c_BDTSumShape.SaveAs("BDTShapeOnly.png")
  # close the canvas
  c_BDTSumShape.Close()

  rootfile_Inclusive.Close()
  rootfile_TT.Close()
  rootfile_TL.Close()
  rootfile_LL.Close()

if __name__ == "__main__":

  InputROOTFile_Inclusive = "/users/wuxingyu/desktop/WorkingSpace/h_Inclusive.root"
  InputROOTFile_TT = "/users/wuxingyu/desktop/WorkingSpace/h_TT.root"
  InputROOTFile_TL = "/users/wuxingyu/desktop/WorkingSpace/h_TL.root"
  InputROOTFile_LL = "/users/wuxingyu/desktop/WorkingSpace/h_LL.root"
  # InputROOTFile="Angle_v4.root"
  plot(InputROOTFile_Inclusive, InputROOTFile_TT, InputROOTFile_TL, InputROOTFile_LL)



