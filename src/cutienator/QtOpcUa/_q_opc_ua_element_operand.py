"""
QOpcUaElementOperand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaelementoperand.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaElementOperand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaElementOperand: a plain Python object standing
  in front of one C++ QOpcUaElementOperand.

  C++ hands a QOpcUaElementOperand around as a copy, so every C++
  QOpcUaElementOperand behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaElementOperand that has a ritual and that
  Python can call so far, 4 names in all: 'index', 'setIndex', '__eq__',
  '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaElementOperand &QOpcUaElementOperand::operator=(const
    QOpcUaElementOperand &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaElementOperand::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaElementOperand::~QOpcUaElementOperand()': the destructor:
    Python removes its C++ QOpcUaElementOperand by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaElementOperand is created at the first use, not by
    'QOpcUaElementOperand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaElementOperand back gives a copy the ritual
    made for Python, in a new cute QOpcUaElementOperand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaElementOperand'

  #  Qt's '~QOpcUaElementOperand()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaElementOperand behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaElementOperandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def index(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaElementOperand::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaelementoperand.html#index
    """
    #  quint32 QOpcUaElementOperand::index() const
    return self.uglySide.call('ritual_ZNK20QOpcUaElementOperand5indexEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QOpcUaElementOperand::setIndex(quint32 index)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaelementoperand.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpcUaElementOperand::setIndex(quint32 index)
    self.uglySide.call('ritual_ZN20QOpcUaElementOperand8setIndexEj', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaElementOperand) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaElementOperand &lhs, const
    QOpcUaElementOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaelementoperand.html#operator==

    Parameters
    ----------

    rhs : QOpcUaElementOperand
      Passed on as a value: Qt reads the C++ QOpcUaElementOperand, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaElementOperand &lhs, const
    #      QOpcUaElementOperand &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpcUaElementOperandS1_',
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
  def __ne__(self, rhs: QOpcUaElementOperand) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaElementOperand &lhs, const
    QOpcUaElementOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaelementoperand.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaElementOperand
      Passed on as a value: Qt reads the C++ QOpcUaElementOperand, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaElementOperand &lhs, const
    #      QOpcUaElementOperand &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpcUaElementOperandS1_',
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
    'QOpcUaElementOperand::QOpcUaElementOperand()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaelementoperand.html#QOpcUaElementOperand
    """
    #  QOpcUaElementOperand::QOpcUaElementOperand()
    self._noteCreation(QOpcUaElementOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaElementOperandC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaElementOperand) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaElementOperand::QOpcUaElementOperand(const QOpcUaElementOperand
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaelementoperand.html#QOpcUaElementOperand

    Parameters
    ----------

    a0 : QOpcUaElementOperand
      Passed on as a value: Qt reads the C++ QOpcUaElementOperand, which
      stays Python's own.
    """
    #  QOpcUaElementOperand::QOpcUaElementOperand(const QOpcUaElementOperand
    #      &a0)
    self._noteCreation(QOpcUaElementOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaElementOperandC1ERKS_', self._valueOf(a0),
    ))

  @overload(int)
  def __init__(self, index: int) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaElementOperand::QOpcUaElementOperand(quint32 index)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaelementoperand.html#QOpcUaElementOperand

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  QOpcUaElementOperand::QOpcUaElementOperand(quint32 index)
    self._noteCreation(QOpcUaElementOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaElementOperandC1Ej', index,
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
