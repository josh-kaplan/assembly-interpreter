#!/usr/bin/env
"""

File:           /arch/x86.py
Author:         Josh Kaplan
Email:          contact@joshkaplan.org

Description:    A software definition of the x86 architecture.

TODO:
    - Add support for memory and addressing
    - Add ability for interpretor to handle labels (for branching)

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
        '''Returns the value of the AX register.'''
        return self._eax >> 16


    @ax.setter
    def ax(self, value):
        '''Sets the value of the AX register.'''
        if value > 0xFFFF:
            raise x86SyntaxError('Register AX cannot accept a value greater than 16 bits')
        self._eax = ((self._eax << 16) >> 16) | (value << 16)


    @property
    def ah(self):
        '''Returns the value of the AH register.'''
        return (self._eax >> 8) & 0xFF


    @ah.setter
    def ah(self, value):
        '''Sets the value of the AH register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register AH cannot accept a value greater than 8 bits')
        self._eax = (self._eax & 0xFFFF00FF) | (value << 8)


    @property
    def al(self):
        '''Returns the value of the AL register.'''
        return self._eax & 0xFF


    @al.setter
    def al(self, value):
        '''Sets the value of the AL register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register AL cannot accept a value greater than 8 bits')
        self._eax = ((self._eax >> 8) << 8 )| value


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
        '''Returns the value of the BX register.'''
        return self._ebx >> 16


    @bx.setter
    def bx(self, value):
        '''Sets the value of the BX register.'''
        if value > 0xFFFF:
            raise x86SyntaxError('Register BX cannot accept a value greater than 16 bits')
        self._ebx = ((self._ebx << 16) >> 16) | (value << 16)


    @property
    def bh(self):
        '''Returns the value of the BH register.'''
        return (self._ebx >> 8) & 0xFF


    @bh.setter
    def bh(self, value):
        '''Sets the value of the BH register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register BH cannot accept a value greater than 8 bits')
        self._ebx = (self._ebx & 0xFFFF00FF) | (value << 8)


    @property
    def bl(self):
        '''Returns the value of the BL register.'''
        return self._ebx & 0xFF


    @bl.setter
    def bl(self, value):
        '''Sets the value of the BL register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register BL cannot accept a value greater than 8 bits')
        self._ebx = ((self._ebx >> 8) << 8 )| value


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
        '''Returns the value of the CX register.'''
        return self._ecx >> 16


    @cx.setter
    def cx(self, value):
        '''Sets the value of the CX register.'''
        if value > 0xFFFF:
            raise x86SyntaxError('Register CX cannot accept a value greater than 16 bits')
        self._ecx = ((self._ecx << 16) >> 16) | (value << 16)


    @property
    def ch(self):
        '''Returns the value of the CH register.'''
        return (self._ecx >> 8) & 0xFF


    @ch.setter
    def ch(self, value):
        '''Sets the value of the CH register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register CH cannot accept a value greater than 8 bits')
        self._ecx = (self._ecx & 0xFFFF00FF) | (value << 8)


    @property
    def cl(self):
        '''Returns the value of the CL register.'''
        return self._ecx & 0xFF


    @cl.setter
    def cl(self, value):
        '''Sets the value of the CL register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register CL cannot accept a value greater than 8 bits')
        self._ecx = ((self._ecx >> 8) << 8 )| value


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
        '''Returns the value of the DX register.'''
        return self._edx >> 16


    @dx.setter
    def dx(self, value):
        '''Sets the value of the DX register.'''
        if value > 0xFFFF:
            raise x86SyntaxError('Register DX cannot accept a value greater than 16 bits')
        self._edx = ((self._edx << 16) >> 16) | (value << 16)


    @property
    def dh(self):
        '''Returns the value of the DH register.'''
        return (self._edx >> 8) & 0xFF


    @dh.setter
    def dh(self, value):
        '''Sets the value of the DH register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register DH cannot accept a value greater than 8 bits')
        self._edx = (self._edx & 0xFFFF00FF) | (value << 8)


    @property
    def dl(self):
        '''Returns the value of the DL register.'''
        return self._edx & 0xFF


    @dl.setter
    def dl(self, value):
        '''Sets the value of the DL register.'''
        if value > 0xFF:
            raise x86SyntaxError('Register DL cannot accept a value greater than 8 bits')
        self._edx = ((self._edx >> 8) << 8 )| value


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


    def int(self, args):
        '''Handles/implements system calls based on current register 
        contents. For now, the following calls are supported:

            - sys_exit
            - sys_fork      => Not implemented
            - sys_read      => Not implemented
            - sys_write     => Doesn't support files other than 1
        '''
        arg = helpers.resolve_constant(args)
        if arg != 0x80:
            raise x86SyntaxError('Unknown argument for int: % s' % (arg))

        # sys_exit
        if self.eax == 1:
            # call exit
            pass
        # sys_fork
        elif self.eax == 2:
            raise x86SyntaxError('Sorry, sys_fork not supported.')
        # sys_read
        elif self.eax == 3:
            raise x86SyntaxError('Sorry, sys_read not supported.')
        # sys_write
        elif self.eax == 4:
            # unsigned int fd, const char * buf, size_t count
            if self.ebx != 1:
                x86SyntaxError('Sorry, sys_write only supports stdout.')
            buf = self.ecx



###############################################################################
# Interpreter
###############################################################################


class x86Interpreter():

    def __init__(self):
        # Processor
        self.InstructionSet = x86InstructionSet()
        # Stack - see note below
        self.stack = list()
        
        # Interpreter
        while 1:
            try:
                # take input from user, ignoring comments, 
                # grab operation/command name
                cmd = raw_input('0x{:08X}    '.format(len(self.stack)*4))
                cmd = cmd.split(';')[0]
                cmd = cmd.strip().split(' ')

                # check that processor has command
                # call operation with args or raise SyntaxError
                if hasattr(self.InstructionSet, cmd[0]):
                    # NOTE: Not really sure how I want to handle the stack, 
                    # but I'm gonna do it like this for now so I can at least
                    # use the addresses as the interpreter prompt.
                    # This will almost definitely change. This also might give
                    # me just enough to start figuring out how I want to 
                    # handle labels.
                    self.stack.append(' '.join(cmd))
                    
                    # call the command
                    getattr(self.InstructionSet, cmd[0])(cmd[1:])

                # providing a shortcut notation for printing register values
                elif hasattr(self.InstructionSet.proc, cmd[0]):
                    print getattr(self.InstructionSet.proc, cmd[0])

                # if not a valid (ISA or custom) command, raise SyntaxError
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
