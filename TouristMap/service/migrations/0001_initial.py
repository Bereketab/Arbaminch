# Generated by Django 4.0.3 on 2022-04-02 10:44

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('is_admin', models.BooleanField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'accounts_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'accounts_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'accounts_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('z', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('code', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('full_name', models.CharField(blank=True, max_length=254, null=True)),
                ('short_name', models.CharField(blank=True, max_length=254, null=True)),
                ('zone', models.CharField(blank=True, max_length=254, null=True)),
                ('wereda', models.CharField(blank=True, max_length=254, null=True)),
                ('kebele', models.CharField(blank=True, max_length=254, null=True)),
                ('locality_n', models.CharField(blank=True, max_length=254, null=True)),
                ('organizati', models.CharField(blank=True, max_length=254, null=True)),
                ('destinatio', models.CharField(blank=True, max_length=254, null=True)),
                ('status_of', models.CharField(blank=True, max_length=254, null=True)),
                ('area_in_sq', models.CharField(blank=True, max_length=254, null=True)),
                ('estimated', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unesco_reg', models.CharField(blank=True, max_length=254, null=True)),
                ('when', models.CharField(blank=True, max_length=254, null=True)),
                ('short_hist', models.CharField(blank=True, max_length=254, null=True)),
                ('what_uniqu', models.CharField(blank=True, max_length=254, null=True)),
                ('additional', models.CharField(blank=True, max_length=254, null=True)),
                ('distance_f', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'destination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MapsalesProduct',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('index_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'mapsales_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PhotoappPhoto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=250)),
                ('created', models.DateTimeField()),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'photoapp_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.DecimalField(blank=True, decimal_places=Decimal('65535'), max_digits=65535, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=Decimal('65535'), max_digits=65535, null=True)),
                ('z', models.DecimalField(blank=True, decimal_places=Decimal('65535'), max_digits=65535, null=True)),
                ('code', models.DecimalField(blank=True, decimal_places=Decimal('65535'), max_digits=65535, null=True)),
                ('full_name', models.CharField(blank=True, max_length=254, null=True)),
                ('short_name', models.CharField(blank=True, max_length=254, null=True)),
                ('zone', models.CharField(blank=True, max_length=254, null=True)),
                ('wereda', models.CharField(blank=True, max_length=254, null=True)),
                ('kebele', models.CharField(blank=True, max_length=254, null=True)),
                ('locality_n', models.CharField(blank=True, max_length=254, null=True)),
                ('phone_line', models.CharField(blank=True, max_length=254, null=True)),
                ('phone_mobi', models.CharField(blank=True, max_length=254, null=True)),
                ('postal_cod', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=254, null=True)),
                ('hot_line', models.CharField(blank=True, max_length=254, null=True)),
                ('organizati', models.CharField(blank=True, max_length=254, null=True)),
                ('service', models.CharField(blank=True, max_length=254, null=True)),
                ('service_ty', models.CharField(blank=True, max_length=254, null=True)),
                ('service_da', models.CharField(blank=True, max_length=254, null=True)),
                ('service_ti', models.CharField(blank=True, max_length=254, null=True)),
                ('additional', models.CharField(blank=True, max_length=254, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=254, null=True)),
                ('establishm', models.DecimalField(blank=True, decimal_places=Decimal('65535'), max_digits=65535, null=True)),
                ('branch', models.CharField(blank=True, max_length=254, null=True)),
                ('moto', models.CharField(blank=True, max_length=254, null=True)),
                ('distance_f', models.CharField(blank=True, max_length=254, null=True)),
                ('distance_1', models.CharField(blank=True, max_length=254, null=True)),
                ('short_disc', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetsWgs1984',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(blank=True, max_length=50, null=True)),
                ('road_class', models.BigIntegerField(blank=True, null=True)),
                ('road_weath', models.BigIntegerField(blank=True, null=True)),
                ('condition_field', models.BigIntegerField(blank=True, db_column='condition_', null=True)),
                ('vertical_r', models.BigIntegerField(blank=True, null=True)),
                ('track_or_l', models.IntegerField(blank=True, null=True)),
                ('median_pre', models.BigIntegerField(blank=True, null=True)),
                ('load_beari', models.BigIntegerField(blank=True, null=True)),
                ('horizontal', models.BigIntegerField(blank=True, null=True)),
                ('commertial', models.CharField(blank=True, max_length=50, null=True)),
                ('source_dat', models.BigIntegerField(blank=True, null=True)),
                ('source_typ', models.BigIntegerField(blank=True, null=True)),
                ('ft_zlev', models.BigIntegerField(blank=True, null=True)),
                ('tf_zlev', models.BigIntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, null=True)),
                ('road_area_field', models.CharField(blank=True, db_column='road_area_', max_length=254, null=True)),
                ('shape_leng', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('streets_na', models.CharField(blank=True, max_length=60, null=True)),
                ('walkspeed_field', models.BigIntegerField(blank=True, db_column='walkspeed_', null=True)),
                ('speedlimit', models.IntegerField(blank=True, null=True)),
                ('bicyclespe', models.BigIntegerField(blank=True, null=True)),
                ('oneway', models.CharField(blank=True, max_length=30, null=True)),
                ('ft_minutes', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('meters', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('length_km', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('the_geom', models.TextField(blank=True, null=True)),
                ('source', models.IntegerField(blank=True, null=True)),
                ('target', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'streets_wgs_1984',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaggitTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'taggit_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaggitTaggeditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
            ],
            options={
                'db_table': 'taggit_taggeditem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsAdminuser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.accountsuser')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'accounts_adminuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsClientuser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.accountsuser')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'accounts_clientuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MapsalesRequest',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.mapsalesproduct')),
                ('message', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'mapsales_request',
                'managed': False,
            },
        ),
    ]