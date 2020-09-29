delay:
	push ax
	push dx
	
	mov dx,10h  ;循环100000h次
	mov ax,0
s1:	sub ax,1
	sbb dx,0
	cmp ax,0
	jne s1
	cmp dx, 0
	jne s1
	
	pop dx
	pop ax
	ret