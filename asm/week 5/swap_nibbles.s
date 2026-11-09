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


ldi r16, 0x81 ; important value

ldi r29, 0x0f ; lower mask
ldi r30, 0xf0 ; upper mask

mov r25, r16 ; storing r16 elsewhere for lower nibble
and r25, r29

; shifts left four times
ldi r31, 4
left_shifter:
  lsl r25
  dec r31
  cpi r31, 0
  brne left_shifter


mov r26, r16 ; storing r16 elsewhere for upper nibble
and r26, r30

; shifts right four times
ldi r31, 4
right_shifter:
  lsr r26
  dec r31
  cpi r31, 0
  brne right_shifter


ldi r17, 0
mov r17, r26

; the final swapped nibble byte
or r17, r25

; repeatedly swap them with a delay of 0.5 seconds
main:
    out PORTB, r17
    out PORTD, r17
    rcall delay

    out PORTB, r16
    out PORTD, r16
    rcall delay

    rjmp main


; ig something cool is you can just descale now
; if you want 0.25 seconds then half one of the values
; or if you want 1 second then double a value
; or just do the maths and you essentially have
; 16 million clock cycles a second
; let x be the time i want
; let n be the number of operations needed
; and bare in mind we have 5 clock cycles in a loop


; x = n / 16,000,000
; n = 16,000,000x
; n = 16,000,000x / 5
; n = 3,200,000x
; then just find three numbers that multiply closest to n
; n1, n2, n3 = r20, r21, r22

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
