import emoji


class Films:
    def __init__(self, name=None, text=None, response=None):
        self.name = name
        self.text = text
        self.response = response

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        emj = {'response good': ':thumbs_up:', 'response bad': ':thumbs_down:', 'response': '-', None: '-'}
        self._response = emoji.emojize(emj[value])

    def Tuple(self):
        return [self.name, self.text, self.response]
