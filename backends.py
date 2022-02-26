import logging

from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPBindError

from django.conf import settings
from django.contrib.auth import get_user_model



logger = logging.getLogger(__name__)
UserModel = get_user_model()


class LDAPBackend:

    def authenticate(self, request, username=None, password=None, **kwargs):
        # set username to lowercase for consistency
        username = username.lower()
        # get the bind client to resolve DN
        logger.info('authenticating %s' % username)
        # set your server
        server = Server(settings.LDAP_HOST, get_info="__all__")
        try:
            conn = Connection(server, f"{username}@{settings.LDAP_DOMAIN}", password=password, auto_bind=True)
        except LDAPBindError as e:
            logger.info('LDAP authentication failed')
            logger.info(e)
            return None
        user = UserModel.objects.update_or_create(username=username)
        return user

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None