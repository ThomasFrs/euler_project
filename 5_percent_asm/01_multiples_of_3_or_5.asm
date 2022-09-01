; this might be shit but it's my first assembly program
%include "macro.asm"

section .data
	newline db 10,0

section .bss
	sum resb 100

section .text
	global _start

_start:
	mov rax, 2
	call _loop

	exit

_loop:
	inc rax ; increase by 1 at each loop

	cmp rax, 1000
	je _printSum

	; test if rax divisible by 3
	mov rbx, 3
	mov rdx, 0
	div rbx
	cmp rdx, 0
	je _add_sum_3 ; add rax to sum if 3/rax
	
	; reset rax
	push rdx ; store rdx in another register
	mul rbx
	pop rdx
	add rax, rdx

	; test if rax divisible by 5
	mov rbx, 5
	mov rdx, 0
	div rbx
	cmp rdx, 0
	je _add_sum_5 ; add rax to sum if 5/rax	

	; reset rax
	push rdx
	mul rbx
	pop rdx
	add rax, rdx
	
	; test 
	call _loop

	ret 

_add_sum_3:
	mov rbx, 3
	mul rbx
	add [sum], rax ; add rax to sum
	call _loop

	ret	

_add_sum_5:
	mov rbx, 5
	mul rbx
	add [sum], rax
	call _loop

	ret
	

_printSum:
	mov rax, [sum]
	printVal rax
	print newline

	ret
