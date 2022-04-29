import sqlite3
import os
from datetime import datetime
import socket


class DbLogger:

    def __init__(self):
        if os.path.exists("my_logger.db"):
            os.remove("my_logger.db")
        self.con = sqlite3.connect("my_logger.db")
        self.curs = self.con.cursor()
        self.curs.execute(
            '''CREATE TABLE game (game_id integer primary key autoincrement, time timestamp, ip text, wordle text)''')
        self.curs.execute(
            '''CREATE TABLE details (game_id integer primary key autoincrement, time timestamp, attempt integer, input text, wordle text)''')
        self.curs.execute(
            '''CREATE TABLE statistics (game_id integer primary key autoincrement, time timestamp, win_status text, number_of_attempt integer)''')
        self.ip = self.get_ip()

    def get_ip(self):
        # function refered from : https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def insert_to_game(self, wordle):
        time = datetime.now()
        self.curs.execute(
            "insert into game values (null, ?, ?, ?)", (time, self.ip, wordle))
        self.con.commit()

    def insert_to_details(self, attempt, input_word, wordle):
        time = datetime.now()
        self.curs.execute(
            "insert into details values (null, ?, ?, ?, ?)", (time, attempt, input_word, wordle))
        self.con.commit()

    def insert_to_statistics(self, win_status, number_of_games):
        time = datetime.now()
        self.curs.execute(
            "insert into statistics values (null, ?, ?, ?)", (time, win_status, number_of_games))
        self.con.commit()

    def close(self):
        print("Records made in database")
        self.con.close()

    def report_analysis(self, startdate, enddate):
        if not os.path.exists("report_analysis.txt"):
            f = open('report_analysis.txt', 'a+')
        self.curs.execute(
            "SELECT * FROM 'game' where time>= :startdate and time<= :enddate", {"startdate": startdate, "enddate": enddate})
        print_vals = self.curs.fetchall()
        with open('report_analysis.txt', 'w') as f:
            f.write(str(print_vals))
        print(
            f"\nReport made for date range entered from {startdate} to {enddate} \n")
