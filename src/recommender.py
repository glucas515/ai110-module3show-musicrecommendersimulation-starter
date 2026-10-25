import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts with numeric fields converted."""
    with open(csv_path, encoding="utf-8", newline="") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return its score and matching reasons."""
    score = 0.0
    reasons = []

    if song["genre"].strip().casefold() == user_prefs["favorite_genre"].strip().casefold():
        score += 0.35
        reasons.append("genre match (+0.35)")

    if song["mood"].strip().casefold() == user_prefs["favorite_mood"].strip().casefold():
        score += 0.35
        reasons.append("mood match (+0.35)")

    energy_score = 0.30 * (1 - abs(song["energy"] - user_prefs["target_energy"]))
    if energy_score > 0:
        score += energy_score
        reasons.append(
            f"energy {song['energy']:.2f} vs target "
            f"{user_prefs['target_energy']:.2f} (+{energy_score:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by preference score and return the top k songs with scores and explanations."""
    recommendations = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        recommendations.append((song, score, "; ".join(reasons)))

    return sorted(recommendations, key=lambda recommendation: recommendation[1], reverse=True)[:k]
