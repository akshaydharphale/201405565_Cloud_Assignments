nasm -f elf32 32_bit.asm
gcc -m32 32_bit.o -o 32_bit_run
./32_bit_run

nasm -f elf64 64_bit.asm
ld 64_bit.o -o 64_bit_run
./64_bit_run

python translator.py

nasm -f elf64 64_bit_converted.asm
ld 64_bit_converted.o -o 64_bit_converted_run
./64_bit_converted_run
