# sample_custom_monitor

This ModelOp Center monitor computes record and column counts of a dataset.

## Input Assets

| Type          | Number | Description                                           |
| ------------- | ------ | ----------------------------------------------------- |
| Baseline Data | **0**  |                                                       |
| Sample Data   | **1**  | A dataset corresponding to a slice of production data |


## Monitor Output

```JSON
{
    "record_count": <record_count>,
    "column_count": <column_count>,
    "volumetrics": [
        {
            "test_category": "volumetrics",
            "test_name": "Record Counter",
            "test_type": "record_counter",
            "test_id": "volumetrics_record_counter",
            "values": {
                "record_count": <record_count>,
                "column_count": <column_count>
            }
        }
    ]
}
```
