"""
QStringConverter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QStringConverterBase, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QStringConverter(QStringConverterBase):
  """
  The cute side of Qt's QStringConverter: a plain Python object standing in
  front of one C++ QStringConverter.

  It is built on the cute 'QStringConverterBase', as Qt's QStringConverter is
  built on Qt's QStringConverterBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStringConverter that has a ritual and that Python
  can call so far, 6 names in all: 'isValid', 'resetState', 'hasError',
  'name', 'nameForEncoding', 'availableCodecs'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  10 of the 16 functions Qt declares: 5 protected; 5 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QStringConverter is created at the first use, not by
    'QStringConverter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStringConverter.
  """

  #  The enums Qt writes inside QStringConverter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Encoding(CuteNum):
    """
    The enum 'QStringConverter::Encoding' of Qt, with the 10 names Qt gives
    in it.
    """

    Utf8 = Kee[int](0)
    Utf16 = Kee[int](1)
    Utf16LE = Kee[int](2)
    Utf16BE = Kee[int](3)
    Utf32 = Kee[int](4)
    Utf32LE = Kee[int](5)
    Utf32BE = Kee[int](6)
    Latin1 = Kee[int](7)
    System = Kee[int](8)
    LastEncoding = Kee[int](8)

  class FinalizeResultError(CuteNum, scoped=True):
    """
    The enum 'QStringConverter::FinalizeResultError' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NoError = Kee[int](0)
    InvalidCharacters = Kee[int](1)
    NotEnoughSpace = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Encoding)
  def nameForEncoding(e: Encoding) -> Optional[str]:
    """
    Calls Qt's 'const char *QStringConverter::nameForEncoding(Encoding e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringconverter.html#nameForEncoding

    Parameters
    ----------

    e : Encoding
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QStringConverter::nameForEncoding(Encoding e)
    chars = Rituals.call(
        'ritual_ZN16QStringConverter15nameForEncodingENS_8EncodingE',
        e.value,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def availableCodecs() -> QStringList:
    """
    Calls Qt's 'QStringList QStringConverter::availableCodecs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringconverter.html#availableCodecs

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QStringConverter::availableCodecs()
    address = Rituals.call('ritual_ZN16QStringConverter15availableCodecsEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringConverter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QStringConverter::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringconverter.html#isValid
    """
    #  bool QStringConverter::isValid() const
    return self.uglySide.call('ritual_ZNK16QStringConverter7isValidEv')

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QStringConverter::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringconverter.html#hasError
    """
    #  bool QStringConverter::hasError() const
    return self.uglySide.call('ritual_ZNK16QStringConverter8hasErrorEv')

  def name(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QStringConverter::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringconverter.html#name

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QStringConverter::name() const
    chars = self.uglySide.call('ritual_ZNK16QStringConverter4nameEv')
    return None if chars is None else chars.decode()

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

  def resetState(self) -> None:
    """
    Calls Qt's 'void QStringConverter::resetState()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringconverter.html#resetState
    """
    #  void QStringConverter::resetState()
    self.uglySide.call('ritual_ZN16QStringConverter10resetStateEv')
