%include "macro.asm"

section .data
	newline db 10,0

section .text
	global _start

_start:
	; 775147, sqrt of number to find
	mov rax, 775147 	; sqrt since it's faster
	call _isFactor

	exit

_isFactor:
	dec rax 	; decrement rax until it's the first prime factor of number

	; test if rax/big number
	push rax
	mov rbx, rax 	; this way we can divide the big number by rax and see if rax/big number
	mov rax, 600851475143
	mov rdx, 0
	div rbx
	
	pop rax
	cmp rdx, 0
	je _isPrime

	; if not prime then we repeat
	call _isFactor

	ret

_isPrime:
	mov rbx, 1 ; since we increment at start and first divisor must be 2

_isPrimeLoop:
	; test if rbx/rax (if rax has a divisor and is not a prime)
	push rax
	inc rbx 	; increment divisor
	mov rdx, 0
	div rbx

	; if it is divisible (not a prime) then we try number below
	pop rax
	cmp rdx, 0
	je _isFactor

	; test if rbx is equal to rax (if rax is a prime number)
	mov rcx, rbx 	; rbx can't be changed before subroutine call
	inc rcx 	; if rbx+1 = rax then loop is stopped
	cmp rcx, rax
	jl _isPrimeLoop	

	
	printVal rax
	print newline
	
	ret
