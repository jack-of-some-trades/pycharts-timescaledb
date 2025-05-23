import pytest
import pandas as pd
from pandas.testing import assert_series_equal
from psyscale.series_df import Series_DF

# region  ---- ---- Test fixtures ---- ----

TEST_DATA_SIMPLE = {
    "timestamp": pd.date_range("2025-01-01", periods=5, freq="D"),
    "o": [100, 105, 110, 115, 120],
    "last": [105, 110, 115, 120, 125],
    "MAX": [107, 112, 117, 122, 127],
    "Low": [98, 103, 108, 113, 118],
    "voL": [1000, 1100, 1200, 1300, 1400],
    "vwap": [105, 110, 115, 120, 125],
    "count": [500, 550, 600, 650, 700],
}

TEST_DATA = {
    "date": [
        "2023-02-07 11:00:00+00:00",
        "2023-02-07 11:30:00+00:00",
        "2023-02-07 12:00:00+00:00",
        "2023-02-07 12:30:00+00:00",
        "2023-02-07 13:00:00+00:00",
        "2023-02-07 13:30:00+00:00",
        "2023-02-07 14:00:00+00:00",
        "2023-02-07 14:30:00+00:00",
        "2023-02-07 15:00:00+00:00",
        "2023-02-07 15:30:00+00:00",
        "2023-02-07 16:00:00+00:00",
        "2023-02-07 16:30:00+00:00",
        "2023-02-07 17:00:00+00:00",
        "2023-02-07 17:30:00+00:00",
        "2023-02-07 18:00:00+00:00",
        "2023-02-07 18:30:00+00:00",
        "2023-02-07 19:00:00+00:00",
        "2023-02-07 19:30:00+00:00",
        "2023-02-07 20:00:00+00:00",
        "2023-02-07 20:30:00+00:00",
        "2023-02-07 21:00:00+00:00",
        "2023-02-07 21:30:00+00:00",
        "2023-02-07 22:00:00+00:00",
        "2023-02-07 22:30:00+00:00",
        "2023-02-07 23:00:00+00:00",
        "2023-02-07 23:30:00+00:00",
        "2023-02-08 00:00:00+00:00",
        "2023-02-08 00:30:00+00:00",
        "2023-02-08 09:00:00+00:00",
        "2023-02-08 09:30:00+00:00",
        "2023-02-08 10:00:00+00:00",
        "2023-02-08 10:30:00+00:00",
        "2023-02-08 11:00:00+00:00",
        "2023-02-08 11:30:00+00:00",
        "2023-02-08 12:00:00+00:00",
        "2023-02-08 12:30:00+00:00",
    ],
    "open": [
        151.71,
        151.7,
        151.78,
        152.01,
        151.7,
        151.62,
        151.39,
        150.73,
        152.31,
        152.14,
        152.6,
        153.19,
        153.02,
        152.63,
        154.83,
        152.88,
        152.12,
        153.68,
        154.22,
        154.29,
        154.64,
        154.08,
        154.0,
        154.1,
        154.15,
        154.47,
        154.19,
        154.04,
        154.15,
        154.0,
        153.86,
        153.68,
        153.76,
        153.66,
        153.74,
        153.97,
    ],
    "high": [
        151.77,
        151.7,
        152.1,
        152.03,
        152.39,
        151.65,
        151.39,
        152.93,
        152.44,
        153.19,
        153.37,
        153.6,
        153.19,
        155.23,
        155.15,
        152.91,
        153.93,
        154.47,
        154.58,
        155.22,
        154.66,
        154.65,
        154.09,
        154.2,
        154.6,
        154.49,
        154.25,
        154.15,
        154.38,
        154.0,
        153.88,
        153.82,
        153.88,
        153.76,
        154.24,
        154.19,
    ],
    "low": [
        151.6,
        151.61,
        151.68,
        151.86,
        151.35,
        151.19,
        150.33,
        150.63,
        151.84,
        152.1,
        152.56,
        152.99,
        152.52,
        152.38,
        152.85,
        151.36,
        152.04,
        153.56,
        153.43,
        154.07,
        153.87,
        153.94,
        153.99,
        154.03,
        154.15,
        154.12,
        153.91,
        154.0,
        153.87,
        153.55,
        153.5,
        153.51,
        153.52,
        153.52,
        153.74,
        153.7,
    ],
    "close": [
        151.7,
        151.64,
        151.96,
        151.95,
        151.63,
        151.37,
        150.71,
        152.32,
        152.14,
        152.6,
        153.19,
        153.01,
        152.63,
        154.81,
        152.88,
        152.13,
        153.65,
        154.22,
        154.3,
        154.64,
        154.07,
        153.99,
        154.08,
        154.19,
        154.43,
        154.2,
        154.0,
        154.15,
        154.0,
        153.68,
        153.68,
        153.76,
        153.53,
        153.76,
        154.0,
        153.83,
    ],
    "volume": [
        7657.0,
        2193.0,
        35430.0,
        24208.0,
        111569.0,
        117887.0,
        255714.0,
        8296536.0,
        3638572.0,
        4275259.0,
        3284401.0,
        2253726.0,
        1820071.0,
        5537939.0,
        5362187.0,
        5113876.0,
        4003133.0,
        3230270.0,
        3758108.0,
        8982480.0,
        11232697.0,
        69702.0,
        12642.0,
        30777.0,
        61553.0,
        22904.0,
        20674.0,
        26351.0,
        31266.0,
        21185.0,
        14808.0,
        28600.0,
        10276.0,
        6418.0,
        36725.0,
        41798.0,
    ],
    "ticks": [
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
        130,
        131,
        132,
        133,
        134,
        135,
    ],
}


@pytest.fixture
def TEST_DF_SIMPLE():
    return pd.DataFrame(TEST_DATA_SIMPLE)


@pytest.fixture
def TEST_DF():
    return pd.DataFrame(TEST_DATA)


# endregion


def test_simple_series_df_initialization(TEST_DF_SIMPLE):
    """Test that the Series_DF is correctly initialized."""
    # Create Series_DF instance
    series_df = Series_DF(TEST_DF_SIMPLE)

    assert series_df.columns == {
        "dt",
        "open",
        "close",
        "high",
        "low",
        "volume",
        "vwap",
        "ticks",
    }

    # Test the DataFrame is correctly set
    assert "dt" in series_df.df.columns
    assert isinstance(series_df.df, pd.DataFrame)

    # Test if the `timedelta` property is set
    assert isinstance(series_df.timedelta, pd.Timedelta)
    assert series_df.timedelta == pd.Timedelta("1D")

    # Test if `ext` is None initially, since it relies on the session marking
    assert series_df.ext is None


def test_realistic_df_mark_ext(TEST_DF):
    series_df_no_exchange = Series_DF(TEST_DF, None)
    assert "rth" not in series_df_no_exchange.columns
    assert series_df_no_exchange.ext is None

    series_df_crypto = Series_DF(TEST_DF, "crypto")
    assert "rth" not in series_df_crypto.columns
    assert series_df_crypto.ext is None

    series_df_nyse = Series_DF(TEST_DF, "NYSE")
    assert "rth" in series_df_nyse.columns
    assert series_df_nyse.timedelta == pd.Timedelta("30min")
    assert_series_equal(
        pd.Series(
            [1, 1, 1, 1, 1, 1, 1]
            + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            + [2, 2, 2, 2, 2, 2, 2, 2]
            + [1, 1, 1, 1, 1, 1, 1, 1],
            index=pd.DatetimeIndex(
                [
                    "2023-02-07 11:00:00+00:00",
                    "2023-02-07 11:30:00+00:00",
                    "2023-02-07 12:00:00+00:00",
                    "2023-02-07 12:30:00+00:00",
                    "2023-02-07 13:00:00+00:00",
                    "2023-02-07 13:30:00+00:00",
                    "2023-02-07 14:00:00+00:00",
                    "2023-02-07 14:30:00+00:00",
                    "2023-02-07 15:00:00+00:00",
                    "2023-02-07 15:30:00+00:00",
                    "2023-02-07 16:00:00+00:00",
                    "2023-02-07 16:30:00+00:00",
                    "2023-02-07 17:00:00+00:00",
                    "2023-02-07 17:30:00+00:00",
                    "2023-02-07 18:00:00+00:00",
                    "2023-02-07 18:30:00+00:00",
                    "2023-02-07 19:00:00+00:00",
                    "2023-02-07 19:30:00+00:00",
                    "2023-02-07 20:00:00+00:00",
                    "2023-02-07 20:30:00+00:00",
                    "2023-02-07 21:00:00+00:00",
                    "2023-02-07 21:30:00+00:00",
                    "2023-02-07 22:00:00+00:00",
                    "2023-02-07 22:30:00+00:00",
                    "2023-02-07 23:00:00+00:00",
                    "2023-02-07 23:30:00+00:00",
                    "2023-02-08 00:00:00+00:00",
                    "2023-02-08 00:30:00+00:00",
                    "2023-02-08 09:00:00+00:00",
                    "2023-02-08 09:30:00+00:00",
                    "2023-02-08 10:00:00+00:00",
                    "2023-02-08 10:30:00+00:00",
                    "2023-02-08 11:00:00+00:00",
                    "2023-02-08 11:30:00+00:00",
                    "2023-02-08 12:00:00+00:00",
                    "2023-02-08 12:30:00+00:00",
                ],
                name="dt",
            ),
            name="rth",
            dtype=pd.CategoricalDtype([-1, 0, 1, 2]),
        ),
        series_df_nyse.df["rth"],
    )
