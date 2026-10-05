import ROOT

#Creat a 1D histogram
h=ROOT.TH1F("h", "Gaussian Histogram",100,-5,5)

#Generate Gaussian-distributed random values
#Mean=0, Standard deviation=1
for i in range(10000):
  x=ROOT.gRandom.Gaus(0, 1)
  h.Fill(x)

#Define a Gaussian fitting function
fit_func=ROOT.TF1("fit_func","gaus",-3, 3)

#Fit the histogram within the specified range
h.Fit(fit_func, "R")

#Extract fitted parameters
mean=fit_func.GetParameter(1)
sigma=fit_func.GetParameter(2)

print("Fitted mean =", mean)
print("Fitted sigma =",sigma)

#Draw and save the histogram
c=ROOT.TCanvas("c", "Gaussian Histogram", 800, 600)

h.Draw()
c.SaveAs("gaussian_histogram.png")
