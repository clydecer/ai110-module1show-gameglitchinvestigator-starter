# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- When I was inputting my guesses, it tell me to go lower, even though I couldn't go any lower, and vice versa. 
- Another bug was that the game never restarted when i clicked the button, I had to reload the page to start a new game.
- The difficulty settings are scuffed, hard is easier than normal
-

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|99     |go lower           |go higher.       |none                    |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude AI for this project.
Claude suggested that I move the logic functions from app.py into logic_utils.py and I did. And the game was successful and the code worked.

The AI wanted to keep the try/except Type Error block in check_guess, but I wanted to remove because it wasn't needed, and the game still worked so I was right.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

 ---- I was able to see whether a bug was fixed by running the game and seeing if the problem was still there. Also, Claude was able to give me advice on what it thought looked correct, and then I was able to double check.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- I would tell them it's like a GBA emulator save state, where you have your game running and your playing, but you can reset to that point at any time and keep making your own states.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---- Overall, I think the use of AI in this project was really helpful, because it helped me see exactly was wrong with the code and really helped make sure that I can debug the program properly. Without it, this definitely would have taken a lot more time and potentially even days to fix.