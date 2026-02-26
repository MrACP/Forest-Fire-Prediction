def mapper(_, text, writer):
    w = text.split(',')
    w1= int(w[5])
    if w1>30:
	writer.emit(w[5], 'FireAlert')
#    else:
#	writer.emit(w[5], "Safe")
