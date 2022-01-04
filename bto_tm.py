from operation import Operation

op = Operation('')

transaction_op_type = ''

def bto_tm(msg):
	while(msg):
		if msg.type == 'transaction operation':
			#let op be the operation
			if op.Type == 'BT':
				S = None
				#assign timestamp ts(T) to transaction
				dp(op)
			elif op.Type == 'R' or op.Type == 'W':
				print('Say Si')
				bto_sc(op,ts(T))#Si
				S = S + Si
			elif op.Type == 'A' or op.Type == 'C':
				dp(op)#S
		elif msg.type == 'SC response':
			op.Type = A 
			bto_sc(op,_)#S
			#restart transaction with a new timestamp
		elif msg.type == 'DP response':
			#let op be the operation
			if transaction_op_type == 'R':
				return op.value