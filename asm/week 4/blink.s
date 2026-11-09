.equ SREG, 0x3f
.equ PORTB, 0x05
.equ DDRB, 0x01


ldi r16, 0x00
out SREG, r16

ldi r16, 0x01
out DDRB, r16

main:
  ldi r16, 0x01
  out PORTB, r16

  rcall delay

  ldi r16, 0x00
  out PORTB, r16

  rcall delay
  rjmp main


; an approximate 0.5 second gap
; 16MHz is clock speed, so 1/16,000,000 clock cycles a second
; NOP runs at 1 clock cycle 
; so we just need 8 million clock cycles
; nop is one cycle, dec is one cycle, brne is two cycles and brne not taken is one cycle. thats five cycles a loop
; so 8 million / 5 is 1.6 million, so the nested loops should achieve a number near 1.6 million, a few thousand over is negligible
; each register is an 8 bit register which is why we use nested loops as 1.6 million is quite a bit larger than 255 which is the maximum 8 bit usize
; so 200x200x40 = 1.6 million
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


mainloop:	rjmp mainloop
