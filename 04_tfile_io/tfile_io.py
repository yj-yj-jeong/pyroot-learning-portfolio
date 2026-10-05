import ROOT
from array import array

f=ROOT.TFile("pt_data.root", "RECREATE")

tree=ROOT.TTree("tree", "TFile I/O Practice")

pt=array('f', [0.])
tree.Branch("pt", pt, "pt/F")

for i in range(2000):
  pt[0]=ROOT.gRandom.Gaus(50, 15)
  tree.Fill

#Write the tree to the ROOT file
tree.Write()
f.Close()

#Reopen the ROOT file
f=ROOT.TFile("pt_data.root", "READ")

#Retrieve the stored tree
tree=f.Get("tree")

h=ROOT.TH1F("h", "Selected pt from ROOT file", 50, 0, 100)

#Read entries and apply a selection cut
for i in range(tree.GetEntries()):
  tree.GetEntries(i)
  if tree.pt>40:
    h.Fill(tree.pt)

c=ROOT.TCanvas("c", "TFile I/O Practice", 800, 600)
