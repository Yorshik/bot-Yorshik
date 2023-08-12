import os
import json
import random
import webbrowser
import math
import numpy
import matplotlib
import time
import string
#     def remove_file(self, path):
#         try:
#             os.remove(path)
#             print('successful')
#         except FileNotFoundError:
#             print('incorrect file name')
#
#     def create_file(self, path):
#         try:
#             with open(path, 'a', encoding='UTF-8') as file:
#                 file.write('created by console bot Yorshik')
#             print('successful')
#         except ValueError:
#             pass


# def passage(file_name, folder):
#     for element in os.scandir(folder):
#         if element.is_file():
#             if element.name == file_name:
#                 yield folder
#         else:
#             yield from passage(file_name, element.path)
#
# print(*passage('system.py', os.getcwd()))
class User:
    def __init__(self):
        self.analog_bot_bandit_registered = False
        self.real_life_registered = False
        self.has_acc = False
        self.big_politic_game_registered = False
        self.data = {}
        self.abbd = {}  # analog bot bandit data
        self.rld = {}  # real life data
        self.bpgd = {}  # big politic game data
        self.nick = ''
        self.status = 'standard'  # standard / admin

    @staticmethod
    def register(login, password, nick, codeword, promos):
        user.data[nick] = {"login": "", "password": "", "code_word": "", "activated_promo": [],
                           "analog_bot_bandit_login": "", "analog_bot_bandit_password": "", "real_life_login": "",
                           "real_life_password": "", "big_politic_game_login": "", "big_politic_game_password": ""}
        user.data[nick]['login'] = login
        user.data[nick]['login'] = password
        user.data[nick]['login'] = codeword if codeword is not None else ''
        for promo in promos:
            if promo in bot.data['bot_data']['promos']:
                user.data[nick]['activated_promo'].append(promo)
            else:
                print('incorrect promo')


class Bot:
    def __init__(self):
        self.data = json.load(open('data.json', encoding='utf-8'))

    def init(self):
        print('Bot Yorshik')
        time.sleep(1)
        print('Created by Noname')
        print('Version Beta')
        time.sleep(1)
        if self.wanna_login():
            self.log_reg()
        self.start_loop()

    @staticmethod
    def wanna_login():
        if input('do you want to login/register? (yes/no) >>> ') == 'yes':
            return True
        return False

    @staticmethod
    def login():
        nick = input('enter your nick >>> ')
        if nick in bot.data['accounts']:
            password = input('enter your password >>> ')
            if bot.data['accounts'][nick]['self_info']['password'] == password:
                user.data = bot.data['accounts'][nick]
                user.nick = nick

    def register(self):
        login = input('create your login (do not leave empty) >>> ')
        if login == '':
            print('login is empty')
            self.register()
        password = input(
            'create your password (minimum eight characters, at least 1 digit and at least 1 letter, also do not leave empty) >>> ')
        digit_flag = False
        letters_flag = False
        for i in password:
            if i in string.ascii_letters:
                letters_flag = True
            elif i in string.digits:
                digit_flag = True
            if letters_flag and digit_flag:
                break
        if len(password) < 8:
            print('password is shorter than eight characters')
            self.register()
        elif not digit_flag:
            print('password doesn`t contain a digit')
            self.register()
        elif not letters_flag:
            print('password doesn`t contain a letter')
            self.register()
        nick = input('create your nick in bot (do not leave empty) >>> ')
        if nick == '':
            print('nick is empty')
            self.register()
        code_word = input('create code word if you want (you can skip it)')
        if code_word == '':
            code_word = None
        promos = input('if you have promos for this bot you can enter them (write them with spaces)').split(' ')
        if promos == ['']:
            promos = []
        user.register(login, password, nick, code_word, promos)
        other_registrations = input(
            'do you want to register in other places such as analog bot bandit game/real life game/big politic game (unavailable) >>> ')
        if other_registrations != '':
            print('to this moment this is unavailable')

    def exit(self):
        print('in this update exit is unavailable\nstay tuned for next updates')

    def weather(self):
        print('in this update weather is unavailable\nstay tuned for next updates')

    def sort(self):
        print('in this update sort is unavailable\nstay tuned for next updates')

    def analyze(self):
        print('in this update text analyze is unavailable\nstay tuned for next updates')

    def search_net(self):
        print('in this update search_net is unavailable\nstay tuned for next updates')

    def search_file(self):
        print('in this update search_file is unavailable\nstay tuned for next updates')

    def shuffle(self):
        print('in this update shuffling is unavailable\nstay tuned for next updates')

    def exchange(self):
        print('in this update see exchange is unavailable\nstay tuned for next updates')

    def file(self):
        print('in this update opening file is unavailable\nstay tuned for next updates')

    def link(self):
        print('in this update opening link is unavailable\nstay tuned for next updates')

    def math_infinity(self):
        print('in this update math_infinity is unavailable\nstay tuned for next updates')

    def tictactoe(self):
        print('in this update tictactoe is unavailable\nstay tuned for next updates')

    def fool(self):
        print('in this update fool is unavailable\nstay tuned for next updates')

    def rps(self):
        print('in this update rps is unavailable\nstay tuned for next updates')

    def uno(self):
        print('in this update uno is unavailable\nstay tuned for next updates')

    def calculator(self):
        print('in this update calculator is unavailable\nstay tuned for next updates')

    def website(self):
        print('in this update website is unavailable\nstay tuned for next updates')

    def telegram(self):
        print('in this update telegram bot is unavailable\nstay tuned for next updates')

    def account(self):
        print('in this update account is unavailable\nstay tuned for next updates')

    def help(self):
        print('in this update help is unavailable\nstay tuned for next updates')

    def localisation(self):
        print('in this update localisation is unavailable\nstay tuned for next updates')

    def graphics(self):
        print('in this update graphics are unavailable\nstay tuned for next updates')

    def python(self):
        print('in this update python is unavailable\nstay tuned for next updates')

    def chronology(self):
        print('in this update chronology is unavailable\nstay tuned for next updates')

    def bandit(self):
        print('in this update bandit is unavailable\nstay tuned for next updates')

    def rl(self):
        print('in this update real life is unavailable\nstay tuned for next updates')

    def politic(self):
        print('in this update politic game is unavailable\nstay tuned for next updates')

    def manchkin(self):
        print('in this update manchkin is unavailable\nstay tuned for next updates')

    def test(self):
        print('in this update test are unavailable\nstay tuned for next updates')

    def achievements(self):
        print('in this update achievements are unavailable\nstay tuned for next updates')

    def editor(self):
        print('in this update editor is unavailable\nstay tuned for next updates')

    def recent_file(self):
        print('in this update recent_files are unavailable\nstay tuned for next updates')

    def poker(self):
        print('in this update texas poker is unavailable\nstay tuned for next updates')

    def admin_init(self):
        print('in this update admin_init is unavailable\nstay tuned for next updates')

    @staticmethod
    def print_info():
        print('Bot Yorshik Abilities:')
        print('*****************************************************************************')
        print('public:')
        print('0: exit (0, exit)')
        print('1: check weather in current city/region (1, weather) !in future updates!')
        print('2: sort something (2, sort) !in future updates!')
        print('3: text analyze (3, analyze) !in future updates!')
        print('4: search on the Internet (4, search_net) !in future updates!')
        print('5: searching file on PC (5, search_file) !in future updates!')
        print('6: shuffling (6, shuffling) !in future updates!')
        print('7: exchange rate (7, exchange) !in future updates!')
        print('8: open file (8, file) !in future updates!')
        print('9: open link (9, link) !in future updates!')
        print('10: game math infinity (10, math_infinity) !in future updates!')
        print('11: game tictactoe (11, tictactoe) !in future updates!')
        print('12: game fool (12, fool) !in future updates!')
        print('13: game rock paper scissors (13, rock/paper/scissors/rps/rock_paper_scissors !in future updates!')
        print('14: game uno (27, uno) !in future updates!')
        print('15: calculator+ (14, calculator) !in future updates!')
        print('16: visit my website (15, website) !in future updates!')
        print('17: open my bot in telegram (16, telegram) !in future updates!')
        print('18: account (17, account) !in future updates!')
        print('19: help (18, help) !in future updates!')
        print('20: localisation (19, localisation)')
        print('21: draw graphics (21, graphics)')
        print('22: standard python console (22, python')
        print('23: chronology of versions (23, chronology)')
        print('*****************************************************************************')
        print('only for registered users')
        print('24: analog bot bandit game (24, bandit) !in future updates!')
        print('25: real life game (25, real/life/rl/real_life !in future updates!')
        print('26: big politic game (26, politic) !in future updates!')
        print('27: manchkin game (27, manchkin) !in future updates!')
        print('28: tests on some themes (28, test) !in future updates!')
        print('29: achievements (29, achievements) !in future updates!')
        print('30: open editor (30, editor) !in future updates!')
        print('31: open recent file (31, recent_file) !in future updates!')
        print('32: game texas poker (32, poker) !in future updates!')
        print('*****************************************************************************')
        print('only for admin (hehe you won`t get it !in future updates!')
        print('33: init admin (33, admin_init)')

    def log_reg(self):
        while True:
            print('with registration you can:\n'
                  'open editor\n'
                  'open recent files\n'
                  'play texas poker, analog bot bandit, real life, manchkin and big politic game (only for registered because it is hard to write them)\n'
                  'test yourself and save results\n'
                  'and reach achievements')
            log_reg = input('login/register or skip? (q for exit) >>> ')
            if log_reg == 'login':
                self.login()
                break
            elif log_reg == 'register':
                self.register()
                break
            elif log_reg == 'skip':
                break
            elif log_reg == 'q':
                print('have a nice day')
                quit()

    def start_loop(self):
        while True:
            self.print_info()
            request = input('>>> ')
            if request in ['0', 'exit']:
                self.exit()
            elif request in ['1', 'weather']:
                self.weather()
            elif request in ['2', 'sort']:
                self.sort()
            elif request in ['3', 'analyze']:
                self.analyze()
            elif request in ['4', 'search_net']:
                self.search_net()
            elif request in ['5', 'search_file']:
                self.search_file()
            elif request in ['6', 'sort']:
                self.shuffle()
            elif request in ['7', 'exchange']:
                self.exchange()
            elif request in ['8', 'file']:
                self.file()
            elif request in ['9', 'link']:
                self.link()
            elif request in ['10', 'math_infinity']:
                self.math_infinity()
            elif request in ['11', 'tictactoe']:
                self.tictactoe()
            elif request in ['12', 'fool']:
                self.fool()
            elif request in ['13', 'rock', 'paper', 'scissors', 'rock_paper_scissors', 'rps']:
                self.rps()
            elif request in ['14', 'uno']:
                self.uno()
            elif request in ['15', 'calculator']:
                self.calculator()
            elif request in ['16', 'website']:
                self.website()
            elif request in ['17', 'telegram']:
                self.telegram()
            elif request in ['18', 'account']:
                self.account()
            elif request in ['19', 'help']:
                self.help()
            elif request in ['20', 'localisation']:
                self.localisation()
            elif request in ['21', 'graphics']:
                self.graphics()
            elif request in ['22', 'python']:
                self.python()
            elif request in ['23', 'chronology']:
                self.chronology()
            elif request in ['24', 'bandit']:
                self.bandit()
            elif request in ['25', 'real', 'life', 'rl', 'real_life']:
                self.rl()
            elif request in ['26', 'politic']:
                self.politic()
            elif request in ['27', 'manchkin']:
                self.manchkin()
            elif request in ['28', 'test']:
                self.test()
            elif request in ['29', 'achievements']:
                self.achievements()
            elif request in ['30', 'editor']:
                self.editor()
            elif request in ['31', 'recent_file']:
                self.recent_file()
            elif request in ['32', 'poker']:
                self.poker()
            elif request in ['33', 'admin_init']:
                self.admin_init()


bot = Bot()
user = User()
bot.init()
