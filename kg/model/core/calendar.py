import relationalai.semantics as rai

# Core temporal concepts used across multiple models


def define_calendar(m: rai.Model):
    """Define core calendar and temporal concepts.

    These concepts are used by observations, astronomical events, and other
    time-based entities in the knowledge graph.
    """
    m.Year = m.Concept("Year", extends=[rai.Integer])
    m.DayOfYear = m.Concept("DayOfYear", extends=[rai.Integer])

    m.CalendarEvent = m.Concept("CalendarEvent", identify_by={
        "year": m.Year,
        "datetime": rai.DateTime,
    })
