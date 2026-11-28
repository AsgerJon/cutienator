"""
Qt3DCore::QThreadPooler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qthreadpooler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QThreadPooler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadPooler(QObject):
  """
  The cute side of Qt's Qt3DCore::QThreadPooler: a plain Python object
  standing in front of one C++ Qt3DCore::QThreadPooler.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QThreadPooler is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QThreadPooler that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'waitForAllJobs', 'taskFinished', 'skipTask', 'enqueueDepencies',
  'acquire', 'release', 'currentCount'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QThreadPooler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QThreadPooler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QThreadPooler::~QThreadPooler()': the destructor: Python
    never removes a C++ Qt3DCore::QThreadPooler.
  - Qt's 'QFuture<void>
    Qt3DCore::QThreadPooler::mapDependables(QList<RunnableInterface *>
    &taskQueue)': takes a type Python has no way to hand over yet.
  - Qt's 'QFuture<void> Qt3DCore::QThreadPooler::future()': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DCore::QThreadPooler::enqueueTasks(const
    QList<RunnableInterface *> &tasks)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QThreadPooler is created at the first use, not by
    'Qt3DCore::QThreadPooler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QThreadPooler.
  - Qt tells when it has removed the C++ Qt3DCore::QThreadPooler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QThreadPooler that has no cute function yet,
    'enqueueTasks', 'future', 'mapDependables', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QThreadPooler::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#tr

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
    #  QString Qt3DCore::QThreadPooler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore13QThreadPooler2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QThreadPooler'

  #  A C++ Qt3DCore::QThreadPooler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QThreadPooler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QThreadPooler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QThreadPooler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QThreadPooler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentCount(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QThreadPooler::currentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#currentCount
    """
    #  int Qt3DCore::QThreadPooler::currentCount() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QThreadPooler12currentCountEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QThreadPooler::QThreadPooler(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#QThreadPooler

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QThreadPooler::QThreadPooler(QObject *parent)
    self._noteCreation(QThreadPooler, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore13QThreadPoolerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def waitForAllJobs(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QThreadPooler::waitForAllJobs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#waitForAllJobs
    """
    #  int Qt3DCore::QThreadPooler::waitForAllJobs()
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore13QThreadPooler14waitForAllJobsEv',
    )

  @overload(WAIT['Qt3DCore.RunnableInterface'])
  @overload(NoneType)
  def taskFinished(self, task: Optional[Qt3DCore.RunnableInterface]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QThreadPooler::taskFinished(RunnableInterface
    *task)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#taskFinished

    Parameters
    ----------

    task : Optional[Qt3DCore.RunnableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QThreadPooler::taskFinished(RunnableInterface *task)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QThreadPooler12taskFinishedEPNS_17RunnableInte'
        'rfaceE',
        self._addressOf(task),
    )

  @overload(WAIT['Qt3DCore.RunnableInterface'])
  @overload(NoneType)
  def skipTask(self, task: Optional[Qt3DCore.RunnableInterface]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QThreadPooler::skipTask(RunnableInterface
    *task)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#skipTask

    Parameters
    ----------

    task : Optional[Qt3DCore.RunnableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QThreadPooler::skipTask(RunnableInterface *task)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QThreadPooler8skipTaskEPNS_17RunnableInterface'
        'E',
        self._addressOf(task),
    )

  @overload(WAIT['Qt3DCore.RunnableInterface'])
  @overload(NoneType)
  def enqueueDepencies(
      self,
      task: Optional[Qt3DCore.RunnableInterface],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QThreadPooler::enqueueDepencies(RunnableInterface *task)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#enqueueDepencies

    Parameters
    ----------

    task : Optional[Qt3DCore.RunnableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QThreadPooler::enqueueDepencies(RunnableInterface
    #      *task)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QThreadPooler16enqueueDepenciesEPNS_17Runnable'
        'InterfaceE',
        self._addressOf(task),
    )

  @overload(int)
  def acquire(self, add: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QThreadPooler::acquire(int add)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#acquire

    Parameters
    ----------

    add : int
      Passed on as it is.
    """
    #  void Qt3DCore::QThreadPooler::acquire(int add)
    self.uglySide.call('ritual_ZN8Qt3DCore13QThreadPooler7acquireEi', add)

  def release(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QThreadPooler::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qthreadpooler.html#release
    """
    #  void Qt3DCore::QThreadPooler::release()
    self.uglySide.call('ritual_ZN8Qt3DCore13QThreadPooler7releaseEv')

  @staticmethod
  def enqueueTasks(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QThreadPooler::enqueueTasks(const
    QList<RunnableInterface *> &tasks)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QThreadPooler.enqueueTasks' has no cute function yet. "
        "Qt's 'void Qt3DCore::QThreadPooler::enqueueTasks(const "
        "QList<RunnableInterface *> &tasks)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def future(*__, **_) -> Never:
    """
    Qt's 'QFuture<void> Qt3DCore::QThreadPooler::future()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QThreadPooler.future' has no cute function yet. Qt's "
        "'QFuture<void> Qt3DCore::QThreadPooler::future()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mapDependables(*__, **_) -> Never:
    """
    Qt's 'QFuture<void>
    Qt3DCore::QThreadPooler::mapDependables(QList<RunnableInterface *>
    &taskQueue)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QThreadPooler.mapDependables' has no cute function yet. "
        "Qt's 'QFuture<void> "
        "Qt3DCore::QThreadPooler::mapDependables(QList<RunnableInterface *> "
        "&taskQueue)': takes a type Python has no way to hand over yet.")
