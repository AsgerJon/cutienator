"""
QThreadPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QThreadPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBindingStatus, QObject, QThread
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadPrivate(QObjectPrivate):
  """
  The cute side of Qt's QThreadPrivate: a plain Python object standing in
  front of one C++ QThreadPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QThreadPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QThreadPrivate that has a ritual and that Python can
  call so far, 8 names in all: 'q_func', 'wakeAll', 'cleanup', 'ref',
  'deref', 'bindingStatus', 'addObjectWithPendingBindingStatusChange',
  'removeObjectWithPendingBindingStatusChange'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QThread *QThreadPrivate::q_func() const': takes in Python
    what 'QThread *QThreadPrivate::q_func()' takes.
  - Qt's 'Qt::HANDLE QThreadPrivate::threadId() const': gives 'void', which
    has no cute class yet.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 8 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QThreadPrivate is created at the first use, not by
    'QThreadPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThreadPrivate.
  - Each name of Qt's QThreadPrivate that has no cute function yet,
    '__init__', 'createEventDispatcher', 'finish', 'setPriority',
    'setQualityOfServiceLevel', 'start', 'threadId', 'wait', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QThreadPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QThreadPrivate::State' of Qt, with the 4 names Qt gives in it.
    """

    NotStarted = Kee[int](0)
    Running = Kee[int](1)
    Finishing = Kee[int](2)
    Finished = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QThreadPrivate::QThreadPrivate(QThreadData *d)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.__init__' has no cute function yet. Qt's "
        "'QThreadPrivate::QThreadPrivate(QThreadData *d)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

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

  def q_func(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QThreadPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#q_func

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QThreadPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QThreadPrivate6q_funcEv')
    from . import QThread
    return QThread._cuteAt(address)

  def wakeAll(self) -> None:
    """
    Calls Qt's 'void QThreadPrivate::wakeAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#wakeAll
    """
    #  void QThreadPrivate::wakeAll()
    self.uglySide.call('ritual_ZN14QThreadPrivate7wakeAllEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QThreadPrivate::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#cleanup
    """
    #  void QThreadPrivate::cleanup()
    self.uglySide.call('ritual_ZN14QThreadPrivate7cleanupEv')

  def ref(self) -> None:
    """
    Calls Qt's 'void QThreadPrivate::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#ref
    """
    #  void QThreadPrivate::ref()
    self.uglySide.call('ritual_ZN14QThreadPrivate3refEv')

  def deref(self) -> None:
    """
    Calls Qt's 'void QThreadPrivate::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#deref
    """
    #  void QThreadPrivate::deref()
    self.uglySide.call('ritual_ZN14QThreadPrivate5derefEv')

  def bindingStatus(self) -> Optional[QBindingStatus]:
    """
    Calls Qt's 'QBindingStatus *QThreadPrivate::bindingStatus()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadprivate.html#bindingStatus

    Returns
    -------

    Optional[QBindingStatus]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBindingStatus *QThreadPrivate::bindingStatus()
    address = self.uglySide.call(
        'ritual_ZN14QThreadPrivate13bindingStatusEv',
    )
    from . import QBindingStatus
    return QBindingStatus._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def addObjectWithPendingBindingStatusChange(
      self,
      obj: Optional[QObject],
  ) -> Optional[QBindingStatus]:
    """
    Calls Qt's 'QBindingStatus
    *QThreadPrivate::addObjectWithPendingBindingStatusChange(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBindingStatus]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBindingStatus
    #      *QThreadPrivate::addObjectWithPendingBindingStatusChange(QObject
    #      *obj)
    address = self.uglySide.call(
        'ritual_ZN14QThreadPrivate39addObjectWithPendingBindingStatusChange'
        'EP7QObject',
        self._addressOf(obj, 'QObject'),
    )
    from . import QBindingStatus
    return QBindingStatus._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def removeObjectWithPendingBindingStatusChange(
      self,
      obj: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QThreadPrivate::removeObjectWithPendingBindingStatusChange(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QThreadPrivate::removeObjectWithPendingBindingStatusChange(QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN14QThreadPrivate42removeObjectWithPendingBindingStatusCha'
        'ngeEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @staticmethod
  def createEventDispatcher(*__, **_) -> Never:
    """
    Qt's 'QAbstractEventDispatcher
    *QThreadPrivate::createEventDispatcher(QThreadData *data)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.createEventDispatcher' has no cute function yet. "
        "Qt's 'QAbstractEventDispatcher "
        "*QThreadPrivate::createEventDispatcher(QThreadData *data)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def finish(*__, **_) -> Never:
    """
    Qt's 'void QThreadPrivate::finish(bool a0)': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.finish' has no cute function yet. Qt's 'void "
        "QThreadPrivate::finish(bool a0)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setPriority(*__, **_) -> Never:
    """
    Qt's 'void QThreadPrivate::setPriority(QThread::Priority prio)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.setPriority' has no cute function yet. Qt's 'void "
        "QThreadPrivate::setPriority(QThread::Priority prio)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setQualityOfServiceLevel(*__, **_) -> Never:
    """
    Qt's 'void
    QThreadPrivate::setQualityOfServiceLevel(QThread::QualityOfService
    qosLevel)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.setQualityOfServiceLevel' has no cute function "
        "yet. Qt's 'void "
        "QThreadPrivate::setQualityOfServiceLevel(QThread::QualityOfService "
        "qosLevel)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void *QThreadPrivate::start(void *arg)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.start' has no cute function yet. Qt's 'void "
        "*QThreadPrivate::start(void *arg)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def threadId(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QThreadPrivate::threadId() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QThreadPrivate.threadId' has no cute function yet. Qt's "
        "'Qt::HANDLE QThreadPrivate::threadId() const': gives 'void', which "
        "has no cute class yet.")

  @staticmethod
  def wait(*__, **_) -> Never:
    """
    Qt's 'bool QThreadPrivate::wait(QMutexLocker<QMutex> &locker,
    QDeadlineTimer deadline)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QThreadPrivate.wait' has no cute function yet. Qt's 'bool "
        "QThreadPrivate::wait(QMutexLocker<QMutex> &locker, QDeadlineTimer "
        "deadline)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
