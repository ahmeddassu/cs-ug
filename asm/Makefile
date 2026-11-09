# assembling
%.o: %.s # converts the .s file to .o, $@ is the generated file and $< is the inputted file
	avr-as -g -mmcu=atmega328p -o $@ $<

# linking
%.elf: %.o # converts .o file to .elf hohoho
	avr-ld -o $@ $<

# converting the .elf to hex
%.hex: %.elf
	avr-objcopy -O ihex -R .eeprom $< $@

# flashes the program to chip
flash-%: %.hex
	avrdude -C /etc/avrdude.conf -p atmega328p -c arduino -P /dev/ttyUSB0 -D -U flash:w:$<:i

# removes all the silly files made
clean-%:
	rm -f $*.o
	rm -f $*.elf
	rm -f $*.hex

# builds, flashes then cleans
cycle-%:
	$(MAKE) $*
	$(MAKE) flash-$*
	$(MAKE) clean-$*