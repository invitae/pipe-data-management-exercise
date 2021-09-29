from . import db


class Record(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)

    nfs_path = db.Column(
        db.String(255),
        doc="Absolute path of the nfs directory containing this data",
    )

    def __repr__(self):
        return f"<Data at {self.nfs_path}>"

    @staticmethod
    def get_all():
        return {r.id: str(r) for r in Record.query.all()}
