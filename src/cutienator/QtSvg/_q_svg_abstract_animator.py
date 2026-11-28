"""
QSvgAbstractAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgAbstractAnimator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSvgAbstractAnimation, QSvgNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgAbstractAnimation = WAIT['QSvgAbstractAnimation']
  QSvgNode = WAIT['QSvgNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgAbstractAnimator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgAbstractAnimator: a plain Python object standing
  in front of one C++ QSvgAbstractAnimator.

  What exists
  -----------

  Every function of Qt's QSvgAbstractAnimator that has a ritual and that
  Python can call so far, 9 names in all: 'appendAnimation',
  'animationsForNode', 'advanceAnimations', 'restartAnimation',
  'currentElapsed', 'setAnimatorTime', 'setAnimationDuration',
  'animationDuration', 'combinedAnimationsForNode'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAbstractAnimator::~QSvgAbstractAnimator()': the destructor:
    Python never removes a C++ QSvgAbstractAnimator.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSvgAbstractAnimator is created at the first use, not by
    'QSvgAbstractAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAbstractAnimator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAbstractAnimator'

  #  A C++ QSvgAbstractAnimator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAbstractAnimator'

  #  The functions Qt calls itself that QSvgAbstractAnimator is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'restartAnimation': (
          ('_ZN20QSvgAbstractAnimator16restartAnimationEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'currentElapsed': (
          ('_ZN20QSvgAbstractAnimator14currentElapsedEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setAnimatorTime': (
          ('_ZN20QSvgAbstractAnimator15setAnimatorTimeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
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

  @overload(QSvgNode)
  @overload(NoneType)
  def animationsForNode(
      self,
      node: Optional[QSvgNode],
  ) -> QList[QSvgAbstractAnimation]:
    """
    Calls Qt's 'QList<QSvgAbstractAnimation *>
    QSvgAbstractAnimator::animationsForNode(const QSvgNode *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#animationsForNode

    Parameters
    ----------

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QSvgAbstractAnimation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSvgAbstractAnimation *>
    #      QSvgAbstractAnimator::animationsForNode(const QSvgNode *node)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QSvgAbstractAnimator17animationsForNodeEPK8QSvgNode',
        self._addressOf(node),
    )
    from . import QSvgAbstractAnimation
    return QList[QSvgAbstractAnimation]._cuteOwning(address)

  def animationDuration(self) -> int:
    """
    Calls Qt's 'qint64 QSvgAbstractAnimator::animationDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#animationDuration
    """
    #  qint64 QSvgAbstractAnimator::animationDuration() const
    return self.uglySide.call(
        'ritual_ZNK20QSvgAbstractAnimator17animationDurationEv',
    )

  @overload(QSvgNode)
  @overload(NoneType)
  def combinedAnimationsForNode(
      self,
      node: Optional[QSvgNode],
  ) -> QList[QSvgAbstractAnimation]:
    """
    Calls Qt's 'QList<QSvgAbstractAnimation *>
    QSvgAbstractAnimator::combinedAnimationsForNode(const QSvgNode *node)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html

    Parameters
    ----------

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QSvgAbstractAnimation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSvgAbstractAnimation *>
    #      QSvgAbstractAnimator::combinedAnimationsForNode(const QSvgNode
    #      *node) const
    address = self.uglySide.call(
        'ritual_ZNK20QSvgAbstractAnimator25combinedAnimationsForNodeEPK8QSv'
        'gNode',
        self._addressOf(node),
    )
    from . import QSvgAbstractAnimation
    return QList[QSvgAbstractAnimation]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAnimatorTime(self, time: int) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimator::setAnimatorTime(qint64 time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#setAnimatorTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QSvgAbstractAnimator::setAnimatorTime(qint64 time)
    self.uglySide.call(
        'ritual_ZN20QSvgAbstractAnimator15setAnimatorTimeEx', time,
    )

  @overload(int)
  def setAnimationDuration(self, dur: int) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimator::setAnimationDuration(qint64 dur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#setAnimationDuration

    Parameters
    ----------

    dur : int
      Passed on as it is.
    """
    #  void QSvgAbstractAnimator::setAnimationDuration(qint64 dur)
    self.uglySide.call(
        'ritual_ZN20QSvgAbstractAnimator20setAnimationDurationEx', dur,
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
    'QSvgAbstractAnimator::QSvgAbstractAnimator()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#QSvgAbstractAnimator
    """
    #  QSvgAbstractAnimator::QSvgAbstractAnimator()
    self._noteCreation(QSvgAbstractAnimator, lambda: Rituals.call(
        'ritual_ZN20QSvgAbstractAnimatorC1Ev',
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

  @overload(QSvgNode, QSvgAbstractAnimation)
  @overload(QSvgNode, NoneType)
  @overload(NoneType, QSvgAbstractAnimation)
  @overload(NoneType, NoneType)
  def appendAnimation(
      self,
      node: Optional[QSvgNode],
      anim: Optional[QSvgAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimator::appendAnimation(const QSvgNode
    *node, QSvgAbstractAnimation *anim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#appendAnimation

    Parameters
    ----------

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    anim : Optional[QSvgAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgAbstractAnimator::appendAnimation(const QSvgNode *node,
    #      QSvgAbstractAnimation *anim)
    self.uglySide.call(
        'ritual_ZN20QSvgAbstractAnimator15appendAnimationEPK8QSvgNodeP21QSv'
        'gAbstractAnimation',
        self._addressOf(node), self._addressOf(anim,
        'QSvgAbstractAnimation'),
    )

  def advanceAnimations(self) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimator::advanceAnimations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#advanceAnimations
    """
    #  void QSvgAbstractAnimator::advanceAnimations()
    self.uglySide.call(
        'ritual_ZN20QSvgAbstractAnimator17advanceAnimationsEv',
    )

  def restartAnimation(self) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimator::restartAnimation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#restartAnimation
    """
    #  void QSvgAbstractAnimator::restartAnimation()
    self.uglySide.call('ritual_ZN20QSvgAbstractAnimator16restartAnimationEv')

  def currentElapsed(self) -> int:
    """
    Calls Qt's 'qint64 QSvgAbstractAnimator::currentElapsed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimator.html#currentElapsed
    """
    #  qint64 QSvgAbstractAnimator::currentElapsed()
    return self.uglySide.call(
        'ritual_ZN20QSvgAbstractAnimator14currentElapsedEv',
    )
