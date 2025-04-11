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


col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=80)
with col2:
    st.markdown("## Welcome to Vexa")

st.markdown("""
Vexa connects your brand to next-generation discovery opportunities.

🌐 Join our private beta and explore a new way to grow visibility.

---

👁️ We work with select partners during early access.  
✍️ Submit your content to get started.
""")

if st.button("Submit Sponsored Content"):
    st.switch_page("pages/2_Submit_Content.py")
