# Introductory Sequence
## Step 1 - Taxonomic Hierarchy Query

**Goal**: navigate hierarchical taxonomic relationships to understand the full classification of species

This kata will help you work with derived relationships in the taxonomy hierarchy and filter by taxonomic rank

---
**Instructions**:
- Read the query spec below and view the provided query in `kata/step_1/__main__.py`
- Implement the provided query:
    - Filter to species with genus name "Acaena"
    - Use derived taxonomic relationships to get the full classification
    - Return: species canonical name, genus name, family name, order name
    - Use `.alias()` to name columns: species_name, genus_name, family_name, order_name
    - The derived taxonomy relationships are defined in `kg/model/derived/taxonomy.py`
- Verify: `uv run -m kata.step_1`
    - Note: you may need to approve Snowflake MFA

---
**Spec**:

Business Question: Given a plant genus (Acaena), show me all species in that genus along with their full taxonomic classification through the hierarchy. This query helps researchers understand taxonomic relationships and biodiversity within a genus.

Acceptance Criteria:
```
Given I am a botanist studying the Acaena genus,
When I want to see all species in that genus with their full classification,
Then I can run a query that provides species names along with their genus, family, and order
```

Functional Query Definition:
```sql
SELECT
    s.canonical_name as species_name,
    g.canonical_name as genus_name,
    f.canonical_name as family_name,
    o.canonical_name as order_name
FROM
    taxa s
JOIN taxa g ON s.parent_id = g.taxon_id AND g.rank = 'genus'
JOIN taxa f ON g.parent_id = f.taxon_id AND f.rank = 'family'
JOIN taxa o ON f.parent_id = o.taxon_id AND o.rank = 'order'
WHERE
    s.rank = 'species'
    AND g.canonical_name = 'Acaena'
```
