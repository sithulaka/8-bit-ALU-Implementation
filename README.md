# 8-bit ALU Implementation in IoT

This project demonstrates the design and implementation of an 8-bit Arithmetic Logic Unit (ALU) using various IoT components. The ALU adds two 8-bit binary values and displays the result on seven-segment displays.

## Project Overview

This project is a blend of digital electronics and embedded systems, showcasing the potential of IoT in creating sophisticated digital systems. The main components include DIP switches for input, SN74LS83N Adder ICs for computation, logic level shifters for voltage compatibility, and a Raspberry Pi Pico for processing and display control.

## Features

- **Addition of Two 8-bit Binary Numbers:** Inputs are provided via DIP switches.
- **Real-Time Display:** Results are shown on three seven-segment displays.
- **Embedded Control:** Raspberry Pi Pico processes input and controls the display.
- **Voltage Level Shifting:** Ensures compatibility between different components.

## Components Used

- **Hardware:**
  - DIP switches
  - SN74LS83N Adder ICs
  - Logic level shifters
  - Raspberry Pi Pico
  - Seven-segment displays
  - Seven-segment decoder
  - NPN transistors
  - Resistors
  - LEDs

- **Software:**
  - Python for programming the Raspberry Pi Pico

## Project Files

- `alu.py`: Python code for converting 8-bit binary values to BCD and controlling the display.
- `circuit_diagram.brd`: BRD file for the circuit diagram.
- `components.csv`: CSV file listing all the components used.

## Circuit Diagram

Include an image of the circuit diagram here for quick reference.

## Installation and Usage

### Hardware Setup

1. **Circuit Design:**
   - Follow the circuit diagram provided in `circuit_diagram.brd`.

2. **Input Handling:**
   - Use pull-down resistors with DIP switches for stable input signals.
   - Connect two 4-bit adder ICs to form an 8-bit adder setup.

3. **Voltage Level Shifting:**
   - Convert the 8-bit output from the adder ICs (5V) to 3.3V using logic level shifters.

4. **Data Processing and Display:**
   - Connect the output to the Raspberry Pi Pico.
   - Wire the seven-segment displays to the decoder and control them using NPN transistors.

### Software Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/8-bit-ALU-Implementation.git
   cd 8-bit-ALU-Implementation
