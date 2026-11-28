"""
QUtf8BaseTraits binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUtf8BaseTraits to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUtf8BaseTraits(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUtf8BaseTraits: a plain Python object standing in
  front of one C++ QUtf8BaseTraits.

  C++ hands a QUtf8BaseTraits around as a copy, so every C++ QUtf8BaseTraits
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUtf8BaseTraits that has a ritual and that Python
  can call so far, 2 names in all: 'peekByte', 'availableBytes'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'uchar QUtf8BaseTraits::peekByte(const uchar *ptr, qsizetype n)':
    names 'uchar', which has no cute class yet.
  - Qt's 'uchar QUtf8BaseTraits::peekByte(const qchar8_t *ptr, qsizetype n)':
    names 'qchar8_t', which has no cute class yet.
  - Qt's 'qptrdiff QUtf8BaseTraits::availableBytes(const uchar *ptr, const
    uchar *end)': names 'uchar', which has no cute class yet.
  - Qt's 'qptrdiff QUtf8BaseTraits::availableBytes(const qchar8_t *ptr, const
    qchar8_t *end)': names 'qchar8_t', which has no cute class yet.
  - Qt's 'char16_t QUtf8BaseTraits::peekUtf16(const char16_t *ptr, qsizetype
    n)': names 'char16_t', which has no cute class yet.
  - Qt's 'qptrdiff QUtf8BaseTraits::availableUtf16(const char16_t *ptr, const
    char16_t *end)': names 'char16_t', which has no cute class yet.
  - Qt's 'QUtf8BaseTraits::~QUtf8BaseTraits()': the destructor: Python
    removes its C++ QUtf8BaseTraits by it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 19 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QUtf8BaseTraits is created at the first use, not by
    'QUtf8BaseTraits(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUtf8BaseTraits back gives a copy the ritual made for
    Python, in a new cute QUtf8BaseTraits.
  - Each name of Qt's QUtf8BaseTraits that has no cute function yet,
    'advanceByte', 'advanceUtf16', 'appendByte', 'appendUcs4', 'appendUtf16',
    'availableUtf16', 'peekUtf16', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def peekByte(ptr: Optional[str], n: int = 0) -> int:
    """
    Calls Qt's 'uchar QUtf8BaseTraits::peekByte(const char *ptr, qsizetype
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qutf8basetraits.html#peekByte

    Parameters
    ----------

    ptr : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  uchar QUtf8BaseTraits::peekByte(const char *ptr, qsizetype n)
    return Rituals.call(
        'ritual_ZN15QUtf8BaseTraits8peekByteEPKcx',
        CuteMixin._bytesOf(ptr), n,
    )

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def availableBytes(ptr: Optional[str], end: Optional[str]) -> int:
    """
    Calls Qt's 'qptrdiff QUtf8BaseTraits::availableBytes(const char *ptr,
    const char *end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qutf8basetraits.html#availableBytes

    Parameters
    ----------

    ptr : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    end : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  qptrdiff QUtf8BaseTraits::availableBytes(const char *ptr, const char
    #      *end)
    return Rituals.call(
        'ritual_ZN15QUtf8BaseTraits14availableBytesEPKcS1_',
        CuteMixin._bytesOf(ptr), CuteMixin._bytesOf(end),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUtf8BaseTraits'

  #  Qt's '~QUtf8BaseTraits()'. Naming it makes this a value class: Python
  #  owns every C++ QUtf8BaseTraits behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QUtf8BaseTraitsD1Ev'

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
  def advanceByte(*__, **_) -> Never:
    """
    - Qt's 'void QUtf8BaseTraits::advanceByte(const char *&ptr, qsizetype
      n)': takes or gives a type that cannot be passed yet: const char *&.
    - Qt's 'void QUtf8BaseTraits::advanceByte(const uchar *&ptr, qsizetype
      n)': takes or gives a type that cannot be passed yet: const uchar *&.
    - Qt's 'void QUtf8BaseTraits::advanceByte(const qchar8_t *&ptr, qsizetype
      n)': takes or gives a type that cannot be passed yet: const qchar8_t
      *&.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.advanceByte' has no cute function yet. Qt's 'void "
        "QUtf8BaseTraits::advanceByte(const char *&ptr, qsizetype n)': "
        "takes or gives a type that cannot be passed yet: const char *&. "
        "Qt's 'void QUtf8BaseTraits::advanceByte(const uchar *&ptr, "
        "qsizetype n)': takes or gives a type that cannot be passed yet: "
        "const uchar *&. Qt's 'void QUtf8BaseTraits::advanceByte(const "
        "qchar8_t *&ptr, qsizetype n)': takes or gives a type that cannot "
        "be passed yet: const qchar8_t *&.")

  @staticmethod
  def advanceUtf16(*__, **_) -> Never:
    """
    Qt's 'void QUtf8BaseTraits::advanceUtf16(const char16_t *&ptr, qsizetype
    n)': takes or gives a type that cannot be passed yet: const char16_t *&.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.advanceUtf16' has no cute function yet. Qt's "
        "'void QUtf8BaseTraits::advanceUtf16(const char16_t *&ptr, "
        "qsizetype n)': takes or gives a type that cannot be passed yet: "
        "const char16_t *&.")

  @staticmethod
  def appendByte(*__, **_) -> Never:
    """
    - Qt's 'void QUtf8BaseTraits::appendByte(uchar *&ptr, uchar b)': takes or
      gives a type that cannot be passed yet: uchar *&.
    - Qt's 'void QUtf8BaseTraits::appendByte(qchar8_t *&ptr, qchar8_t b)':
      takes or gives a type that cannot be passed yet: qchar8_t *&.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.appendByte' has no cute function yet. Qt's 'void "
        "QUtf8BaseTraits::appendByte(uchar *&ptr, uchar b)': takes or gives "
        "a type that cannot be passed yet: uchar *&. Qt's 'void "
        "QUtf8BaseTraits::appendByte(qchar8_t *&ptr, qchar8_t b)': takes or "
        "gives a type that cannot be passed yet: qchar8_t *&.")

  @staticmethod
  def appendUcs4(*__, **_) -> Never:
    """
    - Qt's 'void QUtf8BaseTraits::appendUcs4(char16_t *&ptr, char32_t uc)':
      takes or gives a type that cannot be passed yet: char16_t *&.
    - Qt's 'void QUtf8BaseTraits::appendUcs4(char32_t *&ptr, char32_t uc)':
      takes or gives a type that cannot be passed yet: char32_t *&.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.appendUcs4' has no cute function yet. Qt's 'void "
        "QUtf8BaseTraits::appendUcs4(char16_t *&ptr, char32_t uc)': takes "
        "or gives a type that cannot be passed yet: char16_t *&. Qt's 'void "
        "QUtf8BaseTraits::appendUcs4(char32_t *&ptr, char32_t uc)': takes "
        "or gives a type that cannot be passed yet: char32_t *&.")

  @staticmethod
  def appendUtf16(*__, **_) -> Never:
    """
    - Qt's 'void QUtf8BaseTraits::appendUtf16(char16_t *&ptr, char16_t uc)':
      takes or gives a type that cannot be passed yet: char16_t *&.
    - Qt's 'void QUtf8BaseTraits::appendUtf16(char32_t *&ptr, char16_t uc)':
      takes or gives a type that cannot be passed yet: char32_t *&.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.appendUtf16' has no cute function yet. Qt's 'void "
        "QUtf8BaseTraits::appendUtf16(char16_t *&ptr, char16_t uc)': takes "
        "or gives a type that cannot be passed yet: char16_t *&. Qt's 'void "
        "QUtf8BaseTraits::appendUtf16(char32_t *&ptr, char16_t uc)': takes "
        "or gives a type that cannot be passed yet: char32_t *&.")

  @staticmethod
  def availableUtf16(*__, **_) -> Never:
    """
    Qt's 'qptrdiff QUtf8BaseTraits::availableUtf16(const char16_t *ptr, const
    char16_t *end)': names 'char16_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.availableUtf16' has no cute function yet. Qt's "
        "'qptrdiff QUtf8BaseTraits::availableUtf16(const char16_t *ptr, "
        "const char16_t *end)': names 'char16_t', which has no cute class "
        "yet.")

  @staticmethod
  def peekUtf16(*__, **_) -> Never:
    """
    Qt's 'char16_t QUtf8BaseTraits::peekUtf16(const char16_t *ptr, qsizetype
    n)': names 'char16_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QUtf8BaseTraits.peekUtf16' has no cute function yet. Qt's "
        "'char16_t QUtf8BaseTraits::peekUtf16(const char16_t *ptr, "
        "qsizetype n)': names 'char16_t', which has no cute class yet.")
