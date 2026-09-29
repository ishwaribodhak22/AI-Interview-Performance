import plotly.graph_objects as go


# =====================================================
# 1. Communication Gauge Chart
# =====================================================

def gauge_chart(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=score,
            number={"suffix": "%", "font": {"size": 42}},
            delta={"reference": 75},

            title={
                "text": "<b>Communication Score</b>",
                "font": {"size": 24}
            },

            gauge={

                "axis": {
                    "range": [0, 100],
                    "tickwidth": 2,
                    "tickcolor": "white"
                },

                "bar": {
                    "color": "#00E5FF",
                    "thickness": 0.35
                },

                "bgcolor": "#1E293B",

                "borderwidth": 2,
                "bordercolor": "white",

                "steps": [

                    {"range": [0, 40], "color": "#EF4444"},
                    {"range": [40, 70], "color": "#FACC15"},
                    {"range": [70, 100], "color": "#22C55E"}

                ],

                "threshold": {

                    "line": {
                        "color": "white",
                        "width": 6
                    },

                    "thickness": 0.8,
                    "value": score
                }
            }
        )
    )

    fig.update_layout(

        paper_bgcolor="#111827",
        font_color="white",
        height=420,
        margin=dict(l=30, r=30, t=80, b=30)

    )

    return fig


# =====================================================
# 2. Performance Bar Chart
# =====================================================

def performance_chart(interview, grammar, filler):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=[
                "Interview",
                "Grammar",
                "Filler Words"
            ],

            y=[
                interview,
                grammar,
                filler
            ],

            text=[
                round(interview, 2),
                grammar,
                filler
            ],

            textposition="outside",

            marker=dict(

                color=[
                    "#3B82F6",
                    "#F59E0B",
                    "#EF4444"
                ]

            )

        )

    )

    fig.update_layout(

        title={
            "text": "<b>Performance Analysis</b>",
            "x": 0.5
        },

        paper_bgcolor="#111827",
        plot_bgcolor="#111827",

        font_color="white",

        yaxis_title="Values",

        height=420,

        showlegend=False

    )

    return fig


# =====================================================
# 3. Donut Chart
# =====================================================

def donut_chart(interview, grammar, filler):

    fig = go.Figure(

        data=[

            go.Pie(

                labels=[
                    "Interview Score",
                    "Grammar Errors",
                    "Filler Words"
                ],

                values=[
                    interview,
                    grammar,
                    filler
                ],

                hole=0.60,

                marker=dict(

                    colors=[
                        "#3B82F6",
                        "#F59E0B",
                        "#EF4444"
                    ]

                )

            )

        ]

    )

    fig.update_layout(

        title={
            "text": "<b>Analysis Distribution</b>",
            "x": 0.5
        },

        paper_bgcolor="#111827",

        font_color="white",

        height=420

    )

    return fig


# =====================================================
# 4. Radar Chart
# =====================================================

def radar_chart(score, grammar, filler, sentiment):

    if "Positive" in sentiment:
        sentiment_score = 95

    elif "Neutral" in sentiment:
        sentiment_score = 70

    else:
        sentiment_score = 40

    grammar_score = max(100 - grammar * 10, 10)
    filler_score = max(100 - filler * 8, 10)

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=[
                score,
                grammar_score,
                filler_score,
                sentiment_score,
                score
            ],

            theta=[
                "Communication",
                "Grammar",
                "Fluency",
                "Sentiment",
                "Communication"
            ],

            fill="toself",

            line=dict(
                color="#00E5FF",
                width=3
            )

        )

    )

    fig.update_layout(

        polar=dict(

            bgcolor="#111827",

            radialaxis=dict(

                visible=True,

                range=[0, 100],

                tickfont=dict(
                    color="white"
                )

            )

        ),

        paper_bgcolor="#111827",

        font_color="white",

        title={
            "text": "<b>Skill Radar</b>",
            "x": 0.5
        },

        height=420,

        showlegend=False

    )

    return fig