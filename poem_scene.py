from parser import Poem
from manim import (
    DOWN,
    UP,
    BOLD,
    config,
    ImageMobject,
    Write,
    Scene,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    LaggedStart,
    ReplacementTransform,
)

config.pixel_width = 720
config.pixel_height = 1280


raw_poem = ""
with open("./poem", "r") as f:
    raw_poem = f.read()


parsed_poem = Poem(raw_poem)
config.output_file = parsed_poem.out_file_name


class PoemScene(Scene):
    def construct(self):
        background_image = None
        if parsed_poem.image:
            background_image = ImageMobject(parsed_poem.image)
            background_image.set(
                width=self.camera.frame_width, height=self.camera.frame_height
            )
            background_image.set_opacity(0.50)
            self.add(background_image)

        title = Text(
            parsed_poem.title,
            font_size=70,
            font="Zed Mono",
            weight=BOLD,
        )

        title.to_edge(UP, buff=0.2)
        self.play(FadeIn(title, run_time=1.5))
        self.wait()

        for verse_index, verse in enumerate(parsed_poem.verses):
            verse_lines = verse.strip().split("\n")
            text_group = VGroup()

            for line in verse_lines:
                text = Text(
                    line.strip(),
                    font_size=47,
                    font="Zed Mono",
                )
                text_group.add(text)

            text_group.arrange(DOWN, buff=0.2)
            text_group.next_to(title, DOWN, buff=0.5)

            for line in text_group:
                # self.play(FadeIn(line, scale=0.3, run_time=1), run_time=1.5)
                self.play(Write(line, run_time=2))
                self.wait()

            if verse_index < len(parsed_poem.verses) - 1:
                self.play(
                    FadeOut(text_group, run_time=1),
                    run_time=1.5,
                )
                self.wait()

        author_text = Text(
            f"By {parsed_poem.author}" or "Anonymous",
            font_size=55,
            font="Zed Mono",
            weight=BOLD,
        )
        author_text.next_to(title, DOWN, buff=0.5)
        if background_image:
            self.play(
                LaggedStart(
                    FadeOut(text_group, run_time=1, shift=DOWN),
                ),
                background_image.animate.set_opacity(0.15),
                lag_ratio=0.25,
                run_time=2,
            )
        else:
            self.play(FadeOut(text_group, run_time=1, shift=DOWN))

        self.wait()
        self.play(ReplacementTransform(title, author_text, run_time=1.5))
        self.wait()
