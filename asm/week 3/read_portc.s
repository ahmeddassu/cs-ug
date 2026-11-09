; reads the value of all port c pins dependent on voltage (resistor placement on the hi or lo)

.equ SREG, 0x3f
.equ DDRB, 0x04
.equ PORTB, 0x05
.equ DDRC, 0x07
.equ PINC, 0x06

.org 0
main:
  ldi r16, 0
  out SREG, r16

  ; config output pins
  ldi r16, 0x0f
  out DDRB, r16

  ; config input pins
  ldi r16, 0xf0
  out DDRC, r16

  ; takes in pinc and outputs on led row
  in r16, PINC
  out PORTB, r16

mainloop: rjmp mainloop
