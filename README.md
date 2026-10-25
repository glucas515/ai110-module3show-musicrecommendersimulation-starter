# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.



Real-world recommenders like Spotify and YouTube combine two ideas. Collaborative filtering looks at behavior: if listeners with tastes like yours liked a song, it may be recommended to you, using signals such as likes, skips and playlists. Content-based filtering looks at the songs themselves, comparing attributes like genre, mood, tempo and energy with music you already like. Real platforms do this at a much larger scale, learning from millions of listeners and billions of plays, and they learn what to weigh from that data, while my version uses a handful of weights I chose by hand. My version is content-based only, because it has a small catalog and a single user profile, with no listening history from other users to learn from. Each song is compared with the user's taste profile and given a score. The score prioritizes how close a song's energy is to the user's target energy, then whether the mood matches, then whether the genre matches. The songs with the highest scores are recommended.

### Features used

**`Song`** (loaded from `data/songs.csv`):
- Used in scoring: `genre`, `mood`, `energy`
- Available for later experiments: `tempo_bpm`, `valence`, `danceability`, `acousticness`
- Identifying only: `id`, `title`, `artist`

**`UserProfile`:**
- `favorite_genre`
- `favorite_mood`
- `target_energy` (0 to 1)
- `likes_acoustic` (True or False), reserved to pair with `acousticness` in later experiments

### Scoring and ranking

- **Score one song** (`score_song`): 0.25 if the genre matches, plus 0.35 if the mood matches, plus 0.40 × (1 − |song energy − target energy|). The function also returns the reasons for the score.
- **Rank** (`recommend_songs` and `Recommender.recommend`): score every song, sort from highest to lowest, and return the top `k` with an explanation for each.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



