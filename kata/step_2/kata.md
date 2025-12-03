## Step 2 - Species Richness by Region

**Goal**: calculate species diversity metrics by counting distinct species per country

This kata will help you work with aggregations and distinct counts to understand biodiversity patterns across regions

---
**Instructions**:
- Read the query spec below and view the provided query in `kata/step_2/__main__.py`
- Implement the provided query:
    - Count distinct species per country using the classification relationship
    - Also count total observations per country
    - Use `rai.count()` with `.per()` to group by country
    - To count distinct species, count the distinct taxon IDs at species rank
    - Use `.alias()` to name columns: country_code, species_count, observation_count
- Verify: `uv run -m kata.step_2`
    - Note: you may need to approve Snowflake MFA

---
**Spec**:

Business Question: Which countries have the highest plant species diversity in our dataset? This query helps identify biodiversity hotspots and guides conservation priorities by showing both species richness (unique species) and sampling effort (total observations) per country.

Acceptance Criteria:
```
Given I am a conservation biologist studying global plant diversity,
When I want to identify countries with the highest species richness,
Then I can run a query that counts distinct species and total observations per country
```

Functional Query Definition:
```sql
SELECT
    country_code,
    COUNT(DISTINCT CASE WHEN rank = 'species' THEN taxon_id END) as species_count,
    COUNT(*) as observation_count
FROM
    observations o
JOIN
    taxa t ON o.taxon_id = t.taxon_id
GROUP BY
    country_code
ORDER BY
    species_count DESC
LIMIT 10;
```
