import os
import pandas as pd
import pytest
# TODO: set up pytest


@pytest.fixture(scope="session")
def datapath():
    return 'Examples/data'


@pytest.fixture(scope="session")
def outdir():
    # output folder
    outdir = 'sfrmaker/test/temp/'
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    return outdir


@pytest.fixture(scope="function")
def sfr_test_numbering():
    rd = pd.DataFrame()
    rd['i'] = [3, 4, 5,
              7, 8, 9,
              0, 1, 2,
              4, 4, 5,
              0, 0, 0,
              3, 4, 5,
              0, 1, 2,
              4, 5, 6,
              2, 2, 2]
    rd['j'] = [0, 1, 2,
              6, 6, 6,
              6, 6, 6,
              3, 4, 5,
              9, 8, 7,
              6, 6, 6,
              0, 0, 0,
              6, 6, 6,
              9, 8, 7]
    rd['iseg'] = sorted(list(range(1, 10)) * 3)
    rd['ireach'] = [1, 2, 3] * 9

    sd = pd.DataFrame()
    sd['nseg'] = range(1, 10)
    sd['outseg'] = [4, 0, 6, 8, 3, 8, 1, 2, 8]
    return rd, sd
