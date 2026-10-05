import ROOT
from array import array

#Create a TTree
tree=ROOT.TTree("tree", "Basic TTree Practice")

#Create a float array to store pt values
pt=array('f', [0.])

#Create a branch connected to the pt array
tree.Branch("pt", pt, "pt/F")

#Generate and store event-by-event pt values
for i in range(1000):
  pt[0]=ROOT.gRandom.Gaus(30, 10)
  tree.Fill()

#Print the number of stored entries
print("Number of entries =", tree.GetEntries())
