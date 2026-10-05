import ROOT
from array import array

# Create a ROOT file
f = ROOT.TFile("pt_data.root", "RECREATE")

# Create a TTree
tree = ROOT.TTree("tree", "TFile I/O Practice")

# Create a float array and branch
pt = array('f', [0.])
tree.Branch("pt", pt, "pt/F")

# Generate and store pt values
for i in range(2000):
    pt[0] = ROOT.gRandom.Gaus(50, 15)
    tree.Fill()

# Write the tree to the ROOT file
tree.Write()
f.Close()

# Reopen the ROOT file
f = ROOT.TFile("pt_data.root", "READ")

# Retrieve the stored tree
tree = f.Get("tree")

# Create a histogram
h = ROOT.TH1F(
    "h",
    "Selected pt from ROOT file",
    50,
    0,
    100
)

# Read entries and apply a selection cut
for i in range(tree.GetEntries()):
    tree.GetEntry(i)

    if tree.pt > 40:
        h.Fill(tree.pt)

# Draw and save the result
c = ROOT.TCanvas(
    "c",
    "TFile I/O Practice",
    800,
    600
)

h.Draw()
c.SaveAs("pt_from_file.png")

f.Close()
