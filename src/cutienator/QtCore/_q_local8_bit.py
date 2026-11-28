"""
QLocal8Bit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLocal8Bit to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLocal8Bit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocal8Bit: a plain Python object standing in front
  of one C++ QLocal8Bit.

  C++ hands a QLocal8Bit around as a copy, so every C++ QLocal8Bit behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QLocal8Bit yet. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QLocal8Bit::convertToUnicode(QByteArrayView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
  - Qt's 'QByteArray QLocal8Bit::convertFromUnicode(QStringView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
  - Qt's 'QLocal8Bit::~QLocal8Bit()': the destructor: Python removes its C++
    QLocal8Bit by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLocal8Bit is created at the first use, not by 'QLocal8Bit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocal8Bit back gives a copy the ritual made for
    Python, in a new cute QLocal8Bit.
  - Each name of Qt's QLocal8Bit that has no cute function yet,
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
  __qt_class__ = 'QLocal8Bit'

  #  Qt's '~QLocal8Bit()'. Naming it makes this a value class: Python owns
  #  every C++ QLocal8Bit behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QLocal8BitD1Ev'

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
    Qt's 'QByteArray QLocal8Bit::convertFromUnicode(QStringView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QLocal8Bit.convertFromUnicode' has no cute function yet. Qt's "
        "'QByteArray QLocal8Bit::convertFromUnicode(QStringView in, "
        "QStringConverter::State *state)': names 'QStringConverter::State', "
        "which has no cute class yet.")

  @staticmethod
  def convertToUnicode(*__, **_) -> Never:
    """
    Qt's 'QString QLocal8Bit::convertToUnicode(QByteArrayView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QLocal8Bit.convertToUnicode' has no cute function yet. Qt's "
        "'QString QLocal8Bit::convertToUnicode(QByteArrayView in, "
        "QStringConverter::State *state)': names 'QStringConverter::State', "
        "which has no cute class yet.")
