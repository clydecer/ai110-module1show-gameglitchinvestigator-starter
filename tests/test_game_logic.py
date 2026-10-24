from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty  ## FIX: import the other functions so their fixes are tested too

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)  ## FIX: check_guess returns (outcome, message), so unpack it
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)  ## FIX: unpack (outcome, message)
    assert outcome == "Too High"
    assert "LOWER" in message  ## FIX: guards against the swapped-hint bug

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)  ## FIX: unpack (outcome, message)
    assert outcome == "Too Low"
    assert "HIGHER" in message  ## FIX: guards against the swapped-hint bug

def test_three_digit_guess_compares_as_number():
    # 100 vs 50 used to compare as text ("100" < "50"); it must be Too High
    outcome, _ = check_guess(100, 50)
    assert outcome == "Too High"

def test_parse_guess_rejects_decimals_and_out_of_range():
    assert parse_guess("42.9")[0] is False
    assert parse_guess("0", 1, 100)[0] is False
    assert parse_guess("101", 1, 100)[0] is False
    assert parse_guess(" 42 ", 1, 100) == (True, 42, None)

def test_wrong_guesses_always_cost_points_and_never_go_negative():
    assert update_score(10, "Too High", 2) == 5
    assert update_score(10, "Too Low", 2) == 5
    assert update_score(0, "Too High", 3) == 0

def test_first_try_win_scores_100():
    assert update_score(0, "Win", 1) == 100

def test_hard_range_is_wider_than_normal():
    assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]
