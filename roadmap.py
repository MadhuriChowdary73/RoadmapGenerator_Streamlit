import streamlit as st
import pandas as pd

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

st.write(
    "Generate a personalized roadmap based on your goal, "
    "current level, and available study time."
)

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
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
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
            "Dynamic Programming",
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
    },

    "App Development": {

        "Beginner": [
            "Programming Basics",
            "Flutter Basics",
            "Widgets",
            "Layouts",
            "Navigation",
            "Mini Apps"
        ],

        "Intermediate": [
            "Firebase",
            "APIs",
            "State Management",
            "Authentication",
            "Projects"
        ],

        "Advanced": [
            "Animations",
            "Clean Architecture",
            "Play Store Deployment",
            "Scalable Apps"
        ]
    },

    "Cyber Security": {

        "Beginner": [
            "Networking Basics",
            "Linux Basics",
            "Cyber Security Fundamentals",
            "Web Security"
        ],

        "Intermediate": [
            "Ethical Hacking",
            "Burp Suite",
            "OWASP",
            "CTF Practice"
        ],

        "Advanced": [
            "Penetration Testing",
            "Advanced Exploitation",
            "Security Auditing"
        ]
    },

    "Data Science": {

        "Beginner": [
            "Python",
            "Pandas",
            "NumPy",
            "Data Cleaning",
            "Visualization"
        ],

        "Intermediate": [
            "SQL",
            "Statistics",
            "Machine Learning",
            "Projects"
        ],

        "Advanced": [
            "Deep Learning",
            "Big Data",
            "Deployment",
            "Advanced Analytics"
        ]
    }
}

resources = {

    "DSA": {
        "YouTube": [
            "Striver",
            "Apna College",
            "Kunal Kushwaha"
        ],
        "Platforms": [
            "LeetCode",
            "GeeksforGeeks",
            "CodeStudio"
        ]
    },

    "Web Development": {
        "YouTube": [
            "CodeWithHarry",
            "JavaScript Mastery",
            "SuperSimpleDev"
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
    },

    "App Development": {
        "YouTube": [
            "Flutter",
            "Codepur",
            "Programming with Mosh"
        ],
        "Platforms": [
            "Firebase",
            "GitHub",
            "Play Console"
        ]
    },

    "Cyber Security": {
        "YouTube": [
            "NetworkChuck",
            "John Hammond",
            "David Bombal"
        ],
        "Platforms": [
            "TryHackMe",
            "Hack The Box",
            "OverTheWire"
        ]
    },

    "Data Science": {
        "YouTube": [
            "Krish Naik",
            "CampusX",
            "Data School"
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

        if time_available <= 2:
            study_type = "Slow Pace"

        elif time_available <= 5:
            study_type = "Balanced Pace"

        else:
            study_type = "Fast Pace"

        st.info(f"📚 Study Mode: {study_type}")

        st.header("📌 Your Personalized Roadmap")

        for i, step in enumerate(roadmap_steps, start=1):

            st.markdown(f"""
            <div class="goal-card">
                <h3>Step {i}: {step}</h3>
                <p>Recommended Study Time:
                {time_available} hrs/day</p>
            </div>
            """, unsafe_allow_html=True)

        st.header("📅 Personalized Monthly Timeline")

        total_steps = len(roadmap_steps)

        roadmap_plan = []

        for month in range(duration):

            start_index = int(month * total_steps / duration)

            end_index = int((month + 1) * total_steps / duration)

            month_topics = roadmap_steps[start_index:end_index]

            if month_topics:

                roadmap_plan.append({
                    "Month": f"Month {month + 1}",
                    "Focus Areas": ", ".join(month_topics)
                })

        df = pd.DataFrame(roadmap_plan)

        st.table(df)

        st.header("📈 Roadmap Completion Preview")

        progress_value = min(int((time_available / 12) * 100), 100)

        st.progress(progress_value)

        st.write(
            f"Estimated consistency level based on your "
            f"study time: {progress_value}%"
        )

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

        st.header("⏰ Suggested Daily Routine")

        coding_time = round(time_available * 0.5, 1)

        learning_time = round(time_available * 0.3, 1)

        revision_time = round(time_available * 0.2, 1)

        st.write(f"📖 Learning Concepts → {learning_time} hrs")

        st.write(f"💻 Practice/Coding → {coding_time} hrs")

        st.write(f"🔁 Revision → {revision_time} hrs")

        st.header("🔥 Motivation")

        st.success(
            f"""
            {name}, if you consistently study
            {time_available} hours daily for
            {duration} months, you can become highly skilled in {goal}.
            """
        )

    else:
        st.error("Roadmap data not available for selected option.")
