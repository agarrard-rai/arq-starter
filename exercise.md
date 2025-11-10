# Exercise 1 - Add a column

**Goal**:
Add the column `TEAM_ARQ.PUBLIC.OBSERVATION.BASISOFRECORD` to the KG.

Add it to the KG and write a query which uses it.

**Instructions**:
- Run `uv run pytest -sk test_observation_bindings`. The test should fail because it expects the new column.
- Model the new column in the existing [Observation core model](./kg/model/core/observation.py)
- Update the Observation [Protocols](./kg/model/__init__.py) to keep type hints and autocomplete up-to-date
- Come up with a query which uses Observation Basis of Record and add it to the [observation_eda app](./kg/apps/observation_eda.py)
- Add a test for your query in the [tests folder](./kg/tests)

Verify: `uv run pytest -s kg/tests`
