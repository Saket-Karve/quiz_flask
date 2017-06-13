from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
question = Table('question', post_meta,
    Column('question_id', Integer, primary_key=True, nullable=False),
    Column('quiz_id', Integer),
    Column('q_text', String),
    Column('option1', String),
    Column('option2', String),
    Column('option3', String),
    Column('option4', String),
    Column('answer', String),
    Column('category', String),
)

response = Table('response', post_meta,
    Column('response_id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('quiz_id', Integer),
    Column('question_id', Integer),
    Column('response', String),
    Column('result', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['question'].columns['q_text'].create()
    post_meta.tables['response'].columns['response'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['question'].columns['q_text'].drop()
    post_meta.tables['response'].columns['response'].drop()
