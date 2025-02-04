ROLE_CHOICES = [
        ('Instructor', 'Instructor'),
        ('Student', 'Student')
    ]


from rest_framework.authtoken.models import Token
def TOKEN_USER(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    
    except Exception as e:
        return None 