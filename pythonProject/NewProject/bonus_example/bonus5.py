contents = ["all carrots are to be sliced longitually.",
            "The carrots were reportedly sliced",
            "the slicing process are difficult"]

filenames = ["doc.txt","reports.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../file/{filename}", 'w')
    file.write(content)