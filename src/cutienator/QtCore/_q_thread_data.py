"""
QThreadData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QThreadData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QThread
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QThreadData: a plain Python object standing in front
  of one C++ QThreadData.

  What exists
  -----------

  Every function of Qt's QThreadData that has a ritual and that Python can
  call so far, 5 names in all: 'get2', 'ref', 'hasEventDispatcher',
  'canWaitLocked', 'clearEvents'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  9 of the 15 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied; 3 leans on 'QThreadData; 2
  leans on 'QThreadPrivate; 1 leans on 'QtPrivate.

  What to expect
  --------------

  - The C++ QThreadData is created at the first use, not by
    'QThreadData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThreadData.
  - Each name of Qt's QThreadData that has no cute function yet,
    'clearCurrentThreadData', 'createCurrentThreadData',
    'createEventDispatcher', 'current', 'currentThreadData', 'deref',
    'ensureEventDispatcher', 'reuseBindingStatusForNewNativeThread', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QThread)
  @overload(NoneType)
  def get2(thread: Optional[QThread]) -> Optional[QThreadData]:
    """
    Calls Qt's 'QThreadData *QThreadData::get2(QThread *thread)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreaddata.html#get2

    Parameters
    ----------

    thread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QThreadData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadData *QThreadData::get2(QThread *thread)
    address = Rituals.call(
        'ritual_ZN11QThreadData4get2EP7QThread',
        CuteMixin._addressOf(thread),
    )
    return QThreadData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasEventDispatcher(self) -> bool:
    """
    Calls Qt's 'bool QThreadData::hasEventDispatcher() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreaddata.html#hasEventDispatcher
    """
    #  bool QThreadData::hasEventDispatcher() const
    return self.uglySide.call(
        'ritual_ZNK11QThreadData18hasEventDispatcherEv',
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
  @overload(int)
  def __init__(self, initialRefCount: int = 1) -> None:
    """
    Notes what was given, for Qt's 'QThreadData::QThreadData(int
    initialRefCount)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qthreaddata.html#QThreadData

    Parameters
    ----------

    initialRefCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QThreadData::QThreadData(int initialRefCount)
    self._noteCreation(QThreadData, lambda: Rituals.call(
        'ritual_ZN11QThreadDataC1Ei', initialRefCount,
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

  def ref(self) -> None:
    """
    Calls Qt's 'void QThreadData::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreaddata.html#ref
    """
    #  void QThreadData::ref()
    self.uglySide.call('ritual_ZN11QThreadData3refEv')

  def canWaitLocked(self) -> bool:
    """
    Calls Qt's 'bool QThreadData::canWaitLocked()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreaddata.html#canWaitLocked
    """
    #  bool QThreadData::canWaitLocked()
    return self.uglySide.call('ritual_ZN11QThreadData13canWaitLockedEv')

  def clearEvents(self) -> None:
    """
    Calls Qt's 'void QThreadData::clearEvents()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreaddata.html#clearEvents
    """
    #  void QThreadData::clearEvents()
    self.uglySide.call('ritual_ZN11QThreadData11clearEventsEv')

  @staticmethod
  def clearCurrentThreadData(*__, **_) -> Never:
    """
    Qt's 'void QThreadData::clearCurrentThreadData()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QThreadData.clearCurrentThreadData' has no cute function yet. "
        "Qt's 'void QThreadData::clearCurrentThreadData()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def createCurrentThreadData(*__, **_) -> Never:
    """
    Qt's 'QThreadData *QThreadData::createCurrentThreadData()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QThreadData.createCurrentThreadData' has no cute function yet. "
        "Qt's 'QThreadData *QThreadData::createCurrentThreadData()': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def createEventDispatcher(*__, **_) -> Never:
    """
    Qt's 'QAbstractEventDispatcher *QThreadData::createEventDispatcher()':
    leans on 'QThreadPrivate::createEventDispatcher(QThreadData*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QThreadData.createEventDispatcher' has no cute function yet. Qt's "
        "'QAbstractEventDispatcher *QThreadData::createEventDispatcher()': "
        "leans on 'QThreadPrivate::createEventDispatcher(QThreadData*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def current(*__, **_) -> Never:
    """
    Qt's 'QThreadData *QThreadData::current()': leans on
    'QThreadData::currentThreadData()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QThreadData.current' has no cute function yet. Qt's 'QThreadData "
        "*QThreadData::current()': leans on "
        "'QThreadData::currentThreadData()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def currentThreadData(*__, **_) -> Never:
    """
    Qt's 'QThreadData *QThreadData::currentThreadData()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QThreadData.currentThreadData' has no cute function yet. Qt's "
        "'QThreadData *QThreadData::currentThreadData()': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def deref(*__, **_) -> Never:
    """
    Qt's 'void QThreadData::deref()': leans on
    'QThreadData::clearCurrentThreadData()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QThreadData.deref' has no cute function yet. Qt's 'void "
        "QThreadData::deref()': leans on "
        "'QThreadData::clearCurrentThreadData()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def ensureEventDispatcher(*__, **_) -> Never:
    """
    Qt's 'QAbstractEventDispatcher *QThreadData::ensureEventDispatcher()':
    leans on 'QThreadPrivate::createEventDispatcher(QThreadData*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QThreadData.ensureEventDispatcher' has no cute function yet. Qt's "
        "'QAbstractEventDispatcher *QThreadData::ensureEventDispatcher()': "
        "leans on 'QThreadPrivate::createEventDispatcher(QThreadData*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def reuseBindingStatusForNewNativeThread(*__, **_) -> Never:
    """
    Qt's 'void QThreadData::reuseBindingStatusForNewNativeThread()': leans on
    'QtPrivate::setBindingStatus(QBindingStatus*,
    QtPrivate::QBindingStatusAccessToken)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QThreadData.reuseBindingStatusForNewNativeThread' has no cute "
        "function yet. Qt's 'void "
        "QThreadData::reuseBindingStatusForNewNativeThread()': leans on "
        "'QtPrivate::setBindingStatus(QBindingStatus*, "
        "QtPrivate::QBindingStatusAccessToken)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
