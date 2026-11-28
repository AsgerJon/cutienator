"""
QNdefNfcTextRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefnfctextrecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QList
from . import QNdefRecord


class QNdefNfcTextRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcTextRecord: a plain Python object standing in
  front of one C++ QNdefNfcTextRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcTextRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcTextRecord around as a copy, so every C++
  QNdefNfcTextRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcTextRecord that has a ritual and that Python
  can call so far, 6 names in all: 'locale', 'setLocale', 'text', 'setText',
  'encoding', 'setEncoding'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcTextRecord::~QNdefNfcTextRecord()': the destructor: Python
    removes its C++ QNdefNfcTextRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcTextRecord is created at the first use, not by
    'QNdefNfcTextRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcTextRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcTextRecord.
  """

  #  The enums Qt writes inside QNdefNfcTextRecord, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Encoding(CuteNum):
    """
    The enum 'QNdefNfcTextRecord::Encoding' of Qt, with the 2 names Qt gives
    in it.
    """

    Utf8 = Kee[int](0)
    Utf16 = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcTextRecord'

  #  Qt's '~QNdefNfcTextRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcTextRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QNdefNfcTextRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def locale(self) -> str:
    """
    Calls Qt's 'QString QNdefNfcTextRecord::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctextrecord.html#locale

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNdefNfcTextRecord::locale() const
    return self.uglySide.call('ritual_ZNK18QNdefNfcTextRecord6localeEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QNdefNfcTextRecord::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctextrecord.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNdefNfcTextRecord::text() const
    return self.uglySide.call('ritual_ZNK18QNdefNfcTextRecord4textEv')

  def encoding(self) -> Encoding:
    """
    Calls Qt's 'Encoding QNdefNfcTextRecord::encoding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctextrecord.html#encoding

    Returns
    -------

    Encoding
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Encoding(number)' gives.
    """
    #  Encoding QNdefNfcTextRecord::encoding() const
    return QNdefNfcTextRecord.Encoding(self.uglySide.call(
        'ritual_ZNK18QNdefNfcTextRecord8encodingEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLocale(self, locale: str) -> None:
    """
    Calls Qt's 'void QNdefNfcTextRecord::setLocale(const QString &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctextrecord.html#setLocale

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNdefNfcTextRecord::setLocale(const QString &locale)
    self.uglySide.call(
        'ritual_ZN18QNdefNfcTextRecord9setLocaleERK7QString', locale,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QNdefNfcTextRecord::setText(const QString text)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctextrecord.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNdefNfcTextRecord::setText(const QString text)
    self.uglySide.call(
        'ritual_ZN18QNdefNfcTextRecord7setTextE7QString', text,
    )

  @overload(Encoding)
  def setEncoding(self, encoding: Encoding) -> None:
    """
    Calls Qt's 'void QNdefNfcTextRecord::setEncoding(Encoding encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctextrecord.html#setEncoding

    Parameters
    ----------

    encoding : Encoding
      Passed on as its number.
    """
    #  void QNdefNfcTextRecord::setEncoding(Encoding encoding)
    self.uglySide.call(
        'ritual_ZN18QNdefNfcTextRecord11setEncodingENS_8EncodingE',
        encoding.value,
    )

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
    Notes what was given, for Qt's
    'QNdefNfcTextRecord::QNdefNfcTextRecord()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctextrecord.html#QNdefNfcTextRecord
    """
    #  QNdefNfcTextRecord::QNdefNfcTextRecord()
    self._noteCreation(QNdefNfcTextRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcTextRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcTextRecord::QNdefNfcTextRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctextrecord.html#QNdefNfcTextRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcTextRecord::QNdefNfcTextRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcTextRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcTextRecordC1ERK11QNdefRecord',
        self._valueOf(other),
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


#  Qt's 'QList<QNdefNfcTextRecord>': the list of QNdefNfcTextRecord, which
#  'QList[QNdefNfcTextRecord]' gives. It is made here, so that there is one
#  as soon as there can be a QNdefNfcTextRecord.
QList.createKind(
    QNdefNfcTextRecord, 'value',
    make='ritual_list_make_QNdefNfcTextRecord',
    add='ritual_list_add_QNdefNfcTextRecord',
    size='ritual_list_size_QNdefNfcTextRecord',
    at='ritual_list_at_QNdefNfcTextRecord',
    drop='ritual_list_drop_QNdefNfcTextRecord',
)
