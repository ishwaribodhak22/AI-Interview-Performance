def communication_score(interview_score, grammar_errors, filler_words, sentiment):

    # Convert interview score (out of 10) to 40 marks
    score = interview_score * 4

    # Grammar deduction
    score -= grammar_errors * 2

    # Filler word deduction
    score -= filler_words * 2

    # Sentiment bonus
    if "Positive" in sentiment:
        score += 15
    elif "Neutral" in sentiment:
        score += 8
    else:
        score += 2

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    return round(score, 2)