from django.test import TestCase
from .setupTest import SetupTest


class TestUsersViewGet(SetupTest, TestCase):

    def test_realiza_request_get_sem_credencial_e_retorna_401(self):
        res = self.app.get(self.url, format="json")
        self.assertEquals(res.status_code, 401)

    def test_realiza_request_get_com_credencial_invalida_401(self):
        headers={'HTTP_AUTHORIZATION':"Bearer 123456"}
        res = self.app.get(self.url, **headers)
        
        self.assertEquals(res.status_code, 401)
    
    def test_realiza_request_get_com_credencial_de_superuser_e_retorna_200(self):

        token = self.get_tokens_for_user(self.usuarioAdmin)
        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(self.url, **headers)
        
        
        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_credencial_de_usuario_comum_e_retorna_301(self):

        token = self.get_tokens_for_user(self.usuarioComum)
        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(self.url, **headers)
        
        self.assertEquals(res.status_code, 403)

    def test_realiza_request_get_com_id_sem_credencial_e_retorna_401(self):
        url = self.url + f'{self.usuarioComum.id}/'
        res = self.app.get(url)
        
        self.assertEquals(res.status_code, 401)

    def test_realiza_request_get_com_id_de_outro_usuario_com_credencial_comum_e_retorna_403(self):
        url = self.url + f'{self.usuarioComum2.id}/'
        token = self.get_tokens_for_user(self.usuarioComum)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(url, **headers)
        
        self.assertEquals(res.status_code, 403)

    def test_realiza_request_get_com_proprio_id_com_credencial_comum_e_retorna_200(self):
        url = self.url+f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioComum)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(url,**headers)

        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_proprio_id_com_credencial_admin_e_retorna_200(self):
        user = self.usuarioAdmin
        url = self.url + f'{user.id}/'
        token = self.get_tokens_for_user(user)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(url, **headers)

        self.assertEquals(res.status_code, 200)

    def test_realiza_request_get_com_outro_id_com_credencial_admin_e_retorna_200(self):
        url = self.url + f'{self.usuarioComum.id}/'
        token = self.get_tokens_for_user(self.usuarioAdmin)

        headers= {'HTTP_AUTHORIZATION':f"Bearer {token['access']}"}
        res = self.app.get(self.url, **headers)

        self.assertEquals(res.status_code, 200)
    

    