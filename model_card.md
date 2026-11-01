# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
The system works much better for listeners whose tastes are well represented in the catalog. A chill lofi listener gets four strong matches (0.99, 0.99, 0.64 and 0.62), but a deep intense rock listener gets only two (1.00 and 0.65) before the scores fall to 0.29. This happens because genre and mood only score on exact label matches, and 13 of the 15 genres and 11 of the 14 moods appear on just one song. The system also ignores likes_acoustic completely, and it never checks that target_energy is between 0 and 1, so an out-of-range value gives every song a score of 0. Together these make the recommender narrow and unintentionally favor some users over others.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 



### What I noticed

- Ordinary profiles gave sensible top results, such as Sunrise City for pop/happy and Library Rain and Midnight Coding for chill lofi.
- Genre and mood together are worth 0.70 of the score, so they can outweigh a large energy mismatch. A chill lofi listener asking for energy 0.90 still gets the calm lofi songs first.
- A mood that isn't in the catalog ("sad") contributes nothing, so the results fall back to genre and energy and include a happy song.
- Beyond the first two or three results, scores drop to about 0.3 and the list is effectively "songs with similar energy."
- `likes_acoustic` is stored in the profile but isn't used, so an acoustic fan gets the same results as everyone else.
- A target energy outside 0 to 1 isn't rejected. It produces all-zero scores in CSV order.

### Does it feel right?

For High-Energy Pop, the results feel right: Sunrise City first, then Gym Hero and Rooftop Lights. A workout pop track and a bright indie-pop track both fit that listener.

For Deep Intense Rock, Storm Runner first is right, but Gym Hero second feels off. It's a pop song that gets there through the "intense" mood and high energy. Iron Comet (metal, angry, energy 0.94) is arguably closer to rock, yet it scores only 0.29 because the scoring treats "metal" and "rock" as completely different.

The same song doesn't win every list, because the #1 result changes with the profile. But Gym Hero and Storm Runner each appear in the top 5 of 5 of the 7 meaningful profiles, and four songs never appear at all. That comes from the small catalog and from energy being the only graded signal, which fills the lower positions with high-energy songs.

Storm Runner scores 0.997 for the Deep Intense Rock profile (0.35 genre + 0.35 mood + 0.297 energy), and Gym Hero scores 0.647 (0.35 mood + 0.297 energy) without a genre match. The scoring never penalizes a mismatch, so a pop song can rank second for a rock listener just by matching the mood and the energy.

### User profiles I tested

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Chill Lofi with energy 0.90
- Pop/sad
- Classical/angry
- Acoustic fan (pop/happy, energy 0.80)
- Energy 2.0

### What surprised me

I was surprised that Gym Hero could rank near the top for several very different profiles, including Pop/sad and Deep Intense Rock. Its high energy and intense mood help it score well even when its genre or mood is not the profile's match. I also expected raising Chill Lofi's energy to 0.90 to change the results more, but the two lofi songs still lead. The acoustic preference did not create a noticeably different set of recommendations, which fits with the fact that the model does not use that preference.

### Comparing profile pairs

- **High-Energy Pop vs. Chill Lofi:** High-Energy Pop puts Sunrise City first (0.98), followed by Gym Hero (0.64) and Rooftop Lights (0.61). Chill Lofi instead puts Library Rain and Midnight Coding first (both 0.99), then Focus Flow (0.64) and Spacewalk Thoughts (0.62). The pop and lofi profiles favor different genres and moods, so the change in leading songs makes sense.
- **High-Energy Pop vs. Deep Intense Rock:** Sunrise City leads for High-Energy Pop at 0.98, while Storm Runner leads for Deep Intense Rock at 1.00. Gym Hero appears in both lists (0.64 for Pop and 0.65 for Rock), while Iron Comet is third for Rock at 0.29. The rock profile's intense mood and genre favor Storm Runner, while Gym Hero's high energy and intense mood help it appear despite being pop.
- **Chill Lofi vs. Chill Lofi at energy 0.90:** With the regular Chill Lofi profile, Library Rain and Midnight Coding both score 0.99. At energy 0.90, Midnight Coding scores 0.86 and Library Rain 0.83. Their order switches and their scores are lower because the requested energy is higher than what these calm lofi songs offer.
- **Pop/happy vs. Pop/sad:** Pop/happy (the Acoustic fan profile at energy 0.80) puts Sunrise City first at 0.99, then Rooftop Lights at 0.64 and Gym Hero at 0.61. Pop/sad instead puts Gym Hero first at 0.64 and Sunrise City second at 0.63. Because "sad" is not in the catalog, that profile cannot get a sad-mood match; genre and energy still help pop songs rank. Gym Hero keeps showing up for people who want Happy Pop because it is pop and intense, and has very high energy, even though its mood is not happy.
- **High-Energy Pop at 0.90 vs. Acoustic fan at 0.80:** The High-Energy Pop results are Sunrise City at 0.98, Gym Hero at 0.64, and Rooftop Lights at 0.61. The Acoustic fan profile (pop/happy at energy 0.80) gives Sunrise City 0.99, Rooftop Lights 0.64, and Gym Hero 0.61. Sunrise City leads both, while Rooftop Lights moves ahead of Gym Hero for the Acoustic fan; the model does not use the acoustic preference, and the different energy target helps explain the change in ordering and scores.


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
