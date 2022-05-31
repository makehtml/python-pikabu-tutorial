from app.extensions import db


class Area(db.Model):
    """
    Таблица NavArea областей. Всего их 21 штука. Изменениям подвергаться
    будут только ссылки на сайты для парсинга. Можно будет использовать
    эту базу для отображения на сайта с быстрым доступом к нужной Navarea
    """
    id = db.Column(db.Integer, primary_key=True)
    nav_area = db.Column(db.String(64), index=True)
    url2 = db.Column(db.String(1024))

    def __repr__(self):
        return f'{self.id}: {self.area_name}'


class Sea(db.Model):
    """
    Таблица для морей и областей в Navarea. Не должна меняться.
    """
    id = db.Column(db.Integer, primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    title = db.Column(db.String(128))


class Message(db.Model):
    """
    Таблица сообщений.
    """
    id = db.Column(db.Integer, primary_key=True)
    sea_id = db.Column(db.Integer, db.ForeignKey('sea.id'))
    date = db.Column(db.Date())
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
