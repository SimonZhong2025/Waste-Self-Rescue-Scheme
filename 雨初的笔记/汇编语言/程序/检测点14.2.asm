assume cs:code

code segment

start:
	mov ax,1
	mov bx,ax
	mov dx,ax
	shl bx,1
	mov cl,3
	shl dx,cl
	mov ax,bx
	add ax,dx
	
	mov ah,4ch
	int 21h

code ends
end start