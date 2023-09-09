import paralleldots
class API:
    def __init__(self):

        paralleldots.set_api_key( "NUNKqcYnIy5QffKF4pO0JoATQVTjy26vJIhoHFyWtGo")

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis (self, text):

        response = paralleldots.ner(text)
        return response

    def emo_analysis (self, text):

        response = paralleldots.emotion(text)
        return response
