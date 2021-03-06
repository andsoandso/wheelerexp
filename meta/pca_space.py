"""
usage: python ./pca_space.py name data roifile cond tr [, filtfile]
"""

import sys, os
import numpy as np

from fmrilearn.analysis import fir

from sklearn.decomposition import PCA

from wheelerexp.base import Space
from wheelerexp.base import DecomposeExp
from wheelerexp.common import process_exp_argv

from wheelerdata.load.meta import get_data

# ---------------------------------------------------------------------------
# Process argv
# ---------------------------------------------------------------------------
basename, dataname, rois, cond, tr, filtfile = process_exp_argv(sys.argv)
data = get_data(dataname)

# ---------------------------------------------------------------------------
# Setup exp
# ---------------------------------------------------------------------------
spacetime = Space(PCA(5, whiten=True), fir, mode="decompose")
exp = DecomposeExp(spacetime, data, window=15, nsig=3, tr=tr)

# ---------------------------------------------------------------------------
# And run each roi
# ---------------------------------------------------------------------------
for n, roi in enumerate(rois):
    print("{3}: {0} ({1}/{2})".format(roi, n+1, len(rois), dataname))   
    exp.run(basename, roi, cond, smooth=False, filtfile=filtfile, event=True)

