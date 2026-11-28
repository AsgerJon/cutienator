"""
QNdefNfcTypeRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNdefNfcTypeRecord to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QNdefRecord


class QNdefNfcTypeRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcTypeRecord: a plain Python object standing in
  front of one C++ QNdefNfcTypeRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcTypeRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcTypeRecord around as a copy, so every C++
  QNdefNfcTypeRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcTypeRecord that has a ritual and that Python
  can call so far, 2 names in all: 'setTypeInfo', 'typeInfo'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcTypeRecord::~QNdefNfcTypeRecord()': the destructor: Python
    removes its C++ QNdefNfcTypeRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcTypeRecord is created at the first use, not by
    'QNdefNfcTypeRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcTypeRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcTypeRecord.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcTypeRecord'

  #  Qt's '~QNdefNfcTypeRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcTypeRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QNdefNfcTypeRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeInfo(self) -> str:
    """
    Calls Qt's 'QString QNdefNfcTypeRecord::typeInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfctyperecord.html#typeInfo

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNdefNfcTypeRecord::typeInfo() const
    return self.uglySide.call('ritual_ZNK18QNdefNfcTypeRecord8typeInfoEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTypeInfo(self, type: str) -> None:
    """
    Calls Qt's 'void QNdefNfcTypeRecord::setTypeInfo(const QString &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctyperecord.html#setTypeInfo

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNdefNfcTypeRecord::setTypeInfo(const QString &type)
    self.uglySide.call(
        'ritual_ZN18QNdefNfcTypeRecord11setTypeInfoERK7QString', type,
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
    'QNdefNfcTypeRecord::QNdefNfcTypeRecord()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctyperecord.html#QNdefNfcTypeRecord
    """
    #  QNdefNfcTypeRecord::QNdefNfcTypeRecord()
    self._noteCreation(QNdefNfcTypeRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcTypeRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcTypeRecord::QNdefNfcTypeRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfctyperecord.html#QNdefNfcTypeRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcTypeRecord::QNdefNfcTypeRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcTypeRecord, lambda: Rituals.call(
        'ritual_ZN18QNdefNfcTypeRecordC1ERK11QNdefRecord',
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
