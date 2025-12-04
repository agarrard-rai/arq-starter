import relationalai.semantics as rai

# Core geographic concepts


def define_geography(m: rai.Model):
    """Define core geographic concepts.

    Geographic concepts include hemispheres, coordinates, and spatial references
    used across the knowledge graph for location-based analysis.

    Defines four hemispheres:
    - Northern (latitude >= 0)
    - Southern (latitude < 0)
    - Eastern (longitude >= 0)
    - Western (longitude < 0)
    """
    # Hemispheres
    m.Hemisphere = m.Concept("Hemisphere", identify_by={"id": rai.String})
    rai.define(north := m.Hemisphere.new(id="north"))
    rai.define(south := m.Hemisphere.new(id="south"))
    rai.define(east := m.Hemisphere.new(id="east"))
    rai.define(west := m.Hemisphere.new(id="west"))

    # Store references for use by other modules
    m.HemisphereNorth = north
    m.HemisphereSouth = south
    m.HemisphereEast = east
    m.HemisphereWest = west

    # Coordinate value concepts
    m.Latitude = m.Concept("Latitude", extends=[rai.Float])
    m.Longitude = m.Concept("Longitude", extends=[rai.Float])
    m.H3Cell = m.Concept("H3Cell", extends=[rai.Integer])
