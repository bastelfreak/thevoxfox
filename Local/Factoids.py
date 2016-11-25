import logging
from Legobot.Lego import Lego

logger = logging.getLogger(__name__)

class Factoids(Lego):
    def listening_for(self, message):
        cmds = ['!shrug', '!tableflip', '!nope', '!doit', '!wat']
        return message['text'].split()[0] in cmds

    def handle(self, message):
        opts = None
        logger.info(message)
        try:
            target = message['metadata']['source_channel']
            opts = {'target':target}
        except IndexError:
            logger.error('Could not identify message source in message: %s' % str(message))
        command = message['text'].split()[0]
        if command == '!shrug':
            txt = '¯\_(ツ)_/¯'
        elif command == '!tableflip':
            txt = '(╯°O°）╯︵ ┻━┻'
        elif command == '!nope':
            txt = 'http://i3.kym-cdn.com/photos/images/original/000/727/925/2b5.gif'
        elif command == '!doit':
            txt = 'Dooooooooo eeeeeeeettttttttt'
        elif command == '!wat':
            txt = 'https://p.bastelfreak.de/1gxL/'
        self.reply(message, txt, opts)


    def get_name(self):
        return 'factoids'

    def get_help(self):
        help_text = "collection of nice factoids (static reponses). " \
                "Usage: !shrug, !tableflip, !nope, !doit, !wat "
        return help_text