%include "macro.asm"

section .data
	newline db 10,0 ; pointer to 2 byte space called newline
	text1 db "Sum of even fibonacci number is equal to : ",0

section .bss
	sum resb 100

section .text
	global _start

_start:
	mov rax, 1
	mov rcx, 1
	call _fib_loop
	
	exit

_add_to_sum:
	mov rbx, 2
	mul rbx
	add [sum], rax

_fib_loop:
	; next fibonacci term
	mov rbx, rcx
	push rax
	add rax, rbx
	pop rcx

	; test if rax divisible by 2 (even)
	mov rbx, 2
	mov rdx, 0
	div rbx
	cmp rdx, 0
	je _add_to_sum	
	
	; reset rax
	push rdx
	mul rbx
	pop rdx
	add rax, rdx

	; test  if rax lt 4,000,000
	cmp rax, 4000000
	jl _fib_loop	
	
	; print sum of even terms of the fibonacci sequence below 4,000,000
	print text1
	printVal [sum]
	print newline
	ret

