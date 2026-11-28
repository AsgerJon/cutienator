"""
QNdefNfcSizeRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNdefNfcSizeRecord to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QNdefRecord


class QNdefNfcSizeRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcSizeRecord: a plain Python object standing in
  front of one C++ QNdefNfcSizeRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcSizeRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcSizeRecord around as a copy, so every C++
  QNdefNfcSizeRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcSizeRecord that has a ritual and that Python
  can call so far, 2 names in all: 'setSize', 'size'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcSizeRecord::~QNdefNfcSizeRecord()': the destructor: Python
    removes its C++ QNdefNfcSizeRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcSizeRecord is created at the first use, not by
    'QNdefNfcSizeRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcSizeRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcSizeRecord.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcSizeRecord'

  #  Qt's '~QNdefNfcSizeRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcSizeRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QNdefNfcSizeRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QNdefNfcSizeRecord::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcsizerecord.html#size
    """
    #  quint32 QNdefNfcSizeRecord::size() const
    return self.uglySide.call('ritual_ZNK18QNdefNfcSizeRecord4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNdefNfcSizeRecord::setSize(quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcsizerecord.html#setSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNdefNfcSizeRecord::setSize(quint32 size)
    self.uglySide.call('ritual_ZN18QNdefNfcSizeRecord7setSizeEj', size)

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
    'QNdefNfcSizeRecord::QNdefNfcSizeRecord()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsizerecord.html#QNdefNfcSizeRecord
    """
    #  QNdefNfcSizeRecord::QNdefNfcSizeRecord()
    self._noteCreation(QNdefNfcSizeRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcSizeRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcSizeRecord::QNdefNfcSizeRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsizerecord.html#QNdefNfcSizeRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcSizeRecord::QNdefNfcSizeRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcSizeRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcSizeRecordC1ERK11QNdefRecord',
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
