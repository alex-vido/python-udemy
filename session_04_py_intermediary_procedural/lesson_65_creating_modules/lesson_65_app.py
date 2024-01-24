# The running app is the __main__ app
# If I running this app, the app who is imported, be the name I gave to it.
import session_03_py_intermediary_procedural.lesson_65_creating_modules.lesson_65_math as lesson_65_math
from session_03_py_intermediary_procedural.lesson_65_creating_modules.lesson_65_other import speak_hello

lst = [2, 4]
print(lesson_65_math.multiply(lst))
speak_hello()
print(lesson_65_math.multiply([5, 2]))
