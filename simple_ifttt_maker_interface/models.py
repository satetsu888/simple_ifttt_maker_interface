from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MenuModel(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    action = Column(Text)
    value1 = Column(Text)
    value2 = Column(Text)
    value3 = Column(Text)

    def toDict(self):
        return {
            "id": self.id,
            "action": self.action,
            "value1": self.value1,
            "value2": self.value2,
            "value3": self.value3,
        };
