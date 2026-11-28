"""
QAbstractAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qabstractaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QAbstractAxis, QGraphsView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphsView = WAIT['QGraphsView']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAxisPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractAxisPrivate: a plain Python object standing
  in front of one C++ QAbstractAxisPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstractAxisPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAxisPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'setGraph', 'setMin', 'setMax',
  'setRange', 'min', 'max', 'handleRangeChanged', 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractAxisPrivate::~QAbstractAxisPrivate()': the destructor:
    Python never removes a C++ QAbstractAxisPrivate.
  - Qt's 'const QAbstractAxis *QAbstractAxisPrivate::q_func() const': takes
    in Python what 'QAbstractAxis *QAbstractAxisPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAbstractAxisPrivate is created at the first use, not by
    'QAbstractAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAxisPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAbstractAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractAxisPrivate'

  #  The functions Qt calls itself that QAbstractAxisPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setMin': (
          ('_ZN20QAbstractAxisPrivate6setMinERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setMax': (
          ('_ZN20QAbstractAxisPrivate6setMaxERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setRange': (
          ('_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
          ('_ZN20QAbstractAxisPrivate8setRangeEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'min': (
          ('_ZN20QAbstractAxisPrivate3minEv',
           ('double', 'number', ''),
           ()),
      ),
      'max': (
          ('_ZN20QAbstractAxisPrivate3maxEv',
           ('double', 'number', ''),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphsView)
  @overload(NoneType)
  def setGraph(self, graph: Optional[QGraphsView]) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setGraph(QGraphsView *graph)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setGraph

    Parameters
    ----------

    graph : Optional[QGraphsView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractAxisPrivate::setGraph(QGraphsView *graph)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8setGraphEP11QGraphsView',
        self._addressOf(graph),
    )

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setMin(const QVariant &min)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate6setMinERK8QVariant',
        self._valueOf(min),
    )

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setMax(const QVariant &max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate6setMaxERK8QVariant',
        self._valueOf(max),
    )

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8setRangeEdd', min, max,
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
    'QAbstractAxisPrivate::QAbstractAxisPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#QAbstractAxisPrivate
    """
    #  QAbstractAxisPrivate::QAbstractAxisPrivate()
    self._noteCreation(QAbstractAxisPrivate, lambda: Rituals.call(
        'ritual_ZN20QAbstractAxisPrivateC1Ev',
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

  def min(self) -> float:
    """
    Calls Qt's 'qreal QAbstractAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#min
    """
    #  qreal QAbstractAxisPrivate::min()
    return self.uglySide.call('ritual_ZN20QAbstractAxisPrivate3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QAbstractAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#max
    """
    #  qreal QAbstractAxisPrivate::max()
    return self.uglySide.call('ritual_ZN20QAbstractAxisPrivate3maxEv')

  @overload(float, float)
  def handleRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::handleRangeChanged(qreal min,
    qreal max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#handleRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::handleRangeChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate18handleRangeChangedEdd', min, max,
    )

  def q_func(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QAbstractAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#q_func

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QAbstractAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QAbstractAxisPrivate6q_funcEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)
