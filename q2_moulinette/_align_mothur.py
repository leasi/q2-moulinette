# -*- coding: iso-8859-15 -*-
# ----------------------------------------------------------------------------
# Copyright (c) 2020, L. Siegwald, F. Foata, B. Berger
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import shutil
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


def align_mothur(sequences: DNAFASTAFormat,
                 reference: AlignedDNAFASTAFormat) -> AlignedDNAFASTAFormat:
    reference_fp = str(reference)
    sequences_fp = str(sequences)
    # Escape hyphens in input names so mothur does not get upset
    sequences_escaped_fp = sequences_fp.replace("-", "\-")
    result = AlignedDNAFASTAFormat()

    cmd = "mothur \"#set.dir(debug={0});" \
          "align.seqs(fasta={1}, reference={2});\"".format(
            os.path.dirname(sequences_fp), sequences_escaped_fp, reference_fp)
    run_mothur(cmd)
    # Path to output file is in alignment_fp defined below:
    mother_alignment_fp = os.path.splitext(sequences_fp)[0] + ".align"

    # copy the mothur output alignment to the AlignedDNAFASTAFormat filepath
    shutil.copyfile(mother_alignment_fp, str(result))

    # once the file is in place, just return the AlignedDNAFASTAFormat object
    return result
