# Generated by Django 2.2.4 on 2019-12-02 04:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('subjectID', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Subject Number')),
                ('consent_given', models.BooleanField(default=False)),
                ('flower_order', models.CharField(default=None, max_length=400, validators=[django.core.validators.int_list_validator])),
                ('source_site', models.CharField(default=None, max_length=20, null=True, verbose_name='Source website')),
                ('linkID', models.CharField(default=None, max_length=25, null=True, verbose_name='Survey Link ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('P', 'Prefer not to say')], default=None, max_length=10)),
                ('age', models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(18, 'You must be 18 or over to participate in this experiment'), django.core.validators.MaxValueValidator(110, 'Please enter your age.')])),
                ('country', models.CharField(choices=[('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic of The'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Cote D'ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and Mcdonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libyan Arab Jamahiriya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia, The Former Yugoslav Republic of'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States of'), ('MD', 'Moldova, Republic of'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SH', 'Saint Helena'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and The Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and The South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan, Province of China'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2)),
                ('expertise_in_horticulture', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'Please select an option.'), django.core.validators.MaxValueValidator(5, 'Please select an option.')], verbose_name='Horticultural Expertise')),
                ('expertise_in_floral_design', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'You must select an option.'), django.core.validators.MaxValueValidator(5, 'You must select an option.')], verbose_name='Floral Design Expertise')),
                ('purchase_frequency', models.CharField(choices=[('Never', 'Never'), ('Quarterly', 'Once or twice in the space of several months'), ('Monthly', 'Once or twice per month'), ('Weekly', 'Once per week'), ('Bi-weekly', 'Several times per week')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('subjectID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sID', serialize=False, to='polls.Participant', verbose_name='Subject ID')),
                ('survey_attention', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)])),
                ('comments', models.CharField(default=None, max_length=500, null=True)),
                ('num_answers_unresponsive', models.DecimalField(decimal_places=0, default=None, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Unresponsive (%)')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('responseID', models.AutoField(primary_key=True, serialize=False, verbose_name='Response ID')),
                ('flowerID', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='Flower ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Timestamp')),
                ('appeal', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Appeal')),
                ('bullseye', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Bullseye')),
                ('busyness', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Busyness')),
                ('complexity', models.PositiveIntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Complexity')),
                ('depth', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Flower depth')),
				('interest', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Visual interest')),
                ('petal_quantity', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Quantity of Petals')),
                ('petal_size', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Petal size')),
                ('petal_variability', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Petal variability')),
                ('pointiness', models.PositiveIntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Pointiness')),
                ('symmetry', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Symmetry')),
                ('uniqueness', models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Uniqueness')),
                ('subjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Participant', verbose_name='Subject ID')),
            ],
        ),
    ]
