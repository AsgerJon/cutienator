"""
QHashDummyValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qhash.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QHashDummyValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHashDummyValue: a plain Python object standing in
  front of one C++ QHashDummyValue.

  C++ hands a QHashDummyValue around as a copy, so every C++ QHashDummyValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHashDummyValue that has a ritual and that Python
  can call so far, 2 names in all: '__eq__', '__ne__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHashDummyValue::~QHashDummyValue()': the destructor: Python
    removes its C++ QHashDummyValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHashDummyValue is created at the first use, not by
    'QHashDummyValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHashDummyValue back gives a copy the ritual made for
    Python, in a new cute QHashDummyValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHashDummyValue'

  #  Qt's '~QHashDummyValue()'. Naming it makes this a value class: Python
  #  owns every C++ QHashDummyValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QHashDummyValueD1Ev'

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
  def __eq__(self, a1: QHashDummyValue) -> bool:
    """
    Calls Qt's 'bool operator==(QHashDummyValue a0, QHashDummyValue a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashdummyvalue.html#operator==

    Parameters
    ----------

    a1 : QHashDummyValue
      Passed on as a value: Qt reads the C++ QHashDummyValue, which stays
      Python's own.
    """
    #  bool operator==(QHashDummyValue a0, QHashDummyValue a1)
    return Rituals.call(
        'ritual_Zeq15QHashDummyValueS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, a1: QHashDummyValue) -> bool:
    """
    Calls Qt's 'bool operator!=(QHashDummyValue a0, QHashDummyValue a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashdummyvalue.html#operator!=

    Parameters
    ----------

    a1 : QHashDummyValue
      Passed on as a value: Qt reads the C++ QHashDummyValue, which stays
      Python's own.
    """
    #  bool operator!=(QHashDummyValue a0, QHashDummyValue a1)
    return Rituals.call(
        'ritual_Zne15QHashDummyValueS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QHashDummyValue::QHashDummyValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashdummyvalue.html#QHashDummyValue
    """
    #  QHashDummyValue::QHashDummyValue()
    self._noteCreation(QHashDummyValue, lambda: Rituals.call(
        'ritual_ZN15QHashDummyValueC1Ev',
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
