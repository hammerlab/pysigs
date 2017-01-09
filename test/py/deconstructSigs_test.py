#!/usr/bin/env python

import unittest

from pandas import DataFrame, read_csv

import pandas as pd
import tempfile
from which_signatures import which_signatures
import subprocess
#from datasets import signatures_cosmic

class test_deconstruct_sigs(unittest.TestCase):
  
  def test_whichSignatures_on_ovarian_cancer_data(self):
    input_data_frame \
      = read_csv("../data/aocs-chemo-neoantigens/mutation_contexts_counts.csv")
    output_data_frame = which_signatures(input_data_frame)
    golden_output \
      = read_csv("../data/aocs-chemo-neoantigens/deconstructSigs_output.csv")
    self.assertTrue(golden_output.equals(output_data_frame))
    

if __name__ == '__main__':
  unittest.main()
