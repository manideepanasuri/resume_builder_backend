from django.contrib.auth import get_user_model

from ai_integration.serializers import ResumeSerializer

from google import genai

from resume_builder import settings

prompt="""
You are an expert LaTeX resume generator, specialized in creating ATS-optimized, grammatically refined resumes tailored to job descriptions. Input will be in 3 parts, separated by double newlines (\n\n):

1. LaTeX resume template (raw string)
2. Structured resume data of user (JSON or similar)
3. Job description (plain text, or empty if not provided)

Use **only the data provided by the user**. Do not fabricate, infer, or assume any information. If any field or section (like skills, projects, experience, etc.) is missing or empty in the structured data, comment out that section in the resume output.

If a job description is provided:

- Analyze the LaTeX template structure and formatting.
- Extract relevant skills, experiences, and project types from the job description.
- From the user data:
  - Include **all education entries**.
  - Select **at least 3 relevant projects** (or all, if fewer).
  - Include **all relevant experiences**.
- Optimize for ATS:
  - Use standard LaTeX commands and section headers ("Education", "Experience", "Skills", etc.).
  - Avoid tables, images, nonstandard formatting or symbols.
  - Use full words instead of abbreviations.
  - Prioritize and integrate keywords from the job description.
- Expand bullet points using related input data when possible.
- Add extra bullet points using related input data when possible.
- Refine grammar and sentence clarity for professional tone.
- Insert user-provided data into the template, preserving its format.

If no job description is provided:

- Use **all** structured data provided by the user.
- Include **all education, projects, and experiences**.
- Ensure ATS compliance, refine language, and fill the LaTeX template accordingly.

Output:

- Return only the **complete LaTeX code** of the resume.
- Ensure it is **compilable without any errors**.
- **Do not include markdown code blocks or extra text** — only the raw LaTeX.
- If the output is too long, split it into clearly labeled parts like "Part 1 of N", "Part 2 of N", etc.
- End each part (except the last) with `%%CONTINUE%%`.
- Always end the **final part** with `%%END%%`, even if the entire output fits in one message.

"""

User=get_user_model()
def gen_resume(user:User,jobdescription,template):
    data=ResumeSerializer(user).data
    user_data=str(data)
    total_text=prompt+'Latex template: \n'+template+'\nUser data: \n'+user_data+'\nJob descreption: \n'+jobdescription
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    chat = client.chats.create(model="gemini-2.0-flash")
    total_res=""
    resp=chat.send_message(total_text)
    total_res+=resp.text
    coun=0
    while True:
        if coun>10:
            break
        if "%%END%%" in total_res:
            break
        resp=chat.send_message("continue")
        total_res+=resp.text
    return total_res