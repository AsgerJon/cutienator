"""
QLatin1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLatin1 to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLatin1(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLatin1: a plain Python object standing in front of
  one C++ QLatin1.

  C++ hands a QLatin1 around as a copy, so every C++ QLatin1 behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QLatin1 yet. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QLatin1::convertFromUnicode(char *out, QStringView in,
    QStringConverter::State *state)': names 'char', which has no cute class
    yet.
  - Qt's 'char *QLatin1::convertFromUnicode(char *out, QStringView in)':
    names 'char', which has no cute class yet.
  - Qt's 'QLatin1::~QLatin1()': the destructor: Python removes its C++
    QLatin1 by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 2 leans on 'qt_from_latin1(char16_t*,
  char const*, unsigned long)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QLatin1 is created at the first use, not by 'QLatin1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLatin1 back gives a copy the ritual made for Python,
    in a new cute QLatin1.
  - Each name of Qt's QLatin1 that has no cute function yet,
    'convertFromUnicode', 'convertToUnicode', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLatin1'

  #  Qt's '~QLatin1()'. Naming it makes this a value class: Python owns every
  #  C++ QLatin1 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QLatin1D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def convertFromUnicode(*__, **_) -> Never:
    """
    - Qt's 'char *QLatin1::convertFromUnicode(char *out, QStringView in,
      QStringConverter::State *state)': names 'char', which has no cute class
      yet.
    - Qt's 'char *QLatin1::convertFromUnicode(char *out, QStringView in)':
      names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QLatin1.convertFromUnicode' has no cute function yet. Qt's 'char "
        "*QLatin1::convertFromUnicode(char *out, QStringView in, "
        "QStringConverter::State *state)': names 'char', which has no cute "
        "class yet. Qt's 'char *QLatin1::convertFromUnicode(char *out, "
        "QStringView in)': names 'char', which has no cute class yet.")

  @staticmethod
  def convertToUnicode(*__, **_) -> Never:
    """
    - Qt's 'char16_t *QLatin1::convertToUnicode(char16_t *dst,
      QLatin1StringView in)': takes or gives a type that cannot be passed
      yet: char16_t *.
    - Qt's 'QChar *QLatin1::convertToUnicode(QChar *buffer, QLatin1StringView
      in)': leans on 'qt_from_latin1(char16_t*, char const*, unsigned long)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QChar *QLatin1::convertToUnicode(QChar *dst, QByteArrayView in,
      QStringConverter::State *state)': leans on 'qt_from_latin1(char16_t*,
      char const*, unsigned long)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLatin1.convertToUnicode' has no cute function yet. Qt's "
        "'char16_t *QLatin1::convertToUnicode(char16_t *dst, "
        "QLatin1StringView in)': takes or gives a type that cannot be "
        "passed yet: char16_t *. Qt's 'QChar "
        "*QLatin1::convertToUnicode(QChar *buffer, QLatin1StringView in)': "
        "leans on 'qt_from_latin1(char16_t*, char const*, unsigned long)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'QChar "
        "*QLatin1::convertToUnicode(QChar *dst, QByteArrayView in, "
        "QStringConverter::State *state)': leans on "
        "'qt_from_latin1(char16_t*, char const*, unsigned long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
