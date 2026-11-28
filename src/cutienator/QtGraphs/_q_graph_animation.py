"""
QGraphAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qgraphanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QVariantAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QGraphAnimation(QVariantAnimation):
  """
  The cute side of Qt's QGraphAnimation: a plain Python object standing in
  front of one C++ QGraphAnimation.

  It is built on the cute 'QVariantAnimation', as Qt's QGraphAnimation is
  built on Qt's QVariantAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphAnimation that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'animationType',
  'setAnimatingValue', 'animate', 'end', 'interpolated', 'animating',
  'valueUpdated', 'animatingChanged'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphAnimation::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGraphAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphAnimation::~QGraphAnimation()': the destructor: Python never
    removes a C++ QGraphAnimation.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 3 leans on 'QGraphAnimation; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QGraphAnimation is created at the first use, not by
    'QGraphAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphAnimation.
  - Qt tells when it has removed the C++ QGraphAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphAnimation that has no cute function yet,
    '__init__', 'setAnimating', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphAnimation, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AnimationState(CuteNum, scoped=True):
    """
    The enum 'QGraphAnimation::AnimationState' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Playing = Kee[int](0)
    Stopped = Kee[int](1)

  class GraphAnimationType(CuteNum, scoped=True):
    """
    The enum 'QGraphAnimation::GraphAnimationType' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    GraphPoint = Kee[int](0)
    ControlPoint = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphAnimation'

  #  A C++ QGraphAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphAnimation'

  #  The functions Qt calls itself that QGraphAnimation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'animationType': (
          ('_ZN15QGraphAnimation13animationTypeEv',
           ('int', 'enum', 'QtGraphs:QGraphAnimation.GraphAnimationType'),
           ()),
      ),
      'setAnimatingValue': (
          ('_ZN15QGraphAnimation17setAnimatingValueERK8QVariantS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'animate': (
          ('_ZN15QGraphAnimation7animateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'end': (
          ('_ZN15QGraphAnimation3endEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'valueUpdated': (
          ('_ZN15QGraphAnimation12valueUpdatedERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphAnimation::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGraphAnimation10metaObjectEv')
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
    Calls Qt's 'QVariant QGraphAnimation::interpolated(const QVariant &start,
    const QVariant &end, qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#interpolated

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
    #  QVariant QGraphAnimation::interpolated(const QVariant &start, const
    #      QVariant &end, qreal progress) const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphAnimation12interpolatedERK8QVariantS2_d',
        self._valueOf(start), self._valueOf(end), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def animating(self) -> AnimationState:
    """
    Calls Qt's 'AnimationState QGraphAnimation::animating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#animating

    Returns
    -------

    AnimationState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AnimationState(number)'
      gives.
    """
    #  AnimationState QGraphAnimation::animating() const
    return QGraphAnimation.AnimationState(self.uglySide.call(
        'ritual_ZNK15QGraphAnimation9animatingEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setAnimatingValue(self, start: QVariant, end: QVariant) -> None:
    """
    Calls Qt's 'void QGraphAnimation::setAnimatingValue(const QVariant
    &start, const QVariant &end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphanimation.html#setAnimatingValue

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGraphAnimation::setAnimatingValue(const QVariant &start, const
    #      QVariant &end)
    self.uglySide.call(
        'ritual_ZN15QGraphAnimation17setAnimatingValueERK8QVariantS2_',
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
    Qt's 'QGraphAnimation::QGraphAnimation(QObject *parent)': leans on
    'QGraphAnimation::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QGraphAnimation.__init__' has no cute function yet. Qt's "
        "'QGraphAnimation::QGraphAnimation(QObject *parent)': leans on "
        "'QGraphAnimation::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def animationType(self) -> GraphAnimationType:
    """
    Calls Qt's 'GraphAnimationType QGraphAnimation::animationType()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#animationType

    Returns
    -------

    GraphAnimationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'GraphAnimationType(number)' gives.
    """
    #  GraphAnimationType QGraphAnimation::animationType()
    return QGraphAnimation.GraphAnimationType(self.uglySide.call(
        'ritual_ZN15QGraphAnimation13animationTypeEv',
    ))

  def animate(self) -> None:
    """
    Calls Qt's 'void QGraphAnimation::animate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#animate
    """
    #  void QGraphAnimation::animate()
    self.uglySide.call('ritual_ZN15QGraphAnimation7animateEv')

  def end(self) -> None:
    """
    Calls Qt's 'void QGraphAnimation::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#end
    """
    #  void QGraphAnimation::end()
    self.uglySide.call('ritual_ZN15QGraphAnimation3endEv')

  @overload(QVariant)
  def valueUpdated(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QGraphAnimation::valueUpdated(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphanimation.html#valueUpdated

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGraphAnimation::valueUpdated(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QGraphAnimation12valueUpdatedERK8QVariant',
        self._valueOf(value),
    )

  def animatingChanged(self) -> None:
    """
    Calls Qt's 'void QGraphAnimation::animatingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphanimation.html#animatingChanged
    """
    #  void QGraphAnimation::animatingChanged()
    self.uglySide.call('ritual_ZN15QGraphAnimation16animatingChangedEv')

  @staticmethod
  def setAnimating(*__, **_) -> Never:
    """
    Qt's 'void QGraphAnimation::setAnimating(AnimationState newAnimating)':
    leans on 'QGraphAnimation::animatingChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphAnimation.setAnimating' has no cute function yet. Qt's "
        "'void QGraphAnimation::setAnimating(AnimationState newAnimating)': "
        "leans on 'QGraphAnimation::animatingChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
