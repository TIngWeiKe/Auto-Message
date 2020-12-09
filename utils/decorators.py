from functools import wraps
import re
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
# from utils.auth import get_org_from_username

from .exceptions import *
from rest_framework.exceptions import ParseError


def DRF_response(func):
    @wraps(func)
    def inner(*args, **kwargs):
        from rest_framework import status as DRF_status
        from rest_framework.response import Response

        response = {'SUCCESS': True}
        status = DRF_status.HTTP_200_OK

        try:
            view_return = func(*args, **kwargs)

            if isinstance(view_return, tuple):
                payload, status_code = view_return
                if status_code == 201:
                    status = DRF_status.HTTP_201_CREATED
                elif status_code == 204:
                    status = DRF_status.HTTP_204_NO_CONTENT
                elif status_code == 500:
                    response = {
                        'SUCCESS': False,
                        'ERR_MSG': 'Internal Server Error'
                    }
                    status = DRF_status.HTTP_500_INTERNAL_SERVER_ERROR
                    return Response(response, status=status)

            elif isinstance(view_return, Response):
                return view_return
            else:
                payload = view_return

            response['PAYLOAD'] = payload

        except UserError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': str(e)
            }
            status = DRF_status.HTTP_400_BAD_REQUEST

        except MissingInputError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Missing input data: {str(e)}"
            }
            status = DRF_status.HTTP_400_BAD_REQUEST

        except GeneralError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"{str(e)}"
            }
            status = DRF_status.HTTP_400_BAD_REQUEST

        except AlreadyExistError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Object already exist: {str(e)}"
            }
            status = DRF_status.HTTP_400_BAD_REQUEST

        except ObjectDoesNotExist as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Object does not exist: {str(e)}"
            }
            status = DRF_status.HTTP_400_BAD_REQUEST

        except PermissionDenied as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Permission denied: {str(e)}"
            }
            status = DRF_status.HTTP_403_FORBIDDEN

        except ParseError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"{str(e)}"
            }
            status = DRF_status.HTTP_400_BAD_REQUEST
        return Response(response, status=status)
    return inner


def http_response(func):
    @wraps(func)
    def inner(*args, **kwargs):
        from django.http import HttpResponse, JsonResponse

        status = 200
        try:
            payload = func(*args, **kwargs)
            response = payload
        except MissingInputError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Missing input data: {str(e)}"
            }
            status = 400
            return JsonResponse(response, status=status)
        except ObjectDoesNotExist as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Object does not exist: {str(e)}"
            }
            status = 400
            return JsonResponse(response, status=status)

        return HttpResponse(response, status=status)
    return inner


def json_response(func):
    @wraps(func)
    def inner(*args, **kwargs):
        from django.http import JsonResponse

        response = {'SUCCESS': True}
        status = 200

        try:
            payload = func(*args, **kwargs)

            if isinstance(payload, tuple):
                payload, status = payload

            response['PAYLOAD'] = payload

        except UserError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': str(e)
            }
            status = 400

        except GeneralError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"{str(e)}"
            }
            status = 400

        except MissingInputError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Missing input data: {str(e)}"
            }
            status = 400

        except AlreadyExistError as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Object already exist: {str(e)}"
            }
            status = 400

        except ObjectDoesNotExist as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Object does not exist: {str(e)}"
            }
            status = 400

        except PermissionDenied as e:
            response = {
                'SUCCESS': False,
                'ERR_MSG': f"Permission denied: {str(e)}"
            }
            status = 403

        return JsonResponse(response, status=status)
    return inner
