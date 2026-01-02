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
        "title": "Concussion in Football",
        "description": "When it comes to concussion, don’t take chances",
        "image_url": "https://cdn.englandfootball.com/-/media/EnglandFootball/Hero/Desktop/learn/Brain-Health/20220812-concussion---hero.jpg?h=700&iar=0&w=1440&rev=3fa6bdd9610a4629ad063507804a1aa4&hash=25E5CEC7EB01A128C018492822EFE1DF",
        "link": "https://www.englandfootball.com/concussion"
    },
    {
        "title": "Football Concussions",
        "description": "Prevention, Diagnosis, and Recovery",
        "image_url": "https://www.cognitivefxusa.com/hubfs/football-concussion-prevention-and-recovery.jpg",
        "link": "https://www.cognitivefxusa.com/blog/football-concussion-prevention-and-recovery"
    },
    {
        "title": "Concussion Basics",
        "description": "For Everyone",
        "image_url": "https://www.charliewaterslaw.com/wp-content/uploads/2020/06/concussion.jpg",
        "link": "https://www.cdc.gov/heads-up/about/index.html"
    }
]

def main():
    # Page header
    st.title("🌐 Community ")

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
