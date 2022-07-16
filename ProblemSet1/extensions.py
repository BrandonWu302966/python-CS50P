file = input("File Name")
file = file.split(".")
i = file[-1].lower()
i = i.strip()
if i == "gif":
    print("image/gif")
elif i == "jpg":
        print("image/jpeg")
elif i == "jpeg":
        print("image/jpeg")
elif i == "png":
        print("image/png")
elif i == "pdf":
        print("application/pdf")
elif i == "txt":
        print("text/plain")
elif i == "zip":
        print("application/zip")
else:
        print("application/octet-stream")