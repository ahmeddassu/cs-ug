; displays 13 on a 4 bit led line

; instantiating registers and port b
.equ SREG, 0x3f
.equ PORTB, 0x05
.equ DDRB, 0x04

.org 0
main:	
		; clearing the register
		ldi r16, 0
		out SREG, r16

		; lower four pins as output
		ldi r16, 0x0f
		out DDRB, r16
        
        ; writing and displaying 13
        ldi r16, 13
		out PORTB, r16
		
mainloop:	rjmp mainloop
