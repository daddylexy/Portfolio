import random
import streamlit as st
import pandas as pd
from PIL import Image
import smtplib 
from email.mime.text import MIMEText

# Color picker for text color
# Color picker (hidden but still functional)
color = st.color_picker("", "#ffffff", label_visibility="collapsed")

# Sidebar navigation - always aligned left
active_tab = st.sidebar.radio("", ["HOME", "ABOUT ME", "PROJECTS", "RESUME", "CONTACT"])

# Background style based on active tab
if active_tab == "HOME":
    background_style = """
        background-image: url("https://i.imgur.com/9Fb8i3J.gif");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    """
else:
    background_style = "background-color: #c59e8f;" 

style_holder = st.empty()

# Inject CSS for pixel font, background, text color, sidebar styling
style_holder.markdown(
    f"""
    <style>
    /* Import pixel font */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    .stApp {{
        {background_style}
        font-family: 'Press Start 2P', monospace !important;
    }}

    body, .css-1d391kg p, .stText, .stMarkdown, .st-emotion-cache-qbgoph, .st-emotion-cache-1ort0lt, .st-bp, .st-emotion-cache-8atqhb, .st-emotion-cache-3jjymv,
    h1, h2, h3, h4, h5, h6 {{
        color: {color} !important;
        font-family: 'Press Start 2P', monospace !important;
    }}

    /* Hide radio circles only in sidebar */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] input[type="radio"] {{
        display: none !important;
    }}

    /* Style labels to remove padding and apply font */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label {{
        padding-left: 0 !important;
        margin-left: 0 !important;
        cursor: pointer;
        font-family: 'Press Start 2P', monospace !important;
    }}

    /* Make more space between sidebar items */
    .st-bs {{
        line-height: 2;
    }}

    /* Hide buttons on sidebar */
    .st-b9 {{
        width: 0;
    }}

    .st-emotion-cache-1lqf7hx {{
        position: relative;
        top: 0px;
        background-color: rgba(38, 39, 48, 0);
        z-index: 999991;
        min-width: 200px;
        max-width: 600px;
        transform: none;
        transition: transform 300ms, min-width 300ms, max-width 300ms;
        color: rgba(250, 250, 250, 0);
        color-scheme: dark;
    }}

    /*st.write text font size*/
    .st-emotion-cache-1w7qfeb {{
    font-family: 'Press Start 2P', monospace !important;
    font-size: .8rem;
    color: inherit;
    }}

    .st-emotion-cache-1weic72 {{
    font-size: 0.875rem;
    color: rgb(250, 250, 250);
    display: flex;
    visibility: visible;
    margin-bottom: 0.25rem;
    margin-top: 0rem;
    height: auto;
    min-height: 1.5rem;
    vertical-align: middle;
    flex-direction: row;
    -moz-box-align: center;
    align-items: center;
    }}

    /* Completely hide the color picker component */
    div[data-testid="stColorPicker"] {{
    display: none !important;
    }}

    /* Make the full top header bar semi-transparent */
    header[data-testid="stHeader"] {{
    background-color: rgba(62, 47, 44, 0) !important;
    backdrop-filter: blur(0px);
    border-bottom: 0px solid rgba(234, 212, 204, 0.8);
    transition: background-color 0.3s ease;
    }}

    /* Sidebar background (expanded and collapsed) */
    [data-testid="stSidebar"] {{
    background-color: rgba(127, 88, 73, 0.5) !important;
    backdrop-filter: blur(2px);
    transition: background-color 0.3s ease;
    }}

    /* Sidebar inner content */
    [data-testid="stSidebarContent"] {{
    background-color: rgba(62, 47, 44, 0) !important;
    transition: background-color 0.3s ease;
    }}

    /*Move sidebar down*/
    .st-emotion-cache-ja5xo9 {{
    padding-top: 150px;
    padding-bottom: 0rem;
    padding-left: max( calc(var(--scrollbar-width)), calc(1rem - var(--scrollbar-width)) );
    padding-right: max( calc(var(--scrollbar-width)), calc(1rem - var(--scrollbar-width)) );
    }}

    /* Fix flashing background during collapse animation */
    [data-testid="stSidebar"]::before {{
    background-color: rgba(62, 47, 44, 0) !important;
    }}

    /* Base style for sidebar labels with transition prep */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label {{
    display: inline-block;
    transition: all 0.3s ease-in-out;
    font-size: 6px; /* base size, adjust if needed */
    }}

    /* Hover effect on sidebar items with expansion */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label:hover {{
    background-color: rgba(234, 212, 204, 0.2) !important;
    color: #fff !important;
    transform: scale(1.1);
    font-size: 11px;
    border-radius: 6px;
    }}


    /* Move the selectbox higher on the page */
    div[data-testid="stSelectbox"] {{
    margin-top: 20px !important;  /* Adjust the value to your liking */
    }}

    /* Style the image container */
    div[data-testid="stImageContainer"] img {{
    border: 9px solid #EAD4CC;         /* Pixel-style color */
    border-radius: 0px;                /* Rounded corners (optional) */
    box-shadow: 0 0 12px #EAD4CC;      /* Soft glow effect */
    padding: 0px;                      /* Padding inside the border */
    max-width: 100%;
    height: auto;
    }}

    /* Selectbox container transparency */
    div[class*="st-c5"][class*="st-c6"][class*="st-c7"] {{
    background-color: rgba(62, 47, 44, 0.2) !important;
    backdrop-filter: blur(0px);
    border-radius: 18px;
    border: 0px solid #EAD4CC;
    padding: 0px;
    transition: background-color 0.3s ease;
    }}

    /* Dropdown background container */
    ul[data-testid="stSelectboxVirtualDropdown"] {{
    background-color: rgba(62, 47, 44, 0.4) !important;
    backdrop-filter: blur(0px);
    border-radius: 18px;
    padding: 10px;
    border: 0px solid rgba(255, 255, 255, 0.2);
    }}

    /* Dropdown list items */
    ul[data-testid="stSelectboxVirtualDropdown"] li {{
    background-color: rgba(255, 255, 255, 0);
    border-radius: 0px;
    padding: 8px 12px;
    margin-bottom: 5px;
    color: #ffffff !important;
    transition: background-color 0.2s ease, transform 0.2s ease;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 10px;
    }} 

    /* Hover effect on dropdown items */
    ul[data-testid="stSelectboxVirtualDropdown"] li:hover {{
    background-color: rgba(255, 255, 255, 0.15);
    transform: scale(1.01);
    cursor: pointer;
    }}

    /* Make Streamlit DataFrame square-edged */
    [data-testid="stDataFrame"] .stDataFrameGlideDataEditor {{
        border-radius: 2rem !important;
    }}

    /*Width of the text_area boxes*/
    .st-c4 {{
    width: 100%;
    }}

    /* Target the actual textarea inside base-input */
    div[data-baseweb="base-input"] textarea {{
        background-color: rgba(179, 147, 127, 0) !important;
        color: white !important;              /* Change text color */
        border: 0px solid #72769b !important; /* Optional border */
        border-radius: 12px !important;        /* Rounded corners */
        padding: 24px !important;              /* Optional: inner space */
    }}

    /* Optional: clear background of wrapper */
    div[data-baseweb="base-input"] {{
        background-color: transparent !important;
    }}

    /* Change the background color of the container */
    .st-d0 {{
    background-color: rgba(234, 212, 204, 0.2) !important;  /* example soft beige */
    }}

    /* Change border colors */
    .st-cz {{
    border-bottom-color: rgba(234, 212, 204, 0.2) !important;  /* light border bottom */
    }}

    .st-cy {{
    border-top-color: rgba(234, 212, 204, 0.2) !important;
    }}

    .st-cx {{
    border-right-color: rgba(234, 212, 204, 0.2) !important;
    }}

    .st-cw {{
    border-left-color: rgba(234, 212, 204, 0.2) !important;
    }}

    .st-emotion-cache-zuyloh {{
    border: 5px solid rgba(250, 250, 250, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    width: 100%;
    height: 100%;
    overflow: visible;
    }}

    .st-emotion-cache-z8vbw2 {{
        background-color: rgba(255, 255, 255, 0.2)
    }}

    .st-b3 {{
    margin-top: -0.6rem;
    }}
    
    .st-ao {{
    margin-top: 12px;
    }}
    
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content based on selected tab
if active_tab == "HOME":
    st.write("")

elif active_tab == "ABOUT ME":
    st.subheader("ABOUT ME")
    st.divider()

    st.write("Hi! My name is Analexy Galvan Galvan. I am a Computer Science Senior currently attending the University of Texas Rio Grande Valley.")

    c1, c2, c3= st.columns([.5, 3, .5])
    
    with c2:
        st.image("languages.gif", use_container_width=True)


    st.write("I enjoy working with data — organizing, analyzing, and turning it into meaningful insights that help solve real problems. I’m eager to grow as a data analyst and make an impact in this world.")
    st.write("Currently, I know a total of three lamguages; C++, SQL, and Python. I would not say I am proficient in them but I can defientelly solve easy to medium problems on LeetCode.")

    

elif active_tab == "PROJECTS":
    st.subheader("PROJECTS")
    projects = st.selectbox("Search", [
        " ",
        "Amazon's Sales Dataset",
        "p2",
        "p3",
        "p4"
    ])

    if projects == "Amazon's Sales Dataset":

        st.subheader("Description")
        st.write("For this project I took an amazon data set found on Kraggle, and tried to find useful insights that would benefit the company!")
        Amazon_Dataset = pd.read_csv("amazon_sales_data 2025.csv")
        st.dataframe(Amazon_Dataset)

        st.write("What is the total sales revenue for the entire dataset?\n")
        st.markdown('<p style="color: pink;">$184,257,625</p>', unsafe_allow_html=True)
        st.write("How many total orders were made?\n")
        st.markdown('<p style="color: pink;">243,835</p>', unsafe_allow_html=True)
        st.write("What is the average order value?\n")
        st.write("")
        st.write("How do monthly sales compare over the year?\n")
        st.markdown('<p style="color: pink;">The most sales were made in the month of February.</p>', unsafe_allow_html=True)
        st.write("**Which day of the week has the highest number of orders?\n**")
        st.write("")

    elif projects == "p2":
        st.write("p2 project info")
    elif projects == "p3":
        st.write("p3 project info")
    elif projects == "p4":
        st.write("p4 project info")

elif active_tab == "RESUME":
    st.subheader("Analexy Galvan Galvan")
    st.write("**Languages:**")
    st.write("C++, Python, SQL")
    st.write("**Experience:**")


elif active_tab == "CONTACT":
    st.subheader("CONTACT ME")
    st.divider()
    image = Image.open("contactpicture.jpg")
    resized_image = image.resize((221, 300), Image.LANCZOS)

    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.image(resized_image)
        st.write("Email: lexy5076@gmail.com")

    

    # Email function
    def send_otp(email, otp_code):
        msg = MIMEText(f"Your verification code is: {otp_code}")
        msg["Subject"] = "Verify your email"
        msg["From"] = st.secrets["email"]["address"]
        msg["To"] = email

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(st.secrets["email"]["address"], st.secrets["email"]["password"])
        server.send_message(msg)
        server.quit()

    # Set default state values
    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False
    if "otp" not in st.session_state:
        st.session_state.otp = ""
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "message" not in st.session_state:
        st.session_state.message = ""
    if "clear_form_now" not in st.session_state:
        st.session_state.clear_form_now = False

    # Clear form values before widgets are created
    if st.session_state.clear_form_now:
        st.session_state.email = ""
        st.session_state.name = ""
        st.session_state.message = ""
        st.session_state.clear_form_now = False



    # Form to collect email, name, and message
    with st.form("contact_form"):
        st.text_area("Your Email", key="email", height=68)
        st.text_area("Your Name", key="name", height=68)
        st.text_area("Send Me A Message:", key="message", height=200)

        submit_label = "Send Message" if st.session_state.otp_sent else "Send Verification Code"
        submitted = st.form_submit_button(submit_label)

        if submitted:
            if not st.session_state.otp_sent:
                if st.session_state.email:
                    st.session_state.otp = str(random.randint(100000, 999999))
                    try:
                        send_otp(st.session_state.email, st.session_state.otp)
                        st.session_state.otp_sent = True
                        st.success(f"Verification code sent to {st.session_state.email}")
                    except Exception as e:
                        st.error(f"Failed to send verification code: {e}")
                else:
                    st.warning("Please enter your email to get verification code.")

    # Separate input (outside the form) for the OTP field
    if st.session_state.otp_sent:
        entered_otp = st.text_input("Enter Verification Code")
        if entered_otp:
            if entered_otp == st.session_state.otp:
                try:
                    full_message = f"From: {st.session_state.name} <{st.session_state.email}>\n\n{st.session_state.message}"
                    msg = MIMEText(full_message)
                    msg["Subject"] = "New Message From Portfolio"
                    msg["From"] = st.secrets["email"]["address"]
                    msg["To"] = st.secrets["email"]["address"]

                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.login(st.secrets["email"]["address"], st.secrets["email"]["password"])
                    server.send_message(msg)
                    server.quit()

                    st.success("✅ Message sent successfully!")
                    st.session_state.otp_sent = False
                    st.session_state.otp = ""
                    st.session_state.email = ""
                    st.session_state.name = ""
                    st.session_state.message = ""
                except Exception as e:
                    st.error(f"Failed to send message: {e}")
            else:
                st.error("Incorrect verification code. Please try again.")
        
    if st.button("Cancel"):
        st.session_state.otp_sent = False
        st.session_state.otp = ""
        st.session_state.clear_form_now = True  # Set the clear flag
        st.rerun()





