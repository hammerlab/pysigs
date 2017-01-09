#!/usr/bin/env python

from pandas import read_csv
from datasets import signatures_cosmic

def which_signatures(tumor, sample_id,
                    contexts_needed = False,
                    signature_cutoff = 0.06,
                    tri_counts_method = "default",
                    signatures = signatures_cosmic):

  # Remove signatures from possibilities if they have a "strong" peak not seen 
  # in the tumor sample
  zero_contexts = tumor.columns[(tumor < 0.1).all()]
  sig_contexts = signatures[zero_contexts]
  signatures = signatures[(sig_contexts < 0.2).all(1)]
  return read_csv("../data/aocs-chemo-neoantigens/deconstructSigs_output.csv")
