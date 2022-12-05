import datetime
from database import Base, Session, AdvModel, OwnerModel
from pytest import fixture


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

@fixture()
def create_owner():
    with Session() as session:
        new_owner = OwnerModel(name='NEW_NAME')
        session.add(new_owner)
        session.commit()
        return {''
                'id': new_owner.id,
                'name': new_owner.name,
                }
@fixture()
def create_adv():
    with Session() as session:
        new_adv = AdvModel(title='NEW_TITLE', text='NEW_TEXT_ADV', published_at=f"{datetime.datetime.now()}", user_id=1)
        session.add(new_adv)
        session.commit()
        return {
                'id': new_adv.id,
                'title': new_adv.title,
                'text': new_adv.text,
                'published_at': new_adv.published_at,
                'user_id': new_adv.user_id,
                }
