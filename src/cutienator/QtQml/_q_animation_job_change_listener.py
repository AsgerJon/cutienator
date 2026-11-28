"""
QAnimationJobChangeListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAnimationJobChangeListener to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationJobChangeListener(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAnimationJobChangeListener: a plain Python object
  standing in front of one C++ QAnimationJobChangeListener.

  C++ hands a QAnimationJobChangeListener around as a copy, so every C++
  QAnimationJobChangeListener behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QAnimationJobChangeListener that has a ritual and
  that Python can call so far, 4 names in all: 'animationFinished',
  'animationStateChanged', 'animationCurrentLoopChanged',
  'animationCurrentTimeChanged'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAnimationJobChangeListener::~QAnimationJobChangeListener()': the
    destructor: Python removes its C++ QAnimationJobChangeListener by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QAnimationJobChangeListener is created at the first use, not by
    'QAnimationJobChangeListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAnimationJobChangeListener back gives a copy the
    ritual made for Python, in a new cute QAnimationJobChangeListener.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAnimationJobChangeListener'

  #  A C++ QAnimationJobChangeListener Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAnimationJobChangeListener'

  #  The functions Qt calls itself that QAnimationJobChangeListener is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'animationFinished': (
          ('_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstrac'
           'tAnimationJob',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
           )),
      ),
      'animationStateChanged': (
          ('_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbs'
           'tractAnimationJobNS0_5StateES2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
               ('int', 'enum', 'QtQml:QAbstractAnimationJob.State'),
               ('int', 'enum', 'QtQml:QAbstractAnimationJob.State'),
           )),
      ),
      'animationCurrentLoopChanged': (
          ('_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP'
           '21QAbstractAnimationJob',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
           )),
      ),
      'animationCurrentTimeChanged': (
          ('_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP'
           '21QAbstractAnimationJobi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QAnimationJobChangeListener()'. Naming it makes this a value
  #  class: Python owns every C++ QAnimationJobChangeListener behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QAnimationJobChangeListenerD1Ev'

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

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationFinished(self, a0: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QAnimationJobChangeListener::animationFinished(QAbstractAnimationJob
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationjobchangelistener.html#animationFinished

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationJobChangeListener::animationFinished(
    #      QAbstractAnimationJob *a0)
    ritual = (
        'ritual_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbst'
        'ractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAnimationJobChangeListener17animationFinishedEP2'
          '1QAbstractAnimationJob')
    self._callAs(
        'QAnimationJobChangeListener', ritual,
        self._addressOf(a0, 'QAbstractAnimationJob'),
    )

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
    QAnimationJobChangeListener::animationStateChanged(QAbstractAnimationJob
    *a0, QAbstractAnimationJob::State a1, QAbstractAnimationJob::State a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationjobchangelistener.html

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
    #  void QAnimationJobChangeListener::animationStateChanged(
    #      QAbstractAnimationJob *a0, QAbstractAnimationJob::State a1,
    #      QAbstractAnimationJob::State a2)
    ritual = (
        'ritual_ZN27QAnimationJobChangeListener21animationStateChangedEP21Q'
        'AbstractAnimationJobNS0_5StateES2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAnimationJobChangeListener21animationStateChange'
          'dEP21QAbstractAnimationJobNS0_5StateES2_')
    self._callAs(
        'QAnimationJobChangeListener', ritual,
        self._addressOf(a0, 'QAbstractAnimationJob'), a1.value, a2.value,
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationCurrentLoopChanged(
      self,
      a0: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationJobChangeListener::animationCurrentLoopChanged(
    QAbstractAnimationJob *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationjobchangelistener.html

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationJobChangeListener::animationCurrentLoopChanged(
    #      QAbstractAnimationJob *a0)
    ritual = (
        'ritual_ZN27QAnimationJobChangeListener27animationCurrentLoopChange'
        'dEP21QAbstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAnimationJobChangeListener27animationCurrentLoop'
          'ChangedEP21QAbstractAnimationJob')
    self._callAs(
        'QAnimationJobChangeListener', ritual,
        self._addressOf(a0, 'QAbstractAnimationJob'),
    )

  @overload(QAbstractAnimationJob, int)
  @overload(NoneType, int)
  def animationCurrentTimeChanged(
      self,
      a0: Optional[QAbstractAnimationJob],
      a1: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationJobChangeListener::animationCurrentTimeChanged(
    QAbstractAnimationJob *a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationjobchangelistener.html

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  void QAnimationJobChangeListener::animationCurrentTimeChanged(
    #      QAbstractAnimationJob *a0, int a1)
    ritual = (
        'ritual_ZN27QAnimationJobChangeListener27animationCurrentTimeChange'
        'dEP21QAbstractAnimationJobi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAnimationJobChangeListener27animationCurrentTime'
          'ChangedEP21QAbstractAnimationJobi')
    self._callAs(
        'QAnimationJobChangeListener', ritual,
        self._addressOf(a0, 'QAbstractAnimationJob'), a1,
    )
