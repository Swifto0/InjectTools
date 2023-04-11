import os
import binascii

def read_bin():
	shellcode = ''
	with open('demon.bin', 'rb') as file:
		byte_array = bytearray(file.read(1))
		while True:
			if not byte_array:
				break	
			hex_string = binascii.hexlify(byte_array).decode()
			#print('\\x%s' % hex_string, end='')
			unit = '\\x' + hex_string
			shellcode += unit
			byte_array = bytearray(file.read(1))
		#print(shellcode)

	return shellcode


def payload2c(shellcode):
	print('\"', end='')
	index = 0
	for i in range(len(shellcode)):
		if shellcode[i] == '\\':
			index += 1
		if(index == 30):
			print('\"\n\"', end = '')
			index = 0
		print(shellcode[i], end = '')
	print('\";')

def main():
	shellcode = read_bin()
	payload2c(shellcode)

if __name__ == '__main__':
	main()