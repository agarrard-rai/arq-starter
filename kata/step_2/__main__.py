import pandas as pd
from rich.console import Console
import relationalai.semantics as rai
from kg.model import ARQModel, define_arq

"""
Step 2: Species Richness by Region
- Count distinct species per country to measure biodiversity
- Count total observations per country to measure sampling effort
- Filter to observations classified at species level
- Name the columns "country_code", "species_count", "observation_count" in the query result
"""
def species_richness_query(arq: ARQModel) -> rai.Fragment:
    raise NotImplementedError("TODO: Implement the species richness query")


def test_solution(result: pd.DataFrame) -> None:
    expected = pd.read_csv("kata/step_2/expected_results.csv")
    result["species_count"] = result["species_count"].astype("int64")
    result["observation_count"] = result["observation_count"].astype("int64")
    pd.testing.assert_frame_equal(result, expected)
    console.print("✅ Query result is correct!")
    console.print("[dim]Congratulations! You've completed both kata steps![/dim]\n")


if __name__ == "__main__":
    console = Console()
    console.print("\n[bold blue]Testing Kata Step 2...")
    arq = define_arq(rai.Model(f"kata_step_2"))
    result = species_richness_query(arq).to_df()
    console.print("Step [white]2[/white] - Species Richness by Region Result", style="bold")
    console.print("-" * 50 + "\n" + str(result) + "\n")
    test_solution(result)
