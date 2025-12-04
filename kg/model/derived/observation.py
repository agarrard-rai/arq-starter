import relationalai.semantics as rai

# Derived relationships for observations


def define_derived_observation(m: rai.Model):
    """Define derived relationships for observations.

    Includes geographic relationships derived from observation coordinates,
    such as hemisphere assignments based on latitude and longitude.
    """
    # Derived relationship: hemisphere based on latitude and longitude
    # Each observation can be in multiple hemispheres (e.g., north AND east)
    # Northern hemisphere: latitude >= 0, Southern hemisphere: latitude < 0
    # Eastern hemisphere: longitude >= 0, Western hemisphere: longitude < 0

    rai.define(
        m.Observation.hemisphere(m.HemisphereNorth)
    ).where(
        m.Observation.latitude >= 0
    )

    rai.define(
        m.Observation.hemisphere(m.HemisphereSouth)
    ).where(
        m.Observation.latitude < 0
    )

    rai.define(
        m.Observation.hemisphere(m.HemisphereEast)
    ).where(
        m.Observation.longitude >= 0
    )

    rai.define(
        m.Observation.hemisphere(m.HemisphereWest)
    ).where(
        m.Observation.longitude < 0
    )
