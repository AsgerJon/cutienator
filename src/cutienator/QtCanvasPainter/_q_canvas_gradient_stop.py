"""
QCanvasGradientStop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasgradient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QCanvasGradientStop(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasGradientStop: a plain Python object standing
  in front of one C++ QCanvasGradientStop.

  C++ hands a QCanvasGradientStop around as a copy, so every C++
  QCanvasGradientStop behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasGradientStop that has a ritual and that
  Python can call so far, 3 names in all: '__eq__', '__ne__', '__rlshift__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasGradientStop
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasGradientStop &a1)':
    an operator between other classes, written inside this one.
  - Qt's 'QCanvasGradientStop::~QCanvasGradientStop()': the destructor:
    Python removes its C++ QCanvasGradientStop by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCanvasGradientStop is created at the first use, not by
    'QCanvasGradientStop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasGradientStop back gives a copy the ritual made
    for Python, in a new cute QCanvasGradientStop.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasGradientStop'

  #  Qt's '~QCanvasGradientStop()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasGradientStop behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCanvasGradientStopD1Ev'

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
  def __eq__(self, rhs: QCanvasGradientStop) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasGradientStop &lhs, const
    QCanvasGradientStop &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradientstop.html#operator==

    Parameters
    ----------

    rhs : QCanvasGradientStop
      Passed on as a value: Qt reads the C++ QCanvasGradientStop, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasGradientStop &lhs, const
    #      QCanvasGradientStop &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QCanvasGradientStopS1_',
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
  def __ne__(self, rhs: QCanvasGradientStop) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasGradientStop &lhs, const
    QCanvasGradientStop &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradientstop.html#operator!=

    Parameters
    ----------

    rhs : QCanvasGradientStop
      Passed on as a value: Qt reads the C++ QCanvasGradientStop, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasGradientStop &lhs, const
    #      QCanvasGradientStop &rhs)
    return Rituals.call(
        'ritual_ZneRK19QCanvasGradientStopS1_',
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

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QCanvasGradientStop
    &stop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradientstop.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QCanvasGradientStop &stop)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QCanvasGradientStop',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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


#  Qt's 'QList<QCanvasGradientStop>': the list of QCanvasGradientStop, which
#  'QList[QCanvasGradientStop]' gives. It is made here, so that there is one
#  as soon as there can be a QCanvasGradientStop. Qt has a name of its own
#  for it.
QCanvasGradientStops = QList.createKind(
    QCanvasGradientStop, 'value',
    name='QCanvasGradientStops',
    make='ritual_list_make_QCanvasGradientStop',
    add='ritual_list_add_QCanvasGradientStop',
    size='ritual_list_size_QCanvasGradientStop',
    at='ritual_list_at_QCanvasGradientStop',
    drop='ritual_list_drop_QCanvasGradientStop',
)
