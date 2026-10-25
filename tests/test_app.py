import pandas as pd

def test_csv_sample_can_be_read():
    df = pd.read_csv('sample.csv')
    assert len(df) > 0
