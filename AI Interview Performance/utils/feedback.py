def generate_feedback(grammar_errors, filler_words, sentiment):

    feedback = []

    # Grammar Feedback
    if grammar_errors == 0:
        feedback.append("✅ Excellent grammar.")
    elif grammar_errors <= 2:
        feedback.append("⚠️ Improve your grammar slightly.")
    else:
        feedback.append("❌ Too many grammar mistakes. Practice writing and speaking.")

    # Filler Word Feedback
    if filler_words <= 2:
        feedback.append("✅ Good! You used very few filler words.")
    elif filler_words <= 5:
        feedback.append("⚠️ Try to reduce filler words like 'um' and 'actually'.")
    else:
        feedback.append("❌ Too many filler words. Pause for a second instead of saying 'um' or 'like'.")

    # Sentiment Feedback
    if "Positive" in sentiment:
        feedback.append("😊 Excellent positive attitude.")
    elif "Neutral" in sentiment:
        feedback.append("🙂 Try to sound more enthusiastic and confident.")
    else:
        feedback.append("😟 Your answer sounds negative. Try to maintain a positive tone.")

    return feedback