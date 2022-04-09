# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsAdminuser(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounts_adminuser'


class AccountsClientuser(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounts_clientuser'


class AccountsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Destination(models.Model):
    gid = models.AutoField(primary_key=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    z = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_name = models.CharField(max_length=254, blank=True, null=True)
    short_name = models.CharField(max_length=254, blank=True, null=True)
    zone = models.CharField(max_length=254, blank=True, null=True)
    wereda = models.CharField(max_length=254, blank=True, null=True)
    kebele = models.CharField(max_length=254, blank=True, null=True)
    locality_n = models.CharField(max_length=254, blank=True, null=True)
    organizati = models.CharField(max_length=254, blank=True, null=True)
    destinatio = models.CharField(max_length=254, blank=True, null=True)
    status_of = models.CharField(max_length=254, blank=True, null=True)
    area_in_sq = models.CharField(max_length=254, blank=True, null=True)
    estimated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unesco_reg = models.CharField(max_length=254, blank=True, null=True)
    when = models.CharField(max_length=254, blank=True, null=True)
    short_hist = models.CharField(max_length=254, blank=True, null=True)
    what_uniqu = models.CharField(max_length=254, blank=True, null=True)
    additional = models.CharField(max_length=254, blank=True, null=True)
    distance_f = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'destination'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MapsalesProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    index_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mapsales_product'


class MapsalesRequest(models.Model):
    product = models.OneToOneField(MapsalesProduct, models.DO_NOTHING, primary_key=True)
    message = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mapsales_request'


class PhotoappPhoto(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    created = models.DateTimeField()
    image = models.CharField(max_length=100)
    submitter = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photoapp_photo'


class Service(models.Model):
    gid = models.AutoField(primary_key=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    z = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_name = models.CharField(max_length=254, blank=True, null=True)
    short_name = models.CharField(max_length=254, blank=True, null=True)
    zone = models.CharField(max_length=254, blank=True, null=True)
    wereda = models.CharField(max_length=254, blank=True, null=True)
    kebele = models.CharField(max_length=254, blank=True, null=True)
    locality_n = models.CharField(max_length=254, blank=True, null=True)
    phone_line = models.CharField(max_length=254, blank=True, null=True)
    phone_mobi = models.CharField(max_length=254, blank=True, null=True)
    postal_cod = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    hot_line = models.CharField(max_length=254, blank=True, null=True)
    organizati = models.CharField(max_length=254, blank=True, null=True)
    service = models.CharField(max_length=254, blank=True, null=True)
    service_ty = models.CharField(max_length=254, blank=True, null=True)
    service_da = models.CharField(max_length=254, blank=True, null=True)
    service_ti = models.CharField(max_length=254, blank=True, null=True)
    additional = models.CharField(max_length=254, blank=True, null=True)
    owner_name = models.CharField(max_length=254, blank=True, null=True)
    establishm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    branch = models.CharField(max_length=254, blank=True, null=True)
    moto = models.CharField(max_length=254, blank=True, null=True)
    distance_f = models.CharField(max_length=254, blank=True, null=True)
    distance_1 = models.CharField(max_length=254, blank=True, null=True)
    short_disc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'service'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class StreetsWgs1984(models.Model):
    gid = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    road_class = models.BigIntegerField(blank=True, null=True)
    road_weath = models.BigIntegerField(blank=True, null=True)
    condition_field = models.BigIntegerField(db_column='condition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    vertical_r = models.BigIntegerField(blank=True, null=True)
    track_or_l = models.IntegerField(blank=True, null=True)
    median_pre = models.BigIntegerField(blank=True, null=True)
    load_beari = models.BigIntegerField(blank=True, null=True)
    horizontal = models.BigIntegerField(blank=True, null=True)
    commertial = models.CharField(max_length=50, blank=True, null=True)
    source_dat = models.BigIntegerField(blank=True, null=True)
    source_typ = models.BigIntegerField(blank=True, null=True)
    ft_zlev = models.BigIntegerField(blank=True, null=True)
    tf_zlev = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    road_area_field = models.CharField(db_column='road_area_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    streets_na = models.CharField(max_length=60, blank=True, null=True)
    walkspeed_field = models.BigIntegerField(db_column='walkspeed_', blank=True, null=True)  # Field renamed because it ended with '_'.
    speedlimit = models.IntegerField(blank=True, null=True)
    bicyclespe = models.BigIntegerField(blank=True, null=True)
    oneway = models.CharField(max_length=30, blank=True, null=True)
    ft_minutes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meters = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    length_km = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    source = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streets_wgs_1984'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)
