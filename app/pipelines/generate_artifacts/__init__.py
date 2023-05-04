import pathlib

from mara_pipelines.commands.sql import ExecuteSQL
from mara_pipelines.pipelines import Pipeline, Task

pipeline = Pipeline(
    id="generate_artifacts",
    description="Create flattened data set tables for various front-ends",
    base_path=pathlib.Path(__file__).parent)

from .metabase import pipeline as metabase_pipeline

pipeline.add(metabase_pipeline)

from .mara_data_explorer import pipeline as mara_data_explorer_pipeline

pipeline.add(mara_data_explorer_pipeline)

from .mondrian import pipeline as mondrian_pipeline

pipeline.add(mondrian_pipeline)


pipeline.add_final(
    Task(
        id='replace_schemas',
        description='Replaces the frontend schemas with their next versions',
        commands=[
            ExecuteSQL(
                sql_file_name='switch_metabase_schema.sql',
                db_alias='metabase-data-write',
            ),
            ExecuteSQL(
                sql_statement="SELECT util.replace_schema('data_sets', 'data_sets_next')",
                db_alias='dwh',
            ),
            ExecuteSQL(
                sql_statement="SELECT util.replace_schema('mondrian', 'mondrian_next')",
                db_alias='dwh',
            ),
        ],
    )
)

