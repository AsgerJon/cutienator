"""
QQuickAnimatorProxyJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimatorProxyJob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QMetaObject
  from . import QQuickAbstractAnimation, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QQuickAbstractAnimation = WAIT['QQuickAbstractAnimation']
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatorProxyJob(QObject, QAbstractAnimationJob):
  """
  The cute side of Qt's QQuickAnimatorProxyJob: a plain Python object
  standing in front of one C++ QQuickAnimatorProxyJob.

  It is built on the cute 'QObject', as Qt's QQuickAnimatorProxyJob is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QAbstractAnimationJob' as well, as Qt's QQuickAnimatorProxyJob is built on
  Qt's QAbstractAnimationJob too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatorProxyJob that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'duration',
  'updateCurrentTime', 'updateLoopCount', 'updateState', 'debugAnimation',
  'windowChanged', 'sceneGraphInitialized', 'syncBackCurrentValues',
  'readyToAnimate', 'setWindow', 'findAnimationContext'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimatorProxyJob::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAnimatorProxyJob::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAnimatorProxyJob::~QQuickAnimatorProxyJob()': the destructor:
    Python never removes a C++ QQuickAnimatorProxyJob.
  - Qt's 'const QSharedPointer<QAbstractAnimationJob>
    &QQuickAnimatorProxyJob::job() const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnimatorProxyJob is created at the first use, not by
    'QQuickAnimatorProxyJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatorProxyJob.
  - Qt tells when it has removed the C++ QQuickAnimatorProxyJob. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAnimatorProxyJob that has no cute function yet,
    'job', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickAnimatorProxyJob::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAnimatorProxyJob::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickAnimatorProxyJob2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuickAbstractAnimation)
  @overload(NoneType)
  def findAnimationContext(
      a0: Optional[QQuickAbstractAnimation],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQuickAnimatorProxyJob::findAnimationContext(QQuickAbstractAnimation
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#findAnimationContext

    Parameters
    ----------

    a0 : Optional[QQuickAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickAnimatorProxyJob::findAnimationContext(
    #      QQuickAbstractAnimation *a0)
    address = Rituals.call(
        'ritual_ZN22QQuickAnimatorProxyJob20findAnimationContextEP23QQuickA'
        'bstractAnimation',
        CuteMixin._addressOf(a0),
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatorProxyJob'

  #  Qt's QQuickAnimatorProxyJob is built on more than one class. The part of
  #  a C++ QQuickAnimatorProxyJob that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractAnimationJob':
          'ritual_cast_QQuickAnimatorProxyJob_QAbstractAnimationJob',
  }

  #  A C++ QQuickAnimatorProxyJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatorProxyJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnimatorProxyJob::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimatorProxyJob::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickAnimatorProxyJob10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatorProxyJob::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#duration
    """
    #  int QQuickAnimatorProxyJob::duration() const
    ritual = 'ritual_ZNK22QQuickAnimatorProxyJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickAnimatorProxyJob8durationEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::setWindow(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorProxyJob::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN22QQuickAnimatorProxyJob9setWindowEP12QQuickWindow',
        self._addressOf(window),
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

  @overload(QAbstractAnimationJob, QQuickAbstractAnimation)
  @overload(QAbstractAnimationJob, NoneType)
  @overload(NoneType, QQuickAbstractAnimation)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      job: Optional[QAbstractAnimationJob],
      animation: Optional[QQuickAbstractAnimation],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnimatorProxyJob::QQuickAnimatorProxyJob(QAbstractAnimationJob
    *job, QQuickAbstractAnimation *animation)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#QQuickAnimatorProxyJob

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    animation : Optional[QQuickAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickAnimatorProxyJob::QQuickAnimatorProxyJob(QAbstractAnimationJob
    #      *job, QQuickAbstractAnimation *animation)
    self._noteCreation(QQuickAnimatorProxyJob, lambda: Rituals.call(
        'ritual_ZN22QQuickAnimatorProxyJobC1EP21QAbstractAnimationJobP23QQu'
        'ickAbstractAnimation',
        self._addressOf(job, 'QAbstractAnimationJob'),
        self._addressOf(animation),
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

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAnimatorProxyJob::updateCurrentTime(int a0)
    ritual = 'ritual_ZN22QQuickAnimatorProxyJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickAnimatorProxyJob17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def updateLoopCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::updateLoopCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#updateLoopCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAnimatorProxyJob::updateLoopCount(int a0)
    ritual = 'ritual_ZN22QQuickAnimatorProxyJob15updateLoopCountEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickAnimatorProxyJob15updateLoopCountEi'
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimationJob.State, QAbstractAnimationJob.State)
  def updateState(
      self,
      newState: QAbstractAnimationJob.State,
      oldState: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickAnimatorProxyJob::updateState(QAbstractAnimationJob::State
    newState, QAbstractAnimationJob::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimationJob.State
      Passed on as its number.

    oldState : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QQuickAnimatorProxyJob::updateState(QAbstractAnimationJob::State
    #      newState, QAbstractAnimationJob::State oldState)
    ritual = (
        'ritual_ZN22QQuickAnimatorProxyJob11updateStateEN21QAbstractAnimati'
        'onJob5StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickAnimatorProxyJob11updateStateEN21QAbstractA'
          'nimationJob5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QQuickAnimatorProxyJob::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK22QQuickAnimatorProxyJob14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QQuickAnimatorProxyJob14debugAnimationE6QDebug')
    self.uglySide.call(ritual, self._valueOf(d))

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::windowChanged(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#windowChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorProxyJob::windowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN22QQuickAnimatorProxyJob13windowChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  def sceneGraphInitialized(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::sceneGraphInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#sceneGraphInitialized
    """
    #  void QQuickAnimatorProxyJob::sceneGraphInitialized()
    self.uglySide.call(
        'ritual_ZN22QQuickAnimatorProxyJob21sceneGraphInitializedEv',
    )

  def syncBackCurrentValues(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::syncBackCurrentValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#syncBackCurrentValues
    """
    #  void QQuickAnimatorProxyJob::syncBackCurrentValues()
    self.uglySide.call(
        'ritual_ZN22QQuickAnimatorProxyJob21syncBackCurrentValuesEv',
    )

  def readyToAnimate(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorProxyJob::readyToAnimate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorproxyjob.html#readyToAnimate
    """
    #  void QQuickAnimatorProxyJob::readyToAnimate()
    self.uglySide.call('ritual_ZN22QQuickAnimatorProxyJob14readyToAnimateEv')

  @staticmethod
  def job(*__, **_) -> Never:
    """
    Qt's 'const QSharedPointer<QAbstractAnimationJob>
    &QQuickAnimatorProxyJob::job() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorProxyJob.job' has no cute function yet. Qt's 'const "
        "QSharedPointer<QAbstractAnimationJob> "
        "&QQuickAnimatorProxyJob::job() const': gives a type Python has no "
        "way to take yet.")
