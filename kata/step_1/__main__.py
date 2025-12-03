import pandas as pd
from rich.console import Console
import relationalai.semantics as rai
from kg.model import ARQModel, define_arq

"""
Step 1: Taxonomic Hierarchy Query
- Query species in the Acaena genus
- Use derived taxonomic relationships to get genus, family, and order
- Show how RAI simplifies hierarchical queries compared to SQL
- Name the columns "species_name", "genus_name", "family_name", "order_name" in the query result
"""
def taxonomic_hierarchy_query(arq: ARQModel) -> rai.Fragment:
    return rai.where(
        arq.Species.genus.canonical_name == "Acaena"
    ).select(
        arq.Species.canonical_name.alias("species_name"),
        arq.Species.genus.canonical_name.alias("genus_name"),
        arq.Species.family.canonical_name.alias("family_name"),
        arq.Species.order.canonical_name.alias("order_name"),
    )


def test_solution(result: pd.DataFrame) -> None:
    expected = pd.read_csv("kata/step_1/expected_results.csv")
    pd.testing.assert_frame_equal(result, expected)
    console.print("✅ Query result is correct!")
    console.print("[dim]Next: move on to Step 2 with `uv run -m kata.step_2`[/dim]\n")


if __name__ == "__main__":
    console = Console()
    console.print("\n[bold blue]Testing Kata Step 1...")
    arq = define_arq(rai.Model(f"kata_step_1"))
    result = taxonomic_hierarchy_query(arq).to_df()
    console.print("Step [white]1[/white] - Taxonomic Hierarchy Query Result", style="bold")
    console.print("-" * 50 + "\n" + str(result) + "\n")
    test_solution(result)
