# -*- coding: iso-8859-15 -*-
# ----------------------------------------------------------------------------
# Copyright (c) 2020, L. Siegwald, F. Foata, B. Berger
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
# TODO: add proper citations

import qiime2
from q2_types.feature_data import FeatureData, Sequence, Taxonomy, AlignedSequence
import q2_moulinette
from q2_moulinette._extract_bifs import extract_bifs
from q2_moulinette._align_mothur import align_mothur


plugin = qiime2.plugin.Plugin(
    name='moulinette',
    version=q2_moulinette.__version__,
    website='http://www.github.com/cduvallet/q2-perc-norm',
    package='q2_moulinette',
    description=('This QIIME 2 plugin performs a model-free normalization '
                 'procedure where features (i.e. bacterial taxa) in case '
                 'samples are converted to percentiles of the equivalent '
                 'features in control samples within a study prior to pooling data across studies.'),
    short_description='Plugin to identify Bifidobacterium subspecies based on SNVs in V3-V4 16S rDNA sequences',
    user_support_text=('TODO')
)

# Register Bifidobacterium sequences extraction
plugin.pipelines.register_function(
	function=extract_bifs,
	inputs={
		'rep_seqs': FeatureData[Sequence],
		'taxonomy': FeatureData[Taxonomy]
	},
	outputs=[('bifs_seqs', FeatureData[Sequence])],
	input_descriptions={
		'rep_seqs': ('Representative sequences of each OTU.'),
		'taxonomy': ('Taxonomic assignment of each OTU.'),
    },
    parameters={},
    parameter_descriptions={},
    output_descriptions={
        'bifs_seqs': ('Representative sequences of each OTU annotated as genus Bifidobacterium.')},
    name='Extract Bifidobacterium representative sequences',
    description=('Extracts Bifidobacterium representative sequences') 
)

plugin.methods.register_function(
    function=align_mothur,
    inputs={'sequences': FeatureData[Sequence]},
    outputs=[('alignment', FeatureData[AlignedSequence])],
    input_descriptions={'sequences': 'The sequences to be aligned.'},
    output_descriptions={'alignment': 'The aligned sequences.'},
    parameters={},
    parameter_descriptions={},
    name='Alignment of sequences on SILVA using mothur', 
    description=("Alignment of sequences on SILVA using mothur"),
)