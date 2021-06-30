import psychopy

class DrawHexGrid:
	'''
	Formula for calculating coordinates:
	xx = x + (d * cos(alpha))
	yy = y + (d * sin(alpha))
	'''
	def __init__(self, top_left_origin, edge_length = 100, x_count = 5, y_count = 5):
		self.top_left_origin = top_left_origin
		self.edge_length = edge_length
		self. x_count = x_count
		self.y_count = y_count
		self.point_list = ['top_left', 'bottom_left', 'bottom', 'bottom_right', 'top_right', 'top']
		self.point_dictionary = {
'top_left': '[start_coord[0], start_coord[1] - self.edge_length]',
'bottom_left': '[start_coord[0] + self.edge_length * cos(120), start_coord[1] - self.edge_length * sin(120)]',
'bottom': '[start_coord[0] + self.edge_length * cos(120), start_coord[1] + self.edge_length * sin(120)]',
'bottom_right': '[start_coord[0], start_coord[1] + self.edge_length]',
'top_right': '[start_coord[0] - self.edge_length * cos(120), start_coord[1] + self.edge_length * sin(120)]',
'top': '[start_coord[0] - self.edge_length * cos(120), start_coord[1] - self.edge_length * sin(120)]'
}
		
	def make_grid(self):
		for row in range(self.y_count):
			for col in range(self.x_count):
				## if it's the first hex
				if not row and not col:
					self._draw_hex('top_left', 'top_left', self.top_left_origin)
					self.first_row_start_coord = self._coord_calculator(self.top_left_origin, 'top_left', 2)
					self.new_hex_start_coord = self._coord_calculator(self.top_left_origin, 'top_left', 3)
				
				## if it's the first row
				elif not row:
					self._draw_hex('bottom_left', 'top_left', self.new_hex_start_coord)
					self.new_hex_start_coord = self._coord_calculator(self.new_hex_start_coord, 'bottom_left', 2)
					
				## if it's the first column
				elif not col:
					
					## conditional to account for the staggered pattern
					if not row % 2:
					## if even
						start_pos = 'top'
						new_hex_n_turns = 4
						first_row_n_turns = 3
						
					else:
					## if odd
						start_pos = 'top_left'
						new_hex_n_turns = 3
						first_row_n_turns = 1
						
					self._draw_hex(start_pos, 'top_right', self.first_row_start_coord)
					self.new_hex_start_coord = self._coord_calculator(self.first_row_start_coord, start_pos, new_hex_n_turns)
					self.first_row_start_coord = self._coord_calculator(self.first_row_start_coord, start_pos, first_row_n_turns)
					
				## for all internal hex's
				else:
					## catch the last hex on odd rows
					if col == self.x_count - 1 and row % 2:
						end_pos = 'top'
					else:
						end_pos = 'top_right'

					self._draw_hex('bottom_left', end_pos, self.new_hex_start_coord)
					self.new_hex_start_coord = self._coord_calculator(self.new_hex_start_coord, 'bottom_left', 2)


					
	def _coord_calculator(self, start_coord, start_pos, n_turns):
		## takes in a starting coordinate, starting pos, and number of calcs to do
		## returns ending coord as [x, y]
		## this function will fail if you try to turn past top left, which i dont think ill need to do
		
		## calc a slice out of point_list to iterate over what's appropriate
		new_point_list = self._rearrange_point_list(start_pos)
		
		for pos in new_point_list[:n_turns]:
			start_coord = eval(self.point_dictionary[pos])
		
		return start_coord
			
			
	
	def _draw_hex(self, start_pos, end_pos, start_coord):
		## draws a line from start_pos to end_pos

		new_point_list = self._rearrange_point_list(start_pos)

		for position in new_point_list:
			if start_pos != end_pos and position == end_pos:
				break
			
			line = self._define_line_type()
			line.start = start_coord
			line.end = eval(self.point_dictionary[position])
			start_coord= line.end
			line.draw()

	def _rearrange_point_list(self, start_pos):
		## outputs a list where the first element is start_pos and the last element is the one before start_pos in point_list

		if start_pos == 'top_left':
			return self.point_list

		return self.point_list[self.point_list.index(start_pos):] + self.point_list[:self.point_list.index(start_pos)-1]

	def _define_line_type(self):
		return psychopy.visual.Line(
			win = win,
			units='pix',
			lineColor=[-1, -1, -1]
			)
