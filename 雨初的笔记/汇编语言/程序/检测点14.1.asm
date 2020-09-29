assume cs:code

data segment
    db 'welcome to masm', '$'
data ends

code segment
start:
    mov al,2
    out 70h,al
    in al,71h

    mov ah,4ch
    int 21h
code ends
end start


assume cs:code

code segment

start:  mov al, 2   ; （al）=2 2号单元

        out 70h, al ; 将al送入端口70h，选中2号单元

      mov al, 0     ; （al）=0 写入端口的内容

      out 71h, al   ; 将（al）=0写入到71h端口的2号单元内。

        mov ax,4c00h

        int 21h

code ends

end start



