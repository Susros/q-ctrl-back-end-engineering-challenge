"""
Views for controsl app
"""

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from .models import Control
from .serializers import ControlSerializer, ControlBulkSerializer
import csv

class ControlView(viewsets.ModelViewSet):

	"""
		Controls Views

		This handle API Request and Response.

		Available APIs are:
			- GET    /controls 			: List all controls
			- POST   /controls 			: Create a new control
			- GET    /controls/<id> 	: Get a specific control
			- PUT    / controls/<id> 	: Update a specific control
			- DELETE /controls<id> 		: Delete a specific control
			- POST   /controls/bulk     : Bulk create control with CSV file
			- GET    /controls/download : Download all controls in CSV format

	"""

	# Control object query set
	queryset = Control.objects.all()

	# Get control serializer
	serializer_class = ControlSerializer

	parser_class = (FileUploadParser,)

	@action(detail = False, methods = ['POST'])
	def bulk(self, request, *args, **kwargs):
		
		'''
			Bulk create controls by uploading CSV file.
			This method read CSV file and create control.
		'''

		control_bulk_serializer = ControlBulkSerializer(data = request.data)
		control_bulk_serializer.is_valid(raise_exception = True)
		control_bulk_serializer.save()
		return Response(control_bulk_serializer.control_serializer.data, status=status.HTTP_201_CREATED)


	@action(detail = False, methods = ['GET'])
	def download(self, request, *args, **kwargs):

		'''
			Download controls in CSV format
		'''

		# Set HTTP Response Header
		response = HttpResponse(content_type = 'text/csv')
		response['Content-Disposition'] = 'attachment; filename="controls.csv"'

		# Get CSV writer
		writer = csv.writer(response)

		# Create header
		writer.writerow(['name', 'type', 'maximum_rabi_rate', 'polar_angle'])

		# Get all controls
		controls_info = Control.objects.all().values_list('name', 'control_type', 'maximum_rabi_rate', 'polar_angle')

		# Write controls info to CSV
		for data in controls_info:
			writer.writerow(data)

		return response

