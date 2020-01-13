"""
Helper class for controls app
"""

class ControlsCSV:
	
	"""
		This class parse controls csv file then extract the data
		from it.

		.is_valid() need to be called to see if there is any error
		before getting the data.
	"""

	def __init__(self, file):

		# Get CSV file and read it
		controls_csv = file.read()

		# Make sure string in UTF-8
		controls_csv = str(controls_csv, 'utf-8')

		# Get controls information from csv file
		self.controls_info = [line for line in controls_csv.split("\n")]

		# Get header of csv
		self.controls_info_header = self.controls_info.pop(0)

		self.error_message = ''

		# Get controls attributes label and index
		self.header = {}

		label_index = 0

		header_data = self.controls_info_header.split(',')

		# Check if there are 4 columns
		if (len(header_data) != 4):
			self.error_message = 'Invalid Controls CSV format. Please check documentation.'
	
		else:

			for label in header_data:

				# Remove quotes
				label = label.replace('"', '')

				self.header[label] = label_index
				label_index += 1

			# Check if all header labels are correct
			if (not 'name' in self.header or not 'control_type' in self.header or
				not 'maximum_rabi_rate' in self.header or not 'polar_angle' in self.header):
				
				self.error_message = 'Invalid Controls CSV labels. Please check documentation'

			else:

				# Control data to be added
				self.data = []

				for control_info in self.controls_info:
					control_info_chunk = control_info.split(',')

					if (len(control_info_chunk) == len(self.header)):
						self.data.append({
							'name': control_info_chunk[self.header['name']].replace('"', ''),
							'control_type': control_info_chunk[self.header['type']].replace('"', ''),
							'maximum_rabi_rate': float(control_info_chunk[self.header['maximum_rabi_rate']]),
							'polar_angle': float(control_info_chunk[self.header['polar_angle']])
						})
		

	def is_valid(self):
		if (self.error_message != ''):
			return False

		return True
		