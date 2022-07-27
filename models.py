from calendar import MONDAY, SATURDAY, SUNDAY
from re import T
import sched
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





##### Init class #####
db = SQLAlchemy()

##models###
class Schedual(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    saturday = db.Column(db.String(80), nullable=True)
    sunday = db.Column(db.String(80), nullable=True)
    monday = db.Column(db.String(80), nullable=True)
    tuesday = db.Column(db.String(80), nullable=True)
    wednesday = db.Column(db.String(80), nullable=True)
    thursday = db.Column(db.String(80), nullable=True)
    friday = db.Column(db.String(80), nullable=True)
    doctor_username = db.Column(db.Integer, db.ForeignKey('doctor.username'), nullable=False)

    def __init__(self,saturday,sunday, monday, tuesday,wednesday,thursday ,friday ,doctor_username  ):
        self.saturday=saturday
        self.sunday = sunday
        self.monday = monday
        self.tuesday =tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.doctor_username = doctor_username
    def __repr__(self):
        return f"<Doctor({self.doctor}, {self.stusername[:20]}...)> "

    @classmethod
    def insert(self,saturday,sunday, monday, tuesday,wednesday,thursday ,friday ,doctor_username ):

        sessions = Schedual(saturday = saturday ,sunday=sunday , monday = monday , tuesday=tuesday , wednesday = wednesday , thursday = thursday , friday=friday , doctor_username =doctor_username)

        # add to db and commit
        db.session.add(sessions)
        db.session.commit()
    @classmethod
    def get(self, id):

        query = self.query.get(id)

        return query



        return stsssusername
    @classmethod
    def update_saturday(self, id, saturday):
        query = self.query.get(id)

        # update values in query
        query.saturday = saturday
        # commit the updates
        db.session.commit()
    @classmethod
    def getid(self, doctor_username):
        query = self.query.filter_by(doctor_username=doctor_username).first()
        email = query.id

        return email

    @classmethod
    def update_saturday(self, id, username):
        query = self.query.get(id)

        # update values in query
        query.username = username
        # commit the updates
        db.session.commit()





class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ismadmin = db.Column(db.Boolean, nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    certificates = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    stsusername = db.relationship('Student', backref='author', lazy=True)
    schedual = db.relationship('Schedual', backref='author', lazy=True)
    st_adv = db.relationship('Advising', backref='author', lazy=True)
    profile_pic = db.Column(db.String(), nullable=True)


    def __init__(self,ismadmin,isadmin, name, username,email,password ,certificates ,profile_pic  ):
        self.ismadmin = ismadmin 
        self.isadmin = isadmin
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.certificates = certificates
        self.profile_pic = profile_pic
        

    def __repr__(self):
        return f"<Doctor({self.id}, #{self.name}, {self.username}> "


    @classmethod
    def update(self, id, name, username, password):
        query = self.query.filter_by(id=id).first()
        query.name = name
        query.username = username
        query.password = password
        # commit changes to db
        db.session.commit()
    @classmethod
    def getUser(self, id):
        query = self.query.filter_by(id=id).first()
        return query

    @classmethod
    def update_dr_name(self, id, name):
        query = self.query.get(id)

        # update values in query
        query.name = name
        # commit the updates
        db.session.commit()

    @classmethod
    def update_dr_username(self, id, username):
        query = self.query.get(id)

        # update values in query
        query.username = username
        # commit the updates
        db.session.commit()
        
    @classmethod
    def update_dr_password(self, id, password):
        query = self.query.get(id)

        # update values in query
        query.password = password
        # commit the updates
        db.session.commit()
    @classmethod
    def update_dr_certificates(self, id, certificates):
        query = self.query.get(id)

        # update values in query
        query.certificates = certificates
        # commit the updates
        db.session.commit()

    @classmethod
    def getByUsername(self, username):
        query = self.query.filter_by(username=username).first()
        return query

    @classmethod
    def getByemail(self, name):
        query = self.query.filter_by(name=name).first()
        email = query.email

        return email

        
    @classmethod
    def get(self, id):

        query = self.query.get(id)

        return query

    @classmethod
    def getschedual(self, name):
        query = self.query.filter_by(name=name).first()
        schedual = query.schedual

        return schedual
    @classmethod
    def getDOCTORSTUDENT(self, username):
        query = self.query.filter_by(username=username).first()
        stsssusername = query.stsusername

        return stsssusername

    @classmethod
    def get_schedual(self, username):
        query = self.query.filter_by(username=username).first()
        chedual = query.schedual
        return chedual


    @classmethod
    def getDOCTORid(self, username):
        query = self.query.filter_by(username=username).first()
        id = query.id

        return id


    @classmethod
    def get_stu_advs(self, username):
        query = self.query.filter_by(username=username).first()
        st_adv = query.st_adv

        return st_adv


    @classmethod
    def get_email(self, username):
        query = self.query.filter_by(username=username).first()
        email = query.email

        return email

    @classmethod
    def getname(self, username):
        query = self.query.filter_by(username=username).first()
        name = query.name

        return name

    @classmethod
    def get_dr_password(self, username):
        query = self.query.filter_by(username=username).first()
        password = query.password

        return password

    @classmethod
    def get_dr_certificates(self, username):
        query = self.query.filter_by(username=username).first()
        certificates = query.certificates

        return certificates

    @classmethod
    def get_id_bymail(self, email):
        query = self.query.filter_by(email=email).first()
        dr_id = query.id

        return dr_id

    @classmethod
    def get_name_bymail(self, email):
        query = self.query.filter_by(email=email).first()
        dr_name = query.name

        return dr_name


    @classmethod
    def get_usrname_bymail(self, email):
        query = self.query.filter_by(email=email).first()
        dr_name = query.stsusername

        return dr_name

    @classmethod
    def get_cetificates_bymail(self, email):
        query = self.query.filter_by(email=email).first()
        certificates = query.certificates

        return certificates

    @classmethod
    def get_prifile_pic_bymail(self, email):
        query = self.query.filter_by(email=email).first()
        profile_pic = query.profile_pic

        return profile_pic



    @classmethod
    def getUserId(self, username):
        '''
        get id associated with the given username
        '''
        email = self.query.filter_by(username=username).first().email
        return email

    @classmethod
    def get_message_by_id(self, id):
        '''
        get id associated with the given username
        '''
        email = self.query.filter_by(id=id).first().email
        return email



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    stusername = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(80),unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    doctor_email = db.Column(db.Integer, db.ForeignKey('doctor.email'), nullable=False)
    advise = db.relationship('Advising', backref='authorr', lazy=True)


    def __init__(self, stusername,name,password, doctor_email  ):
        self.stusername = stusername
        self.name = name
        self.password = password
        self.doctor_email = doctor_email
        

    def __repr__(self):
        return f"<Doctor({self.doctor}, {self.stusername[:20]}...)> "


    @classmethod
    def getUsermial(self, id):
        mail = self.query.filter_by(id=id).first().doctor_email
        return mail

    @classmethod
    def insert(self, stusername,name,password,doctor_email):

        stusername = Student(stusername=stusername,name = name,password = password,doctor_email=doctor_email)

        # add to db and commit
        db.session.add(stusername)
        db.session.commit()

    @classmethod
    def get_adv_by_id(self, id):
        query = self.query.filter_by(id=id).first()
        adv = query.isadmin

        return adv

    @classmethod
    def get_adv_by_iid(self, id):
        query = self.query.filter_by(id=id).first()
        adv = query.doctor_email

        return adv
    @classmethod
    def get_nam_by_iid(self, id):
        query = self.query.filter_by(id=id).first()
        adv = query.stusername

        return adv
    @classmethod
    def update(self, id, stusername):
        
        query = self.query.get(id)

        # update values in query
        query.stusername = stusername
 
        query.date_created = datetime.utcnow()

        # commit the updates
        db.session.commit()

    @classmethod
    def update_name(self, id, name):
        
        query = self.query.get(id)

        # update values in query
        query.name = name
 
        # commit the updates
        db.session.commit()



    @classmethod
    def delete(self, id):

        query = self.query.get(id)
        db.session.delete(query)
        db.session.commit()

    @classmethod
    def get(self, id):

        query = self.query.get(id)

        return query

    @classmethod
    def getByname(self, name):
        query = self.query.filter_by(name=name).first()
        return query
    
    @classmethod
    def getByUsername(self, username):
        query = self.query.filter_by(username=username).first()
        return query

    @classmethod
    def getUserId(self, name):
        '''
        get id associated with the given username
        '''
        id = self.query.filter_by(name=name).first().id
        return id

    @classmethod
    def getUsersessions(self, id):

        query = self.query.filter_by(id=id).first()
        sessionSS = query.advise

        return sessionSS  
    @classmethod
    def getUser_id_bymail(self, doctor_email):

        query = self.query.filter_by(doctor_email=doctor_email).first()
        stu_id = query.id

        return stu_id

        
        

    @classmethod
    def getUsersessionsid(self, stusername):

        query = self.query.filter_by(stusername=stusername).first()
        id = query.id

        return id
    @classmethod
    def getUsersessions_sts(self, stusername):

        query = self.query.filter_by(stusername=stusername).first()
        sessionSSq = query.advise

        return sessionSSq


class Advising(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=True)
    message = db.Column(db.String(100), unique=False, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    readed=db.Column(db.String(100), unique=False, nullable=True)
    replay=db.Column(db.String(100), unique=False, nullable=True)

    def __init__(self, name,message, user_id , doctor_id , readed ,replay ):
        self.name = name
        self.message = message
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.readed = readed
        self.replay = replay

    def __repr__(self):
        return f"<Student({self.student}> "
    def __repr__(self):
        return f"<doctor({self.doctor}> "


    @classmethod
    def update(self, id, readed):
        query = self.query.get(id)

        # update values in query
        query.readed = readed
        # commit the updates
        db.session.commit()

    @classmethod
    def updatereplay(self, id, replay):
        query = self.query.get(id)

        # update values in query
        query.replay = replay
        # commit the updates
        db.session.commit()


    @classmethod
    def get(self, id):

        query = self.query.get(id)

        return query

    @classmethod
    def delete(self, id):

        query = self.query.get(id)
        db.session.delete(query)
        db.session.commit()

    @classmethod
    def insert(self,name,message , user_id , doctor_id , readed , replay):

        sessions = Advising(name = name ,message=message , user_id = user_id , doctor_id=doctor_id , readed = readed , replay = replay)

        # add to db and commit
        db.session.add(sessions)
        db.session.commit()

  
    

