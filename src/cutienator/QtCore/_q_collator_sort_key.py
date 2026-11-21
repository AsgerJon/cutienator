"""
QCollatorSortKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QCollatorSortKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCollatorSortKey: a plain Python object standing in
  front of one C++ QCollatorSortKey.

  C++ hands a QCollatorSortKey around as a copy, so every C++
  QCollatorSortKey behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCollatorSortKey that has a ritual and that Python
  can call so far, 1 name in all: 'compare'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCollatorSortKey::~QCollatorSortKey()': the destructor: Python
    removes its C++ QCollatorSortKey by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 9 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 forbidden; 1 protected.

  What to expect
  --------------

  - The C++ QCollatorSortKey is created at the first use, not by
    'QCollatorSortKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCollatorSortKey back gives a copy the ritual made
    for Python, in a new cute QCollatorSortKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCollatorSortKey'

  #  Qt's '~QCollatorSortKey()'. Naming it makes this a value class: Python
  #  owns every C++ QCollatorSortKey behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QCollatorSortKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def compare(self, key: QCollatorSortKey) -> int:
    """
    Calls Qt's 'int QCollatorSortKey::compare(const QCollatorSortKey &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#compare

    Parameters
    ----------

    key : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  int QCollatorSortKey::compare(const QCollatorSortKey &key) const
    return self.uglySide.call(
        'ritual_ZNK16QCollatorSortKey7compareERKS_', self._valueOf(key),
    )

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

  @overload(THIS)
  def __init__(self, other: QCollatorSortKey) -> None:
    """
    Notes what was given, for Qt's 'QCollatorSortKey::QCollatorSortKey(const
    QCollatorSortKey &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollatorsortkey.html#QCollatorSortKey

    Parameters
    ----------

    other : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  QCollatorSortKey::QCollatorSortKey(const QCollatorSortKey &other)
    self._noteCreation(QCollatorSortKey, lambda: Rituals.call(
        'ritual_ZN16QCollatorSortKeyC1ERKS_', self._valueOf(other),
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
