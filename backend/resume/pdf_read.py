import pdfplumber
text = ""
with pdfplumber.open("rahulresume.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() or ""
        text=text.lower()

with open("skille.txt","r") as f:
    data = f.read()
    data = data.splitlines()
    totle_skills=len(data)
    found_skills=[]
    print(f"Total skills to check: {totle_skills}")
    for line in data:
        line=line.lower()
        if line in text:
            found_skills.append(line)

score = (len(found_skills) / totle_skills) * 100
print(f"Total skills found: {len(found_skills)}")
print("Resume Score:", int(score), "/100")
print("Skills Found:", found_skills)

missing_skills = set(data) - set(found_skills)
print("Missing Skills:", list(missing_skills))