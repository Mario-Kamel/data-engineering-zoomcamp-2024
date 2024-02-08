import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    #remove zero passenger_count and trip_distance
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] >0)]
    
    #create date columns
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date

    #column names modulation
    data.rename(columns={'VendorID': 'vendor_id', 'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_location_id', 'DOLocationID': 'do_location_id'}, inplace=True)
    return data


@test
def test_vendor_id_exists(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, 'vendor_id is one of the existing values in the column (currently)'

@test
def test_all_trips_have_non_zero_passenger_count(output, *args) -> None:
    assert all(output['passenger_count'] > 0)

@test
def test_all_trips_have_non_zero_trip_distance(output, *args) -> None:
    assert all(output['trip_distance'] > 0)