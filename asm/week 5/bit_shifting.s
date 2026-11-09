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

; continuously right shifts and left shifts the bits
; we can only use four bits of port B so we use the other four of port D
; port B acts as our lower nibble and port D acts as our upper nibble
main:
    ldi r16, 0x55
    out PORTB, r16
    out PORTD, r16
    rcall delay

    lsl r16
    out PORTB, r16
    out PORTD, r16
    rcall delay

    rjmp main


; similar delays as seen in week four
  ldi r20, 200
  ldi r21, 200
  ldi r22, 40

  delay:    ldi r22, 25
  outer:    ldi r21, 0
  middle:   ldi r20, 0

  inner:
    nop
    dec r20
    cpi r20, 0
    brne inner

    dec r21
    cpi r21, 0
    brne middle

    dec r22
    cpi r22, 0
    brne outer

    ret

mainloop: rjmp mainloop
