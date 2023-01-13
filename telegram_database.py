import sqlite3
from config import *

class Database:
    def __init__(self, db_file: str):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()


    async def add_tasks(self, user_id, date, task):
        with self.con:

            for_db = [user_id,task,date]
            return self.cur.executemany("INSERT INTO `telegram_tasks` (`user_id`,`task`,`date`) VALUES (?,?,?)", (for_db, ))
    

    async def get_task(self, user_id: int, date: str):
        tasks = []
        with self.con:

            for i in self.cur.execute("SELECT `task` FROM `telegram_tasks` WHERE (`user_id`, `date`) = (?,?)", (user_id, date)).fetchall():

                tasks.append(i)
                
            return tasks


    async def get_dates(self, user_id):
        dates = []
        with self.con:

            for i in self.cur.execute("SELECT `date` FROM `telegram_tasks` WHERE `user_id` = ?", (user_id, )).fetchall():

                dates.append(i)
            
            return dates
    

    async def delete_tasks(self, user_id,date):
        with self.con:

            return self.cur.execute("DELETE FROM `telegram_tasks` WHERE (`user_id`,`date`) = (?,?)", (user_id, date, ))
