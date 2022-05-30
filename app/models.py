from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Navarea(db.Model):
    """
    База данных Navarea областей. Всего их 21 штука. Изменениям подвергаться
    будут только ссылки на сайты для парсинга. Можно будет использовать
    эту базу для отображения на сайта с быстрым доступом к нужной Navarea
    """
    id = db.Column(db.Integer, primary_key=True)
    nav_area = db.Column(db.String(64), index=True)
    url = db.Column(db.String(128))

    def __repr__(self):
        return '{} : {}'.format(self.id, self.area_name)

class NavareaArea(db.Model):
    """
    База данных для морей и областей в Navarea. Не должна меняться.
    """
    id = db.Column(db.Integer, primary_key=True)
    nav_area_id = db.Column(db.Integer, db.ForeignKey('navarea.id'))
    nav_area = db.Column(db.String, db.ForeignKey('navarea.nav_area'))
    area = db.Column(db.String(128))
    # parent = db.relationship("Navarea", back_populates="NavareaArea")

class NavareaMessage(db.Model):
    """
    База данных сообщений.
    """
    id = db.Column(db.Integer, prinmary_key=True)
    date = db.Column(db.Date(), nullabe=False)
    nav_area = db.Column(db.String, db.ForeignKey('navarea.nav_area'))
    area = db.Column(db.String, db.ForeignKey('navareaarea.area'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
