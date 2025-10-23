# ARQ Starter

Contains 
- [SnowSQL scripts](/script) for uploading source data
- [DBT models](/dbt/models) for preprocessing and documenting source data 
  - https://github.com/dbt-labs/dbt-core
- [RAI model](/kg/model) for building semantics and queries
  - https://private.relational.ai/early-access/pyrel
  - https://private.relational.ai/manage/install

## Setup

Requires [uv](https://github.com/astral-sh/uv) for python runtime management.
Assumes RAI Native App has been installed and configured.

```bash
uv sync

# input Snowflake config
# if using user/pass auth, you can leave fields after schema blank
# https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-cli
uvx --from snowflake-cli snow connection add
uvx --from snowflake-cli snow connection set-default <name>

# create ARQ role, db, and warehouse. the code assumes these exist
uvx --from snowflake-cli snow sql -f script/team_arq.sql

# GBIF Backbone Taxonomy
# https://drive.google.com/file/d/19KbBCcfZ5Mpwbo4y9UdO3nDMBL_7yAUp/view?usp=drive_link
# download & unzip this file, and give the script the full path to the folder
# it will create tables in team_arq.source from the given data
uvx --from snowflake-cli snow sql -f script/gbif_backbone.sql -D "path=/Users/agarrard/arq/data/backbone"

# GBIF Observation
# https://drive.google.com/file/d/1DZHHo08eJnVG-Eju5t-n6ECK6MDUyHNV/view?usp=drive_link
# download & unzip this file, and give the script the full path to the file
uvx --from snowflake-cli snow sql -f script/gbif_observation.sql -D "path=/Users/agarrard/arq/data/gbif_observation.csv"

# DBT
# create a config file https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup
# dbt_project.yaml assumes a profile named "default" which targets the schema "team_arq.public"
uv run dbt deps
uv run dbt build

# RAI
uv run rai init

# Run tests
uv run pytest

# Run apps
uv run -m kg.apps.observation_eda observations_per_genus --threshold 100
uv run -m kg.apps.observation_eda nearby_observations
```

## AI Assistance
Some useful prompts which Claude Code has been pretty good with:
- "add the core model definition for the concept MyCoolConcept which is sourced from dbt/models/staging/boop.yml, following the example in kg/model/core/observation.py"
- "add a test for the bindings of MyCoolConcept to kg/tests/test_bindings.py"
- "update the protocols in kg/model/__init__.py to reflect the dynamic assignments to the RAI model"
- "update the comments in kg/model/core/taxon.py to reflect the documentation in the dbt/models/staging/taxon.yml"

You can try asking it to generate queries, but it seems pretty hit or miss. maybe it will be better with more queries to serve as examples.





