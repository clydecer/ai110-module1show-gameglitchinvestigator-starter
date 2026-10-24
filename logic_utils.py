def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200  ## FIX: Hard was 1-50 (easier than Normal); widened to 1-200 so it's actually harder
    return 1, 100


def parse_guess(raw: str, low: int = None, high: int = None):  ## FIX: added optional low/high so out-of-range guesses can be rejected
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()  ## FIX: ignore stray spaces so " 42" counts as "42"

    if raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)  ## FIX: no longer silently truncates decimals ("42.9" used to become 42)
    except ValueError:
        return False, None, "Please enter a whole number."  ## FIX: clearer message that also covers decimals

    if low is not None and high is not None and not (low <= value <= high):  ## FIX: reject guesses outside the difficulty's range
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"  ## FIX: hint messages were swapped (Too High used to say "Go HIGHER!")
    return "Too Low", "📉 Go HIGHER!"  ## FIX: removed the string-comparison fallback; guesses are always compared as numbers


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)  ## FIX: was (attempt_number + 1); a first-try win now scores 100 instead of 70
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):  ## FIX: "Too High" used to give +5 on even attempts; every wrong guess now costs 5
        return max(0, current_score - 5)  ## FIX: score can no longer go negative

    return current_score
