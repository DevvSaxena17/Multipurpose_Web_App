import streamlit as st
import time
import os
import webbrowser
import urllib.parse

# Page settings
st.set_page_config(page_title="🖤 Python Automation App", layout="centered")

# Custom CSS (neon glow + TikTok palette)
st.markdown(
    """
    <style>
        body {
            background-color: #000000;
        }
        .main {
            background-color: #111111;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 0 20px #74f0ed88;
            border: 1px solid #222;
        }
        h1 {
            color: white;
            text-align: center;
            font-size: 2.8rem;
            text-shadow: 2px 2px #ea445a;
        }
        .stButton>button {
            background-color: #181818;
            border: 2px solid #74f0ed;
            color: white;
            font-weight: bold;
            border-radius: 24px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #ea445a;
            border-color: #ea445a;
            color: white;
            transform: scale(1.05);
        }
        @media (max-width: 600px) {
            .main {
                padding: 10px;
                border-radius: 10px;
            }
            h1 {
                font-size: 1.5rem;
            }
            .stButton>button {
                padding: 8px 10px;
                font-size: 1rem;
            }
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    "<h1>MULTIPURPOSE <span style='color:#74f0ed'>WEB APP</span></h1>",
    unsafe_allow_html=True,
)

# Initialize logs in session state
if "logs" not in st.session_state:
    st.session_state["logs"] = []

def log_action(action):
    st.session_state["logs"].append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}")

# Email Section
def email_section():
    st.header("📧 Send an Email")
    recipient = st.text_input("Recipient Email")
    subject = st.text_input("Subject", value="Hello from Streamlit!")
    message = st.text_area("Message", value="This is sent from Streamlit!")
    if st.button("Open Email Client"):
        if not recipient:
            st.error("Recipient email address is required.")
        else:
            mailto_link = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(message)}"
            js = f"window.open('{mailto_link}');"
            st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
            log_action(f"Opened email client for {recipient} with subject '{subject}'")
            st.toast("Opened email client!", icon="✅")

# WhatsApp Section
def whatsapp_section():
    st.header("💬 Send a WhatsApp Message")
    phone = st.text_input("Recipient Phone (with country code, e.g., 9198xxxx3210)")
    wa_message = st.text_area("Message", value="Hello from Streamlit WhatsApp!")
    if st.button("Open WhatsApp Web"):
        if not phone:
            st.error("Phone number is required.")
        else:
            url = f"https://wa.me/{phone}?text={urllib.parse.quote(wa_message)}"
            js = f"window.open('{url}');"
            st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
            log_action(f"Opened WhatsApp Web for {phone} with message '{wa_message}'")
            st.toast("Opened WhatsApp Web!", icon="✅")

# Social Media Section
def social_media_section():
    st.header("🌐 Post on Social Media")
    col1, col2 = st.columns(2)
    post_message = "This is a post done by Multipurpose Web App"
    share_url = "https://multipurposewebapp.streamlit.app/"  # You can use your app's URL or any relevant URL

    # Instagram (no direct post possible)
    with col1:
        if st.button("📸 Instagram"):
            st.markdown("[Open Instagram](https://instagram.com)", unsafe_allow_html=True)
            log_action("Displayed Instagram link")

    # LinkedIn
    with col1:
        if st.button("🗣 LinkedIn"):
            linkedin_share = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(share_url)}"
            st.markdown(f"[Share on LinkedIn]({linkedin_share})", unsafe_allow_html=True)
            log_action("Displayed LinkedIn share link")

    # Twitter
    with col2:
        if st.button("🐦 Twitter"):
            twitter_share = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(post_message)}"
            st.markdown(f"[Tweet]({twitter_share})", unsafe_allow_html=True)
            log_action("Displayed Twitter share link")

    # Facebook
    with col2:
        if st.button("📘 Facebook"):
            facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote(share_url)}"
            st.markdown(f"[Share on Facebook]({facebook_share})", unsafe_allow_html=True)
            log_action("Displayed Facebook share link")

# SMS Section
def sms_section():
    st.header("📱 Send SMS")
    sms_phone = st.text_input("Recipient Phone (with country code, e.g., 9198xxxx2210)", key="sms_phone_tab")
    sms_message = st.text_area("Message", value="Hello from Python!", key="sms_message_tab")
    if st.button("Open SMS App"):
        if not sms_phone:
            st.error("Phone number is required.")
        else:
            sms_url = f"sms:{sms_phone}?body={urllib.parse.quote(sms_message)}"
            js = f"window.open('{sms_url}');"
            st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
            log_action(f"Opened SMS app for {sms_phone} with message '{sms_message}'")
            st.toast("Opened SMS app!", icon="✅")

# Phone Call Section
def phone_call_section():
    st.header("📞 Make a Phone Call")
    call_phone = st.text_input("Phone Number to Call (with country code, e.g., 91987xxxx210)", key="call_phone_tab")
    if st.button("Open Dialer"):
        if not call_phone:
            st.error("Phone number is required.")
        else:
            call_url = f"tel:{call_phone}"
            js = f"window.open('{call_url}');"
            st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
            log_action(f"Opened dialer for {call_phone}")
            st.toast("Opened dialer!", icon="✅")

# Tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📧 Email",
    "📱 SMS",
    "📞 Phone Call",
    "💬 WhatsApp",
    "🌐 Social Media"
])

with tab1:
    email_section()
with tab2:
    sms_section()
with tab3:
    phone_call_section()
with tab4:
    whatsapp_section()
with tab5:
    social_media_section()

# Remove the task history/logs section from the bottom of the app. Do not display logs or info about actions performed.
# Keep log_action function for possible future use.

st.markdown("🖤 Designed by Dev Saxena")
