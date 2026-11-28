"""
QAnimationGroupJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qanimationgroupjob_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAnimationGroupJob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationGroupJob(QAbstractAnimationJob):
  """
  The cute side of Qt's QAnimationGroupJob: a plain Python object standing in
  front of one C++ QAnimationGroupJob.

  It is built on the cute 'QAbstractAnimationJob', as Qt's QAnimationGroupJob
  is built on Qt's QAbstractAnimationJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAnimationGroupJob that has a ritual and that Python
  can call so far, 15 names in all: 'appendAnimation', 'prependAnimation',
  'removeAnimation', 'clear', 'uncontrolledAnimationFinished',
  'topLevelAnimationLoopChanged', 'animationInserted', 'animationRemoved',
  'resetUncontrolledAnimationsFinishTime',
  'resetUncontrolledAnimationFinishTime', 'uncontrolledAnimationFinishTime',
  'setUncontrolledAnimationFinishTime', 'debugChildren', 'ungroupChild',
  'handleAnimationRemoved'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAnimationGroupJob::~QAnimationGroupJob()': the destructor: Python
    never removes a C++ QAnimationGroupJob.
  - Qt's 'Children *QAnimationGroupJob::children()': gives
    'QDoubleEndedList<QAbstractAnimationJob>', which has no cute class yet.
  - Qt's 'const Children *QAnimationGroupJob::children() const': gives
    'QDoubleEndedList<QAbstractAnimationJob>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QAnimationGroupJob is created at the first use, not by
    'QAnimationGroupJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAnimationGroupJob.
  - Each name of Qt's QAnimationGroupJob that has no cute function yet,
    'children', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QAnimationGroupJob'

  #  A C++ QAnimationGroupJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAnimationGroupJob'

  #  The functions Qt calls itself that QAnimationGroupJob is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clear': (
          ('_ZN18QAnimationGroupJob5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'uncontrolledAnimationFinished': (
          ('_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbst'
           'ractAnimationJob',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
           )),
      ),
      'animationInserted': (
          ('_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimatio'
           'nJob',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
           )),
      ),
      'animationRemoved': (
          ('_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimation'
           'JobS1_S1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
               ('address', 'address', 'QtQml:QAbstractAnimationJob'),
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

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def uncontrolledAnimationFinishTime(
      self,
      anim: Optional[QAbstractAnimationJob],
  ) -> int:
    """
    Calls Qt's 'int QAnimationGroupJob::uncontrolledAnimationFinishTime(const
    QAbstractAnimationJob *anim) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAnimationGroupJob::uncontrolledAnimationFinishTime(const
    #      QAbstractAnimationJob *anim) const
    return self.uglySide.call(
        'ritual_ZNK18QAnimationGroupJob31uncontrolledAnimationFinishTimeEPK'
        '21QAbstractAnimationJob',
        self._addressOf(anim, 'QAbstractAnimationJob'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAnimationJob, int)
  @overload(NoneType, int)
  def setUncontrolledAnimationFinishTime(
      self,
      anim: Optional[QAbstractAnimationJob],
      time: int,
  ) -> None:
    """
    Calls Qt's 'void QAnimationGroupJob::setUncontrolledAnimationFinishTime(
    QAbstractAnimationJob *anim, int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : int
      Passed on as it is.
    """
    #  void QAnimationGroupJob::setUncontrolledAnimationFinishTime(
    #      QAbstractAnimationJob *anim, int time)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob34setUncontrolledAnimationFinishTimeE'
        'P21QAbstractAnimationJobi',
        self._addressOf(anim, 'QAbstractAnimationJob'), time,
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
    'QAnimationGroupJob::QAnimationGroupJob()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#QAnimationGroupJob
    """
    #  QAnimationGroupJob::QAnimationGroupJob()
    self._noteCreation(QAnimationGroupJob, lambda: Rituals.call(
        'ritual_ZN18QAnimationGroupJobC1Ev',
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

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def appendAnimation(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::appendAnimation(QAbstractAnimationJob *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#appendAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::appendAnimation(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob15appendAnimationEP21QAbstractAnimati'
        'onJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def prependAnimation(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::prependAnimation(QAbstractAnimationJob *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#prependAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::prependAnimation(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob16prependAnimationEP21QAbstractAnimat'
        'ionJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def removeAnimation(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::removeAnimation(QAbstractAnimationJob *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#removeAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::removeAnimation(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob15removeAnimationEP21QAbstractAnimati'
        'onJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QAnimationGroupJob::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroupjob.html#clear
    """
    #  void QAnimationGroupJob::clear()
    ritual = 'ritual_ZN18QAnimationGroupJob5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAnimationGroupJob5clearEv'
    self.uglySide.call(ritual)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def uncontrolledAnimationFinished(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::uncontrolledAnimationFinished(QAbstractAnimationJob
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::uncontrolledAnimationFinished(
    #      QAbstractAnimationJob *animation)
    ritual = (
        'ritual_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QA'
        'bstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAnimationGroupJob29uncontrolledAnimationFinished'
          'EP21QAbstractAnimationJob')
    self.uglySide.call(
        ritual, self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  def topLevelAnimationLoopChanged(self) -> None:
    """
    Calls Qt's 'void QAnimationGroupJob::topLevelAnimationLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html
    """
    #  void QAnimationGroupJob::topLevelAnimationLoopChanged()
    ritual = 'ritual_ZN18QAnimationGroupJob28topLevelAnimationLoopChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAnimationGroupJob28topLevelAnimationLoopChangedE'
          'v')
    self.uglySide.call(ritual)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationInserted(self, a0: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#animationInserted

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)
    ritual = (
        'ritual_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnima'
        'tionJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAnimationGroupJob17animationInsertedEP21QAbstrac'
          'tAnimationJob')
    self.uglySide.call(ritual, self._addressOf(a0, 'QAbstractAnimationJob'))

  @overload(
      QAbstractAnimationJob, QAbstractAnimationJob, QAbstractAnimationJob,
  )
  @overload(QAbstractAnimationJob, QAbstractAnimationJob, NoneType)
  @overload(QAbstractAnimationJob, NoneType, QAbstractAnimationJob)
  @overload(QAbstractAnimationJob, NoneType, NoneType)
  @overload(NoneType, QAbstractAnimationJob, QAbstractAnimationJob)
  @overload(NoneType, QAbstractAnimationJob, NoneType)
  @overload(NoneType, NoneType, QAbstractAnimationJob)
  @overload(NoneType, NoneType, NoneType)
  def animationRemoved(
      self,
      a0: Optional[QAbstractAnimationJob],
      a1: Optional[QAbstractAnimationJob],
      a2: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::animationRemoved(QAbstractAnimationJob *a0,
    QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#animationRemoved

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::animationRemoved(QAbstractAnimationJob *a0,
    #      QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
    ritual = (
        'ritual_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimat'
        'ionJobS1_S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAnimationGroupJob16animationRemovedEP21QAbstract'
          'AnimationJobS1_S1_')
    self.uglySide.call(
        ritual,
        self._addressOf(a0, 'QAbstractAnimationJob'), self._addressOf(a1,
        'QAbstractAnimationJob'), self._addressOf(a2,
        'QAbstractAnimationJob'),
    )

  def resetUncontrolledAnimationsFinishTime(self) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::resetUncontrolledAnimationsFinishTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html
    """
    #  void QAnimationGroupJob::resetUncontrolledAnimationsFinishTime()
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob37resetUncontrolledAnimationsFinishTi'
        'meEv',
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def resetUncontrolledAnimationFinishTime(
      self,
      anim: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::resetUncontrolledAnimationFinishTime(
    QAbstractAnimationJob *anim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::resetUncontrolledAnimationFinishTime(
    #      QAbstractAnimationJob *anim)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob36resetUncontrolledAnimationFinishTim'
        'eEP21QAbstractAnimationJob',
        self._addressOf(anim, 'QAbstractAnimationJob'),
    )

  @overload(QDebug)
  def debugChildren(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QAnimationGroupJob::debugChildren(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#debugChildren

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QAnimationGroupJob::debugChildren(QDebug d) const
    self.uglySide.call(
        'ritual_ZNK18QAnimationGroupJob13debugChildrenE6QDebug',
        self._valueOf(d),
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def ungroupChild(self, animation: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void QAnimationGroupJob::ungroupChild(QAbstractAnimationJob
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#ungroupChild

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::ungroupChild(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob12ungroupChildEP21QAbstractAnimationJ'
        'ob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def handleAnimationRemoved(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupJob::handleAnimationRemoved(QAbstractAnimationJob
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupjob.html#handleAnimationRemoved

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupJob::handleAnimationRemoved(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN18QAnimationGroupJob22handleAnimationRemovedEP21QAbstract'
        'AnimationJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @staticmethod
  def children(*__, **_) -> Never:
    """
    - Qt's 'Children *QAnimationGroupJob::children()': gives
      'QDoubleEndedList<QAbstractAnimationJob>', which has no cute class yet.
    - Qt's 'const Children *QAnimationGroupJob::children() const': gives
      'QDoubleEndedList<QAbstractAnimationJob>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAnimationGroupJob.children' has no cute function yet. Qt's "
        "'Children *QAnimationGroupJob::children()': gives "
        "'QDoubleEndedList<QAbstractAnimationJob>', which has no cute class "
        "yet. Qt's 'const Children *QAnimationGroupJob::children() const': "
        "gives 'QDoubleEndedList<QAbstractAnimationJob>', which has no cute "
        "class yet.")
