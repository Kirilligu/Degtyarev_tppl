section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    y dd 0, 10, 1, 9, 2, 8, 5
    n dd 7                                          ;кол-во элементов в массиве
    format db 'Result program: %d', 0xA, 0

section .text
    extern ExitProcess
    extern printf                                   ;вывод
    global main                                     ;точка входа

main:
    xor eax, eax                                    ;обнуление
    mov ecx, [n]                                    ;кол-во элементов
    mov ebx, 0

.loop:
    cmp ebx, ecx
    jge .average
    add eax, [x + ebx*4]                            ;добавляем
    sub eax, [y + ebx*4]                            ;вычитаем
    inc ebx                                         ;увел индекс
    jmp .loop

.average:
    cdq
    idiv dword [n]                                  ;сумма/кол-во

    push eax
    push dword format                               ;помещаем на стек
    call printf                                     ;вывод
    add esp, 8                                      ;очищаем стек

    xor ebx, ebx
    push ebx
    call ExitProcess
