import re
import twilio.twiml

__author__ = 'codyaray'


class Applet(object):

    ABSOLUTE_URL = re.compile('http(s)?://(.*)', re.IGNORECASE)

    def handle(self, req, res):
        raise NotImplementedError("Must implement Applet#handle")

    def set_verb_for_value(self, value, res, voice=twilio.twiml.Say.MAN, language=twilio.twiml.Say.ENGLISH):
        if self.ABSOLUTE_URL.match(value):
            return res.play(value)
        else:
            return res.say(value, voice=voice, language=language)

    @staticmethod
    def redirect(res, url=""):
        return res.redirect("/?applet=%s" % url if url else "")