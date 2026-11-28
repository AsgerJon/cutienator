"""
QtCbor::ByteData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtCbor::ByteData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QChar, QLatin1String


class ByteData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtCbor::ByteData: a plain Python object standing in
  front of one C++ QtCbor::ByteData.

  C++ hands a QtCbor::ByteData around as a copy, so every C++
  QtCbor::ByteData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtCbor::ByteData that has a ritual and that Python
  can call so far, 9 names in all: 'byte', 'utf16', 'toByteArray',
  'toString', 'toUtf8String', 'asByteArrayView', 'asLatin1', 'asStringView',
  'asQStringRaw'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QtCbor::ByteData::byte()': gives 'char', which has no cute
    class yet.
  - Qt's 'QChar *QtCbor::ByteData::utf16()': takes in Python what 'const
    QChar *QtCbor::ByteData::utf16() const' takes.
  - Qt's 'QUtf8StringView QtCbor::ByteData::asUtf8StringView() const': gives
    a type Python has no way to take yet.
  - Qt's 'QtCbor::ByteData::~ByteData()': the destructor: Python removes its
    C++ QtCbor::ByteData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtCbor::ByteData is created at the first use, not by
    'QtCbor::ByteData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtCbor::ByteData back gives a copy the ritual made
    for Python, in a new cute QtCbor::ByteData.
  - Each name of Qt's QtCbor::ByteData that has no cute function yet,
    'asUtf8StringView', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtCbor::ByteData'

  #  Qt's '~QtCbor::ByteData()'. Naming it makes this a value class: Python
  #  owns every C++ QtCbor::ByteData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN6QtCbor8ByteDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def byte(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QtCbor::ByteData::byte() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#byte

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtCbor::ByteData::byte() const
    chars = self.uglySide.call('ritual_ZNK6QtCbor8ByteData4byteEv')
    return None if chars is None else chars.decode()

  def utf16(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QtCbor::ByteData::utf16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#utf16

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QtCbor::ByteData::utf16() const
    address = self.uglySide.call('ritual_ZNK6QtCbor8ByteData5utf16Ev')
    from . import QChar
    return QChar._cuteAt(address)

  def toByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtCbor::ByteData::toByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#toByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtCbor::ByteData::toByteArray() const
    address = self.uglySide.call('ritual_ZNK6QtCbor8ByteData11toByteArrayEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QtCbor::ByteData::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtCbor::ByteData::toString() const
    return self.uglySide.call('ritual_ZNK6QtCbor8ByteData8toStringEv')

  def toUtf8String(self) -> str:
    """
    Calls Qt's 'QString QtCbor::ByteData::toUtf8String() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#toUtf8String

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtCbor::ByteData::toUtf8String() const
    return self.uglySide.call('ritual_ZNK6QtCbor8ByteData12toUtf8StringEv')

  def asByteArrayView(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtCbor::ByteData::asByteArrayView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcbor-bytedata.html#asByteArrayView

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtCbor::ByteData::asByteArrayView() const
    address = self.uglySide.call(
        'ritual_ZNK6QtCbor8ByteData15asByteArrayViewEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def asLatin1(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QtCbor::ByteData::asLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#asLatin1

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QtCbor::ByteData::asLatin1() const
    address = self.uglySide.call('ritual_ZNK6QtCbor8ByteData8asLatin1Ev')
    from . import QLatin1String
    return QLatin1String._cuteOwning(address)

  def asStringView(self) -> str:
    """
    Calls Qt's 'QStringView QtCbor::ByteData::asStringView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#asStringView

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QtCbor::ByteData::asStringView() const
    return self.uglySide.call('ritual_ZNK6QtCbor8ByteData12asStringViewEv')

  def asQStringRaw(self) -> str:
    """
    Calls Qt's 'QString QtCbor::ByteData::asQStringRaw() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-bytedata.html#asQStringRaw

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtCbor::ByteData::asQStringRaw() const
    return self.uglySide.call('ritual_ZNK6QtCbor8ByteData12asQStringRawEv')

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
  def asUtf8StringView(*__, **_) -> Never:
    """
    Qt's 'QUtf8StringView QtCbor::ByteData::asUtf8StringView() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtCbor.ByteData.asUtf8StringView' has no cute function yet. Qt's "
        "'QUtf8StringView QtCbor::ByteData::asUtf8StringView() const': "
        "gives a type Python has no way to take yet.")
