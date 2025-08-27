import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import re
import math
import random
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import skew
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import chisquare

st.set_page_config(page_title='Portfolio',
                   page_icon='✨',
                   layout='wide')

#SIDEBAR
sidebar_style = """
    <style>
    [data-testid="stSidebar"] {
        background-color: #EEF7FF;  
    }
    </style>
"""
st.markdown(sidebar_style, unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu(
        menu_title='Julie Shcherbyna',
        menu_icon='lightning',
        options=['About Me', 'Blog', 'SQL', 'Python', 'Visualization', 'Recommender System', 'Diagrams'],
        icons=['person-hearts', 'quote', 'database', 'code-slash', 'bar-chart-line', 'controller', 'diagram-3'],
        default_index=0,)
    # 'Google Sheets' - 'table'

# ABOUT ME
if selected == 'About Me':
    st.markdown("<h1 style='text-align: center;'>Portfolio</h1>", unsafe_allow_html=True)
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("Julie Shcherbyna")
            st.subheader("Aspiring Data Analyst/Product Manager")
            st.write("👋🏻 Hey, I'm Julie! I'm a data science and analytics almost undergraduate based in Ukraine. With prior relevant experience in tech, writing, sales, and social media management, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation.")
            st.write("📚 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🎸 In addition, I'm into guitar playing, music, gym, running, video games, and books... A-a-and enjoy eating good food in my free time!")
            st.write("👩🏻‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            st.write("📄 [Resume ](https://drive.google.com/file/d/1x4FLEOxQfWFZnTcVMyO_2l1_Zzu_Ndn3/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(Image.open("images/me.jpg"))

    # --- CONTACT BUTTONS на боковій панелі ---
    with st.sidebar:
        EMAIL = "juliafest05@gmail.com"
        SUBJECT = "Hello%20from%20your%20portfolio"
        BODY = "Hi!%20I%20saw%20your%20portfolio%20and..."
        LI_LINK = "https://www.linkedin.com/in/julie-shcherbyna-15a47a297/"
        TG_USERNAME = "ejikjulie"

        mailto = f"mailto:{EMAIL}?subject={SUBJECT}&body={BODY}"
        TG_APP = f"tg://resolve?domain={TG_USERNAME}"
        TG_WEB = f"https://t.me/{TG_USERNAME}"

        button_html = f"""
        <style>
        .contact-wrap {{
        display:flex; flex-direction:column; gap:8px;
        align-items:center; justify-content:center; margin-top:30px;
        }}
        .contact-btn {{
        --radius: 9999px;
        --pad: 12px 20px;
        --shadow: 0 6px 18px rgba(0,0,0,.15);
        --grad: linear-gradient(135deg,#7c3aed, #06b6d4);
        display:inline-flex; align-items:center; justify-content:center;
        padding: var(--pad);
        border-radius: var(--radius);
        font-weight: 600; letter-spacing:.2px;
        text-decoration:none; user-select:none;
        background: var(--grad);
        color: white !important;
        box-shadow: var(--shadow);
        transition: transform .12s ease, box-shadow .2s ease, filter .2s ease;
        }}
        .contact-btn:hover {{
        transform: translateY(-1px);
        box-shadow: 0 10px 22px rgba(0,0,0,.2);
        filter: brightness(1.05);
        }}
        .contact-btn .dot {{
        width:8px; height:8px; margin-right:8px; border-radius:9999px; background:white; opacity:.9;
        animation: pulse 1.8s infinite ease-in-out;
        }}
        @keyframes pulse {{
        0%,100% {{ transform: scale(1); opacity: .9; }}
        50% {{ transform: scale(1.35); opacity: .6; }}
        }}
        .chip {{
        padding:8px 14px; border-radius:9999px; font-weight:600;
        text-decoration:none; border:1px solid rgba(0,0,0,.08);
        background: rgba(255,255,255,.6); color: inherit !important;
        transition: background .2s ease, transform .12s ease;
        }}
        .chip:hover {{ background: rgba(255,255,255,.9); transform: translateY(-1px); }}
        </style>

        <div class="contact-wrap">
        <a class="contact-btn" href="{mailto}">
            <span class="dot"></span>Contact me
        </a>
        <a class="chip" href="{TG_WEB}"
            onclick="(function(){{window.location.href='{TG_APP}'; setTimeout(function(){{window.open('{TG_WEB}','_blank');}},800);}})(); return false;">
            Telegram
        </a>
        <a class="chip" href="{LI_LINK}">LinkedIn</a>
        </div>
        """

        st.markdown(button_html, unsafe_allow_html=True)

# BLOG
if selected == 'Blog':
    st.markdown("<h1 style='text-align: center;'>Blog</h1>", unsafe_allow_html=True)
    selected_options = ["Overview", "Article & Essay List", 
                        "Data Science Tools in Gaming Industry",
                        "Development of Game Recommender System",
                        "Consumer Segmentation to Study the Underconsumption Core Trend",
                        "Machine Learning in Healthcare", 
                        "Застосування машинного навчання в рекомендаційній системі на прикладі Netflix",
                        "Блокчейн у медицині та фармацевтиці",
                        "Смарт-полички: як аналітика створює оптимальне розташування товарів",
                        "Parental Leave Regulations"
                        ]
    selected = st.selectbox("Choose a section you would like to read:", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
                    Welcome to my blog, a haven where words come alive and thoughts find their wings. 
                    
                    I must admit - from a young age, I have been enchanted by the magic of storytelling, 
                    a curious child with an insatiable appetite for reading and writing. 
                    Creativity has always been my constant companion, guiding me through a world brimming with endless possibilities. 
                    
                    Here, I joyfully share my articles, essays, and musings, hoping to spark a sense of wonder and reflection in you, dear reader. 
                    Join me on this journey, where every post is a piece of my heart and a glimpse into my ever-curious mind.
        """)
        st.write("For those looking forward to a good read, enjoy! 😊")
    
    elif selected == "Article & Essay List":
        st.subheader("Article & Essay List")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/1.jpeg"), use_column_width=True)
            with text_column:
                st.subheader("Data Science Tools in Gaming Industry")
                st.write("April 13, 2023 | [Presentation](https://drive.google.com/file/d/15-XtkL5AiL4qU6rNgWchmZ572WUByuze/view?usp=sharing)")
                st.write("The application of data science tools on real life examples")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/2.jpeg"), use_column_width=True)
            with text_column:
                st.subheader("Game Recommender System")
                st.write("April 18, 2024 | [Presentation](https://drive.google.com/file/d/1FRclX0J_qmyUhbJv_0orYQhJ42fxzaLW/view?usp=sharing)")
                st.write("Deatiled description of different filtering methods for recommender systems")  
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/8.jpg"), use_column_width=True)
            with text_column:
                st.subheader("Consumer Segmentation to Study the Underconsumption Core Trend")
                st.write("November 04, 2024 | [Article](https://docs.google.com/document/d/1v4Bao3t-z6RxaALdRvAvgJb3L-2cvZTd/edit?usp=sharing&ouid=107266174450085669622&rtpof=true&sd=true)")
                st.write("The Underconsumption core trend reflects a growing shift in consumer behavior toward doing more with less—prioritizing simplicity, " \
                "sustainability, and intentionality over excess. It highlights how individuals are increasingly rejecting overconsumption in favor of minimalism, " \
                "durability, and mindful purchasing decisions.")   
                st.markdown("**Think wiser, buy thrifted clothes**") 
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/3.webp"))
            with text_column:
                st.subheader("Machine Learning in Healthcare")
                st.write("April 16, 2024 | [Presentation](https://drive.google.com/file/d/1vEiC5A3XTRnR4t10oJxMhH0SWwbpSPTg/view)")
                st.markdown("Real life examples of machine learning in healthcare industry")       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/4.jpeg"))
            with text_column:
                st.subheader("Application of Machine Learning on the example of Netflix")
                st.write("March 11-17, 2024 | [Article](https://conference.ikto.net/pub/akit_2024_11-17march_1.pdf#page=364)")
                st.markdown("Application of Machine Learning on the example of Netflix, how it started, how it works")       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/5.jpeg"))
            with text_column:
                st.subheader("Blockcain in Healthcare")
                st.write("June 07, 2024 | [Article](https://www.lex-line.com.ua/?go=full_article&id=3877)")
                st.markdown("""Blockchain technology holds immense potential for revolutionizing the healthcare industry, particularly in the pharmaceutical field. 
                            In this article, several examples illustrate how blockchain can be utilized to enhance various aspects of pharmaceutical operations.""")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/6.jpg"))
            with text_column:
                st.subheader("Smart shelves: how analytics create optimal product placement")
                st.write("November 07-08, 2024 | [Article](http://www.wayscience.com/wp-content/uploads/2024/11/Conference-Proceedings-November-7-8-2024.pdf#page=298)")
                st.markdown("""Example of big companies. Analytics, AI, IoT, and big data help retailers optimize inventory, forecast demand, and enhance customer experience.""")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(Image.open("images/7.jpg"))
            with text_column:
                st.subheader("Parental Leave Regulations")
                st.write("January 13, 2025 | [Presentation](https://drive.google.com/file/d/15TADYJuA_eRI37Vho1NfcxmL4u7NoR9B/view?usp=sharing)")
                st.markdown("""The presentation compares national frameworks, highlighting how some states offer generous paid leave while others provide only 
                            limited unpaid options. This presentation was created with my colleagues from Erasmus program.""")
        
    elif selected == "Data Science Tools in Gaming Industry":
        st.subheader("Data Science Tools in Gaming Industry")
        st.write("April 13, 2023 | [Presentation](https://drive.google.com/file/d/15-XtkL5AiL4qU6rNgWchmZ572WUByuze/view?usp=sharing)")
        st.markdown("""
                    **~ Introduction**

                    Gaming has taken a massive leap from the days of Snake and Tetris. With technological advancements and innovations, gaming has become one 
                    of the most powerful industries in the world. As this market becomes more competitive, game creators are pushed to produce more innovative 
                    and generally better games, therefore data analysts are turning out to be really useful staff in gaming companies. The ultimate goal is to 
                    create an engaging experience for the player to spend more time playing the game. Analysts examine enormous surge of multi-source user data 
                    to gather and change into important insights. Thus, with these insights on hand, gaming companies can get a lot of benefits and produce more profits.

                    So, let’s consider on the particular examples most popular ways of how today’s gaming companies can augment their capabilities with data analytics, 
                    where analytics alongside data science is deployed for game development on.

                    **~ Three main ways**
                    
                    **1. Design**

                    The first one and the most exciting applications of data science in gaming is its use in the game development process. A game should be regarded 
                    as a kind mechanism which performance may be measured, and for example shows that a few levels may be excessively dull, some - excessively challenging, 
                    and some - essentially contain bugs that don't let users push ahead. 

                    Coincidentally, this is what happened to King Digital Entertainment. This well-known game designer once caught an unanticipated issue with its most popular 
                    game, Candy Crush Saga. Users were hugely abandoning level 65. «We wanted to give our players a real challenge, as we didn’t know how long it would take before 
                    we did another update, thus, it required a little bit more effort and eyesight to win. So, the original version had 52 moves and 65 double jellies, which was 
                    impossible to complete without the strategy created mathematically. Plus, it has contained some bugs, so after the particular move the level was breaking without 
                    the possibility to be fixed by users», the creator says. The data analysts classified this level as a ‘NP-hard problem’. 

                    **2. Tracking key performance indicators**

                    In their endeavour to precisely measure a game's overall performance, makers definitely face the need to respond to some fairly pressing inquiries. (examples) 
                    By using these questions companies can more likely comprehend the explanations behind a game's high points and low points, and construct increasingly powerful 
                    strategies. For instance, if a game attracts new users every day, the likelihood that some of them will upgrade to a paid account ascents exponentially or make 
                    a profit for company by purchasing beautiful skins on frankly unattractive characters. Also, degrading monthly active users’ rates may discuss approaching users 
                    wearing down, which is yet conceivable to fight off whenever recognised in time.

                    **3. Increasing monetisation**

                    Data analytics likewise enables gaming companies to perceive what precisely brings them more money and, consequently, modify their monetisation accordingly. 
                    To be sure, if a company uncovers those numerous users lean toward altering their armour or weapon, it's really sensible to offer them in-game armour and weapon 
                    upgrade.

                    Therefore, Zynga's example is here to demonstrate it. This gaming company's plan of action was allowed to play freely; however, it likewise offered a premium, 
                    ad-free account. The issue was that typically just **2%** of players really paid. Fortunately, the company discovered that in the first version of Farmville, users 
                    loved interacting with animals that were at first just decorations. A few users even began acquiring animals with real money, so in the accompanying version of 
                    the game, Zynga made animals a focal feature and even made 'uncommon species' to animate users additionally. Such a data driven methodology toward monetisation 
                    not just shows high return of investments for gaming companies; it likewise hits chord with users.

                    **~ Stocking Your Shop with Data Science**

                    Now to make the research more practical I would like to show on the instance how the data science tools work. Let’s talk about well-known company in gaming 
                    industry «Riot Games» and their masterpiece «League of Legends». Firstly, I’ll dive deep into one data science-fueled product - Your Shop. I’ll explain in details 
                    on how the offers get to players in every region.

                    **1. Recommendation systems**

                    Recommendation systems fall under one of two categories, which, in general, are defined by the kind of data they’re built on. For **collaborative filtering methods**, 
                    user-item interactions are the underlying source. In contrast, **content-based** recommender systems focus on tagged attributes of the users and items.

                    For the latter system to work, a specific skin should have multiple tags that describe various features of the content; this could be anything from “funny” to “cute” 
                    to “edgelord.”. In the same light, champions would have labels as well, from basic role categorizations (“ADC,” “Support,” “Mid”) to damage type. As players start to 
                    build up a catalog of content that they own and play, they would start to inherit the traits of those items to create a unique player profile. This profile, along with 
                    item features, could be used to rank content that a player would prefer. 

                    **2. Utility matrix**

                    Regardless of the tags, the fundamental data structure fed into these algorithms is the same - a utility matrix of users and individual scores for champions they've 
                    interacted with or purchased. Here's an example: The obvious question is: How are these player-item scores calculated?

                    There are many random components, for instance game modes in League where champions are chosen at random, other may force a choice amongst a subset of heroes and skins, 
                    so, in these cases, the player is likely not explicitly expressing a deep interest for a particular champion or skin. But the similar players have similar preferences 
                    and that a piece of content is in the same “neighborhood” as related items. Therefore, If two players, Tom and Jane, exhibit similar scores, then one can use Tom’s 
                    inferred ratings on the champion Zed to predict Jane’s unobserved rating on the same champion. Champions exist in neighborhoods, some closer than others, which inform what 
                    recommendations are made. One disadvantage is limited coverage due to sparsity; most players only interact with a small portion of champions and skins.

                    **3. Crucial metrics**

                    When launching any of the models, the company need high confidence in the recommendations it generates. In order to measure the effectiveness of a recommender, 
                    they evaluate a variety of metrics:

                    - **Coverage** encapsulates how many users will receive recommendations. If a player’s rating matrix is mostly empty because they are new to the game or haven’t 
                    played in quite some time, then their offers are usually replaced by a default set.

                    - **Novelty** evaluates the likelihood of a recommender system to provide offers that the player may not be aware of. This allows the player to discover 
                    additional information with their own likes and dislikes.

                    - **Serendipity** refers to recommendations that are unexpected. Imagine a player who likes to solo lane Riven. A recommendation to play Vayne might be seen 
                    as serendipitous, since it is somewhat unexpected by the player. This is because on the surface, Riven and Vayne don’t seem to share the same characteristics - 
                    but hidden underneath, their player bases are very similar.

                    - **Accuracy** has better short-term effects, as players are shown content they want now. The instinct here is that offering a skin on a champion that a player 
                    doesn’t currently play opens the door to a more diverse champion pool and a broader experience with *League*. 

                    **4. Loading of the shop**  

                    Ultimately, the whole process starts well before Your Shop opens for business and the icon shows up in players’ clients. The algorithms are run a few days in 
                    advance so the analysts can ensure that all of evaluation metrics are satisfactory and that they have produced a solid set of recommendations for players. 
                    The crew stores the resulting datasets in a bucket which is then uploaded to the "Your Shop" services, where the company has deployments across the globe. 
                    Once Your Shop is activated, the service loads in the suggested recommendations as players turn over their cards. During this process, the eye is kept on the 
                    telemetry reflecting which recommendations were successful, pinpoint possible errors and measure the overall success of the system so the future iterations can 
                    be made with an even better experience.   

                    **~ Personality Quizzes**

                    Also, I would like to mention the iconic method: a **Personality Quiz**. Finding products most similar to the user based on their responses to a questionnaire. 
                    So how does this all apply to recommending a *League of Legends Champion* (playable character)?  

                    **1. Create a multi-dimensional space with features that help describe each Champion in the game (there’s currently 152 Champions to choose from).**

                    All of us are familiar with the 3-dimensional model, where each axis has different metrics, but what will happen then with n-dimensional one? Let’s be simple, 
                    we build a script that fetches games from the Riot API, from this extract the Champion played and in which lane, grab some features that will help describe the 
                    Champion, like how many kills they got, how much damage they did to objectives, how much damage they’ve blocked, etc… Then convert the dataframe into a matrix, 
                    where each row represents a Champion with 21 various statistics about their in-game performance on average across many samples.

                    **2. Fit the NN algorithm to this space.**

                    **Nearest Neighbours (NN)** is exactly what it says on the tin. For any point in a space, there are N-number of nearest neighbours. Literally, you just pick 
                    a point and find the N-closest points to that one. “N” can be any number, however the standard Python implementation defaults to 5. Hopefully, the visualisation 
                    below makes this crystal clear. Blue is the example point; Reds are the 5 nearest neighbours:

                    In the 2D space we can just press a ruler to our screen, however what happens in the unimaginable 4-dimensional space and beyond? We use formula Euclidean distance. 
                    On the slide 13 you can see the calculations.

                    **3. Create a survey that tries to place the person in that space.**

                    To do this, for each statistic, there needs to be a corresponding question and a way of translating their answer into a usable number. So, there is used a 
                    *“How much do you agree with the following statement”* style of questions. The reason it works well is because people respond on a scale. 
                    The first statistic in the dataset is: percentage of a Champion kills which were done without assistance. Artfully is translated into the following 
                    statement: *“I am a lone wolf”* Why? Champions with a high % are people who get most of their kills when acting alone. Those with a low % rely on their team mates 
                    to help secure kills. Hence, lone wolf. This is the art of science part.Here you can see the following logic. Then continue creating questions, each time 
                    converting their answer to an actual value. A full list of the questions and their related statistics can be found on the slide 14.

                    Now, when someone completes the **Personality Quiz**, convert each answer to a statistic, normalise the values and boom — we have converted their personality 
                    to a position in our 21-dimensional space and now have the exact results!

                    **~ Conclusion**
                    
                    The gaming industry has been growing exponentially. The number of active users tends to increase every minute and so does the overall income of the companies’ 
                    developing games. Data science has entered various industries and improved the principles of their functioning forever. It has brought various businesses to a 
                    qualitatively new level of their development. The industry of gaming is no exception here. Moreover, data science techniques and methodologies have become integral 
                    parts of games development, design, operation, and many other stages of their functioning. 
                    """)
    
    elif selected == "Development of Game Recommender System":
        st.subheader("DEVELOPMENT OF GAME RECOMMENDER SYSTEM")
        st.write("April 18, 2024 | [Presentation](https://drive.google.com/file/d/1FRclX0J_qmyUhbJv_0orYQhJ42fxzaLW/view?usp=sharing)")
        st.markdown("""
                    As the gaming industry continues to experience rapid growth, driven by an estimated **2.96 billion** games available worldwide, the sheer abundance of options 
                    presents a challenge for gamers in selecting which game to play. This expansion, from the inception of the first computer game, Spacewar! in **1962** at MIT 
                    (Stephen Russell a.o.) [1], to today's landscape of over **50,000** titles spanning various genres, underscores the need for effective navigation and discovery 
                    mechanisms. 

                    While early games like *Spacewar!* laid the groundwork, advancements in technology have ushered in a new era of more advanced and interactive gaming experiences. 
                    In response to this, global giants would benefit if started creating powerful content-based game recommendation systems to fit the user's interests amidst the 
                    overwhelming array of choices. 

                    A recommender system is a type of information filtering system that predicts or suggests items, such as products, services, or content, that a user might be 
                    interested in. These systems are commonly used in e-commerce, entertainment, social media, and other online platforms to personalize and improve user experiences 
                    by providing relevant recommendations based on user data, such as past behavior, preferences, and demographics. [2]

                    Two common methods used in creating recommendation systems are Content-based Filtering and Collaborative Filtering. Content-based Filtering involves selecting 
                    items by evaluating the connection between item characteristics and user preferences, while Collaborative Filtering selects items based on the association between 
                    users with similar preferences [3]. Due to the capability of suggesting items that have not yet been rated by any user, future recommendation system will be based 
                    on Content-Based Filtering.

                    The main idea is simple: to create a user model, from collected data, and further use it to rate the dataset based on its compatibility to user.

                    The first stage of this research is to collect data of any game that is available on STEAM using dataset **“50 000 Steam Store Game”**, published by Nik Davis in **2019** 
                    [4]. The next step is to check data’s validity and utility to make sure that all data are useful and filled without any defected value through EDA method. 
                    Done the Feature Selection later, it is apparent that the most common and best parameters that could be used to build a suitable recommendation system are developer, 
                    categories, and genres.

                    The user's input of any STEAM game and given rating of that game is being converted into the user profile matrix using Content-based Filtering.
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,2,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/grs.1.png"), width=500)
                st.markdown("<p style='text-align: center;'><em>User Input and Rating</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    The following matrix is based on content which includes developer, genre, and categories since these three features are the most likely used tags for users to 
                    determine what game to their liking. On this basis, three broken down matrices will be created where condition of each attribute in each feature will be 
                    determined with One-Hot Encoding where “0” assigned to attributes that is not belong to the game and “1” assigned to attributes that is belong to the game. 
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1, 7, 1))
            with col1:
                st.empty()
            with col2:
                col2_1, col2_2 = st.columns(2)
                with col2_1:
                    st.image(Image.open("images/grs.2.png"), caption='Matrices Based on Categories', width=450)
                with col2_2:
                    st.image(Image.open("images/grs.3.png"), caption='Matrices Based on Genres', width=450)
            with col3:
                st.empty()
        with st.container():
            col1, col2, col3 = st.columns((1, 2, 1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/grs.4.png"), caption='Matrices Based on Developers', width=500)
            with col3:
                st.empty() 
        st.markdown("""
                    At the next stage, a weighted matrix is created, where the value in each column for the selected games is equal to the product of the One-Hot Encoding variables and 
                    the posted user rating, and the line Total is a sum of all values. 

                    Then, the total values in each table were normalized to ensure a proportional distribution of preferences. This normalization process facilitated fair comparison and 
                    interpretation of user preferences across different categories, genres, and developers.

                    The User Profile Matrix is the base to categorize which game to recommend to user. The step that needed is to multiply the User-Profile value on each game score. 
                    The result of the multiplication will become the level of similarity of the game to the user's preferences. The higher the result, the higher the chance that user would 
                    like to play the games. 

                    From the initial dataset, 5 users were picked randomly to test the method by asking them to input game that they have played or interested before and rate them based on their 
                    personal opinion. Using this method, the recommendation for 5 users have accuracy which can be calculated using formula (1).
                    """)
        st.latex(r'\text{Accuracy} = \frac{\text{Chosen game result}}{\text{Total result}}')
        st.markdown("""
                    The overall performance accuracy can be calculated, utilizing equation (2). Hence, the proposed method achieves an overall accuracy of 82%. In other words, out of every 
                    10 recommended games, 8 are deemed favorable for users to play. Based on the overall accuracy achieved by the proposed method, it can be concluded that the proposed mechanism 
                    successfully utilizes Content-based Filtering to give a game recommendation with user input as its base.
                    """)
        st.latex(r'''
                \text{Overall Accuracy} = \frac{\sum \text{(accuracy of all users)}}{\sum \text{(users)}}
                ''')

        st.markdown("""
                    From this project, it can be concluded that Content-based Filtering is suitable to be used on database that contain the attribute that used as comparing factor. For future work, 
                    this method can be improved by enhancing the database by inputting the demography data of user that chosen the same item and implementing Collaborative Filtering and Content-based 
                    Filtering at the same time, this way the result given can be more accurate and more personalized.

                    **References**

                    1.	A history of the computer game. Jesper Juul. URL: https://www.jesperjuul.net/thesis/2-historyofthecomputergame.html (April 1, 2024)
                    2.	J. Lee, M. Sun, and G. Lebanon, “A Comparative Study of Collaborative Filtering Algorithms,” 2012, [Online]. Available: http://arxiv.org/abs/1205.3193 (April 1, 2024)
                    3.	Van Meteren R., Van Someren M. Using Content-Based Filtering for Recommendation. URL: https://users.ics.forth.gr/~potamias/mlnia/paper_6.pdf (April 1, 2024)
                    4.	Davis, N. (2019) Steam store games (clean dataset), Kaggle. Available at: https://www.kaggle.com/datasets/nikdavis/steam-store-games (April 2, 2024)
                    """)

    elif selected == "Consumer Segmentation to Study the Underconsumption Core Trend":
        st.subheader("Consumer Segmentation to Study the Underconsumption Core Trend")
        st.write("Nov 04, 2024 | [Article](https://docs.google.com/document/d/1v4Bao3t-z6RxaALdRvAvgJb3L-2cvZTd/edit?usp=sharing&ouid=107266174450085669622&rtpof=true&sd=true)")
        with open("files/Consumer Segmentation to Study the Underconsumption Core Trend.docx", "rb") as f:
            st.download_button(
                label="📄 Download my coursework",
                data=f,
                file_name="Consumer Segmentation to Study the Underconsumption Core Trend.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    elif selected == "Machine Learning in Healthcare":
        st.subheader("Machine Learning in Healthcare")
        st.write("May 16, 2024 | [Presentation](https://drive.google.com/file/d/1vEiC5A3XTRnR4t10oJxMhH0SWwbpSPTg/view?usp=sharing)")
        st.markdown("""
                    The Fourth Industrial Revolution and the processes associated with this social phenomenon affect virtually all areas, and it can be argued that 
                    there is no chance of not being involved in any field of human activity. The healthcare industry is also covered by automation processes in various areas - 
                    from diagnostics and patient records to the development of new drugs and surgical interventions using software applications, hardware and software robotic artificial intelligence systems [1]. 

                    Traditionally, the pharmaceutical industry has been rather slow to adopt new technologies due to strict regulations and complex supply chains. However, the coronavirus pandemic and full-scale
                    invasion have had a significant impact on the pharmaceutical industry, forcing it to quickly adapt and respond to the challenges posed by the spread of new "viruses."

                    One of the most prominent applications of Machine Learning in healthcare is medical imaging analysis. ML algorithms, particularly deep learning models, have shown remarkable performance 
                    in tasks such as image classification, segmentation, and disease detection. For example, convolutional neural networks **(CNNs)** have been used to automate the interpretation of radiological 
                    images, leading to faster and more accurate diagnosis of conditions such as cancer, neurological disorders, and cardiovascular diseases.

                    The next important issue is electronic health records **(EHRs)** which contain a wealth of information about patients' medical history, treatments, and outcomes. ML algorithms can 
                    analyse **EHR** data to identify disease risk factors, predict patient trajectories, and optimize treatment plans. Natural language processing **(NLP)** techniques enable the extraction of
                    valuable insights from unstructured clinical notes, facilitating clinical decision-making and improving healthcare delivery.

                    Machine Learning algorithms play a crucial role in accelerating drug discovery and development processes. By analysing molecular structures, genomic data, and clinical trial results, 
                    ML models can identify potential drug candidates, predict drug efficacy, and optimize treatment regimens. Today, a successful drug or vaccine requires several billion dollars in funding 
                    and takes several years to develop. By detecting patterns in data, artificial intelligence models can narrow down the resources needed to develop and find new drugs. In 2021, the biotech 
                    company Insilico Medicine announced the first AI-discovered drug to treat idiopathic pulmonary fibrosis [2]. Thanks to AI Insilico saved **90%** of the planned budget.

                    Personalized medicine approaches leverage ML algorithms to tailor treatments to individual patients based on their genetic makeup, medical history, and other personalized factors, 
                    leading to improved therapeutic outcomes, sleep, eating habits, nutrition supplement and reduced adverse effects. ML can also use big data and individualized data to deliver 
                    **"precision longevity"** by preparing personalized plans for nutrition, supplements, exercise, sleep, medications, and therapies. Rejuvenation biotechnology will no longer be 
                    limited to the rich, but will become available to everyone.

                    Internet of Things **(IoT)-enabled** infrastructure, such as smart hospitals and smart homes, integrates sensors, actuators, and ML-powered analytics to create intelligent 
                    environments that enhance patient care and operational efficiency. The IoT as part of ML is used to create smart rooms with temperature sensors, smart toilets, beds, and other 
                    types of invisible gadgets that will regularly analyse vital signs and other patient data to detect possible health crises. Aggregated data from wearable devices will allow us to 
                    accurately determine the status and course of serious illnesses, whether cardiovascular, fever, apnoea, pulmonary disease, asphyxiation, out-of-control falls, or fall injuries. 
                    Sudden changes in condition may trigger patient alerts, notification of next of kin, or an ambulance call.

                    Even complex surgeries that rely on sophisticated judgment and dexterous movements will become increasingly automated over time. Robotic surgeries grew from **1.8%** of all 
                    surgeries in **2012** to **15.1%** in **2018** [3]. Robots can already perform semi-autonomous surgical tasks such as colonoscopy, suturing, intestinal anastomosis, 
                    and dental implants under the supervision of a doctor. As ML learns from big data, robotic surgeries can move from a human surgeon controlling the robot to a surgeon 
                    supervising the robot and delegating some tasks. This could eventually lead to fully autonomous surgical robots. Finally, the emergence of medical nanorobots will offer numerous 
                    capabilities that surpass human surgeons. These miniature (1 to 10 nanometers) bots can repair damaged cells, fight cancer, correct genetic defects, and replace DNA molecules 
                    to eradicate disease.

                    A **2019** study [4] shows that ML healthcare markets will grow by **41.7%** annually to **$13 billion** by **2025** in areas such as hospital workflow, wearables, medical imaging 
                    and diagnostics, therapy planning, virtual assistants, and, most importantly, drug development. 

                    ML healthcare should not be viewed as just a market. In fact, it is a wave of transformations that will change the entire industry. ML-powered healthcare provides a perspective 
                    for human society to have a healthier and longer life. Global ML experts assessing the state and pace of ML development conclude that in 20 years, ML will be able to measure and 
                    improve human health, as well as help us get more happy moments in the life cycle of each person. At the same time, the further implementation of ML in the medical field has a 
                    number of urgent problems, including moral discomfort with machines making decisions affecting human health and life; legal and regulatory processes for doctors and surgeons in 
                    cases of death; investigation into responsibility in ML-related accidents or fatalities; potential parties responsible: hardware manufacturer, ML algorithm supplier, software company, 
                    supervising physician.

                    These problems are not short-term and will need to be solved in the long term. Analysis of research and practice shows that competition in the healthcare market, 
                    financial and other economic levers, new discoveries, and the accumulation of large amounts of medical data give optimistic estimates of the solution to these problems and the 
                    continued development of ML in healthcare.

                    References
                    
                    1. Ben Dickson. AI could help reduce the administrative costs of health car. VentureBeat. URL: https://venturebeat.com/ai/ai-could-help-reduce-the-administrative-costs-of-health-care/ (2024, March 27)
                    2. Conor Hale. Insilico Medicine begins first human trial of its AI-designed drug for pulmonary fibrosis. Nov 30, 2021. Fierce Biotech. URL: https://www.fiercebiotech.com/medtech/insilico-medicine-begins-first-human-trial-its-ai-designed-drug-for-pulmonary-fibrosis (2024, March 27)
                    3. Kyle H. Sheetz. Trends in the Adoption of Robotic Surgery for Common Surgical Procedures. Jan 10, 2020. JAMA Network Open. URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6991252/#:~:text=From%20January%202012%20through%20June,laparoscopic%20and%20open%20surgery%20declined (2024, March 28)
                    4. Millicent Abadicio. AI in the Hospital Setting – Challenges and Trends. Sep 8, 2020. Emerj. URL: https://emerj.com/ai-sector-overviews/ai-in-the-hospital-setting/ (2024, March 28)
                    """)

    elif selected == "Застосування машинного навчання в рекомендаційній системі на прикладі Netflix":
        st.subheader("Застосування машинного навчання в рекомендаційній системі на прикладі Netflix")
        st.write("March 11-17, 2024 | [Article](https://conference.ikto.net/pub/akit_2024_11-17march_1.pdf#page=364)")
        st.markdown("""
                    Популярність стрімінгових платформ різко зросла за останні кілька років, що в основному пояснюється глобальною пандемією COVID-19, яка спричинила повсюдні 
                    локдауни та збільшення використання цифрових розваг як для дозвілля, так і для віддаленої роботи. Попит на різноманітний контент за запитом стрімко зріс, 
                    зробивши послуги надання потокового відео основним джерелом розваг, відпочинку та інформації, тим самим прискоривши вже зростаючу тенденцію споживання цифрового контенту. 

                    Наразі дослідження методів оцінювання та підвищення ефективності потокових платформ є надзвичайно актуальним, оскільки ці платформи стали невід’ємною частиною того, 
                    як люди споживають контент та взаємодіють із ним. Зміни вподобань і очікувань користувачів вимагають постійного аналізу та вдосконалення, щоб забезпечити безперебійне 
                    постачання, персоналізований досвід і технологічну адаптивність. Саме тому в даній статті будуть проаналізовані складні алгоритмічні системи та їх застосування на прикладі 
                    системи рекомендації компанії **«Netflix»**. 

                    Крихітний стартап, що починався два десятиліття тому, та просив Blockbuster придбати його всього за **$50 млн** перетворився на найбільшу у світі потокову платформу. 
                    Але як Netflix це вдалося? У перші дні свого існування бізнес-модель Netflix базувалася лише на прокаті фільмів на DVD, пропонуючи необмежену кількість цих самих 
                    DVD без дат повернення, комісій за прострочення або місячних обмежень на оренду. Компанія використовувала просту систему рекомендацій на основі 5-зіркового рейтингу. 
                    Людям було запропоновано оцінювати фільми, які вони брали напрокат після їх повернення. На той час оцінки були єдиним точним способом дізнатися, що хтось дійсно дивився DVD. 
                    5-зіркова система рекомендацій допомогла Netflix зібрати важливі дані. Що вищий рейтинг, то краща якість DVD-дисків, і тим більша ймовірність, що він сподобається іншим клієнтам. 

                    Коли Інтернет почав розвиватися, Рід Гастінгс, генеральний директор Netflix, визначив унікальну перевагу Netflix у поєднанні вмілого оповідання і розповсюджуваної потужності 
                    Інтернету, щоб забезпечити найкращі враження від перегляду для своїх користувачів. У **2007** році Netflix представив свою першу послугу потокового передавання Watch Now, 
                    а вже через два роки започаткував Netflix Prize з метою покращити користувацький досвід на **≥ 10%**. Команда, яка отримала винагороду у розмірі **$1 млн**, розробила складну 
                    систему рекомендацій, що будувалася на фільтрації та складалася з понад 100 різних наборів прогнозів. 

                    Спільна фільтрація — це метод машинного навчання, який використовує дані минулої поведінки користувачів для аналізу зв’язків між «користувачами та взаємозалежності 
                    між продуктами для виявлення нових асоціацій між користувачами та елементами». Існує два варіанти спільної фільтрації: на основі користувачів **(UBCF)** і на основі елементів **(IBCF)**. 
                    **UBCF** інтуїтивно припускає, що люди, які мали подібні думки в минулому, швидше за все, будуть поділяти ті ж думки знову в майбутньому, тоді як **IBCF** припускає, що люди завжди хочуть мати схожі речі. 
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/netflix.1.webp"))
                st.markdown("<p style='text-align: center;'><em>UBCF vs IBCF</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    Як показано на малюнку вище, в **UBCF** Тім і Джон обоє люблять шоколад і морозиво, як показано стрілками, тому вони класифікуються як такі, що мають подібні думки. 
                    Тім також любить морозиво та пончики, отже, можна передбачити, що Джон буде мати високу ймовірність насолодитися морозивом та пончиками, оскільки вони мають схожі інтереси. 
                    Для порівняння, в IBCF морозиво в ріжках і порційне морозиво є двома видами морозива. Якщо Джон любить морозиво в ріжку, він, швидше за все, полюбить й порційне морозиво.

                    Для реалізації методів колаборативного та заснованого на змісті рекомендаційного підходів **(UBCF та IBCF відповідно)** користувачі та елементи представлені у вигляді векторів
                    на основі шаблонів оцінки, до яких застосовуються методи матричної факторизації. Для елемента *i*, *qi* вимірює, наскільки сильно (позитивно) чи слабко (негативно) елемент 
                    володіє переліком факторів, таких як розвиток характеру чи романтичний кінець. Для користувача *u*, *Pu* вимірює ступінь зацікавленості користувача елементами на основі тих же 
                    факторів. Обчислюючи скалярний добуток двох векторів, можна отримати число *Rui*, яке оцінює інтерес користувача до характеристик елемента.
                    """)
        st.latex(r"""
                R_{ui} = q_i * P_u
                 """)
        st.markdown("""
                    Основна перевага матричної факторизації полягає в її гнучкості для роботи з великою кількістю даних. Для Netflix аспекти даних щодо елементів можуть включати жанри, 
                    акторський склад, тривалість стрічки тощо. Інтерес користувачів можна відстежувати за допомогою таких показників, як кількість переглядів, кількість безперервних переглядів 
                    та час доби, коли користувач зазвичай перебуває на Netflix. Тож, ці методи дозволяють налаштувати систему рекомендацій для персоналізації вмісту для окремих користувачів, 
                    використовуючи характеристики вмісту та звички перегляду.

                    Системи рекомендацій спрощують людям процес вибору. Британський телепродюсер і професор Джон Елліс у своїй книзі «Seeing Things: Television in the Age of Uncertainty» 
                    пише: «Вибирати означає усвідомлювати альтернативні можливості, можливості, які втрачаються». Саме цей страх втрати швидко охоплює людей, змушуючи їх сумніватися. Netflix, 
                    аналізуючи поведінку своїх користувачів, зрозумів, що багато людей гублять інтерес до вибору контенту протягом 60-90 секунд, переглянувши від **10 до 20** заголовків. 
                    Тож їхньою метою стало запропонувати цікавий контент користувачеві менше, ніж за **1,5 хвилини**, щоб зберегти увагу та утримати юзера на платформі.

                    Незалежно від того, на якому пристрої ви дивитеся Netflix, ви завжди першим потрапляєте на домашню сторінку. Згідно з дослідницькою статтею, опублікованою Netflix на **ACM**, 
                    80% годин потокової трансляції є результатом системи рекомендацій на домашній сторінці, а решта **20%** – результатом пошуку. Для легкої та інтуїтивно зрозумілої навігації 
                    Netflix використовує макет сітки. Це дозволяє користувачам глибше зануритися в певний жанр або пропустити рядки, які їх не цікавлять.
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,2,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/netflix.2.png"))
                st.markdown("<p style='text-align: center;'><em>Netflix Main Screen</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    Для Netflix дуже важливо розміщувати контент, який найбільше цікавить користувачів, у верхньому лівому куті. Для створення сітки використовується кілька алгоритмів. 
                    По-перше, це – **Personalized Video Ranker (PVR)**, який створює унікальний порядок каталогу для кожного облікового запису на основі попередніх звичок перегляду учасника. 
                    Згодом, отриманий порядок у каталозі використовується для створення рядків на основі жанру та визначення порядку впорядкування вмісту в одному рядку. 
                    Таким чином, користувачі можуть мати абсолютно різний вміст у рядках, які мають однакову назву жанру, як-от жахи.

                    Після того, як **PVR** звужує каталог, Top N video ranker, алгоритм, що використовується для створення рекомендацій для заголовків, які відображаються в рядку **Top Picks** 
                    на домашній сторінці, визначає найбільш релевантні відео для кожного користувача та перераховує їх у новому рядку. Інші рядки, як-от «Популярні зараз», 
                    «Продовжити перегляд» і «Оскільки ви дивилися» **(BYW)**, також створюються за допомогою алгоритмів. Зокрема, **BYW** генерується алгоритмом подібності відео до відео, 
                    типом спільної фільтрації на основі елементів **(IBCF)**. Рейтинговий список відео обчислюється для кожного відео в каталозі, а потім до нього додається підмножина списку 
                    з найбільшою схожістю на основі уподобань користувача. Алгоритм генерації сторінок відображає найрелевантніші рядки для кожного користувача, уникаючи дублювання вмісту 
                    та зберігаючи різноманітність сторінки. 

                    Наступним кроком є створення конкретних метаданих для кожного телешоу та фільму, таких як обкладинка, короткий опис, акторський склад і піджанри. За даними нейробіологів 
                    з Массачусетського технологічного інституту, людському мозку для обробки зображення потрібно лише **13 мілісекунд**. Оскільки обкладинка займає найбільше місця на екрані, 
                    користувач не може його проігнорувати. Для **Stranger Things**, найпопулярнішого шоу на Netflix у **2019** році, обкладинки, показані на малюнку нижче, були створені спеціально 
                    для різних користувачів із різними кадрами, кольорами шрифтів, розмірами та розташуванням.
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,2,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/netflix.3.png"), width=500)
                st.markdown("<p style='text-align: center;'><em>Stranger Things' Example</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    Жодна інша потокова платформа наразі не налаштовує обкладинки так, як це робить Netflix. Найсильнішою перевагою Netflix перед конкурентами є персоналізація. 
                    У блозі Netflix: «у нас є не один продукт, а понад **100 мільйонів** різних продуктів, по одному для кожного з наших учасників із персональними рекомендаціями та 
                    персоналізованими візуальними ефектами.»

                    Враховуючи величезну різноманітність у смаках і вподобаннях, чи не було б краще, якби Netflix міг знайти найкращий твір мистецтва для кожного з користувачів, 
                    щоб підкреслити аспекти назви, які мають для них особливе значення?

                    Розглянемо наступні приклади, коли різні учасники мають різну історію перегляду. Ліворуч три заголовки, які учасник переглядав у минулому. Праворуч від стрілки 
                    показано обкладинку, яку учасник отримав би для певного фільму відштовхуючись від рекомендації.

                    Залежно від того, наскільки користувач віддає перевагу різним жанрам і темам, легко персоналізувати зображення фільму «Добрий Вілл Хантінг». Глядач, який переглядав 
                    багато романтичних фільмів, може зацікавитися «Добрим Віллом Хантінгом», якщо на обкладинці буде зображено закоханих Мета Деймона та Міні Драйвер, тоді як користувач, 
                    який дивився багато комедій, зацікавиться фільмом, якщо буде використано зображення Робіна Вільямса, відомого коміка.
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,2,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/netflix.4.png"), width=600)
                st.markdown("<p style='text-align: center;'><em>Movies Recommendations</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    За іншим сценарієм, різні уподобання членів акторського складу можуть вплинути на персоналізацію ілюстрації до фільму «Кримінальне чтиво». Користувач, 
                    який дивиться багато фільмів за участю Уми Турман, швидше за все, позитивно відреагує на обкладинку для «Кримінального Чтива», яка містить Уму. 
                    Тим часом шанувальник Джона Траволти може бути більш зацікавленим у перегляді фільму, якщо на картині зображений Джон.
                    """)
        with st.container():
            col1, col2, col3 = st.columns((1,2,1))
            with col1:
                st.empty()
            with col2:
                st.image(Image.open("images/netflix.5.png"), width=600)
                st.markdown("<p style='text-align: center;'><em>Movies Recommendations</em></p>", unsafe_allow_html=True)
            with col3:
                st.empty()
        st.markdown("""
                    **Літературні джерела:**
                    
                    1.	Gomez-Uribe C. A., Hunt N. The Netflix Recommender System: Algorithms, Business Value, and Innovation. 2015. [Електронне Джерело] URL: https://dl.acm.org/doi/10.1145/2843948 
                    2.	How Netflix Became a $100 Billion Company in 20 Years. Product Habits. [Електронне Джерело] URL: https://producthabits.com/how-netflix-became-a-100-billion-company-in-20-years/
                    3.	Koren Y., Bell R., Volinsky C. Matrix Factorization Techniques for Recommender Systems. [Електронне Джерело]. 2009. Vol. 42, no. 8. P. 30–37. URL: https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf
                    4.	Item-Based Collaborative Filtering in Python – Predictive Hacks. Predictive Hacks. [Електронне Джерело] URL: https://predictivehacks.com/item-based-collaborative-filtering-in-python/ 
                    5.	Blog N. T. Learning a Personalized Homepage. Medium. [Електронне Джерело] URL: https://predictivehacks.com/item-based-collaborative-filtering-in-python/#google_vignette 
                    6.	Chandrashekar A. Amat F. Basilico J. Jebera T. Artwork Personalization at Netflix. Medium. [Електронне Джерело] URL: https://netflixtechblog.com/artwork-personalization-c589f074ad76
                    """)

    elif selected == "Блокчейн у медицині та фармацевтиці":
        st.subheader("Блокчейн у медицині та фармацевтиці")
        st.write("June 07, 2024 | [Article](https://www.lex-line.com.ua/?go=full_article&id=3877)")
        st.markdown("""
                    Технологія блокчейн привертає все більше уваги завдяки здатності забезпечувати прозоре та безпечне зберігання і передачу даних. 
                    Хоча блокчейн відомий своєю роллю у фінансових операціях і криптовалютах, його потенціал виходить за межі цих сфер. 
                    Медична та фармацевтична галузі стикаються з підробкою ліків, складністю ланцюгів поставок, потребою у безпеці та конфіденційності 
                    медичних даних, а також необхідністю підвищення ефективності та прозорості. Блокчейн може стати ключовим інструментом для вирішення цих проблем.
                    
                    Блокчейн (від англ. “block” –”блок”, “chain” – “ланцюг”) — це розподілена база даних, яка підтримується численними комп'ютерами, розміщеними 
                    по всьому світу. Дані в цій базі організовані в блоки, які розташовані в хронологічному порядку і захищені криптографією, де кожен новий блок містить 
                    інформацію про кількість транзакцій та зашифровані за певним алгоритмом дані попереднього блоку [1]. Це забезпечує високий рівень безпеки та незмінність даних.
                    
                    Блокчейн є цифровим реєстром, який надійно записує транзакції між сторонами, захищаючи їх від несанкціонованого доступу. Дані записуються глобальною розподіленою
                    мережею спеціальних комп'ютерів (нод). При ініціюванні транзакції, наприклад, переказу криптовалюти, вона транслюється в мережу, де ноди проводять аутентифікацію, 
                    перевіряючи цифрові підписи та інші дані. Після перевірки транзакція додається до блоку, який поєднується з іншими в блокчейн. Завдяки безпеці, прозорості та 
                    незмінності даних, блокчейн підвищує ефективність і надійність у медицині та фармацевтиці. 
                    
                    Використання блокчейн-технологій у медицині значно зросло протягом останніх років. У 2017 році відсоток використання блокчейну в цій галузі становив лише 6%. 
                    Проте вже в 2018 році цей показник зріс до 18%, а у 2019 році досягнув 29%. Найбільше зростання відбулося у 2020 році, коли відсоток використання блокчейну в медицині досягнув 46%.[2]
                    
                    **Управління даними пацієнтів** є одним з найефективніших застосувань блокчейну в охороні здоров'я. Шифрування блокчейну забезпечує безпечне зберігання медичних записів, 
                    номерів соціального страхування та банківських реквізитів. Розподілений реєстр гарантує безпечну передачу даних, запобігаючи несанкціонованому доступу. Блокчейн 
                    забезпечує незмінність даних, тобто інформацію не можна змінити без згоди мережі, що гарантує точність і достовірність даних пацієнтів з часом.
                    
                    **Зберігання записів клінічних випробувань.** Дослідники часто мають записувати велику кількість даних під час проведення клінічних випробувань нових ліків або дослідження 
                    нових захворювань. Функція незмінності блокчейну забезпечує цілісність даних випробувань, запобігаючи їх підробці або маніпуляціям, допомагає фіксувати кожну зміну 
                    в клінічних випробуваннях і відстежувати деталі внесених змін. Крім того, механізм консенсусу блокчейну забезпечує, що будь-які зміни у записах клінічних випробувань 
                    потребують згоди кількох сторін, підтверджуючи кожну модифікацію та позначаючи її як достовірну, що сприяє довірі та надійності. 
                    
                    **Управління ланцюгом постачання фармацевтичної продукції.** Фальшиві ліки є значною проблемою в системі охорони здоров'я, яка не тільки поширена, але й може бути небезпечною. 
                    Підроблені ліки можуть містити токсичні інгредієнти, що негативно впливають на здоров'я пацієнтів. Іноді нелегальні ліки повторно упаковуються після закінчення терміну придатності 
                    за допомогою підроблених етикеток. За даними Національної ради з попередження злочинності, понад 10% ліків у глобальному ланцюгу постачання є підробленими. 
                    У багатьох країнах фальшиві ліки становлять до 70% фармацевтичної продукції в ланцюгу постачання. 
                    
                    Впровадження блокчейну дасть змогу відстежувати шлях ліків від заводу до аптеки, включно з інтеграцією з виробниками та гуртовими продажами, що полегшить виявлення та 
                    вилучення підроблених препаратів. Крім того, використання блокчейну може допомогти в моніторингу життєвого циклу ліків, прогнозуванні попиту та відповідно до цього оптимізації пропозицій.
                    
                    **Обмін медичними даними.** Пацієнтам часто потрібно консультація кількох спеціалістів та доступ до повної історії свого здоров'я. Однак зберігання та обмін медичними даними 
                    між лікарями є значною проблемою. Блокчейн допомагає у цьому, усуваючи проблеми з несумісністю форматів, конфіденційністю та безпекою. Децентралізована архітектура дозволяє 
                    багатьом учасникам мати доступ до одного набору даних, що полегшує спільну роботу лікарів та надає пацієнтам доступ до повної історії їх здоров'я.
                    
                    **Відстеження кваліфікацій медичних працівників.** Коли пацієнтам потрібно відвідати лікаря, вони хочуть перевірити його кваліфікації перед записом. 
                    Блокчейн забезпечує децентралізований та незмінний реєстр кваліфікацій лікарів, унеможливлюючи несанкціоновані зміни. Це допомагає пацієнтам перевіряти кваліфікації 
                    перед візитом до лікаря, а лікарням у наймі високоякісних працівників, забезпечуючи прозорість та достовірність інформації для всіх зацікавлених сторін.
                    
                    **Платежі в охороні здоров'я.** Лікарні, клініки, діагностичні центри та страхові компанії щодня обробляють безліч транзакцій і заявок, включаючи обмін конфіденційними даними, 
                    а тому захист платіжних даних став ще більш важливим. Блокчейн забезпечує безпечне і ефективне управління фінансовими операціями, використовуючи криптографію для 
                    захисту даних та створення стійкого до злому ланцюга транзакцій. Крім того, він оптимізовує платежі, усуваючи посередників, що призводить до швидших транзакцій і зниження витрат. 
                    Статистика показує, що 10% страхових випадків заперечуються, а 17% вимог відхиляються через неповну інформацію, неправильну реєстрацію тощо [3]. 
                    Тож коли пацієнт відвідує лікаря, подія записується в реєстр блокчейну, а страхова отримує повідомлення, що вирішує виникнення будь-яких спорів.  
                    
                    **Електронні медичні карти.** У 2016 році Університет Джона Хопкінса опублікував дослідження, третьою за значущістю причиною смерті в США стали помилки, 
                    допущені внаслідок упущень в історії хвороби. Електронні медичні карти на базі блокчейн можуть легко розв’язати цю проблему. Кожен запис у системі — записка лікаря, 
                    рецепт чи результат аналізів — перетворюється на унікальну хеш-функцію, яку можна розшифрувати тільки з дозволу пацієнта. Кожна поправка або передача даних реєструється як транзакція. 
                    Це забезпечує зручність для пацієнтів і медичних постачальників, спрощує взаємодію зі страховими компаніями та дає пацієнтам контроль над своїми даними. 
                    
                    Bisresearch прогнозує, що використання блокчейну в охороні здоров'я підвищить рівень довіри та дозволить заощадити до 100 мільярдів доларів до 2025 року завдяки зниженню витрат 
                    і запобіганню шахрайству. Отже, у найближчі кілька років очікується ще активніше впровадження блокчейн-рішень у медицину.

                    Література:

                    1.	Binance Academy | Що таке блокчейн і як він працює?. URL: https://academy.binance.com/uk/articles/what-is-blockchain-and-how-does-it-work (2024, May 31)
                    2.	PubMed Central (PMC) | Blockchain technology in the pharmaceutical industry: a systematic review. URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9137953/ (2024, May 31)
                    3.	WhiteBIT Blog | Блокчейн у медицині та фармацевтиці: огляд технології з прикладами. URL: https://blog.whitebit.com/uk/blockchain-in-medicine/ (2024, May 31)
                    """)
    
    elif selected == "Смарт-полички: як аналітика створює оптимальне розташування товарів":
        st.subheader("Смарт-полички: як аналітика створює оптимальне розташування товарів")
        st.write("Nov 07-08, 2024 | [Article](http://www.wayscience.com/wp-content/uploads/2024/11/Conference-Proceedings-November-7-8-2024.pdf#page=298)")
        st.markdown("""
                    У сучасних умовах роздрібна торгівля зазнає значних змін завдяки впровадженню інноваційних технологій. Супермаркети та рітейлери отримують нові можливості для поліпшення клієнтського досвіду, 
                    збільшення продажів і оптимізації внутрішніх процесів. Важливим чинником успіху рітейлу є грамотне розміщення товарів на полицях. Застосування аналітики, штучного інтелекту (ШІ), інтернету 
                    речей (IoT) та технологій великих даних (Big Data) дозволяє компаніям краще розуміти поведінку покупців і вдосконалювати стратегії для збільшення прибутків. 
                    
                    У цій роботі будуть розглянуті приклади того, як лідери ринку використовують сучасні технології для оптимізації своїх бізнес-процесів. Буде проаналізовано, як ці компанії впроваджують інноваційні 
                    рішення для покращення викладки товарів, застосовують аналітичні методи для вивчення поведінки споживачів, використовують IoT для управління запасами та персоналізують свої пропозиції відповідно до потреб клієнтів. 
                    
                    **Аналітика** стала ключовим елементом стратегічного управління у роздрібній торгівлі, надаючи можливість отримувати глибоке розуміння поведінки споживачів, визначати тренди та адаптувати пропозиції до вимог ринку. 
                    Важливим прикладом є використання аналітики компанією **Target**, яка застосовує складні алгоритми для створення детальних профілів покупців. Зібрані дані про покупки дозволяють аналізувати звички клієнтів і передбачати їхні потреби.
                    
                    Одним із найвідоміших підходів є спрямованість на молодих матерів. Завдяки аналізу покупок, таких як безрецептурні ліки, певні вітаміни та інші специфічні товари, компанія змогла виявити ранні ознаки вагітності у своїх клієнтів. 
                    Використовуючи ці дані, **Target** розробила систему, яка автоматично надсилає відповідні рекламні пропозиції, наприклад, купони на дитячі товари або товари для новонароджених. Це дозволило не тільки підвищити рівень персоналізації, 
                    а й утримати лояльність клієнтів. [1]
                    
                    Наступним важливим інструментом можна вважати використання **штучного  інтелекту (ШІ)** для прогнозування попиту та підвищення якості обслуговування. Один із провідних прикладів його використання демонструє мережа 
                    супермаркетів **Walmart**. Завдяки впровадженню ШІ **Walmart** може здійснювати аналіз величезних обсягів даних про продажі, інвентаризацію та поведінку покупців, що дозволяє більш точно прогнозувати попит на товари.
                    
                    Ці прогнози базуються на машинному навчанні, яке враховує історичні дані, сезонні коливання та локальні тенденції. Наприклад, під час свят або спеціальних акцій **Walmart** за допомогою ШІ може прогнозувати зростання попиту на певні товари, 
                    як-от продукти харчування, електроніку чи іграшки. Це дозволяє заздалегідь збільшити обсяги постачання цих товарів, зменшити витрати на зберігання та уникнути дефіциту товарів на полицях, що особливо важливо під час пікових періодів. 
                    Крім того, **Walmart** активно використовує чат-боти, які працюють на базі ШІ, для покращення обслуговування клієнтів. Ці боти надають покупцям миттєві відповіді на поширені запитання, допомагають з оформленням замовлень, надають інформацію 
                    про наявність товарів та статус доставки. [2]
                    
                    **Інтернет речей (IoT)** дозволяє створювати інтерактивну інфраструктуру, де різні пристрої, як-от датчики, RFID-мітки та камери, підключені до інтернету і здатні збирати та обмінюватися інформацією в режимі реального часу. Це дозволяє 
                    рітейлерам відстежувати запаси товарів, оптимізувати логістичні процеси та реагувати на зміни в потребах покупців. Наприклад, датчики можуть автоматично сигналізувати про необхідність поповнення полиць або виявляти товари, які не 
                    користуються попитом, що допомагає краще планувати постачання. **Big Data**, в свою чергу, забезпечує можливість аналізу величезних масивів даних, що надходять від різних джерел, як-от транзакції, відгуки покупців та поведінка користувачів 
                    на сайтах. Завдяки аналітиці **Big Data** можна визначати тренди, вивчати споживчі вподобання та оптимізувати ціноутворення. Крім того, ці технології допомагають прогнозувати майбутні тенденції, підвищувати ефективність маркетингових кампаній 
                    та покращувати управління товарними запасами, що в кінцевому підсумку сприяє зростанню продажів і поліпшенню клієнтського досвіду.
                    
                    **Теплові карти** активно використовуються в рітейлі для аналізу поведінки покупців, і одна з компаній, яка успішно впровадила цей інструмент, — це **IKEA**. У своїх магазинах **IKEA** застосовує теплові карти для вивчення того, як покупці 
                    пересуваються по торговому простору, які ділянки відвідують найчастіше та де затримуються найдовше.
                    
                    На основі теплових карт **IKEA** виявила, що деякі популярні зони, такі як кухонні відділи або відділи зі спальнями, привертають найбільше покупців. Використовуючи ці дані, компанія оптимізувала розташування товарів, створивши 
                    спеціальні маршрути через менш відвідувані частини магазину, щоб направити покупців до нових або акційних товарів. Цей підхід дозволив IKEA збільшити продажі товарів, які не потрапляли у поле зору покупців раніше. 
                    
                    Маршрутизація покупців — технологія, яка дозволяє рітейлерам аналізувати, як покупці переміщуються по магазину, з метою оптимізації розміщення товарів та поліпшення досвіду споживачів – досягається за допомогою збору даних 
                    про маршрути, які проходять споживачі, використовуючи різноманітні технології, такі як камери, датчики та мобільні додатки.
                    
                    Компанія Tesco, один із найбільших рітейлерів у Великій Британії, активно впроваджує технології маршрутизації покупців у своїх супермаркетах. Використовуючи аналітику та великі дані, Tesco має можливість відстежувати маршрути покупців 
                    у магазинах і аналізувати, які ділянки є найпопулярнішими, а які залишаються без уваги. Ця інформація дозволяє Tesco не лише оптимізувати розташування товарів на полицях, але й розробляти маркетингові стратегії, які залучають увагу покупців. 
                    Наприклад, якщо певні товари, такі як свіжі овочі та фрукти, не отримують достатньо уваги, Tesco може помістити їх у зони, де покупці найчастіше проходять, або влаштувати акції, щоб привернути їхню увагу. Завдяки впровадженню технологій маршрутизації покупців, 
                    компанія зафіксувала підвищення продажів свіжих продуктів на 20% у магазинах, де було оптимізовано розташування товарів на основі даних маршрутизації. [3]
                    
                    Прогнозування попиту є критично важливим аспектом управління роздрібною торгівлею, оскільки дозволяє рітейлерам оптимізувати запаси, зменшити витрати і покращити обслуговування клієнтів. Це процес, в якому аналізуються дані про продажі, сезонність, 
                    ринкові тренди та поведінку споживачів для передбачення майбутнього попиту на певні товари. Прогнозування попиту ґрунтується на аналізі історичних даних, які можуть включати: обсяги продажів у різні періоди часу, для виявлення патернів та трендів; сезонні коливання, 
                    такі як святкові періоди та спеціальні події, що впливають на попит; макроекономічні фактори, які впливають на купівельну спроможність споживачів; дані про поведінку покупців, для розуміння, які фактори впливають на їхні рішення щодо покупки.
                    
                    A/B тестування є ще одним потужним інструментом для оптимізації розташування товарів. Цей метод полягає у порівнянні двох варіантів розташування товарів для визначення, який з них є більш ефективним у залученні покупців.
                    
                    Один з яскравих прикладів A/B тестування є Amazon. Компанія регулярно проводить тести, змінюючи порядок відображення товарів на сторінках, щоб визначити, який варіант краще конвертує відвідувачів у покупців. Одним із прикладів є тестування різних 
                    варіантів відображення кнопки "Додати до кошика". Amazon змінювала кольори, розміри та розташування кнопки, щоб визначити, який варіант сприяє найбільшій кількості кліків та конверсій. У результаті одного з таких тестів компанія виявила, що зміна кольору кнопки на яскравіший відтінок призвела до збільшення продажів на 3%. Хоча це здається незначним, для компанії з такими обсягами продажів, як Amazon, навіть маленьке підвищення конверсії може означати мільйони додаткових доларів у прибутках. [4]
                    
                    Моніторинг запасів за допомогою Інтернету речей (IoT) є не менш важливим аспектом управління рітейлом, який дозволяє компаніям автоматизувати та оптимізувати процеси контролю за товарними запасами. IoT включає використання сенсорів, підключених до Інтернету, для збору даних про стан товарів на складах і в магазинах. Це забезпечує рітейлерам можливість отримувати в реальному часі інформацію про рівень запасів, терміни придатності товарів та інші критично важливі показники. 
                    
                    Сенсори: Рітейлери встановлюють сенсори на полицях, у холодильниках та на складі для автоматичного моніторингу кількості товарів. Ці сенсори можуть виявляти, коли запаси знижуються до критичного рівня. Збір даних: Дані з сенсорів передаються в реальному часі на центральну платформу, де вони аналізуються. Це дозволяє рітейлерам отримувати інформацію про поточний стан запасів без необхідності проводити фізичну інвентаризацію. Аналіз і управління: На основі зібраних даних рітейлери можуть прогнозувати попит на товари, виявляти недоліки у запасах і своєчасно поповнювати асортимент. Автоматизація: У разі досягнення критичного рівня запасів система може автоматично генерувати замовлення на поповнення товарів, що знижує ризик дефіциту.
                    
                    Carrefour – одна з найбільших мереж супермаркетів у світі – активно використовує технології IoT для управління запасами. Carrefour впровадила рішення, які базуються на сенсорах, що відстежують запаси товарів на полицях магазинів. До прикладу, компанія реалізувала проект у Франції, де сенсори автоматично фіксували, коли рівень товарів на полицях знижується до певного порогу. Ця інформація надходила в центральну систему управління, яка в режимі реального часу моніторила запаси по всій мережі магазинів. Для моніторингу свіжості продуктів, особливо в секторах свіжих овочів і фруктів компанія використовувала датчики температури і вологості, щоб контролювати умови зберігання товарів Завдяки цьому підходу Carrefour змогла зменшити витрати, збільшити задоволення споживачів та підвищити ефективність. [5]
                    
                    Впровадження інноваційних технологій у роздрібній торгівлі є необхідністю для адаптації до сучасних умов ринку. Це не лише змінює правила гри, але й відкриває нові можливості для підвищення ефективності бізнесу та глибшого розуміння клієнтів. Використання штучного інтелекту, великих даних, аналітики та IoT допомагає рітейлерам не лише задовольняти очікування споживачів, але й створювати персоналізований досвід, який є ключовим для лояльності та успіху в умовах високої конкуренції.

                    Літературні джероела:
                    1.	Duhigg C. How Companies Learn Your Secrets. The New York Time Magazine. 2012. URL: https://doi.org/10.7312/star16075-025
                    2.	de Mattos C. A., Correia F. C., Kissimoto K. O. Artificial Intelligence Capabilities for Demand Planning Process. Logistics. 2024. Vol. 8, no. 2. P. 53. URL: https://doi.org/10.3390/logistics8020053 
                    3.	Smith D. Logistics in Tesco: Past, Present and Future. Logistics And Retail Management insights Into Current Practice And Trends From Leading Experts. Boca Raton, 2023. P. 154–183. URL: https://doi.org/10.4324/9780429271144-8 
                    4.	The impacts of learning analytics and A/B testing research: a case study in differential scientometrics / R. S. Baker et al. International Journal of STEM Education. 2022. Vol. 9, no. 1. URL: https://doi.org/10.1186/s40594-022-00330-6 
                    5.	CarrefourSA's Rapid Expansion Strategy: Leveraging IoT | IoT ONE Digital Transformation Advisors. IoT ONE. URL: https://www.iotone.com/case-study/carrefoursa-s-rapid-expansion-strategy-leveraging-iot-for-retail-growth/c3169 
                    """)

# SQL
if selected == 'SQL':
    st.markdown("<h1 style='text-align: center;'>SQL</h1>", unsafe_allow_html=True)
    selected_options = ["Overview", 
                        "PostgreSQL",
                        "SQLite"]
    selected = st.selectbox("Choose a topic you would like to check me on:", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
                    Here, I share my journey and projects involving some of the most powerful and widely used database technologies: PostgreSQL, SQLite and MongoDB. 
                    
                    Each project showcases unique features, practical applications, and best practices for using these databases effectively.
        """)
        st.subheader("What You'll Find Here")
        st.markdown("""
                    - **PostgreSQL Projects:** 

                    - **SQLite Projects:** 
                    """)

        st.write("Let's dive deep into my practical realm... 🔎")
   
    elif selected == "PostgreSQL":
        st.subheader("PostgreSQL")
        selected_options = ["#1. Titanic-Dataset", 
                            "#2 Tennis country club"]
        selected = st.selectbox("Choose a project:", options = selected_options)
        if selected == "#1. Titanic-Dataset":
            st.subheader("Titanic-Dataset")
            df = pd.read_csv('datasets/Titanic-Dataset.csv')
            st.write(df)
            st.write("**Here is a description of each column in the Titanic dataset:**")
            st.write("📌 **PassengerId** - Unique identifier for each passenger.",
                 "<br>📌 **Survived** - Survival status (0 = No, 1 = Yes).",
                 "<br>📌 **Pclass** - Passenger class (1st, 2nd, 3rd)",
                 "<br>📌 **Name** - Full name of the passenger",
                 "<br>📌 **Sex** - Gender of the passenger",
                 "<br>📌 **Age** - Age of the passenger in years",
                 "<br>📌 **SibSp** - Number of siblings/spouses aboard the Titanic",
                 "<br>📌 **Parch** - Number of parents/children aboard the Titanic",
                 "<br>📌 **Ticket** - Ticket number",
                 "<br>📌 **Fare** - Passenger fare",
                 "<br>📌 **Cabin** - Cabin number (if known)",
                 "<br>📌 **Embarked** - Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)",
                 unsafe_allow_html=True)
            # 1
            st.write("**1. A list of the first 5 passangers of the Titanic.**")
            code = '''SELECT * FROM titanic LIMIT 5'''
            st.code(code, language='sql')
            subset_df = df.head(5)  
            st.write(subset_df)
            # 2
            st.write("**2. A list of passengers of the Titanic whose sex is female.**")
            code = '''SELECT * FROM titanic WHERE sex = 'female' '''
            st.code(code, language='sql')
            subset_df = df[df['Sex'] == 'female']
            st.write(subset_df)
            # 3
            st.write("**3. A list of passengers who were younger than 10 years old, did not survive on sinking Titanic, and were in class 1.**")
            code = """SELECT * FROM titanic WHERE age < 10 AND survived = 0 AND pclass = 1"""
            st.code(code, language='sql')
            subset_df = df[(df['Age'] < 10) & (df['Survived'] == 0) & (df['Pclass'] == 1)]
            st.write(subset_df)
            # 4
            st.write("**4. A list of passengers who are either male or younger than 5 years old.**")
            code = """SELECT age, sex WHERE age < 5 OR age = 'female' """
            st.code(code, language='sql')
            subset_df = df[(df['Sex'] == 'male') | (df['Age'] < 5)][['Sex', 'Age']] 
            st.write(subset_df)
            # 5
            st.write("**5. A list of unique values for the sex of the passengers from the Titanic.**")
            code = """SELECT DISTINCT sex AS unique_sex FROM titanic"""
            st.code(code, language='sql')
            unique_sex = pd.DataFrame(df['Sex'].dropna().unique(), columns=['unique_sex']) 
            st.write(unique_sex)
            # 6
            st.write("**6. A list of passengers from the Titanic whose cabins have a name.**")
            code = """SELECT * FROM titanic WHERE cabin IS NOT NULL"""
            st.code(code, language='sql')
            non_null_cabin_df = df[df['Cabin'].notna()] 
            st.write(non_null_cabin_df)
            # 7
            st.write("**7. A list of passengers from the Titanic showing their survival status, port of embarkation, and the number of siblings/spouses aboard, "
                     "where the port of embarkation is either 'S' (Southampton) or 'C' (Cherbourg) and the number of siblings/spouses aboard is either 0, 1, or 3.**")
            code = """SELECT survived, embarked, sibsp FROM titanic 
                      WHERE embarked IN ('S', 'C') AND
                      sibsp IN (0, 1, 3)"""
            st.code(code, language='sql')
            filtered_df = df[(df['Embarked'].isin(['S', 'C'])) & (df['SibSp'].isin([0, 1, 3]))][['Survived', 'Embarked', 'SibSp']]
            st.write(filtered_df)
            # 8
            st.write("**8. A list of passengers from the Titanic whose number of siblings/spouses aboard is between 2 and 4 (inclusive) and the port of embarkation "
                     "is between 'A' and 'Q' (alphabetically).**")
            code = """SELECT survived, embarked, sibsp FROM titanic 
                      WHERE (sibsp BETWEEN 2 AND 4) AND 
                      (embarked BETWEEN 'A' AND 'Q')"""
            st.code(code, language='sql')
            filtered_df = df[(df['SibSp'].between(2, 4)) & (df['Embarked'].between('A', 'Q'))][['Survived', 'Embarked', 'SibSp']]
            st.write(filtered_df)
            # 9
            st.write("**9. A list of passengers from the Titanic showing their names and cabin values, where the passenger's name contains the letter 'a' "
                      "(case insensitive) and the cabin starts with the letter 'G' followed by any single character.**")
            code = """SELECT name, cabin FROM titanic WHERE 
                      LOWER(name) LIKE '%a%' AND
                      LOWER(cabin) LIKE 'g_'"""
            st.code(code, language='sql')
            df['name_lower'] = df['Name'].str.lower()
            df['cabin_lower'] = df['Cabin'].str.lower()
            filtered_df = df[df['name_lower'].str.contains('a') & df['cabin_lower'].str.match('g.')][['Name', 'Cabin']]
            st.write(filtered_df)
            # 10
            st.write("**10. Calculate and display the following statistics for the 'age' column in the Titanic: count, sum, mean, minimum, maximum, variance, "
                     "and standard deviation.**")
            code = """SELECT COUNT(age) AS "age_count",
                      SUM(age) AS "age_sum",
                      AVG(age) AS "age_mean",
                      MIN(age) AS "age_min",
                      MAX(age) AS "age_max",
                      VARIANCE(age) AS "age_variance",
                      STDDEV(age) AS "age_stdev"                      
                      FROM titanic"""
            st.code(code, language='sql')
            age_count = df['Age'].count()
            age_sum = df['Age'].sum()
            age_mean = df['Age'].mean()
            age_min = df['Age'].min()
            age_max = df['Age'].max()
            age_variance = df['Age'].var()
            age_stdev = df['Age'].std()
            age_stats = pd.DataFrame({
                "Count": [age_count],
                "Sum": [age_sum],
                "Mean": [age_mean],
                "Min": [age_min],
                "Max": [age_max],
                "Variance": [age_variance],
                "StDev": [age_stdev]
                })
            st.write(age_stats)
            # 11
            st.write("**11. Calculate and display the correlation and sample covariance between the 'age' and 'fare' columns.**")
            code = """SELECT CORR(age, fare),
                      COVAR_SAMP(age, fare) 
                      FROM titanic"""
            st.code(code, language='sql')
            corr_age_fare = df['Age'].corr(df['Fare'])
            covar_samp_age_fare = df[['Age', 'Fare']].cov().iloc[0, 1]
            stats_df = pd.DataFrame({
                "Pearson’ correlation coefficient": [corr_age_fare],
                "Sample covariance": [covar_samp_age_fare]
            })
            st.write(stats_df)
            # 12
            st.write("**12. A list of passengers in the Titanic, showing their age and survival status, where the age is not null, ordered by age in descending order.**")
            code = """SELECT age, survived FROM titanic 
                      WHERE age IN NOT NULL 
                      ORDER BY age DESC"""
            st.code(code, language='sql')
            filtered_df = df[df['Age'].notnull()][['Age', 'Survived']].sort_values(by='Age', ascending=False)
            st.write(filtered_df)
            # 13
            st.write("**13. Count the number of passengers for each sex in the Titanic and display the results ordered by count in descending order.**")
            code = """SELECT sex, COUNT(sex) FROM titanic
                      GROUP BY sex
                      ORDER BY COUNT(sex) DESC"""
            st.code(code, language='sql')
            sex_counts = df.groupby('Sex').size().reset_index(name='Count').sort_values(by='Count', ascending=False)
            st.write(sex_counts)
            # 14
            st.write("**14. Count the number of passengers for each 'sibsp' value in the Titanic dataset, showing only those with a count greater than 10, and display the "
                     "results ordered by count in descending order.**")
            code = """SELECT sibsp, COUNT(*) FROM titanic 
                      GROUP BY sibsp 
                      HAVING COUNT(*) > 10
                      ORDER BY COUNT(*) DESC"""
            st.code(code, language='sql')
            sibsp_counts = df.groupby('SibSp').size().reset_index(name='Count')
            sibsp_counts_filtered = sibsp_counts[sibsp_counts['Count'] > 10].sort_values(by='Count', ascending=False)
            st.write(sibsp_counts_filtered)
            # 15
            st.write("**15. Calculate and display several mathematical transformations of the fare values. Include rounding to one decimal place, square root, cube root, floor, ceiling, truncation, logarithm (with a slight adjustment for values close to zero), exponential, and power of 2 transformations.**")
            code = """SELECT fare, 
                      ROUND(fare::NUMERIC, 1) AS round,
                      ROUND(SQRT(fare)::NUMERIC, 1) AS sqrt, 
                      ROUND(CBRT(fare)::NUMERIC, 1) AS cbrt,
                      ROUND(FLOOR(fare)::NUMERIC, 1) AS floor,
                      ROUND(CEIL(fare)::NUMERIC, 1) AS ceil,
                      TRUNC(fare),
                      ROUND(LOG(fare + 0.0000001)::NUMERIC, 1) AS log,
                      ROUND(EXP(fare)::NUMERIC, 1) AS exp,
                      ROUND(POWER(fare, 2)::NUMERIC, 1) AS power_2
                      FROM titanic"""
            st.code(code, language='sql')
            def apply_transformations(df):
                df['round'] = df['Fare'].round(1)
                df['sqrt'] = np.sqrt(df['Fare']).round(1)  # Square root of fare
                df['cbrt'] = np.cbrt(df['Fare']).round(1)  # Cube root of fare
                df['floor'] = np.floor(df['Fare']).round(1)  # Floor value of fare
                df['ceil'] = np.ceil(df['Fare']).round(1)  # Ceiling value of fare
                df['trunc'] = df['Fare'].apply(int)  # Truncate fare to integer
                df['log'] = np.log(df['Fare'] + 0.0000001).round(1)  # Logarithm of fare (adjusted for values close to zero)
                df['exp'] = np.exp(df['Fare']).round(1)  # Exponential of fare
                df['power_2'] = np.power(df['Fare'], 2).round(1)  # Power of 2 of fare

                df = df[['Fare', 'round', 'sqrt', 'cbrt', 'floor', 'ceil', 'trunc', 'log', 'exp', 'power_2']]

                df = df.rename(columns={
                                        'round': 'Rounded Fare (1 decimal)',
                                        'sqrt': 'Square Root',        
                                        'cbrt': 'Cube Root',
                                        'floor': 'Floor Value',
                                        'ceil': 'Ceiling Value',
                                        'trunc': 'Truncated Fare',
                                        'log': 'Logarithm',
                                        'exp': 'Exponential',
                                        'power_2': 'Fare Squared'
                                        })
                return df 
            transformed_df = apply_transformations(df)
            st.write(transformed_df)
            # 16
            st.write("**16. Perform various string operations on the 'name' column in the Titanic dataset and order by length.**")
            code = """SELECT name, 
                      LOWER(name),
                      UPPER(name),
                      INITCAP(lLOWER(name)),
                      TRIM(name) AS trim,
                      LEFT(name, 2),
                      RIGHT(name, 2),
                      LENGTH(name),
                      SUBSTR(name, 2, 5),
                      POSITION('r' IN name),
                      SUBSTRING(name FROM 2 FOR 3),
                      SUBSTRING(LOWER(name), '^l.*i$'),
                      SUBSTRING(LOWER(name), 'l', 'lll'),
                      REPEAT(LEFT(name, 2), 3),
                      REVERSE(name),
                      FROM titanic
                      ORDER BY length"""
            st.code(code, language='sql')
            df['Lower name'] = df['Name'].str.lower() # Converts letters to Lowercase
            df['Upper name'] = df['Name'].str.upper() # Converts letters to Uppercase
            df['First letter'] = df['Name'].str.title() # Capitalizes the first letter of each word
            df['Spaces'] = df['Name'].str.strip() # Removes extra spaces at the beginning and end
            df['Left 2'] = df['Name'].str[:2] # Extracts the first two characters
            df['Right 2'] = df['Name'].str[-2:] # Extracts the last two characters.
            df['Length'] = df['Name'].str.len() # Calculates the length of each name
            df['Substr'] = df['Name'].str[1:6] # Extracts 5 characters from 2nd position (starting fro 1)
            df['Position r'] = df['Name'].str.find('r') # Finds the position of the first occurrence of the letter "r"
            df['Substring'] = df['Name'].str[1:4] # Extracts 3 characters from index 2
            df['Substring Regex'] = df['Name'].str.lower().str.extract(r'^(l.*i)$', expand=False) # Finds names starting with 'l' and ending with 'i'
            df['Replace l with lll'] = df['Name'].str.lower().str.replace('l', 'lll', regex=True) # Replaces every "l" with "lll"
            df['Repeat left 2'] = df['Name'] * 3  # Repeat the first 2 chars of name 3 times
            df['Reverse name'] = df['Name'].apply(lambda x: x[::-1] if isinstance(x, str) else x) # Reverses the name 
            
            df_sorted = df[['Name', 'Lower name', 'Upper name', 'First letter', 'Spaces', 'Left 2', 'Right 2', 
                'Length', 'Substr', 'Position r', 'Substring', 'Substring Regex', 'Replace l with lll', 'Repeat left 2', 'Reverse name']].sort_values(by='Length')
            st.write(df_sorted)
            # 17
            st.write("**17. What percentage of males and females survived?**")
            code = """SELECT sex,
                      ROUND(COUNT(sex) / AVG(c.count)) * 100, 1) AS survived_percentage
                      FROM titanic
                      LEFT JOIN
                      (SELECT sex, COUNT(sex) FROM titanic GROUP BY sex) AS c USING(sex)
                      WHERE survived = 1
                      GROUP BY sex, survived 
                      ORDER BY survived_percentage DESC"""
            st.code(code, language='sql')
            survival_percentage = (df[df['Survived'] == 1]['Sex'].value_counts() / df['Sex'].value_counts()) * 100
            survival_percentage_df = survival_percentage.reset_index()
            survival_percentage_df.columns = ['Sex', 'Survived Percentage']
            survival_percentage_df['Survived Percentage'] = survival_percentage_df['Survived Percentage'].round(1)
            survival_percentage_df = survival_percentage_df.sort_values(by='Survived Percentage', ascending=False)
            st.write(survival_percentage_df) 
            # 18
            st.write("**18. What percentage of passengers survived per class?**")
            code = """SELECT pclass,
                      ROUND((COUNT(*) / AVG(c.count)) * 100, 1) AS percent_survived
                      FROM titanic
                      LEFT JOIN (SELECT pclass, COUNT(pclass) FROM titanic GROUP BY pclass) AS c
                      USING(pclass)
                      GROUP BY pclass, survived
                      HAVING survived = 1
                      ORDER BY pclass"""
            st.code(code, language='sql')
            survival_percentage = (df[df['Survived'] == 1]['Pclass'].value_counts() / df['Pclass'].value_counts()) * 100
            survival_percentage_df = survival_percentage.reset_index()
            survival_percentage_df.columns = ['Pclass', 'Survived Percentage']
            survival_percentage_df['Survived Percentage'] = survival_percentage_df['Survived Percentage'].round(1)
            survival_percentage_df = survival_percentage_df.sort_values(by='Pclass')
            st.write(survival_percentage_df)
            # 19
            st.write("**19. Count the number of passengers by their title.**")
            code = """WITH total AS (SELECT COUNT(*) FROM titianic)
                      SELECT REPLACE(SUBSTRING(name, ', [a-zA-Z]*'), ', ', '') AS title,
                      COUNT(*) AS frequency, 
                      CONCAT(ROUND((COUNT(*) / avg(total.count)) * 100, 2), '%') AS relative_frequency
                      FROM titanic, total
                      GROUP BY title
                      ORDER BY frequency DESC"""
            st.code(code, language='sql')
            df['Title'] = df['Name'].apply(lambda x: re.search(r', (\w+)', x).group(1) if re.search(r', (\w+)', x) else 'Unknown')
            title_counts = df['Title'].value_counts().reset_index()
            title_counts.columns = ['Title', 'Frequency']
            total_passengers = len(df) 
            title_counts['Relative_Frequency'] = title_counts['Frequency'].apply(lambda x: f"{round((x / total_passengers) * 100, 2)}%")
            st.write(title_counts)
            # 20
            st.write("**20. What is the average fare, number of passengers and total fare earned per class?**")
            code = """SELECT pclass,
            ROUND(AVG(fare)::DECIMAL, 2) AS average_fare,
            TRUNC(AVG(c.count)) AS passenger_count,
            ROUND(SUM(fare)::DECIMAL, 2) AS total_fare
            FROM titanic
            LEFT JOIN (SELECT pclass, COUNT(pclass) FROM titanic GROUP BY pclass) AS c 
            USING(pclass)
            GROUP BY pclass
            ORDER BY pclass"""
            st.code(code, language='sql')
            pclass_stats = df.groupby('Pclass').agg(
                average_fare=('Fare', lambda x: round(x.mean(), 2)),
                passenger_count=('Pclass', 'count'),
                total_fare=('Fare', lambda x: round(x.sum(), 2))
                ).reset_index()
            pclass_stats = pclass_stats.sort_values(by='Pclass')
            st.write(pclass_stats)
            # 21
            st.write("**21. Did having a sibling/spouse aboard help the passengers survive?**")
            code = """SELECT sibsp, 
            ROUND((COUNT(*) / AVG(c.count)) * 100, 1) AS percent_survived
            FROM titanic
            LEFT JOIN (SELECT sibsp, COUNT(sibsp) FROM titanic GROUP BY sibsp) AS c
            USING(sibsp)
            GROUP BY sibsp, survived
            HAVING survived = 1
            ORDER BY percent_survived DESC"""
            st.code(code, language='sql')
            sibsp_counts = df.groupby('SibSp').size().reset_index(name='Total_Count')
            sibsp_survivors = df[df['Survived'] == 1].groupby('SibSp').size().reset_index(name='Survived_Count')
            sibsp_stats = sibsp_counts.merge(sibsp_survivors, on='SibSp', how='left').fillna(0)
            sibsp_stats['Percent Survived'] = round((sibsp_stats['Survived_Count'] / sibsp_stats['Total_Count']) * 100, 1)
            sibsp_stats = sibsp_stats[['SibSp', 'Percent Survived']].sort_values(by='Percent Survived', ascending=False)
            st.write(sibsp_stats)
            # 22
            st.write("**22. What is the count of passengers per cabin code (first character in the cabin string)?**")
            code = """SELECT LEFT(cabin, 1) AS cabin_code,
                      COUNT(*)
                      FROM titanic
                      WHERE cabin IS NOT NULL
                      GROUP BY cabin_code
                      ORDER BY count DESC"""
            st.code(code, language='sql')
            df_cabin = df[df['Cabin'].notna()]
            df_cabin['Cabin Code'] = df_cabin['Cabin'].astype(str).str[0] 
            cabin_counts = df_cabin['Cabin Code'].value_counts().reset_index()
            cabin_counts.columns = ['Cabin Code', 'Count']
            cabin_counts = cabin_counts.sort_values(by='Count', ascending=False)
            st.write(cabin_counts)
        elif selected == "#2 Tennis country club":
            st.write("The datasets are for a newly created country club, "
                     "with a set of members, facilities such as "
                     "tennis courts, and booking history for those facilities. Amongst other things, the club wants to understand "
                     "how they can use their information to analyse facility usage/demand.")
            st.subheader("Members table:")
            df_m = pd.read_csv('datasets/members.csv')
            st.write(df_m)
            st.write("I'll start off with a look at the Members table. Each member has an ID, basic address information, a reference to the "
                     "member that recommended them (if any), and a timestamp for when they joined. The addresses in the "
                     "dataset are entirely (and unrealistically) fabricated.")
            st.subheader("Facilities table:")
            df_f = pd.read_csv('datasets/facilities.csv')
            st.write(df_f)
            st.write("The facilities table lists all the bookable facilities that the country club possesses. The club stores id/name "
                     "information, the cost to book both members and guests, the initial cost to build the facility, and estimated "
                     "monthly upkeep costs. The main purpose of this table is to track how financially worthwhile each facility is.")
            st.subheader("Table tracking bookings of facilities:")
            df_b = pd.read_csv('datasets/bookings.csv')
            st.write(df_b)
            st.write("Finally, there's a table tracking bookings of facilities. This stores the facility id, the member who made the "
                     "booking, the start of the booking, and how many half hour 'slots' the booking was made for.")
            selected_options = ["Simple SQL Queries",
                                "Joins and Subqueries",
                                "Modifying Data",
                                "Aggregation",
                                "Working with Timestamps",
                                "String Operations"]
            selected = st.selectbox("Choose the topic you are intered in:", options = selected_options)
            if selected == "Simple SQL Queries":
                st.subheader("Simple SQL Queries B")
                # 1
                st.write("**1. Retrieve everything from a facilities table.**")
                code = '''SELECT * FROM cd.facilities'''
                st.code(code, language='sql')
                st.write(df_f)
                # 2
                st.write("**2. Print out a list of all of the facilities and their cost to members.**")
                code = '''SELECT name, membercost FROM cd.facilities'''
                st.code(code, language='sql')
                st.write(df_f[['name', 'membercost']])
                # 3
                st.write("**3. Produce a list of facilities that charge a fee to members?**")
                code = '''SELECT * FROM cd.facilities WHERE membercost != 0'''
                st.code(code, language='sql')
                st.write(df_f[df_f['membercost'] != 0])
                # 4
                st.write("**4. Produce a list of facilities that charge a fee to members, and that fee is less than 1/50th "
                     "of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of "
                     "the facilities in question.**")
                code = '''SELECT facid, name, membercost, monthlymaintenance 
                FROM cd.facilities 
                WHERE membercost > 0 AND membercost < monthlymaintenance/50.0'''
                st.code(code, language='sql')
                st.write(df_f[(df_f['membercost'] > 0) & (df_f["membercost"] < df_f["monthlymaintenance"]/50)])
                # 5
                st.write("**5. Produce a list of all facilities with the word 'Tennis' in their name?**")
                code = '''SELECT * FROM cd.facilities WHERE name LIKE '%Tennis%'''
                st.code(code, language='sql')
                st.write(df_f[df_f['name'].str.contains('Tennis', case=False)])
                # 6
                st.write("**6. Retrieve the details of facilities with ID 1 and 5. Do it without using the OR operator.**")
                code = '''SELECT * FROM cd.facilities WHERE facid IN (1, 5)'''
                st.code(code, language='sql')
                st.write(df_f[df_f['facid'].isin([1, 5])])
                # 7
                st.write("**7. Produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly "
                     "maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.**")
                code = '''SELECT name, 
                CASE 
                WHEN monthlymaintenance > 100 THEN 'expensive' 
                ELSE 'cheap' 
                END AS cost     
                FROM cd.facilities'''
                st.code(code, language='sql')
                df_filtered = df_f.assign(cost=df_f['monthlymaintenance'].apply(lambda x: 'expensive' if x > 100 else 'cheap'))[['name', 'cost']]
                st.write(df_filtered)
                # 8
                st.write("**8. Produce a list of members who joined after the start of September 2012. Return the memid, surname, firstname, "
                     "and joindate of the members in question.**")
                code = """SELECT memid, surname, firstname, joindate 
                FROM cd.members
                WHERE joindate >= '2012-09-01'"""
                st.code(code, language='sql')
                df_filtered = df_m[df_m['joindate'] >= '9/1/2012']
                st.write(df_filtered[['memid', 'surname', 'firstname', 'joindate']])
                # 9
                st.write("**9.  Produce an ordered list of the first 10 surnames in the members table. The list must not contain duplicates.**")
                code = """SELECT DISTINCT surname 
                FROM cd.members 
                ORDER BY surname ASC 
                LIMIT 10"""
                st.code(code, language='sql')
                st.write(df_m['surname'].drop_duplicates().sort_values().head(10))
                # 10
                st.write("**10. You, for some reason, want a combined list of all surnames and all facility names. Produce that list! :)**")
                code = """SELECT surname
                FROM cd.members
                UNION
                SELECT name
                FROM cd.facilities"""
                st.code(code, language='sql')
                st.write(pd.concat([df_m['surname'], df_f['name']]).drop_duplicates())
                # 11
                st.write("**11. Get the signup date of your last member.**")
                code = """SELECT max(joindate) AS latest FROM cd.members"""
                st.code(code, language='sql')
                latest_signup = pd.DataFrame({'joindate': ['9/26/2012 18:08']})
                st.table(latest_signup)
                # 12
                st.write("**12. Get the first and last name of the last member(s) who signed up - not just the date.**")
                code = """SELECT firstname, surname, joindate
                FROM cd.members
                WHERE joindate = (SELECT MAX(joindate) FROM cd.members)"""
                st.code(code, language='sql')
                latest_signup_name = pd.DataFrame({
                'firstname': ['Drarren'],
                'surname': ['Smith'], 
                'joindate': ['9/26/2012 18:08']})
                st.table(latest_signup_name)
            
            elif selected == "Joins and Subqueries":
                st.subheader("Joins and Subqueries")
                # 1
                st.write("**1. Produce a list of the start times for bookings by members named 'David Farrell'?**")
                code = """SELECT bks.starttime 
                FROM cd.bookings bks
                INNER JOIN cd.members mems
                ON bks.memid = mems.memid
                WHERE mems.firstname = 'David' AND mems.surname = 'Farrell'"""
                st.code(code, language='sql')
                df_merged = pd.merge(df_b, df_m, on='memid')
                df_result = df_merged[(df_merged['firstname'] == 'David') & (df_merged['surname'] == 'Farrell')]
                st.write(df_result[['starttime']])
                # 2
                st.write("**2. Produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'. "
                     "Return a list of start time and facility name pairings, ordered by the time.**")
                code = ("""SELECT bks.starttime as start, facs.name as name
                FROM 
                cd.facilities facs
                INNER JOIN cd.bookings bks
                ON facs.facid = bks.facid
                WHERE bks.starttime >= '2012-09-21' 
                AND bks.starttime < '2012-09-22'
                AND facs.name LIKE 'Tennis Court%'
                ORDER BY bks.starttime
                """)
                st.code(code, language='sql')
                df_merged = pd.merge(df_b, df_f, on='facid')
                df_merged['starttime'] = pd.to_datetime(df_merged['starttime'])
                df_result = df_merged[
                (df_merged['starttime'] >= '2012-09-21') & 
                (df_merged['starttime'] < '2012-09-22') & 
                (df_merged['name'].str.contains('Tennis Court'))]
                df_result = df_result.sort_values(by='starttime')
                st.table(df_result[['starttime', 'name']])
                # 3
                st.write("**3. Output a list of all members who have recommended another member. Ensure that there are "
                     "no duplicates in the list, and that results are ordered by (surname, firstname).**")
                code = """SELECT DISTINCT recs.firstname as firstname, recs.surname as surname
                FROM	
                cd.members mems
                INNER JOIN cd.members recs
                ON recs.memid = mems.recommendedby
                ORDER BY surname, firstname"""
                st.code(code, language='sql')
                df_recommended = df_m.merge(df_m, left_on='recommendedby', right_on='memid', suffixes=('', '_recommender'))
                df_recommended = df_recommended[['firstname_recommender', 'surname_recommender']].drop_duplicates()
                df_recommended.columns = ['firstname', 'surname']
                df_recommended = df_recommended.sort_values(by=['surname', 'firstname'])
                st.table(df_recommended)
                # 4
                st.write("**4. Output a list of all members, including the individual who recommended them (if any)."
                     "Ensure that results are ordered by (surname, firstname).**")
                code = """SELECT mems.firstname as memfname, mems.surname as memsname, 
                recs.firstname as recfnaem, recs.surname as recsname
                FROM 
                cd.members mems
                LEFT OUTER JOIN cd.members recs
                ON recs.memid = mems.recommendedby
                ORDER BY memsname, memfname"""
                st.code(code, language='sql')
                df_joined = df_m.merge(df_m, how='left', left_on='recommendedby', right_on='memid', suffixes=('_member', '_recommender'))
                df_result = df_joined[['firstname_member', 'surname_member', 'firstname_recommender', 'surname_recommender']]
                df_result.columns = ['memfname', 'memsname', 'recfname', 'recsname'] 
                df_result = df_result.sort_values(by=['memsname', 'memfname'])
                st.table(df_result)
                # 5
                st.write("**5. Produce a list of all members who have used a tennis court. Include in your output the name "
                     "of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and "
                     "order by the member name.**")
                code = """SELECT DISTINCT mems.firstname || ' ' || mems.surname as member, facs.name as facility
                FROM
                cd.members mems
                INNER JOIN cd.bookings bks
                ON mems.memid = bks.memid
                INNER JOIN cd.facilities facs
                ON bks.facid = facs.facid
                WHERE bks.facid IN (0,1)
                ORDER BY member, facility"""
                st.code(code, language='sql')
                df_merged = df_m.merge(df_b, on='memid').merge(df_f, on='facid')
                df_tennis = df_merged[df_merged['facid'].isin([0, 1])]
                df_tennis['member'] = df_tennis['firstname'] + ' ' + df_tennis['surname']
                df_result = df_tennis[['member', 'name']].drop_duplicates().sort_values(by=['member', 'name'])
                df_result.columns = ['member', 'facilities']
                st.table(df_result)
                # 6
                st.write("**6. Produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) "
                     "more than $30? Remember that guests have different costs to members (the listed costs are per half-hour "
                     "'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the "
                     "member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.**")
                code = """SELECT mems.firstname || ' ' || mems.surname as member, facs.name as facility, 
                CASE 
                WHEN mems.memid = 0 THEN
                    bks.slots*facs.guestcost
                ELSE
                    bks.slots*facs.membercost
                END AS cost
                FROM
                cd.members mems                
                INNER JOIN cd.bookings bks
                        ON mems.memid = bks.memid
                INNER JOIN cd.facilities facs
                        ON bks.facid = facs.facid
                WHERE
		        bks.starttime >= '2012-09-14' AND
		        bks.starttime < '2012-09-15' AND (
			        (mems.memid = 0 and bks.slots*facs.guestcost > 30) OR
			        (mems.memid != 0 and bks.slots*facs.membercost > 30)
                )
                ORDER BY cost DESC"""
                st.code(code, language='sql') 
                df_merged = df_b.merge(df_m, on='memid').merge(df_f, on='facid')
                df_merged['starttime'] = pd.to_datetime(df_merged['starttime'])
                df_filtered = df_merged[(df_merged['starttime'].dt.date == pd.to_datetime('2012-09-14').date())]
                df_filtered['cost'] = df_filtered.apply(
                    lambda row: row['slots'] * row['guestcost'] if row['memid'] == 0 else row['slots'] * row['membercost'], axis=1)
                df_result = df_filtered[df_filtered['cost'] > 30]
                df_result['member'] = df_result['firstname'] + ' ' + df_result['surname']
                df_result = df_result[['member', 'name', 'cost']].rename(columns={'name': 'facility'}).sort_values(by='cost', ascending=False)
                df_result['cost'] = df_result['cost'].astype(int)
                st.table(df_result)
                # 7
                st.write("**7. Output a list of all members, including the individual who recommended them (if any), without using any joins? "
                     "Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.**")
                code = """SELECT DISTINCT mems.firstname || ' ' ||  mems.surname as member,
                (SELECT recs.firstname || ' ' ||  recs.surname as recommender
                FROM cd.members recs 
                WHERE recs.memid = mems.recommendedby)
                FROM cd.members mems
                ORDER BY member"""
                st.code(code, language='sql')
                member_dict = df_m.set_index('memid').apply(lambda row: f"{row['firstname']} {row['surname']}", axis=1).to_dict()
                df_m['recommender'] = df_m['recommendedby'].map(member_dict)
                df_m['member'] = df_m['firstname'] + ' ' + df_m['surname']
                df_result = df_m[['member', 'recommender']].drop_duplicates().sort_values(by='member')
                st.table(df_result)
                # 8
                st.write("**8. Produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests "
                     "have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output "
                     "the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost.**")
                code = """SELECT member, facility, cost FROM (
                SELECT
  		        mems.firstname || ' ' || mems.surname as member,
  		        facs.name as facility,
  		        CASE 
  			        WHEN mems.memid = 0 THEN
  				    bks.slots*facs.guestcost
  		    	ELSE
  				    bks.slots*facs.membercost
  		        END AS cost
  		        FROM
  			    cd.members mems
  			    INNER JOIN cd.bookings bks
  				    ON mems.memid = bks.memid
  			    INNER JOIN cd.facilities facs
  				    ON facs.facid = bks.facid
  		        WHERE
  			    bks.starttime >= '2012-09-14' AND
			    bks.starttime < '2012-09-15'
                ) AS bookings
                WHERE COST > 30
                ORDER BY cost DESC
                """
                st.code(code, language='sql')
                df_m["member"] = df_m["firstname"] + " " + df_m["surname"]
                df_b["starttime"] = pd.to_datetime(df_b["starttime"])
                df_filtered = df_b[(df_b["starttime"] >= "2012-09-14") & (df_b["starttime"] < "2012-09-15")]
                df_merged = df_filtered.merge(df_m, on="memid", how="left").merge(df_f, on="facid", how="left")
                df_merged["cost"] = df_merged.apply(
                    lambda row: row["slots"] * row["guestcost"] if row["memid"] == 0 else row["slots"] * row["membercost"], axis=1
                    )
                df_result = df_merged[df_merged["cost"] > 30][["member", "name", "cost"]].rename(columns={"name": "facility"})
                df_result = df_result.sort_values(by="cost", ascending=False)
                df_result['cost'] = df_result['cost'].astype(int)
                st.table(df_result)

            elif selected == "Modifying Data":
                st.subheader("Modifying Data")
                # 1
                st.write("**1. The club is adding a new facility - a spa. You need to add it into the facilities table. Use the following values:**")
                st.markdown(""" 
                - **facid:** 9, **Name:** 'Spa', **membercost:** 20, **guestcost:** 30, **initialoutlay:** 100000, **monthlymaintenance:** 800""")
                code = """INSERT INTO cd.facilities (facid, name, membercost, 
                guestcost, initialoutlay, monthlymaintenance)
                VALUES ('9', 'Spa', '20', '30', '100000', '800')"""
                st.code(code, language='sql')
                new_facility = pd.DataFrame([{
                "facid": 9,
                "name": "Spa",
                "membercost": 20,
                "guestcost": 30,
                "initialoutlay": 100000,
                "monthlymaintenance": 800
                }])
                df_f = pd.concat([df_f, new_facility], ignore_index=True)
                st.table(df_f)
                # 2
                st.write("**2. Now add multiple facilities in one command. Use the following values:**")
                st.markdown(""" 
                - **facid:** 9, **Name:** 'Spa', **membercost:** 20, **guestcost:** 30, **initialoutlay:** 100000, **monthlymaintenance:** 800
                - **facid:** 10, **Name:** 'Squash Court 2', **membercost:** 3.5, **guestcost:** 17.5, **initialoutlay:** 5000, **monthlymaintenance:** 80""")
                code = """INSERT INTO cd.fascilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
                VALUES (9, 'Spa', 20, 30, 100000, 800),
                   (10, 'Squash Court 2', 3.5, 17.5, 5000, 80)"""
                st.code(code, language='sql')
                new_facilities = pd.DataFrame([{
                "facid": 9,
                "name": "Spa",
                "membercost": 20,
                "guestcost": 30,
                "initialoutlay": 100000,
                "monthlymaintenance": 800
                },
                {"facid": 10,
                 "name": "Squash Court 2",
                 "membercost": 3.5,
                 "guestcost": 17.5,
                 "initialoutlay": 5000,
                 "monthlymaintenance": 80
                    }])
                df_f = pd.concat([df_f, new_facilities], ignore_index=True)
                st.table(df_f)
                # 3
                st.write("**3. Add the spa to the facilities table again. This time, though, we want to automatically generate the value for the next facid, "
                     "rather than specifying it as a constant. Use the following values for everything else:**")
                st.markdown("""
                - **Name:** 'Spa', **membercost:** 20, **guestcost:** 30, **initialoutlay:** 100000, **monthlymaintenance:** 800.""")
                code = """
                INSERT INTO cd.facilities (facid, name, membercost, 
                        guestcost, initialoutlay, monthlymaintenance)
                        SELECT (SELECT max(facid) FROM cd.facilities)+1, 'Spa', '20', '30', '100000', '800'
                """
                st.code(code, language='sql')
                next_facid = df_f["facid"].max() + 1
                new_facility = pd.DataFrame([{
                "facid": next_facid,
                "name": "Spa",
                "membercost": 20,
                "guestcost": 30,
                "initialoutlay": 100000,
                "monthlymaintenance": 800
                }])
                df_f = pd.concat([df_f, new_facility], ignore_index=True)
                st.table(df_f)
                # 4
                st.write("**4. We made a mistake when entering the data for the second tennis court. The initial outlay was 10000 rather than 8000: you need to alter the data to fix the error.**")
                code = """UPDATE cd.facilities
                      SET initialoutlay = 10000
                      WHERE facid = 1"""
                st.code(code, language='sql')
                df_f.loc[df_f["facid"] == 1, "initialoutlay"] = 10000
                st.table(df_f)
                # 5
                st.write("**5. We want to increase the price of the tennis courts for both members and guests. Update the costs to be 6 for members, and 30 for guests.**")
                code = """UPDATE cd.facilities 
                SET 
                membercost = 6,
                guestcost = 30 
                WHERE facid IN (0,1)"""
                st.code(code, language='sql')
                df_f.loc[df_f["facid"].isin([0, 1]), ["membercost", "guestcost"]] = [6, 30]
                st.table(df_f)
            
            elif selected == "Aggregation":
                st.subheader("Aggregation")
                # 1
                st.write("**1. We want to know how many facilities exist - simply produce a total count.**")
                code = '''SELECT count(*) FROM cd.facilities'''
                st.code(code, language='sql')
                count_value = 9
                df = pd.DataFrame({'count': [count_value]})
                st.dataframe(df)
                # 2
                st.write("**2. Produce a count of the number of facilities that have a cost to guests of 10 or more.**")
                code = """SELECT count(*) FROM cd.facilities
                WHERE guest_cost >= 10"""
                st.code(code, language='sql')
                filtered_count = 6
                df = pd.DataFrame({'count': [filtered_count]})
                st.dataframe(df)
                # 3
                st.write("**3. Produce a count of the number of recommendations each member has made. Order by member ID.**")
                code = """SELECT recommendedby, count(*) 
                FROM cd.members 
                WHERE recommendedby IS NOT NULL
                GROUP BY recommendedby
                ORDER BY recommendedby"""
                st.code(code, language='sql')
                filtered_df = df_m[df_m['recommendedby'].notna()]
                grouped_df = filtered_df.groupby('recommendedby').size().reset_index(name='count')
                grouped_df = grouped_df.sort_values(by='recommendedby')
                st.dataframe(grouped_df)
                # 4
                st.write("**4. Produce a list of the total number of slots booked per facility. For now, just produce an output table consisting of facility id and slots, sorted by facility id.**")
                code = """SELECT facid, sum(slots) as "Total Slots" 
                FROM cd.bookings 
                GROUP BY facid 
                ORDER by facid
                """
                st.code(code, language='sql')   
                grouped_df = df_b.groupby('facid')['slots'].sum().reset_index()
                grouped_df = grouped_df.rename(columns={'slots': 'Total Slots'})
                grouped_df = grouped_df.sort_values(by='facid')
                st.dataframe(grouped_df)
                # 5
                st.write("**5. Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.**")
                code = """SELECT facid, sum(slots) as "Total Slots"
                FROM cd.bookings
                WHERE starttime >= '2012-09-01' AND starttime < '2012-10-01'
                GROUP BY facid
                ORDER BY sum(slots)"""
                st.code(code, language='sql')
                df_b['starttime'] = pd.to_datetime(df_b['starttime'])
                start_date = pd.to_datetime('2012-09-01')
                end_date = pd.to_datetime('2012-10-01')
                filtered_df = df_b[(df_b['starttime'] >= start_date) & (df_b['starttime'] < end_date)]
                grouped_df = (
                    filtered_df.groupby('facid')['slots']
                    .sum()
                    .reset_index()
                    .rename(columns={'slots': 'Total Slots'})
                    .sort_values(by='Total Slots')
                )
                st.dataframe(grouped_df)
                # 6
                st.write("**6. Produce a list of the total number of slots booked per facility per month in the year of 2012. Produce an output table consisting of facility id and slots, sorted by the id and month.**")
                code = """SELECT facid, extract(month FROM starttime) as month, sum(slots) as "Total Slots"
                FROM cd.bookings
                WHERE extract(year FROM starttime) = 2012
                GROUP BY facid, month
                ORDER BY facid, month
                """
                st.code(code, language='sql')
                df_b['starttime'] = pd.to_datetime(df_b['starttime'])
                df_2012 = df_b[df_b['starttime'].dt.year == 2012].copy()
                df_2012['month'] = df_2012['starttime'].dt.month
                grouped_df = (
                    df_2012.groupby(['facid', 'month'])['slots']
                    .sum()
                    .reset_index()
                    .rename(columns={'slots': 'Total Slots'})
                    .sort_values(by=['facid', 'month'])
                )
                st.dataframe(grouped_df)
                # 7
                st.write("**7. Find the total number of members (including guests) who have made at least one booking.**")
                code = """SELECT count(DISTINCT memid) FROM cd.bookings"""
                st.code(code, language='sql')
                unique_members = df_b['memid'].nunique()
                df_result = pd.DataFrame({'Unique Members': [unique_members]})
                st.dataframe(df_result)
                # 8
                st.write("**8. Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and slots, sorted by facility id.**")
                code = """SELECT facid, sum(slots) as "Total Slots"
                FROM cd.bookings
                GROUP BY facid
                HAVING sum(slots) > 1000
                ORDER BY facid
                """
                st.code(code, language='sql')
                grouped_df = df_b.groupby('facid')['slots'].sum().reset_index()
                filtered_df = grouped_df[grouped_df['slots'] > 1000]
                filtered_df = filtered_df.rename(columns={'slots': 'Total Slots'})
                filtered_df = filtered_df.sort_values(by='facid')
                st.dataframe(filtered_df)
                # 9
                st.write("**9. Produce a list of facilities along with their total revenue. The output table should consist of facility name and revenue, sorted by revenue. Remember that there's a different cost for guests and members!**")
                code = """SELECT facs.name, sum(slots * case
			    when memid = 0 then facs.guestcost
			    else facs.membercost
		        end) as revenue
	            FROM cd.bookings bks
	            INNER JOIN cd.facilities facs
		        ON bks.facid = facs.facid
	            GROUP BY facs.name
                    ORDER BY revenue"""
                st.code(code, language='sql')
                merged_df = pd.merge(df_b, df_f, on='facid', how='inner')
                merged_df['cost_per_slot'] = merged_df.apply(
                    lambda row: row['guestcost'] if row['memid'] == 0 else row['membercost'], axis=1
                )
                merged_df['revenue'] = merged_df['slots'] * merged_df['cost_per_slot']
                result_df = merged_df.groupby('name')['revenue'].sum().reset_index()
                result_df = result_df.sort_values(by='revenue')
                st.dataframe(result_df)
                # 10
                st.write("**10. Produce a list of facilities with a total revenue less than 1000. Produce an output table consisting of facility name and revenue, sorted by revenue. Remember that there's a different cost for guests and members!**")
                code = """SELECT name, revenue FROM (
	                SELECT facs.name, sum(case 
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			        end) AS revenue
		        FROM cd.bookings bks
		        INNER JOIN cd.facilities facs
			    ON bks.facid = facs.facid
		        GROUP BY facs.name
	                ) AS agg WHERE revenue < 1000
                        ORDER BY revenue"""
                st.code(code, language='sql')
                merged_df = pd.merge(df_b, df_f, on='facid', how='inner')
                merged_df['cost_per_slot'] = merged_df.apply(
                    lambda row: row['guestcost'] if row['memid'] == 0 else row['membercost'],
                    axis=1
                )
                merged_df['revenue'] = merged_df['slots'] * merged_df['cost_per_slot']
                agg_df = merged_df.groupby('name')['revenue'].sum().reset_index()
                filtered_df = agg_df[agg_df['revenue'] < 1000]
                filtered_df = filtered_df.sort_values(by='revenue')
                st.dataframe(filtered_df)

            elif selected == "Working with Timestamps":
                st.subheader("Working with Timestamps")
                # 1
                st.write("**1. Produce a timestamp for 1 a.m. on the 31st of August 2012.**")
                code = """SELECT timestamp '2012-08-31 01:00:00"""
                st.code(code, language='sql')
                dt = pd.to_datetime('2012-08-31 01:00:00')
                st.write("Selected timestamp:", dt)
                # 2
                st.write("**2. Find the result of subtracting the timestamp '2012-07-30 01:00:00' from the timestamp '2012-08-31 01:00:00'**")
                code = '''SELECT timestamp '2012-08-31 01:00:00' - timestamp '2012-07-30 01:00:00' as interval'''
                st.code(code, language='sql')
                dt1 = pd.to_datetime('2012-08-31 01:00:00')
                dt2 = pd.to_datetime('2012-07-30 01:00:00')
                interval = dt1 - dt2
                st.write(f"Interval between dates: {interval}")
                # 3
                st.write("**3. Produce a list of all the dates in October 2012. They can be output as a timestamp (with time set to midnight) or a date.**")
                code = '''SELECT generate_series(timestamp '2012-10-01', timestamp '2012-10-31', interval '1 day') as ts'''
                st.code(code, language='sql')
                date_range = pd.date_range(start='2012-10-01', end='2012-10-31', freq='D')
                df_dates = pd.DataFrame({'ts': date_range})
                st.dataframe(df_dates)
                # 4
                st.write("**4. Get the day of the month from the timestamp '2012-08-31' as an integer.**")
                code = '''SELECT extract(day FROM timestamp '2012-08-31')'''
                st.code(code, language='sql')
                dt = pd.to_datetime('2012-08-31')
                day = dt.day
                st.write(f"Day of the month: {day}")
                # 5
                st.write("**5. Work out the number of seconds between the timestamps '2012-08-31 01:00:00' and '2012-09-02 00:00:00'**")
                code = '''SELECT extract(epoch FROM (timestamp '2012-09-02 00:00:00' - '2012-08-31 01:00:00'))'''
                st.code(code, language='sql')
                dt1 = pd.to_datetime('2012-09-02 00:00:00')
                dt2 = pd.to_datetime('2012-08-31 01:00:00')
                diff = dt1 - dt2
                seconds = diff.total_seconds()
                st.write(f"Difference in seconds: {seconds}")
                # 6
                st.write("**6. For each month of the year in 2012, output the number of days in that month. " \
                "Format the output as an integer column containing the month of the year, and a second column containing an interval data type.**")
                code = '''SELECT extract(month from cal.month) AS month,
                        (cal.month + interval '1 month') - cal.month AS length
                        FROM
                        (
                            SELECT generate_series(timestamp '2012-01-01', timestamp '2012-12-01', interval '1 month') AS month
                        ) cal
                        ORDER BY month;'''
                st.code(code, language='sql')
                months = pd.date_range(start='2012-01-01', end='2012-12-01', freq='MS')  
                df = pd.DataFrame({'month': months})
                df['month_number'] = df['month'].dt.month
                df['length'] = (df['month'] + pd.offsets.MonthBegin(1)) - df['month']
                df['length'] = df['length'].dt.days
                st.dataframe(df[['month_number', 'length']].sort_values(by='month_number'))
                # 7
                st.write("**7. For any given timestamp, work out the number of days remaining in the month. " \
                "The current day should count as a whole day, regardless of the time. Use '2012-02-11 01:00:00' " \
                "as an example timestamp for the purposes of making the answer. Format the output as a single interval value.**")
                code = '''SELECT (date_trunc('month',ts.testts) + interval '1 month') - date_trunc('day', ts.testts) AS remaining
	                        FROM (select timestamp '2012-02-11 01:00:00' AS testts) ts  '''
                st.code(code, language='sql')
                testts = pd.to_datetime('2012-02-11 01:00:00')
                month_start = testts.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                next_month_start = month_start + pd.offsets.MonthBegin(1)
                day_start = testts.replace(hour=0, minute=0, second=0, microsecond=0)
                remaining = next_month_start - day_start
                st.write(f"Time remaining until the end of the month from the beginning of the day {testts.date()}: {remaining}")
                # 8
                st.write("**8. Return a count of bookings for each month, sorted by month**")
                code = '''SELECT date_trunc('month', starttime) as month, COUNT(*)
                            FROM cd.bookings
                            GROUP BY month
                            ORDER by month '''
                st.code(code, language='sql')
                df_b['starttime'] = pd.to_datetime(df_b['starttime'], errors='coerce')
                df_b['month'] = df_b['starttime'].dt.to_period('M').dt.to_timestamp()
                monthly_counts = df_b.groupby('month').size().reset_index(name='booking_count')
                monthly_counts = monthly_counts.sort_values(by='month')
                st.dataframe(monthly_counts)

            elif selected == "String Operations":
                st.subheader("String Operations")
                # 1
                st.write("**1. Output the names of all members, formatted as 'Surname, Firstname'**")
                code = '''SELECT surname || ', ' || firstname AS name from cd.members'''
                st.code(code, language='sql')
                df_m['name'] = df_m['surname'] + ', ' + df_m['firstname']
                st.dataframe(df_m[['name']])
                # 2
                st.write("**2. Find all facilities whose name begins with 'Tennis'. Retrieve all columns.**")
                code = '''SELECT * FROM cd.facilities WHERE name LIKE 'Tennis%'  '''
                st.code(code, language='sql')
                tennis_facilities = df_f[df_f['name'].str.startswith('Tennis', na=False)]
                st.dataframe(tennis_facilities)
                # 3
                st.write("**3. Perform a case-insensitive search to find all facilities whose name begins with 'tennis'. Retrieve all columns.**")
                code = '''SELECT * FROM cd.facilities WHERE upper(name) LIKE 'TENNIS%'; '''
                st.code(code, language='sql')
                tennis_facilities = df_f[df_f['name'].str.upper().str.startswith('TENNIS', na=False)]
                st.dataframe(tennis_facilities)
                # 4
                st.write("**4. You've noticed that the club's member table has telephone numbers with very inconsistent formatting. " \
                "You'd like to find all the telephone numbers that contain parentheses, returning the member ID and telephone number sorted by member ID.**")
                code = """SELECT memid, telephone FROM cd.members WHERE telephone ~ '[()]'"""
                st.code(code, language='sql')
                pattern = r"[()]"
                df_filtered = df_m[df_m['telephone'].str.contains(pattern, na=False, regex=True)]
                st.dataframe(df_filtered[['memid', 'telephone']])
                # 5
                st.write("**5. The zip codes in our example dataset have had leading zeroes removed from them by virtue of being stored as a numeric type. " \
                "Retrieve all zip codes from the members table, padding any zip codes less than 5 characters long with leading zeroes. Order by the new zip code.**")
                code = '''SELECT lpad(cast(zipcode as char(5)),5,'0') zip FROM cd.members ORDER BY zip'''
                st.code(code, language='sql')
                df_m['zip'] = df_m['zipcode'].astype(str).str.zfill(5)
                df_sorted = df_m.sort_values(by='zip')
                st.dataframe(df_sorted[['zip']])
                # 6
                st.write("**6. You'd like to produce a count of how many members you have whose surname starts with each letter of the alphabet. " \
                "Sort by the letter, and don't worry about printing out a letter if the count is 0.**")
                code = '''SELECT substr (mems.surname,1,1) AS letter, COUNT(*) AS count 
                            FROM cd.members mems
                            GROUP BY letter
                            ORDER BY letter'''
                st.code(code, language='sql')
                df_m['letter'] = df_m['surname'].str[0]
                letter_counts = df_m.groupby('letter').size().reset_index(name='count')
                letter_counts = letter_counts.sort_values(by='letter')
                st.dataframe(letter_counts)
                # 7
                st.write("**7. The telephone numbers in the database are very inconsistently formatted. You'd like to print a list of member " \
                "ids and numbers that have had '-','(',')', and ' ' characters removed. Order by member id.**")
                code = '''SELECT memid, translate(telephone, '-() ', '') AS telephone
                            FROM cd.members
                            ORDER BY memid;  '''
                st.code(code, language='sql')
                df_m['telephone_clean'] = df_m['telephone'].str.replace(r'[-() ]', '', regex=True)
                df_sorted = df_m.sort_values(by='memid')
                st.dataframe(df_sorted[['memid', 'telephone_clean']])

    # elif selected == "BigQuery":
        # st.write("**SQL to MongoDB**")

    elif selected == "SQLite":
        st.subheader("SQLite")
        selected_options = ["#1. Movie Insights (basics)",
                            "#2. Movie Insights (joins)",
                            "#3. Pizza Sales Analysis"]
        selected = st.selectbox("Choose a project:", options = selected_options)
        if selected == "#1. Movie Insights (basics)":
            st.subheader("Movie Insights (basics)")
            df = pd.read_csv('datasets/Movies.csv')
            st.write(df)
            st.write("**Here is a description of each column in this dataset:**")
            st.write("📌 **Id** - Unique identifier for each movie.",
                 "<br>📌 **Title** - The name of the movie.",
                 "<br>📌 **Director** - The director of the movie",
                 "<br>📌 **Year** - Year this movie was released",
                 "<br>📌 **Length_minutes** - Length of the movie in minutes",
                 unsafe_allow_html=True)
            # 1
            st.write("**1. Find a list of the names of all movies.**")
            code = """SELECT Title FROM Movies"""
            st.code(code, language='sql')
            subset_df = df["Title"]  
            st.write(subset_df)
            # 2
            st.write("2. Find the director and year of each movie.")
            code = """SELECT Title, Director, Yar FROM Movies"""
            st.code(code, language='sql')
            subset_df = df[["Title", "Director", "Year"]]
            st.write(subset_df)
            # 3
            st.write("3. Find information about each movie.")
            code = """SELECT * FROM Movies"""
            st.code(code, language='sql')
            st.write(df)
            # 4
            st.write("4. Find movie which Id is 6")
            code = """SELECT * FROM Movies WHERE Id = 6"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Id'] == 6]
            st.write(subset_df)
            # 5
            st.write("5. Find movies released from 2000 to 2010")
            code = """SELECT * FROM Movies WHERE Year BETWEEN 2000 AND 2010"""
            st.code(code, language='sql')
            subset_df = df.loc[(df['Year'] >= 2000) & (df['Year'] <= 2010)]
            subset_df = subset_df.sort_values(by='Year')
            st.write(subset_df)
            # 6
            st.write("6. Find movies which were released in 2006, 2008, 2010.")
            code = """SELECT * FROM Movies WHERE Year IN (2006, 2008, 2010)"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Year'].isin([2006, 2008, 2010])]
            st.write(subset_df)
            # 7
            st.write("7. Find movies released before 2010 (using NOT).")
            code = """SELECT Title, Director FROM Movies WHERE NOT Year >= 2010"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Year']< 2010]
            #subset_df = df[["Title", "Director", "Year"]]
            st.write(subset_df)
            # 8
            st.write("8. Find all Toy Story movies.")
            code = """SELECT * FROM Movies WHERE Title LIKE '%Toy Story%'"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Title'].str.contains('Toy Story', case=False)]
            st.write(subset_df)
            # 9
            st.write("9. Find 2 Toy Story movies in a different way.")
            code = """SELECT * FROM Movies WHERE Title LIKE '%Toy Story%' LIMIT 2"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Title'].str.contains('Toy Story', case=False)]
            subset_df = subset_df.head(2)
            st.write(subset_df)
            # 10
            st.write("10. Find all movies directed by John Lasseter.")
            code = """SELECT * FROM Movies WHERE Director = 'John Lasseter'"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Director'] == 'John Lasseter']
            st.write(subset_df)
            # 11
            st.write("11. Find all movies NOT directed by John Lasseter.")
            code = """SELECT * FROM Movies WHERE Director != 'John Lasseter'"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Director'] != 'John Lasseter']
            st.write(subset_df)
            # 12
            st.write("12. Find all WALL-* movies.")
            code = """SELECT * FROM Movies WHERE Title Like 'WALL-_'"""
            st.code(code, language='sql')
            subset_df = df.loc[df['Title'].str.contains('WALL-', case=False)]
            st.write(subset_df)
            # 13
            st.write("13. List the directors (without dubbing) in alphabetical order.")
            code = """SELECT DISTINCT Director FROM Movies ORDER BY Director ASC"""
            st.code(code, language='sql')
            subset_df = df['Director'].unique()
            subset_df.sort()
            st.write(subset_df)
            # 14
            st.write("14. List the 4 most recent movies.")
            code = """SELECT * FROM Movies ORDER BY Year DESC LIMIT 4"""
            st.code(code, language='sql')
            subset_df = df.sort_values(by='Year', ascending=False).head(4)
            st.write(subset_df)
            # 15
            st.write("15. List the 5 movies sorted alphabetically.")
            code = """SELECT * FROM Movies ORDER BY Title ASC LIMIT 5"""
            st.code(code, language='sql')
            subset_df = df.sort_values(by='Title', ascending=True).head(5)
            st.write(subset_df)
            # 16
            st.write("16. List the next 5 movies sorted alphabetically.")
            code = """SELECT * FROM Movies ORDER BY Title ASC LIMIT 5 OFFSET 5"""
            st.code(code, language='sql')
            df_sorted = df.sort_values(by='Title', ascending=True)
            subset_df = df_sorted.iloc[5:10]
            st.write(subset_df)
            
        elif selected == "#2. Movie Insights (joins)":
            st.subheader("Movie Insights (joins)")
            df_m = pd.read_csv('datasets/Movies.csv')
            df_bf = pd.read_csv('datasets/Boxoffice.csv')
            df_e = pd.read_csv('datasets/Employees.csv')
            df_b = pd.read_csv('datasets/Buildings.csv')
            # Розміщення у два стовпчики
            col1, col2 = st.columns(2)
            # === LEFT COLUMN ===
            with col1:
                st.subheader("Movies Table")
                st.dataframe(df_m)
                st.markdown("**Description of each column:**")
                st.markdown(
                    """
                    - **Id**: Unique identifier for each movie  
                    - **Title**: The name of the movie  
                    - **Director**: The director of the movie  
                    - **Year**: Year the movie was released  
                    - **Length_minutes**: Length of the movie in minutes
                    """
                )
                st.markdown("---")

                st.subheader("Employees Table")
                st.dataframe(df_e)
                st.markdown("**Description of each column:**")
                st.markdown(
                    """
                    - **Role**: Job title of the employee  
                    - **Name**: Full name of the employee  
                    - **Building**: Building where the employee works  
                    - **Years_employed**: Number of years the employee has worked
                    """
                )
            # === RIGHT COLUMN ===
            with col2:
                st.subheader("Boxoffice Table")
                st.dataframe(df_bf)
                st.markdown("**Description of each column:**")
                st.markdown(
                    """
                    <ul>
                        <li style="color: black;"><b>Movie_id</b>: Unique identifier for each movie</li>
                        <li style="color: black;"><b>Rating</b>: Viewer rating (e.g., PG, R)</li>
                        <li style="color: black;"><b>Domestic_sales</b>: Revenue from local markets</li>
                        <li style="color: black;"><b>International_sales</b>: Revenue from international markets</li>
                        <li style="color: white;"><b></b></li>
                    </ul>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("---")

                st.subheader("Buildings Table")
                st.dataframe(df_b)
                st.markdown("**Description of each column:**")
                st.markdown(
                    """
                    <ul>
                        <li style="color: black;"><b>Building_names</b>: Name of the building</li>
                        <li style="color: black;"><b>Capacity</b>: Maximum number of people it can accommodate</li>
                    </ul>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("---")
            # 1
            st.write("1. Find the domestic and international sales for each movie.")
            code = """SELECT Title, Domestic_sales, International_sales FROM Movies INNER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id"""
            st.code(code, language='sql')
            sales_df = pd.merge(df_m, df_bf, left_on='Id', right_on='Movie_id')
            sales_df = sales_df[['Title', 'Domestic_sales', 'International_sales']]
            st.dataframe(sales_df)
            # 2
            st.write("2. Display all movies with their ratings in descending order.")
            code = """SELECT Title, Rating FROM Movies INNER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id ORDER BY Rating DESC"""
            st.code(code, language='sql')
            df2 = pd.merge(df_m, df_bf, left_on='Id', right_on='Movie_id')
            df2 = df2[['Title', 'Rating']].sort_values(by='Rating', ascending=False)
            st.dataframe(df2)
            # 3
            st.write("3. Display a list of buildings and people who live in those buildings with their occupations.")
            code = """SELECT Role, Name, Building FROM Employees WHERE Building IS NOT ''"""
            st.code(code, language='sql')
            df3 = df_e[df_e['Building'].notna()]
            st.dataframe(df3[['Role', 'Name', 'Building']])
            # 4
            st.write("4. Display a list of people and their occupations that are not attached to buildings.")
            code = """SELECT Role, Name FROM Employees WHERE Building IS ''"""
            st.code(code, language='sql')
            df4 = df_e[df_e['Building'].isna()]
            st.dataframe(df4[['Role', 'Name']])
            # 5
            st.write("5. Display all movie titles and their total box office in dollars.")
            code = """SELECT Title, (Domestic_sales + International_sales) AS Total_sales FROM Movies INNER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id"""
            st.code(code, language='sql')
            df5 = pd.merge(df_m, df_bf, left_on='Id', right_on='Movie_id')
            df5['Total_sales'] = df5['Domestic_sales'] + df5['International_sales']
            st.dataframe(df5[['Title', 'Total_sales']])

        elif selected == "#3. Pizza Sales Analysis":
            # page settings
            page = st.sidebar.selectbox('Choose a page:',
                                            ['Main Info',
                                            'Tables Closer',
                                            'SQL Code',
                                            'Findings'])
            if page == 'Main Info':
                st.subheader("Pizza Sales Analysis")
                st.write('**On the side bar choose the page on which you can focus)**')
                st.subheader("Dataset Overview")
                st.markdown("""
                        Dataset contains valuable information that could help restaurant optimize their operations, 
                        boost sales, and enhance customer satisfaction. Here's a quick rundown of what you can expect from the dataset:

                        - **Date and Time:** The author has meticulously recorded the date and time of each order, allowing to analyze 
                        customer behavior and identify potential peak hours.
                        - **Pizza Details:** Each entry includes comprehensive details about the pizzas ordered, including their types, 
                        sizes, quantities, prices, and the tantalizing ingredients that create an unforgettable culinary experience.
                        """)
                st.subheader("Main Points")
                st.markdown("""
                            1. **Customer Traffic Analysis:** Uncovering how many customers visits each day and exploring whether certain 
                            times of day experience higher footfall.
                            2. **Bestselling Pizzas:** Analyzing the data to find out which pizzas are the most popular among the customers. 
                            Identifying bestsellers can inform restaurant's marketing strategies and help focus on promoting crowd favorites.
                            3. **Revenue and Seasonality:** Calculating the total revenue generated over the year to get an overall picture 
                            of the financial performance. Additionally, investigating whether there are any seasonal patterns in sales to plan 
                            for peak and slow periods.
                            4. **Menu Optimization and Promotions:** Using the data to identify pizzas that are underperforming or receiving 
                            little attention.""")
                st.write("**We have 4 tables with the important information. Here we can see the explanation of each column in each table 👇🏻**")
                df = pd.read_csv('datasets/data_dictionary.csv')
                st.write(df)
            
            elif page == 'Tables Closer':
                st.subheader("Table Description")
                st.subheader("Pizzas")
                df_p = pd.read_csv('datasets/pizzas.csv')
                st.write(df_p)
                st.write("**Here is a description of each column in this dataset:**")
                st.write("📌 **pizza_id** - Unique identifier for each pizza variant (includes type and size).",
                    "<br>📌 **pizza_type_id** - Identifies the pizza type or flavor, without size.",
                    "<br>📌 **size** - Indicates pizza size.",
                    "<br>📌 **price** - Price of the pizza for the given size (in USD).",
                    unsafe_allow_html=True)
                
                st.subheader("Pizza Types")
                df_p_t = pd.read_csv('datasets/pizza_types.csv', encoding='latin1')
                st.write(df_p_t)
                st.write("**Here is a description of each column in this dataset:**")
                st.write("📌 **pizza_type_id** - A unique identifier for each type of pizza (used as a key to link with other datasets).",
                    "<br>📌 **name** - The full name of the pizza type.",
                    "<br>📌 **category** - The category of the pizza, usually based on the main ingredient or style.",
                    "<br>📌 **ingredients** - A comma-separated list of ingredients used in that pizza.",
                    unsafe_allow_html=True)
                
                st.subheader("Order Details")
                df_o_d = pd.read_csv('datasets/order_details.csv', encoding='latin1')
                st.write(df_p_t)
                st.write("**Here is a description of each column in this dataset:**")
                st.write("📌 **pizza_type_id** - A unique identifier for the pizza type (used for joining with other tables).",
                    "<br>📌 **name** - The full name of the pizza type.",
                    "<br>📌 **category** - Category of the pizza based on style or main ingredient.",
                    "<br>📌 **ingredients** - List of ingredients in the pizza, separated by commas.",
                    "<br>📌 **Length_minutes** - Length of the movie in minutes",
                    unsafe_allow_html=True)
                
                st.subheader("Orders")
                df_p_t = pd.read_csv('datasets/orders.csv', encoding='latin1')
                st.write(df_p_t)
                st.write("**Here is a description of each column in this dataset:**")
                st.write("📌 **order_id** - Unique identifier for each customer order.",
                    "<br>📌 **date** - The date when the order was placed, in YYYY-MM-DD format.",
                    "<br>📌 **time** - The time the order was placed, in HH : MM : SS format.", 
                    unsafe_allow_html=True)  

                st.subheader("Pizza Sales")
                df_p_s = pd.read_csv('datasets/pizza_sales.csv', encoding='latin1') 
                st.write(df_p_s)
                st.write("**Here is a description of each column in this dataset:**")
                st.write("📌 **pizza_id** - Unique identifier for a specific pizza item in the dataset (often links to pizza details).",
                    "<br>📌 **order_id** - Unique identifier for a customer order (groups multiple pizzas under one order).",
                    "<br>📌 **pizza_name_id** - Identifier for the pizza type, without size.", 
                    "<br>📌 **quantity** - Number of units of this pizza in the order.", 
                    "<br>📌 **order_date** - Date when the order was placed, typically in YYYY-MM-DD format.", 
                    "<br>📌 **order_time** - Time when the order was placed, typically in HH:MM:SS format.", 
                    "<br>📌 **unit_price** - Price of a single pizza unit (in USD).", 
                    "<br>📌 **total_price** - Total price for that line item (unit_price * quantity).", 
                    "<br>📌 **pizza_size** - Size of the pizza (S, M, L, XL, XXL).", 
                    "<br>📌 **pizza_category** - Category of the pizza (e.g., Chicken, Classic, Veggie).", 
                    "<br>📌 **pizza_ingredients** - List of ingredients used in the pizza.", 
                    "<br>📌 **pizza_name** - Full name of the pizza type.", 
                    unsafe_allow_html=True) 

            elif page == 'SQL Code':
                st.subheader("A. KPI's (Key Performance Indicators).")
                # 1
                df_p_s = pd.read_csv('datasets/pizza_sales.csv', encoding='latin1') 
                st.write("**1. Total Revenue:**")
                code = """
                SELECT 
                    SUM(total_price) AS total_revenue
                FROM 
                    pizza_sales;"""
                st.code(code, language='sql')
                total_revenue = df_p_s['total_price'].sum()
                st.metric(label="", value=f"${total_revenue:,.2f}")
                # 2
                st.write("**2. Average Order Value:**")
                code = """
                SELECT 
                    SUM(total_price) / COUNT (DISTINCT order_id) AS AVG_Order_Value
                FROM 
                    pizza_sales;"""
                st.code(code, language='sql')
                total_revenue = df_p_s['total_price'].sum()
                total_orders = df_p_s['order_id'].nunique() 
                avg_order_value = total_revenue / total_orders
                st.metric(label="", value=f"${avg_order_value:,.16f}")
                # 3
                st.write("**3. Total Pizza Sold:**")
                code = """
                SELECT 
                    SUM(quantity) AS Total_Pizza_Sold
                FROM 
                    pizza_sales;"""
                st.code(code, language='sql')
                total_pizza_sold = df_p_s['quantity'].sum()
                st.metric(label="", value=f"{total_pizza_sold:,}")
                # 4
                st.write("**4. Total Orders**")
                code = """
                SELECT
                    COUNT(DISTINCT order_id) AS Total_Orders
                FROM
                    pizza_sales;"""
                st.code(code, language='sql')
                total_orders = df_p_s['order_id'].nunique()
                st.metric(label="", value=f"{total_orders:,}")
                # 5
                st.write("**5. Average Pizzas Per Orders**")
                code = """
                SELECT
                    ROUND(
                        ROUND(SUM(quantity),2) / ROUND(COUNT(DISTINCT order_id),2),2) AS Average_pizza_per_order
                FROM
                    pizza_sales;"""
                st.code(code, language='sql')
                total_pizzas = df_p_s['quantity'].sum()
                total_orders = df_p_s['order_id'].nunique()
                avg_pizza_per_order = total_pizzas / total_orders
                st.metric(label="", value=f"{avg_pizza_per_order:.2f}")
                st.subheader("B. Daily Trend for Total Orders.")
                # 6
                code = """
                SELECT
                    TO_CHAR(order_date, 'Day') AS order_day,
                    COUNT(DISTINCT order_id) AS Total_Orders
                FROM
                    pizza_sales
                GROUP BY
                    order_day
                ORDER BY
                    Total_Orders DESC;"""
                st.code(code, language='sql')
                df_p_s['order_date'] = pd.to_datetime(df_p_s['order_date'], dayfirst=True)
                orders_by_day = (
                    df_p_s.groupby(df_p_s['order_date'].dt.day_name())['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_id': 'Total_Orders', 'order_date': 'order_day'})
                    .sort_values(by='Total_Orders', ascending=False)
                )
                st.dataframe(orders_by_day)
                # 7
                st.subheader("C. Monthly Trend for Total Orders.")
                code = """
                SELECT
                    TO_CHAR(order_date, 'Month') AS Month_Name,
                    COUNT(DISTINCT order_id) AS Total_Orders
                FROM
                    pizza_sales
                GROUP BY
                    Month_Name
                ORDER BY
                    Total_Orders DESC;"""
                st.code(code, language='sql')
                df_p_s['order_date'] = pd.to_datetime(df_p_s['order_date'], dayfirst=True)
                monthly_orders = (
                    df_p_s.groupby(df_p_s['order_date'].dt.month_name())['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_date': 'Month_Name', 'order_id': 'Total_Orders'})
                )
                monthly_orders = monthly_orders.sort_values(by='Total_Orders', ascending=False)
                st.dataframe(monthly_orders)
                # 8
                st.subheader("D. % of Sales by Pizza Category.")
                code = """
                SELECT
                    pizza_category,
                    ROUND(SUM(total_price) *100 / (SELECT SUM(total_price)
                        FROM pizza_sales),2) AS percent_of_Sales
                FROM
                    pizza_sales
                GROUP BY
                    pizza_category;"""
                st.code(code, language='sql')
                sales_by_category = (
                    df_p_s.groupby('pizza_category')['total_price']
                    .sum()
                    .reset_index()
                )
                total_sales = sales_by_category['total_price'].sum()
                sales_by_category['percent_of_Sales'] = round((sales_by_category['total_price'] / total_sales) * 100, 2)
                sales_by_category = sales_by_category[['pizza_category', 'percent_of_Sales']]
                sales_by_category = sales_by_category.sort_values(by='percent_of_Sales', ascending=False)
                st.dataframe(sales_by_category)
                # 9
                st.subheader("E. % of Sales by Pizza Size.")
                code = """
                SELECT
                    pizza_size,
                    ROUND(SUM(total_price)*100 / (SELECT SUM(total_price)
                        FROM pizza_sales),2) AS percent_of_sales
                FROM
                    pizza_sales
                GROUP BY
                    pizza_size
                ORDER BY
                    percent_of_sales DESC;"""
                st.code(code, language='sql')
                sales_by_size = (
                    df_p_s.groupby('pizza_size')['total_price']
                    .sum()
                    .reset_index()
                )
                total_sales = sales_by_size['total_price'].sum()
                sales_by_size['percent_of_sales'] = round((sales_by_size['total_price'] / total_sales) * 100, 2)
                sales_by_size = sales_by_size[['pizza_size', 'percent_of_sales']]
                sales_by_size = sales_by_size.sort_values(by='percent_of_sales', ascending=False)
                st.dataframe(sales_by_size)
                # 10
                st.subheader("F. Top 5 Best Sellers by Revenue, Total Quantity & Total Orders.")
                st.write("**1. Top 5 Best Sellers by Revenue**")
                code = """
                SELECT
                    pizza_name, SUM(total_price) AS Total_Revenue
                FROM
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Revenue DESC
                LIMIT 5;"""
                st.code(code, language='sql')
                top5_revenue = (
                    df_p_s.groupby('pizza_name')['total_price']
                    .sum()
                    .reset_index()
                    .rename(columns={'total_price': 'Total_Revenue'})
                    .sort_values(by='Total_Revenue', ascending=False)
                    .head(5)
                )
                st.dataframe(top5_revenue)
                # 11
                st.write("**2. Bottom 5 Sellers by Revenue**")
                code = """
                SELECT
                    pizza_name, SUM(total_price) AS Total_Revenue
                FROM
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Revenue 
                LIMIT 5;"""
                st.code(code, language='sql')
                bottom5_revenue = (
                    df_p_s.groupby('pizza_name')['total_price']
                    .sum()
                    .reset_index()
                    .rename(columns={'total_price': 'Total_Revenue'})
                    .sort_values(by='Total_Revenue', ascending=True)
                    .head(5)
                )
                st.dataframe(bottom5_revenue)
                # 12
                st.write("**3. Top 5 Best Sellers by Quantity**")
                code = """
                SELECT
                    pizza_name, SUM(quantity) AS Total_Quantity
                FROM 
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Quantity DESC
                LIMIT 5;"""
                st.code(code, language='sql')
                top5_quantity = (
                    df_p_s.groupby('pizza_name')['quantity']
                    .sum()
                    .reset_index()
                    .rename(columns={'quantity': 'Total_Quantity'})
                    .sort_values(by='Total_Quantity', ascending=False)
                    .head(5)
                )
                st.dataframe(top5_quantity)
                # 13
                st.write("**4. Bottom 5 Sellers by Revenue**")
                code = """
                SELECT
                    pizza_name, SUM(quantity) AS Total_Quantity
                FROM
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Quantity
                LIMIT 5;"""
                st.code(code, language='sql')
                bottom5_quantity = (
                    df_p_s.groupby('pizza_name')['quantity']
                    .sum()
                    .reset_index()
                    .rename(columns={'quantity': 'Total_Quantity'})
                    .sort_values(by='Total_Quantity', ascending=True)
                    .head(5)
                )
                st.dataframe(bottom5_quantity)
                # 14
                st.write("**5. Top 5 Best Sellers by Total Orders**")
                code = """
                SELECT
                    pizza_name, COUNT(DISTINCT order_id) AS Total_Orders
                FROM
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Orders DESC
                LIMIT 5;"""
                st.code(code, language='sql')
                top5_orders = (
                    df_p_s.groupby('pizza_name')['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_id': 'Total_Orders'})
                    .sort_values(by='Total_Orders', ascending=False)
                    .head(5)
                )
                st.dataframe(top5_orders)
                # 15
                st.write("**6. Bottom 5 Sellers by Total Orders**")
                code = """
                SELECT
                    pizza_name, COUNT(DISTINCT order_id) AS Total_Orders
                FROM
                    pizza_sales
                GROUP BY
                    pizza_name
                ORDER BY
                    Total_Orders
                LIMIT 5;"""
                st.code(code, language='sql')
                bottom5_orders = (
                    df_p_s.groupby('pizza_name')['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_id': 'Total_Orders'})
                    .sort_values(by='Total_Orders', ascending=True)
                    .head(5)
                )
                st.dataframe(bottom5_orders)
                # 16
                st.subheader("G. Number of Customers each day & Busiest hours.")
                code = """
                SELECT 
                    order_date,
                    COUNT(DISTINCT order_id) AS num_customers
                FROM
                    pizza_sales
                GROUP BY
                    order_date
                ORDER BY
                    order_date;"""
                st.code(code, language='sql')
                code = """
                SELECT
                    EXTRACT(HOUR FROM order_time) AS order_hour,
                    COUNT(DISTINCT order_id) AS num_orders
                FROM
                    pizza_sales
                GROUP BY
                    order_hour
                ORDER BY
                    num_orders DESC;"""
                st.code(code, language='sql')
                df_p_s['order_hour'] = pd.to_datetime(df_p_s['order_time'], format='%H:%M:%S').dt.hour
                orders_per_hour = (
                    df_p_s.groupby('order_hour')['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_id': 'num_orders'})
                    .sort_values(by='num_orders', ascending=False)
                )
                st.dataframe(orders_per_hour)
                # 17
                st.subheader("H. Seasonality Trends.")
                code = """
                SELECT
                    EXTRACT(MONTH FROM order_date) AS month,
                    COUNT(DISTINCT order_id) AS total_orders
                FROM
                    pizza_sales
                GROUP BY
                    month
                ORDER BY
                    month;"""
                st.code(code, language='sql')
                df_p_s['order_date'] = pd.to_datetime(df_p_s['order_date'], dayfirst=True)
                seasonality = (
                    df_p_s.groupby(df_p_s['order_date'].dt.month)['order_id']
                    .nunique()
                    .reset_index()
                    .rename(columns={'order_date': 'month', 'order_id': 'total_orders'})
                )
                month_map = {
                    1: "January", 2: "February", 3: "March", 4: "April",
                    5: "May", 6: "June", 7: "July", 8: "August",
                    9: "September", 10: "October", 11: "November", 12: "December"
                }
                seasonality['month'] = seasonality['month'].map(month_map)
                st.dataframe(seasonality)
                # 18
                st.subheader("I. Average Orders per Day.")
                code = """
                WITH daily_orders AS (
                    SELECT
                        order_date,
                        COUNT(DISTINCT order_id) AS daily_order_count
                    FROM
                        pizza_sales
                    GROUP BY
                        order_date)
                    SELECT
                        AVG(daily_order_count) AS avg_orders_per_day
                    FROM
                        daily_orders;"""
                st.code(code, language='sql')
                df_p_s['order_date'] = pd.to_datetime(df_p_s['order_date'], dayfirst=True)
                daily_orders = df_p_s.groupby('order_date')['order_id'].nunique()
                avg_orders_per_day = daily_orders.mean()
                st.metric(label="", value=f"{avg_orders_per_day:.16f}")
                # 19
                st.subheader("J. Average Pizza Per Day sold.")
                code = """
                WITH avg_pizza as(
                    SELECT order_date,
                        COUNT(quantity) as daily_pizza
                    FROM pizza_sales
                    GROUP BY order_date
                )
                SELECT
                    AVG(daily_pizza) AS AVG_PIZZA_PER_DAY
                FROM avg_pizza;"""
                st.code(code, language='sql')
                df_p_s['order_date'] = pd.to_datetime(df_p_s['order_date'], dayfirst=True)
                daily_pizza = df_p_s.groupby('order_date')['quantity'].sum()
                avg_pizza_per_day = daily_pizza.mean()
                st.metric(label="", value=f"{avg_pizza_per_day:.16f}")
            
            elif page == 'Findings':
                st.subheader("Summary of Findings")
                st.markdown("""
                            - **Most occupied Days & Month:**
                               
                                **Days**-Orders are highest on Friday & Saturday evenings
                                
                                **Month**-Orders are highest on January & July
                            
                            - **Sales Performance:**
                                
                                **Category**-Classical contributes maximum to Sales & Total Orders
                                
                                **Size**-Large pizza contributes maximum to Sales
                            
                            - **Best Sellers:**
                                
                                **Revenue**-Thai Chicken Pizza contribute maximum to Revenue
                                
                                **Quantity**-Classical Deluxe Pizza contributes maximum to Total Quantities
                                
                                **Total Orders**-Classic Deluxe Pizza contributes maximum to Total Orders
                            
                            - **Lowest Sellers:**
                                
                                **Revenue**-Brie Carre Pizza contribute minimum to Revenue
                                
                                **Quantity**-Brie Carre Pizza contribute minimum to Total Quantities
                                
                                **Total Orders**-Brie Carre Pizza contribute minimum to Total Orders
                            
                            - **Most occupied Time:**
                                
                                **Lunch**-12 P.M. - 1:30 P.M.
                                
                                **Dinner**-6 P.M. - 8 P.M.""")

# PYTHON
if selected == 'Python':
    st.markdown("<h1 style='text-align: center;'>Python</h1>", unsafe_allow_html=True)
    st.markdown("""
                Welcome to the **Python** section of my portfolio!

                This collection showcases the projects I developed during my university studies. 
                They range from beginner-level tasks to more complex applications — 
                each one marking a step in my learning journey and personal growth as a developer.
                """)
    selected_options = ["Simple calculator", 
                        "Virtual Wallet",
                        "Fictional Person", 
                        "EDA TMDb Movie Dataset", 
                        "Regular Expressions"]
    selected = st.selectbox("Feel free to explore and click on any project to learn more and see the code 👇", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Simple calculator":
        st.subheader("Simple calculator :)")
        python_code = """import math 

def add(x, y):
    return (x + y)
        
def subtract(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)

def divide(x, y):
    return (x / y)

def degree(x):
    return (math.pow(x, 2))

def degree_1(x, y):
    return (math.pow(x, y))

def sin(x):
    return (math.sin(x))

def cos(x):
    return (math.cos(x))

print('Select operation: \n1.Add \n2.Substract \n3.Multiply \n4.Divide \n5.Square \n6.To the power of \n7.sin \n8.cos \n9.Exit
')

while True:
    choice = input('Choose operation(1/2/3/4/5/6/7/8/9)')
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        try:
            num1 = int(input('Enter first number:'))
            num2 = int(input('Enter second number:'))
        except ValueError:
            print('Enter please a number!')

        if choice == '1':
           print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                break
            print(divide(num1, num2))

        elif choice == '5':
            print(math.pow(num1, 2))

        elif choice == '6':
            print(math.pow(num1, num2))

        elif choice == '7':
            print(math.sin(num1))

        elif choice == '8':
            print(math.cos(num1))

    if choice in ('9'):
        try:
            print('Thank you :)')
            exit()
        except ValueError:
            print('Enter please a number!')"""
        st.code(python_code, language='python')
        import math 

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            if y == 0:
                return "❌ Division by zero!"
            return x / y

        def square(x):
            return math.pow(x, 2)

        def power(x, y):
            return math.pow(x, y)

        def sin(x):
            return math.sin(x)

        def cos(x):
            return math.cos(x)
        st.subheader("🧮 That Simple Calculator")
        operation = st.selectbox("Choose operation:", [
            "Add", "Subtract", "Multiply", "Divide",
            "Square", "Power", "Sine", "Cosine"
            ])
        num1 = st.number_input("Enter first number:", format="%.0f")
        need_second = operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]
        if need_second:
            num2 = st.number_input("Enter second number:", format="%.0f")
        if st.button("Calculate"):
            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
            elif operation == "Square":
                result = square(num1)
            elif operation == "Power":
                result = power(num1, num2)
            elif operation == "Sine":
                result = sin(num1)
            elif operation == "Cosine":
                result = cos(num1)
            else:
                result = "Unknown operation"
    
        if 'result' in locals() and result is not None:
            st.success(f"Result: {result}")

    elif selected == "Virtual Wallet":
        st.subheader("Virtual Wallet: A Person Class with Balance Control")
        python_code = """class Person():
        def __init__(self, name, gender, mood):
        self.name = name
        self.gender = gender
        self.mood = mood
        self.__cash = 0

    def get_balance(self):
        return self.__cash

    def insert(self, x):
        self.__cash += x

    def payment(self, x):
        self.__cash -= x

    def check(self):
        if self.gender == 'хлопець':
            print('Мене звати ' + self.name + '. ' + 'Я - прикольний '
              + self.gender + '. ' + 'У мене ' + self.mood + ' настрій.')
        else:
            print('Мене звати ' + self.name + '. ' + 'Я - прикольна '
                  + self.gender + '. ' + 'У мене ' + self.mood + ' настрій.')

    #def __del__(self):
     #   print('Видалення ' + str(self))


Person1 = Person(input('Імя: '), input('Стать: '), input('Настрій: '))
Person1.check()

print('Оберіть дію: \n1.Поповнення \n2.Оплата \n3.Залишок на рахунку')

while True:
    choice = input('Оберіть значення(1/2/3) ')

    if choice == '1':
        x = int(input('Поповнити на: '))
        Person1.insert(x)

    elif choice == '2':
        y = int(input('Оплатити: '))
        if y > Person1.get_balance():
            print('Недостатньо грошей!')
        else:
            Person1.payment(y)

    else:
        print('Ваш баланс:', Person1.get_balance())"""
        st.code(python_code, language='python')
        st.subheader("🧍🏻‍♀️ Create Your Person")

        class Person:
            def __init__(self, name, gender, mood):
                self.name = name
                self.gender = gender
                self.mood = mood
                self.__cash = 0

            def get_balance(self):
                return self.__cash

            def insert(self, x):
                self.__cash += x

            def payment(self, x):
                self.__cash -= x

            def check(self):
                if self.gender.lower() == 'boy':
                    return f"My name is {self.name}. I am a cool {self.gender}, and right now I have {self.mood} mood."
                else:
                    return f"My name is {self.name}. I am a cool {self.gender}, and right now I have {self.mood} mood."

        if 'person' not in st.session_state:
            with st.form("user_form"):
                name = st.text_input("Name:")
                gender = st.selectbox("Gender:", ["boy", "girl"])
                mood = st.text_input("Mood:")
                submitted = st.form_submit_button("Create")

                if submitted:
                    st.session_state.person = Person(name, gender, mood)
                    st.success("The object has been created!")

        if 'person' in st.session_state:
            person = st.session_state.person
            st.info(person.check())

            action = st.radio("Choose the option:", ["Top-up", "Payment", "View balance"])

            if action == "Top-up":
                amount = st.number_input("Top-up amount:", min_value=0, step=1)
                if st.button("Continue"):
                    person.insert(amount)
                    st.success(f"Your balance has been successfully topped up with ${amount}")

            elif action == "Payment":
                amount = st.number_input("Payment amount:", min_value=0, step=1)
                if st.button("Continue"):
                    if amount > person.get_balance():
                        st.error("Not enough money!")
                    else:
                        person.payment(amount)
                        st.success(f"Payment of ${amount} was successful.")

            elif action == "View balance":
                st.write(f"Your currnet balance is ${person.get_balance()}.")

    elif selected == "Fictional Person":
        st.subheader("FictionalPersona: Interactive Life Simulator")
        python_code = """import random

import fictional
person = fictional.FictionalPerson

class MyDay():
    def __init__(self, person):
        self.person = person
        self.events = self.generate_events()

    def generate_events(self):
        events = []
        wakeup_time = random.randint(5, 7)
        events.append(f'{self.person.name} wakes up at {wakeup_time}:45 am')    
        breakfast_choices = ['cereal', 'toast', 'eggs', 'smoothie']
        breakfast = random.choice(breakfast_choices)
        events.append(f'{self.person.name} has {breakfast} for breakfast')  
        work_start_time = random.randint(9, 11)
        events.append(f'{self.person.name} starts work at {work_start_time}:30 am')   
        if work_start_time == 11:
            movie_choices = ['1+1', 'All Quiet on the Western Front', "Don't Look Up"]
            movie = random.choice(movie_choices)
            events.append(f'{self.person.name} watches {movie}') 
        else:
            tv_shows_choices = ['Breaking Bad', 'Supernatural', 'You']
            tv_show = random.choice(tv_shows_choices)
            events.append(f'{self.person.name} watches {tv_show}')  
        bedtime = random.randint(00, 2)
        events.append(f'{self.person.name} goes to bed at {bedtime}:00 pm')  
        return events

    def describe_day(self):
        print(f"{self.person.name}'s day:")
        for event in self.events:
            print('- ' + event)

person1 = fictional.FictionalPerson('Jane', 25, 'neutral', 5, 80, 5)
my_day = MyDay(person1)
my_day.describe_day()"""
        st.code(python_code, language='python')       
        # === Базовий клас ===
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        # === Розширений клас FictionalPerson ===
        class FictionalPerson(Person):
            def __init__(self, name, age, mood, reaction, heart_beats, energy):
                super().__init__(name, age)
                self.mood = mood
                self.reaction = reaction
                self.heart_beats = heart_beats
                self.energy = energy

            def coffee_cup(self):
                self.mood = 'happier than before'
                self.reaction += 5
                self.heart_beats += 10
                return "After coffee, mood: {}, reaction: {}, heart beats: {}".format(
                    self.mood, self.reaction, self.heart_beats
                )

            def music_listening(self):
                self.mood = 'happier than ever'
                self.reaction -= 2
                self.energy += 5
                return f"After music, mood: {self.mood}, reaction: {self.reaction}, energy: {self.energy}"

            def have_a_date(self):
                self.mood = 'excited'
                self.heart_beats += 30
                return f"On a date! Mood: {self.mood}, heart beats: {self.heart_beats}"

            def shower(self):
                self.energy -= 2
                return f"Took a shower. Energy: {self.energy}. Feeling fresh!"

            def celebrate_birthday(self):
                self.age += 1
                return f"{self.name} is now {self.age} years old! 🎉"

        # === Генератор подій дня ===
        class MyDay:
            def __init__(self, person):
                self.person = person
                self.events = self.generate_events()

            def generate_events(self):
                events = []
                wakeup_time = random.randint(5, 7)
                events.append(f'{self.person.name} wakes up at {wakeup_time}:45 am')

                breakfast = random.choice(['cereal', 'toast', 'eggs', 'smoothie'])
                events.append(f'{self.person.name} has {breakfast} for breakfast')

                work_start = random.randint(9, 11)
                events.append(f'{self.person.name} starts work at {work_start}:30 am')

                if work_start == 11:
                    movie = random.choice(['1+1', 'All Quiet on the Western Front', "Don't Look Up"])
                    events.append(f'{self.person.name} watches {movie}')
                else:
                    tv_show = random.choice(['Breaking Bad', 'Supernatural', 'You'])
                    events.append(f'{self.person.name} watches {tv_show}')

                bedtime = random.randint(0, 2)
                events.append(f'{self.person.name} goes to bed at {bedtime}:00 pm')
                return events

            def describe_day(self):
                return self.events

        # === STREAMLIT APP ===
        st.markdown("Meet Jane, a fictional person whose day you get to explore. " \
        "From waking up and choosing breakfast to working and relaxing with shows or movies, " \
        "every moment shapes her mood, energy, and reactions. This project brings Jane’s life to life " \
        "through code — showing how little events like drinking coffee or taking a shower change her " \
        "feelings and energy throughout the day.")

        # Ініціалізація персонажа у session_state
        if "person" not in st.session_state:
            st.session_state.person = FictionalPerson('Jane', 25, 'neutral', 5, 80, 5)

        person = st.session_state.person

        # Симуляція дня
        st.subheader("Create Jane's Day")
        if st.button("generate"):
            my_day = MyDay(person)
            for event in my_day.describe_day():
                st.write("- " + event)

        # Кнопки дій
        st.subheader("Daily Activities (choose 'celebrate birthday')")
        if st.button("drink coffee"):
            st.success(person.coffee_cup())

        if st.button("listen to music"):
            st.success(person.music_listening())

        if st.button("go on a date"):
            st.success(person.have_a_date())

        if st.button("take a shower"):
            st.success(person.shower())

        if st.button("celebrate birthday"):
            st.balloons()
            st.success(person.celebrate_birthday())

        # Показати поточний стан
        st.subheader("🧠 Current Status")
        st.write(f"Name: {person.name}")
        st.write(f"Age: {person.age}")
        st.write(f"Mood: {person.mood}")
        st.write(f"Reaction: {person.reaction}")
        st.write(f"Heart Beats: {person.heart_beats}")
        st.write(f"Energy: {person.energy}")

    elif selected == "EDA TMDb Movie Dataset":
        st.markdown("""
                    **A bucket of popcorn and a cozy blanket, that’s my perfect movie night...** 🎬🍿
                
                    But choosing which movie to watch is always a tricky decision. For this, I often 
                    turn to TMDb – one of the world’s most popular and community-driven movie databases. 
                    From ratings to reviews, it provides a vast collection of insights into the film industry.  
                    
                    Being a movie enthusiast, I decided to dive deeper into this dataset. This project focuses 
                    on performing Exploratory Data Analysis (EDA) on the TMDb Movie Dataset 
                    to uncover trends, patterns, and interesting facts about movies and the global cinema world.
                    """)
        selected_options = [
            "1. Project overview",
            "2. Data Wrangling",
            "3. Exploratory Data Analysis",
            "4. Conclusions"
            ]
        selected = st.selectbox("Let's begin. To make it easier to understand, I divided this project into several sections 👇🏻", options = selected_options)
        st.write("Current selection:", selected)
        if selected == "1. Project overview":
            st.title("1. Project Overview")
            st.markdown("""The main objective of this project is to analyze a dataset containing information about 10,000 movies 
                        from 1960 to 2015, collected from The Movie Database (TMDb) and including all films details such as the 
                        production cost, the revenue generated, rating information, actors and directors, etc. You can ckeck the whole dataset and I will 
                        try to answer to the questions below...""")
            df = pd.read_csv('datasets/DATA.csv')
            st.write(df)
            st.subheader("*Research questions*")
            st.markdown("""
                        1. **Movie Properties and Success Factors**
                            - What kinds of properties are associated with the most and least successful movies?
                            - Which movie had the highest or lowest profit?
                            - In which year did the movie industry make the highest profit?
                            - In which month did the movie industry make the highest profit?
                            - Do popular movies generate higher profit?
                            - What were the most and least expensive movies?
                            - What is the statistical relationship between budget and profit?
                            - Do movies with the highest budget receive the highest ratings?
                            - Which movie had the highest or lowest revenue?
                            - Is there any statistical relationship between revenue and profit / revenue and budget?
                            - What movie length is most liked by the audience?
                            - Which movies were rated the highest or lowest?
                            - Do highly rated movies generate higher profit?
                        2. **Top 10 Movies According to Different Features**
                            - Profit
                            - Budget
                            - Revenue
                            - Popularity
                        3. **Genres: Popularity and Profitability**
                            - Which genres are the most popular and profitable overall?
                            - Which genres are the most profitable year by year?
                            - Which genres are the most popular overall?
                            - How has genre popularity evolved over time?
                        4. **Top 10 Cast, Directors, and Production Companies**
                            - Who are the top 10 actors/actresses (cast)?
                            - Who are the top 10 directors?
                            - What are the top 10 production companies?""")
        
        elif selected == "2. Data Wrangling":
            st.title("2. Data Wrangling")
            with open("html/data_wrangling.html", "r", encoding="utf-8") as f:
                notebook_html = f.read()
            st.components.v1.html(notebook_html, height=800, scrolling=True)

        elif selected == '3. Exploratory Data Analysis':
            st.title("3. Exploratory Data Analysis")
            with open("html/exploratory_data_analysis.html", "r", encoding="utf-8") as f:
                notebook_html = f.read()
            st.components.v1.html(notebook_html, height=800, scrolling=True)
        
        elif selected == '4. Conclusions':
            st.title("4. Conclusions")
            st.markdown("""
            Throughout this data analysis, I found that:

            - **"Star Wars," "Avatar," and "Titanic"** are the most profitable movies, while the top movies by revenue are "Avatar," "Star Wars," and "Titanic." Despite their financial success, these films are not among the top 5 in popularity.
            - **June and December** are the months when movies generate the highest profits, highlighting the impact of holidays and festivities on box office performance.
            - There is a **strong positive correlation between profit and revenue**, indicating that higher revenue generally leads to higher profit. Revenue and budget are also positively correlated, suggesting that higher production costs often result in greater earnings. However, profit shows only a weak relationship with movie ratings, and there is no significant relationship between budget and runtime.
            - The **top 5 dominant genres (1960–2015)** are Drama, Comedy, Thriller, Action, and Adventure. This does not imply they are the most profitable (Animation, Adventure, Family, Fantasy, and Science Fiction) or the most popular (Adventure, Science Fiction, Fantasy, Animation, and Action). Profitability and popularity vary over the years, with a noticeable upward trend in recent periods.
            - The **most frequent actors** are Robert De Niro, Bruce Willis, and Samuel L. Jackson; the **top directors** are Steven Spielberg, Clint Eastwood, and Ridley Scott; and the **leading production companies** are Universal Pictures, Warner Bros, and Paramount Pictures.
            """)

            st.markdown("### *Limitations...*")
            st.write("""
            This is only a preliminary analysis of a small sample of movies. 
            The film industry includes thousands more films, but due to the large amount of missing data, it was not possible to perform this analysis on a larger sample. 
            Therefore, these findings may differ if a more comprehensive dataset were used.
            """)

    elif selected == "Regular Expressions":
        st.subheader("Regular Expressions")
        st.write("""
                 What are Regular Expressions?
                    
                 Regular expressions (or regex) are like special search patterns that help us **find, match, or change text** in a smart way.  
                 For example:
                    - Find all email addresses in a text.
                    - Replace all spaces with underscores.
                    - Check if a password is strong.

                    They are useful when you work with **text data** and need to **search or clean it quickly**.
                    """)
        selected_options = [
            "1. Word Counter",
            "2. Email Extractor",
            "3. Extract Phone Numbers",
            "4. Car Number Validator",
            "5. Validate Password Strength",
            "6. Replace Multiple Spaces with One"]
        selected = st.selectbox("Now, choose a project to explore here 👇🏻", options = selected_options)
        st.write("Current selection:", selected)

        if selected == "1. Word Counter":
            def count_words(text):
                # Regex: \b means word boundary, [a-zA-ZА-Яа-яЇїІіЄєҐґ]+ means letters only
                pattern = r'\b[a-zA-ZА-Яа-яЇїІіЄєҐґ]{2,}\b'
                words = re.findall(pattern, text)
                return len(words)

            def word_count_project():
                st.subheader("Word Count App (Regex)")
                st.write("""
                **Description:**  
                This tool counts words in a text using **regular expressions**, considering English and Cyrillic letters.
                
                **Regex pattern:**  
                `\\b[a-zA-ZА-Яа-яЇїІіЄєҐґ]{2,}\\b`
                
                - It ignores punctuation  
                - Works for multiple languages  
                - Counts only words with 2+ letters
                """)

                text = st.text_area("Enter text here:", "")
                if st.button("Count Words"):
                    result = count_words(text)
                    st.success(f"Total words: {result}")

                    st.write("**Matched words:**")
                    st.write(re.findall(r'\b[a-zA-ZА-Яа-яЇїІіЄєҐґ]{2,}\b', text))

            if __name__ == "__main__":
                word_count_project()
        
        elif selected == "2. Email Extractor":
            def email_extractor_project():
                st.subheader("Email Extractor")
                st.write("""
                **Description:**  
                This tool extracts **valid email addresses** from your text using a regular expression.  

                **Regex pattern:**  
                `\\b[\\w\\.-]+@[\\w\\.-]+\\.\\w+\\b`
                
                - Handles multiple emails  
                - Works with different domain formats  
                - Ignores invalid entries
                """)

                example_text = """Here are some emails as examples:
                - disposable.style.email.with+symbol@example.com
                - other.email-with-hyphen@example.net
                - A@b@c@example.com
                - fully-qualifies-domain@example.com
                - user.name@example.com
                - x@example.com
                - 5786@example.ua
                - ‘’john..doe’’@example.org
                - mailhost!username@example.org
                - this is"notallowed@example.com 
                - i_like_underscore@but_its_not_allow_in _this_part.example.com 
                """

                text = st.text_area("Enter text here:", example_text, height=150)
                
                if st.button("Extract Emails"):
                    pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
                    matches = re.findall(pattern, text)

                    if matches:
                        st.success(f"Found {len(matches)} email(s):")
                        for email in matches:
                            st.markdown(f"- **{email}**")
                    else:
                        st.warning("No valid email addresses found.")

            if __name__ == "__main__":
                email_extractor_project()

        elif selected == "3. Extract Phone Numbers":
            def phone_number_extractor():
                st.subheader("Phone Number Extractor")
                st.write("""
                **Description:**  
                This tool extracts phone numbers from text.  
                Typical valid formats include:
                - +380 XX XXX XXXX  
                - 0XX XXX XX XX  
                - +380XXXXXXXXX

                **Regex pattern:**  
                `(?:\+380|0)\s?\(?\d{2}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}` 
                """)

                example_text = """Try these phone numbers as examples:
Alex - +380 67 123 45 67 
Tom - 067 123 45 67
Linda - +380(44)123-45-67
Nick - 0441234567
John - +380 123 456 7890
                """

                text = st.text_area("Enter text here:", example_text, height=150)

                if st.button("Extract Phone Numbers"):
                    pattern = r'(?:\+380|0)\s?\(?\d{2}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}'
                    matches = re.findall(pattern, text)

                    if matches:
                        st.success(f"Found {len(matches)} phone number(s):")
                        for num in matches:
                            st.markdown(f"- **{num}**")
                    else:
                        st.warning("No valid phone numbers found.")

            if __name__ == "__main__":
                phone_number_extractor()

        elif selected == "4. Car Number Validator":
            def car_number_validator_project():
                st.subheader("Car Number Validator")
                st.write("""
                **Description:**  
                This tool validates Ukrainian car number plates matching the format:  
                Two uppercase letters (Cyrillic or Latin) + 4 digits + two uppercase letters.
                
                It also identifies the region based on the first two letters.
                
                **Regex pattern:**  
                `[А-ЯІЇЄҐA-Z]{2}\\d{4}[А-ЯІЇЄҐA-Z]{2}`
                         
                (For clarity, this section has been provided in Ukrainian.)
                """)

                regions = {
                    'АВ': 'Вінницька область',
                    'КВ': 'Вінницька область',
                    'АС': 'Волинська область',
                    'КС': 'Волинська область',
                    'АЕ': 'Дніпропетровська область',
                    'КЕ': 'Дніпропетровська область',
                    'АН': 'Донецька область',
                    'КН': 'Донецька область',
                    'АМ': 'Житомирська область',
                    'КМ': 'Житомирська область',
                    'АО': 'Закарпатська область',
                    'КО': 'Закарпатська область',
                    'АР': 'Запорізька область',
                    'КР': 'Запорізька область',
                    'АТ': 'Івано-Франківська область',
                    'КТ': 'Івано-Франківська область',
                    "АА": "Київ",
                    "АІ": "Київська область",
                    'ВА': 'Кіровоградська область',
                    'АН': 'Кіровоградська область',
                    'ВВ': 'Луганська область',
                    'НВ': 'Луганська область',
                    'ВС': 'Львівська область',
                    'НС': 'Львівська область',
                    'ВЕ': 'Миколаївська область',
                    'НЕ': 'Миколаївська область',
                    'ВН': 'Одеська область',
                    'НН': 'Одеська область',
                    'ВІ': 'Полтавська область',
                    'НІ': 'Полтавська область',
                    'ВК': 'Рівненська область',
                    'НК': 'Рівненська область',
                    'ВМ': 'Сумська область',
                    'НМ': 'Сумська область',
                    'ВО': 'Тернопільська область',
                    'НО': 'Тернопільська область',
                    'АХ': 'Харківська область',
                    'КХ': 'Харківська область',
                    'ВТ': 'Херсонська область',
                    'НТ': 'Херсонська область',
                    'ВХ': 'Хмельницька область',
                    'НХ': 'Хмельницька область',
                    'СА': 'Черкаська область',
                    'ІА': 'Черкаська область',
                    'СА': 'Чернігівська область',
                    'ІА': 'Чернігівська область'
                }

                car_number = st.text_input("Введіть номер вашого авто (формат: XX1234XX)", "")

                if st.button("Перевірити номер"):
                    pattern = r'[А-ЯІЇЄҐA-Z]{2}\d{4}[А-ЯІЇЄҐA-Z]{2}'

                    if re.fullmatch(pattern, car_number):
                        region_code = car_number[0:2]
                        region = regions.get(region_code)
                        if region:
                            st.success(f"Номер {car_number} дійсний. Авто зареєстроване в регіоні: {region}")
                        else:
                            st.info(f"Номер {car_number} дійсний. Регіон реєстрації не визначено.")
                    else:
                        st.error(f"Номер {car_number} недійсний. Будь ласка, введіть правильний номер авто.")

            if __name__ == "__main__":
                car_number_validator_project()

        elif selected == "5. Validate Password Strength":
            def password_strength_checker():
                st.subheader("Password Strength Validator")
                st.write("""
                **Description:**  
                Checks if a password meets the following criteria:  
                - At least 8 characters  
                - Contains at least one uppercase letter  
                - Contains at least one lowercase letter  
                - Contains at least one digit  
                - Contains at least one special character (`!@#$%^&*()_+-=[]{}|;:'",.<>?/`)  
                - No spaces allowed

                **Regex pattern:**  
                `^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+\\-=\[\]{}|;:'",.<>?/])[A-Za-z\\d!@#$%^&*()_+\\-=\[\]{}|;:'",.<>?/]{8,}$`
                """)

                password = st.text_input("Enter password:", type="password")

                if st.button("Check Strength"):
                    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{}|;:\'",.<>?/])[A-Za-z\d!@#$%^&*()_+\-=\[\]{}|;:\'",.<>?/]{8,}$'
                    if re.match(pattern, password):
                        st.success("Strong password!")
                    else:
                        st.error("Weak password. Make sure it meets all the criteria.")

            if __name__ == "__main__":
                password_strength_checker()

        elif selected == "6. Replace Multiple Spaces with One":
            def clean_text_project():
                st.subheader("🧹 Clean Text: Replace Multiple Spaces & Remove Duplicate Words")
                st.write("""
                **Description:**  
                This tool cleans up text by:  
                - Replacing multiple consecutive spaces with a single space  
                - Removing consecutive duplicate words (case-insensitive)
                
                **Regex patterns used:**  
                - Multiple spaces: `\\s{2,}`
                - Duplicate words: `\\b(\\w+)\\s+\\1\\b` 
                """)

                example_text = """This is is    an example   text with  multiple   spaces and and duplicate duplicate words."""

                text = st.text_area("Enter text here:", example_text, height=150)

                if st.button("Clean Text"):
                    # Replace multiple spaces with one
                    text_single_space = re.sub(r'\s{2,}', ' ', text)

                    # Remove consecutive duplicate words (case-insensitive)
                    cleaned_text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text_single_space, flags=re.IGNORECASE)

                    st.success("Text cleaned!")
                    st.write(cleaned_text)

            if __name__ == "__main__":
                clean_text_project()

# VISUALIZATION
if selected == 'Visualization':
    st.markdown("<h1 style='text-align: center;'>Visualization</h1>", unsafe_allow_html=True)
    st.markdown("""
                Welcome to the part of my portfolio where data comes to life!

                In this section, you’ll find some of my favorite projects where I’ve turned numbers into stories using different tools:

                - 🐍 Python – because sometimes code is art.
                - 📊 Tableau – for when I want to impress you with drag-and-drop magic.
                - 🧮 R – the tool I use when I feel fancy and statistical.
                
                Whether you're into clean dashboards, interactive charts, or just enjoy watching data glow up — you're in the right place.
                
                Grab a cup of coffee and scroll through. I promise no pie charts were harmed in the making of these visuals. 🍰
                """)
    selected_options = ["Python", 
                        "Tableau",
                        "R"]
    selected = st.selectbox("Feel free to explore and click here 👇", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Python":
        selected_optipns = ["Shopology. Analysis of Clothes Shopping",
                            "Visualization of Mortality",
                            "Letterbox Movie Classification"]
        selected = st.selectbox("Select a project", options = selected_optipns)
        st.write("Current selection:", selected)
        if selected == "Shopology. Analysis of Clothes Shopping":
            import pandas as pd
            import streamlit as st
            import pandas as pd
            import streamlit as st
            import plotly.express as px
            import folium
            def main():
            # page settings
                page = st.sidebar.selectbox('Choose a page:',
                                            ['DataSet',
                                            'Items Info',
                                            'Location',
                                            'Payment Methods'])
                if page == 'DataSet':

                    df = pd.read_csv('datasets/Shopping_Trends.csv')

                    st.title(':necktie: Shopology: Decoding Customer Shopping Trends')

                    st.write("**The Shopping Trends Dataset** offers valuable insights into consumer behavior "
                            "and purchasing patterns. Understanding customer preferences and trends is critical "
                            "for businesses to tailor their products, marketing strategies, and overall customer experience. ")
                    st.write(
                        "\nThis dataset captures a **wide range of customer attributes** including age, gender, purchase history, "
                        "preferred payment methods, frequency of purchases, and more. ")
                    st.write("\nAnalyzing this data can help businesses make informed decisions, optimize product offerings, "
                            "and enhance customer satisfaction. The dataset stands as a valuable resource for businesses "
                            "aiming to align their strategies with customer needs and preferences. ")
                    st.write('\nHere it is 🙃')

                    st.write(df)

                    st.markdown("## Details")
                    st.write("**Title**: Shopping Trends ",
                            "<br>**Rows**: 3900",
                            "<br>**Columns**: 22",
                            unsafe_allow_html=True)

                    st.markdown('## Data Dictionary')
                    st.write("📌 **Customer ID** - Unique identifier for each customer.",
                            "<br>📌 **Age** - Age of the customer.",
                            "<br>📌 **Gender** - Gender of the customer (Male/Female)",
                            "<br>📌 **Item Purchased** - The item purchased by the customer",
                            "<br>📌 **Category** - Category of the item purchased",
                            "<br>📌 **Purchase Amount (USD)** - The amount of the purchase in USD",
                            "<br>📌 **Location** - Location where the purchase was made",
                            "<br>📌 **Size** - Size of the purchased item",
                            "<br>📌 **Color** - Color of the purchased item",
                            "<br>📌 **Season** - Season during which the purchase was made",
                            "<br>📌 **Review Rating** - Rating given by the customer for the purchased item",
                            "<br>📌 **Payment Method** - Customer's most preferred payment method",
                            "<br>📌 **Shipping Type** - Type of shipping chosen by the customer",
                            "<br>📌 **Previous Purchases** - Number of previous purchases made by the customer",
                            "<br>📌 **Preferred Payment Method** - Method which was used to pay for the purchase",
                            "<br>📌 **Frequency of Purchases** - Frequency at which the customer makes purchases",
                            "<br>📌 **Customer Segmentation** - The official label of a customer",
                            "<br>📌 **Seasonal Trends** - The purpose of purchase",
                            "<br>📌 **Delivery Time** - Duration it takes for a products to be delivered",
                            "<br>📌 **Number of Items Purchased** - The amount of items purchased by a customer",
                            unsafe_allow_html=True)

                elif page == 'Items Info':
                
                    df = pd.read_csv('datasets/Shopping_Trends.csv')

                    st.title(':bar_chart: Sales Dashboard')
                    st.markdown('##')

                    st.write("Here, you can easily discover a wealth of relevant information tailored to your needs. "
                            "Navigate effortlessly through the data by employing our user-friendly filtering options. "
                            "Explore details related to Categories, delve into specifics about individual Items, "
                            "and gain insights into Size and Color attributes. ")
                    st.write('Your journey to comprehensive and insightful data exploration begins here...')

                    # sidebar
                    st.sidebar.header('Choose Filter Here: ')
                    gender = st.sidebar.multiselect(
                        "Select the Gender: ",
                        options=df['Gender'].unique(),
                        default=df['Gender'].unique()
                    )

                    season = st.sidebar.multiselect(
                        'Select the Season: ',
                        options=df['Season'].unique(),
                        default=df['Season'].unique()
                    )

                    segmentation = st.sidebar.multiselect(
                        'Select the Customer Segmentation: ',
                        options=df["Customer Segmentation"].unique(),
                        default=df['Customer Segmentation'].unique()
                    )

                    df_selection = df.query(
                        "Gender == @gender & Season == @season & `Customer Segmentation` == @segmentation"
                    )

                    # main page
                    total_sales = int(df_selection['Purchase Amount (USD)'].sum())
                    average_rating = round(df_selection['Review Rating'].mean(), 1)
                    star_rating = ':star:' * int(round(average_rating, 0))
                    average_amount_of_orders = round(df_selection['Number of Items Purchased'].mean())

                    left_column, middle_column, right_column = st.columns(3)
                    with left_column:
                        st.subheader('Total Sales:')
                        st.write(f'**USD $ {total_sales}**')
                    with middle_column:
                        st.subheader('Average Rating:')
                        st.write(f'**{average_rating} {star_rating}**')
                    with right_column:
                        st.subheader('Average Items Purchased:')
                        st.write(f'**{average_amount_of_orders} items**')

                    st.markdown('---')

                    # Data Set
                    st.dataframe(df_selection)

                    # first left graph
                    items_line = df_selection.groupby(by=['Item Purchased']).sum()[['Purchase Amount (USD)']]. \
                        sort_values(by='Purchase Amount (USD)')

                    fig_items = px.histogram(
                        items_line,
                        x=items_line.index,
                        y='Purchase Amount (USD)',
                        title='<b>Purchase Amount for each item (USD)</b>',
                        color_discrete_sequence=['#9B67E2'] * len(items_line),
                        template='plotly_white'
                    )

                    # st.plotly_chart(fig_items)

                    # first right graph
                    category_line = df_selection.groupby(by=['Category']).sum()[['Purchase Amount (USD)']]
                    fig_category = px.bar(
                        category_line,
                        x='Purchase Amount (USD)',
                        y=category_line.index,
                        title='<b>Purchase Amount for each category (USD)</b>',
                        color_discrete_sequence=['#FBE426'] * len(category_line),
                        template='plotly_white'
                    )

                    # right place
                    left_column, right_column = st.columns(2)
                    left_column.plotly_chart(fig_items, use_container_width=True)
                    right_column.plotly_chart(fig_category, use_container_width=True)

                    # second left graph
                    colors = df_selection['Color'].unique()
                    selected_color = st.multiselect('Choose color:', colors)
                    filtered_df = df_selection[df_selection['Color'].isin(selected_color)]

                    color_graph = px.histogram(
                        filtered_df,
                        x='Purchase Amount (USD)',
                        y='Color',
                        title=f'<b>Purchase amount for {", ".join(selected_color)} items<b>',
                        color_discrete_sequence=['#FBE426'] * len(category_line),
                        template='plotly_white'
                    )

                    # second right graph
                    size_graph = px.pie(filtered_df,
                                        title='<b>Purchase Amount for each Size<b>',
                                        values='Purchase Amount (USD)',
                                        names='Size',
                                        color='Size',
                                        color_discrete_map={'M': '#9B67E2',
                                                            'L': '#BEADFA',
                                                            'S': '#DFCCFB',
                                                            'XL': '#FFF8C9'},
                                        hole=0.4
                                        )

                    # right place
                    left_column, right_column = st.columns(2)
                    left_column.plotly_chart(color_graph, use_container_width=True)
                    right_column.plotly_chart(size_graph, use_container_width=True)

                elif page == 'Location':

                    df = pd.read_csv('datasets/Shopping_Trends.csv')

                    st.title(':bar_chart: Sales Dashboard')
                    st.markdown('##')

                    st.write(
                        "Step into the next level of precision by filtering information based on Location and Shipping Type columns."
                        " Seamlessly refine your search to pinpoint data relevant to specific locations and shipping preferences."
                        " Whether you're seeking details about a particular region or looking to understand the nuances of different "
                        "shipping methods, our platform empowers you to tailor your exploration. "
                        "Navigate with ease as you unlock insights tied to location-based dynamics and shipping intricacies. "
                        "Your quest for targeted and refined data analysis continues here.")

                    # filter the data
                    st.sidebar.header('Choose Filter Here: ')
                    # create for location
                    location = st.sidebar.multiselect('Pick your State', df['Location'].unique())
                    if not location:
                        df2 = df.copy()
                    else:
                        df2 = df[df['Location'].isin(location)]

                    # create for shipping type
                    shipping = st.sidebar.multiselect('Pick your Shipping Type', df2['Shipping Type'].unique())
                    if not shipping:
                        df3 = df2.copy()
                    else:
                        df3 = df2[df2['Shipping Type'].isin(shipping)]

                    # filter the data
                    if not location and not shipping:
                        filtered_df = df
                    elif location and shipping:
                        filtered_df = df3[df['Location'].isin(location) & df3['Shipping Type'].isin(shipping)]
                    elif location:
                        filtered_df = df3[df['Location'].isin(location)]
                    else:
                        filtered_df = df3[df['Shipping Type'].isin(shipping)]

                    # Data Set
                    st.dataframe(filtered_df)

                    # left graph
                    st.markdown('### Percentage by Gender/Season/Customer Segmentation:')
                    fig = px.sunburst(
                        data_frame=filtered_df,
                        path=['Gender', 'Season', 'Customer Segmentation'],
                        color='Season',
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        maxdepth=-1
                    )

                    fig.update_traces(textinfo='label+percent entry')
                    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

                    st.markdown("---")  # Add horizontal space

                    # сenter the chart 
                    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider
                    with col2:
                        st.plotly_chart(fig, use_container_width=True)
           
                    st.markdown("---")  # Add more horizontal space

                    # map
                    st.title(':world_map: Sales Map')
                    st.markdown('##')

                    st.write("Here you can explore and uncover insights into the spending habits of different states across the "
                            "United States. Dive into the data to find 8 states that lead the way in terms of purchase expenditures. ")

                    df_map = pd.read_csv('datasets/map_file.csv')

                    st.dataframe(df_map)

                    fig = px.scatter_geo(
                        df_map,
                        locations='Code',
                        locationmode='USA-states',
                        color='Code',
                        scope='usa',
                        color_discrete_map={'MT': '#636EFA', 'ME': '#00CC96', 'FL': '#AB63FA', 'DE': '#FFA15A', 'VA': '#B6E880',
                                            'KY': '#B6E880', 'IN': '#FBE426', 'AR': '#DEA0FD'}
                    )

                    # сenter the chart 
                    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider
                    with col2:
                        st.plotly_chart(fig, use_container_width=True)

                elif page == 'Payment Methods':
                    
                    df = pd.read_csv('datasets/Shopping_Trends.csv')

                    st.title(':bar_chart: Sales Dashboard')
                    st.markdown('##')

                    st.write("Comprehensive payment methods information page. "
                            "Here, you'll effortlessly discover everything you need to know about various payment methods. "
                            "Our platform provides a user-friendly interface that allows you to navigate seamlessly and explore "
                            "details related to payment options, ensuring a smooth and informed experience. "
                            "Whether you're interested in understanding available payment methods, comparing their features, "
                            "or seeking insights into payment trends, this page is your go-to resource. "
                            "Simplify your quest for payment information and make informed decisions with ease."
                            "Take your exploration to the next level by customizing your payment methods information based on age "
                            "and customer segmentation. ")

                    # selection
                    customer = df['Customer Segmentation'].unique().tolist()
                    ages = df['Age'].unique().tolist()

                    age_selection = st.sidebar.slider('**Age:**',
                                                    min_value=min(ages),
                                                    max_value=max(ages),
                                                    value=(min(ages), max(ages)))

                    customer_selection = st.sidebar.multiselect('**Customer Segmentation:**',
                                                                customer,
                                                                default=customer)

                    # filter dataframe
                    mask = (df['Age'].between(*age_selection)) & (df['Customer Segmentation'].isin(customer_selection))
                    number_of_results = df[mask].shape[0]
                    st.markdown(f'*Available Results: {number_of_results}*')

                    # group dataframe
                    df_grouped = df[mask].groupby(by=['Payment Method']).count()[['Age']]
                    df_grouped = df_grouped.rename(columns={'Age': 'Number of Customers'})
                    df_grouped = df_grouped.reset_index()

                    # first left graph
                    bar_chart = px.bar(df_grouped,
                                    title='<b>Number of Customers for every Payment Method<b>',
                                    x='Payment Method',
                                    y='Number of Customers',
                                    text='Number of Customers',
                                    color_discrete_sequence=['#9B67E2'] * len(df_grouped),
                                    template='plotly_white')

                    bar_chart.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    bar_chart.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

                    # first right graph
                    pie_chart = px.pie(df_grouped,
                                    title='<b>Percent of Customers for every Payment Method<b>',
                                    values='Number of Customers',
                                    names='Payment Method',
                                    color='Payment Method',
                                    color_discrete_map={'Credit Card': '#FF9B9B',
                                                        'Venmo': '#FFD28F',
                                                        'Cash': '#D0BFFF',
                                                        'Paypal': '#FFFAD7',
                                                        'Debit Card': '#FFFEC4',
                                                        'Bank Transfer': '#CBFFA9'},
                                    hole=0.4
                                    )

                    left_column, right_column = st.columns(2)
                    left_column.plotly_chart(bar_chart, use_container_width=True)
                    right_column.plotly_chart(pie_chart, use_container_width=True)

            main()
        
        elif selected == "Visualization of Mortality":
            st.title('🚑 How Do People Die in the USA? A Visualization of Mortality')
            st.markdown("""**Death** is a difficult topic, but it is crucial for government, healthcare, economy, and medicine. 
                        Understanding how people die can lead to changes in research funding or strengthening preventive measures against certain contemporary diseases. """)
            st.markdown("""In the USA, **Centers for Disease Control and Prevention (CDC)** collected [mortality data](https://wonder.cdc.gov/ucd-icd10.html) from 1999 to 2015. 
                        The data is rich in demographic information, including age at death, the disease causing it, gender, race, and geographical location (city/state).""")
            st.markdown("""
                This data will help us answer many **questions about death**:

                - What are the leading causes of death in the USA?
                - Are men or women more likely to die? Does it depend on the cause of death? Or the age?
                - Which causes of death are becoming more or less common over time?
                """)
            st.markdown("For this project the dataset was used:")
            df = pd.read_csv('datasets/deaths.csv')
            st.write(df)
            col1, col2 = st.columns(2)
            # --- Колонка 1: Загальна кількість смертей по роках ---
            with col1:
                col1.markdown("### 1. Total Deaths by Year")
                by_year = df.groupby("Year")["Deaths"].sum()
                
                fig1, ax1 = plt.subplots(figsize=(5, 4))
                by_year.plot(kind="bar", color=['blue', 'blue', 'red'], ax=ax1)
                ax1.set_title("Total Deaths by Year")
                ax1.set_xlabel("Year")
                ax1.set_ylabel("Deaths")
                ax1.tick_params(axis='x', rotation=45)
                st.pyplot(fig1)
            # --- Колонка 2: Смерті за статтю у 2015 ---
            with col2:
                col2.markdown("### 2. Deaths by Gender in 2015")
                df2015 = df[df["Year"] == 2015]
                by_gender_2015 = df2015.groupby("Gender")["Deaths"].sum()
                
                fig2, ax2 = plt.subplots(figsize=(5, 4))
                by_gender_2015.plot(kind="bar", color=["red", "blue"], ax=ax2)
                ax2.set_title("Deaths by Gender (2015)")
                ax2.set_xlabel("Gender")
                ax2.set_ylabel("Deaths")
                st.pyplot(fig2)
            st.markdown("In the **first graph** I demonstrated the total deaths by years and highlighted " \
            "the year with the greatest amount. In the **second graph** I created a simple bar chart to " \
            "compare the total number of deaths by gender in this year.")
            df2015 = df[df["Year"] == 2015]
            causes = df2015.groupby('Cause')['Deaths'].sum().reset_index()
            causes_sorted = causes.sort_values(by='Deaths', ascending=False)
            # Топ-5 найпопулярніших і найменш популярних
            top_5 = causes_sorted.head(5)
            bottom_5 = causes_sorted.tail(5)
            # Дві колонки
            col1, col2 = st.columns(2)
            # --- Колонка 1: Топ-5 ---
            with col1:
                col1.markdown("### 3. Top 5 Most Common Causes")
                fig_top, ax_top = plt.subplots(figsize=(6, 4))
                top_5.set_index('Cause').plot(kind='barh', color='darkgreen', ax=ax_top)
                ax_top.set_xlabel("Number of Deaths")
                ax_top.set_ylabel("Cause")
                ax_top.invert_yaxis()
                st.pyplot(fig_top)
            # --- Колонка 2: Найменш 5 ---
            with col2:
                col2.markdown("### 4. Bottom 5 Least Common Causes")
                fig_bottom, ax_bottom = plt.subplots(figsize=(6, 4))
                bottom_5.set_index('Cause').plot(kind='barh', color='orange', ax=ax_bottom)
                ax_bottom.set_xlabel("Number of Deaths")
                ax_bottom.set_ylabel("Cause")
                ax_bottom.invert_yaxis()
                st.pyplot(fig_bottom)
            st.markdown("""
                        Here I broke down one big graph into two small ones for clear understanding. 
                        
                        **Conclusions:**
                        
                        - The most prevalent diseases - heart disease, malignant neoplasms.
                        - The least prevalent - acute poliomyelitis; arthropod-borne viral encephalitis; measles; scarlet fever and diphtheria.""")

            st.subheader("5. Deaths by Age and Gender in 2015")
        
            df2015 = df[df["Year"] == 2015]
            age_gender_deaths = df2015.groupby(["Age", "Gender"])["Deaths"].sum()
            pivot_table = age_gender_deaths.unstack(1)
            fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(17, 10), sharex=True)
            colors = ["blue", "red"]  # Для статей
            pivot_table.plot(
                kind="bar",
                ax=axes,
                subplots=True,
                color=colors,
                legend=False,
                width=0.8
            )
            axes[0].set_title("Deaths by Age - Male")
            axes[1].set_title("Deaths by Age - Female")
            axes[1].set_xlabel("Age")
            axes[0].set_ylabel("Deaths")
            axes[1].set_ylabel("Deaths")

            plt.tight_layout()
            st.pyplot(fig)
            st.markdown("""
                **Conclusions:**
                - First months of life: males (higher mortality).
                - Up to 13 years old: approximately the same.
                - Up to 84 years old: males (higher mortality).
                - Up to 100 years old: females (higher mortality).""")
            
            st.subheader("6. Stacked Bar Chart of Deaths by Age and Gender (2015)")
            # Фільтруємо дані за 2015 рік
            df2015 = df[df["Year"] == 2015]

            # Групування: Age + Gender → Deaths
            age_gender_deaths = df2015.groupby(["Age", "Gender"])["Deaths"].sum()

            # Перетворення в таблицю для побудови графіка
            pivot_table = age_gender_deaths.unstack(1)

            # Побудова stacked bar chart
            fig, ax = plt.subplots(figsize=(22, 12))  # змінено з 18x10 на 12x6 для кращого вигляду в браузері

            pivot_table.plot(
                kind="bar",
                stacked=True,
                color=["red", "blue"],
                ax=ax
            )

            ax.set_title("Deaths by Age and Gender (2015)", fontsize=14)
            ax.set_xlabel("Age")
            ax.set_ylabel("Number of Deaths")
            ax.legend(title="Gender", loc="upper right")
            ax.tick_params(axis='x', rotation=45)

            plt.tight_layout()
            st.pyplot(fig)
            st.markdown("""
                        I would combine the two graphs... However, it's not very informative because 
                        it's difficult to compare male and female indicators in a single bar chart.
                        
                        **That would be suitable for:**
                        
                        - Comparison of one characteristic across different types.
                        - Sales of different types of products across different points.""")
            st.subheader("7. Line Chart of Deaths by Age and Gender (2015)")
            df2015 = df[df["Year"] == 2015]
            age_gender_deaths = df2015.groupby(["Age", "Gender"])["Deaths"].sum()
            pivot_table = age_gender_deaths.unstack(1)
            fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 6), sharex=True)
            colors = ["blue", "red"]
            pivot_table.plot(
                kind="line",
                subplots=True,
                ax=axes,
                color=colors,
                legend=False
            )

            axes[0].set_title("Deaths by Age - Male")
            axes[1].set_title("Deaths by Age - Female")
            axes[1].set_xlabel("Age")
            axes[0].set_ylabel("Deaths")
            axes[1].set_ylabel("Deaths")

            plt.tight_layout()
            st.pyplot(fig)
            st.markdown("Since **Age**] is a continuous variable, it would be appropriate to use a line plot for comparison.")
            st.subheader("8. Line Chart of Deaths by Age and Gender (2015) – Combined View")
            # Дані за 2015 рік
            df2015 = df[df["Year"] == 2015]

            # Групування: Age + Gender → Deaths
            pivot_table = df2015.groupby(["Age", "Gender"])["Deaths"].sum().unstack(1)

            # Побудова графіка
            fig, ax = plt.subplots(figsize=(12, 5))  # змінено з 18x6 на зручний розмір
            pivot_table.plot(kind="line", color=["red", "blue"], ax=ax, title="Deaths in 2015 by Age and Gender")

            ax.set_ylabel("Deaths")
            ax.set_xlabel("Age")
            ax.legend(title="Gender")
            ax.grid(False)

            st.pyplot(fig)

            st.markdown("Now, using only lines, it's easy to compare the difference between genders by age on **one line graph.**")
            
            st.subheader("9. Causes of Death in 2015")
            deaths_by_cause = (
                df[df["Year"] == 2015]
                .groupby("Cause")
                .agg({"Deaths": "sum"})
                .sort_values("Deaths", ascending=True)
            )
            fig, ax = plt.subplots(figsize=(9, 12))
            deaths_by_cause.plot(
                kind="barh",
                legend=False,
                color="black",
                ax=ax
            )

            ax.set_xlabel("Number of Deaths")
            ax.set_ylabel("Cause")
            ax.set_title("Causes of Death in 2015")
            plt.tight_layout()

            st.pyplot(fig)
            st.markdown("Excess information in visualizations hinders data comprehension, " \
            "creates visual noise, and distracts from the main insights.")
            st.subheader("10. 10 Most Common Causes of Death in 2015")
            least_common_causes = (
                df[df["Year"] == 2015]
                .groupby("Cause")
                .agg({"Deaths": "sum"})
                .sort_values("Deaths", ascending=True)
                .tail(10) 
            )
            fig, ax = plt.subplots(figsize=(9, 6))
            least_common_causes.plot(
                kind="barh",
                legend=False,
                color="black",
                ax=ax
            )
            ax.set_xlabel("Number of Deaths")
            ax.set_ylabel("Cause")
            ax.set_title("10 Most Common Causes of Death in 2015")
            plt.tight_layout()

            st.pyplot(fig)
            st.markdown("""
                        This graph is easier to understand. It is clear that:
                        
                        - Diseases of heart
                        - Malignant neoplasms
                        - Chronic lower respiratory diseases
                        
                        are the most prevalent causes of mortality.""")
            st.subheader("11. Top causes of death by age ")
            cause_year_deaths = (
                df.groupby(["Cause", "Year"])
                .agg({'Deaths': 'sum'})
                .sort_values('Deaths', ascending=False)
                .unstack(1)  # Роки — окремі колонки
            )
            # Побудова вертикального графіка
            fig, ax = plt.subplots(figsize=(20, 15))  # ширший, бо багато категорій
            cause_year_deaths.plot(kind="bar", legend=True, ax=ax)

            ax.set_xlabel("Cause")
            ax.set_ylabel("Number of Deaths")
            ax.set_title("Deaths by Cause and Year")
            ax.tick_params(axis='x', rotation=90)

            plt.tight_layout()
            st.pyplot(fig)

            st.markdown("""The visualization above contains a lot of information (perhaps too much). 
                        However, it's easy to notice that **mortality due to HIV infection has been decreasing every 5 years, 
                        starting from 2005!**""")
            
            st.subheader("12. Deaths by Cause and Gender")
            cause_gender_deaths = (
                df.groupby(['Cause', 'Gender'])
                .agg({'Deaths': 'sum'})
                .sort_values('Deaths', ascending=True)
                .unstack(1)  # Gender → окремі колонки
            )

            # Побудова графіка з кольорами
            fig, ax = plt.subplots(figsize=(20, 15))
            cause_gender_deaths.plot(
                kind='bar',
                legend=True,
                ax=ax,
                color=['blue', 'red']  # Чоловіки — blue, Жінки — red
            )

            ax.set_xlabel("Cause")
            ax.set_ylabel("Number of Deaths")
            ax.set_title("Deaths by Cause and Gender")
            plt.tight_layout()

            st.pyplot(fig)
            st.subheader("13. Causes of death by age")
            st.markdown ("""
                         Since the dataset contains a large number of causes of death, I've selected only a few for visualization:

                        - "Alzheimer's disease"
                        - "Diseases of heart"
                        - "Malignant neoplasms"
                        - "Accidents (unintentional injuries)""")

            clist = [
                "Alzheimer's disease",
                "Diseases of heart",
                "Malignant neoplasms",
                "Accidents (unintentional injuries)"
            ]
            df2015_clist = df[df["Year"] == 2015]
            df2015_clist = df2015_clist[df2015_clist["Cause"].isin(clist)]

            age_cause_deaths = (
                df2015_clist
                .groupby(["Age", "Cause"])
                .agg({'Deaths': 'sum'})
                .unstack(1)  # Cause → окремі лінії
            )

            fig, ax = plt.subplots(figsize=(10, 6))
            age_cause_deaths.plot(kind="line", ax=ax)

            ax.set_title("Deaths by Age for Selected Causes in 2015")
            ax.set_xlabel("Age")
            ax.set_ylabel("Number of Deaths")
            ax.legend(title="Cause", loc="upper left")
            ax.grid(True)

            plt.tight_layout()
            st.pyplot(fig)

            st.markdown("""
                        **Conclusions:**
                        
                        - Mortality due to unintentional injuries is almost constant.
                        - Mortality due to Alzheimer's disease remains constant until 70 years old, then increases until 90 years old, and decreases afterward.
                        - Mortality due to heart diseases increases from 19 years old to 90. It then sharply decreases after 90.
                        - Mortality due to malignant neoplasms increases from 20 years old to 70. It then sharply decreases after 70.""")

            st.subheader("14. Deaths by Age and Gender for 3 Selected Causes (2015)")
            clist = df["Cause"].unique()[:3]

            for cause in clist:
                # Фільтрація по поточній причині
                df2015_clist = df[df["Year"] == 2015]
                df2015_clist = df2015_clist[df2015_clist["Cause"] == cause]
                
                # Групування та побудова графіка
                grouped = (
                    df2015_clist
                    .groupby(["Age", "Gender"])
                    .agg({'Deaths': 'sum'})
                    .unstack("Gender")  # Стає дві лінії: Male, Female
                )
                
                fig, ax = plt.subplots(figsize=(10, 6))
                grouped.plot(kind="line", ax=ax, color=['red', 'blue'], title=cause)
                
                ax.set_xlabel("Age")
                ax.set_ylabel("Number of Deaths")
                ax.legend(title="Gender")
                ax.grid(True)
                plt.tight_layout()
                
                st.pyplot(fig)

            st.markdown("""
                            **Overall conclusions:**

                            - The most common causes of death across all years are heart diseases and malignant neoplasms.
                            - The least common are acute poliomyelitis; arthropod-borne viral encephalitis; measles; scarlet fever; and diphtheria.
                            - The number of deaths is generally higher among men than women.
                            - Mortality due to unintentional injuries remains almost constant throughout life, depending on Alzheimer's disease, heart diseases, and neoplasms.
                            - Higher mortality is observed among both men and women from 75 to 100 years old.""")

        elif selected == "Letterbox Movie Classification":
            page = st.sidebar.selectbox('Choose a page:',
                                ['DataSet',
                                 'About language',
                                 'Genres',
                                 'Studios Behind the Success',
                                 'Rating-Based Film Rankings'])
            if page == 'DataSet':
                df = pd.read_csv('datasets/Letterbox Movie Classification Dataset.csv')

                st.title('🎬 Letterbox Movie Analysis')

                st.markdown("""
                            The Letterbox Movie Classification Dataset is a rich and detailed 
                            collection of metadata for 10,002 movies, sourced from a popular 
                            movie rating and review platform (inspired by Letterboxd-like data). 
                            This dataset provides a comprehensive snapshot of movie attributes, 
                            including titles, directors, genres, ratings, runtime, language, studios, 
                            and user engagement metrics such as watches, likes, and list appearances. 
                            """)
                st.write('\nHere it is 🙃')

                st.write(df)
                st.markdown('---')
                st.markdown("## Details")
                st.write("**Title**: Letterbox Movie Classification Dataset ",
                        "<br>**Rows**: 10,002",
                        "<br>**Columns**: 15",
                        unsafe_allow_html=True)
                
                st.markdown('## Data Dictionary')
                st.write("📌 **Film_title** - The title of the movie.",
                    "<br>📌 **Director** - The primary director(s) of the movie. Multiple directors are listed together.",
                    "<br>📌 **Average_rating** - The average user rating for the movie (on a scale of 1 to 5).",
                    "<br>📌 **Genres** - A list of genres associated with the movie (e.g., ['Horror', 'Drama']).",
                    "<br>📌 **Runtime** - The runtime of the movie in minutes.",
                    "<br>📌 **Original_language** - The runtime of the movie in minutes.",
                    "<br>📌 **Description** - A brief synopsis or description of the movie’s plot or theme.",
                    "<br>📌 **Studios** - A list of production studios associated with the movie.",
                    "<br>📌 **Watches** - The total number of times the movie has been watched by users.",
                    "<br>📌 **List_appearances** - The number of times the movie appears in user-curated lists.",
                    "<br>📌 **Likes** - The total number of likes the movie has received from users.",
                    "<br>📌 **Fans** - The number of users who have marked themselves as fans of the movie.",
                    "<br>📌 **Lowest ★** - The number of 1-star ratings the movie has received.",
                    "<br>📌 **Medium ★★★** - The number of 3-star ratings the movie has received.",
                    "<br>📌 **Highest ★★★★★** - The number of 5-star ratings the movie has received.",
                    "<br>📌 **Total_ratings** - The total number of ratings (across all star levels) for the movie.",
                        unsafe_allow_html=True)
            
            elif page == 'About language':
                st.title("Language Distribution & Cultural Reach")
                st.markdown("""
                            Let’s take a trip around the world — no passport needed (sounds like a dream for men in Ukraine now). 
                            This section explores how different languages shape the movie landscape. 
                            From runtime quirks to average ratings and which languages dominate the screen, each chart gives 
                            a peek into how culture and cinema go hand in hand. And yes, English might be the loudest in the room... 
                            but it's definitely not the only one talking.""")

                df = pd.read_csv('datasets/Letterbox Movie Classification Dataset.csv')

                st.markdown(
                    """
                    <style>
                    .highlight-block {
                        background-color: #f2f6fc;
                        border-left: 6px solid #1f77b4;
                        padding: 1rem;
                        margin-bottom: 2rem;
                        border-radius: 8px;
                    }
                    .highlight-block h3 {
                        margin-top: 0;
                        color: #1f4e79;
                    }
                    .highlight-block ul {
                        padding-left: 1.2rem;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                # Compute values
                num_movies = df["Film_title"].nunique()
                top_language = df["Original_language"].mode().iloc[0]
                avg_runtime = round(df["Runtime"].mean(), 1)
                top_rated = df.loc[df["Average_rating"].idxmax()]
                top_movie_title = top_rated["Film_title"]
                top_movie_rating = top_rated["Average_rating"]

                # Creative container block
                st.markdown(
                    f"""
                    <div class="highlight-block">
                        <h3>🎬 Dataset Overview: Key Insights</h3>
                        <ul>
                            <li><strong>Total movies:</strong> {num_movies}</li>
                            <li><strong>Most common language:</strong> {top_language}</li>
                            <li><strong>Average runtime:</strong> {avg_runtime} minutes</li>
                            <li><strong>Top-rated film:</strong> <em>{top_movie_title}</em> ⭐ {top_movie_rating}</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown('---')
                st.write(df)

                # ---- Top Languages by Movie Count (Histogram) ----
                top_lang_counts = (
                    df["Original_language"]
                    .value_counts()
                    .head(10)
                    .reset_index()
                )
                top_lang_counts.columns = ["Language", "Movie Count"]

                fig_hist = px.bar(
                    top_lang_counts,
                    x="Language",
                    y="Movie Count",
                    color="Language",
                    title="Top 10 Most Common Languages",
                )
                st.plotly_chart(fig_hist, use_container_width=True)
                st.markdown('---')

                # Pie Chart for Percentage Distribution
                top_lang_count = df["Original_language"].value_counts().head(10).reset_index()
                top_lang_count.columns = ["Language", "Number of Movies"]

                fig_pie = px.pie(
                    top_lang_count,
                    names="Language",
                    values="Number of Movies",
                    title="Language Share of Top 10 Movie Languages",
                    hole=0.3  
                )
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_pie, use_container_width=True)
                st.markdown('---')

                st.subheader("Now you can interact with grpahs. Choose the options here 👇🏻")

                # --- Dropdowns on main screen (not sidebar) ---
                all_languages = df["Original_language"].dropna().unique()

                selected_languages = st.multiselect(
                    "Select Languages:",
                    sorted(all_languages),
                    default=["English", "Japanese", "Ukrainian", "Italian", "Swedish", "Finnish"]
                )

                metric = st.selectbox(
                    "Choose a Metric:",
                    ["Number of Movies", "Average Rating", "Average Runtime"]
                )

                # --- Filter Data ---
                filtered_df = df[df["Original_language"].isin(selected_languages)]

                # --- Plot based on selected metric ---
                if metric == "Number of Movies":
                    data = filtered_df["Original_language"].value_counts().reset_index()
                    data.columns = ["Language", "Count"]
                    fig = px.bar(
                        data,
                        x="Language",
                        y="Count",
                        title="Number of Movies by Language",
                        color="Language"
                    )

                elif metric == "Average Rating":
                    data = filtered_df.groupby("Original_language")["Average_rating"].mean().reset_index()
                    data.columns = ["Language", "Average Rating"]
                    fig = px.bar(
                        data,
                        x="Language",
                        y="Average Rating",
                        title="Average Rating by Language",
                        color="Language"
                    )

                elif metric == "Average Runtime":
                    data = filtered_df.groupby("Original_language")["Runtime"].mean().reset_index()
                    data.columns = ["Language", "Average Runtime"]
                    fig = px.bar(
                        data,
                        x="Language",
                        y="Average Runtime",
                        title="Average Runtime by Language",
                        color="Language"
                    )

                # --- Display the chart ---
                st.plotly_chart(fig, use_container_width=True)

            elif page == 'Genres':
                df = pd.read_csv('datasets/Letterbox Movie Classification Dataset.csv')

                st.title("Genres and Popularity")
                st.markdown("""
                            In the genres section, I wanted to see what kind of movies dominate the platform—spoiler: 
                            drama never dies. I broke down the data to find which genres are the most common, 
                            which ones get the highest ratings, and which attract the most likes. 
                            It turns out that action and science fiction are like that one friend who always shows up 
                            (and gets all the attention). Meanwhile, poor experimental films are probably crying 
                            in a corner of the dataset.""")
                
                st.write(df)
                st.markdown("---")

                # --- Preprocess genres ---
                df["Genres"] = df["Genres"].str.strip("[]").str.replace("'", "")
                df_genres = df.assign(Genres=df["Genres"].str.split(", ")).explode("Genres")

                # --- Filter UI ---
                st.subheader("Filter Options")
                col1, col2 = st.columns(2)

                with col1:
                    genre_limit = st.slider("Number of genres to display", min_value=5, max_value=30, value=15)

                with col2:
                    selected_directors = st.multiselect(
                        "Select Director(s):",
                        sorted(df["Director"].dropna().unique()),
                        default=[]
                    )

                # --- Apply director filter if selected ---
                if selected_directors:
                    df_genres_filtered = df_genres[df_genres["Director"].isin(selected_directors)]
                else:
                    df_genres_filtered = df_genres.copy()

                # --- Chart 1: Genre frequency ---
                genre_counts = df_genres_filtered["Genres"].value_counts().head(genre_limit).reset_index()
                genre_counts.columns = ["Genre", "Count"]

                fig1 = px.bar(
                    genre_counts,
                    x="Genre",
                    y="Count",
                    title="Most Common Genres",
                    labels={"Count": "Number of Movies"},
                    color="Genre"
                )
                st.plotly_chart(fig1, use_container_width=True)

                st.markdown("---")

                # --- Chart 2: Average rating by genre ---
                avg_rating = (
                    df_genres_filtered.groupby("Genres")["Average_rating"]
                    .mean()
                    .sort_values(ascending=False)
                    .head(genre_limit)
                    .reset_index()
                )

                fig2 = px.bar(
                    avg_rating,
                    x="Genres",
                    y="Average_rating",
                    title="Average Rating by Genre",
                    labels={"Genres": "Genre", "Average_rating": "Average Rating"},
                    color="Genres"
                )
                st.plotly_chart(fig2, use_container_width=True)

                st.markdown("---")

                st.subheader("For the next graph I offer you to deep your interaction and choose the main topic :)")

                # --- Chart 3: Selected popularity metric by genre ---
                popularity_metric = st.selectbox(
                    "Select metric for popularity analysis:",
                    ["Likes", "Fans", "Watches", "Runtime"]
                )
                popularity_data = (
                    df_genres_filtered.groupby("Genres")[popularity_metric]
                    .mean() if popularity_metric == "Runtime" else df_genres_filtered.groupby("Genres")[popularity_metric].sum()
                ).sort_values(ascending=False).head(genre_limit).reset_index()

                fig3 = px.bar(
                    popularity_data,
                    x="Genres",
                    y=popularity_metric,
                    title=f"{popularity_metric} by Genre",
                    labels={"Genres": "Genre", popularity_metric: popularity_metric},
                    color="Genres"
                )
                st.plotly_chart(fig3, use_container_width=True)

                st.markdown("---")

                st.subheader("And, finally, here is the last graph in this section...")

                # --- Chart 3: Top Fan-Favourite Films with Genres ---
                genre_fans = df.groupby(["Film_title", "Genres"])["Fans"].sum().nlargest(genre_limit).reset_index()

                fig3 = px.bar(
                    genre_fans,
                    x="Fans",
                    y="Film_title",
                    color="Genres",
                    title=f"Top {genre_limit} Fan-Favourite Films and Their Genres",
                    labels={"Fans": "Fan Count", "Film_title": "Film Title"}
                )
                fig3.update_layout(yaxis=dict(autorange="reversed"))
                st.plotly_chart(fig3, use_container_width=True)

                st.markdown("---")

            elif page == 'Studios Behind the Success':
                df = pd.read_csv('datasets/Letterbox Movie Classification Dataset.csv')

                st.title("Studios Behind the Success")
                st.markdown("""
                            Ever wondered who’s pulling the strings behind your favorite films? 
                            In this section, I explore which studios are truly making movie magic — and which ones are just... 
                            showing up with snacks. From average ratings to total likes and fan love, 
                            let’s see which studios are the real MVPs (Movie-Valuing Producers 😄).""")
                
                st.write(df)
                st.markdown("---")

                # --- Sidebar Filter ---
                st.sidebar.header("Chart Settings")
                top_n = st.sidebar.slider("Select number of top films to show", min_value=5, max_value=50, value=25)

                # --- Chart 1: Top Films by Ratings and Studios ---
                ratings_studio = df.groupby(["Film_title", "Studios"])["Total_ratings"]\
                    .sum().nlargest(top_n).reset_index()
                ratings_studio["Label"] = ratings_studio["Film_title"] + " (" + ratings_studio["Studios"] + ")"

                fig1 = px.bar(
                    ratings_studio,
                    x="Total_ratings",
                    y="Label",
                    orientation="h",
                    title=f"Top {top_n} Highest Rated Films and Their Studios",
                    labels={"Total_ratings": "Total Ratings", "Label": "Film (Studio)"},
                    color="Total_ratings",
                    color_continuous_scale="purp"
                )
                fig1.update_layout(yaxis=dict(autorange="reversed"))
                st.plotly_chart(fig1, use_container_width=True)

                st.markdown("---")

                # --- Chart 2: Top Films by Ratings and Directors ---
                ratings_director = df.groupby(["Film_title", "Director"])["Total_ratings"]\
                    .sum().nlargest(top_n).reset_index()
                ratings_director["Label"] = ratings_director["Film_title"] + " (" + ratings_director["Director"] + ")"

                fig2 = px.bar(
                    ratings_director,
                    x="Total_ratings",
                    y="Label",
                    orientation="h",
                    title=f"Top {top_n} Highest Rated Films and Their Directors",
                    labels={"Total_ratings": "Total Ratings", "Label": "Film (Director)"},
                    color="Total_ratings",
                    color_continuous_scale="purp"
                )
                fig2.update_layout(yaxis=dict(autorange="reversed"))
                st.plotly_chart(fig2, use_container_width=True)

                st.markdown("---")

                # --- Chart 4: Most Watched Movies ---
                most_watched = df.groupby("Film_title")["Watches"].sum().nlargest(top_n).reset_index()

                fig4 = px.bar(
                    most_watched,
                    x="Film_title",
                    y="Watches",
                    title=f"Top {top_n} Most Watched Movies",
                    color="Watches",
                    color_continuous_scale="purp"
                )
                fig4.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig4, use_container_width=True)

                st.markdown("---")

                # --- Chart 5: Movies with Most Fans ---
                most_fans = df.groupby(["Film_title", "Genres"])["Fans"].sum().nlargest(top_n).reset_index()

                fig5 = px.bar(
                    most_fans,
                    x="Film_title",
                    y="Fans",
                    title=f"Top {top_n} Most Followed Movies (Fan Count)",
                    color="Fans",
                    color_continuous_scale="purp",
                    labels={"Fans": "Fan Count", "Film_title": "Film Title"},
                    hover_data=["Genres"]  # Show genres only on hover
                )
                fig5.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig5, use_container_width=True)

                st.markdown("---")

                # --- Chart 6: Most Liked Movies ---
                most_liked = df.groupby("Film_title")["Likes"].sum().nlargest(top_n).reset_index()

                fig6 = px.bar(
                    most_liked,
                    x="Film_title",
                    y="Likes",
                    title=f"Top {top_n} Most Liked Movies",
                    color="Likes",
                    color_continuous_scale="purp"
                )
                fig6.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig6, use_container_width=True)

                st.markdown("---")

            elif page == 'Rating-Based Film Rankings':
                
                df = pd.read_csv('datasets/Letterbox Movie Classification Dataset.csv')

                st.title("Rating-Based Film Rankings")
                st.markdown("""
                            Not all stars shine equally in the film world! In this section, I explore how movies 
                            stack up based on the number of 1-star, 3-star, and glorious 5-star ratings they’ve received — plus 
                            their total rating count. Whether it's universally adored or a beautiful disaster, each chart helps 
                            uncover how the audience really felt. Spoiler alert: not every "classic" is beloved by the crowd 😅.""")
                
                st.write(df)
                st.markdown("---")

                st.subheader("Chart Settings")

                # --- Film count slider ---
                top_n_rating = st.slider("Select number of top films to display", min_value=5, max_value=50, value=25)

                # --- 1 Star Rated ---
                lowest_rated = (
                    df.groupby("Film_title")["Lowest★"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(top_n_rating)
                    .reset_index()
                )

                fig1 = px.bar(
                    lowest_rated,
                    x="Film_title",
                    y="Lowest★",
                    title=f"Top {top_n_rating} Lowest 1★ Rated Films",
                    labels={"Lowest★": "1 Star Ratings", "Film_title": "Film Title"},
                    color="Lowest★",
                    color_continuous_scale="purp"
                )
                fig1.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig1, use_container_width=True)

                st.markdown("---")

                # --- 3 Star Rated ---
                medium_rated = (
                    df.groupby("Film_title")["Medium★★★"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(top_n_rating)
                    .reset_index()
                )

                fig2 = px.bar(
                    medium_rated,
                    x="Film_title",
                    y="Medium★★★",
                    title=f"Top {top_n_rating} Medium 3★ Rated Films",
                    labels={"Medium★★★": "3 Star Ratings", "Film_title": "Film Title"},
                    color="Medium★★★",
                    color_continuous_scale="purp"
                )
                fig2.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig2, use_container_width=True)

                st.markdown("---")

                # --- 5 Star Rated ---
                highest_rated = (
                    df.groupby("Film_title")["Highest★★★★★"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(top_n_rating)
                    .reset_index()
                )

                fig3 = px.bar(
                    highest_rated,
                    x="Film_title",
                    y="Highest★★★★★",
                    title=f"Top {top_n_rating} Highest 5★ Rated Films",
                    labels={"Highest★★★★★": "5 Star Ratings", "Film_title": "Film Title"},
                    color="Highest★★★★★",
                    color_continuous_scale="purp"
                )
                fig3.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig3, use_container_width=True)

                st.markdown("---")

                # --- Total Ratings ---
                total_rated = (
                    df.groupby("Film_title")["Total_ratings"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(top_n_rating)
                    .reset_index()
                )

                fig4 = px.bar(
                    total_rated,
                    x="Film_title",
                    y="Total_ratings",
                    title=f"Top {top_n_rating} Films by Total Ratings",
                    labels={"Total_ratings": "Total Ratings", "Film_title": "Film Title"},
                    color="Total_ratings",
                    color_continuous_scale="purp"
                )
                fig4.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig4, use_container_width=True)

       # elif selected == "Student Habits vs Academic Performance":
            page = st.sidebar.selectbox('Choose a page:',
                                            ['DataSet',
                                            'Basic Analysis',
                                            'Location',
                                            'Payment Methods'])
            if page == 'DataSet':
                df = pd.read_csv("datasets/student_habits_performance.csv")
                st.title("👩🏻‍🎓 Student Habits vs Academic Performance")
                st.markdown("""
                            Ever wondered how much Netflix, sleep, or TikTok scrolling affects your grades? 👀
                            
                            This dataset shows how students’ daily habits — like how much they study, how often 
                            they attend classes, and whether they’re early birds or night owls — affect their 
                            academic performance.

                            It includes things like:

                            - Study hours (a.k.a. how long they stared at the book before scrolling TikTok again),
                            - Attendance (because showing up is half the battle, right?),
                            - Gender, sleep habits, and of course,
                            - Their Performance score (the final boss of all this effort).

                            I used this dataset to explore if habits actually matter — or if some students are 
                            just naturally lucky. Spoiler: attending classes might still be useful 😅""")
                st.write(df)
                st.markdown("---")
                st.markdown("## Details")
                st.write("**Title**: Student Habits vs Academic Performance ",
                        "<br>**Rows**: 1000",
                        "<br>**Columns**: 16",
                        unsafe_allow_html=True)
                st.markdown('## Data Dictionary')
                st.markdown("""
                            📌 **student_id** – Unique identifier for each student.<br>
                            📌 **age** – Student’s age.<br>
                            📌 **gender** – Gender of the student (e.g., Male, Female, Other).<br>
                            📌 **study_hours_per_day** – Average number of hours spent studying per day.<br>
                            📌 **social_media_hours** – Time spent scrolling and liking – includes TikTok, Instagram, etc.<br>
                            📌 **netflix_hours** – How long the student spends binge-watching Netflix per day.<br>
                            📌 **part_time_job** – Whether the student has a part-time job (Yes/No).<br>
                            📌 **attendance_percentage** – Class attendance percentage. Skipping class?<br>
                            📌 **sleep_hours** – Average sleep per night.<br>
                            📌 **diet_quality** – Rating of their diet (e.g., Poor, Average, Excellent). Pizza doesn’t count as a veggie!<br>
                            📌 **exercise_frequency** – How often the student exercises (times per week).<br>
                            📌 **parental_education_level** – Highest education level of the student’s parents.<br>
                            📌 **internet_quality** – Self-rated quality of their internet connection (Slow, Medium, Fast).<br>
                            📌 **mental_health_rating** – How the student rates their mental health on a scale.<br>
                            📌 **extracurricular_participation** – Whether the student takes part in activities beyond class (clubs, sports, etc.).<br>
                            📌 **exam_score** – Final exam score.
                            """, unsafe_allow_html=True)
                st.markdown("---")

            # elif page == 'Basic Analysis':
                
    elif selected == "Tableau":
        selected_optipns = ["1. Sales Dashboard: Food & Beverages",
                            "2. Sales & Customer Analysis",
                            "3. Tube Map Kyiv",
                            "4. Car Sales Analysis"]
        selected = st.selectbox("Select a project", options = selected_optipns)
        st.write("Current selection:", selected)
        if selected == "1. Sales Dashboard: Food & Beverages":
            st.title('Sales Dashboard: Food & Beverages')
            st.markdown("## **[Project - 1](https://public.tableau.com/app/profile/julie.shcherbyna/viz/SalesAnalysis_17551785285480/Dashboard1)**")
            st.write("In this project I used the dataset presented below:")
            df = pd.read_csv('datasets/sales_analysis.csv')
            st.write(df)
            st.markdown("""
                        This dashboard provides a comprehensive overview of **sales performance** across categories, products, regions, and customers.  

                        #### *Key Features*:
                        - **Profit by Categories** – bar chart showing which product categories generate the highest profit.  
                        - **Top 5 Products** – ranking of the most profitable products.  
                        - **Profit by Regions** – comparison of regional sales performance.  
                        - **Regional Share** – pie chart visualizing each region’s contribution to total profit.  
                        - **Quarterly Profit** – trend analysis of profit dynamics by quarters across different years.  
                        - **Customer Profitability** – profit distribution by customers with percentage contribution.  
                        - **City Information (Map)** – geographic visualization displaying profits by major European cities.  

                        #### *Interactivity*:
                        The dashboard includes filters for **city, region, customer, category, and year** to allow users to dynamically explore the dataset and customize the view.  

                        #### *Value*:
                        This dashboard helps to:  
                        - identify the most profitable categories and regions,  
                        - monitor performance trends over time,  
                        - and better understand customer contributions.  
                        """)
            st.image(Image.open("images/t1.png"))

        elif selected == "2. Sales & Customer Analysis":
            st.title('Sales & Customer Analysis')
            st.markdown("## **[Project - 2](https://public.tableau.com/app/profile/julie.shcherbyna/viz/SalesCustomerAnalysis_17552719229610/SalesDashboard)**")
            st.write("In this project I used 4 datasets (Costomers, Location, Orders, Products).")
            st.markdown("The first dashboard was created to depict **Sales Analysis**.")
            st.image(Image.open("images/t2.png"))
            st.markdown("""
                        #### *Created Calculated Fields*:
                        - **Current/Previous Year Metrics** – to compare key performance indicators across different years.
                        - **Percentage Difference** – to measure growth or decline between periods.
                        - **Min/Max Values** – to highlight the highest and lowest sales, profit, and quantity values.
                        
                        #### *Visualizations*:
                        - **Total Sales, Total Profit, Total Quantity** – provides an overall view of business performance.
                        - **Sales & Profit by Subcategory** – helps identify which product categories contribute most to revenue and profit.
                        - **Sales & Profit Trends over Time** – shows performance trends, enabling analysis of seasonality and growth patterns.  
                        """)
            st.markdown("The second dashboard was created to depict **Customer Analysis**.")
            st.image(Image.open("images/t3.png"))
            st.markdown("""
                        #### *Created Calculated Fields*:
                        - **Current/Previous Year Metrics** – to compare key performance indicators across different years.
                        - **Percentage Difference** – to measure growth or decline between periods.
                        - **Min/Max Values** – to highlight the highest and lowest sales, profit, and quantity values.
                        
                        #### *Visualizations*:
                        - **Total Customers, Total Sales per Customer, Total Orders** – provides an overview of customer activity and revenue contribution.
                        - **Customer Distribution by Nr. of Orders** – shows how frequently customers make purchases, helping identify loyal vs. occasional buyers.
                        - **Top 10 Customers by Profit** – highlights the most profitable customers, useful for targeted marketing and relationship management. 
                        """)
            st.markdown("And You can also open **Filter Section**.")
            st.image(Image.open("images/t4.png"))
            st.markdown("""
                        #### *Interactivity*:
                        The dashboard includes filters for **category, sub-category, year, region, state and city** to allow users to dynamically explore the dataset and customize the view.""")

        elif selected == "3. Tube Map Kyiv":
            st.title('Tube Map Kyiv')
            st.markdown("## **[Project - 3](https://public.tableau.com/app/profile/julie.shcherbyna/viz/TubeMapKyiv/sheet2)**")
            st.write("In this project I used the dataset presented below with the name of the station:")
            df = pd.read_csv('datasets/tube.csv')
            st.dataframe(df.drop(columns=["Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9"])) 
            st.markdown("""
                        #### *Created Calculated Fields*:
                        - **Geocoded Station Names** – to map each Kyiv station to its geographic location.

                        #### *Visualizations*:
                        - **Interactive Map of Kyiv Stations** – displays all stations on a city map, enabling spatial analysis and exploration.
                        """)
            st.image(Image.open("images/t5.png"))

        elif selected == "4. Car Sales Analysis":
            st.title('Car Sales Analysis')
            st.markdown("## **[Project - 4](https://public.tableau.com/app/profile/julie.shcherbyna/viz/Book1_17555904414740/Dashboard1)**")
            st.write("In this project I used the dataset presented below:")
            df = pd.read_csv('datasets/Car-Sales-Data.csv')
            st.write(df)
            st.markdown("""
                        #### *Created Calculated Fields*:
                        - **YTD/PYTD Sales, Cars Sold, Average Price** – to track year-to-date performance compared to the previous year.
                        - **YoY Sales, Cars Sold, Average Price** – to measure year-over-year growth and performance trends.

                        #### *Visualizations*:
                        - **YTD Sales Monthly Trend** – shows how sales evolve month by month within the current year.
                        - **Sales Distribution by Region** – provides insights into regional performance differences.
                        - **Total Sales by Car Body Type** – highlights which car body types contribute the most to sales volume.
                        - **Annual Revenue Distribution by Company** – compares revenue across companies on a yearly basis.
                        """)
            st.image(Image.open("images/t6.png"))

    elif selected == "R":
        selected_optipns = ["Data Input and Output in R",
                            "Data Loading and its Description in R",
                            "Descriptive Analytics",
                            "Probability Distributions of Random Variables",
                            "Statistical Hypothesis Testing",
                            "Exploratory Analytics. Using Basic Graphics Package",
                            "Advanced Visual Analytics Tools"]
        selected = st.selectbox("Select a project", options = selected_optipns)
        st.write("Current selection:", selected)
        if selected == "Data Input and Output in R":
            st.title("Data Input and Output in R")
            # 1
            st.write("**1. A code that asks the user for their name and displays a message like 'Hello, name!**")
            code = """
            name <- readline(prompt = "Enter your name: ")
            cat("Hello, ", name, "!", sep = "")"""
            st.code(code, language='r')
            # 2.1
            st.write("**2.1 A code that asks the user to input two floating-point numbers (one number – one input) "
            "and displays their sum on the screen. The user enters floating-point numbers using a dot as the decimal separator.**")
            code = """
            num1 <- as.numeric(readline(prompt = "Введіть перше дробове число (через крапку): ")) 
num2 <- as.numeric(readline(prompt = "Введіть друге дробове число (через крапку): "))
            
sum_result <- num1 + num2
cat("Сума чисел", num1, "та", num2, "дорівнює", sum_result)"""
            st.code(code, language='r')
            # 2.2
            st.write("**2.2 A code that asks the user to input two floating-point numbers (one number – one input) "
            "and displays their sum on the screen. The user enters floating-point numbers using a comma as the decimal separator.**")
            code = """
            num1 <- readline(prompt = "Введіть перше дробове число (через кому): ")
num2 <- readline(prompt = "Введіть друге дробове число (через кому): ")

num1 <- as.numeric(gsub(",", ".", num1))
num2 <- as.numeric(gsub(",", ".", num2))

sum_result <- num1 + num2
cat("Сума чисел", num1, "та", num2, "дорівнює", sum_result)"""
            st.code(code, language='r')
            # 3
            st.write("**3. A code that asks the user to enter a speed value in kilometers per hour and displays the speed in meters per second.**")
            code = """
            kmph <- as.numeric(readline(prompt = "Введіть швидкість в кілометрах на годину (км/год): "))

mps <- kmph * (1000 / 3600)

cat("Швидкість в метрах на секунду (м/c) дорівнює ", mps)"""
            st.code(code, language='r')
            # 4
            st.write("**4. Create a table with meaningful data in Excel that contains 5 rows and 3 columns with both numeric and character data, " \
            "as well as column names. Read this file in R from a CSV format.**")
            code = """
            data <- read.csv("/Users/julie/Desktop/lab2/olympics.csv", header = TRUE)
            data"""
            st.code(code, language='r')
            df_o = pd.read_csv('datasets/olympics.csv', sep=';')
            st.write(df_o)
            # 5.1
            st.write("**5.1 Create a data frame in R with meaningful data, containing 5 rows and 3 columns with both numeric and character data, " \
            "as well as column headers. Enter the table values by initializing three separate vectors.**")
            code = """
            ISBN <- c("978-617-679-832-3", "978-617-8203-81-8", "978-617-548-147-9", "978-617-8023-80-5", "978-617-7853-82-3")
            Title <- c("Я бачу вас цікавить пітьма", "За перекопом є земля", "Дім у волошковому морі", "Вавилон", "Макова війна")
            Author <- c("Іларіон Павлюк", "Анастасія Левкова", "Ті Джей Клун", "Ребекка Кван", "Ребекка Кван")

            books <- data.frame(ISBN, Title, Author, stringsAsFactors = FALSE)
            print(books)"""
            st.code(code, language='r')
            # 5.2
            st.write("**5.2 Enter the table values using a text editor and the edit() function.**")
            code = """
            new_books <- edit(books)
            print(new_books)"""
            st.code(code, language='r')
            st.image(Image.open("images/r1.png"))
            # 5.3
            st.write("**5.3 At first, export the result to a text file using the write.table() function. Then export the result to an " \
            "MS Excel file using the functions from the xlsReadWrite package.**")
            code = """
            write.table(new_books, file = "/Users/julie/Desktop/lab2/books.txt", sep = ",")
            
            write_xlsx(new_books, "/Users/julie/Desktop/lab2/books.xlsx")"""
            st.code(code, language='r')
            st.image(Image.open("images/r2.png"))
        
        elif selected == "Data Loading and its Description in R":
            st.title("Data Loading and its Description in R")
            # 1
            st.write("**1. Load data from the file firtree.csv, which contains the results of a fictional survey of visitors " \
            "to a Christmas tree market, and store it in the variable tree.**")
            code = """
            tree <- read.csv("firtree.csv", encoding = "UTF-8", header = TRUE, sep = ","  )
            head(tree)"""
            st.code(code, language='r')
            df_f = pd.read_csv('datasets/firtree.csv')
            st.write(df_f)
            # 2
            st.write("**2. Display the first rows of the dataset using the head() function.**")
            code = """
            head(tree)"""
            st.code(code, language='r')
            st.write(df_f.head())
            # 3
            st.write("**3. Display the first 8 rows of the tree dataset.**")
            code = """
            head(tree, 8)"""
            st.code(code, language='r')
            st.write(df_f.head(8))
            # 4
            st.write("**4. Display the last rows of the dataset using the tail() function.**")
            code = """
            tail(tree)"""
            st.code(code, language='r')
            st.write(df_f.tail())
            # 5
            st.write("**5. Display the last 10 rows in a separate window using the View() function.**")
            code = """
            last_10_rows <- tail(tree, 10)
            View(last_10_rows)"""
            st.code(code, language='r')
            st.write(df_f.tail(10))
            # 6
            st.write("**6. Determine the dimensions of the dataset (number of rows and columns) using the dim() function.**")
            code = """
            dim(tree)"""
            st.code(code, language='r')
            rows, columns = df_f.shape
            st.write(f"The dataset has {rows} rows and {columns} columns.")
            # 7
            st.write("**7. Determine the number of rows and columns separately using the nrow() and ncol() functions.**")
            code = """
            nrow(tree)
            ncol(tree)"""
            st.code(code, language='r')
            st.write(f"The dataset has {df_f.shape[0]} rows and {df_f.shape[1]} columns")
            # 8
            st.write("**8. Get the full technical structure of the dataset using the str() function. What type of data is stored in each field of the dataset?**")
            code = """
            str(tree)"""
            st.code(code, language='r')
            st.write(df_f.dtypes)
            st.markdown(""" 
            - **integer** – whole number
            - **character** – string (text) type""")
            # 9
            st.write("**9. Check if the dataset contains any missing values.**")
            code = """
            any(is.na(tree))
            sum(is.na(tree))"""
            st.code(code, language='r')
            has_na = df_f.isnull().values.any()
            st.write(f"Чи є пропущені значення у датасеті? **{has_na}**")

            total_na = df_f.isnull().sum().sum()
            st.write(f"Загальна кількість пропущених значень: **{total_na}**")
            # 10
            st.write("**10. Knowing the columns and row indices (IDs) that contain missing values, print the specific 'empty' elements to confirm that they are truly missing.**")
            code = """
            wish_47 <- tree$wish[47]
wish_20 <- tree$wish[20]

print(paste("Значення у рядку 47 стовпця 'wish':", wish_47))
print(paste("Значення у рядку 20 стовпця 'wish':", wish_20))"""
            st.code(code, language='r')
            # 11
            st.write("**11. Replace missing values with NA during data import so that R treats them as valid missing data.**")
            code = """
            tree <- read.csv("firtree.csv", encoding = "UTF-8", header = TRUE, sep = ",", na.strings = "") 
            View(tree)"""
            st.code(code, language='r')
            # 12
            st.write("**12. Count the number of rows in the dataset that contain missing values..**")
            code = """
            empty <- complete.cases(tree)
            num_rows_with_na <- sum(!empty)
            print(paste("Кількість рядків, що містять пропущені значення:", num_rows_with_na))"""
            st.code(code, language='r')
            # 13
            st.write("**13. Since R treats TRUE as 1 and FALSE as 0, use sum(complete.cases()) to count the complete rows.**")
            code = """
            num_complete_rows <- sum(complete.cases(tree))
print(paste("Кількість рядків без пропущених значень:", num_complete_rows))

num_rows_with_na <- sum(!complete.cases(tree))
print(paste("Кількість рядків з пропущеними значеннями:", num_rows_with_na))"""
            st.code(code, language='r')
            # 14
            st.write("**14. Use another way to identify missing values — the is.na() function.**")
            code = """
            missing_values <- is.na(tree)
head(missing_values)

total_na <- sum(missing_values)
print(paste("Загальна кількість пропущених значень:", total_na))"""
            st.code(code, language='r')
            # 15
            st.write("**15. Load the installed libraries (VIM and mice) and display plots that show which variables have the most " \
            "missing values and what the pattern of missing values in the dataset looks like.**")
            code = """
            library(VIM)
            aggr(tree, numbers = TRUE, prop = TRUE, cex.axis = 0.7)"""
            st.code(code, language='r')
            st.image(Image.open("images/r3.png"))
            st.markdown("""
                        - The plot on the left shows how frequently missing values occur in each variable. 
                        
                        - The plot on the right shows in which combinations these missing values appear.""")
            # 16 
            st.write("**16. Use the matrixplot function from the mice package.**")
            code = """
            library(mice)
            matrixplot(tree)"""
            st.code(code, language='r')
            st.image(Image.open("images/r4.png"))
            st.markdown("""
                        The resulting plot visualizes the completeness of observations (missing values are marked in red, while the rest are 
                        observed values; the darker the color, the higher the value). 
                        The vertical axis represents the row number in the data frame, i.e., the observation ID.""")
            # 17
            st.write("**17. Use the matrixplot() function to visualize missing values in the dataset test.**")
            code = """
            library(mice)
test <- cbind.data.frame(a = c(NA, 2, 3), b = c(NA, NA, 1))
sum(!complete.cases(test))
sum(is.na(test))
matrixplot(test)"""
            st.code(code, language='r')
            st.image(Image.open("images/r5.png"))

        elif selected == "Descriptive Analytics":
            st.title("Descriptive Analytics")
            # 1
            st.write("**1. Create a variable lvl that contains the following numeric elements. Now perform the sum, mean, median, length and sd.**")
            code = """
            lvl <- c(8, 10, 10, 1, 10, 10, 8, 12, 1, 12)

            cat("Сума елементів:", sum(lvl))
            cat("Середнє значення елементів:", mean(lvl))
            cat("Медіана елементів:", median(lvl))
            cat("Довжина змінної:", length(lvl))
            cat("Стандартне відхилення:", sd(lvl))
            cat("Округлене стандартне відхилення:", round(sd(lvl), 2))"""
            st.code(code, language='r')
            lvl = [8, 10, 10, 1, 10, 10, 8, 12, 1, 12]
            st.write("Сума елементів:", np.sum(lvl))
            st.write("Середнє значення елементів:", np.mean(lvl))
            st.write("Медіана елементів:", np.median(lvl))
            st.write("Довжина змінної:", len(lvl))
            st.write("Стандартне відхилення:", np.std(lvl, ddof=1))
            st.write("Округлене стандартне відхилення:", round(np.std(lvl, ddof=1), 2))
            # 2
            st.markdown("""**2. Imagine you are tracking the mileage of a car after each refueling. 
                        After the last eight refuelings, the mileage was recorded. Enter these numbers into R. What do you get as a result? We see the number of miles between refuelings. 
                        Use the max(), mean(), and min() functions to calculate the maximum, 
                        average, and minimum mileage between refuelings.**""")
            code = """
            mileage <- c(65311, 65624, 65908, 66219, 66499, 66821, 67145, 67447)

            cat("Пробіг між заправками:", diff(mileage))

            cat("Максимальний пробіг між заправками:", max(diff(mileage)))
            cat("Середній пробіг між заправками:", mean(diff(mileage)))
            cat("Мінімальний пробіг між заправками:", min(diff(mileage)))"""
            st.code(code, language='r')
            mileage = np.array([65311, 65624, 65908, 66219, 66499, 66821, 67145, 67447])
            mileage_diff = np.diff(mileage)
            st.write("Пробіг між заправками:", ", ".join(str(x) for x in mileage_diff))
            st.write()
            st.write("Максимальний пробіг між заправками:", mileage_diff.max())
            st.write("Середній пробіг між заправками:", mileage_diff.mean())
            st.write("Мінімальний пробіг між заправками:", mileage_diff.min())
            # 3
            st.markdown("""**3. Suppose you need to buy equipment for your factory and you have 2 options to choose from. 
                        Before making the final decision, you collected 10 performance measurements for each option. 
                        If your final decision was based on these measurements, which equipment would you choose?**""")
            code = """
            equip1 <- c(151.2, 150.5, 149.2, 147.5, 152.9, 152.0, 151.3, 149.7, 149.4, 150.7)
            equip2 <- c(151.9, 151.4, 150.3, 151.2, 151.0, 150.2, 151.2, 151.4, 150.4, 151.7)

            cat("Середнє значення устаткування 1:", mean(equip1))
            cat("Середнє значення устаткування 2:", mean(equip2))

            if (mean(equip1) > mean(equip2)) {
                cat("Устаткування 1 є кращим вибором.")
            } else if (mean(equip1) < mean(equip2)) {
                cat("Устаткування 2 є кращим вибором.")
            } else {
                cat("Обидва устаткування мають однакове середнє значення.")
            }"""
            st.code(code, language='r')
            equip1 = np.array([151.2, 150.5, 149.2, 147.5, 152.9, 152.0, 151.3, 149.7, 149.4, 150.7])
            equip2 = np.array([151.9, 151.4, 150.3, 151.2, 151.0, 150.2, 151.2, 151.4, 150.4, 151.7])
            mean1 = np.mean(equip1)
            mean2 = np.mean(equip2)
            st.write("Середнє значення устаткування 1:", round(mean1, 2))
            st.write("Середнє значення устаткування 2:", round(mean2, 2))
            if mean1 > mean2:
                st.success("Устаткування 1 є кращим вибором.")
            elif mean1 < mean2:
                st.success("Устаткування 2 є кращим вибором.")
            else:
                st.info("Обидва устаткування мають однакове середнє значення.")
            # 4
            st.markdown("""**4. Create a vector of the heights of twenty students in a class. Which student is in the middle 
                        of this list (by height)? Which height is the most frequent? Calculate these values using descriptive analytics tools in R.**""")
            code = """
            heights <- c(100, 106, 121, 111, 109, 111, 103, 117, 114, 108, 111, 105, 120, 116, 104, 103, 108, 111, 101, 120)
            # Який учень знаходиться посередині цього списку (за зростом)?
            median_height <- median(heights)
            cat("Зріст учня посередині:", median_height)

            # Який зріст є найбільш популярним?
            mode_height <- as.numeric(names(sort(table(heights), decreasing = TRUE)[1]))
            cat("Найбільш популярний зріст:", mode_height)"""
            st.code(code, language='r')
            heights = [100, 106, 121, 111, 109, 111, 103, 117, 114, 108, 111, 105, 120, 116, 104, 103, 108, 111, 101, 120]
            sorted_heights = sorted(heights)
            n = len(sorted_heights)
            if n % 2 == 1:
                median_height = sorted_heights[n // 2]
            else:
                median_height = (sorted_heights[n // 2 - 1] + sorted_heights[n // 2]) / 2
            counts = {}
            for h in heights:
                counts[h] = counts.get(h, 0) + 1
            mode_height = max(counts, key=counts.get)
            st.write("Зріст учня посередині (медіана):", median_height)
            st.write("Найбільш популярний зріст (мода):", mode_height)
            # 5
            st.markdown("""**5. Calculate quantiles, quartiles, the interquartile range (IQR), and the standard error based on the data 
                        from the previous task.**""")
            code = """
            cat("Квантилі:", quantile(heights))

            quartiles <- quantile(heights, probs = c(0.25, 0.75))
            cat("Перший квартиль (Q1):", quartiles[1])
            cat("Перший квартиль (Q2):", median(heights))
            cat("Третій квартиль (Q3):", quartiles[2])

            cat("Міжквартильний розмах (IQR):", IQR(heights))

            cat("Стандартна похибка:", sd(heights))"""
            st.code(code, language='r')
            heights = [100, 106, 121, 111, 109, 111, 103, 117, 114, 108,
                    111, 105, 120, 116, 104, 103, 108, 111, 101, 120]
            quantiles = np.quantile(heights, [0, 0.25, 0.5, 0.75, 1])
            Q1 = quantiles[1]
            Q2 = quantiles[2]
            Q3 = quantiles[3]
            IQR = Q3 - Q1
            std_dev = np.std(heights, ddof=1)
            se = std_dev / np.sqrt(len(heights))
            df_quartiles = pd.DataFrame({
                'Percentile': ['0%', '25%', '50%', '75%', '100%'],
                'Height': quantiles
            })
            st.write("Квартилі та відповідні відсотки")
            st.table(df_quartiles)
            st.write("Перший квартиль (Q1):", Q1)
            st.write("Медіана (Q2):", Q2)
            st.write("Третій квартиль (Q3):", Q3)
            st.write("Міжквартильний розмах (IQR):", IQR)
            st.write("Стандартне відхилення:", std_dev)
            st.write("Стандартна похибка:", se)
            # 6 
            st.markdown("""**6. Calculate the standard deviation for the data from task 4 using the formula, 
                        and compare the result with the sd() function. Are the results the same?**""")
            code = """
            cat("Стандартне відхилення за допомогою sd():", sd(heights))

            variance <- sum((heights - mean(heights))^2) / length(heights)  
            std_dev <- sqrt(variance)  

            cat("Стандартне відхилення за формулою:", std_dev)

            if (identical(round(sd(heights), 4), round(std_dev, 4))) {
            cat("Результати однакові.")
            } else {
            cat("Результати різняться.")"""
            st.code(code, language='r')
            heights = [100, 106, 121, 111, 109, 111, 103, 117, 114, 108,
                    111, 105, 120, 116, 104, 103, 108, 111, 101, 120]
            std_numpy = np.std(heights, ddof=1)
            mean_height = np.mean(heights)
            variance_manual = sum((x - mean_height) ** 2 for x in heights) / len(heights)
            std_manual = np.sqrt(variance_manual)
            st.write("Стандартне відхилення за допомогою np.std:", std_numpy)
            st.write("Стандартне відхилення за формулою:", std_manual)
            if round(std_numpy, 4) == round(std_manual, 4):
                st.success("Результати однакові.")
            else:
                st.warning("Результати різняться.")
            # 7
            st.markdown("""**7. Load data from two columns of a table into two vectors. Determine the skewness of the data 
                        visually using exploratory analytics tools, and using descriptive statistics metrics. Interpret the results.**""")
            code = """
            column1 <- c(212, 869, 220, 654, 511, 624, 420, 121, 428, 865, 
                        799, 405, 230, 670, 870, 366, 99, 55, 489, 312, 
                        493, 163, 221, 84, 144, 48, 375, 86, 168, 100)

            column2 <- c(586, 760, 495, 678, 559, 415, 370, 659, 119, 288, 
                        241, 787, 522, 207, 160, 526, 656, 848, 720, 676, 
                        581, 929, 653, 661, 770, 800, 529, 975, 995, 947)

            par(mfrow = c(1, 2))
            hist(column1, main = "Гістограма колонки 1", xlab = "Значення", col = "lightblue", border = "black")
            hist(column2, main = "Гістограма колонки 2", xlab = "Значення", col = "lightgreen", border = "black")

            install.packages("moments")
            library(moments)

            cat("Скошеність колонки 1:", skewness(column1))
            cat("Скошеність колонки 2:", skewness(column2))

            cat("Cкошеність колонки 1 дорівнює 1.5, а колонки 2 дорівнює -0.5, 
                це вказує на те, що перша колонка має правосторонню скошеність, 
                а друга - лівосторонню скошеність.")"""
            st.code(code, language='r')
            column1 = [212, 869, 220, 654, 511, 624, 420, 121, 428, 865, 
                    799, 405, 230, 670, 870, 366, 99, 55, 489, 312, 
                    493, 163, 221, 84, 144, 48, 375, 86, 168, 100]

            column2 = [586, 760, 495, 678, 559, 415, 370, 659, 119, 288, 
                    241, 787, 522, 207, 160, 526, 656, 848, 720, 676, 
                    581, 929, 653, 661, 770, 800, 529, 975, 995, 947]
            skew1 = skew(column1)
            skew2 = skew(column2)
            st.write("Скошеність колонки 1:", skew1)
            st.write("Скошеність колонки 2:", skew2)
            st.markdown("""
                        Скошеність **колонки 1** дорівнює приблизно **1.5**, а **колонки 2** — приблизно **-0.5**, 
                        що вказує на те, що перша колонка має **правосторонню скошеність**, 
                        а друга — **лівосторонню скошеність**.""")
            st.image(Image.open("images/r6.png"))

        elif selected == "Probability Distributions of Random Variables":
            st.title("Probability Distributions of Random Variables")
            # 1
            st.write("""**1. An insurance company has 500 life insurance contracts with 500 clients. 
                     The probability of an insured event occurring in this group of clients is the same and equals 0.002. 
                     The payout amount to each client is the same and equals 40,000 UAH. What is the probability distribution 
                     law of the random variable representing the number of insured events? Plot the distribution graph of the total 
                     payout amount by the insurance company. Calculate the probability that the insurance company will pay its clients 
                     no more than 100,000 UAH.**""")
            code = """
            n <- 500 
            p <- 0.002
            per_person <- 40000 
            max <- 100000 

            # Кількість страхових випадків розподілена за законом біноміальному розподілу
            probs <- dbinom(0:n, size = n, prob = p)
            payout <- 0:n * per_person

            plot(payout, probs, type = "l", 
                main = "Розподіл сумарних виплат страхової компанії",
                xlab = "Сума виплат (грн)", ylab = "Ймовірність")

            prob_payout <- pbinom(max/per_person, size = n, prob = p)
            cat("Ймовірність, що виплати не перевищать 100 тис. грн:", prob_payout)"""
            st.code(code, language='r')
            n = 500
            p = 0.002
            per_person = 40000
            max_payout = 100000
            x = np.arange(n + 1)
            probs = binom.pmf(x, n, p)
            payout = x * per_person
            max_cases = max_payout // per_person
            prob_payout = binom.cdf(max_cases, n, p)
            st.write("Ймовірність, що виплати не перевищать 100 тис. грн:", prob_payout)
            st.image(Image.open("images/r7.png"))
            # 2
            st.write("**2. Plot the binomial distribution with parameters n = 1000 and p = 0.25.**")
            code = """
            n <- 1000  
            p <- 0.25  
            size <- 10000

            rbinom(size, size = n, prob = p)
            hist(rbinom(size, size = n, prob = p), col = "lightblue",
                main = "Біноміальний закон розподілу")"""
            st.code(code, language='r')
            st.image(Image.open("images/r8.png"))
            # 3
            st.write("**3. Generate 100 random numbers and graphically display the Poisson distribution with parameter λ = 10.**")
            code = """
            rpois(n=100, lambda=10)

            plot(rpois(n=100, lambda=10), type='s', col = "lightgreen",
                ylab = "Розподіл",
                main = "Гістограма розподілу Пуассона")"""
            st.code(code, language='r')
            st.image(Image.open("images/r9.png"))
            # 4
            st.write("""**4. Calculate the probability that a random variable distributed according to the Poisson distribution 
                     with parameter λ = 7 takes values in the interval [5; 10].**""")
            code = """
            cat("Ймовірність того, що випадкова величина буде в межах [5; 10]:"
                , ppois(10, lambda = 7) - ppois(5, lambda = 7))"""
            st.code(code, language='r')
            lambda_ = 7
            prob = poisson.cdf(10, lambda_) - poisson.cdf(4, lambda_)
            st.write("Ймовірність того, що випадкова величина буде в межах [5; 10]:", prob)
            # 5
            st.write("""**5. Plot the cumulative distribution function and the probability density function 
                     of a uniformly distributed random variable on the interval [15; 25].**""")
            code = """
            ?dunif
            ru = runif(n = 100, max = 100)
            hist(ru, main = 'Гістограма', col = 'darkolivegreen1')

            plot(dunif(ru, min = 15, max = 25), type = 'h', main = 'Щільність розподілу')
            plot(punif(ru, min = 15, max = 25), type = 'h', main = 'Функція розподілу')"""
            st.code(code, language='r')
            st.image(Image.open("images/r10.png"))
            st.image(Image.open("images/r11.png"))
            st.image(Image.open("images/r12.png"))
            # 6
            st.write("""**6. Generate 500 uniformly distributed random variables in the range from 50 to 100. 
                     Graphically display the resulting distribution.**""")
            code = """
            u <- runif(n= 0:500, min = 50, max = 100)
            names(u) = c(0:500)
            u

            hist(u, col = "darkslategray", border = "black",
                main = "Розподіл випадкових величин",
                xlab = "Значення", ylab = "Частота")"""
            st.code(code, language='r')
            st.image(Image.open("images/r13.png"))
            # 7
            st.write("""**7. Generate a sample of 50 values of a random variable distributed according to the exponential 
                     distribution law with parameter λ = 105. Graphically display the exponential distribution with this parameter.**""")
            code = """
            exp_data <- dexp(x=0:500, rate = 105)

            plot(exp_data, type = 'o', col = "palegoldenrod",
                main = "Експоненціальний закон розподілу")
            warnings()"""
            st.code(code, language='r')
            st.image(Image.open("images/r14.png"))
            # 8
            st.write("""**8. Calculate the probability that a random variable distributed according to the exponential distribution 
                     law with parameter λ = 10 does not exceed the value 7.**""")
            code = """
            ?pexp
            pexp(7, rate = 0.1)
            plot(pexp(7, rate = 0.1), type = 'h', lwd = 3, col = 'plum2')
            """
            st.code(code, language='r')
            st.image(Image.open("images/r15.png"))
            # 9
            st.write("**9. Output a set of 200 random numbers distributed according to the standard normal distribution.**")
            code = """
            normal_data <- rnorm(200, mean = 0, sd = 1)
            normal_data"""
            st.code(code, language='r')
            # 10
            st.write("""**10. Calculate the probability that a random variable distributed according to the normal distribution with parameters α = 20 and σ = 87 takes values in the interval [14; 70]. Plot the cumulative distribution function and the probability density function of such distribution.**""")
            code = """
            prob <- pnorm(70, mean = 20, sd = 87) - pnorm(14, mean = 20, sd = 87)
            cat("Ймовірність того, що випадкова величина набуватиме значень з проміжку [14; 70]:", prob, "\n")

            a = seq(14, 70, by = 1)
            plot(a, dnorm(a, 20, 87), type = 's', col = 'peru',
                main = 'Нормальний закон розподілу')
            plot(a, dnorm(a, 20, 87),
                main = 'Нормальний закон розподілу')"""
            st.code(code, language='r')
            mu = 20
            sigma = 87
            a, b = 14, 70
            prob = norm.cdf(b, loc=mu, scale=sigma) - norm.cdf(a, loc=mu, scale=sigma)
            st.write(f"Ймовірність того, що випадкова величина набуватиме значень з проміжку [{a}; {b}]:", prob)
            st.image(Image.open("images/r16.png"))
            st.image(Image.open("images/r17.png"))

        elif selected == "Statistical Hypothesis Testing":
            st.title("Statistical Hypothesis Testing")
            st.subheader("Part 1")
            # 1
            st.write("**1. Plot the density graph of the random variable 'weight of the box' and visually assess its similarity to the normal distribution.**")
            code = """
            library(ggplot2)

            hist(butter, col='cornflowerblue', main='Графік щільності розподілу ваги',
                xlab='Вага коробки', ylab='Кількість коробок')"""
            st.code(code, language='r')
            st.image(Image.open("images/r18.png"))
            st.markdown("""
                        Based on the resulting density plot, it can be concluded that the distribution of box weights is close to normal. 
                        The graph visually resembles a normal distribution, although there are some deviations near the edges (especially on the right side, 
                        where there is some asymmetry).""")
            # 2
            st.write("**2. Test the hypothesis of normality of the box weight distribution using the Pearson's chi-squared test.**")
            code = """
            ?chisq.test
            chisq.test(butter, y = NULL, correct = TRUE,
                    p = rep(1/length(butter), length(butter)), rescale.p = FALSE,
                    simulate.p.value = FALSE)"""
            st.code(code, language='r')
            st.markdown("""
                        Normal distribution of box weight:
                        - X-squared = 16.646
                        - Degrees of freedom (df) = 179
                        - p-value = 1
                        
                        The obtained **p-value = 1** is significantly greater than the standard significance level (0.05). 
                        The test results indicate that **the distribution of box weights does not differ from the normal distribution**. 
                        Thus, the hypothesis of normality of the box weight distribution is supported by the Pearson's test.""")
            # 3
            st.write("**3. Test the hypothesis of normality using the Shapiro-Wilk test.**")
            code = """
            shapiro.test(butter)"""
            st.code(code, language='r')
            st.markdown("""
                        Results of the Shapiro-Wilk test for normality of the box weight:
                        - W = 0.9907
                        - p-value = 0.2943
                        
                        The obtained **p-value = 0.2943** is greater than the standard significance level (0.05). 
                        This means there is no reason to reject the null hypothesis that the data come from a normal distribution. 
                        Thus, according to the Shapiro-Wilk test, it can be stated that the **weight of the boxes with butter is normally distributed**.""")
            # 4 
            st.write("""**4. The weight of the box with butter should be 10 kg. Can it be considered that the deviation from the norm of 10 kg 
                     is insignificant? Use Student’s t-test for the equality of the mean of a normally distributed random variable to the specified value.**""")
            code = """
            t.test(butter, mu=10)"""
            st.code(code, language='r')
            st.markdown("""
                        Results of the test for equality of the mean box weight to 10 kg:
                        - t = 0.61577
                        - degrees of freedom (df) = 179
                        - p-value = 0.5388
                        - confidence interval: from 9.9022 to 10.1865
                        - mean value: 10.0444 kg
                        
                        The obtained **p-value = 0.5388** is greater than the standard significance level (0.05). 
                        This means there is **no reason to reject the null hypothesis**. Thus, according to the t-test results, the **deviation from the 
                        10 kg norm is insignificant**. The average box weight is approximately 10.0444 kg, and this deviation is not statistically significant.""")
            st.subheader("Part 2")
            # 1
            st.write("**1. Plot on the same coordinate system the daily revenues of both firms as scatter plots. Each firm's points should have its own color.**")
            code = """
            plot(revenue1, col='darkorchid3', pch=16, xlab='Дні',
                ylab='Виручка в день (тис. грн)', main='Денна виручка')
            points(revenue2, pch=16, col='goldenrod2')
            grid()"""
            st.code(code, language='r')
            st.image(Image.open("images/r19.png"))
            # 2
            st.write("**2. Can the volumes of daily revenues of both firms be considered comparable? Provide an answer based on the results of testing the hypothesis about the equality of the means of revenue volumes of the two firms using Student’s t-test.**")
            code = """
            t.test(revenue1, revenue2)"""
            st.code(code, language='r')
            st.markdown("""
                        Results of Welch’s t-test for testing the hypothesis about equality of the means of daily revenues of two firms:
                        - t value = 0.96119
                        - Degrees of freedom (df) = 197.51
                        - p-value = 0.3376
                        - Confidence interval: from -5.9171 to 17.1697
                        - Estimated mean revenues:
                            - Firm 1: 579.6824
                            - Firm 2: 574.0561
                        
                        Since the obtained p-value = 0.3376 is much greater than the standard significance level (0.05), there is **no reason to reject the null hypothesis** 
                        stating that the mean revenues of both firms are equal. Thus, based on the test results, it can be concluded that the **volumes of daily revenues of both 
                        firms can be considered comparable**. No statistically significant difference was found between the mean revenue volumes of the firms.""")
            # 3
            st.write("**3. Test the hypothesis about equality of variances of sales volumes of the two firms using Fisher's F-test.**")
            code = """
            var.test(revenue1, revenue2)"""
            st.code(code, language='r')
            st.markdown("""
                        Results of the F-test for testing the hypothesis about equality of variances of sales volumes of two firms:
                        - F value = 1.1044
                        - Degrees of freedom numerator: 99
                        - Degrees of freedom denominator: 99
                        - p-value = 0.6222
                        - Confidence interval: from 0.7431 to 1.6414
                        - Estimated ratio of variances: 1.1044
                        
                        Since the obtained **p-value = 0.6222** is much greater than the standard significance level (0.05), there is **no reason to reject the null hypothesis** stating 
                        that the variances of sales volumes of the two firms are equal. Thus, it can be concluded that the **variances of sales volumes of the two firms can be considered equal**, 
                        as no statistically significant difference between them was detected.""")
            # 4.1
            st.write("**4.1 Conduct a correlation analysis of sales volumes of the two firms. A scatter plot of sales volumes of firm 1 versus firm 2.**")
            code = """
            par(mfrow=c(1,1))
            plot(revenue1, revenue2, pch=16, col='darkseagreen3',
                main='Залежність доходу фірми 1 від фірми 2',
                xlab='Фірма 1', ylab='Фірма 2')"""
            st.code(code, language='r')
            st.image(Image.open("images/r20.png"))
            # 4.2
            st.write("**4.2 Conduct a correlation analysis of sales volumes of the two firms. A scatter plot of sales volumes of firm 2 versus firm 1.**")
            code = """
            plot(revenue2, revenue1, pch=16, col='deeppink4',
                main='Залежність доходу фірми 2 від фірми 1',
                xlab='Фірма 2', ylab='Фірма 1')"""
            st.code(code, language='r')
            st.image(Image.open("images/r21.png"))
            st.markdown("""If a strong correlation existed, we would expect to see some structure or trend (a line) in the distribution of points. 
                        In this case, the points are scattered throughout the plots without a clear trend, indicating the absence of a significant relationship between sales volumes.""")
            # 5
            st.write("**5. Use Pearson, Spearman, and Kendall criteria to test for the presence of correlation between sales volumes of the two firms.**")
            st.markdown("Results:")
            code = """
            cor(revenue1, revenue2, method='pearson')"""
            st.code(code, language='r')
            st.markdown("Pearson correlation coefficient: -0.0991")
            code = """
            cor(revenue1, revenue2, method='spearman')"""
            st.code(code, language='r')
            st.markdown("Spearman correlation coefficient: -0.0903")
            code = """
            cor(revenue1, revenue2, method='kendall')"""
            st.code(code, language='r')
            st.markdown("Kendall correlation coefficient: -0.0683")
            st.markdown("""
                        **Presence of correlation:**
                        
                        - All three correlation coefficients (Pearson, Spearman, and Kendall) are negative and close to zero. This indicates that there is no significant correlation between the sales volumes of the two firms.
                        - Values close to zero suggest that changes in the sales volume of one firm do not noticeably affect the sales volume of the other firm.
                        
                        **Type of correlation:**
                        
                        Pearson coefficient measures linear relationship, while Spearman and Kendall evaluate monotonic relationship. All three methods give similar results confirming the lack of correlation.
                        
                        **Significance of results:**
                        
                        Since all correlation coefficients are near zero, it can be stated that there is no statistically significant correlation between the sales volumes of the two firms.
                        
                        Thus, the results indicate that the sales volumes of the firms are not related, and changes in one firm’s sales do not necessarily cause changes in the other’s.""")

        elif selected == "Exploratory Analytics. Using Basic Graphics Package":
            st.title("Exploratory Analytics. Using Basic Graphics Package")
            # 1
            st.write("**1. Create a scatter plot in R using the built-in women dataset to visualize the relationship between height and weight of American women.**")
            code = """
            women
            plot(women$height, women$weight, 
                xlab = "Height", ylab = "Weight", 
                main = "American Women-weight vs Height", 
                col = "blue", 
                pch = 19)"""
            st.code(code, language='r')
            st.image(Image.open("images/r22.png"))
            # 2
            st.write("**2. Using R’s built-in dataset Nile, plot the annual river flow over the years, calculate the mean annual flow and add a horizontal line representing this average.**")
            code = """
            Nile
            plot(Nile, 
                main = "Nile River Annual Flow",  
                xlab = "Year",                    
                ylab = "Flow",                    
                col = "red",                     
                type = "l")                       

            abline(h=mean(Nile)) 

            text(1940, 1300, 
                labels = paste("Average Flow:", round(mean(Nile), 2)))"""
            st.code(code, language='r')
            st.image(Image.open("images/r23.png"))
            # 3
            st.write("**3. The dataset cars contains speed and braking distance. Plot the data on a scatter plot and analyze the results.**")
            code = """
            cars
            plot(cars$speed, cars$dist, 
                xlab = "Швидкість",          
                ylab = "Гальмівна відстань",
                main = "Залежність гальмівної відстані від швидкості",  
                pch = 19,                 
                col = "lightseagreen", 
                col.main = "darkred",  
                col.lab = "blue")   
            grid(col = 'black', lty = 1)"""
            st.code(code, language='r')
            st.image(Image.open("images/r24.png"))
            st.markdown("""
                        **Relationship between speed and braking distance:** The points on the graph are arranged approximately 
                        along a line that goes from the lower left to the upper right, indicating a positive correlation between 
                        the car’s speed and braking distance. This means that as the car’s speed increases, the braking distance 
                        also increases.
                        
                        **Linearity of the relationship:** Although the points do not form a perfectly straight line, the trend 
                        toward linearity is quite clear. At higher speeds, the car needs more time and distance to come to a full stop. 
                        Therefore, an increase in speed significantly affects braking distance.
                        """)
            # 4
            st.write("""**4. Use the rivers dataset. Create a graph showing the lengths of rivers against their index in the dataset. 
                     Add a label to the Y-axis: "Length in miles". Add a red-colored title in two lines: "Length of Major N. American Rivers". Display the points in green.**""")
            code = """
            rivers
            plot(rivers,
                ylab = "Length in miles",          
                col = "lightgreen",                  
                pch = 19)                             
            title(main = "Length of Major N. American Rivers", 
                col.main = "red", font.main = 2)"""
            st.code(code, language='r')
            st.image(Image.open("images/r25.png"))
            # 5
            st.write("""**5. Create a vector with the following numbers: 60 85 72 59 37 75 93 7 98 63 41 90 5 17 97. 
                     Build a histogram and a bar chart for this vector, placing them in one row. What is the difference?**""")
            code = """
            numbers <- c(60, 85, 72, 59, 37, 75, 93, 7, 98, 63, 41, 90, 5, 17, 97)

            par(mfrow = c(1, 2))

            hist(numbers, 
                col = rainbow(length(numbers)), 
                main = "Гістограма",
                col.main = "lightgreen",
                font.main = 3)

            barplot(numbers, 
                    col = rainbow(length(numbers)),  
                    main = "Стовпчикова діаграма",
                    col.main = 'blue', 
                    font.main = 3)"""
            st.code(code, language='r')
            st.image(Image.open("images/r26.png"))
            st.markdown("""
                        - **Histogram:**
                            - Used to display the distribution of numerical data.
                            - Divides the data into intervals (bins), showing the count of values that fall into each bin.
                            - Displays frequency as adjacent bars.
                        
                        - **Bar chart:**
                            - Used for categorical data.
                            - Each bar represents a separate category (in this case, the individual values of the vector).
                            - The height of each bar shows the frequency or magnitude of the corresponding category.
                        """)
            # 6
            st.write("""**6. Using the command rnorm(100), generate 100 random numbers from a normal distribution. 
                     Create two histograms with two different sets of 100 numbers generated from a normal distribution using 
                     the same command. Will the histograms be identical?**""")
            code = """
            par(mfrow = c(1, 2))
            set1 <- rnorm(100, mean = 10, sd = 5)
            hist(set1, breaks = 20, col = "lightgreen", main = "Гістограма 1")

            set2 <- rnorm(100, mean = 10, sd = 5)
            hist(set2, breaks = 20, col = "lightblue", main = "Гістограма 2")"""
            st.code(code, language='r')
            st.image(Image.open("images/r27.png"))
            st.markdown("""
                        The histograms will not be exactly the same, as each set of random numbers is generated independently 
                        and will differ due to randomness. However, they may look similar because both sets are generated from 
                        the same normal distribution.
                        """)
            # 7
            st.write("**7. Load the data from the file firtree.csv. Build a bar chart showing the distribution of the number of coniferous trees in both numeric and percentage formats, using different shades of green.**")
            code = """
            data <- read.csv("firtree.csv")
            str(data)
            data <- na.omit(data)
            par(mfrow = c(1, 2))

            barplot(table(data$ftype), main = "Хвойні дерева", 
                        col = c('darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3'))

            perc <- table(data$ftype)/sum(table(data$ftype)) * 100
            perc
            barplot(perc, main = 'Хвойні дерева',
                    col = c('palegreen1', 'palegreen2', 'palegreen3', 'palegreen4'))"""
            st.code(code, language='r')
            st.image(Image.open("images/r28.png"))
            # 8
            st.write("**8. Build a histogram for tree height. Add a title to the histogram, change its color, and label the axes.**")
            code = """
            par(mfrow = c(1, 1))
            hist(data$height, 
                main = "Histogram of height",  
                xlab = "Height (in cm)",      
                ylab = "Counts",                   
                col = "lightgreen")"""
            st.code(code, language='r')
            st.image(Image.open("images/r29.png"))
            # 9
            st.write("**9. Build a pie chart showing the distribution of coniferous tree types. Change the colors of the chart to your own.**")
            code = """
            pie(table(data$ftype), 
                main = "Хвойні дерева",   
                col = c("lightcoral", "lightskyblue", "peachpuff", "plum")) """
            st.code(code, language='r')
            st.image(Image.open("images/r30.png"))
            # 10
            st.write("**10. Add percentage values of tree distribution to the pie chart. Add a legend to the pie chart.**")
            code = """
            tree_counts <- table(data$ftype)
            tree_percentages <- round(100 * tree_counts / sum(tree_counts), 1)
            labels <- paste(tree_percentages, "%")

            pie(table(data$ftype), 
                labels = labels, 
                main = "Хвойні дерева",   
                col = c("lightcoral", "lightskyblue", "peachpuff", "plum"))

            legend("topright", legend = names(tree_counts), fill = c("lightcoral", "lightskyblue", "peachpuff", "plum"))"""
            st.code(code, language='r')
            st.image(Image.open("images/r31.png"))

        elif selected == "Advanced Visual Analytics Tools":
            st.title("Advanced Visual Analytics Tools")
            # 1
            st.write("""**1. Install the vcd package. Load the Arthritis table, which is part of the installed package. 
                     The table contains data from a clinical trial that investigated a new treatment for rheumatoid arthritis. 
                     Create simple vertical and horizontal bar charts.**""")
            code = """
            install.packages("vcd")
            library(vcd)
            Arthritis

            freq <- table(Arthritis$Improved)  
            freq
            par(mfrow = c(1,2))
            barplot(freq, 
                    main = "Вертикальна стовпчикова діаграма", 
                    xlab = "Покращення", 
                    ylab = "Частота", 
                    col = "red")
            barplot(freq, 
                    main = "Горизонтальна стовпчикова діаграма", 
                    xlab = "Частота", 
                    ylab = "Покращення", 
                    horiz = TRUE, 
                    col = "green")"""
            st.code(code, language='r')
            st.image(Image.open("images/r32.png"))
            # 2
            st.write("**2. Create bar charts with vertical and horizontal subgroup distributions.**")
            code = """
            freq_subgroups <- table(Arthritis$Improved, Arthritis$Treatment)
            freq_subgroups
            par(mfrow = c(1,2))
            barplot(freq_subgroups, 
                    main = "Стовпчикова діаграма з верт розбиттям", 
                    xlab = "Лікування", 
                    ylab = "Частота", 
                    col = c("red", "yellow", "green"), 
                    legend = rownames(freq_subgroups))
            barplot(freq_subgroups, 
                    main = "Стовпчикова діаграма з гориз розбиттям", 
                    xlab = "Лікування", 
                    ylab = "Частота", 
                    beside = TRUE, 
                    col = c("red", "yellow", "green"), 
                    legend = rownames(freq_subgroups))"""
            st.code(code, language='r')
            st.image(Image.open("images/r33.png"))
            # 3
            st.write("**3. Create spine plots – a special type of bar chart.**")
            code = """
            library(vcd)
            attach(Arthritis)
            freq <- table(Treatment, Improved)
            spine(freq, 
                main = "Приклад спінограми")
            detach(Arthritis)"""
            st.code(code, language='r')
            st.image(Image.open("images/r34.png"))
            st.markdown("*(I tried several options, but unfortunately, I couldn’t manage to color them.)*")
            # 4
            st.write("""**4. Using R base visualization commands, reproduce the given chart.**""")
            code = """
            head(InsectSprays)
            str(InsectSprays)
            par(mfrow = c(1, 2))
            boxplot(InsectSprays$count, 
                    main = "Effectiveness of Spray", 
                    ylab = "Count", 
                    xlab = "All Sprays", 
                    col = "coral")
            boxplot(InsectSprays$count~InsectSprays$spray,
                    main = "Effectiveness by Spray",
                    ylab = "Count",
                    xlab = "Type of sprays", 
                    col = "lightblue")"""
            st.code(code, language='r')
            st.image(Image.open("images/r35.png"))
            # 5
            st.write("""**5. For the mtcars dataset, create enhanced boxplots.**""")
            code = """
            mtcars
            par(mfrow = c(1, 1))
            boxplot(mpg ~ cyl, 
                    data = mtcars, 
                    notch = TRUE, 
                    varwidth = TRUE, 
                    col = c("lightblue", "lightgreen", "salmon"),
                    main = "Інформація про авто", 
                    ylab = "Витрати пального", 
                    xlab = "Число циліндрів")"""
            st.code(code, language='r')
            st.image(Image.open("images/r36.png"))
            # 6
            st.write("""**6. For example, let’s set the task of examining fuel consumption not only by the number of cylinders but also by the type of car transmission (manual or automatic).**""")
            code = """
            mtcars$cyl.f <- factor(mtcars$cyl, 
                                levels = c(4, 6, 8),
                                labels = c("4ц", "6ц", "8ц"))
            mtcars$am.f <- factor(mtcars$am,
                                levels = c(0, 1),
                                labels = c("АТ", "МТ"))

            boxplot(mpg ~ am.f * cyl.f, 
                    data = mtcars, 
                    varwidth = TRUE, 
                    col = c("darkolivegreen1", "lightskyblue"), 
                    main = "Витрати пального в залежності від циліндрів і типу трансмісії", 
                    ylab = "Витрати пального (mpg)", 
                    xlab = "Кількість циліндрів та тип трансмісії")

            legend("topright", 
                legend = c("АТ", "МТ"), 
                fill = c("darkolivegreen1", "lightskyblue"), 
                title = "Тип трансмісії")"""
            st.code(code, language='r')
            st.image(Image.open("images/r37.png"))
            # 7
            st.write("**7. For the mtcars dataset, create another modification of the fuel consumption plots for cars with four, six, and eight cylinders – violin plots.**")
            code = """
            install.packages("vioplot")
            library(vioplot)
            x1 <- mtcars$mpg[mtcars$cyl == 4]
            x2 <- mtcars$mpg[mtcars$cyl == 6]
            x3 <- mtcars$mpg[mtcars$cyl == 8]
            par(mfrow = c(1, 1))
            vioplot(x1, x2, x3, 
                    names = c("4 циліндри", "6 циліндрів", "8 циліндрів"), 
                    col = "mediumorchid1")
            title("Скрипкові діаграми витрат пального")"""
            st.code(code, language='r')
            st.image(Image.open("images/r38.png"))

# GOOGLE SHEETS
# if selected == 'Google Sheets':
    st.markdown("<h1 style='text-align: center;'>Google Sheets</h1>", unsafe_allow_html=True)

# RECOMMENDER SYSTEM
if selected == 'Recommender System':
    # DATASETS
    l_data = pd.read_csv('grs/data extraction and preprocessing/data3.csv')
    l_data.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)

    similarity = pickle.load(open('grs/data/similarity.pkl','rb'))


    # MAINPAGE
    st.markdown("<h1 style='text-align: center;'>🎮 Game Recommender system</h1>", unsafe_allow_html=True)

    st.write("Imagine you're wandering through a vast library of games, and suddenly, a quirky little friend pops up, saying, ")

    st.markdown("""<div style="text-align: center;">
                    <p><em><strong>"Hey there! Feeling lost in this jungle of pixels? Let me be your guide!"</strong></em></p>
                </div>
            """, unsafe_allow_html=True)

    st.write("That's what a game recommender system is like—it's your trusty sidekick in the world of gaming, "
         "helping you find the perfect game without getting lost in the maze of choices."
         " Think of it as your own personal game genie 🧞‍♂️, but instead of granting wishes, it grants you "
         "hours of entertainment and fun! It's like having a friend who knows you better than you know "
         "yourself when it comes to gaming...")

    st.write("\nSo, next time you're scratching your head, wondering what "
         "game to play next, just come here and follow the set of instructions on the sidebar!")



    # RECOMMENDATION

    st.write("<h4>Choose games here</h4>", unsafe_allow_html=True)
        
    games = st.multiselect('', l_data['name'], [], key='games')
        
    recommed = st.button('Recommend')
    col1,col2 = st.columns(2)

    if recommed:
        top_recommendations = []

        for game in games:
            index = l_data[l_data['name'] == game].index[0]
            top_six = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:7]
            top_recommendations.extend([top_six[i][0] for i in range(len(top_six))]) 

        top_recommendations = list(set(top_recommendations))[:6]
            
        for i, k in enumerate(top_recommendations):
            if i % 2 == 0:
                with col1:
                    st.markdown("""
                            <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
                            <a href="{link}" target="_blank"><img src="{image}" style="width:500px;height:250px; margin-bottom: 10px;"></a>
                            <div style="text-align: center;">
                                <p style="margin: 0; font-size: 20px;"><b>Title: </b>{name}</p>
                                <p style="margin: 0; font-size: 20px;"><b>Developer: </b>{developer}</p>
                            </div>
                            </div>
                            """.format(link=l_data["Steam Page"][k], image=l_data["header_image"][k], name=l_data["name"][k], developer=l_data['developer'][k]), unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown("""
                            <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
                            <a href="{link}" target="_blank"><img src="{image}" style="width:500px;height:250px; margin-bottom: 10px;"></a>
                            <div style="text-align: center;">
                                <p style="margin: 0; font-size: 20px;"><b>Title: </b>{name}</p>
                                <p style="margin: 0; font-size: 20px;"><b>Developer: </b>{developer}</p>
                            </div>
                            </div>
                            """.format(link=l_data["Steam Page"][k], image=l_data["header_image"][k], name=l_data["name"][k], developer=l_data['developer'][k]), unsafe_allow_html=True)
 

    # SIDEBAR
    # sidebar.instructions
    st.sidebar.header("Set of instructions 🙂")

    st.sidebar.markdown("1. Choose a game from the dropdown menu.")
    st.sidebar.markdown("2. Click the 'Recommend' button.")
    st.sidebar.markdown("3. Explore the recommended games.")
    st.sidebar.markdown("4. Click on image to visit Steam page. ")
    st.sidebar.markdown("5. Enjoy!")

    st.sidebar.markdown('---')

    # sidebar.tags
    for game in games:
        selected_game_categories = l_data.loc[l_data['name'] == game, 'Tags'].iloc[0]
    
        if selected_game_categories:
            st.sidebar.subheader(f"The chosen game '{game}' belongs to:")
            categories_list = selected_game_categories.split(',')
            for category in categories_list:
                st.sidebar.write(f"- {category.strip()}")

    
    # TRENDING

    st.markdown('---')
  
    trending = st.subheader('Trending games')

    st.write("**Need a break from reality?** 🙃")

    st.write("\nGames offer the perfect escape! They whisk us away to fantastical realms, where we can "
                 "embark on thrilling adventures, solve mind-bending puzzles, or simply unwind after a long day."
                 " Whether you're battling dragons in a mythical land or building your dream city from scratch, "
                 "games provide a welcome reprieve from the stresses of everyday life. ")
        
    st.write("\nDive into the world of gaming and discover why millions around the globe turn to Steam for their dose of fun and relaxation. "
                 "Check out the trending games on Steam now and treat yourself to some well-deserved entertainment! **Click on the image...**")
                 

    col3, col4 = st.columns(2)
    for i in range(4):
            if i % 2 == 0:
                with col3:
                    st.markdown("""
                        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
                        <a href="{link}" target="_blank"><img src="{image}" style="width:500px;height:250px; margin-bottom: 10px;"></a>
                        <div style="text-align: center;">
                            <p style="margin: 0; font-size: 20px;"><b>Title: </b>{name}</p>
                            <p style="margin: 0; font-size: 20px;"><b>Developer: </b>{developer}</p>
                        </div>
                        </div>
                        """.format(link=l_data["Steam Page"][i], image=l_data["header_image"][i], name=l_data['name'][i], developer=l_data['developer'][i]), unsafe_allow_html=True)
            else:
                with col4:
                    st.markdown("""
                        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
                        <a href="{link}" target="_blank"><img src="{image}" style="width:500px;height:250px; margin-bottom: 10px;"></a>
                        <div style="text-align: center;">
                            <p style="margin: 0; font-size: 20px;"><b>Title: </b>{name}</p>
                            <p style="margin: 0; font-size: 20px;"><b>Developer: </b>{developer}</p>
                        </div>
                        </div>
                        """.format(link=l_data["Steam Page"][i], image=l_data["header_image"][i], name=l_data['name'][i], developer=l_data['developer'][i]), unsafe_allow_html=True)

# DIAGRAMS                
if selected == 'Diagrams':
    st.markdown("<h1 style='text-align: center;'>Diagrams</h1>", unsafe_allow_html=True)
    st.markdown("""
                This section showcases a collection of diagrams (BPMN, Flowcharts, Use Case, Activity Diagram, IDEF0, IDEF3, DFD) 
                that I created during a university course. While they were technically part of an academic assignment, the focus 
                was on practical, real-world business scenarios—because companies don’t really care how pretty your arrows are if 
                the process still gets stuck halfway. We modeled common business situations, identified where things could (and often do) 
                go wrong, and worked on making processes more efficient.
                
                These diagrams highlight not only my ability to use different visualization and modeling techniques but also my 
                problem-solving mindset. In short, I didn’t just draw boxes and lines—I tried to make sense of chaos and turn it into 
                something that actually works. (And yes, sometimes it felt like detective work for business processes!)
                """)
    selected_optipns = ["1. IDEF0 Notation. Context Diagram",
                        "2. IDEF0 Notation. Decomposition",
                        "3. IDEF0 + IDEF3",
                        "4. Data Flow Diagram (DFD)",
                        "5. IDEF0 + IDEF3 + DFD",
                        "6. Flowchart. Customer Satisfaction Analysis",
                        "7. Use Case Diagrams",
                        "8. Activity Diagram",
                        "9. BPMN Models",
                        "10. BPMN. Data collection and processing for decision-making",
                        "11. BPMN Collaboration Diagram",
                        "12. BPMN Process Diagram",
                        "13. BPMN Process Model. Needs Analysis"]
    selected = st.selectbox("Select a project", options = selected_optipns)
    st.write("Current selection:", selected)
    if selected == "1. IDEF0 Notation. Context Diagram":
        st.markdown("""
                    ## *IDEF0 Notation. Context Diagram*
                    - **Define the business process you will model (either the one selected earlier or a new one).**
                    - **Identify and specify the following for the entire process and its subprocesses:**
                        1. Inputs (resources that enter the process),
                        2. Outputs (results produced by the process),
                        3. Mechanisms (tools, people, or systems performing the process),
                        4. Controls (rules, standards, or management influencing the process).
                    - **Create a context diagram in IDEF0 notation and add arrows to represent the attributes listed above.**""")
        st.image(Image.open("images/d9.jpeg"), use_column_width=True)
    
    elif selected == "2. IDEF0 Notation. Decomposition":
        st.markdown("""
                    ## *IDEF0 Notation. Decomposition*
                    - **Create decomposition diagrams**
                        1. Develop two IDEF0 decomposition diagrams based on your context diagram and the defined subprocesses and operations.
                        2. If you identify errors in the context diagram, correct them in the working file before proceeding.
                    - **Describe each subprocess. For every subprocess, provide the following details**:
                        1. Name of the subprocess,
                        2. Unit of measurement (e.g., duration),
                        3. Short description,
                        4. Possible costs in the Cost Center (if applicable).
                    - **Add connections**
                        1. Attach external arrows to the functional blocks at the first level of decomposition.
                        2. Add arrows to indicate relationships between subprocesses.
                    - **Perform deeper decomposition**
                        1. Select one or two subprocesses and create their second-level decomposition diagrams.""")
        st.image(Image.open("images/d10.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the first level*")
        st.image(Image.open("images/d11.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the second level*")
        st.image(Image.open("images/d12.jpeg"), use_column_width=True)
        
    elif selected == "3. IDEF0 + IDEF3":
        st.markdown("""
                    ## *IDEF0 + IDEF3. General Report*
                    - **Create a model for one of the following business processes (BPs) using IDEF0 notation (context diagram) and IDEF3 notation (Level 1 decomposition, Level 2 decomposition):**
                        1. Design of an information system for resource management or management subsystems
                        2. Analysis of market segments
                        3. Analysis of company business indicators
                        4. Monitoring of labor productivity
                        5. Monitoring of team/project performance
                    - **In the IDEF0 diagram, specify the name of the BP and its external arrows.**
                    - **In the decomposition diagrams, specify for each Unit of Work (UOW):**
                        1. name,
                        2. duration (cost, where applicable),
                        3. short description,
                        4. junctions,
                        5. arrows,
                        6. objects (if needed).
                    - **Demonstrate different types of relationships and junctions. Pay attention to synchronization and types of operators (AND, OR) in junctions, as well as their compatibility in conjunctions and disjunctions.**
                    - **Ensure that arrows are connected to blocks/UOWs and that they contain the required level of detail.**""")
        st.image(Image.open("images/d13.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the first level*")
        st.image(Image.open("images/d14.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the second level*")
        st.image(Image.open("images/d15.jpeg"), use_column_width=True)

    elif selected == "4. Data Flow Diagram (DFD)":
        st.markdown("""
                    ## *Data Flow Diagram (DFD)*
                    - **Create a Data Flow Diagram (DFD) for the product purchase process on the Rozetka website — from selecting a product to completing the order.**
                    - **Use the following short description of the process, taking into account the requirements for naming activities and the number of tasks on one level. Divide subprocesses into two decomposition levels:**
                        1. The user visits the Rozetka website.
                        2. Selects the desired product from the catalog (search or filtering may be used).
                        3. Adds the product to the shopping cart.
                        4. Proceeds to checkout: enters personal data, selects delivery and payment methods.
                        5. The system processes the order and sends confirmation.
                    - **Consider the following elements in your DFD:**
                        1. **External entities:** User / Buyer, Payment System, Delivery Service
                        2. **Processes / Activities**
                        3. **Data stores:** Product Catalog, Shopping Cart, Customer Data
                        4. **Data flows**
                    - **Create the model structure as follows:**
                        1. DFD Level 0 (Context Diagram): general view of the purchase process, showing the overall process and external entities.
                        2. DFD Level 1 and Level 2 Decomposition Diagrams: break the process down into individual subprocesses.""")
        st.image(Image.open("images/d16.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the first level*")
        st.image(Image.open("images/d17.jpeg"), use_column_width=True)
        st.markdown("## *Decomposition of the second level*")
        st.image(Image.open("images/d18.jpeg"), use_column_width=True)
        
    elif selected == "5. IDEF0 + IDEF3 + DFD":   
        st.markdown("""
                    ## *IDEF0 + IDEF3 + DFD*
                    - **General Task:**
                    Create a model of one of the suggested business processes below, or use an example of your own business process from previous tasks, and build a single model that incorporates all three notations: IDEF0, IDEF3, and DFD.
                    - **Workflow Algorithm:**
                        1. Describe the selected business process in the context of the organization, considering model attributes (approx. 0.5 page). Also, state the purpose of modeling.
                        2. Build the AS-IS model (the model should include at least two levels of process decomposition).
                        3. Describe the model and attach figures from the report (1–n pages).
                        4. Identify bottlenecks / problematic areas in this process (0.5–1 page).
                        5. In a copy of your model, restructure the operations/subprocesses to show improvements. This will be the TO-BE model.
                        6. Describe the TO-BE model and attach figures from the report (0.5–n pages).""")
        st.markdown("""
                    ## *Task 1*
                    The business process considered in this report covers the full cycle of **elevator equipment manufacturing** — from the development of technical documentation to the delivery of the finished product to the client. This process is a key activity at the machine-building enterprise, as it ensures order fulfillment, revenue generation, and customer satisfaction.
                    
                    **Purpose of modeling:**
                    To identify shortcomings (bottlenecks) in the existing process, formalize its structure using **IDEF0, IDEF3, and DFD** models, and propose optimization through the development of a **TO-BE model**.
                    
                    **Main objectives of the model:**
                    - Standardize approaches to design and production
                    - Minimize time and resource costs
                    - Improve product quality
                    - Automate routine processes
                    
                    **Model attributes:**
                    - Name: Elevator Equipment Manufacturing
                    - Author: Shcherbyna J.O.
                    - Context diagram: A-0
                    - Creation date: 28.04.2025
                    - Project: lab 13–14""")
        st.markdown("""
                    ## *Task 2*
                    **2.1. Level 1 — IDEF0 Context Diagram**
                    At the first level, the overall process **“Manufacturing of Elevator Equipment”** is shown. The entire business process takes **32 days**. Inputs, outputs, controls, and mechanisms are represented as follows:
                    - **Inputs:** Technical requirements and specifications; Raw materials and supplies.
                    - **Controls:** Product quality control regulations; Production process management regulations.
                    - **Mechanisms:** Human resources; Materials and equipment; Financial resources for equipment procurement.
                    - **Outputs:** Finished elevator equipment.""")
        st.image(Image.open("images/d19.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.2. Decomposition of the Process "Manufacturing of Elevator Equipment" (IDEF0)**
                    This level reveals the internal structure of the key production process, including the following subprocesses:
                    - Development of technical documentation
                    - Production of parts
                    - Quality control
                    - Delivery to the client""")
        st.image(Image.open("images/d20.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.3. Decomposition of the Process "Production of Parts" (IDEF3)**
                    
                    This sub-level details the manufacturing part of the process. It shows how raw materials and drawings are transformed into finished parts. The model describes which operations make up the production of elevator equipment components.
                    
                    **Main processes:**

                    | № | Subprocess name                | Function description                                                    |
                    | - | ------------------------------ | ----------------------------------------------------------------------- |
                    | 1 | Preparation of blanks          | Receiving drawings and technical requirements, selecting materials      |
                    | 2 | Processing of blanks           | Mechanical and/or thermal processing according to specifications        |
                    | 3 | Dimensional control            | Verification of compliance of processed blanks with required dimensions |
                    | 4 | Surface quality control        | Visual or technical assessment of blank surfaces                        |
                    | 5 | Analysis of inspection results | Determination of suitability / unsuitability of parts                   |
                    | 6 | Welding                        | Joining of units after quality confirmation                             |
                    | 7 | Rework and welding             | Reprocessing or welding of unsuitable parts                             |
                    | 8 | Assembly                       | Assembly of suitable and welded units into finished parts               |

                    **Process logic:**

                    * **J1 — AND:** processed blanks must undergo both dimensional control and surface quality control.
                    * **J2 — AND:** results of both inspections are passed to analysis.
                    * **J3 — OR:** if the part is suitable, it goes directly to welding or to rework and welding.
                    * **J4 — OR:** units after welding or rework and welding can be immediately transferred to assembly.""")
        st.image(Image.open("images/d21.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.3. Decomposition of the Process “Delivery to the Client” (DFD)**

                    At this stage, a detailed description of the information flows that occur during the organization of the delivery of finished elevator equipment is presented. The DFD model demonstrates which data are transmitted between subsystems, databases, the client, and internal departments.

                    **Main processes:**

                    | № | Process name                  | Action description                                                                   |
                    | - | ----------------------------- | ------------------------------------------------------------------------------------ |
                    | 1 | Receiving inspected equipment | Arrival of equipment from production after quality control                           |
                    | 2 | Creating a delivery order     | Summarizing client data, address, type of delivery, creating a request               |
                    | 3 | Organizing transportation     | Communication with the logistics department, preparation of waybills, transportation |
                    | 4 | Shipping to the client        | Transfer of equipment to the client, confirmation of completion                      |

                    
                    **Databases:**

                    | Name                            | Purpose                                 |
                    | ------------------------------- | --------------------------------------- |
                    | Customer Database               | Data on regular customers               |
                    | Delivery Registry               | Log of created delivery requests        |
                    | Supporting Documents / Waybills | Generation of legally binding documents |

                    **External participants:**

                    | Name                 | Role                         |
                    | -------------------- | ---------------------------- |
                    | Client               | Equipment orderer, recipient |
                    | Logistics Department | Organizes transportation     |""")
        st.image(Image.open("images/d22.jpeg"), use_column_width=True)
        st.markdown("""
                    ## *Task 3*
                    **Description of Problematic “Bottlenecks” in the Process**
                    1. **Manual documentation development**
                    The lack of automation in creating technical documentation leads to delays and increases the risk of errors.
                    2. **Inefficient quality control**
                    An excessive number of manual inspections slows down the process and does not guarantee consistent quality.
                    3. **Lack of production automation**
                    Processing parts on conventional machines without integrated monitoring reduces productivity.
                    4. **Complex logistics**
                    Order creation and delivery are performed manually, creating a risk of information loss or duplication.""")
        st.markdown("""
                    ## *Task 4*
                    **Description of the TO-BE Model**
                    
                    Based on the analysis of the current model and identification of bottlenecks, a **TO-BE model** was developed that incorporates modern digital technologies to improve the efficiency of manufacturing and delivery of elevator equipment to clients.
                    
                    **Key improvements in the TO-BE model:**
                    1. **Automated generation of technical documentation**
                        * Drawings, specifications, and requirements are created using **AutoCAD** integrated with the **ERP system**.
                        * All documents are stored centrally and synchronized with production modules.
                    2. **Part manufacturing using CNC machines**
                        * Blank processing is performed on modern **CNC equipment**.
                        * Quality control is integrated into the process via built-in sensors and automated controllers.
                    3. **Integrated quality control in MES**
                        * All inspection results are transmitted to the **MES system**.
                        * MES generates inspection reports and analytics without operator intervention.
                    4. **Automation of logistics and delivery**
                        * After equipment inspection, a delivery order is automatically created via the **CRM system**.
                        * Logistics are fully coordinated by the ERP module; documents are generated automatically, and the client receives notifications.
                    5. **Optimized client interaction**
                        * The **CRM system** stores order history, automatically populates client data, and tracks delivery status.
                        * Delivery tracking and confirmation are implemented via **API** or **email notifications**.
                    **Illustrations in the report**:
                        * Context diagram (IDEF0) showing inputs, outputs, controls, and resources with automated modules.
                        * Subprocess decomposition (IDEF3) highlighting CNC and MES integration in production.
                        * DFD diagram showing automated data flows between ERP, MES, CRM, logistics, and client.""")
        st.markdown("""
                    **2.1. Level 1 — IDEF0 Context Diagram**
                    
                    ERP system and MES have been added as management methods, while AutoCAD, CNC machines, and automated controllers have been added as implementation mechanisms.""")
        st.image(Image.open("images/d23.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.2. Decomposition of the Process “Elevator Equipment Manufacturing” (IDEF0)**
                    
                    Instead of manual documentation development, a block **“Automated Generation”** is implemented. Manufacturing and quality control are carried out via **CNC machines, AutoCAD, and the ERP system**. Quality control has been enhanced to **“Integrated Quality Control in MES”** using automated controllers.""")
        st.image(Image.open("images/d24.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.3. Decomposition of the Process “Parts Manufacturing” (IDEF3)**
                    
                    Processing and inspection have been combined into a single block — **“CNC Processing of Blanks with Embedded Quality Control.**”""")
        st.image(Image.open("images/d25.jpeg"), use_column_width=True)
        st.markdown("""
                    **2.4. Decomposition of the Process “Delivery to Client” (DFD)**
                    
                    Logistics request creation and transportation management are carried out through **CRM and ERP systems**. A block **“Automatic Order Generation”** has been added.""")
        st.image(Image.open("images/d26.jpeg"), use_column_width=True)

    elif selected == "6. Flowchart. Customer Satisfaction Analysis":
        st.markdown("""
                    ## *Flowchart “Customer Satisfaction Analysis”*
                    - **Create a flowchart for the business process (BP) “Customer Satisfaction Analysis”. The company conducts a customer satisfaction analysis in order to:**
                        1. Understand customer demand
                        2. Perform a root cause analysis of purchases or user stories
                        3. Learn how customers rate their experience
                        4. Identify the most interesting areas for customers
                        5. Determine the level of customer satisfaction
                        6. Define areas for improvement""")
        col1, col2, col3 = st.columns([1, 2, 1])  
        with col2:
            st.image(Image.open("images/15-16. Аналіз задоволеності.jpg"), use_column_width=True)
    
    elif selected == "7. Use Case Diagrams":
        st.markdown("""
                    ## *Use Case Diagrams*
                    - **Build two Use Case Diagrams for the online purchase process on the Rozetka website, showing user actions during:**
                        1. product selection
                        2. payment completion
                    - **Represent include or extend relationships between main and additional use cases. Types of users (Actors):**
                        1. Registered User
                        2. Website Administrator
                        3. Payment System (as an external actor)""")
        st.markdown("## *Use case diagram. Product selection*")
        col1, col2, col3 = st.columns([1, 2, 1])  
        with col2:
            st.image(Image.open("images/17. Use case diagram Вибір товару.jpg"), use_column_width=True)
        st.markdown("## *Use case diagram. Payment completion*")
        col1, col2, col3 = st.columns([1, 2, 1])  
        with col2:
            st.image(Image.open("images/17. Use case diagram Здійснення оплати.jpg"), use_column_width=True)

    elif selected == "8. Activity Diagram":
        st.markdown("""
                    ## *Activity Diagram*
                    - **Create an activity diagram for the process “Data Analysis”.**
                    - **Apply all diagram elements:**
                        1. Initial nodes
                        2. Control flows
                        3. Actions
                        4. Decisions
                        5. Forks and joins (branching and merging)
                        6. Final nodes""")
        st.markdown("## *Activity Diagram. Data Analysis*")
        col1, col2, col3 = st.columns([1, 2, 1])  
        with col2:
            st.image(Image.open("images/18. Activity diagram Аналіз даних.jpg"), use_column_width=True)

    elif selected == "9. BPMN Models":
        st.markdown("""
                    ## *BPMN Models*
                    - **Main task: Build two process models according to the scenarios below.**
                    - **Scenario 1: Business Trip Request**
                        1. Submit a business trip request.
                        2. Send a notification about the new request and ask for approval from managers.
                        3. Agree on cost and duration.
                        4. Reserve tickets and proceed with payment if the manager approves.
                        5. Cancel the business trip if the manager rejects the request.
                        6. Prepare a report on the trip results after returning.
                    - **Scenario 2: Event Organization**
                        1. Collect information regarding participants and the organizing committee (e.g., booth, presentation, logo, etc.).
                        2. Create a list of participants attending the event.
                        3. Consolidate data — coordinate press releases, logos, and other information for the organizers.
                        4. Select a speaker, approve the presentation topic, and prepare the presentation.
                        5. Conduct the event.
                        6. Summarize the event results.""")
        st.markdown("## *Scenario 1. Business Trip Request*")
        st.image(Image.open("images/d2.jpg"), use_column_width=True)
        st.markdown("## *Scenario 2. Event organization*")
        st.image(Image.open("images/d1.jpg"), use_column_width=True)

    elif selected == "10. BPMN. Data collection and processing for decision-making":
        st.markdown("""
                    ## *BPMN. Data collection and processing for decision-making*
                    **Build a BPMN model**
                    - **Business Process Option:** Data collection and processing for decision-making
                    - **Context of the Business Process in the Digital Economy:** Analysis of online transaction data, user behavior, and market trends.
                    - **In Business Analytics:** Using tools to collect, clean, and analyze large volumes of data.""")
        st.image(Image.open("images/d3.jpg"), use_column_width=True)

    elif selected == "11. BPMN Collaboration Diagram":
        st.markdown("""
                    ## *BPMN Collaboration Diagram*
                    Build a BPMN Collaboration Diagram that shows the interaction between a company and a software developer.
                    
                    **Context:**
                    The company collaborates with a software developer to implement a CRM system.

                    **Execution Steps:**
                    1. Open software for building a BPMN business process model.
                    2. Create two pools for participants:
                        - Company – the system client, provides requirements and checks the results.
                        - Software Developer – implements the CRM system and adapts it to the company’s needs.
                    3. Display the main message flows:
                        - The company sends requirements to the developer.
                        - The developer implements the CRM system and notifies the company that it is ready for testing.
                        - The company sends feedback to the developer regarding the system’s performance.""")
        st.image(Image.open("images/d4.jpg"), use_column_width=True)
        st.markdown("## *Sub-process (collapsed)*")
        st.image(Image.open("images/d5.jpg"), use_column_width=True)
    
    elif selected == "12. BPMN Process Diagram":
        st.markdown("""
                    ## *BPMN Process Diagram*
                    Build a BPMN Process Diagram for the process “Implementation of a New Analytical Model in the Company.”
                    
                    **Context:**
                    The company implements an analytical model to forecast sales and optimize inventory levels.
                    
                    **Execution Steps:**
                    1. Open software for building a BPMN business process model.
                    2. Create a process model using notation elements according to the context and process description.
                    3. Process Description:
                        - The Analytics Department develops the model based on historical data.
                        - The system tests the model on real data from the last month.
                        - Test results are analyzed: if the model works correctly, the process continues; if not, the model is adjusted.
                        - The model is integrated into the production system.
                        - The system automatically updates sales forecasts and inventory levels.
                        - The Sales Department (closed pool) receives reports for decision-making.
                    4. Include in the model:
                        - ateway to evaluate the success of testing;
                        - iteration for the iterative task;
                        - intermediate event with a trigger;
                        - sub-process, either expanded or collapsed.""")
        st.image(Image.open("images/d6.jpg"), use_column_width=True)
        st.markdown("## *Sub-process (collapsed)*")
        st.image(Image.open("images/d7.jpg"), use_column_width=True)

    elif selected == "13. BPMN Process Model. Needs Analysis":
        st.markdown("""
                    ## *BPMN Process Model. Needs Analysis*
                    Create a BPMN process model for “Needs Analysis”.
                    
                    **Process Context:**
                    A business analyst conducts a needs analysis for a client to gather requirements for a potential digitalization project. The process includes a flow of tasks, interactions, and decision points.
                    
                    **Execution Steps:**
                    1. Include the following sub-processes.
                        - Initial Meeting with Client:
                            - The client schedules a meeting with the business analyst.
                            - The analyst confirms the meeting time and prepares the agenda.
                        - Requirements Gathering:
                            - During the meeting, the analyst collects high-level requirements from the client.
                        - Requirements Analysis:
                            - The analyst analyzes the collected information to identify gaps or unclear points.
                        - Client Feedback:
                            - The analyst shares the initial analysis with the client to get feedback.
                            - Gateway: If feedback is positive, the process continues; otherwise, the analyst returns to the analysis step.
                        - Final Report Preparation:
                            - The analyst prepares a detailed needs analysis report.
                        - Report Delivery:
                            - The final report is sent to the client for approval.
                    2. Include in the model:
                        - Message flows between pools,
                        - An exclusive gateway,
                        - Events with triggers,
                        - Text annotations,
                        - A closed pool for the client.
                    3. Add additional parameters:
                        - Duration for some tasks in alternative flows (e.g., requirements gathering – 2 hours; requirements analysis – 4 hours).
                        - Probabilities for decision points (e.g., 80% positive feedback, 20% requires re-analysis).
                    4. Analyze the results and create a separate document with suggestions:
                        - Identify bottlenecks or problematic areas (e.g., which part often delays the process).
                        - Provide optimization proposals (e.g., shorten process flow, assign an assistant for specific tasks, automate feedback collection).""")
        st.image(Image.open("images/d8.jpg"), use_column_width=True)
        st.markdown("""
                    **Bottlenecks / Problematic Areas:**
                    - **Lengthy analysis of collected information (4 hours).** This is the longest stage of the process. If the number of clients increases, the analyst may not keep up.
                    - **Waiting for client feedback.** The model only accounts for receiving feedback but does not control the waiting time.
                    - **Repeated analysis in case of negative feedback.** Requires additional time and resources and may repeat several times if feedback remains unsatisfactory.
                    - **Manual transfer of analysis to a competent analyst.**
                    
                    **Proposals for optimizing the process flow:**
                    1. **Automate feedback collection:**
                        - Use an online form (e.g., Google Forms or a CRM module).
                        - Set a time limit for responses (e.g., 24 hours), after which the system generates reminders or escalates the task.
                    2. **Assign an assistant or automate agenda preparation:**
                        - Delegate this task or support it with templates (question builders) to save the analyst’s time.
                    3. **Reduce analysis time using templates:**
                        - Use a report structure from previous cases.
                        - Use tools for requirement classification (e.g., Trello, Notion, Jira).
                    4. **Optimize handling of negative feedback:**
                        - Implement feedback categorization (technical / communication / expectations) to reduce unnecessary actions.
                        - If negative feedback is minor (e.g., stylistic), correct immediately without a full re-analysis.
                    5. **Implement KPIs for each stage:**
                        - For example: time to feedback, number of feedback cycles, average analysis time, number of cases requiring escalation.""")
