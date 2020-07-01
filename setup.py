# -*- coding: iso-8859-15 -*-
# ----------------------------------------------------------------------------
# Copyright (c) 2020, L. Siegwald, F. Foata, B. Berger
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

# Setup copied from q2-emperor
setup(
    name="moulinette",
    version="2020.6.1",
    packages=find_packages(),
    author="Léa Siegwald, Francis Foata, Bernard Berger",
    author_email="lea.siegwald@rd.nestle.com",
    description="Bifidobacterium subspecies identification based on SNVs in V3-V4 16S rDNA sequences",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-moulinette=q2_moulinette.plugin_setup:plugin']
    },
    zip_safe=False,
    package_data={
        'q2_moulinette': ['assets/silva.bacteria.fasta']
    }
)
