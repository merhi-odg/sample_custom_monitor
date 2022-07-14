import pandas


# modelop.metrics
def metrics(dataframe: pandas.DataFrame) -> dict:

    record_count = dataframe.shape[0]
    column_count = dataframe.shape[1]

    yield {
        "record_count": record_count,
        "column_count": column_count,
        "volumetrics": [
            {
                "test_category": "volumetrics",
                "test_name": "Record Counter",
                "test_type": "record_counter",
                "test_id": "volumetrics_record_counter",
                "values": {
                    "record_count": record_count,
                    "column_count": column_count,
                },
            }
        ],
    }
