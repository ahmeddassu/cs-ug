; subtracts one

.equ SREG, 0x3f
.equ DDRB, 0x04
.equ PORTB, 0x05
.equ DDRC, 0x07
.equ PINC, 0x06

.org 0

main:
  ldi r16, 0
  out SREG, r16

  ldi r16, 0x0f
  out DDRB, r16
  
  ; same as portcadd in taking the input in
  ldi r16, 0xf0
  out DDRC, r16
  in r16, PINC

  ; subtracts one and displays it
  dec r16
  out PORTB, r16

mainloop:
  rjmp mainloop
