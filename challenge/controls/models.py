"""
Models for controls app
"""

from django.db import models

class Control(models.Model):

	"""
		Control Model

		Store the following controls' information:
			- name 				: The name of the control.
			- Control Type		: {Primitive, CORPSE, Gaussian, CinBB, CinSK}
			- Maximum Rabi Rate : The maximum achievable angular frequency of the
								  Rabi cycle for a driven quantum transition. The
								  number is between 0 and 100.
			- Polar Angle		: An angle measured from the z-axis on the Bloch sphere.
								  The number is between 0 andn 1 (units of pi).
			- Created At 		: Date when the control was added to database.
			- Modified At 		: Date when the control was last modified.

	"""

	class Meta:
		ordering = ['-id']

	# Specified the valid type of controls
	ControlType = [
		('Primitive', 'Primitive'),
		('CORPSE'   , 'CORPSE'),
		('Gaussian' , 'Gaussian'),
		('CinBB'    , 'CinBB'),
		('CinSK'    , 'CinSK')
	]

	name   			  = models.CharField(max_length = 256)
	control_type	  = models.CharField(choices = ControlType, max_length = 10)
	maximum_rabi_rate = models.DecimalField(max_digits = 8, decimal_places = 5)
	polar_angle 	  = models.DecimalField(max_digits = 6, decimal_places = 5)
	created_at		  = models.DateTimeField(auto_now_add = True)
	modified_at		  = models.DateTimeField(auto_now = True)

