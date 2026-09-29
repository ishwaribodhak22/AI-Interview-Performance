def create_report(interview_score, final_score, grammar_errors,
                  filler_words, sentiment, feedback):

    report = f"""
AI INTERVIEW PERFORMANCE REPORT
====================================

Interview Score      : {interview_score}/10
Communication Score : {final_score}/100

Grammar Errors      : {grammar_errors}
Filler Words        : {filler_words}
Sentiment           : {sentiment}

AI Suggestions
--------------------------
"""

    for item in feedback:
        report += f"\n• {item}"

    return report