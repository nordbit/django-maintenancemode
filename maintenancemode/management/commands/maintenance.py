#!/usr/bin/env python
# coding: utf-8

from django.core.management.base import BaseCommand, CommandError

from maintenancemode.models import MaintenanceMode

class Command(BaseCommand):
    args = '<maintenance_id> (on|off)'
    help = 'Toggle maintenance mode on or off'

    def handle(self, pk=None, state=None, **kwargs):
        if not pk or not state in ['on', 'off']:
            raise CommandError('maintenance %s' % self.args)

        try:
            mm = MaintenanceMode.objects.get(pk=pk)
        except MaintenanceMode.DoesNotExist:
            self.stderr.write('Available maintenance modes:\n')
            for available in MaintenanceMode.objects.all():
                self.stderr.write(
                    str(available.pk) + '. ' + str(available) + '\n')
            raise CommandError('invalid maintenance id')
        mm.enable_maintenance_mode = (state == 'on')
        mm.save()

