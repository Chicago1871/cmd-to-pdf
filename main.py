import textwrap
import sys
import os

from PIL import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from package import get_to
from package import get_from
from package import get_subject
from package import get_message
from package import make_date
from package import make_pdf

def clear(): os.system('cls') #on Windows System

clear()

print("\n--------\n")
print("* * * Welcome to python to PDF! * * * \n")
print("You will enter the following information:\n -TO:\n -FROM:\n -SUBJECT:\n -MESSAGE:")
print("\nAnd a nicely formatted PDF will be created for you!")
print("\n--------\n")

message_to = get_to.get_to()

clear()

print("\n--------\n")
print("Info So Far:")
print(f"   MESSAGE TO:  {message_to}")
print("\n--------\n")

message_from = get_from.get_from()

clear()

print("\n--------\n")
print("Info So Far:")
print(f"   MESSAGE TO:    {message_to}")
print(f"   MESSAGE FROM:  {message_from}")
print("\n--------\n")

message_subj = get_subject.get_subject()

clear()

print("\n--------\n")
print("Info So Far:")
print(f"   MESSAGE TO:    {message_to}")
print(f"   MESSAGE FROM:  {message_from}")
print(f"   MESSAGE SUBJ:  {message_subj}")
print("\n--------\n")

message_msg = get_message.get_message()

message_date = make_date.make_date()

make_pdf.make_pdf()

clear()

print("\n--------\n")
print("\n* * * Your Message has been saved to PDF * * *\n")
print(f"* * * {message_date} * * *\n\n")
print("Digital Receipt:")
print(f"   MESSAGE TO:    {message_to}")
print(f"   MESSAGE FROM:  {message_from}")
print(f"   MESSAGE SUBJ:  {message_subj}")
print(f"   MESSAGE BODY:  {message_msg}")
print("\n--------\n")