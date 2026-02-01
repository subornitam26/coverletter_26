import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "GOOGLE_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Ai cover letter generator")

job_title = st.text_input("Job Title", placeholder="e.g., Data Analyst")
resume_summary = st.text_area("Resume Summary", placeholder="Enter key points from your resume (e.g., B.Com Honours, Excel/SQL/Power BI skills, Tally cert)...")

if st.button("Generate Cover Letter", type="primary"):
    if job_title and resume_summary:
        prompt = f"Write a cover letter for {job_title} using these resume points: {resume_summary}"
        
        with st.spinner("Generating cover letter with Gemini..."):
            response = model.generate_content(prompt)
            cover_letter = response.text
        
        st.subheader("Generated Cover Letter:")
        st.markdown(cover_letter)
        
        # Download option
        st.download_button(
            label="Download as TXT",
            data=cover_letter,
            file_name=f"cover_letter_{job_title.replace(' ', '_')}.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please fill in both job title and resume summary.")