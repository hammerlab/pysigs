#!/usr/bin/env python

from pandas import read_csv

def which_signatures(input_data_frame):
  return read_csv("../data/aocs-chemo-neoantigens/deconstructSigs_output.csv")
