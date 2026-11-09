; turns on the led

; instantiating registers and port b
.equ SREG, 0x3f
.equ PORTB, 0x05
.equ DDRB, 0x04

.org 0
main:	
		; clearing the register
		ldi r16, 0
		out SREG, r16

		; setting pin 5 to high
		ldi r16, 0x20
		out DDRB, r16
		out PORTB, r16
		
mainloop:	rjmp mainloop
