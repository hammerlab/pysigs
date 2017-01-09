#!/usr/bin/env python

import unittest

from pandas import DataFrame

import pandas as pd
import tempfile
from which_signatures import which_signatures
import subprocess
#from datasets import signatures_cosmic

class test_deconstruct_sigs(unittest.TestCase):
  
  def test_whichSignatures_on_ovarian_cancer_data(self):
    input_data_frame \
      = pd.read_csv("../data/aocs-chemo-neoantigens/mutation_contexts_counts.csv")
    output_data_frame = which_signatures(input_data_frame)
    output_file, output_filename = tempfile.mkstemp(suffix="csv")
    output_data_frame.to_csv(output_filename)

    result = subprocess.call(["diff", 
                  "../data/aocs-chemo-neoantigens/deconstructSigs_output.csv",
                  output_filename])
    self.assertTrue(result == 0)
    

if __name__ == '__main__':
  unittest.main()
