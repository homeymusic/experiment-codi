from dominate.tags import div, p, span, h1, strong, ul, li, em

from psynet.consent import NoConsent
from psynet.modular_page import ModularPage, CheckboxControl
from psynet.page import InfoPage
from psynet.timeline import Module, join

debriefing_html = div()

with debriefing_html:
    h1("Debriefing")
    p(
        """
        Thank you for taking part in this experiment. 
        """
    )
    p(
        """
        In this study, we are examining the perceived happiness or sadness of different musical chords.
        In addition to this, we are interested in uncovering the
        specific structural features in the chords that are responsible for driving their happiness or sadness. 
        These features could be related to interval size, pitch height, or familiarity, to name only a few. 
        We are also interested in the drivers of individual differences in responses to these chords.
        """
    )
    p(
        """
        Thank you for helping us shed light on this section of music psychology.
        """
    )
    p(
        """
        For any questions or concerns please contact Joshua Frank at jbf43@cam.ac.uk.
        """
    )

def debriefing():
    return Module(
        "debriefing",
        join(
            InfoPage(debriefing_html, time_estimate=20),
        )
    )
