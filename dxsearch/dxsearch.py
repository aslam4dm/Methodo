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

    # search switch specified : Note: when -fc or -pc are specified, the argument will ignore letter casing using the .lower() str function
    else:
        # --file_contains specified (search multiple file contains with ',')
        if file_contains != None and path_contains is None:
            if ',' in file_contains:
                file_contains = file_contains.split(',')
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # multiple input by user, separated by ','
                    if type(file_contains) == list:
                        for f in file_contains:
                            if f.lower() in file.lower() and file.endswith(extensions):
                                try:
                                    if search == "*" or search == "ALL":
                                        print(f"{root}/{file}")
                                        os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                    else:
                                        os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                                except:
                                    pass
                            else:
                                pass
                    # single file_contain specified
                    else:
                        if file_contains.lower() in file.lower() and file.endswith(extensions):
                            try:
                                if search == "*" or search == "ALL":
                                    print(f"{root}/{file}")
                                    os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                else:
                                    os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                            except:
                                pass

        # --path_contains specified (search multiple path contains with ',')
        elif file_contains is None and path_contains != None:
            if ',' in path_contains:
                path_contains = path_contains.split(',')
            for root, dirs, files in os.walk(folder_path):
                if type(path_contains) == list:
                    for p in path_contains:
                        for file in files:
                            if p.lower() in root.lower() and file.endswith(extensions):
                                try:
                                    if search == "*" or search == "ALL":
                                        print(f"{root}/{file}")
                                        os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                    else:
                                        os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                                except:
                                    pass
                            else:
                                pass
                # single path_contain specified
                else:
                    if path_contains.lower() in root.lower():
                        for file in files:
                            if file.endswith(extensions):
                                try:
                                    if search == "*":
                                        os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                    else:
                                        os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                                except:
                                    pass

        # --file_contains and --path_contains specified (does not support multi search when both arguments are present)
        elif file_contains != None and path_contains != None:
            for root, dirs, files in os.walk(folder_path):
                if path_contains.lower() in root.lower():
                    for file in files:
                        if file_contains.lower() in file.lower() and file.endswith(extensions):
                            try:
                                if search == "*" or search == "ALL":
                                    print(f"{root}/{file}")
                                    os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                                else:
                                    os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                            except:
                                pass
        else:
            files_found = []
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    try:
                        if search == "*" or search == "ALL":
                            print(f"{root}/{file}")
                            os.system(f"cat \"{root}/{file}\" 2>/dev/null")
                        else:
                            os.system(f"grep -i -H \"{search}\" \"{root}/{file}\" 2>/dev/null")
                    except:
                        pass
                        files_found.append(os.path.join(root, file))

def main():
    folder_path = "/mnt/media/DB/leaks/files"
    extensions = (".txt", ".csv", ".json", ".sql", ".sqlite3", ".html", ".db", ".dump", ".py")

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
