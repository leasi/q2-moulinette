# -*- coding: iso-8859-15 -*-
# ----------------------------------------------------------------------------
# Copyright (c) 2020, L. Siegwald, F. Foata, B. Berger
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2
from pathlib import Path
import subprocess
from q2_types.feature_data import DNAFASTAFormat, AlignedDNAFASTAFormat

# Inspired from https://github.com/qiime2/q2-alignment/blob/master/q2_alignment/_mafft.py
def run_mothur(cmd, verbose=True):
    if verbose:
        print("Running external command line application. This may print "
              "messages to stdout and/or stderr.")
        print("The command being run is below. This command cannot "
              "be manually re-run as it will depend on temporary files that "
              "no longer exist.")
        print("\nCommand:", end=' ')
        print(cmd, end='\n\n')
        subprocess.run(cmd, check=True, shell=True)

def align_mothur(sequences: DNAFASTAFormat)-> AlignedDNAFASTAFormat:
    sequences_fp = str(sequences)
    sequences_escaped_fp=sequences_fp.replace("-", "\-") # Mothur does not allow hyphens in input names
    result = AlignedDNAFASTAFormat()
	
    cmd = "mothur \"#set.dir(debug="+str(Path(sequences_fp).parent)+");align.seqs(fasta="+sequences_escaped_fp+", reference="+str(Path(__file__).parent)+"/assets/silva.bacteria.fasta);\""
    run_mothur(cmd)
	
	# Path to output file is in alignment_fp defined below:
    alignment_fp=str(Path(sequences_fp).parent/(Path(sequences_fp).stem+".align"))
	# ONE COMMAND MISSING HERE: How do I return the content of alignment_fp into result, which is an AlignedDNAFASTAFormat() object?
    return AlignedDNAFASTAFormat(result)
   