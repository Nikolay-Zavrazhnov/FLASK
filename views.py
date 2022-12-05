from flask.views import MethodView
from flask import jsonify, request
from database import AdvModel, OwnerModel, Session
from errors import ApiException


class OwnerViews(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            user = session.query(OwnerModel).get(user_id)
            if user is None:
                raise ApiException(404, 'is user not found')

            return jsonify({
                'id': user.id,
                'name': user.name
            })

    def post(self):
        user_data = request.json
        with Session() as session:
            new_user = OwnerModel(**user_data)
            session.add(new_user)
            session.commit()
            return jsonify({
                'id': new_user.id,
                'name': new_user.name
            })


class AdvViews(MethodView):

    def get(self, adv_id: int):
        with Session() as session:
            adv = session.query(AdvModel).get(adv_id)
            if adv is None:
                raise ApiException(404, 'advertisement not found')

            return jsonify({'id': adv.id,
                            'title': adv.title,
                            'text': adv.text,
                            'user_id': adv.user_id,
                            'published_at': adv.published_at,
                            })

    def post(self):
        adv_data = request.json
        with Session() as session:
            new_adv = AdvModel(**adv_data)
            session.add(new_adv)
            session.commit()
            return jsonify({
                'id': new_adv.id,
                'title': new_adv.title,
                'text': new_adv.text,
                'published_at': new_adv.published_at,
                'user_id': new_adv.user_id
            })

    def patch(self, adv_id):
        adv_data = request.json
        with Session() as session:
            adv = session.query(AdvModel).get(adv_id)
            for field, value in adv_data.items():
                setattr(adv, field, value)
            session.add(adv)
            session.commit()
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'text': adv.text,
                'published_at': adv.published_at,
                'user_id': adv.user_id,
            })

    def delete(self, adv_id: int):
        with Session() as session:
            adv = session.query(AdvModel).get(adv_id)
            session.delete(adv)
            session.commit()
            return jsonify({
                'advertisements': 'delete'
            })
