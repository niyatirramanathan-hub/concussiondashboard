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

    # SHOW QUIZ ONLY IF NOT SUBMITTED
    if not st.session_state.quiz_submitted:

        st.header("Safety Quiz")

        st.subheader("Which symptom can be a sign of a concussion?")
        st.session_state.q1 = st.radio(
            "You don’t have to black out to have a concussion. Most athletes never do.",
            ["Headache", "Feeling “foggy”", "Nausea", "All of the above"],
            index=None
        )

        st.subheader("After being diagnosed with a concussion, a player can return to sports immediately.")
        st.session_state.q2 = st.radio(
            "A concussion isn’t over when symptoms fade",
            ["True", "False"],
            index=None
        )

        st.subheader("When can a player return to play after a concussion diagnosis?")
        st.session_state.q3 = st.radio(
            "Yes, a concussion is a traumatic brain injury, affecting the head",
            ["As soon as they feel better", "After completing a step-by-step return-to-play plan and being cleared by a healthcare provider", "The next day", "Whenever the coach says it’s okay"],
            index=None
        )

        submitted = st.button("Submit Quiz")

        if submitted:
            if st.session_state.q1 is None or st.session_state.q2 is None or st.session_state.q3 is None:
                st.warning("⚠️ Please answer all questions!")
            else:
                st.session_state.quiz_submitted = True
                st.session_state.score = 0

                if st.session_state.q1 == "All of the above":
                    st.session_state.score += 1
                    st.success("✅ Correct! The answer to question 1 is **All of the above**")
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

                st.rerun()   # Hides submit button immediately

    # SHOW RESULT AFTER SUBMISSION
    else:
        st.success(f"🎉 You scored {st.session_state.score} out of 3!")

        if st.button("Retake Quiz"):
            st.session_state.quiz_submitted = False
            st.session_state.score = 0
            st.session_state.q1 = None
            st.session_state.q2 = None
            st.session_state.q3 = None
            st.rerun()

    
if __name__ == "__main__":
    show_quiz()
