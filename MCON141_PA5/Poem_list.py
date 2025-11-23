import os

DOCS_DIR = "docs"


# This function reads the code and saves it as a list
def load_poem_list(doc_filename):

    global lines
    lines = []
    full_path = os.path.join(DOCS_DIR, doc_filename)
    with open(full_path, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                lines.append(os.path.join(line))
    return lines


# This function reverses the lines and saves a new list
def reverse_poem(lines):

    global reversed_lines
    reversed_lines = lines[::-1]    # Reverses the list and saves as a new list
    return reversed_lines


# This function writes the reversed list into a new file
def write_new_poem(reversed_lines, doc_filename="poem2.txt"):

    full_path = os.path.join(DOCS_DIR, doc_filename)
    with open(full_path, "w") as f:
        for line in reversed_lines:
            f.write(line + "\n")


# This function appends my comments to the reversed poem
def append_comments(doc_filename="poem2.txt"):

    load_poem_list(doc_filename)
    full_path = os.path.join(DOCS_DIR, doc_filename)
    with open(full_path, "a") as f:
        f.write(" \n I love this poem because of its soothing melody and brilliant rhyme scheme. \n "
                "Notice how (in the original poem) the third line of each stanza rhymes with the first, second, and fourth of the next stanza. It is a work of genius.")
        f.write("\n Kayla Zagelbaum")


# Call the main function
def main():

    load_poem_list("Poem.txt")
    reverse_poem(lines)
    write_new_poem(reversed_lines)
    append_comments()


if __name__ == "__main__":
    main()
