"""
QSplineControlAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qsplinecontrolanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSplineControlAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QGraphAnimation, QXYSeriesAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QSplineControlAnimation(QXYSeriesAnimation):
  """
  The cute side of Qt's QSplineControlAnimation: a plain Python object
  standing in front of one C++ QSplineControlAnimation.

  It is built on the cute 'QXYSeriesAnimation', as Qt's
  QSplineControlAnimation is built on Qt's QXYSeriesAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSplineControlAnimation that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'animationType',
  'setAnimatingValue', 'interpolated', 'animate', 'end', 'valueUpdated'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSplineControlAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSplineControlAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSplineControlAnimation::~QSplineControlAnimation()': the
    destructor: Python never removes a C++ QSplineControlAnimation.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QSplineControlAnimation.

  What to expect
  --------------

  - The C++ QSplineControlAnimation is created at the first use, not by
    'QSplineControlAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplineControlAnimation.
  - Qt tells when it has removed the C++ QSplineControlAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSplineControlAnimation that has no cute function yet,
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
  __qt_class__ = 'QSplineControlAnimation'

  #  A C++ QSplineControlAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplineControlAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSplineControlAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplineControlAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QSplineControlAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      start: QVariant,
      end: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QSplineControlAnimation::interpolated(const QVariant
    &start, const QVariant &end, qreal progress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#interpolated

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSplineControlAnimation::interpolated(const QVariant &start,
    #      const QVariant &end, qreal progress) const
    ritual = (
        'ritual_ZNK23QSplineControlAnimation12interpolatedERK8QVariantS2_d')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QSplineControlAnimation12interpolatedERK8QVarian'
          'tS2_d')
    address = self.uglySide.call(
        ritual, self._valueOf(start), self._valueOf(end), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setAnimatingValue(self, start: QVariant, end: QVariant) -> None:
    """
    Calls Qt's 'void QSplineControlAnimation::setAnimatingValue(const
    QVariant &start, const QVariant &end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#setAnimatingValue

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSplineControlAnimation::setAnimatingValue(const QVariant &start,
    #      const QVariant &end)
    ritual = (
        'ritual_ZN23QSplineControlAnimation17setAnimatingValueERK8QVariantS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSplineControlAnimation17setAnimatingValueERK8QVa'
          'riantS2_')
    self.uglySide.call(ritual, self._valueOf(start), self._valueOf(end))

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
    Qt's 'QSplineControlAnimation::QSplineControlAnimation(QObject *parent)':
    leans on 'QSplineControlAnimation::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSplineControlAnimation.__init__' has no cute function yet. Qt's "
        "'QSplineControlAnimation::QSplineControlAnimation(QObject "
        "*parent)': leans on "
        "'QSplineControlAnimation::qt_metacall(QMetaObject::Call, int, "
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

  def animationType(self) -> QGraphAnimation.GraphAnimationType:
    """
    Calls Qt's 'GraphAnimationType QSplineControlAnimation::animationType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#animationType

    Returns
    -------

    QGraphAnimation.GraphAnimationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGraphAnimation.GraphAnimationType(number)' gives.
    """
    #  GraphAnimationType QSplineControlAnimation::animationType()
    ritual = 'ritual_ZN23QSplineControlAnimation13animationTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSplineControlAnimation13animationTypeEv'
    return QGraphAnimation.GraphAnimationType(self.uglySide.call(ritual))

  def animate(self) -> None:
    """
    Calls Qt's 'void QSplineControlAnimation::animate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#animate
    """
    #  void QSplineControlAnimation::animate()
    self.uglySide.call('ritual_ZN23QSplineControlAnimation7animateEv')

  def end(self) -> None:
    """
    Calls Qt's 'void QSplineControlAnimation::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplinecontrolanimation.html#end
    """
    #  void QSplineControlAnimation::end()
    self.uglySide.call('ritual_ZN23QSplineControlAnimation3endEv')

  @overload(QVariant)
  def valueUpdated(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QSplineControlAnimation::valueUpdated(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplinecontrolanimation.html#valueUpdated

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSplineControlAnimation::valueUpdated(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN23QSplineControlAnimation12valueUpdatedERK8QVariant',
        self._valueOf(value),
    )
