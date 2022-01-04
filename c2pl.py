from operation import Operation
op =  Operation('R')
lock_request_granted = True
commit_msg_recieved = False
to = ''
def c2pl_tm(msg):
	while(msg):
		if msg == 'transaction operation':
			#let op be the operation
			if op.type == 'BT':
				dp(op)
			else:
				c2pl_lm(op)
		elif msg == 'Lock Manager response':
			if lock_request_granted == True:
				print('say Hi')
				dp(op)#Si
			else:
				print('Transaction terminated')
		elif msg == 'Data Processor response':
			if to == 'R':
				return op.value
			elif to == 'W':
				print('Completion of the write')
			elif to == 'C':
				if commit_msg_recieved == True:
					print('Successful completion of transaction')
					c2pl_lm(op)
				else:
					print('arrival of the commit message recorded')
			elif to == 'A':
					print('Completion of the abort')
					c2pl_lm(op)

lu_unlocked = True
lock_mode = ''
lu_held_by_transaction = []
operations = ''
operation_waiting_for_queue = []
def c2pl_lm(op):
	if op.Type == 'R' or op.Type == 'W':
		#fin the lock nit  lu such that op.arg belongs to lu
		if lu_unlocked == True or lock_mode == op.Type :
			#set lock on lu in appropriate mode on behalf of transaction op.tid
			print("Lock granted")
		else:
			print("op on queue for lu")
	elif op.Type == 'C' or op.Type == 'A' :
		for lu in lu_held_by_transaction :
			#release lock on lu held by transaction
			if operations in operation_waiting_for_queue:
				#find the first operation O on queue
				#set a lock on lu on behalf of O
				print("Lock granted")
		print("Locks released")

def READ(x):
    return x

def WRITE(x):
    print(x, ' written')
    
def COMMIT(x):
    print('op committed')

def ABORT(x):
    print('op aborted')

def dp(op):
	if op.Type == 'BT':
		print('bookkeeping')
	elif op.Type == 'R':
		op.res = READ(op.arg)
		op.res = "Read done"
	elif op.Type == 'W':
		WRITE(op.arg,op.val)
		op.res = "Write done"
	elif op.Type == 'C':
		COMMIT
		op.res = "Commit done"
	elif op.Type == 'A':
		ABORT
		op.res = "Abort done"

	return op
