import pytest
import numpy as np
import astropy.units as u
import os
import shutil
import json

from adx.adx_directory import *


test_data = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'test_data', 'data_dir_noadx')

class TestInit:

    def setup(self):
        self.data_dir = test_data

    def test_non_adx_dir(self):
        dd = DataDirectory(self.data_dir)
        assert not dd.isadx

    def test_init(self):
        init_adx_dir(self.data_dir, ['lofasm', 'bbx'])
        config_file = os.path.join(self.data_dir, 'adx_log/config')
        assert os.path.exists(config_file)
        f = open(config_file, 'r')
        config = json.load(f)
        shutil.rmtree(adx_dir)

    def test_adx_dir(self):
        init_adx_dir(self.data_dir, ['lofasm', 'bbx'])
        dd = DataDirectory(self.data_dir)
        assert dd.isadx
        assert dd.subdirs == []
        shutil.rmtree(self.adx_dir)
