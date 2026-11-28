"""
QStandardItemData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStandardItemData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QStandardItemData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStandardItemData: a plain Python object standing in
  front of one C++ QStandardItemData.

  C++ hands a QStandardItemData around as a copy, so every C++
  QStandardItemData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStandardItemData that has a ritual and that Python
  can call so far, 1 name in all: '__eq__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStandardItemData::QStandardItemData(const std::pair<const int &,
    const QVariant &> &p)': takes a type Python has no way to hand over yet.
  - Qt's 'QStandardItemData::~QStandardItemData()': the destructor: Python
    removes its C++ QStandardItemData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStandardItemData is created at the first use, not by
    'QStandardItemData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStandardItemData back gives a copy the ritual made
    for Python, in a new cute QStandardItemData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStandardItemData'

  #  Qt's '~QStandardItemData()'. Naming it makes this a value class: Python
  #  owns every C++ QStandardItemData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QStandardItemDataD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QStandardItemData) -> bool:
    """
    Calls Qt's 'bool QStandardItemData::operator==(const QStandardItemData
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemdata.html#operator==

    Parameters
    ----------

    other : QStandardItemData
      Passed on as a value: Qt reads the C++ QStandardItemData, which stays
      Python's own.
    """
    #  bool QStandardItemData::operator==(const QStandardItemData &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QStandardItemDataeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStandardItemData::QStandardItemData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemdata.html#QStandardItemData
    """
    #  QStandardItemData::QStandardItemData()
    self._noteCreation(QStandardItemData, lambda: Rituals.call(
        'ritual_ZN17QStandardItemDataC1Ev',
    ))

  @overload(int, QVariant)
  def __init__(self, r: int, v: QVariant) -> None:
    """
    Notes what was given, for Qt's 'QStandardItemData::QStandardItemData(int
    r, const QVariant &v)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemdata.html#QStandardItemData

    Parameters
    ----------

    r : int
      Passed on as it is.

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QStandardItemData::QStandardItemData(int r, const QVariant &v)
    self._noteCreation(QStandardItemData, lambda: Rituals.call(
        'ritual_ZN17QStandardItemDataC1EiRK8QVariant', r, self._valueOf(v),
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
