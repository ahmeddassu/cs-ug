; add 2

.equ SREG, 0x3f
.equ DDRB, 0x04
.equ PORTB, 0x05
.equ DDRC, 0x07
.equ PINC, 0x06

.org 0
main:
; clears sreg
  ldi r16, 0
  out SREG, r16

  ; configures outputtable leds
  ldi r16, 0x0f
  out DDRB, r16


  ; takes input of the pins (if they are high volt or low volt)
  ; only the pins in the specified positions below
  ; and a high is a binary 1, low is binary 0
  ; and thats our number we add 2 to
  ldi r16, 0xf0
  out DDRC, r16
  in r16, PINC

  ; adds 2 and displays it
  ldi r17, 2
  add r16, r17

  out PORTB, r16

mainloop: rjmp mainloop
