"""
This file is part of Lemon.

Lemon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lemon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lemon.  If not, see <http://www.gnu.org/licenses/>.


Copyright (c) 2012 Vicente Ruiz <vruiz2.0@gmail.com>
"""
# See http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4
from lemon.http.response import HttpResponse


class HttpResponseBadRequest(HttpResponse):
    status_code = 400
    status_text = 'BAD REQUEST'


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401
    status_text = 'UNAUTHORIZED'


class HttpResponsePaymentRequired(HttpResponse):
    status_code = 402
    status_text = 'PAYMENT REQUIRED'


class HttpResponseForbidden(HttpResponse):
    status_code = 403
    status_text = 'FORBIDDEN'


class HttpResponseNotFound(HttpResponse):
    status_code = 404
    status_text = 'NOT FOUND'


class HttpResponseMethodNotAllowed(HttpResponse):
    status_code = 405
    status_text = 'METHOD NOT ALLOWED'

    def __init__(self, permitted_methods):
        super(HttpResponseMethodNotAllowed, self).__init__()
        self['Allow'] = ', '.join(permitted_methods)


class HttpResponseNotAcceptable(HttpResponse):
    status_code = 406
    status_text = 'NOT ACCEPTABLE'


class HttpResponseProxyAuthenticationRequired(HttpResponse):
    status_code = 407
    status_text = 'PROXY AUTHENTICATION REQUIRED'


class HttpResponseRequestTimeout(HttpResponse):
    status_code = 408
    status_text = 'REQUEST TIMEOUT'


class HttpResponseConflict(HttpResponse):
    status_code = 409
    status_text = 'CONFLICT'


class HttpResponseGone(HttpResponse):
    status_code = 410
    status_text = 'GONE'


class HttpResponseLengthRequired(HttpResponse):
    status_code = 411
    status_text = 'LENGTH REQUIRED'


class HttpResponsePreconditionFailed(HttpResponse):
    status_code = 412
    status_text = 'PRECONDITION FAILED'


class HttpResponseRequestEntityTooLarge(HttpResponse):
    status_code = 413
    status_text = 'REQUEST ENTITY TOO LARGE'


class HttpResponseRequestURITooLong(HttpResponse):
    status_code = 414
    status_text = 'REQUEST-URI TOO LONG'


class HttpResponseUnsupportedMediaType(HttpResponse):
    status_code = 415
    status_text = 'UNSUPPORTED MEDIA TYPE'


class HttpResponseRequestedRangeNotSatisfiable(HttpResponse):
    status_code = 416
    status_text = 'REQUESTED RANGE NOT SATISFIABLE'


class HttpResponseExpectationFailed(HttpResponse):
    status_code = 417
    status_text = 'EXPECTATION FAILED'
