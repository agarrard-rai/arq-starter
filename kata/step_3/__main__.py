import pandas as pd
from rich.console import Console
import relationalai.semantics as rai
import relationalai.semantics.std as std
from kg.model import ARQModel, define_arq

"""
Step 3: Summer Solstice Observations by Location
- Find observations within 20 days of Summer Solstice
- Count distinct species per family, country, and state/province
- Show regional patterns in peak growing season phenology
- Name the columns "species_count", "family_name", "country_code", "state_province"
"""
def early_bloomers_query(arq: ARQModel) -> rai.Fragment:
    raise NotImplementedError("TODO: Implement the summer solstice observations query")


def test_solution(result: pd.DataFrame) -> None:
    expected = pd.read_csv("kata/step_3/expected_results.csv")
    result["species_count"] = result["species_count"].astype("int64")
    pd.testing.assert_frame_equal(result, expected)
    console.print("✅ Query result is correct!")
    console.print("[dim]Congratulations! You've completed Step 3![/dim]\n")


if __name__ == "__main__":
    console = Console()
    console.print("\n[bold blue]Testing Kata Step 3...")
    arq = define_arq(rai.Model(f"kata_step_3"))
    result = early_bloomers_query(arq).to_df()
    console.print("Step [white]3[/white] - Early Bloomers by Location Result", style="bold")
    console.print("-" * 50 + "\n" + str(result) + "\n")
    test_solution(result)
