def organize_files(directory):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz']
    }
    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                if any(filename.endswith(ext) for ext in extensions):
                    shutil.move(os.path.join(directory, filename), folder_path)