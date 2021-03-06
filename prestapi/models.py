from django.db import models

# Create your models here.
class Config(models.Model):
    logo            = models.ImageField(null = True, blank = True)
    admin_costs     = models.IntegerField(null = False, default = 16000)
    insurance       = models.IntegerField(null = False, default = 17000)
    system_costs    = models.IntegerField(null = False, default = 24000)
    interest        = models.FloatField(null = False, default = 0.018769)
    iva             = models.FloatField(null = False, default = 0.19)

    smtp_server     = models.CharField(max_length = 50, default = '')
    smtp_port       = models.CharField(max_length = 4, default = '')
    email_sender    = models.CharField(max_length = 60, default = '')
    email_password  = models.CharField(max_length = 50, default = '')

    class Meta:
        verbose_name_plural = 'Configuraciones'

    def get_iva(self):
        return int((self.admin_costs + self.insurance + self.system_costs) * self.iva)

class Request(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    approved_date = models.DateField(auto_now=True)
    order = models.CharField(max_length=100, default='', unique=True)
    price = models.IntegerField(default = 0)
    months = models.IntegerField(default = 6)
    pay_day = models.IntegerField(default = 15)
    user = models.ForeignKey('CreditUser', null=True, on_delete=models.SET_NULL)
    approved = models.NullBooleanField(default=False, null=True, blank=True)
    score = models.IntegerField(default = 0, null=True, blank=True)

    def __str__(self):
        return '{}: ${} ({})'.format(self.user, self.price, self.order)

    class Meta:
        verbose_name_plural = 'Solicitudes'

class CreditUser(models.Model):
    email           = models.CharField(max_length =100, default = '', unique = True)
    first_name      = models.CharField(max_length = 30, default = '')
    last_name       = models.CharField(max_length = 30, default = '')
    gender          = models.CharField(max_length = 1, default = '')
    document_type   = models.IntegerField(default = 1)
    document_id     = models.IntegerField(default = 0)
    expedition_date = models.DateField(null = True)
    birthdate       = models.DateField(null = True)
    phone           = models.IntegerField(default = 0)
    civil_status    = models.CharField(max_length = 100, default = '')
    work_activity   = models.CharField(max_length = 100, default = '')
    work_type       = models.CharField(max_length = 100, default = '')
    favorite_bank   = models.CharField(max_length = 100, default = '')
    mail_code       = models.CharField(max_length = 4, default = '')
    sms_code        = models.CharField(max_length = 4, default = '')
    #credit_requests = models.ManyToManyField('Request')
    mensual_outgoings   = models.IntegerField(default = 0)
    mensual_incomings   = models.IntegerField(default = 0)
    address_residence   = models.CharField(max_length = 100, default = '')
    type_of_property    = models.CharField(max_length = 100, default = '')
    personal_reference_city     = models.CharField(max_length = 100, default = '')
    personal_reference_phone    = models.IntegerField(default = 0)
    personal_reference_first_name   = models.CharField(max_length = 100, default = '')
    personal_reference_last_name    = models.CharField(max_length = 100, default = '')

    class Meta:
        verbose_name_plural = 'Usuarios de credito'

    def __str__(self):
        return self.email


class Client(models.Model):
    first_name   = models.CharField(max_length = 30, default = '')
    last_name    = models.CharField(max_length = 30, default = '')
    site_url    = models.CharField(max_length = 300, default = '')
    account_id  = models.IntegerField(null = True, blank = True)
    secret_key  = models.CharField(max_length = 100, default = '')

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{} {} -> [ {} ]'.format(self.first_name, self.last_name, self.site_url)
