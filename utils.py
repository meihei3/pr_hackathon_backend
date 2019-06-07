from enum import Enum, auto

from db import db
from models.ngs import NGs


class Res(Enum):
    ok = auto()
    ng = auto()


def ng_word_filter(text: str, company_id) -> Res:
    cng = db.session.query(NGs).filter_by(company_id=company_id).first()
    if cng is None:
        return Res.ok
    words = cng.to_dict()["ng_words"].split(',')
    for word in words:
        if word in text:
            return Res.ng
    return Res.ok
