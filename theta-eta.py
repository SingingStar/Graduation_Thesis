#!/usr/bin/env python

# import some modules
import sys, os
import ROOT as R




# creat a new canvas named "myC", sign it with "C"
myC = R.TCanvas("C")
# enter this canvas
myC.cd()

# define the 3.14 as pi
pi = R.TMath.Pi()


# draw the plot, "log() represent ln(), use (0, pi) rather than (0, 180)"
graph = R.TF1("graph", "-log(tan(x/2))", 0, pi)
graph.SetTitle("theta-eta; theta; eta")
graph.Draw()

leg = R.TLegend(0.3,0.6,0.5,0.8)
leg.SetHeader("theta-eta","C")
leg.AddEntry("graph", "eta = -ln(tan(theta/2))")
leg.Draw()


myC.SaveAs("theta-eta.png")



