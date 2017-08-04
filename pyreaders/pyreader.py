import pkg_resources

formats = ['.csv']

def main(file_type):
    for entry_point in pkg_resources.iter_entry_points("pyreader_types"):
        formats.extend(entry_point.load())

    if file_type in formats:
        print("Yes, I can read the file")
    else:
        print("No, I cannot read the file")

if __name__ == "__main__":
    import sys
    file_type = sys.argv[1]
    main(file_type)
