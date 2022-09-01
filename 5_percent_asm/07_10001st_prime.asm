%include "macro.asm"

section .data
	newline db 10,0

section .bss
	count resb 8

section .text
	global _start

_start:
	mov rax, 1 ; first number to start with
	mov rcx, [count]
	inc rcx
	mov [count], rcx ; set count 1

	call _loop

	printVal rax
	print newline

	exit

_loop:
	inc rax ; increase rax until n-th prime is found
	call _isPrime

	ret

_isPrime:
	mov rbx, 1 ; reset the first divisor

_isPrimeLoop:
	; test if rax divisible by rbx (not prime)
	push rax
	inc rbx
	mov rdx, 0
	div rbx

	pop rax
	cmp rdx, 0
	je _loop ; increase number since not prime

	; test if rbx+1 divisor = rax (then rax is prime)
	mov rcx, rbx
	inc rcx
	cmp rcx, rax
	jl _isPrimeLoop

	; increment count of prime and verify if equal to n-th prime
	mov rcx, [count]
	inc rcx
	mov [count], rcx	
	cmp rcx, 10001
	jl _loop

	ret	
