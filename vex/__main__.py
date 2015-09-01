#!/usr/bin/env python3
# -*- coding: utf-8-*-
import os
import sys
import shutil
import logging
import argparse
import asyncio

import yaml

import tts, stt
from conversation import Conversation
from adapters import Shell

parser = argparse.ArgumentParser(description='Jasper Voice Control Center')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
args = parser.parse_args()

class Bot(object):
    def __init__(self, config_path=None, bot_name="vex"):
        self.name = bot_name
        # create logger
        self._logger = logging.getLogger(__name__)
        # adapters are inputs into the bot. Like a mic or shell input
        self._adapters = []
        self._adapters.append(Shell(self))

        # Read config
        #self._logger.debug("Trying to read config file: '%s'", new_configfile)
        """
        # TODO: Create a default config and load it by defaul
        try:
            with open(new_configfile, "r") as f:
                self.config = yaml.safe_load(f)
        except OSError:
            self._logger.error("Can't open config file: '%s'", new_configfile)
            raise
        """
        """
        try:
            stt_engine_slug = self.config['stt_engine']
        except KeyError:
            stt_engine_slug = 'sphinx'
            logger.warning("stt_engine not specified in profile, defaulting " +
                           "to '%s'", stt_engine_slug)
        stt_engine_class = stt.get_engine_by_slug(stt_engine_slug)

        try:
            slug = self.config['stt_passive_engine']
            stt_passive_engine_class = stt.get_engine_by_slug(slug)
        except KeyError:
            stt_passive_engine_class = stt_engine_class

        try:
            tts_engine_slug = self.config['tts_engine']
        except KeyError:
            tts_engine_slug = tts.get_default_engine_slug()
            logger.warning("tts_engine not specified in profile, defaulting " +
                           "to '%s'", tts_engine_slug)
        tts_engine_class = tts.get_engine_by_slug(tts_engine_slug)
        """
        """
        # Initialize Mic
        self.mic = Mic(tts_engine_class.get_instance(),
                       stt_passive_engine_class.get_passive_instance(),
                       stt_engine_class.get_active_instance())
        """
    def hear(self, regex, option, callback):
        #self._listeners.append(Listener(regex, option, callback))
        pass

    def message(self, message):
        if message.argument is not None:
            print(message.argument)
    
    def run(self, event_loop=None):
        # TODO: Loop over all the possible adapters and 
        # instantiate them all
        # second step is to run them all
        loop = asyncio.get_event_loop()
        for adapter in self._adapters:
            asyncio.async(adapter.run())
        try:
            loop.run_forever()
        finally:
            loop.close()

def main():
    logging.basicConfig()
    logger = logging.getLogger()
    logger.getChild("client.stt").setLevel(logging.INFO)

    if args.debug:
        logger.setLevel(logging.DEBUG)

    try:
        app = Bot()
    except Exception:
        logger.error("Error occured!", exc_info=True)
        sys.exit(1)

    app.run()

if __name__ == "__main__":
    main()