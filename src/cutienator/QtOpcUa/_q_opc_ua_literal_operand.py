"""
QOpcUaLiteralOperand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcualiteraloperand.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QOpcUaLiteralOperand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaLiteralOperand: a plain Python object standing
  in front of one C++ QOpcUaLiteralOperand.

  C++ hands a QOpcUaLiteralOperand around as a copy, so every C++
  QOpcUaLiteralOperand behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaLiteralOperand that has a ritual and that
  Python can call so far, 6 names in all: 'value', 'setValue', 'type',
  'setType', '__eq__', '__ne__'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaLiteralOperand &QOpcUaLiteralOperand::operator=(const
    QOpcUaLiteralOperand &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaLiteralOperand::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaLiteralOperand::~QOpcUaLiteralOperand()': the destructor:
    Python removes its C++ QOpcUaLiteralOperand by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaLiteralOperand is created at the first use, not by
    'QOpcUaLiteralOperand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaLiteralOperand back gives a copy the ritual
    made for Python, in a new cute QOpcUaLiteralOperand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaLiteralOperand'

  #  Qt's '~QOpcUaLiteralOperand()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaLiteralOperand behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaLiteralOperandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaLiteralOperand::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualiteraloperand.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaLiteralOperand::value() const
    address = self.uglySide.call('ritual_ZNK20QOpcUaLiteralOperand5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> QOpcUa.Types:
    """
    Calls Qt's 'QOpcUa::Types QOpcUaLiteralOperand::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualiteraloperand.html#type

    Returns
    -------

    QOpcUa.Types
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.Types(number)'
      gives.
    """
    #  QOpcUa::Types QOpcUaLiteralOperand::type() const
    return QOpcUa.Types(self.uglySide.call(
        'ritual_ZNK20QOpcUaLiteralOperand4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaLiteralOperand::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualiteraloperand.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaLiteralOperand::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN20QOpcUaLiteralOperand8setValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(QOpcUa.Types)
  def setType(self, type: QOpcUa.Types) -> None:
    """
    Calls Qt's 'void QOpcUaLiteralOperand::setType(QOpcUa::Types type)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualiteraloperand.html#setType

    Parameters
    ----------

    type : QOpcUa.Types
      Passed on as its number.
    """
    #  void QOpcUaLiteralOperand::setType(QOpcUa::Types type)
    self.uglySide.call(
        'ritual_ZN20QOpcUaLiteralOperand7setTypeEN6QOpcUa5TypesE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaLiteralOperand) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaLiteralOperand &lhs, const
    QOpcUaLiteralOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualiteraloperand.html#operator==

    Parameters
    ----------

    rhs : QOpcUaLiteralOperand
      Passed on as a value: Qt reads the C++ QOpcUaLiteralOperand, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaLiteralOperand &lhs, const
    #      QOpcUaLiteralOperand &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpcUaLiteralOperandS1_',
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
  def __ne__(self, rhs: QOpcUaLiteralOperand) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaLiteralOperand &lhs, const
    QOpcUaLiteralOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualiteraloperand.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaLiteralOperand
      Passed on as a value: Qt reads the C++ QOpcUaLiteralOperand, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaLiteralOperand &lhs, const
    #      QOpcUaLiteralOperand &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpcUaLiteralOperandS1_',
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
    'QOpcUaLiteralOperand::QOpcUaLiteralOperand()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualiteraloperand.html#QOpcUaLiteralOperand
    """
    #  QOpcUaLiteralOperand::QOpcUaLiteralOperand()
    self._noteCreation(QOpcUaLiteralOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaLiteralOperandC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaLiteralOperand) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QOpcUaLiteralOperand
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualiteraloperand.html#QOpcUaLiteralOperand

    Parameters
    ----------

    a0 : QOpcUaLiteralOperand
      Passed on as a value: Qt reads the C++ QOpcUaLiteralOperand, which
      stays Python's own.
    """
    #  QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QOpcUaLiteralOperand
    #      &a0)
    self._noteCreation(QOpcUaLiteralOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaLiteralOperandC1ERKS_', self._valueOf(a0),
    ))

  @overload(QVariant)
  @overload(QVariant, QOpcUa.Types)
  def __init__(
      self,
      value: QVariant,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QVariant &value,
    QOpcUa::Types type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualiteraloperand.html#QOpcUaLiteralOperand

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.
    """
    #  QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QVariant &value,
    #      QOpcUa::Types type)
    self._noteCreation(QOpcUaLiteralOperand, lambda: Rituals.call(
        'ritual_ZN20QOpcUaLiteralOperandC1ERK8QVariantN6QOpcUa5TypesE',
        self._valueOf(value), type.value,
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
