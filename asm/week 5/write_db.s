.equ PORTB, 0x05
.equ PORTD, 0x0b
.equ SREG,  0x3f
.equ DDRB,  0x04
.equ DDRD,  0x0a

.org 0


; clear status reg
ldi r16, 0
out SREG, r16

; pb3-0 as out
ldi r16, 0x0f
out DDRB, r16

; d7-4 as out
ldi r16, 0xf0
out DDRD, r16

; writes dc but should be db for the task but as 
; the bits are symmetric about the nybbles
; i wanted to see if i did it right, ie the msb is the led closest to my chip
ldi r16, 0xdc

; lower nibble
out PORTB, r16

; upper nibble
out PORTD, r16

mainloop: rjmp mainloop
