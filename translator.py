import re
class translator:
	
	def func(self):

		file1=open("32_bit.asm","r")
		file2=open("64_bit_converted.asm","w")

		lines=file1.readlines()
		for line in lines:
				if not line.strip():
					continue
				x=re.search("extern",line)
				if(x):
					continue
				x=re.search("section",line)
				if(x):
					file2.write(line+"\n")
					continue
				x=re.search("message db",line)
				if(x):
					file2.write(line+"\n")
					continue
				x=re.search("global main",line)
				if(x):
					file2.write("global _start\n")
					continue
				x=re.search("main:",line)
				if(x):
					file2.write("_start:\n")
					continue
				x=re.search("pushad",line)
				if(x):
					file2.write("\tmov	rax,1\n")
					file2.write("\tmov	rdi,1\n")
					continue
				x=re.search("push dword",line)
				if(x):
					file2.write("\tmov	rsi,message\n")
					continue
				x=re.search("call",line)
				if(x):
					file2.write("\tmov 	rdx,13\n")
					file2.write("\tsyscall\n")
					continue
				x=re.search("add esp, 4",line)
				if(x):
					file2.write("\tmov	rax,60\n")
					file2.write("\tmov	rdi,0\n")
					continue
				x=re.search("ret",line)
				if(x):
					file2.write("\tsyscall\n")
					continue
				x=re.search("popad",line)
				if(x):
					continue
				else:
					file2.write("\n")




if __name__ == "__main__":
	obj=translator()
	obj.func()
