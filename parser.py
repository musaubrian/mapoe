import re
import os


class Poem:
    """
    Poem defines the expected structure for the poem data

    Structure:
    =====
    ::font
    Zed Mono
    ::
    ::image
    path/to/image
    ::
    ::title
    Beautiful Words
    ::
    ::verse
    I may never find
    words beautiful enough
    ::
    ::verse
    to describe all
    that you mean to me,
    ::
    ::author
    John MarkGreen
    ::
    """

    def __init__(self, text):
        self.raw_text = text
        self.title = ""
        self.verses = []
        self.author = ""
        self.image = ""
        self.out_file_name = ""
        self.parse()

    def parse(self):
        comment_pattern = r"{{(.*?)}}"
        comment_match = re.search(comment_pattern, self.raw_text, re.DOTALL)
        if comment_match:
            self.raw_text = re.sub(comment_pattern, "", self.raw_text, flags=re.DOTALL)

        title_pattern = r"::title(.*?)::"
        title_match = re.search(title_pattern, self.raw_text, re.DOTALL)
        if title_match:
            self.title = title_match.group(1).strip()
            self.out_file_name = self.create_file_name()
        else:
            raise ValueError("[POEM]: expected one title, none were found")

        verse_pattern = r"::verse(.*?)::"
        self.verses = [
            verse.strip().replace("\n\n", "\n")
            for verse in re.findall(verse_pattern, self.raw_text, re.DOTALL)
        ]

        if not self.verses:
            raise ValueError("[POEM]: Expects atleast 1 verse")

        image_pattern = r"::image(.*?)::"
        image_match = re.search(image_pattern, self.raw_text, re.DOTALL)
        if image_match:
            self.image = image_match.group(1).strip()
            if "~" in self.image:
                self.image = os.path.abspath(os.path.expanduser(self.image))

            self.image = os.path.abspath(self.image)

        author_pattern = r"::author(.*?)::"
        author_match = re.search(author_pattern, self.raw_text, re.DOTALL)
        if author_match:
            self.author = author_match.group(1).strip()

        font_pattern = r"::font(.*?)::"
        font_match = re.search(font_pattern, self.raw_text, re.DOTALL)
        if font_match:
            self.font = font_match.group(1).strip()

    def create_file_name(self) -> str:
        filename = re.sub(r"[^a-zA-Z0-9]", " ", self.title)
        filename = filename.replace(" ", "_")
        filename = re.sub(r"_+", "_", filename)  # remove excess underscores
        return filename

    def __repr__(self):
        return f"POEM(image='{self.image},'title='{self.title}', verses={len(self.verses)}, author='{self.author}')"
