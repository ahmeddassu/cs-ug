; compares number and does smth
; genuinely forgot because im making the comments three weeks later

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

  ldi r16, 0xf0
  out DDRC, r16


  ; if the input is less than 8, add two
  in r16, PINC
  cpi r16, 8
  brlt add

; if the input is not less than 8, subtract one
sub:
  ldi r17, 1
  sub r16, r17
  out PORTB, r16

  rjmp mainloop


add:
  ldi r17, 2
  add r16, r17
  out PORTB, r16

  rjmp mainloop


mainloop: rjmp mainloop
