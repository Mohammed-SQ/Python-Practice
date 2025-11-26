def extract_files(text):
    # text: single string of file names separated by spaces
    parts = text.split()

    document_list = []
    image_list = []

    for name in parts:
        # case-sensitive checks
        if name.endswith(".pdf") or name.endswith(".docx"):
            document_list.append(name)
        elif name.endswith(".png") or name.endswith(".jpg"):
            image_list.append(name)

    # if a list is empty, put "None"
    if len(document_list) == 0:
        document_list.append("None")
    if len(image_list) == 0:
        image_list.append("None")

    return document_list, image_list


# ---------- Main Program ----------

# 1. Read all file names
line = input("Enter all file names (separated by spaces): ")

# 2. Remove files that start with '*'
files = line.split()

# must use remove() as the question says
for name in files[:]:          # loop over a copy of the list
    if name.startswith("*"):
        files.remove(name)

# rebuild the updated input string (names separated by spaces)
updated_text = ""
for i in range(len(files)):
    if i == 0:
        updated_text = files[i]
    else:
        updated_text = updated_text + " " + files[i]

# 3. Call the function
documents, images = extract_files(updated_text)

# 4. Counts (handle "None" specially)
if documents == ["None"]:
    doc_count = 0
else:
    doc_count = len(documents)

if images == ["None"]:
    img_count = 0
else:
    img_count = len(images)

# 5. Print results like sample
print("\nDocuments List:", documents)
print("Images List:", images)
print("Document count:", doc_count)
print("Image count:", img_count)
