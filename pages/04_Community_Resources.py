import streamlit as st

st.markdown("""
<style>
    .news-container {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: thin;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
    }
    .news-card {
        flex: 0 0 auto;
        width: 300px;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        cursor: pointer;
        display: inline-block;
        vertical-align: top;
    }
    .news-card:hover {
        transform: translateY(-5px);
    }
    .news-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    .news-content {
        padding: 15px;
    }
    .news-title {
        font-weight: bold;
        margin-bottom: 8px;
    }
    .news-desc {
        font-size: 14px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)


# Sample news data
news_data = [
    {
        "title": "Researchers at the Forefront on Breakthrough Concussion Studies",
        "description": "New study reveals that starting vision therapy right after a concussion can boost recovery by 8x—here’s why waiting could make things worse!",
        "image_url": "https://www.salus.edu/news-stories/_files/images/mitch-scheiman-informal-headshot1.jpeg",
        "link": "https://www.salus.edu/news-stories/2025/10/researchers-at-the-forefront-on-breakthrough-concussion-studies.html"
    },
    {
        "title": "Investigating the long-term impacts of concussions on youth athletes",
        "description": "School of Medicine researcher Jessie Oldham is studying why athletes with a past concussion are more at risk of sustaining future musculoskeletal injuries like lower-body sprains and muscle tears.",
        "image_url": "https://news.vcu.edu/image/07869e94-6abf-405d-a806-503a2ad7d6cf",
        "link": "https://news.vcu.edu/article/youth-athlete-concussion-research"
    },
    {
        "title": "Eagles safety diagnosed with concussion after practice",
        "description": "Eagles safety Marcus Epps has been added to the injury report after being diagnosed with a concussion.",
        "image_url": "data:image/jpeg;base64,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",
        "link": "https://www.nbcsportsphiladelphia.com/nfl/philadelphia-eagles/eagles-safety-diagnosed-with-concussion-after-practice/703989/"
    }
]

def main():
    # Page header
    st.title("🌐 Community Resources")

    # Community Info section
    st.header("Community Info")
    st.info("""

    Stay updated with the latest **news**, **events**, and **announcements**. Scroll through the news cards below and click on any that **catch your eye** 👀 to learn more.
    """)

    st.toast("Welcome to **our vibrant community!** ", icon="🎉", duration = 7)

    # News cards section
    st.subheader("Latest News & Updates")

    # Horizontal scrollable container for news cards
    news_cards_html = "<div class='news-container'>"

    for news in news_data:
        # HTML for each news card
        news_cards_html += f"""
<a href="{news['link']}" style="text-decoration: none; color: inherit;">
    <div class="news-card">
        <img src="{news['image_url']}" class="news-image" alt="{news['title']}">
        <div class="news-content">
            <div class="news-title">{news['title']}</div>
            <div class="news-desc">{news['description']}</div>
        </div>
    </div>
</a>
        """

    news_cards_html += "</div>"
    st.markdown(news_cards_html, unsafe_allow_html=True)

    # Spacing at the bottom
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.divider()


# FAQ's

    st.title("FAQs")

    # FAQ 1
    with st.expander("1. How does the app detect whether I have a concussion?"):
        st.markdown("""
    ### 🧠 How the Detection Works
    The app uses an **LLM** trained on medical and sports-related data such as:

    - **Symptoms you report**
    - **Injury**


    After you upload the required inputs, the model analyzes the patterns and predicts whether the signs indicate a:

    - ✅ **Possible concussion**, or
    - ❌ **No concussion detected**

    > ⚠️ **Important:** This app is meant to assist players, coaches, parents, and trainers with quick assessments.
    > It does **not** replace professional medical diagnosis.
    """
                    )


    # FAQ 2
    with st.expander("2. What should I do if the app predicts a concussion?"):
        st.markdown("""
    ### If the App Predicts a Concussion
    If the result indicates a **Concussion**, you should:

    1. **Immediately stop all physical activity**
    2. **Do not continue playing, training, or practicing**
    3. **Seek medical attention** from a doctor or certified athletic trainer

    > 🛑 Ignoring concussion symptoms can worsen the injury.

    This app provides **quick screening only** — it cannot:
    - Measure severity
    - Identify internal injuries
    - Provide treatment
    """
                    )

    # FAQ 3
    with st.expander("3. When should I go doctor to look at my head injury? "):
        st.markdown("""
    ### If the App Predicts a Concussion
    If your symptoms on the Symptom tracking page are not showing a good trend, and you already 
    stopped all physical activity, **seek medical attention** from a doctor

    > 🛑 Ignoring concussion symptoms can worsen the injury.

    This app provides **quick screening only** — it cannot:
    - Measure severity
    - Identify internal injuries
    - Provide treatment
    """
                    )

    # FAQ 4
    with st.expander("4. What symptoms mean I should call 911 right away?"):
        st.markdown("""
    ### 🚨 When to Call 911 Immediately
    Call **911 or emergency services right away** if you or someone else experiences **any** of the following after a head injury:
    
    - Loss of consciousness (even briefly)
    - Seizures or convulsions
    - Repeated vomiting or nausea
    - Severe or worsening headache
    - Slurred speech or difficulty speaking
    - Unequal pupil size or vision problems
    - Extreme drowsiness or inability to wake up
    - Confusion, agitation, or unusual behavior
    - Weakness, numbness, or loss of coordination
    - Clear fluid or blood coming from the nose or ears
    
    > 🚑 **Do not wait for symptoms to improve.**  
    > These signs may indicate a **serious brain injury** that requires immediate medical care.
    
    This app is designed for **screening and awareness only** and is **not equipped to handle emergencies**.
    """
                )

    # FAQ 5
    with st.expander("5. How often should I re-check my symptoms?"):
        st.markdown("""
    ### ⏱️ Re-Checking Your Symptoms
    After a head injury, it’s important to **monitor symptoms regularly**, even if they seem mild at first.
    
    You should re-check your symptoms:
    - **Immediately after the injury**
    - **Every few hours on the first day**
    - **Once per day during recovery**
    - **Anytime symptoms worsen or new symptoms appear**
    
    > 🧠 Concussion symptoms can change over time and may appear **hours or even days later**.
    
    Tracking symptoms consistently helps identify negative trends and ensures you seek medical care at the right time.
    
    This app supports **ongoing symptom tracking**, but it does **not replace professional medical evaluation**.
    """
                )

    # FAQ 6
    with st.expander("6. What should parents look out for after a head injury?"):
        st.markdown("""
    ### 👨‍👩‍👧 What Parents Should Watch For
    After a head injury, parents should closely monitor their child for **physical, cognitive, and behavioral changes**, especially within the first **24–72 hours**.
    
    Watch for signs such as:
    - Headache or pressure in the head
    - Dizziness or balance problems
    - Nausea or vomiting
    - Sensitivity to light or noise
    - Trouble concentrating or remembering
    - Unusual mood changes (irritability, sadness, anxiety)
    - Changes in sleep patterns
    - Slower reaction time or confusion
    
    > 👀 Some symptoms may not appear immediately and can develop hours or days after the injury.
    
    If symptoms **worsen**, **persist**, or interfere with daily activities, seek medical attention from a doctor or certified athletic trainer.
    
    This app helps with **early awareness and tracking**, but it cannot diagnose or treat concussions.
    """
                )
    

if __name__ == "__main__":
    main()
