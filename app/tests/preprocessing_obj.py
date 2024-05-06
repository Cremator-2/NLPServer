from api.api_v1.processing.processing import TextPreprocessor


preprocessor = TextPreprocessor()
example_text = """
I thought this was a wonderful way to spend time on a too hot summer weekend, sitting in the air conditioned theater and watching a light-hearted comedy. The plot is simplistic, but the dialogue is witty and the characters are likable (even the well bread suspected serial killer). While some may be disappointed when they realize this is not Match Point 2: Risk Addiction, I thought it was proof that Woody Allen is still fully in control of the style many of us have grown to love.<br /><br />This was the most I'd laughed at one of Woody's comedies in years (dare I say a decade?). While I've never been impressed with Scarlet Johanson, in this she managed to tone down her ""sexy"" image and jumped right into a average, but spirited young woman.<br /><br />This may not be the crown jewel of his career, but it was wittier than ""Devil Wears Prada"" and more interesting than ""Superman"" a great comedy to go see with friends.
"""

print("\nTo Lowercase:")
print(preprocessor.to_lowercase(example_text))

print("\nRemove HTML Tags:")
print(preprocessor.remove_html_tags(example_text))

print("\nRemove Punctuation:")
print(preprocessor.remove_punctuation(example_text))

print("\nRemove Stop Words:")
print(preprocessor.remove_stop_words(example_text))

print("\nStem Text:")
print(preprocessor.stem_text(example_text))

print("\nFull Preprocessing:")
print(preprocessor.preprocess(example_text))
