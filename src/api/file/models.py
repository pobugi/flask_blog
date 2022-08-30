from datetime import datetime

from src import db


class File(db.Model):
    __tablename__ = "file"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    extension = db.Column(db.String)
    owner_id = db.Column(db.Integer, nullable=False)
    path = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def create(title, extension, owner_id, path):
        file = File(
            title=title,
            extension=extension,
            owner_id=owner_id,
            path=path,
            created=datetime.now(),
            updated=datetime.now(),
        )
        db.session.add(file)
        db.session.commit()
        return file

    @staticmethod
    def get_all():
        return File.query.all()

    @staticmethod
    def to_dict(obj):
        if not obj:
            return None
        return {
            "id": obj.id,
            "title": obj.title,
            "extension": obj.extension,
            "owner_id": obj.owner_id,
            "path": obj.path,
            "created": obj.created,
            "updated": obj.updated,
        }

    @staticmethod
    def to_dict_multi(objects):
        if not objects:
            return []
        return [File.to_dict(obj) for obj in objects]
