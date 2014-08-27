# MicroVBX

A micro VBX framework for [Twilio](http://twilio.com) built on [Flask](http://flask.pocoo.org/).

## Design

* A reusable plugin library provides for common use cases atop of TwiML.
* A flow is a directed graph of applets (configured and instantiated plugins).
* This app supports a single "flow" defined in `config.py`.

Many of these applets are based on [openvbx.org](http://openvbx.org) plugins.

## Example

MicroVBX was built for RSVPing to my wedding by phone. This is included as an example app.
