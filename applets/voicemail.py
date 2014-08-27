from applets.applet import Applet


class VoicemailApplet(Applet):

    def __init__(self, prompt, save_message, postamble=None, next_applet=None):
        self.prompt = prompt
        self.save_message = save_message
        self.postamble = postamble
        self.next_applet = next_applet

    def handle(self, req, res):
        if req.values.get('RecordingUrl'):
            self.save_message(req.values.get('CallSid'), req.values.get('From'), req.values.get('To'),
                              req.values.get('RecordingUrl'), req.values.get('RecordingDuration'))
        else:
            self.set_verb_for_value(self.prompt, res)
            res.record()
            if self.postamble:
                self.set_verb_for_value(self.postamble, res)
        if self.next_applet:
            self.redirect(req, res, self.next_applet)
        return res
