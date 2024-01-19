filenames = ["1.raw data.txt.txt", "2.reports.txt", "3.presentation.txt"]

# filenames[2]= "-"
for filename in filenames:
    # filename[1] = "-"
    filename =filename.replace(".","-",1)

    print(filename)
