# Mapoe
Transform your poems into video art.

## Usage

Rename `poem.example.xm` to `poem.xm`, it looks for this exact filename so unless you change exclusively
in the code just remove the `example`

## How to Use

1. Install dependecies
`pip install -r requirements.txt`
2. Prepare Poem File
Rename `poem.example` to `poem` and structure your poem like [this](https://github.com/musaubrian/mapoe?tab=readme-ov-file#poemstructure)
3. Run the program
```sh
# [-p] tells manim to play the video after its done generating it
manim -p poem_scene.py
```
2. Add your poem contents in the predefined structure
3. Run with `manim poem_scene.py -p`
4. View get your video at `./media/videos/poem_scene/1280p60/<Similar to your poems title>`

## PoemStructure
The Library expects a very specific format of the poem for parsing.
It uses the `::` notation to structure the poem.

 Tag       | Description                  | Required   |
---        | ---                          | ---        |
`::title`  | The poems title              | Yes        |
`::verse`  | Each stanza of the poem      | At least 1 |
`::author` | The poems author             | No         |
`::image`  | path to the background image | No         |

Example:
```txt
::title
<your_title>
::

::image
<path/to/image/file>
::

::author
<poems_author>
::

::verse
<verse contents>
::

::verse
<more_verse_contents>
::
```
