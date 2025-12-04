import relationalai.semantics as rai
from pandas import Timestamp

from kg.model import ARQModel


def test_hemispheres(arq: ARQModel):
    """Test that north and south hemispheres are defined."""
    result = rai.where(
        arq.Hemisphere.id == "north",
    ).select(
        arq.Hemisphere.id,
    ).to_df()
    print(result)
    assert result.shape == (1, 1)
    assert result.iloc[0]["id"] == "north"

    result = rai.where(
        arq.Hemisphere.id == "south",
    ).select(
        arq.Hemisphere.id,
    ).to_df()
    print(result)
    assert result.shape == (1, 1)
    assert result.iloc[0]["id"] == "south"


def test_solstices_exist(arq: ARQModel):
    """Test that solstices are created for a given year."""
    result = rai.where(
        arq.Solstice.year == 2001,
    ).select(
        arq.Solstice.year,
        arq.Solstice.datetime,
    ).to_df()
    print(result)
    # Should have 2 solstices per year (summer and winter)
    assert result.shape == (2, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[1]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-06-21 07:38:00")
    assert result.iloc[1]["datetime"] == Timestamp("2001-12-21 19:22:00")


def test_summer_solstice_hemispheres(arq: ARQModel):
    """Test that summer solstice has correct hemisphere relationships."""
    # The summer solstice (June) should be summer for north, winter for south
    north = arq.Hemisphere.filter_by(id="north")
    south = arq.Hemisphere.filter_by(id="south")

    result = rai.where(
        arq.Solstice.year == 2001,
        arq.Solstice.summer(north),
    ).select(
        arq.Solstice.year,
        arq.Solstice.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-06-21 07:38:00")

    result = rai.where(
        arq.Solstice.year == 2001,
        arq.Solstice.winter(south),
    ).select(
        arq.Solstice.year,
        arq.Solstice.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-06-21 07:38:00")


def test_winter_solstice_hemispheres(arq: ARQModel):
    """Test that winter solstice has correct hemisphere relationships."""
    # The winter solstice (December) should be winter for north, summer for south
    north = arq.Hemisphere.filter_by(id="north")
    south = arq.Hemisphere.filter_by(id="south")

    result = rai.where(
        arq.Solstice.year == 2001,
        arq.Solstice.winter(north),
    ).select(
        arq.Solstice.year,
        arq.Solstice.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-12-21 19:22:00")

    result = rai.where(
        arq.Solstice.year == 2001,
        arq.Solstice.summer(south),
    ).select(
        arq.Solstice.year,
        arq.Solstice.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-12-21 19:22:00")


def test_equinoxes_exist(arq: ARQModel):
    """Test that equinoxes are created for a given year."""
    result = rai.where(
        arq.Equinox.year == 2001,
    ).select(
        arq.Equinox.year,
        arq.Equinox.datetime,
    ).to_df()
    print(result)
    # Should have 2 equinoxes per year (spring and fall)
    assert result.shape == (2, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-03-20 13:31:00")
    assert result.iloc[1]["year"] == 2001
    assert result.iloc[1]["datetime"] == Timestamp("2001-09-22 23:05:00")


def test_spring_equinox_hemispheres(arq: ARQModel):
    """Test that spring equinox has correct hemisphere relationships."""
    # The spring equinox (March) should be spring for north, fall for south
    north = arq.Hemisphere.filter_by(id="north")
    south = arq.Hemisphere.filter_by(id="south")

    result = rai.where(
        arq.Equinox.year == 2001,
        arq.Equinox.spring(north),
    ).select(
        arq.Equinox.year,
        arq.Equinox.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-03-20 13:31:00")

    result = rai.where(
        arq.Equinox.year == 2001,
        arq.Equinox.fall(south),
    ).select(
        arq.Equinox.year,
        arq.Equinox.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-03-20 13:31:00")


def test_fall_equinox_hemispheres(arq: ARQModel):
    """Test that fall equinox has correct hemisphere relationships."""
    # The fall equinox (September) should be fall for north, spring for south
    north = arq.Hemisphere.filter_by(id="north")
    south = arq.Hemisphere.filter_by(id="south")

    result = rai.where(
        arq.Equinox.year == 2001,
        arq.Equinox.fall(north),
    ).select(
        arq.Equinox.year,
        arq.Equinox.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-09-22 23:05:00")

    result = rai.where(
        arq.Equinox.year == 2001,
        arq.Equinox.spring(south),
    ).select(
        arq.Equinox.year,
        arq.Equinox.datetime,
    ).to_df()
    print(result)
    assert result.shape == (1, 2)
    assert result.iloc[0]["year"] == 2001
    assert result.iloc[0]["datetime"] == Timestamp("2001-09-22 23:05:00")
