"""
Tests the financial data structures
"""

import unittest
import os
import numpy as np
import pandas as pd

from mlfinlab.data_structures import imbalance_data_structures as ds


class TestDataStructures(unittest.TestCase):
    """
    Test the various financial data structures:
    1. Imbalance Dollar bars
    2. Imbalance Volume bars
    3. Imbalance Tick bars
    """

    def setUp(self):
        """
        Set the file path for the tick data csv
        """
        project_path = os.path.dirname(__file__)
        self.path = project_path + '/test_data/imbalance_sample_data.csv'

    def test_ema_imbalance_dollar_bars(self):
        """
        Tests the imbalance dollar bars implementation.
        """
        exp_num_ticks_init = 1000
        num_prev_bars = 3

        db1, _ = ds.get_ema_dollar_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                                  expected_imbalance_window=10000,
                                                  num_prev_bars=num_prev_bars, batch_size=2e7, verbose=False, )
        db2, _ = ds.get_ema_dollar_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                                  expected_imbalance_window=10000,
                                                  num_prev_bars=num_prev_bars, batch_size=50, verbose=False)
        db3, _ = ds.get_ema_dollar_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                                  expected_imbalance_window=10000,
                                                  num_prev_bars=num_prev_bars, batch_size=10, verbose=False)
        ds.get_ema_dollar_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                         expected_imbalance_window=10000,
                                         num_prev_bars=num_prev_bars, batch_size=50, verbose=False,
                                         to_csv=True, output_path='test.csv')
        db4 = pd.read_csv('test.csv')

        self.assertEqual(db1.shape, (4770, 9))

        # Assert diff batch sizes have same number of bars
        self.assertTrue(db1.shape == db2.shape)
        self.assertTrue(db1.shape == db3.shape)
        self.assertTrue(db1.shape == db4.shape)

        # Assert same values
        self.assertTrue(np.all(db1.values == db2.values))
        self.assertTrue(np.all(db1.values == db3.values))
        self.assertTrue(np.all(db1.values == db4.values))

        # Assert OHLC is correct (the first value)
        self.assertTrue(db1.loc[0, 'open'] == 1306.0)
        self.assertTrue(db1.loc[0, 'high'] == 1306.0)
        self.assertTrue(db1.loc[0, 'low'] == 1304.25)
        self.assertTrue(db1.loc[0, 'close'] == 1304.5)
        self.assertTrue((db1.loc[:, 'high'] >= db1.loc[:, 'low']).all())

        # Assert OHLC is correct (the some value in the middle)
        self.assertTrue(db1.loc[1387, 'open'] == 1303.5)
        self.assertTrue(db1.loc[1387, 'high'] == 1303.5)
        self.assertTrue(db1.loc[1387, 'low'] == 1303.5)
        self.assertTrue(db1.loc[1387, 'close'] == 1303.5)
        self.assertTrue((db1.loc[:, 'high'] >= db1.loc[:, 'low']).all())
        self.assertTrue((db1.loc[:, 'volume'] >= db1.loc[:, 'cum_buy_volume']).all())

        # Delete generated csv file (if it wasn't generated test would fail)
        os.remove('test.csv')

    def test_imbalance_volume_bars(self):
        """
        Tests the imbalance volume bars implementation.
        """
        exp_num_ticks_init = 100
        num_prev_bars = 3

        db1, _ = ds.get_volume_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                              num_prev_bars=num_prev_bars, batch_size=1000, verbose=False)
        db2, _ = ds.get_volume_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                              num_prev_bars=num_prev_bars, batch_size=50, verbose=False)
        db3, _ = ds.get_volume_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                              num_prev_bars=num_prev_bars, batch_size=10, verbose=False)
        ds.get_volume_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                     num_prev_bars=num_prev_bars, batch_size=50, verbose=False,
                                     to_csv=True, output_path='test.csv')
        db4 = pd.read_csv('test.csv')

        self.assertEqual(db1.shape, (102, 6))

        # Assert diff batch sizes have same number of bars
        self.assertTrue(db1.shape == db2.shape)
        self.assertTrue(db1.shape == db3.shape)
        self.assertTrue(db1.shape == db4.shape)

        # Assert same values
        self.assertTrue(np.all(db1.values == db2.values))
        self.assertTrue(np.all(db1.values == db3.values))
        self.assertTrue(np.all(db1.values == db4.values))

        # Assert OHLC is correct
        self.assertTrue(db1.loc[0, 'open'] == 1306.0)
        self.assertTrue(db1.loc[0, 'high'] == 1306.00)
        self.assertTrue(db1.loc[0, 'low'] == 1305.75)
        self.assertTrue(db1.loc[0, 'close'] == 1305.75)
        self.assertTrue((db1.loc[:, 'high'] >= db1.loc[:, 'low']).all())

        # delete generated csv file (if it wasn't generated test would fail)
        os.remove('test.csv')

    def test_imbalance_tick_bars(self):
        """
        Tests the imbalance tick bars implementation.
        """
        exp_num_ticks_init = 100
        num_prev_bars = 3

        db1, _ = ds.get_tick_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                            num_prev_bars=num_prev_bars, batch_size=1000, verbose=False)
        db2, _ = ds.get_tick_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                            num_prev_bars=num_prev_bars, batch_size=50, verbose=False)
        db3, _ = ds.get_tick_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                            num_prev_bars=num_prev_bars, batch_size=10, verbose=False)
        ds.get_tick_imbalance_bars(self.path, exp_num_ticks_init=exp_num_ticks_init,
                                   num_prev_bars=num_prev_bars, batch_size=50, verbose=False,
                                   to_csv=True, output_path='test.csv')
        db4 = pd.read_csv('test.csv')

        self.assertEqual(db1.shape, (102, 6))

        # Assert diff batch sizes have same number of bars
        self.assertTrue(db1.shape == db2.shape)
        self.assertTrue(db1.shape == db3.shape)
        self.assertTrue(db1.shape == db4.shape)

        # Assert same values
        self.assertTrue(np.all(db1.values == db2.values))
        self.assertTrue(np.all(db1.values == db3.values))

        # Assert OHLC is correct
        self.assertTrue(db1.loc[0, 'open'] == 1306.0)
        self.assertTrue(db1.loc[0, 'high'] == 1306.00)
        self.assertTrue(db1.loc[0, 'low'] == 1305.75)
        self.assertTrue(db1.loc[0, 'close'] == 1305.75)
        self.assertTrue((db1.loc[:, 'high'] >= db1.loc[:, 'low']).all())

        # delete generated csv file (if it wasn't generated test would fail)
        os.remove('test.csv')

    def test_csv_format(self):
        """
        Asserts that the csv data being passed is of the correct format.
        """
        wrong_date = ['2019-41-30', 200.00, np.int64(5)]
        wrong_price = ['2019-01-30', 'asd', np.int64(5)]
        wrong_volume = ['2019-01-30', 200.00, '1.5']
        too_many_cols = ['2019-01-30', 200.00,
                         np.int64(5), 'Limit order', 'B23']

        # pylint: disable=protected-access
        self.assertRaises(ValueError, ds.ImbalanceBars._assert_csv(
            pd.DataFrame(wrong_date).T))
        # pylint: disable=protected-access
        self.assertRaises(AssertionError,
                          ds.ImbalanceBars._assert_csv,
                          pd.DataFrame(too_many_cols).T)
        # pylint: disable=protected-access
        self.assertRaises(AssertionError,
                          ds.ImbalanceBars._assert_csv,
                          pd.DataFrame(wrong_price).T)
        # pylint: disable=protected-access
        self.assertRaises(AssertionError,
                          ds.ImbalanceBars._assert_csv,
                          pd.DataFrame(wrong_volume).T)
