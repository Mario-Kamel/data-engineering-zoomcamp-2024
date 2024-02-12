import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    
    # Initialize an empty list to store data frames
    data_frames = []

    for month in months:
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet'
        
        # Read the data for the current month
        try:
            data = pd.read_parquet(url)
            data_frames.append(data)
            print(f"Loaded data for {month}")
        except Exception as e:
            print(f"Error loading data for {month}: {e}")


    # Concatenate all data frames into a single data frame
    all_data = pd.concat(data_frames, ignore_index=True)

    print(f'loaded {len(all_data.index)} records')
    return all_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
