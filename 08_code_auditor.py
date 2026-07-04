import os
from google import genai

client = genai.Client()
target_folder = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-5/Day-30"
all_files = os.listdir(target_folder)

project_manifest = {}

print("--- Recieving Audits from AI ---\n")

for file in all_files:
    if (file.endswith(".cpp")) :
        full_path = os.path.join(target_folder, file)

        with open(full_path, "r") as f:
            raw_code = f.read()

        project_manifest[file] = raw_code

        response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = f"{file}-\n{raw_code}",
        config = genai.types.GenerateContentConfig(system_instruction = "For the given Code, look specifically for memory leaks, unused tracking components, or structural optimization errors, Also don't use any unnecesary symbols like *** for highlighting since your output will be on a terminal"),
        )
        
        print(response.text)

        print("\n---------------------------------------------------\n")