def minutes_to_ms(time_input):
	break_point = time_input.index(":")
	mins = int( time_input[0:break_point])
	seconds =  int(time_input[(break_point+1):])

	ms_time = (mins * 60000) + (seconds * 1000)

	return ms_time

def ms_to_min(time_ms):
	mins = time_ms / 60000

	string_min = str(mins)
	
	decimal =  (string_min.index("."))

	seconds  = int((float(string_min[decimal:]))*60)

	minutes = int(string_min[0:decimal])

	returnString = f"{minutes}:{seconds}"

	return returnString
