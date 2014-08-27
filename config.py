from flask import session
from applets import *


def save_voicemail(call_sid, call_from, call_to, recording_url, recording_duration):
    print call_sid, call_from, call_to, recording_url, recording_duration

SECRET_KEY = 'a secret key'

APPLETS = {
    "start": GreetingApplet("Hi! Thanks for R.S.V.P.ing to the wedding of Anna Dron and Cody Ray. ",
                            next_applet="rsvp-code"),
    "rsvp-code": CookieStoreMenuApplet("Please enter your personal RSVP code found in your invitation.",
                                       lambda digits: "attending", session, "rsvp_code", numDigits=3,
                                       confirm="We received %s. Press 1 if this is correct. "
                                               "Press any other key to re-enter your RSVP code."),
    "attending": MenuApplet("Will you be attending our wedding? Press 1 for yes. Press 2 for no.",
                            {'1': "how-many", '2': "thanks-anyway"}),
    "thanks-anyway": GreetingApplet("Okay, thanks for letting us know. We hope to see you soon!", next_applet="hangup"),
    "how-many": CookieStoreMenuApplet("Great! How many adults can we expect, including yourself?",
                                      lambda digits: "thanks", session=session, session_key="adults"),
    "thanks": MenuApplet("Wonderful! Do you want to leave us a personal message? Press 1 for yes, 2 for no.",
                         {'1': "call-me", '2': "goodbye"}),
    "call-me": VoicemailApplet("Thanks! Just leave it after the beep.", save_voicemail, postamble="We can't wait to hear it!", next_applet="goodbye"),
    "goodbye": GreetingApplet("Thanks! We'll see you at Crystal Grand on June 27th, 2015! Bye!", next_applet="hangup"),
    "hangup": HangupApplet(session)
}
