# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Date, Float, ForeignKey, Integer, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AllEvents2016(Base):
    __tablename__ = 'all_events2016'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2016')
    response_fio2016 = relationship('ResponseFio2016', secondary='Business.events_response_fio2016')
    content_events2016 = relationship('ContentEvents2016', secondary='Business.events_grbs2016')


class Subprogram2016(AllEvents2016):
    __tablename__ = 'subprogram2016'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2016.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2016(AllEvents2016):
    __tablename__ = 'main_event2016'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2016.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2016.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2016 = relationship('Subprogram2016')


class Event2016(AllEvents2016):
    __tablename__ = 'event2016'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2016.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2016.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2016 = relationship('MainEvent2016')


class AllEvents2017(Base):
    __tablename__ = 'all_events2017'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2017')
    response_fio2017 = relationship('ResponseFio2017', secondary='Business.events_response_fio2017')
    content_events2017 = relationship('ContentEvents2017', secondary='Business.events_grbs2017')


class Subprogram2017(AllEvents2017):
    __tablename__ = 'subprogram2017'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2017.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2017(AllEvents2017):
    __tablename__ = 'main_event2017'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2017.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2017.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2017 = relationship('Subprogram2017')


class Event2017(AllEvents2017):
    __tablename__ = 'event2017'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2017.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2017.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2017 = relationship('MainEvent2017')


class AllEvents2018(Base):
    __tablename__ = 'all_events2018'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2018')
    response_fio2018 = relationship('ResponseFio2018', secondary='Business.events_response_fio2018')
    content_events2018 = relationship('ContentEvents2018', secondary='Business.events_grbs2018')


class Subprogram2018(AllEvents2018):
    __tablename__ = 'subprogram2018'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2018.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2018(AllEvents2018):
    __tablename__ = 'main_event2018'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2018.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2018.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2018 = relationship('Subprogram2018')


class Event2018(AllEvents2018):
    __tablename__ = 'event2018'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2018.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2018.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2018 = relationship('MainEvent2018')


class AllEvents2019(Base):
    __tablename__ = 'all_events2019'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2019')
    response_fio2019 = relationship('ResponseFio2019', secondary='Business.events_response_fio2019')
    content_events2019 = relationship('ContentEvents2019', secondary='Business.events_grbs2019')


class Subprogram2019(AllEvents2019):
    __tablename__ = 'subprogram2019'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2019.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2019(AllEvents2019):
    __tablename__ = 'main_event2019'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2019.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2019.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2019 = relationship('Subprogram2019')


class Event2019(AllEvents2019):
    __tablename__ = 'event2019'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2019.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2019.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2019 = relationship('MainEvent2019')


class AllEvents2020(Base):
    __tablename__ = 'all_events2020'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2020')
    response_fio2020 = relationship('ResponseFio2020', secondary='Business.events_response_fio2020')
    content_events2020 = relationship('ContentEvents2020', secondary='Business.events_grbs2020')


class Subprogram2020(AllEvents2020):
    __tablename__ = 'subprogram2020'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2020.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2020(AllEvents2020):
    __tablename__ = 'main_event2020'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2020.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2020.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2020 = relationship('Subprogram2020')


class Event2020(AllEvents2020):
    __tablename__ = 'event2020'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2020.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2020.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2020 = relationship('MainEvent2020')


class AllEvents2021(Base):
    __tablename__ = 'all_events2021'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj', secondary='Business.events_response_obj2021')
    response_fio2021 = relationship('ResponseFio2021', secondary='Business.events_response_fio2021')
    content_events2021 = relationship('ContentEvents2021', secondary='Business.events_grbs2021')


class Subprogram2021(AllEvents2021):
    __tablename__ = 'subprogram2021'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2021.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2021(AllEvents2021):
    __tablename__ = 'main_event2021'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2021.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2021.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2021 = relationship('Subprogram2021')


class Event2021(AllEvents2021):
    __tablename__ = 'event2021'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2021.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2021.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2021 = relationship('MainEvent2021')


class AllEvents2022(Base):
    __tablename__ = 'all_events2022'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    events = Column(Text, nullable=False)

    content_events2022 = relationship('ContentEvents2022', secondary='Business.events_grbs2022')


class Subprogram2022(AllEvents2022):
    __tablename__ = 'subprogram2022'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2022.code'), primary_key=True)
    id_prog = Column(ForeignKey('gosprogram.id'), nullable=False)
    title_subprog = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class MainEvent2022(AllEvents2022):
    __tablename__ = 'main_event2022'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2022.code'), primary_key=True)
    code_subprog = Column(ForeignKey('Business.subprogram2022.code'), nullable=False)
    main_event = Column(Text, nullable=False)

    subprogram2022 = relationship('Subprogram2022')


class Event2022(AllEvents2022):
    __tablename__ = 'event2022'
    __table_args__ = {'schema': 'Business'}

    code = Column(ForeignKey('Business.all_events2022.code'), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2022.code'), nullable=False)
    event = Column(Text, nullable=False)

    main_event2022 = relationship('MainEvent2022')


class ContentEvents2016(Base):
    __tablename__ = 'content_events2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2016_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2017(Base):
    __tablename__ = 'content_events2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2017_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2018(Base):
    __tablename__ = 'content_events2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2018_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2019(Base):
    __tablename__ = 'content_events2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2019_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2020(Base):
    __tablename__ = 'content_events2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2020_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2021(Base):
    __tablename__ = 'content_events2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2021_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class ContentEvents2022(Base):
    __tablename__ = 'content_events2022'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".content_events2022_id_seq'::regclass)"))
    content = Column(Text, nullable=False)


class Fpsr2016(Base):
    __tablename__ = 'fpsr2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2016_id_seq'::regclass)"))
    fpsr = Column(String(60))


class Fpsr2017(Base):
    __tablename__ = 'fpsr2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2017_id_seq'::regclass)"))
    fpsr = Column(String(60))


class Fpsr2018(Base):
    __tablename__ = 'fpsr2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2018_id_seq'::regclass)"))
    fpsr = Column(String(60))


class Fpsr2019(Base):
    __tablename__ = 'fpsr2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2019_id_seq'::regclass)"))
    fpsr = Column(String(60))


class Fpsr2020(Base):
    __tablename__ = 'fpsr2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2020_id_seq'::regclass)"))
    fpsr = Column(String(60))


class Fpsr2021(Base):
    __tablename__ = 'fpsr2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".fpsr2021_id_seq'::regclass)"))
    fpsr = Column(String(60))


class NamesIndicators2016(Base):
    __tablename__ = 'names_indicators2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2016_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class NamesIndicators2017(Base):
    __tablename__ = 'names_indicators2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2017_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class NamesIndicators2018(Base):
    __tablename__ = 'names_indicators2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2018_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class NamesIndicators2019(Base):
    __tablename__ = 'names_indicators2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2019_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class NamesIndicators2020(Base):
    __tablename__ = 'names_indicators2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2020_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class NamesIndicators2021(Base):
    __tablename__ = 'names_indicators2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".names_indicators2021_id_seq'::regclass)"))
    title_indication = Column(Text, nullable=False)
    type = Column(CHAR(1))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, server_default=text("nextval('categories_id_seq'::regclass)"))
    category = Column(Text, nullable=False)
    unit_of_measurement = Column(String(60))


class Done(Base):
    __tablename__ = 'done'

    id = Column(Integer, primary_key=True)
    done_or_not = Column(CHAR(1), nullable=False)


class FinancingSource(Base):
    __tablename__ = 'financing_source'

    id = Column(Integer, primary_key=True)
    source = Column(Text, nullable=False)


class Gosprogram(Base):
    __tablename__ = 'gosprogram'

    id = Column(String(60), primary_key=True)
    title_prog = Column(Text, nullable=False)


class Kbk2016(Base):
    __tablename__ = 'kbk2016'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2016_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2017(Base):
    __tablename__ = 'kbk2017'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2017_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2018(Base):
    __tablename__ = 'kbk2018'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2018_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2019(Base):
    __tablename__ = 'kbk2019'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2019_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2020(Base):
    __tablename__ = 'kbk2020'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2020_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2021(Base):
    __tablename__ = 'kbk2021'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2021_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2022(Base):
    __tablename__ = 'kbk2022'

    id = Column(Integer, primary_key=True, server_default=text("nextval('kbk2022_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class PlanFact(Base):
    __tablename__ = 'plan_fact'

    id = Column(Integer, primary_key=True)
    plan_fact = Column(CHAR(1), nullable=False)


class ResponseObj(Base):
    __tablename__ = 'response_obj'

    id = Column(Integer, primary_key=True)
    response_obj = Column(Text, nullable=False)


class TitlesItem(Base):
    __tablename__ = 'titles_items'

    id = Column(Integer, primary_key=True, server_default=text("nextval('titles_items_id_seq'::regclass)"))
    expense_item = Column(Text, nullable=False)


class Violation(Base):
    __tablename__ = 'violation'

    id = Column(Integer, primary_key=True)
    violation_or_not = Column(CHAR(1), nullable=False)


t_events_grbs2016 = Table(
    'events_grbs2016', metadata,
    Column('code', ForeignKey('Business.all_events2016.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2016.id')),
    schema='Business'
)


t_events_grbs2017 = Table(
    'events_grbs2017', metadata,
    Column('code', ForeignKey('Business.all_events2017.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2017.id')),
    schema='Business'
)


t_events_grbs2018 = Table(
    'events_grbs2018', metadata,
    Column('code', ForeignKey('Business.all_events2018.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2018.id')),
    schema='Business'
)


t_events_grbs2019 = Table(
    'events_grbs2019', metadata,
    Column('code', ForeignKey('Business.all_events2019.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2019.id')),
    schema='Business'
)


t_events_grbs2020 = Table(
    'events_grbs2020', metadata,
    Column('code', ForeignKey('Business.all_events2020.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2020.id')),
    schema='Business'
)


t_events_grbs2021 = Table(
    'events_grbs2021', metadata,
    Column('code', ForeignKey('Business.all_events2021.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2021.id')),
    schema='Business'
)


t_events_grbs2022 = Table(
    'events_grbs2022', metadata,
    Column('code', ForeignKey('Business.all_events2022.code'), primary_key=True),
    Column('id_content', ForeignKey('Business.content_events2022.id')),
    schema='Business'
)


t_events_response_obj2016 = Table(
    'events_response_obj2016', metadata,
    Column('code_events', ForeignKey('Business.all_events2016.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_obj2017 = Table(
    'events_response_obj2017', metadata,
    Column('code_events', ForeignKey('Business.all_events2017.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_obj2018 = Table(
    'events_response_obj2018', metadata,
    Column('code_events', ForeignKey('Business.all_events2018.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_obj2019 = Table(
    'events_response_obj2019', metadata,
    Column('code_events', ForeignKey('Business.all_events2019.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_obj2020 = Table(
    'events_response_obj2020', metadata,
    Column('code_events', ForeignKey('Business.all_events2020.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_obj2021 = Table(
    'events_response_obj2021', metadata,
    Column('code_events', ForeignKey('Business.all_events2021.code'), primary_key=True, nullable=False),
    Column('id_response_obj', ForeignKey('response_obj.id'), primary_key=True, nullable=False),
    schema='Business'
)


class ExpensesItems2016(Base):
    __tablename__ = 'expenses_items2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2016.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2016 = relationship('AllEvents2016')
    item = relationship('TitlesItem')


class ExpensesItems2017(Base):
    __tablename__ = 'expenses_items2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2017.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2017 = relationship('AllEvents2017')
    item = relationship('TitlesItem')


class ExpensesItems2018(Base):
    __tablename__ = 'expenses_items2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2018.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2018 = relationship('AllEvents2018')
    item = relationship('TitlesItem')


class ExpensesItems2019(Base):
    __tablename__ = 'expenses_items2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2019.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2019 = relationship('AllEvents2019')
    item = relationship('TitlesItem')


class ExpensesItems2020(Base):
    __tablename__ = 'expenses_items2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2020.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2020 = relationship('AllEvents2020')
    item = relationship('TitlesItem')


class ExpensesItems2021(Base):
    __tablename__ = 'expenses_items2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2021.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2021 = relationship('AllEvents2021')
    item = relationship('TitlesItem')


class ExpensesItems2022(Base):
    __tablename__ = 'expenses_items2022'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True)
    code_events = Column(ForeignKey('Business.all_events2022.code'))
    item_id = Column(ForeignKey('titles_items.id'))
    category_id = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    category = relationship('Category')
    all_events2022 = relationship('AllEvents2022')
    item = relationship('TitlesItem')


class Indicators2016(Base):
    __tablename__ = 'indicators2016'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2016_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2016.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2016.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2016.id'))
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2016 = relationship('AllEvents2016')
    fpsr = relationship('Fpsr2016')
    indication = relationship('NamesIndicators2016')


class Rejection2016(Indicators2016):
    __tablename__ = 'rejection2016'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2016.id'), primary_key=True)
    rejection = Column(Text)


class Indicators2017(Base):
    __tablename__ = 'indicators2017'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2017_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2017.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2017.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2017.id'))
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2017 = relationship('AllEvents2017')
    fpsr = relationship('Fpsr2017')
    indication = relationship('NamesIndicators2017')


class Rejection2017(Indicators2017):
    __tablename__ = 'rejection2017'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2017.id'), primary_key=True)
    rejection = Column(Text)


class Indicators2018(Base):
    __tablename__ = 'indicators2018'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2018_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2018.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2018.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2018.id'))
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2018 = relationship('AllEvents2018')
    fpsr = relationship('Fpsr2018')
    indication = relationship('NamesIndicators2018')


class Rejection2018(Indicators2018):
    __tablename__ = 'rejection2018'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2018.id'), primary_key=True)
    rejection = Column(Text)


class Indicators2019(Base):
    __tablename__ = 'indicators2019'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2019_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2019.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2019.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2019.id'))
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2019 = relationship('AllEvents2019')
    fpsr = relationship('Fpsr2019')
    indication = relationship('NamesIndicators2019')


class Rejection2019(Indicators2019):
    __tablename__ = 'rejection2019'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2019.id'), primary_key=True)
    rejection = Column(Text)


class Indicators2020(Base):
    __tablename__ = 'indicators2020'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2020_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2020.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2020.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2020.id'))
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2020 = relationship('AllEvents2020')
    fpsr = relationship('Fpsr2020')
    indication = relationship('NamesIndicators2020')


class Rejection2020(Indicators2020):
    __tablename__ = 'rejection2020'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2020.id'), primary_key=True)
    rejection = Column(Text)


class Indicators2021(Base):
    __tablename__ = 'indicators2021'
    __table_args__ = (
        UniqueConstraint('code_events', 'indication_id', 'fpsr_id'),
        {'schema': 'Business'}
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".indicators2021_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2021.code'))
    indication_id = Column(ForeignKey('Business.names_indicators2021.id'))
    fpsr_id = Column(ForeignKey('Business.fpsr2021.id'))
    is_estimated = Column(Boolean)
    unit_of_measurement = Column(String(60))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2021 = relationship('AllEvents2021')
    fpsr = relationship('Fpsr2021')
    indication = relationship('NamesIndicators2021')


class Rejection2021(Indicators2021):
    __tablename__ = 'rejection2021'
    __table_args__ = {'schema': 'Business'}

    id_value = Column(ForeignKey('Business.indicators2021.id'), primary_key=True)
    rejection = Column(Text)


class ResponseFio2016(Base):
    __tablename__ = 'response_fio2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2016_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class ResponseFio2017(Base):
    __tablename__ = 'response_fio2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2017_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class ResponseFio2018(Base):
    __tablename__ = 'response_fio2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2018_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class ResponseFio2019(Base):
    __tablename__ = 'response_fio2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2019_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class ResponseFio2020(Base):
    __tablename__ = 'response_fio2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2020_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class ResponseFio2021(Base):
    __tablename__ = 'response_fio2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".response_fio2021_id_seq'::regclass)"))
    id_response = Column(ForeignKey('response_obj.id'), nullable=False)
    fio = Column(String(255), nullable=False)

    response_obj = relationship('ResponseObj')


class Sources2016(Base):
    __tablename__ = 'sources2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2016_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2016.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))
    v = Column(Float(53))

    all_events2016 = relationship('AllEvents2016')
    finance = relationship('FinancingSource')


class Sources2017(Base):
    __tablename__ = 'sources2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2017_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2017.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))
    v = Column(Float(53))

    all_events2017 = relationship('AllEvents2017')
    finance = relationship('FinancingSource')


class Sources2018(Base):
    __tablename__ = 'sources2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2018_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2018.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))
    v = Column(Float(53))

    all_events2018 = relationship('AllEvents2018')
    finance = relationship('FinancingSource')


class Sources2019(Base):
    __tablename__ = 'sources2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2019_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2019.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2019 = relationship('AllEvents2019')
    finance = relationship('FinancingSource')


class Sources2020(Base):
    __tablename__ = 'sources2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2020_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2020.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2020 = relationship('AllEvents2020')
    finance = relationship('FinancingSource')


class Sources2021(Base):
    __tablename__ = 'sources2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".sources2021_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.all_events2021.code'))
    finance_id = Column(ForeignKey('financing_source.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))

    all_events2021 = relationship('AllEvents2021')
    finance = relationship('FinancingSource')


t_events_response_fio2016 = Table(
    'events_response_fio2016', metadata,
    Column('code_events', ForeignKey('Business.all_events2016.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2016.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_fio2017 = Table(
    'events_response_fio2017', metadata,
    Column('code_events', ForeignKey('Business.all_events2017.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2017.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_fio2018 = Table(
    'events_response_fio2018', metadata,
    Column('code_events', ForeignKey('Business.all_events2018.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2018.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_fio2019 = Table(
    'events_response_fio2019', metadata,
    Column('code_events', ForeignKey('Business.all_events2019.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2019.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_fio2020 = Table(
    'events_response_fio2020', metadata,
    Column('code_events', ForeignKey('Business.all_events2020.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2020.id'), primary_key=True, nullable=False),
    schema='Business'
)


t_events_response_fio2021 = Table(
    'events_response_fio2021', metadata,
    Column('code_events', ForeignKey('Business.all_events2021.code'), primary_key=True, nullable=False),
    Column('id_fio', ForeignKey('Business.response_fio2021.id'), primary_key=True, nullable=False),
    schema='Business'
)


class ExpensesGrbs2016(Base):
    __tablename__ = 'expenses_grbs2016'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2016_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2016.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2016.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2016 = relationship('EventsGrbs2016')
    category = relationship('Category')
    kbk2016 = relationship('Kbk2016')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2017(Base):
    __tablename__ = 'expenses_grbs2017'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2017_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2017.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2017.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2017 = relationship('EventsGrbs2017')
    category = relationship('Category')
    kbk2017 = relationship('Kbk2017')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2018(Base):
    __tablename__ = 'expenses_grbs2018'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2018_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2018.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2018.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2018 = relationship('EventsGrbs2018')
    category = relationship('Category')
    kbk2018 = relationship('Kbk2018')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2019(Base):
    __tablename__ = 'expenses_grbs2019'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2019_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2019.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2019.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2019 = relationship('EventsGrbs2019')
    category = relationship('Category')
    kbk2019 = relationship('Kbk2019')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2020(Base):
    __tablename__ = 'expenses_grbs2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2020_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2020.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2020.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2020 = relationship('EventsGrbs2020')
    category = relationship('Category')
    kbk2020 = relationship('Kbk2020')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2021(Base):
    __tablename__ = 'expenses_grbs2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2021_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2021.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2021.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2021 = relationship('EventsGrbs2021')
    category = relationship('Category')
    kbk2021 = relationship('Kbk2021')
    response_obj = relationship('ResponseObj')


class ExpensesGrbs2022(Base):
    __tablename__ = 'expenses_grbs2022'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".expenses_grbs2022_id_seq'::regclass)"))
    code_events = Column(ForeignKey('Business.events_grbs2022.code'))
    id_response = Column(ForeignKey('response_obj.id'))
    id_kbk = Column(ForeignKey('kbk2022.id'))
    id_category = Column(ForeignKey('categories.id'))
    fed = Column(Float(53))
    obl = Column(Float(53))

    events_grbs2022 = relationship('EventsGrbs2022')
    category = relationship('Category')
    kbk2022 = relationship('Kbk2022')
    response_obj = relationship('ResponseObj')


class ControlEvent2020(Base):
    __tablename__ = 'control_event2020'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2020.code'), nullable=False)
    control_event = Column(Text, nullable=False)

    main_event2020 = relationship('MainEvent2020')


class ControlEvent2021(Base):
    __tablename__ = 'control_event2021'
    __table_args__ = {'schema': 'Business'}

    code = Column(String(60), primary_key=True)
    code_main_event = Column(ForeignKey('Business.main_event2021.code'), nullable=False)
    control_event = Column(Text, nullable=False)

    main_event2021 = relationship('MainEvent2021')


class DateControlEvent2020(Base):
    __tablename__ = 'date_control_event2020'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".date_control_event2020_id_seq'::regclass)"))
    code_control_event = Column(ForeignKey('Business.control_event2020.code'), nullable=False)
    id_response = Column(ForeignKey('response_obj.id'))
    id_pf = Column(ForeignKey('plan_fact.id'))
    id_done = Column(ForeignKey('done.id'))
    id_viol = Column(ForeignKey('violation.id'))
    date_ce = Column(Date)

    control_event2020 = relationship('ControlEvent2020')
    done = relationship('Done')
    plan_fact = relationship('PlanFact')
    response_obj = relationship('ResponseObj')
    violation = relationship('Violation')


class CommentsCe2020(DateControlEvent2020):
    __tablename__ = 'comments_ce2020'
    __table_args__ = {'schema': 'Business'}

    id_date = Column(ForeignKey('Business.date_control_event2020.id'), primary_key=True)
    comments = Column(Text)


class DateControlEvent2021(Base):
    __tablename__ = 'date_control_event2021'
    __table_args__ = {'schema': 'Business'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Business\".date_control_event2021_id_seq'::regclass)"))
    code_control_event = Column(ForeignKey('Business.control_event2021.code'), nullable=False)
    id_response = Column(ForeignKey('response_obj.id'))
    id_pf = Column(ForeignKey('plan_fact.id'))
    id_done = Column(ForeignKey('done.id'))
    id_viol = Column(ForeignKey('violation.id'))
    date_ce = Column(Date)

    control_event2021 = relationship('ControlEvent2021')
    done = relationship('Done')
    plan_fact = relationship('PlanFact')
    response_obj = relationship('ResponseObj')
    violation = relationship('Violation')


class CommentsCe2021(DateControlEvent2021):
    __tablename__ = 'comments_ce2021'
    __table_args__ = {'schema': 'Business'}

    id_date = Column(ForeignKey('Business.date_control_event2021.id'), primary_key=True)
    comments = Column(Text)