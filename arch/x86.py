#!/usr/bin/env
"""

File:           /arch/x86.py
Author:         Josh Kaplan
Email:          contact@joshkaplan.org
Description:    A class defining the x86 architecture.
Changelog:
"""
import unittest
from __init__ import BaseArchitecture
from __init__ import console
from __init__ import helpers


###############################################################################
# Processor Architecture
###############################################################################


class x86(BaseArchitecture):

    def __init__(self, addr=32):
        '''Initializes an x86 representation in it's state'''
        assert addr == 32, 'Invalid address size.'

        self._eax = 0
        self._ebx = 0
        self._ecx = 0
        self._edx = 0
        self._esi = 0
        self._edi = 0
        self._esp = 0
        self._ebp = 0


    @property
    def eax(self):
        '''Returns the value of the EAX register.'''
        return self._eax


    @eax.setter
    def eax(self, value):
        '''Sets the value of the EAX register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register EAX.')
        self._eax = value % 2**32


    @property
    def ax(self):
        pass


    @ax.setter
    def ax(self, value):
        pass


    @property
    def ah(self):
        pass


    @ah.setter
    def ah(self, value):
        pass


    @property
    def al(self):
        pass


    @al.setter
    def al(self, value):
        pass


    @property
    def ebx(self):
        '''Returns the value of the EBX register.'''
        return self._ebx


    @ebx.setter
    def ebx(self, value):
        '''Sets the value of the EBX register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register EBX.')
        self._ebx = value % 2**32


    @property
    def bx(self):
        pass


    @bx.setter
    def bx(self, value):
        pass


    @property
    def bh(self):
        pass


    @bh.setter
    def bh(self, value):
        pass


    @property
    def bl(self):
        pass


    @bl.setter
    def bl(self, value):
        pass


    @property
    def ecx(self):
        '''Returns the value of the ECX register.'''
        return self._ecx


    @ecx.setter
    def ecx(self, value):
        '''Sets the value of the ECX register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register ECX.')
        self._ecx = value % 2**32


    @property
    def cx(self):
        pass


    @cx.setter
    def cx(self, value):
        pass


    @property
    def ch(self):
        pass


    @ch.setter
    def ch(self, value):
        pass


    @property
    def cl(self):
        pass


    @cl.setter
    def cl(self, value):
        pass


    @property
    def edx(self):
        '''Returns the value of the EDX register.'''
        return self._edx


    @edx.setter
    def edx(self, value):
        '''Sets the value of the EDX register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register EAX.')
        self._edx = value % 2**32


    @property
    def dx(self):
        pass


    @dx.setter
    def dx(self, value):
        pass


    @property
    def dh(self):
        pass


    @dh.setter
    def dh(self, value):
        pass


    @property
    def dl(self):
        pass


    @dl.setter
    def dl(self, value):
        pass


    @property
    def esi(self):
        '''Returns the value of the ESI register.'''
        return self._esi


    @esi.setter
    def esi(self, value):
        '''Sets the value of the ESI register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register ESi.')
        self._esi = value % 2**32


    @property
    def edi(self):
        '''Returns the value of the EDI register.'''
        return self._edi


    @edi.setter
    def edi(self, value):
        '''Sets the value of the EDI register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register EDI.')
        self._edi = value % 2**32


    @property
    def esp(self):
        '''Returns the value of the ESP register.'''
        return self._esp


    @esp.setter
    def esp(self, value):
        '''Sets the value of the ESP register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register ESP.')
        self._esp = value % 2**32


    @property
    def ebp(self):
        '''Returns the value of the EBP resgister.'''
        return self._ebp


    @ebp.setter
    def ebp(self, value):
        '''Sets the value of the EBP register.'''
        if not (0 <= value < 2**32):
            console.warning('Overflow occured with register EBP.')
        self._ebp = value % 2**32


###############################################################################
# Instruction Set Architecture
###############################################################################
  

class x86InstructionSet(object):

    def __init__(self):
        # Yes, there's a reason for this. The ISA needs to be able to directly
        # manipulate the registers of the processor. Therefore, the processor
        # instance is a property of the instruction set. As for implementation,
        # the instruction set and the processor need to be separate classes due
        # to use of the hassattr and getattr built-ins.
        self.proc = x86()

    def mov(self, args):
        '''Takes two arguments, arg1 and arg2. Moves arg1 into arg2. The first 
        argument should be a valid register. The second can be another register
        or a constant.'''

        if len(args) != 2:
            raise x86SyntaxError('Invalid operands after mov command.')
        args = ''.join(args).split(',')
        arg1 = args[0].strip()
        arg2 = args[1].strip()

        # validate arg1 is a valid register
        if not hasattr(self.proc, arg1):
            raise x86SyntaxError('Invalid operand: %s' % (arg1))

        #arg1 = getattr(self.proc, arg1)
        #print arg1

        # check if arg2 is a register or a constant
        if hasattr(self.proc, arg2):
            arg2 = getattr(self.proc, arg2)
        # check if it's a valid constant
        elif helpers.is_constant(arg2):
            arg2 = helpers.resolve_constant(arg2)
        else:
            raise x86SyntaxError('Invalid operand: %s' % (arg2))

        # final error check
        if arg2 is None:
            raise x86SyntaxError('Invalid operand: %s' % (arg2))

        # move arg2 into arg1
        setattr(self.proc, arg1, arg2)



###############################################################################
# Interpreter
###############################################################################


class x86Interpreter():

    def __init__(self):
        # Processor
        self.InstructionSet = x86InstructionSet()
        
        # Interpreter
        while 1:
            try:
                # take input from user, ignoring comments, 
                # grab operation/command name
                cmd = raw_input('-> ')
                cmd = cmd.split(';')[0]
                cmd = cmd.split(' ')

                # check that processor has command
                # call operation with args or raise SyntaxError
                if hasattr(self.InstructionSet, cmd[0]):
                    getattr(self.InstructionSet, cmd[0])(cmd[1:])
                # providing a shortcut notation for printing register values
                elif hasattr(self.InstructionSet.proc, cmd[0]):
                    print getattr(self.InstructionSet.proc, cmd[0])
                else:
                    raise x86SyntaxError('Invalid command.')

            # Handles ctrl-c to exit interpreter
            # must hit ctrl-c twice
            except KeyboardInterrupt:
                try:
                    raw_input('Ctrl-c again to exit. ')
                except KeyboardInterrupt:
                    print 'Goodbye.'
                    break

            except x86SyntaxError as e:
                print 'x86SyntaxError: %s' % (e)


class x86SyntaxError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        

class Testx86(unittest.TestCase):

    def test_interpreter(self):
        x86Interpreter()


if __name__ == '__main__':
    x86Interpreter()
