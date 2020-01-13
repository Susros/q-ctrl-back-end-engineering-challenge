"""
Serializers for controls app
"""

from rest_framework import serializers
from .models import Control
from .utils import ControlsCSV
import os


class ControlSerializer(serializers.ModelSerializer):

	"""
		Control Model Serializer

		This handle CRUD for Control model.
	"""

	# Serializer Meta
	class Meta:
		model = Control
		fields = (
			'id',
			'name',
			'control_type',
			'maximum_rabi_rate',
			'polar_angle',
			'created_at',
			'modified_at',
			'url'
		)

	# Validate data
	def validate(self, data):

		# Make sure maximum rabi rate is between 0 and 100
		if (data['maximum_rabi_rate'] < 0 or data['maximum_rabi_rate'] > 100):
			raise serializers.ValidationError('Maximum Rabi Rate must be between 0 and 100')

		# Make sure polar angle is between 0 and 1
		if (data['polar_angle'] < 0 or data['polar_angle'] > 1):
			raise serializers.ValidationError('Polar Angle must be between 0 and 1.')

		return data

class ControlBulkSerializer(serializers.Serializer):

	"""
		Control Bulk Serializer

		This handle bulk creating controls by uploading CSV file
	"""

	controls_csv = serializers.FileField()

	def save(self):
		self.control_serializer = ControlSerializer(data = self.validated_data, many = True)
		self.control_serializer.is_valid(raise_exception = True)
		self.control_serializer.save()

	def validate(self, data):
		file_extension = os.path.splitext(data['controls_csv'].name)[1]

		if (file_extension != '.csv'):
			raise serializers.ValidationError('Invalid controls_csv file extension.')

		controls_csv_parser = ControlsCSV(data['controls_csv'])

		# Check if valid
		if (controls_csv_parser.is_valid() == False):
			raise serializers.ValidationError(controls_csv_parser.error_message)

		return controls_csv_parser.data