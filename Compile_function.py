#COMPILE ()::
# The compile() function returns the specified source as a code object, ready to be executed.
#Syntax :: compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

print( "Examples using_compile()")
print('Example_1: Compile text as code, :')
x = compile('print(55)', 'test', 'eval')
exec(x)
print("")

print('Example_2:Compile more than one statement :')
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
print("")

print('Example_3:multiply two variables')

srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'
# Converting above source code to an executable
execCode = compile(srcCode, 'mulstring', 'exec')
# Running the executable code.
exec(execCode)
print("")

print('Example_4: Compile text as code, :')
x = compile('print(10)', 'abc', 'eval')
exec(x)
print("")

print('Example_5: Compile() with eval(), :')
x = 50
a = compile('x == 50', '', 'eval')
print(eval(a))

