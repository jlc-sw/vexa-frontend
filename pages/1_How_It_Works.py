import streamlit as st
from PIL import Image
import base64

# === Load and encode the logo ===
logo_path = "assets/vexa_logo.png"
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# === Header: Logo on left, title centered vertically ===
st.markdown(
    f"""
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
        <img src="data:image/png;base64,{encoded_logo}" alt="Vexa Logo" width="120"/>
        <h1 style="margin: 0;">Welcome to Vexa</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# === Body content ===
st.markdown("""
Vexa connects your brand to next-generation discovery opportunities.

🌐 Join our private beta and explore a new way to grow visibility.

---

👁️ We work with select partners during early access.  
✍️ Submit your content to get started.
""")

# === CTA button ===
if st.button("Submit Sponsored Content"):
    st.switch_page("pages/2_Submit_Content.py")




##########################
##########################
#import streamlit as st
#from PIL import Image

# --- Load and display the logo ---
#logo = Image.open("assets/vexa_logo.png")
#st.image(logo, width=150)  # You can adjust the width to fit nicely

#st.title("Welcome to Vexa")

#st.markdown("""
#Vexa connects your brand to next-generation discovery opportunities.

#🌐 Join our private beta and explore a new way to grow visibility.

#---

#👁️ We work with select partners during early access.  
#✍️ Submit your content to get started.
#""")

#if st.button("Submit Sponsored Content"):
#    st.switch_page("pages/2_Submit_Content.py")

#############################
#############################
#import streamlit as st
#from PIL import Image

#logo = Image.open("assets/vexa_logo.png")

#col1, col2 = st.columns([1, 4])
#with col1:
#    st.image(logo, width=120)
#with col2:
#    st.markdown("## Welcome to Vexa")

#st.markdown("""
#Vexa connects your brand to next-generation discovery opportunities.

#🌐 Join our private beta and explore a new way to grow visibility.

#---

#👁️ We work with select partners during early access.  
#✍️ Submit your content to get started.
#""")

#if st.button("Submit Sponsored Content"):
#    st.switch_page("pages/2_Submit_Content.py")

#############################################
############################################


