assume cs:code

datasg segment
	db 'BaSic'
	db 'iNfOr'
datasg ends

code segment 
	
start:	
	
	mov ax,datasg
	mov ds,ax
	
	xor bx,bx ;置0
	mov cx,5
	
s:	mov al,[bx]
	and al,11011111b
	mov [bx],al
	inc bx
	loop s
	
	mov bx,5
	mov cx,5
s0:	mov al,[bx]
	or al,00100000b
	mov [bx],al
	inc bx
	loop s0
	
	mov al,4ch
	int 21h

code ends
end start