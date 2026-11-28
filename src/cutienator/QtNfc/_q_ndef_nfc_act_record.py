"""
QNdefNfcActRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNdefNfcActRecord to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QNdefNfcSmartPosterRecord, QNdefRecord


class QNdefNfcActRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcActRecord: a plain Python object standing in
  front of one C++ QNdefNfcActRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcActRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcActRecord around as a copy, so every C++
  QNdefNfcActRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcActRecord that has a ritual and that Python
  can call so far, 2 names in all: 'setAction', 'action'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcActRecord::~QNdefNfcActRecord()': the destructor: Python
    removes its C++ QNdefNfcActRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcActRecord is created at the first use, not by
    'QNdefNfcActRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcActRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcActRecord.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcActRecord'

  #  Qt's '~QNdefNfcActRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcActRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QNdefNfcActRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def action(self) -> QNdefNfcSmartPosterRecord.Action:
    """
    Calls Qt's 'QNdefNfcSmartPosterRecord::Action QNdefNfcActRecord::action()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcactrecord.html#action

    Returns
    -------

    QNdefNfcSmartPosterRecord.Action
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNdefNfcSmartPosterRecord.Action(number)' gives.
    """
    #  QNdefNfcSmartPosterRecord::Action QNdefNfcActRecord::action() const
    return QNdefNfcSmartPosterRecord.Action(self.uglySide.call(
        'ritual_ZNK17QNdefNfcActRecord6actionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNdefNfcSmartPosterRecord.Action)
  def setAction(self, action: QNdefNfcSmartPosterRecord.Action) -> None:
    """
    Calls Qt's 'void
    QNdefNfcActRecord::setAction(QNdefNfcSmartPosterRecord::Action action)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcactrecord.html#setAction

    Parameters
    ----------

    action : QNdefNfcSmartPosterRecord.Action
      Passed on as its number.
    """
    #  void QNdefNfcActRecord::setAction(QNdefNfcSmartPosterRecord::Action
    #      action)
    self.uglySide.call(
        'ritual_ZN17QNdefNfcActRecord9setActionEN25QNdefNfcSmartPosterRecor'
        'd6ActionE',
        action.value,
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
    Notes what was given, for Qt's 'QNdefNfcActRecord::QNdefNfcActRecord()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcactrecord.html#QNdefNfcActRecord
    """
    #  QNdefNfcActRecord::QNdefNfcActRecord()
    self._noteCreation(QNdefNfcActRecord, lambda: Rituals.call(
        'ritual_ZN17QNdefNfcActRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcActRecord::QNdefNfcActRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcactrecord.html#QNdefNfcActRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcActRecord::QNdefNfcActRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcActRecord, lambda: Rituals.call(
        'ritual_ZN17QNdefNfcActRecordC1ERK11QNdefRecord',
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
