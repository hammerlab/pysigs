#!/usr/bin/env python

import unittest

from pandas import DataFrame, read_csv

import pandas as pd
import tempfile
from which_signatures import which_signatures
import subprocess
from datasets import signatures_cosmic

class test_deconstruct_sigs(unittest.TestCase):
  
  def test_whichSignatures_on_ovarian_cancer_data(self):
    raw_my_signatures \
      = read_csv("../data/aocs-chemo-neoantigens/all_signatures.csv", 
                  index_col = 0)
    siglen = len("Signature")
    cosmic_signatures = [column for column in signatures_cosmic.columns if
    column[:siglen] == "Signature"]
    my_signatures = raw_my_signatures.loc[cosmic_signatures, :]
    input_data_frame \
      = read_csv("../data/aocs-chemo-neoantigens/mutation_contexts_counts.csv")
    input_data_frame = input_data_frame.set_index(['source_id', 'kind'])
    source_id_name = input_data_frame.columns[0]
    kind_name = input_data_frame.columns[-1]
    input_data_frame.drop(source_id_name, 1)
    input_data_frame.drop(kind_name, 1)
    
    first = True
    for sample in input_data_frame.index:
      output_row = which_signatures(tumor_ref = input_data_frame,
                                    sample_id = sample,
                                    contexts_needed = True,
                                    signature_cutoff = 0.0,
                                    tri_counts_method = "default",
                                    signatures_ref = my_signatures)
      if first:
        output_data_frame = output_row
        first = False
      else:
        output_data_frame.append(output_row)
    golden_output \
      = read_csv("../data/aocs-chemo-neoantigens/deconstructSigs_output.csv")
    self.assertTrue(golden_output.equals(output_data_frame))
    

if __name__ == '__main__':
  unittest.main()
