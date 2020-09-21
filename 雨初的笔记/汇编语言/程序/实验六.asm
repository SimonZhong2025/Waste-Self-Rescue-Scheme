assume cs:code, ss:stacksg, ds:datasg

stacksg segment
		dw 0,0,0,0,0,0,0,0
stacksg ends

datasg segment
		db '1. display      '		;16个字节
		db '2. brows        '
		db '3. replace      '
		db '4. modify       '
datasg ends
	
code segment

start:	mov ax,stacksg
	mov ss,ax ;设定栈段
	
	mov ax,datasg
	mov ds,ax ;设定数据段
	
	mov bx,0
	mov cx,4
s:	push cx
	mov cx,4
	mov di,0
s1:	mov al,[bx+di+3]
	and al,11011111b
	mov [bx+di+3],al
	inc di
	loop s1
	
	pop cx
	add bx,10h
	loop s
	mov ah,4ch
	int 21h

code ends
end start