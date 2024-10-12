section .data
    number dd 455
    guess dd 100
    new_guess dd 0
    buffer db '0', 0
    newline db 10

section .text
global _start

print:
    mov rax, 1
    mov rdi, 1
    mov rsi, rsi
    mov rdx, rdx
    syscall
    ret

dprint:
    mov rdi, buffer
    mov rbx, 10
    xor rcx, rcx

    xor rdx, rdx
convert:
    xor rdx, rdx
    div rbx
    add dl, '0'
    dec rdi
    mov [rdi], dl
    inc rcx
    test eax, eax
    jnz convert

    mov rsi, rdi
    mov rdx, rcx
    call print

    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall

    ret

_start:
    mov dword [guess], 100

sqrt_loop:
    mov eax, dword [number]
    mov ebx, dword [guess]
    xor edx, edx
    div ebx
    add eax, ebx
    shr eax, 1
    mov dword [new_guess], eax

    cmp eax, dword [guess]
    jz done

    mov dword [guess], eax
    jmp sqrt_loop

done:
    mov eax, dword [guess]
    call dprint

    mov rax, 60
    xor rdi, rdi
    syscall
