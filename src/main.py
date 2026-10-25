"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.38,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "likes_acoustic": False,
    },
    "Conflict: chill lofi at high energy": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.90,
        "likes_acoustic": True,
    },
    "Mood not in catalog": {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Genre and mood clash": {
        "favorite_genre": "classical",
        "favorite_mood": "angry",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Acoustic fan": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "likes_acoustic": True,
    },
    "Out-of-range energy": {
        "favorite_genre": "none",
        "favorite_mood": "sad",
        "target_energy": 2.00,
        "likes_acoustic": True,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in PROFILES.items():
        print(
            f"\nProfile: {profile_name} "
            f"(genre={user_prefs['favorite_genre']}, "
            f"mood={user_prefs['favorite_mood']}, "
            f"target_energy={user_prefs['target_energy']}, "
            f"likes_acoustic={user_prefs['likes_acoustic']})"
        )

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top recommendations:")
        for index, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{index}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            if explanation:
                for reason in explanation.split("; "):
                    print(f"  - {reason}")
            else:
                print("  - no matching reasons")
            if index < len(recommendations):
                print()


if __name__ == "__main__":
    main()
