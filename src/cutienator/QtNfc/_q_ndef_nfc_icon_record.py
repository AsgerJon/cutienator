"""
QNdefNfcIconRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefnfcsmartposterrecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QNdefRecord

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QNdefNfcIconRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcIconRecord: a plain Python object standing in
  front of one C++ QNdefNfcIconRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcIconRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcIconRecord around as a copy, so every C++
  QNdefNfcIconRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcIconRecord that has a ritual and that Python
  can call so far, 2 names in all: 'setData', 'data'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcIconRecord::~QNdefNfcIconRecord()': the destructor: Python
    removes its C++ QNdefNfcIconRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcIconRecord is created at the first use, not by
    'QNdefNfcIconRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcIconRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcIconRecord.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcIconRecord'

  #  Qt's '~QNdefNfcIconRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcIconRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QNdefNfcIconRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefNfcIconRecord::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfciconrecord.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefNfcIconRecord::data() const
    address = self.uglySide.call('ritual_ZNK18QNdefNfcIconRecord4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefNfcIconRecord::setData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfciconrecord.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefNfcIconRecord::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QNdefNfcIconRecord7setDataERK10QByteArray',
        self._valueOf(data),
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
    'QNdefNfcIconRecord::QNdefNfcIconRecord()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfciconrecord.html#QNdefNfcIconRecord
    """
    #  QNdefNfcIconRecord::QNdefNfcIconRecord()
    self._noteCreation(QNdefNfcIconRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcIconRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcIconRecord::QNdefNfcIconRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfciconrecord.html#QNdefNfcIconRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcIconRecord::QNdefNfcIconRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcIconRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcIconRecordC1ERK11QNdefRecord',
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


#  Qt's 'QList<QNdefNfcIconRecord>': the list of QNdefNfcIconRecord, which
#  'QList[QNdefNfcIconRecord]' gives. It is made here, so that there is one
#  as soon as there can be a QNdefNfcIconRecord.
QList.createKind(
    QNdefNfcIconRecord, 'value',
    make='ritual_list_make_QNdefNfcIconRecord',
    add='ritual_list_add_QNdefNfcIconRecord',
    size='ritual_list_size_QNdefNfcIconRecord',
    at='ritual_list_at_QNdefNfcIconRecord',
    drop='ritual_list_drop_QNdefNfcIconRecord',
)
