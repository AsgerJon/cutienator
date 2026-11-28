"""
QQuickTransitionInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTransitionInstance to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtQml import QAbstractAnimationJob, QAnimationJobChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTransitionInstance(QAnimationJobChangeListener):
  """
  The cute side of Qt's QQuickTransitionInstance: a plain Python object
  standing in front of one C++ QQuickTransitionInstance.

  It is built on the cute 'QAnimationJobChangeListener', as Qt's
  QQuickTransitionInstance is built on Qt's QAnimationJobChangeListener, and
  has everything that class has.

  C++ hands a QQuickTransitionInstance around as a copy, so every C++
  QQuickTransitionInstance behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickTransitionInstance that has a ritual and that
  Python can call so far, 6 names in all: 'start', 'stop', 'complete',
  'isRunning', 'animationStateChanged', 'removeStateChangeListener'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickTransitionInstance::~QQuickTransitionInstance()': the
    destructor: Python removes its C++ QQuickTransitionInstance by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QQuickTransitionInstance.

  What to expect
  --------------

  - The C++ QQuickTransitionInstance is created at the first use, not by
    'QQuickTransitionInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickTransitionInstance back gives a copy the ritual
    made for Python, in a new cute QQuickTransitionInstance.
  - Each name of Qt's QQuickTransitionInstance that has no cute function yet,
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
  __qt_class__ = 'QQuickTransitionInstance'

  #  A C++ QQuickTransitionInstance Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTransitionInstance'

  #  Qt's '~QQuickTransitionInstance()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickTransitionInstance behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuickTransitionInstanceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickTransitionInstance::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitioninstance.html#isRunning
    """
    #  bool QQuickTransitionInstance::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickTransitionInstance9isRunningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QQuickTransitionInstance::QQuickTransitionInstance(QQuickTransition
    *transition, QAbstractAnimationJob *anim)': leans on
    'QQuickTransitionInstance::animationStateChanged(QAbstractAnimationJob*,
    QAbstractAnimationJob::State, QAbstractAnimationJob::State)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickTransitionInstance.__init__' has no cute function yet. Qt's "
        "'QQuickTransitionInstance::QQuickTransitionInstance(QQuickTransitio"
        "n *transition, QAbstractAnimationJob *anim)': leans on "
        "'QQuickTransitionInstance::animationStateChanged(QAbstractAnimation"
        "Job*, QAbstractAnimationJob::State, "
        "QAbstractAnimationJob::State)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def start(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionInstance::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitioninstance.html#start
    """
    #  void QQuickTransitionInstance::start()
    self.uglySide.call('ritual_ZN24QQuickTransitionInstance5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionInstance::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransitioninstance.html#stop
    """
    #  void QQuickTransitionInstance::stop()
    self.uglySide.call('ritual_ZN24QQuickTransitionInstance4stopEv')

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionInstance::complete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitioninstance.html#complete
    """
    #  void QQuickTransitionInstance::complete()
    self.uglySide.call('ritual_ZN24QQuickTransitionInstance8completeEv')

  @overload(
      QAbstractAnimationJob, QAbstractAnimationJob.State,
      QAbstractAnimationJob.State,
  )
  @overload(
      NoneType, QAbstractAnimationJob.State, QAbstractAnimationJob.State,
  )
  def animationStateChanged(
      self,
      a0: Optional[QAbstractAnimationJob],
      a1: QAbstractAnimationJob.State,
      a2: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTransitionInstance::animationStateChanged(QAbstractAnimationJob
    *a0, QAbstractAnimationJob::State a1, QAbstractAnimationJob::State a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitioninstance.html

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QAbstractAnimationJob.State
      Passed on as its number.

    a2 : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QQuickTransitionInstance::animationStateChanged(
    #      QAbstractAnimationJob *a0, QAbstractAnimationJob::State a1,
    #      QAbstractAnimationJob::State a2)
    self.uglySide.call(
        'ritual_ZN24QQuickTransitionInstance21animationStateChangedEP21QAbs'
        'tractAnimationJobNS0_5StateES2_',
        self._addressOf(a0, 'QAbstractAnimationJob'), a1.value, a2.value,
    )

  def removeStateChangeListener(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionInstance::removeStateChangeListener()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitioninstance.html
    """
    #  void QQuickTransitionInstance::removeStateChangeListener()
    self.uglySide.call(
        'ritual_ZN24QQuickTransitionInstance25removeStateChangeListenerEv',
    )
