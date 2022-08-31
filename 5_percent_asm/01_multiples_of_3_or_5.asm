; this might be shit but it's my first assembly program

section .bss
	sum resb 100
	digitSpace resb 100
	digitSpacePos resb 8

section .data
	digit db 0,10

section .text
	global _start

%macro exit 0
	mov rax, 60
	mov rdi, 0
	syscall
%endmacro

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
	mov r8, rdx ; store rdx in another register
	mul rbx
	add rax, r8

	; test if rax divisible by 5
	mov rbx, 5
	mov rdx, 0
	div rbx
	cmp rdx, 0
	je _add_sum_5 ; add rax to sum if 5/rax	

	; reset rax
	mov r8, rdx
	mul rbx
	add rax, r8
	
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
	call _printRAX

	ret

_printRAXDigit:
	add rax, 48
	mov [digit], al
	mov rax, 1
	mov rdi, 1
	mov rsi, digit
	mov rdx, 2
	syscall 

	ret

_printRAX:
	mov rcx, digitSpace
	mov rbx, 10 ; new line character
	mov [rcx], rbx
	inc rcx ; next character after new line
	mov [digitSpacePos], rcx ; digitSpacePos is set to rcx

_printRAXLoop:
	mov rdx, 0 ; cancels the concatenation
	mov rbx, 10
	div rbx ; divide rax by 10
	push rax ; push number/10 on top of stack
	add rdx, 48 ; translate rdx into an ASCII number
	
	; increment digitSpacePos
	mov rcx, [digitSpacePos]
	mov [rcx], dl ; lower byte of rdx (character ASCII)
	inc rcx
	mov [digitSpacePos], rcx

	pop rax
	cmp rax, 0 ; tests if end of loop, quotient is 0 (last number)
	jne _printRAXLoop

; reverse the number
_printRAXLoop2:
	mov rcx, [digitSpacePos]
	mov rax, 1
	mov rdi, 1
	mov rsi, rcx
	mov rdx, 1
	syscall

	mov rcx, [digitSpacePos]
	dec rcx ; decrement rcx
	mov [digitSpacePos], rcx

	cmp rcx, digitSpace ; tests if at the beginning of number (done)
	jge _printRAXLoop2

	ret
