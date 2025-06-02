import os
import time
import argparse

def find_files_with_extensions(folder_path, extensions, search=None, file_contains=None, path_contains=None):
    # search switch not specified
    if search==None:
        files_found = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(extensions):
                    print(f"{root}/{file}")
                    files_found.append(os.path.join(root, file))
        return files_found

    # search switch specified
    else:
        # --file_contains specified
        if file_contains != None and path_contains == None:
            print(f"{file_contains}")
            files_found = []
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file_contains in file and file.endswith(extensions):
                        try:
                            if search == "*" or search == "ALL":
                                os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                            else:
                                os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                        except:
                            pass
                            files_found.append(os.path.join(root, file))

        # --path_contains specified
        elif file_contains == None and path_contains != None:
            files_found = []
            for root, dirs, files in os.walk(folder_path):
                if path_contains in root:
                    for file in files:
                        try:
                            if search == "*":
                                os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                            else:
                                os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                        except:
                            pass
                            files_found.append(os.path.join(root, file))

        # --file_contains and --path_contains specified
        elif file_contains != None and path_contains != None:
            files_found = []
            for root, dirs, files in os.walk(folder_path):
                if path_contains in root:
                    for file in files:
                        if file_contains in file and file.endswith(extensions):
                            print(file)
                            try:
                                if search == "*" or search == "ALL":
                                    os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                else:
                                    os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                            except:
                                pass
                                files_found.append(os.path.join(root, file))

        else:
            files_found = []
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    try:
                        if search == "*" or search == "ALL":
                            os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                        else:
                            os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                    except:
                        pass
                        files_found.append(os.path.join(root, file))

def main():
    folder_path = "/mnt/media/DB/leaks/files"
    extensions = (".txt", ".csv", ".json", ".sql", ".sqlite3", ".html", ".db", ".dump")

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="path to root file (files)", default="/mnt/media/DB/leaks/files")
    parser.add_argument('-s', '--search', help="search Username/Name/Email/IP etc.", default=None)
    parser.add_argument('-fc', '--file_contains', help="the name of the files to be queried contain 'x'", default=None)
    parser.add_argument('-pc', '--path_contains', help="the name of the paths to be queried contain 'x'", default=None)
    args = parser.parse_args()

    if args.search != None:
        find_files_with_extensions(args.path, extensions, args.search, args.file_contains, args.path_contains)
    else:
        find_files_with_extensions(args.path, extensions, None, args.file_contains, args.path_contains)

if __name__ == "__main__":
    main()
