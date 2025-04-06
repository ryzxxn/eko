def replace_ids_with_names(file_path, id_name_mapping):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace IDs with names in the content
    for id, name in id_name_mapping.items():
        content = content.replace(id, name)

    # Save the updated content back to a new file
    updated_file_path = "updated_discord_messages.txt"
    with open(updated_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"IDs replaced with names and saved to '{updated_file_path}'")

# ID-name mappings
id_name_mapping = {
    "625313360128245775": "your favorite aunty",
    "474648328936882206": "vedantK",
    "604157203972096041": "switchKD",
    "599173414317588490": "pussylord",
    "466082173360013314": "obby",
    "647883985455677450": "pringles"
}

# Specify the path to your file
file_path = "discord_messages.txt"

# Run the function
replace_ids_with_names(file_path, id_name_mapping)
