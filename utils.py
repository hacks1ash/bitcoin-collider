def write_text_to_file(filename, text):
    text_file = None
    try:
        text_file = open('{}.txt'.format(filename), "a")
        text_file.write(text)

    except Exception as e:
        print(f"Error Occured while writing content to file - {e}")

    finally:
        text_file.close()


def read_text_from_file(filename):
    text_file = None
    try:
        text_file = open('{}.txt'.format(filename), "r")
        file_content = text_file.readlines()

    except Exception as e:
        print(f"Error Occurred while reading content to file - {e}")

    else:
        return file_content

    finally:
        text_file.close()
