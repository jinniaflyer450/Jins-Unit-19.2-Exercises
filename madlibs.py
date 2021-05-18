from stories import Story
from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def madlibs_form():
    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
    prompts = story.prompts
    return render_template('madlibsform.html', prompts = prompts)

@app.route('/story')
def story_results():
    story = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
    input_for_generate = {}
    for prompt in story.prompts:
        input_for_generate[prompt] = request.args[prompt]
    final_story = story.generate(input_for_generate)
    return render_template('story.html', story = final_story)

