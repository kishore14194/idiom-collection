from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Idiom(Base):
    __tablename__ = "idiom"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    word = Column('word', String, unique=True)
    meaning = Column('meaning', Text)
    example = Column('example', Text)


engine = create_engine('sqlite:////Users/kishore/Documents/idiom_collection/idiom.db')

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

# idiom = Idiom()

# To Add
# idiom.word = "Example"
# idiom.meaning = "Text"
# idiom.example = "Example Example"
# session.add(idiom)
# session.commit()

# To delete
# idiom = session.query(Idiom)
# idiom = idiom.filter_by(id=1).first()
# session.delete(idiom)
# session.commit()

session.close()
