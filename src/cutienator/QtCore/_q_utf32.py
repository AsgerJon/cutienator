"""
QUtf32 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUtf32 to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QUtf32(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUtf32: a plain Python object standing in front of
  one C++ QUtf32.

  C++ hands a QUtf32 around as a copy, so every C++ QUtf32 behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QUtf32 yet. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QUtf32::convertToUnicode(QByteArrayView a0,
    QStringConverter::State *a1, DataEndianness a2)': names
    'QStringConverter::State', which has no cute class yet.
  - Qt's 'QByteArray QUtf32::convertFromUnicode(QStringView a0,
    QStringConverter::State *a1, DataEndianness a2)': names
    'QStringConverter::State', which has no cute class yet.
  - Qt's 'QUtf32::~QUtf32()': the destructor: Python removes its C++ QUtf32
    by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QUtf32 is created at the first use, not by 'QUtf32(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUtf32 back gives a copy the ritual made for Python,
    in a new cute QUtf32.
  - Each name of Qt's QUtf32 that has no cute function yet,
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
  __qt_class__ = 'QUtf32'

  #  Qt's '~QUtf32()'. Naming it makes this a value class: Python owns every
  #  C++ QUtf32 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QUtf32D1Ev'

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
    - Qt's 'QByteArray QUtf32::convertFromUnicode(QStringView a0,
      QStringConverter::State *a1, DataEndianness a2)': names
      'QStringConverter::State', which has no cute class yet.
    - Qt's 'char *QUtf32::convertFromUnicode(char *out, QStringView in,
      QStringConverter::State *state, DataEndianness endian)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'HeaderDone'.
    """
    raise NotImplementedError(
        "'QUtf32.convertFromUnicode' has no cute function yet. Qt's "
        "'QByteArray QUtf32::convertFromUnicode(QStringView a0, "
        "QStringConverter::State *a1, DataEndianness a2)': names "
        "'QStringConverter::State', which has no cute class yet. Qt's 'char "
        "*QUtf32::convertFromUnicode(char *out, QStringView in, "
        "QStringConverter::State *state, DataEndianness endian)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'HeaderDone'.")

  @staticmethod
  def convertToUnicode(*__, **_) -> Never:
    """
    - Qt's 'QString QUtf32::convertToUnicode(QByteArrayView a0,
      QStringConverter::State *a1, DataEndianness a2)': names
      'QStringConverter::State', which has no cute class yet.
    - Qt's 'QChar *QUtf32::convertToUnicode(QChar *out, QByteArrayView a1,
      QStringConverter::State *state, DataEndianness endian)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'Data'; did you mean
      'QHashPrivate::Data'?.
    """
    raise NotImplementedError(
        "'QUtf32.convertToUnicode' has no cute function yet. Qt's 'QString "
        "QUtf32::convertToUnicode(QByteArrayView a0, "
        "QStringConverter::State *a1, DataEndianness a2)': names "
        "'QStringConverter::State', which has no cute class yet. Qt's "
        "'QChar *QUtf32::convertToUnicode(QChar *out, QByteArrayView a1, "
        "QStringConverter::State *state, DataEndianness endian)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'Data'; "
        "did you mean 'QHashPrivate::Data'?.")
