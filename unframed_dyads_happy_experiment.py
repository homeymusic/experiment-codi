# Adjective: Happy
# Dyads: Unframed
# Bass Pitch: Fixed at 60

# Copying imports from the modes experiment. Will remove unused ones later. Adding others as needed.
import random
from random import randint

from dominate import tags
from numpy import isnan
from numpy import linspace
from markupsafe import Markup

import psynet.experiment
from psynet.js_synth import JSSynth, InstrumentTimbre, Note, HarmonicTimbre, Chord
from psynet.modular_page import SurveyJSControl, PushButtonControl
from psynet.page import InfoPage, SuccessfulEndPage, ModularPage, WaitPage, UnsuccessfulEndPage
from psynet.prescreen import AntiphaseHeadphoneTest
from psynet.timeline import Timeline, Event, conditional, join
from psynet.trial.static import StaticTrial, StaticNode, StaticTrialMaker
from psynet.utils import get_logger, corr
from psynet.bot import Bot

from .consent import consent, NoConsent
from .debrief import debriefing
from .instructions import instructions
from .questionnaire import questionnaire, questionnaire_intro
from .stimuli import load_scales, load_melodies
from .volume_calibration import volume_calibration

logger = get_logger()

TIMBRE = HarmonicTimbre(10, 3.0)

# Unframed Dyads
CHORDS = list(map(lambda interval: [0, interval], linspace(start=0, stop=15, num=1000)))

TRIALS_PER_PARTICIPANT = 68
N_REPEAT_TRIALS = 68
BREAK_AFTER_N_TRIALS = 68

NODES = [
    StaticNode(
        definition={
            "chord": chord
        },
    )
    for chord in CHORDS
]

class ChordTrial(StaticTrial):
    time_estimate = 3

    @property
    def base_chord(self):
        return self.definition["chord"]

    # def rating_attribute(self):
    #     return self.definition["rating_attribute"]

    def finalize_definition(self, definition, experiment, participant):
        definition["duration"] = 3
        definition["base_pitch"] = 60

        # TODO: work out correct way to refer to chord.
        definition["realized_chord"] = [note + definition["base_pitch"]
                                        for note in self.base_chord]

        return definition

    def get_bot_response(self, bot):
        if self.is_repeat_trial:
            return self.parent_trial.answer
        else:
            return self.generate_answer(bot)

    def generate_answer(self, bot):
        match bot.id % 2:  # 2 different responding styles
            case 0: #Static response
                return 3
            case 1: #Random response
                return randint(1, 5)

    def show_trial(self, experiment, participant):
        trial_page = ModularPage(
            "rating",
            JSSynth(
                (
                    Markup("""
                    <p>
                    How happy or sad is this chord? 
                    </p>
                    """
                           )
                ),
                [
                    Chord(self.definition["realized_chord"],
                          duration=self.definition["duration"])
                ],
                timbre=TIMBRE,
                text_align="center",
            ),
            PushButtonControl(
                [1, 2, 3, 4, 5],
                ["Very sad", "Somewhat sad", "Neutral", "Somewhat happy", "Very happy"],
                arrange_vertically=False,
                bot_response=self.get_bot_response,
                style="width: 150px; margin: 10px",
            ),
            time_estimate=3,
        )

        break_page = WaitPage(
            wait_time=20,
            content="Please relax for a few moments, we will continue the experiment shortly.",
        )

        if self.position != 0 and self.position % BREAK_AFTER_N_TRIALS == 0:
            return join(break_page, trial_page)
        else:
            return trial_page


class ChordsTrialMaker(StaticTrialMaker):
    performance_check_type = "consistency"
    consistency_check_type = "spearman_correlation"
    give_end_feedback_passed = False

    def compute_performance_reward(self, score, passed):
        max_bonus = 0.40

        if score is None or score <= 0.0:
            bonus = 0.0
        else:
            bonus = max_bonus * score

        bonus = min(bonus, max_bonus)
        return bonus


class Exp(psynet.experiment.Experiment):
    label = "Dyads happy experiment"
    test_n_bots = 12

    timeline = Timeline(
        consent,
        # InfoPage(
        #     tags.div(
        #         tags.p("This experiment requires you to wear headphones. Please ensure you have plugged yours in now."),
        #         tags.p("The next page will play some test audio. Please turn down your volume before proceeding.")
        #     ),
        #     time_estimate=5,
        # ),
        # volume_calibration(mean_pitch=67, sd_pitch=5, timbre=TIMBRE),
        # InfoPage(
        #     """
        #     We will now perform a short listening test to verify that your audio is working properly.
        #     This test will be difficult to pass unless you listen carefully over your headphones.
        #     Press 'Next' when you are ready to start.
        #     """,
        #     time_estimate=5,
        # ),
        # AntiphaseHeadphoneTest(performance_threshold=0),
        # instructions(),
        ChordsTrialMaker(
            id_="main_experiment",
            trial_class=ChordTrial,
            nodes=NODES,
            expected_trials_per_participant=TRIALS_PER_PARTICIPANT,
            max_trials_per_participant=TRIALS_PER_PARTICIPANT,
            recruit_mode="n_participants",
            allow_repeated_nodes=False,
            n_repeat_trials=N_REPEAT_TRIALS,
            balance_across_nodes=False,
            target_n_participants=100,
            check_performance_at_end=True,
        ),
        # questionnaire_intro(),
        # questionnaire(),
        debriefing(),
        SuccessfulEndPage(),
    )

    def test_check_bot(self, bot: Bot, **kwargs):
        module_state = bot.module_states["main_experiment"][0]
        performance_check = module_state.performance_check
        assert performance_check is not None
        assert performance_check["passed"]

        if bot.id % 4 in [2, 3]:
            assert performance_check["score"] == 1.0
            assert bot.performance_reward > 0.0

        chord_trials = [t for t in bot.alive_trials if isinstance(t, ChordTrial)]
        assert len(chord_trials) == TRIALS_PER_PARTICIPANT * 2
