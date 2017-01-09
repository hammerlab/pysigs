#!/usr/bin/env python

from pandas import read_csv
from datasets import signatures_cosmic

def which_signatures(tumor_ref, sample_id,
                    contexts_needed = False,
                    signature_cutoff = 0.06,
                    tri_counts_method = "default",
                    signatures_ref = signatures_cosmic):
  return read_csv("../data/aocs-chemo-neoantigens/deconstructSigs_output.csv")
