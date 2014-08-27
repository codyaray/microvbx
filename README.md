# MicroVBX

A micro VBX framework for [Twilio](http://twilio.com) built on [Flask](http://flask.pocoo.org/).

## Usage

1. Run MicroVBX like any flask app. The easiest way to get going:

    `python app.rb`

2. In a new terminal, use [Ngrok](http://ngrok.com) to proxy a public web address for your app:

    `ngrok 5000`

3. Create a new flow for your app. See `flows/wedding.py` for an example.

4. Assign the ngrok URL and flow route to one of your
   [Twilio numbers](https://www.twilio.com/user/account/phone-numbers/incoming). For example:

    `Voice Request Url: http://7b5a904a.ngrok.com/myflow`

5. Call your Twilio phone number!

## Design

* A library of reusable plugins provide for common use cases atop of TwiML.
* A flow is a state machine of configured applets and their transitions which forms the call tree.
* Multiple flows are supported, each corresponding to a separate flask route.

Many of these applets are based on [openvbx.org](http://openvbx.org) plugins.

## Example

MicroVBX was built for RSVPing to my wedding by phone. This is included as an example flow.
