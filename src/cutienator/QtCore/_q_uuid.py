"""
QUuid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/quuid.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSysInfoEndian, QUuidStringFormat, QUuidVariant, QUuidVersion

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArray, QByteArrayView, QSysInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']


class QUuid(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUuid: a plain Python object standing in front of one
  C++ QUuid.

  C++ hands a QUuid around as a copy, so every C++ QUuid behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUuid that has a ritual and that Python can call so
  far, 9 names in all: 'fromString', 'toString', 'toByteArray', 'toRfc4122',
  'fromRfc4122', 'createUuid', 'createUuidV5', 'createUuidV3',
  'createUuidV7'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUuid::QUuid(Id128Bytes id128, QSysInfo::Endian order)': names
    'QUuid::Id128Bytes', which has no cute class yet.
  - Qt's 'Id128Bytes QUuid::toBytes(QSysInfo::Endian order) const': gives
    'QUuid::Id128Bytes', which has no cute class yet.
  - Qt's 'bool QUuid::isNull(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.
  - Qt's 'Variant QUuid::variant(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.
  - Qt's 'Version QUuid::version(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.
  - Qt's 'QUuid::~QUuid()': the destructor: Python removes its C++ QUuid by
    it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 24 functions Qt declares: 3 private; 2 a template; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QUuid is created at the first use, not by 'QUuid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUuid back gives a copy the ritual made for Python,
    in a new cute QUuid.
  """

  #  The enums Qt writes inside QUuid, and the names Qt has for the
  #  combinations of its flags enums.
  StringFormat = QUuidStringFormat
  Variant = QUuidVariant
  Version = QUuidVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromString(string: str) -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::fromString(QAnyStringView string)'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::fromString(QAnyStringView string)
    address = Rituals.call(
        'ritual_ZN5QUuid10fromStringE14QAnyStringView', string,
    )
    return QUuid._cuteOwning(address)

  @staticmethod
  @overload(QByteArrayView)
  def fromRfc4122(a0: QByteArrayView) -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::fromRfc4122(QByteArrayView a0)'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#fromRfc4122

    Parameters
    ----------

    a0 : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::fromRfc4122(QByteArrayView a0)
    address = Rituals.call(
        'ritual_ZN5QUuid11fromRfc4122E14QByteArrayView',
        CuteMixin._valueOf(a0),
    )
    return QUuid._cuteOwning(address)

  @staticmethod
  def createUuid() -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::createUuid()'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#createUuid

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::createUuid()
    address = Rituals.call('ritual_ZN5QUuid10createUuidEv')
    return QUuid._cuteOwning(address)

  @staticmethod
  @overload(THIS, QByteArrayView)
  def createUuidV5(ns: QUuid, baseData: QByteArrayView) -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::createUuidV5(QUuid ns, QByteArrayView
    baseData)'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#createUuidV5

    Parameters
    ----------

    ns : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.

    baseData : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::createUuidV5(QUuid ns, QByteArrayView baseData)
    address = Rituals.call(
        'ritual_ZN5QUuid12createUuidV5ES_14QByteArrayView',
        CuteMixin._valueOf(ns), CuteMixin._valueOf(baseData),
    )
    return QUuid._cuteOwning(address)

  @staticmethod
  @overload(THIS, QByteArrayView)
  def createUuidV3(ns: QUuid, baseData: QByteArrayView) -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::createUuidV3(QUuid ns, QByteArrayView
    baseData)'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#createUuidV3

    Parameters
    ----------

    ns : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.

    baseData : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::createUuidV3(QUuid ns, QByteArrayView baseData)
    address = Rituals.call(
        'ritual_ZN5QUuid12createUuidV3ES_14QByteArrayView',
        CuteMixin._valueOf(ns), CuteMixin._valueOf(baseData),
    )
    return QUuid._cuteOwning(address)

  @staticmethod
  def createUuidV7() -> QUuid:
    """
    Calls Qt's 'QUuid QUuid::createUuidV7()'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#createUuidV7

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QUuid::createUuidV7()
    address = Rituals.call('ritual_ZN5QUuid12createUuidV7Ev')
    return QUuid._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUuid'

  #  Qt's '~QUuid()'. Naming it makes this a value class: Python owns every
  #  C++ QUuid behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QUuidD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(StringFormat)
  def toString(self, mode: StringFormat = StringFormat.WithBraces) -> str:
    """
    Calls Qt's 'QString QUuid::toString(StringFormat mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#toString

    Parameters
    ----------

    mode : StringFormat
      Passed on as its number. May be left out, as in Qt: it is then
      StringFormat.WithBraces.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUuid::toString(StringFormat mode) const
    return self.uglySide.call(
        'ritual_ZNK5QUuid8toStringENS_12StringFormatE', mode.value,
    )

  @overload()
  @overload(StringFormat)
  def toByteArray(
      self,
      mode: StringFormat = StringFormat.WithBraces,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUuid::toByteArray(StringFormat mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#toByteArray

    Parameters
    ----------

    mode : StringFormat
      Passed on as its number. May be left out, as in Qt: it is then
      StringFormat.WithBraces.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUuid::toByteArray(StringFormat mode) const
    address = self.uglySide.call(
        'ritual_ZNK5QUuid11toByteArrayENS_12StringFormatE', mode.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toRfc4122(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUuid::toRfc4122() const'.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#toRfc4122

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUuid::toRfc4122() const
    address = self.uglySide.call('ritual_ZNK5QUuid9toRfc4122Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QUuid::QUuid()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#QUuid
    """
    #  QUuid::QUuid()
    self._noteCreation(QUuid, lambda: Rituals.call('ritual_ZN5QUuidC1Ev'))

  @overload(int, int, int, int, int, int, int, int, int, int, int)
  def __init__(
      self,
      l: int,
      w1: int,
      w2: int,
      b1: int,
      b2: int,
      b3: int,
      b4: int,
      b5: int,
      b6: int,
      b7: int,
      b8: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QUuid::QUuid(uint l, ushort w1, ushort
    w2, uchar b1, uchar b2, uchar b3, uchar b4, uchar b5, uchar b6, uchar b7,
    uchar b8)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#QUuid

    Parameters
    ----------

    l : int
      Passed on as it is.

    w1 : int
      Passed on as it is.

    w2 : int
      Passed on as it is.

    b1 : int
      Passed on as it is.

    b2 : int
      Passed on as it is.

    b3 : int
      Passed on as it is.

    b4 : int
      Passed on as it is.

    b5 : int
      Passed on as it is.

    b6 : int
      Passed on as it is.

    b7 : int
      Passed on as it is.

    b8 : int
      Passed on as it is.
    """
    #  QUuid::QUuid(uint l, ushort w1, ushort w2, uchar b1, uchar b2, uchar
    #      b3, uchar b4, uchar b5, uchar b6, uchar b7, uchar b8)
    self._noteCreation(QUuid, lambda: Rituals.call(
        'ritual_ZN5QUuidC1Ejtthhhhhhhh',
        l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8,
    ))

  @overload(str)
  def __init__(self, string: str) -> None:
    """
    Notes what was given, for Qt's 'QUuid::QUuid(QAnyStringView string)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/quuid.html#QUuid

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QUuid::QUuid(QAnyStringView string)
    self._noteCreation(QUuid, lambda: Rituals.call(
        'ritual_ZN5QUuidC1E14QAnyStringView', string,
    ))

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
