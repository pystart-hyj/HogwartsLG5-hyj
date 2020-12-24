from typing import List
import logging

class Hero:
    hp=100
    power=10
    magic_hg=200
    speed=1
    tools = []

    def fight(self, hero: ['Hero']):
        while True:
            hero.hp -= self.power
            if self.winner(self, hero):
                return True
            self.hp -= hero.power
            if self.winner(hero, self):
                return False

        def winner(self, hero1, hero2):
            print(f'{hero1} VS {hero2}')
            if hero1.hp <= 0:
                return False
            if hero2.hp <= 0:
                return True

        def test_logging():
            logging.debug('Debugging information')
            logging.info('Informational message')
            logging.warning('Warning:config file %s not found', 'server.conf')
            logging.error('Error occurred')
            logging.critical('Critical error -- shutting down')

    def fight_many(self, heros: List['Hero']):
        pass



