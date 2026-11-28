"""
QQuickAnimatorController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorcontroller_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnimatorController to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from ..QtQml import QAbstractAnimationJob, QAnimationJobChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickWindow

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatorController(QObject, QAnimationJobChangeListener):
  """
  The cute side of Qt's QQuickAnimatorController: a plain Python object
  standing in front of one C++ QQuickAnimatorController.

  It is built on the cute 'QObject', as Qt's QQuickAnimatorController is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QAnimationJobChangeListener' as well, as Qt's
  QQuickAnimatorController is built on Qt's QAnimationJobChangeListener too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatorController that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'advance',
  'beforeNodeSync', 'afterNodeSync', 'animationFinished',
  'animationStateChanged', 'requestSync', 'lock', 'unlock', 'window',
  'start_helper'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimatorController::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickAnimatorController::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAnimatorController::~QQuickAnimatorController()': the
    destructor: Python never removes a C++ QQuickAnimatorController.
  - Qt's 'void QQuickAnimatorController::start(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQuickAnimatorController::cancel(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQuickAnimatorController::pause(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QQuickAnimatorController::isPendingStart(const
    QSharedPointer<QAbstractAnimationJob> &job) const': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 24 functions Qt declares: 3 not a gap; 2 leans on
  'QQuickAnimatorController; 1 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickAnimatorController is created at the first use, not by
    'QQuickAnimatorController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatorController.
  - Qt tells when it has removed the C++ QQuickAnimatorController. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAnimatorController that has no cute function yet,
    '__init__', 'cancel', 'isPendingStart', 'pause', 'start',
    'windowNodesDestroyed', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatorController'

  #  Qt's QQuickAnimatorController is built on more than one class. The part
  #  of a C++ QQuickAnimatorController that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAnimationJobChangeListener':
          'ritual_cast_QQuickAnimatorController_QAnimationJobChangeListener',
  }

  #  A C++ QQuickAnimatorController Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatorController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnimatorController::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimatorController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAnimatorController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickAnimatorController::window() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickAnimatorController::window() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAnimatorController6windowEv',
    )
    from . import QQuickWindow
    return QQuickWindow._cuteAt(address)

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
    Qt's 'QQuickAnimatorController::QQuickAnimatorController(QQuickWindow
    *window)': leans on
    'QQuickAnimatorController::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.__init__' has no cute function yet. Qt's "
        "'QQuickAnimatorController::QQuickAnimatorController(QQuickWindow "
        "*window)': leans on "
        "'QQuickAnimatorController::qt_metacall(QMetaObject::Call, int, "
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

  def advance(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::advance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#advance
    """
    #  void QQuickAnimatorController::advance()
    self.uglySide.call('ritual_ZN24QQuickAnimatorController7advanceEv')

  def beforeNodeSync(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::beforeNodeSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#beforeNodeSync
    """
    #  void QQuickAnimatorController::beforeNodeSync()
    self.uglySide.call(
        'ritual_ZN24QQuickAnimatorController14beforeNodeSyncEv',
    )

  def afterNodeSync(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::afterNodeSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#afterNodeSync
    """
    #  void QQuickAnimatorController::afterNodeSync()
    self.uglySide.call(
        'ritual_ZN24QQuickAnimatorController13afterNodeSyncEv',
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationFinished(self, job: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QQuickAnimatorController::animationFinished(QAbstractAnimationJob *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#animationFinished

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorController::animationFinished(QAbstractAnimationJob
    #      *job)
    ritual = (
        'ritual_ZN24QQuickAnimatorController17animationFinishedEP21QAbstrac'
        'tAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickAnimatorController17animationFinishedEP21QA'
          'bstractAnimationJob')
    self.uglySide.call(ritual, self._addressOf(job, 'QAbstractAnimationJob'))

  @overload(
      QAbstractAnimationJob, QAbstractAnimationJob.State,
      QAbstractAnimationJob.State,
  )
  @overload(
      NoneType, QAbstractAnimationJob.State, QAbstractAnimationJob.State,
  )
  def animationStateChanged(
      self,
      job: Optional[QAbstractAnimationJob],
      newState: QAbstractAnimationJob.State,
      oldState: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickAnimatorController::animationStateChanged(QAbstractAnimationJob
    *job, QAbstractAnimationJob::State newState, QAbstractAnimationJob::State
    oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newState : QAbstractAnimationJob.State
      Passed on as its number.

    oldState : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QQuickAnimatorController::animationStateChanged(
    #      QAbstractAnimationJob *job, QAbstractAnimationJob::State newState,
    #      QAbstractAnimationJob::State oldState)
    ritual = (
        'ritual_ZN24QQuickAnimatorController21animationStateChangedEP21QAbs'
        'tractAnimationJobNS0_5StateES2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickAnimatorController21animationStateChangedEP'
          '21QAbstractAnimationJobNS0_5StateES2_')
    self.uglySide.call(
        ritual,
        self._addressOf(job, 'QAbstractAnimationJob'), newState.value,
        oldState.value,
    )

  def requestSync(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::requestSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#requestSync
    """
    #  void QQuickAnimatorController::requestSync()
    self.uglySide.call('ritual_ZN24QQuickAnimatorController11requestSyncEv')

  def lock(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorcontroller.html#lock
    """
    #  void QQuickAnimatorController::lock()
    self.uglySide.call('ritual_ZN24QQuickAnimatorController4lockEv')

  def unlock(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorController::unlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#unlock
    """
    #  void QQuickAnimatorController::unlock()
    self.uglySide.call('ritual_ZN24QQuickAnimatorController6unlockEv')

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def start_helper(self, job: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QQuickAnimatorController::start_helper(QAbstractAnimationJob *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorcontroller.html#start_helper

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorController::start_helper(QAbstractAnimationJob
    #      *job)
    self.uglySide.call(
        'ritual_ZN24QQuickAnimatorController12start_helperEP21QAbstractAnim'
        'ationJob',
        self._addressOf(job, 'QAbstractAnimationJob'),
    )

  @staticmethod
  def cancel(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimatorController::cancel(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.cancel' has no cute function yet. Qt's "
        "'void QQuickAnimatorController::cancel(const "
        "QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def isPendingStart(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAnimatorController::isPendingStart(const
    QSharedPointer<QAbstractAnimationJob> &job) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.isPendingStart' has no cute function "
        "yet. Qt's 'bool QQuickAnimatorController::isPendingStart(const "
        "QSharedPointer<QAbstractAnimationJob> &job) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def pause(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimatorController::pause(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.pause' has no cute function yet. Qt's "
        "'void QQuickAnimatorController::pause(const "
        "QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimatorController::start(const
    QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.start' has no cute function yet. Qt's "
        "'void QQuickAnimatorController::start(const "
        "QSharedPointer<QAbstractAnimationJob> &job)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def windowNodesDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimatorController::windowNodesDestroyed()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'qquickanimator_invalidate_jobs'.
    """
    raise NotImplementedError(
        "'QQuickAnimatorController.windowNodesDestroyed' has no cute "
        "function yet. Qt's 'void "
        "QQuickAnimatorController::windowNodesDestroyed()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qquickanimator_invalidate_jobs'.")
