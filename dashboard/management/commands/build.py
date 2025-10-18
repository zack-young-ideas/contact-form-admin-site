"""
Builds JavaScript files.
"""

import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Builds JavaScript and SASS files using Vite.'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Building JavaScript and SASS files...')
        )
        try:
            subprocess.run(['npm', 'run', 'build'], check=True)
            self.stdout.write(
                self.style.SUCCESS(
                    'Build completed successfully.'
                )
            )
        except subprocess.CalledProcessError as e:
            self.stderr.write(
                self.style.ERROR(f'Build failed: {e}')
            )
