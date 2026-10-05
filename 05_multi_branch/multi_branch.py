import ROOT
from array import array

tree=ROOT.TTree("tree", "Multiple Branch Practice")

#Create arrays for two variables
pt=array('f', [0.])
eta=array('f', [0.])

tree.Branch("pt", pt, "pt/F")
tree.Branch("eta", eta, "eta/F")

#Generate and store event-by-event data
for i in range(2000):
  pt[0]=ROOT.gRandom.Gaus(40, 12)
  eta[0]=ROOT.gRandom.Uniform(-2.5, 2.5)
  tree.Fill()

h=ROOT.TH1F("h", "Selected pt:pt>30 and |eta|<1.5", 50, 0, 100)

#Read entries and apply combined selection cuts
for i in range(tree.GetEntries()):
  tree.GetEntry(i)
  if pt[0]>30 and abs(eta[0])<1.5:
    h.Fill(pt[0])

c=ROOT.TCanvas("c", "Multiple Branch Practice", 800, 600)

h.Draw()
c.SaveAs("multi_branch.png")
