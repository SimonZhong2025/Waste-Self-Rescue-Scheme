assume cs:code

data segment
	db 'welcome to masm', '$'
data ends

code segment
start:
	mov ah,2  ;置光标
	mov ah,0  ;第0页
	mov dh,5  ;dh中放行号
	mov dl,12  ;dl中放列号
	int 10h
	
	mov ax,data
	mov ds,ax
	mov dx,0
	mov ah,9
	int 21h
	
	mov ah,4ch
	int 21h
code ends
end start