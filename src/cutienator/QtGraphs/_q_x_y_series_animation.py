"""
QXYSeriesAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qxyseriesanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QXYSeriesAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QGraphAnimation, QGraphTransition

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']


class QXYSeriesAnimation(QGraphAnimation):
  """
  The cute side of Qt's QXYSeriesAnimation: a plain Python object standing in
  front of one C++ QXYSeriesAnimation.

  It is built on the cute 'QGraphAnimation', as Qt's QXYSeriesAnimation is
  built on Qt's QGraphAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYSeriesAnimation that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'updateCurrent',
  'setAnimatingValue', 'animate', 'end', 'valueUpdated'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYSeriesAnimation::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QXYSeriesAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QXYSeriesAnimation::~QXYSeriesAnimation()': the destructor: Python
    never removes a C++ QXYSeriesAnimation.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QXYSeriesAnimation.

  What to expect
  --------------

  - The C++ QXYSeriesAnimation is created at the first use, not by
    'QXYSeriesAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXYSeriesAnimation.
  - Qt tells when it has removed the C++ QXYSeriesAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QXYSeriesAnimation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXYSeriesAnimation'

  #  A C++ QXYSeriesAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXYSeriesAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QXYSeriesAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXYSeriesAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QXYSeriesAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setAnimatingValue(self, start: QVariant, end: QVariant) -> None:
    """
    Calls Qt's 'void QXYSeriesAnimation::setAnimatingValue(const QVariant
    &start, const QVariant &end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesanimation.html#setAnimatingValue

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QXYSeriesAnimation::setAnimatingValue(const QVariant &start,
    #      const QVariant &end)
    self.uglySide.call(
        'ritual_ZN18QXYSeriesAnimation17setAnimatingValueERK8QVariantS2_',
        self._valueOf(start), self._valueOf(end),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QXYSeriesAnimation::QXYSeriesAnimation(QObject *parent)': leans on
    'QXYSeriesAnimation::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QXYSeriesAnimation.__init__' has no cute function yet. Qt's "
        "'QXYSeriesAnimation::QXYSeriesAnimation(QObject *parent)': leans "
        "on 'QXYSeriesAnimation::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QGraphTransition.TransitionType, int, QPointF)
  def updateCurrent(
      self,
      tt: QGraphTransition.TransitionType,
      index: int,
      point: QPointF,
  ) -> None:
    """
    Calls Qt's 'void
    QXYSeriesAnimation::updateCurrent(QGraphTransition::TransitionType tt,
    int index, QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesanimation.html#updateCurrent

    Parameters
    ----------

    tt : QGraphTransition.TransitionType
      Passed on as its number.

    index : int
      Passed on as it is.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void
    #      QXYSeriesAnimation::updateCurrent(QGraphTransition::TransitionType
    #      tt, int index, QPointF point)
    self.uglySide.call(
        'ritual_ZN18QXYSeriesAnimation13updateCurrentEN16QGraphTransition14'
        'TransitionTypeEi7QPointF',
        tt.value, index, self._valueOf(point, 'QPointF'),
    )

  def animate(self) -> None:
    """
    Calls Qt's 'void QXYSeriesAnimation::animate()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesanimation.html#animate
    """
    #  void QXYSeriesAnimation::animate()
    self.uglySide.call('ritual_ZN18QXYSeriesAnimation7animateEv')

  def end(self) -> None:
    """
    Calls Qt's 'void QXYSeriesAnimation::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesanimation.html#end
    """
    #  void QXYSeriesAnimation::end()
    self.uglySide.call('ritual_ZN18QXYSeriesAnimation3endEv')

  @overload(QVariant)
  def valueUpdated(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QXYSeriesAnimation::valueUpdated(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesanimation.html#valueUpdated

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QXYSeriesAnimation::valueUpdated(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN18QXYSeriesAnimation12valueUpdatedERK8QVariant',
        self._valueOf(value),
    )
