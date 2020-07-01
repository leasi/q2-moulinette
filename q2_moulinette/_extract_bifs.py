# -*- coding: iso-8859-15 -*-
# ----------------------------------------------------------------------------
# Copyright (c) 2020, L. Siegwald, F. Foata, B. Berger
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2
from q2_types.feature_data import FeatureData, Sequence, Taxonomy

def extract_bifs(ctx, rep_seqs, taxonomy):
    filter_seqs=ctx.get_action('taxa', 'filter_seqs')
    bifs_seqs_results = filter_seqs(sequences=rep_seqs, taxonomy=taxonomy, include='Bifidobacterium')
    filtered_bifs_seqs = bifs_seqs_results.filtered_sequences
    return filtered_bifs_seqs