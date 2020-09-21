assume cs:code
code segment

s:	mov ax,cs
	mov ds,ax
	mov si,offset do0  ;设置ds:si指向源地址
	mov ax,0
	mov es,ax
	mov di,200h  ;设置es:di指向目的地址
	mov cx,offset do0end-offset do0
	cld
	rep movsb
	;这里设置中断向量表
	mov ax,0
	mov es,ax
	mov word ptr es:[0*4],200h
	mov word ptr es:[0 * 4 + 2],0
	
	mov ah,4ch
	int 21h
	
do0:jmp short do0start
	db "overflow!"
do0start:
	mov ax,cs
	mov ds,ax
	mov si,202h  ;设置ds:si指向字符串
	
	mov ax,0b800h
	mov es,ax
	mov di,12*160+36*2  ;设置es:di指向显存空间的中间位置
	
	mov cx,9
s0:
	mov al,[si]
	mov es:[di],al
	inc si
	add di,2
	loop s
	
	mov ah,4ch
	int 21h
do0end:nop
code ends
end s