from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.bigquery import BigQuery
from os import path
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform_in_bigquery(*args, **kwargs) -> DataFrame:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    query = (
        ""
    )

    #sp_project_bucket/new_crime_data.parquet

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).execute(query)

    return "Extr..."


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
