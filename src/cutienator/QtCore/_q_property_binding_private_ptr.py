"""
QPropertyBindingPrivatePtr binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QPropertyBindingPrivatePtr(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPropertyBindingPrivatePtr: a plain Python object
  standing in front of one C++ QPropertyBindingPrivatePtr.

  C++ hands a QPropertyBindingPrivatePtr around as a copy, so every C++
  QPropertyBindingPrivatePtr behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPropertyBindingPrivatePtr that has a ritual and
  that Python can call so far, 4 names in all: 'destroyAndFreeMemory',
  '__bool__', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyBindingPrivatePtr::~QPropertyBindingPrivatePtr()': the
    destructor: Python removes its C++ QPropertyBindingPrivatePtr by it, and
    has no other use for it.
  - Qt's 'bool QPropertyBindingPrivatePtr::operator!() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  24 of the 32 functions Qt declares: 24 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPropertyBindingPrivatePtr is created at the first use, not by
    'QPropertyBindingPrivatePtr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPropertyBindingPrivatePtr back gives a copy the
    ritual made for Python, in a new cute QPropertyBindingPrivatePtr.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyBindingPrivatePtr'

  #  Qt's '~QPropertyBindingPrivatePtr()'. Naming it makes this a value
  #  class: Python owns every C++ QPropertyBindingPrivatePtr behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QPropertyBindingPrivatePtrD1Ev'

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

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingPrivatePtr::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html#operator bool
    """
    #  bool QPropertyBindingPrivatePtr::operator bool() const
    return self.uglySide.call('ritual_ZNK26QPropertyBindingPrivatePtrcvbEv')

  @overload(THIS)
  def __eq__(self, rhs: QPropertyBindingPrivatePtr) -> bool:
    """
    Calls Qt's 'bool operator==(const QPropertyBindingPrivatePtr &lhs, const
    QPropertyBindingPrivatePtr &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html#operator==

    Parameters
    ----------

    rhs : QPropertyBindingPrivatePtr
      Passed on as a value: Qt reads the C++ QPropertyBindingPrivatePtr,
      which stays Python's own.
    """
    #  bool operator==(const QPropertyBindingPrivatePtr &lhs, const
    #      QPropertyBindingPrivatePtr &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QPropertyBindingPrivatePtrS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QPropertyBindingPrivatePtr) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPropertyBindingPrivatePtr &lhs, const
    QPropertyBindingPrivatePtr &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html#operator!=

    Parameters
    ----------

    rhs : QPropertyBindingPrivatePtr
      Passed on as a value: Qt reads the C++ QPropertyBindingPrivatePtr,
      which stays Python's own.
    """
    #  bool operator!=(const QPropertyBindingPrivatePtr &lhs, const
    #      QPropertyBindingPrivatePtr &rhs)
    return Rituals.call(
        'ritual_ZneRK26QPropertyBindingPrivatePtrS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's
    'QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html
    """
    #  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr()
    self._noteCreation(QPropertyBindingPrivatePtr, lambda: Rituals.call(
        'ritual_ZN26QPropertyBindingPrivatePtrC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QPropertyBindingPrivatePtr) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(const
    QPropertyBindingPrivatePtr &o)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html

    Parameters
    ----------

    o : QPropertyBindingPrivatePtr
      Passed on as a value: Qt reads the C++ QPropertyBindingPrivatePtr,
      which stays Python's own.
    """
    #  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(const
    #      QPropertyBindingPrivatePtr &o)
    self._noteCreation(QPropertyBindingPrivatePtr, lambda: Rituals.call(
        'ritual_ZN26QPropertyBindingPrivatePtrC1ERKS_', self._valueOf(o),
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

  def destroyAndFreeMemory(self) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivatePtr::destroyAndFreeMemory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivateptr.html
    """
    #  void QPropertyBindingPrivatePtr::destroyAndFreeMemory()
    self.uglySide.call(
        'ritual_ZN26QPropertyBindingPrivatePtr20destroyAndFreeMemoryEv',
    )
