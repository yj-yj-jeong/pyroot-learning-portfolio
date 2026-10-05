# PyROOT Learning Portfolio

This repository documents my introductory practice with ROOT and PyROOT for scientific data analysis.

I studied physics at the undergraduate level and have been building practical programming and data-analysis skills in preparation for graduate-level research in experimental physics.

The purpose of this repository is to record the PyROOT concepts and analysis workflows that I have practiced directly while learning.

## Topics Covered

### 1. Histogram and Gaussian Distribution
- Creating one-dimensional histograms with `TH1F`
- Filling histograms with Gaussian random numbers
- Understanding bins, underflow, and overflow
- Drawing histograms using `TCanvas`
- Gaussian fitting using `TF1`
- Extracting fitted mean and standard deviation

### 2. TTree and Branch
- Creating a `TTree`
- Creating branches using Python `array`
- Storing event-by-event data using `tree.Fill()`
- Understanding branches and entries

### 3. Event Selection
- Reading entries using `GetEntries()` and `GetEntry()`
- Applying selection conditions such as `pt > 20`
- Filling histograms with selected events

### 4. ROOT File I/O
- Creating ROOT files using `TFile`
- Saving trees using `Write()`
- Reopening ROOT files
- Retrieving stored trees using `Get()`

### 5. Multiple Branches
- Handling variables such as `pt` and `eta`
- Applying combined selection conditions
- Building histograms from selected events

## Repository Structure

This repository contains practice scripts, output plots, and short notes created while learning PyROOT.

## Current Status

This is an ongoing learning portfolio.

My current focus is building a solid understanding of ROOT data structures and basic analysis workflows before moving on to real experimental datasets.

## Next Steps

- Practice with publicly available physics datasets
- Improve histogram fitting and statistical interpretation
- Learn more advanced TTree analysis
- Apply PyROOT to particle-physics data-analysis exercises
