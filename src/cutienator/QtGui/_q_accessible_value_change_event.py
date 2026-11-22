"""
QAccessibleValueChangeEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAccessibleEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleValueChangeEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleValueChangeEvent: a plain Python object
  standing in front of one C++ QAccessibleValueChangeEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleValueChangeEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleValueChangeEvent that has a ritual and
  that Python can call so far, 2 names in all: 'setValue', 'value'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleValueChangeEvent::~QAccessibleValueChangeEvent()': the
    destructor: Python never removes a C++ QAccessibleValueChangeEvent.

  What to expect
  --------------

  - The C++ QAccessibleValueChangeEvent is created at the first use, not by
    'QAccessibleValueChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleValueChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleValueChangeEvent'

  #  A C++ QAccessibleValueChangeEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleValueChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleValueChangeEvent::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevaluechangeevent.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleValueChangeEvent::value() const
    address = self.uglySide.call(
        'ritual_ZNK27QAccessibleValueChangeEvent5valueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, val: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleValueChangeEvent::setValue(const QVariant
    &val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevaluechangeevent.html#setValue

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleValueChangeEvent::setValue(const QVariant &val)
    self.uglySide.call(
        'ritual_ZN27QAccessibleValueChangeEvent8setValueERK8QVariant',
        self._valueOf(val),
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

  @overload(QObject, QVariant)
  @overload(NoneType, QVariant)
  def __init__(self, obj: Optional[QObject], val: QVariant) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QObject *obj,
    const QVariant &val)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevaluechangeevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QObject *obj,
    #      const QVariant &val)
    self._noteCreation(QAccessibleValueChangeEvent, lambda: Rituals.call(
        'ritual_ZN27QAccessibleValueChangeEventC1EP7QObjectRK8QVariant',
        self._addressOf(obj), self._valueOf(val),
    ))

  @overload(QAccessibleInterface, QVariant)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      val: QVariant,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(
    QAccessibleInterface *iface, const QVariant &val)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblevaluechangeevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(
    #      QAccessibleInterface *iface, const QVariant &val)
    self._noteCreation(QAccessibleValueChangeEvent, lambda: Rituals.call(
        'ritual_ZN27QAccessibleValueChangeEventC1EP20QAccessibleInterfaceRK'
        '8QVariant',
        self._addressOf(iface), self._valueOf(val),
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
