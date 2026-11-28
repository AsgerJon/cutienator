"""
QAccessibleValueInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

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


class QAccessibleValueInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleValueInterface: a plain Python object
  standing in front of one C++ QAccessibleValueInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleValueInterface that has a ritual and that
  Python can call so far, 5 names in all: 'currentValue', 'setCurrentValue',
  'maximumValue', 'minimumValue', 'minimumStepSize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleValueInterface::~QAccessibleValueInterface()': the
    destructor: Python never removes a C++ QAccessibleValueInterface.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleValueInterface is created at the first use, not by
    'QAccessibleValueInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleValueInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleValueInterface'

  #  A C++ QAccessibleValueInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleValueInterface'

  #  The functions Qt calls itself that QAccessibleValueInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'currentValue': (
          ('_ZNK25QAccessibleValueInterface12currentValueEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'setCurrentValue': (
          ('_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'maximumValue': (
          ('_ZNK25QAccessibleValueInterface12maximumValueEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'minimumValue': (
          ('_ZNK25QAccessibleValueInterface12minimumValueEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'minimumStepSize': (
          ('_ZNK25QAccessibleValueInterface15minimumStepSizeEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleValueInterface::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleValueInterface::currentValue() const
    address = self._callAs(
        'QAccessibleValueInterface',
        'ritual_ZNK25QAccessibleValueInterface12currentValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleValueInterface::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleValueInterface::maximumValue() const
    address = self._callAs(
        'QAccessibleValueInterface',
        'ritual_ZNK25QAccessibleValueInterface12maximumValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleValueInterface::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleValueInterface::minimumValue() const
    address = self._callAs(
        'QAccessibleValueInterface',
        'ritual_ZNK25QAccessibleValueInterface12minimumValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleValueInterface::minimumStepSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleValueInterface::minimumStepSize() const
    address = self._callAs(
        'QAccessibleValueInterface',
        'ritual_ZNK25QAccessibleValueInterface15minimumStepSizeEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleValueInterface::setCurrentValue(const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleValueInterface::setCurrentValue(const QVariant &value)
    self._callAs(
        'QAccessibleValueInterface',
        'ritual_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant',
        self._valueOf(value),
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
    'QAccessibleValueInterface::QAccessibleValueInterface()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevalueinterface.html
    """
    #  QAccessibleValueInterface::QAccessibleValueInterface()
    self._noteCreation(QAccessibleValueInterface, lambda: Rituals.call(
        'ritual_ZN25QAccessibleValueInterfaceC1Ev',
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
