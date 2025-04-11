
import streamlit as st

st.title("How Vexa Works")

st.markdown("""

# Welcome to Vexa

Vexa connects your brand to next-generation discovery opportunities.

🌐 Join our private beta and explore a new way to grow visibility.

---

👁️ We work with select partners during early access.
✍️ Submit your content to get started.


""")

# --- Call to action button ---
if st.button("Submit Sponsored Content"):
    st.switch_page("pages/2_Submit_Content.py")
