from __future__ import with_statement   # Only necessary for Python 2.5
from applets.applet import Applet


class BaseMenuApplet(Applet):

    def __init__(self, prompt, menu_callback, next_option=None, invalid_option=None, repeat_count=3, **gather_args):
        self.prompt = prompt
        self.menu_callbacks = menu_callback
        self.next_option = next_option
        self.invalid_option = invalid_option
        self.repeat_count = repeat_count
        self.gather_args = gather_args

    def handle(self, req, res):
        digits = req.values.get('Digits', None)
        if digits:
            selected = self.menu_callbacks(digits)
            if selected:
                self.redirect(res, selected)
            else:
                if self.invalid_option:
                    self.set_verb_for_value(self.invalid_option, res)
                    res.redirect()
                else:
                    self.set_verb_for_value('You selected an incorrect option.', res)
            return res
        else:
            with res.gather(**self.gather_args) as gather:
                self.set_verb_for_value(self.prompt, gather)

                if self.repeat_count == -1:
                    res.redirect()
                else:
                    for i in xrange(self.repeat_count):
                        gather.pause(length=5)
                        self.set_verb_for_value(self.prompt, gather)
            if self.next_option:
                self.redirect(self.next_option)
            return res


class CookieStoreMenuApplet(BaseMenuApplet):
    def __init__(self, prompt, menu_callback, session=None, session_key=None, confirm=False, **kwargs):
        super(CookieStoreMenuApplet, self).__init__(prompt, self.wrap(menu_callback), **kwargs)
        self.session = session
        self.session_key = session_key
        self.confirm = confirm

    def handle(self, req, res):
        if self.confirm:
            if self.session.get("%s_confirm" % self.session_key):
                del self.session["%s_confirm" % self.session_key]
            else:
                digits = req.values.get('Digits', None)
                if digits:
                    # CONFIRMATION DIGITS
                    entered_digits = self.session.get("%s_tmp" % self.session_key)
                    if entered_digits:
                        del self.session["%s_tmp" % self.session_key]
                        if digits == "1":
                            self.session["%s_confirm" % self.session_key] = True
                            res.redirect("%s&Digits=%s" % (req.full_path, entered_digits))
                        else:
                            res.redirect()
                            return res
                    # ORIGINAL DIGITS
                    else:
                        self.session["%s_tmp" % self.session_key] = digits
                        with res.gather(**self.gather_args) as gather:
                            self.set_verb_for_value(self.confirm % " ".join(digits), gather)
                        res.redirect()
                    return res
        return super(CookieStoreMenuApplet, self).handle(req, res)

    def wrap(self, original_callback):
        def callback(digits):
            if digits and self.session and self.session_key:
                self.session[self.session_key] = digits
            return original_callback(digits)
        return callback


class MenuApplet(CookieStoreMenuApplet):
    def __init__(self, prompt, menu_items, **kwargs):
        menu_callback = lambda digits: menu_items[digits] if digits in menu_items else False
        num_digits = max(k for k, v in menu_items.iteritems())
        super(MenuApplet, self).__init__(prompt, menu_callback, numDigits=num_digits, **kwargs)
