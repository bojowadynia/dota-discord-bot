# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2024-04-03 07:02
from __future__ import unicode_literals

from django.db import migrations

import os

class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0082_auto_20240315_1504'),
    ]

    db_name = os.environ.get('DB_NAME', 'default_db_name')

    operations = [
        migrations.RunSQL(
            sql=f"ALTER DATABASE `{db_name}` CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;",
            reverse_sql=migrations.RunSQL.noop,
            # Assuming there's no need for a reverse operation for the database collation
        ),
        migrations.RunSQL(
            sql=[
                "ALTER TABLE `auth_group` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `auth_group_permissions` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `auth_permission` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `auth_user` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `auth_user_groups` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `auth_user_user_permissions` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `balancer_balanceanswer` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `balancer_balanceresult` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `django_admin_log` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `django_content_type` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `django_migrations` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `django_session` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_discordchannels` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_discordpoll` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_ladderqueue` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_laddersettings` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_match` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_matchplayer` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_player` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_player_blacklist` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_playerreport` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_queuechannel` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_queueplayer` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_rolespreference` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `ladder_scorechange` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `stock_joke_stockbuyer` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
                "ALTER TABLE `stock_joke_stockjokesettings` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
            ],
            reverse_sql=migrations.RunSQL.noop  # Assuming there's no need for a reverse operation
        )
    ]