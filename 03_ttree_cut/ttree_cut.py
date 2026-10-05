import ROOT
from array import array

#Create a TTree
tree=ROOT.TTree("tree", "TTree Cut Practice")

#Create a float array for pt
pt=array('f', [0.])

#Create the pt branch
tree.Branch("pt", pt, "pt/F")

#Generate and store pt values
for i in range(1000):
  pt[0]=ROOT.gRandom.Gaus(30, 10)
  tree.Fill()

#Create a histogram for selected events
h=ROOT.TH1F("h", "Selected pt: pt>20", 50, 0, 100)

#Read all entries and apply a selection cut
for i in range(tree.GetEntries()):
  tree.GetEntry(i)
  if pt[0]>20:
    h.Fill(pt[0])

#Draw and save the selected distribution
c=ROOT.TCanvas("c", "TTree Cut Practice", 800, 600)

h.Draw()
c.SaveAs("ttree_cut.png")
