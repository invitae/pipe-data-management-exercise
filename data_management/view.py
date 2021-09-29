import uuid

from flask import Blueprint, request

from . import db
from .model import Record

data_api = Blueprint("data_api", __name__, url_prefix="/api/v1")


@data_api.route("/health", methods=("GET",))
def health():
    try:
        db.engine.execute("SELECT 1")
        return "DB is up running \U0001F389."
    except Exception as e:
        return f"DB failure: {str(e)}"


@data_api.route("/list", methods=("GET",))
def list():
    return Record.get_all()


@data_api.route("/register", methods=("GET",))
def register():
    nfs_path = request.args.get("nfs_path")
    if not nfs_path:
        return
    new_record = Record(nfs_path=nfs_path)
    db.session.add(new_record)  # Adds new User record to database
    db.session.commit()
    return {
        "message": "registered one record successfully",
        "result": str(new_record),
    }
