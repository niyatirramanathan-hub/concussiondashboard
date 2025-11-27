# quiz.py
import streamlit as st

def show_quiz():
    st.title("SAFETY KNOWLEDGE QUIZ")
    st.write("Test your knowledge about the safety protocols and best practices when playing!")

    # Initialize session state
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.score = 0
        st.session_state.q1 = None
        st.session_state.q2 = None
        st.session_state.q3 = None
        st.session_state.q4 = None
        st.session_state.q5 = None
        st.session_state.q6 = None
        st.session_state.q7 = None
        st.session_state.q8 = None
        st.session_state.q9 = None
        st.session_state.q10 = None
        st.session_state.q11 = None
        
    # SHOW QUIZ ONLY IF NOT SUBMITTED
    if not st.session_state.quiz_submitted:

        st.header("Safety Quiz")

        st.subheader("Which symptom can be a sign of a concussion?")
        st.session_state.q1 = st.radio(
            "",
            ["Headache", "Feeling “foggy”", "Nausea", "All of the above"],
            index=None
        )

        st.subheader("After being diagnosed with a concussion, a player can return to sports immediately.")
        st.session_state.q2 = st.radio(
            "",
            ["True", "False"],
            index=None
        )

        st.subheader("When can a player return to play after a concussion diagnosis?")
        st.session_state.q3 = st.radio(
            "                                         ",
            ["As soon as they feel better", "After completing a step-by-step return-to-play plan and being cleared by a healthcare provider", "The next day", "Whenever the coach says it’s okay"],
            index=None
        )

        st.subheader("Which symptoms mean you should seek emergency care immediately?")
        st.session_state.q4 = st.radio(
            " ",
            ["Repeated vomiting", "One pupil larger than the other", "Slurred speech", "All of the above"],
            index=None
        )

        st.subheader("How soon after a head hit can symptoms show up?")
        st.session_state.q5 = st.radio(
            "  ",
            ["Right away", "Hours later", "The next day", "Any of the above"],
            index=None
        )

        st.subheader("If you suspect a concussion during play, what’s the correct action?")
        st.session_state.q6 = st.radio(
            "    ",
            ["Sit out immediately and tell a coach/parent", "Play one more play", "Wait to see if it gets worse", "Drink water and continue"],
            index=None
        )

        st.subheader("True or false: It’s safe to return to play once symptoms go away for a few hours.")
        st.session_state.q7 = st.radio(
            "      ",
            ["True", "False"],
            index=None
        )
        
        st.subheader("What is the FIRST step in return-to-play after a concussion?")
        st.session_state.q8 = st.radio(
            "          ",
            ["Full practice", "Light cognitive work and physical rest", "Sprinting drills", "Contact practice"],
            index=None
        )

        st.subheader("True or false: If symptoms return during the return-to-play steps, the athlete should move to the next level anyway.")
        st.session_state.q9 = st.radio(
             "          ",
             ["True", "False"],
             index=None
         )

        st.subheader("Which reason do athletes MOST commonly hide symptoms?")
        st.session_state.q10 = st.radio(
            "                    ",
            ["Fear of losing playing time", "Not wanting to let the team down", "Not recognizing the symptoms", "All of the above"],
            index=None
        )

        st.subheader("If you see a teammate take a hit and look dazed, what’s the safest move?")
        st.session_state.q11 = st.radio(
            "                     ",
            ["Tell them to shake it off", "Tell your coach", "Ignore it unless they ask for help"],
            index=None
        )

        submitted = st.button("Submit Quiz")

        if submitted:
            if st.session_state.q1 is None or st.session_state.q2 is None or st.session_state.q3 is None or st.session_state.q4 is None or st.session_state.q5 is None or st.session_state.q6 is None or st.session_state.q7 is None or st.session_state.q8 is None or st.session_state.q9 is None or st.session_state.q10 is None or st.session_state.q11 is None:
                st.warning("⚠️ Please answer all questions!")
            else:
                st.session_state.quiz_submitted = True
                st.session_state.score = 0

                if st.session_state.q1 == "All of the above":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **All of the above**")
                else:
                    st.error("❌ Incorrect. The correct answer to question 1 is **All of the above**")

                if st.session_state.q2 == "False":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **False**. Feeling “normal” doesn’t equal safe- only a healthcare professional can clear an athlete.")
                else:
                    st.error("❌ Incorrect. The correct answer is **False**. Feeling “normal” doesn’t equal safe- only a healthcare professional can clear an athlete.")

                if st.session_state.q3 == "After completing a step-by-step return-to-play plan and being cleared by a healthcare provider":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **B**. Symptoms going away isn’t enough. Clearance only comes from a medical pro.")
                else:
                    st.error("❌ Incorrect. The correct answer is **B**. Symptoms going away isn’t enough. Clearance only comes from a medical pro.")

                if st.session_state.q4 == "All of the above":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **All of the above**")
                else:
                    st.error("❌ Incorrect. The correct answer is **All of the above**")

                if st.session_state.q5 == "Any of the above":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **Any of the above**")
                else:
                    st.error("❌ Incorrect. The correct answer is **Any of the above**")

                if st.session_state.q6 == "Sit out immediately and tell a coach/parent":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **Sit out immediately and tell a coach/parent**")
                else:
                    st.error("❌ Incorrect. The correct answer is **Sit out immediately and tell a coach/parent**")

                if st.session_state.q7 == "False":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **False**")
                else:
                    st.error("❌ Incorrect. The correct answer is **False**")

                if st.session_state.q8 == "Light cognitive work and physical rest":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **Light cognitive work and physical rest**")
                else:
                    st.error("❌ Incorrect. The correct answer is **Light cognitive work and physical rest**")

                if st.session_state.q9 == "False":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **False**. If symptoms come back, the athlete stops and returns to the previous step.")
                else:
                    st.error("❌ Incorrect. The correct answer is **False**. If symptoms come back, the athlete stops and returns to the previous step.")

                if st.session_state.q10 == "All of the above":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **All of the above**. Pressure, fear, and not recognizing symptoms all play a role.")
                else:
                    st.error("❌ Incorrect. The correct answer is **All of the above**. Pressure, fear, and not recognizing symptoms all play a role.")

                if st.session_state.q11 == "Tell your coach":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer is **Tell your coach**. Early reporting protects them from a second injury, which is far more dangerous.")
                else:
                    st.error("❌ Incorrect. The correct answer is **Tell your coach**. Early reporting protects them from a second injury, which is far more dangerous.")
                st.rerun()   # Hides submit button immediately
                

    # SHOW RESULT AFTER SUBMISSION
    else:
        st.success(f"🎉 You scored {st.session_state.score} out of 12!")

        if st.button("Retake Quiz"):
            st.session_state.quiz_submitted = False
            st.session_state.score = 0
            st.session_state.q1 = None
            st.session_state.q2 = None
            st.session_state.q3 = None
            st.session_state.q4 = None
            st.session_state.q5 = None
            st.session_state.q6 = None
            st.session_state.q7 = None
            st.session_state.q8 = None
            st.session_state.q9 = None
            st.session_state.q10 = None
            st.session_state.q11 = None
            st.rerun()

    
if __name__ == "__main__":
    show_quiz()
