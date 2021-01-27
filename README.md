# Deep-Lyrics
Alexa Skill to generate lyrics from scratch or extend from a prompt using Deep Learning based models in in NLP.

## Concept
The skill aims to help the user build upon their lyrics which might be helpful for any musician, poet or anyone facing a writing block. 
<p> The user can invoke the skill in several ways:
</p>

* Saying "Generate some lyrics" or "Write some lyrics".
* Giving a prompt to build lyrics on. For example, "Start with **_prompt_**." or "Write a song with **_prompt_**."

Upon generating lyrics, the user can ask the skill to continue building on the output. The model uses the last line 

## Datasets Explored

Several datasets were explored for the project.

1. [Lyrics dataset of different artists.](https://www.kaggle.com/paultimothymooney/poetry)
2. [Lyrics of artists from different genres.](https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres)

The issue with working with these datasets was that they weren't very clean and lacked variability within lyrics. 

For example, a large number of lyrics had instructions on how to play the song, chords and other irrelevant information.

Therefore, we decided to build a custom dataset by scraping lyrics.

## Models Used
* We started by exploring with simple fully connected networks and GRUs which yielded poor results. 
* Then a Bidirectional LSTM model was explored which gave better results than other LSTM implementation of the datasets above.
* Finally, we settled on using GPT-2 as it was able to capture the structure of lyrics in the output.
* Both Huggingface Transformers library and OpenAI's implementation were attempted.


