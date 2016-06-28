#!/usr/bin/env python

#Initialization

units		real
dimension	3
newton		on
boundary	p p p
atom_style	molecular

#Atom Definition
molecule 1 spce.lt
create_box 100 block
create_atoms 1 random

#Settings
output thermo

#Run
run



