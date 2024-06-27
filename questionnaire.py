from dominate import tags

from psynet.modular_page import ModularPage, SurveyJSControl
from psynet.page import InfoPage


def questionnaire_intro():
    html = tags.div()
    with html:
        tags.p(
            "Congratulations, you completed the listening part of this experiment!"
        )
        tags.p(
            "Before we finish, we just have a few more questions to ask you. ",
            "They should only take a couple of minutes to complete.",
        )
    return InfoPage(html, time_estimate=6)


def questionnaire():
    # https://surveyjs.io/create-free-survey - export with JSON editor
    return ModularPage(
        "questionnaire",
        "Please fill out the following questions.",
        control=SurveyJSControl(
            {
                "logoPosition": "right",
                "pages": [
                    {
                        "name": "page1",
                        "elements": [
                            {
                                "type": "text",
                                "name": "age",
                                "title": "Your age (years)",
                                "isRequired": True
                            },
                            {
                                "type": "text",
                                "name": "gender",
                                "title": "I identify my gender as _  (please specify).",
                                "isRequired": True
                            },
                            {
                                "type": "checkbox",
                                "name": "occupation",
                                "title": "Occupational status",
                                "isRequired": True,
                                "choices": [
                                    "Still at School",
                                    {
                                        "value": "At University",
                                        "text": "At University"
                                    },
                                    {
                                        "value": "In Full-time employment",
                                        "text": "In Full-time employment"
                                    },
                                    {
                                        "value": "In Part-time employment",
                                        "text": "In Part-time employment"
                                    },
                                    {
                                        "value": "Self-employed",
                                        "text": "Self-employed"
                                    },
                                    {
                                        "value": "Homemaker/full time parent",
                                        "text": "Homemaker/full time parent"
                                    },
                                    {
                                        "value": "Unemployed",
                                        "text": "Unemployed"
                                    },
                                    {
                                        "value": "Retired",
                                        "text": "Retired"
                                    }
                                ],
                                "showOtherItem": True,
                                "maxSelectedChoices": 1
                            },
                            {
                                "type": "radiogroup",
                                "name": "MT_03",
                                "title": "I have never been complimented for my talents as a musical performer",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree not disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "MT_06",
                                "title": "I can play _ musical instruments",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": "0",
                                        "text": "0"
                                    },
                                    {
                                        "value": "1",
                                        "text": "1"
                                    },
                                    {
                                        "value": "2",
                                        "text": "2"
                                    },
                                    {
                                        "value": "3",
                                        "text": "3"
                                    },
                                    {
                                        "value": "4",
                                        "text": "4"
                                    },
                                    {
                                        "value": "5",
                                        "text": "5"
                                    },
                                    {
                                        "value": "6 or more",
                                        "text": "6 or more"
                                    }
                                ],
                            },
                            {
                                "type": "radiogroup",
                                "name": "MT_07",
                                "title": "I would not consider myself a musician",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "PA_08",
                                "title": "When I sing, I have no idea whether I'm in tune or not",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "SA_03",
                                "title": "I am able to hit the right notes when I sing along with a recording",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "SA_04",
                                "title": "I am NOT able to sing in harmony when somebody is singing a familiar tune",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_01",
                                "title": "I sometimes choose music that can trigger shivers down my spine",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_02",
                                "title": "Pieces of music rarely evoke emotions for me",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_03",
                                "title": "I often pick certain music to motivate or excite me",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_04",
                                "title": "I am able to identify what is special about a given musical piece",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_05",
                                "title": "I am able to talk about the emotions that a piece of music evokes for me",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    }
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "EM_06",
                                "title": "Music can evoke my memories of past people and places",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "completely disagree"
                                    },
                                    {
                                        "value": 2,
                                        "text": "strongly disagree"
                                    },
                                    {
                                        "value": 3,
                                        "text": "disagree"
                                    },
                                    {
                                        "value": 4,
                                        "text": "neither agree nor disagree"
                                    },
                                    {
                                        "value": 5,
                                        "text": "agree"
                                    },
                                    {
                                        "value": 6,
                                        "text": "strongly agree"
                                    },
                                    {
                                        "value": 7,
                                        "text": "completely agree"
                                    },
                                ]
                            },
                            {
                                "type": "radiogroup",
                                "name": "language",
                                "title": "Is English both your and your parents' home language?",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "Yes, English is my and both my parents' home language."
                                    },
                                    {
                                        "value": 2,
                                        "text": "English is my home language, but one of my parents has a different home language."
                                    },
                                    {
                                        "value": 3,
                                        "text": "English is my home language, but both of my parents have a different home language."
                                    },
                                    {
                                        "value": 4,
                                        "text": "No, English is not my home language."
                                    },
                                ]
                            },
                            {
                                "type": "text",
                                "name": "wam_training",
                                "title": "I have received _ years of training in Western art music (Classical music).",
                                "isRequired": True
                            },
                            {
                                "type": "radiogroup",
                                "name": "handedness",
                                "title": "What is your handedness?",
                                "isRequired": True,
                                "choices": [
                                    {
                                        "value": 1,
                                        "text": "Right-handed"
                                    },
                                    {
                                        "value": 2,
                                        "text": "Left-handed"
                                    },
                                    {
                                        "value": 3,
                                        "text": "Ambidextrous"
                                    },
                                ]
                            },
                            {
                                        "type": "matrix",
                                        "name": "genre_listening",
                                        "title": "How often do you listen to the following genres of music?",
                                        "isAllRowRequired": "true",
                                        "columns": [
                                            "Never",
                                            "Seldom",
                                            "Sometimes",
                                            "Quite often",
                                            "Very often"
                                        ],
                                        "rows": [
                                            "Pop",
                                            "Rock",
                                            "Hip-hop/rap",
                                            "Metal/hard rock",
                                            "Jazz/blues",
                                            "Folk/ethnic/world",
                                            "Electronic",
                                            "Classical",
                                            "Film or video game (soundtrack)"
                                        ]
                                    },
                            {
                                "type": "matrix",
                                "name": "film_viewing",
                                "title": "How often do you watch to the following genres of film/series?",
                                "isAllRowRequired": "true",
                                "columns": [
                                    "Never",
                                    "Seldom",
                                    "Sometimes",
                                    "Quite often",
                                    "Very often"
                                ],
                                "rows": [
                                    "Thriller",
                                    "Horror",
                                    "Comedy",
                                    "Romance/drama",
                                    "Action",
                                    "Western animated",
                                    "Eastern animated (e.g., anime)",
                                    "Musical",
                                    "Science fiction",
                                    "Fantasy"
                                ]
                            },
                        ]
                    },
                ]
            }
        ),
        time_estimate=60 * 2,
        save_answer="questionnaire",
        bot_response="not yet implemented",
    )

# {
                            #     "type": "dropdown",
                            #     "name": "genre_pop",
                            #     "title": "How often do you listen to pop music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_rock",
                            #     "title": "How often do you listen to rock music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_rap",
                            #     "title": "How often do you listen to hip-hop/rap music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_metal",
                            #     "title": "How often do you listen to metal/hard rock music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_jazz",
                            #     "title": "How often do you listen to jazz/blues music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_folk",
                            #     "title": "How often do you listen to folk/ethnic/world music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_electro",
                            #     "title": "How often do you listen to electronic music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_classical",
                            #     "title": "How often do you listen to classical music?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "genre_film",
                            #     "title": "How often do you listen to film or video game music (soundtracks)?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_thriller",
                            #     "title": "How often do you watch thriller films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_horror",
                            #     "title": "How often do you watch horror films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_comedy",
                            #     "title": "How often do you watch comedy films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_romance",
                            #     "title": "How often do you watch romance or drama films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_action",
                            #     "title": "How often do you watch action films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_animated",
                            #     "title": "How often do you watch Western animated films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_anime",
                            #     "title": "How often do you watch Eastern animated films/series (e.g., anime)?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_musical",
                            #     "title": "How often do you watch musicals?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_scifi",
                            #     "title": "How often do you watch science fiction films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },
                            # {
                            #     "type": "dropdown",
                            #     "name": "film_fantasy",
                            #     "title": "How often do you watch fantasy films/series?",
                            #     "choices": [
                            #         {"value": 0, "text": "Never"},
                            #         {"value": 1, "text": "Seldom"},
                            #         {"value": 2, "text": "Sometimes"},
                            #         {"value": 3, "text": "Quite often"},
                            #         {"value": 4, "text": "Very often"},
                            #     ]
                            # },