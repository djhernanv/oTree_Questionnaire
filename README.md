# Questionnaire for oTree
This App allows you to create a questionnaire in form of a ranking from 1 - 10 in oTree. In this case, specifically, about the perceptions of participants about the fairnesss and the importance of skill in a game.

### Installation

1. In Terminal or PowerShell go to your oTree folder, for instance ```cd oTree```, and create the folder questionnaire with ```mkdir questionnaire``` .
2. Define the App in settings.py with:
~~~
  SESSION_CONFIGS = [
    {
        'name': 'questionnaire',
        'display_name': "Questionnaire",
        'num_demo_participants': 3,
        'app_sequence': ['questionnaire'],
    },
    # other session configs go here ...
  ]
~~~
3. If you want the questionnaire as part of another game, add it to the sequence of that games app.
4. Either download or, ideally, fork this repository and add its contents to the "questionnaire folder"
5. Ready! :-)
