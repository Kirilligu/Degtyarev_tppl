section .data 
    x dd 5, 3, 2, 6, 1, 7, 4
    y dd 0, 10, 1, 9, 2, 8, 5
    len equ ($ - x) / 4
    result db "-", 0

section .bss
    sum resd 1
    avg resd 1

section .text
global _start
_start:
    xor rbx, rbx
    xor rax, rax
    mov rcx, len

.loop:
    mov edx, [x + rbx*4]
    sub edx, [y + rbx*4]
    add eax, edx
    inc rbx
    cmp rbx, rcx
    jl .loop
    mov [sum], eax
    mov eax, [sum]
    cdq
    idiv ecx
    cmp eax, 0
    jge .positive
    neg eax
    add eax, '0'
    mov [result + 1], al
    mov rdx, 2
    jmp .print

.positive:
    add eax, '0'
    mov [result], al
    mov rdx, 1

.print:
    mov rax, 1
    mov rdi, 1
    lea rsi, [result]
    syscall
    mov rax, 60
    xor rdi, rdi
    syscall
