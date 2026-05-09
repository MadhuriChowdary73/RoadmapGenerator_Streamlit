

import streamlit as st
import pandas as pd
from datetime import datetime


st.set_page_config(
    page_title="AI Career Roadmap Generator",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
}

.goal-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 5px solid #8b5cf6;
}

.resource-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Career Roadmap Generator")
st.write("Generate a personalized roadmap based on your goal, skill level, and available time.")


name = st.text_input("Enter Your Name")

goal = st.selectbox(
    "Choose Your Goal",
    [
        "DSA",
        "Web Development",
        "Machine Learning",
        "App Development",
        "Cyber Security",
        "Data Science"
    ]
)

level = st.selectbox(
    "Current Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

time_available = st.slider(
    "Hours You Can Study Per Day",
    1,
    12,
    3
)

duration = st.slider(
    "Roadmap Duration (Months)",
    1,
    24,
    6
)


roadmaps = {

    "DSA": {
        "Beginner": [
            "Learn Programming Basics",
            "Arrays and Strings",
            "Linked Lists",
            "Stacks and Queues",
            "Trees",
            "Graphs",
            "Dynamic Programming",
            "Mock Interviews"
        ],

        "Intermediate": [
            "Advanced Trees",
            "Graphs",
            "DP",
            "Greedy Algorithms",
            "Segment Trees",
            "Competitive Coding",
            "LeetCode Practice"
        ],

        "Advanced": [
            "Hard LeetCode Problems",
            "System Design Basics",
            "Codeforces",
            "Interview Preparation",
            "Contest Practice"
        ]
    },

    "Web Development": {
        "Beginner": [
            "HTML",
            "CSS",
            "JavaScript",
            "Responsive Design",
            "Git & GitHub",
            "Mini Projects",
            "Deploy Website"
        ],

        "Intermediate": [
            "React",
            "API Integration",
            "Node.js",
            "MongoDB",
            "Authentication",
            "Full Stack Projects"
        ],

        "Advanced": [
            "Next.js",
            "System Design",
            "Docker",
            "AWS Basics",
            "Scalable Apps"
        ]
    },

    "Machine Learning": {
        "Beginner": [
            "Python",
            "NumPy",
            "Pandas",
            "Data Visualization",
            "Linear Algebra",
            "Statistics"
        ],

        "Intermediate": [
            "Scikit-Learn",
            "ML Algorithms",
            "Projects",
            "Feature Engineering",
            "Model Evaluation"
        ],

        "Advanced": [
            "Deep Learning",
            "TensorFlow",
            "NLP",
            "Computer Vision",
            "MLOps"
        ]
    }
}


resources = {

    "DSA": {
        "YouTube": [
            "Striver DSA Sheet",
            "Apna College DSA",
            "Kunal Kushwaha"
        ],
        "Platforms": [
            "LeetCode",
            "CodeStudio",
            "GeeksforGeeks"
        ]
    },

    "Web Development": {
        "YouTube": [
            "CodeWithHarry",
            "SuperSimpleDev",
            "JavaScript Mastery"
        ],
        "Platforms": [
            "Frontend Mentor",
            "freeCodeCamp",
            "GitHub"
        ]
    },

    "Machine Learning": {
        "YouTube": [
            "Krish Naik",
            "CampusX",
            "Andrew Ng"
        ],
        "Platforms": [
            "Kaggle",
            "Coursera",
            "Google Colab"
        ]
    }
}


if st.button("Generate Roadmap"):

    st.success(f"Roadmap Generated Successfully for {name} 🎯")

    roadmap_steps = roadmaps.get(goal, {}).get(level, [])

    if roadmap_steps:

        st.header("📌 Your Personalized Roadmap")

        for i, step in enumerate(roadmap_steps, start=1):

            st.markdown(f"""
            <div class="goal-card">
            <h3>Step {i}: {step}</h3>
            <p>Recommended study time: {time_available} hrs/day</p>
            </div>
            """, unsafe_allow_html=True)

        # ---------------- TIMELINE TABLE ----------------
        st.header("📅 Monthly Timeline")

        months = []
        tasks = []

        for idx, task in enumerate(roadmap_steps):
            months.append(f"Month {idx+1}")
            tasks.append(task)

        df = pd.DataFrame({
            "Month": months,
            "Focus Area": tasks
        })

        st.table(df)

        st.header("🎥 Recommended Resources")

        yt_resources = resources.get(goal, {}).get("YouTube", [])
        platforms = resources.get(goal, {}).get("Platforms", [])

        st.subheader("📺 YouTube Channels")

        for yt in yt_resources:
            st.markdown(f"""
            <div class="resource-box">
            ✅ {yt}
            </div>
            """, unsafe_allow_html=True)

        st.subheader("💻 Practice Platforms")

        for p in platforms:
            st.markdown(f"""
            <div class="resource-box">
            🚀 {p}
            </div>
            """, unsafe_allow_html=True)

        
        st.header("🔥 Motivation")

        st.info(
            f"""
            If you consistently study {time_available} hours daily
            for {duration} months, you can become strong in {goal}.
            """
        )

    else:
        st.error("Roadmap data not available for selected option.")