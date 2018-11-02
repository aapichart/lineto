""" This is the module for keeping database definition """
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.schema import CreateTable
from sqlalchemy.ext.declarative import declarative_base


""" Initialize Database """
engine = create_engine(
            'sqlite:///lineto/dbcore.db',
            echo=False
        )
Base = declarative_base()
# This is the password for Delete or Create DB 
AllowedPassword = "adminessoft"

class User_Table(Base):
    """ This is User_Table schema """

    __tablename__ = "lineuser"

    userid = Column(String(20), unique=True, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    usertoken = Column(String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"({self.userid}, {self.username},"\
            f"{self.usertoken})"

    def __init__(self, name):
        self.name = name


class Post_Log(Base):
    """ Use for collecting response message """

    __tablename__ = "postlog"

    logid = Column(String(20), unique=True,  primary_key=True)
    logcategory = Column(String(10), nullable=False)
    logmsg = Column(String(200), nullable=False)

    def __repr__(self):
        return f"({self.logid}, {self.logcategory}, "\
            f"{self.logmsg})"

    def __init__(self, name):
        self.name = name


def create_db():
    """ Create database schema """
    # If we create only one table, use the command below
    # User_Table.__table__.create(engine)
    passwordstr = input("Please input password:  ")
    if passwordstr == AllowedPassword:
        Base.metadata.create_all(engine)
        return print("Creating DataBase is success")
    else:
        return print("You put the wrong password")


def drop_db():
    """ Drop database schema """
    # If we restruct database, we need to drop it first
    passwordstr = input("Please input password:  ")
    if passwordstr == AllowedPassword:
        Base.metadata.drop_all(engine)
        return print("Drop DataBase is success")
    else:
        return print("You put the wrong password")


def CheckTblNameExist(tblname):
    """ Use for check whether tblname is exist or not"""
    if not engine.dialect.has_table(engine, tblname):
        return False
    else:
        return True


def QueryAllUsers():
    """ Use this fuction to query all users'tokens """
    conn = engine.connect()
    outmsg = ""
    if CheckTblNameExist("lineuser"):
        result_db = conn.execute("select * from lineuser")
        for row in result_db:
            outstring = f" [(userid: {row.userid}),"\
                    f" (username: {row.username}),"\
                    f" (usertoken: {row.usertoken})]"
            if outmsg == "":
                outmsg = outstring
            else:
                outmsg = outmsg + ",\n" + outstring
        conn.close()
        return outmsg
    else:
        conn.close()
        return "Table Not Exist"


def findLastUserID():
    """ Use for find the max userid field """
    conn = engine.connect()
    if CheckTblNameExist("lineuser"):
        result_db = conn.execute("select * from lineuser order by userid desc")
        row = result_db.fetchone()
        if row is None:
            conn.close()
            return 0
        else:
            conn.close()
            return int(row.userid)
    else:
        conn.close()
        return -1


def InsertUser(inputuser, inputtoken):
    """ Use for insert any user which will get line msg """
    lastuserid = findLastUserID()
    insertstm = f"insert into lineuser"\
            f"(userid, username, usertoken) "\
            f"values('{lastuserid+1}',"\
            f"'{inputuser}',"\
            f"'{inputtoken}')"
    conn = engine.connect()
    if CheckTblNameExist("lineuser"):
        try:
            conn.execute(insertstm)
            conn.close()
            return f"Execute Success: Insert - {inputuser}" 
        except:
            conn.close()
            return "Execute Errors"
    else:
        conn.close()
        return "Table Not Exist"


def InsertLog():
    """ Use this to keep log """
