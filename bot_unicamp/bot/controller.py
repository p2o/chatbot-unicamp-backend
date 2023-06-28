from .service import BotService

from bot_unicamp.common import GenericError
from bot_unicamp.history import History
from transformers import pipeline


class BotController:
    def __init__(
        self,
        bot_service: BotService,
    ):
        self.bot_service = bot_service

    def ask(self, episode: History, nn: pipeline) -> History:
        try:
            history = self.bot_service.ask(episode, nn)
        except Exception as err:
            raise GenericError(err)

        return history
