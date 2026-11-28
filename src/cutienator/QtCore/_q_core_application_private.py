"""
QCoreApplicationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcoreapplication_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoreApplicationPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCoreApplication, QEvent, QObject, QPostEventList, QThread
  from . import QThreadData, QTranslator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QObject = WAIT['QObject']
  QPostEventList = WAIT['QPostEventList']
  QThreadData = WAIT['QThreadData']
  QTranslator = WAIT['QTranslator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoreApplicationPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCoreApplicationPrivate: a plain Python object
  standing in front of one C++ QCoreApplicationPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCoreApplicationPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoreApplicationPrivate that has a ritual and that
  Python can call so far, 27 names in all: 'q_func', 'init', 'appName',
  'appVersion', 'initLocale', 'checkInstance',
  'sendThroughApplicationEventFilters', 'sendThroughObjectEventFilters',
  'notify_helper', 'setEventSpontaneous', 'createEventDispatcher',
  'eventDispatcherReady', 'compressEvent', 'removePostedEvent', 'ref',
  'deref', 'canQuitAutomatically', 'quitAutomatically', 'quit', 'mainThread',
  'sendPostedEvents', 'checkReceiverThread', 'cleanupThreadData',
  'execCleanup', 'isTranslatorInstalled', 'testAttribute',
  'processCommandLineArguments'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCoreApplication *QCoreApplicationPrivate::q_func() const':
    takes in Python what 'QCoreApplication
    *QCoreApplicationPrivate::q_func()' takes.
  - Qt's 'QCoreApplicationPrivate::~QCoreApplicationPrivate()': the
    destructor: Python never removes a C++ QCoreApplicationPrivate.
  - Qt's 'void
    QCoreApplicationPrivate::addQtOptions(QList<QCommandLineOption>
    *options)': names 'QList<QCommandLineOption>', which has no cute class
    yet.
  - Qt's 'QPostEventListLocker
    QCoreApplicationPrivate::lockThreadPostEventList(QObject *object)': gives
    a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QCoreApplicationPrivate is created at the first use, not by
    'QCoreApplicationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoreApplicationPrivate.
  - Each name of Qt's QCoreApplicationPrivate that has no cute function yet,
    'addQtOptions', 'lockThreadPostEventList', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCoreApplicationPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QCoreApplicationPrivate::Type' of Qt, with the 2 names Qt gives
    in it.
    """

    Tty = Kee[int](0)
    Gui = Kee[int](1)

  #  The classes Qt writes inside QCoreApplicationPrivate, each a class in
  #  here as in C++.

  class QPostEventListLocker(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCoreApplicationPrivate::QPostEventListLocker: a
    plain Python object standing in front of one C++
    QCoreApplicationPrivate::QPostEventListLocker.

    What exists
    -----------

    Every function of Qt's QCoreApplicationPrivate::QPostEventListLocker that
    has a ritual and that Python can call so far, 1 name in all: 'unlock'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What to expect
    --------------

    - The C++ QCoreApplicationPrivate::QPostEventListLocker is created at the
      first use, not by 'QCoreApplicationPrivate::QPostEventListLocker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QCoreApplicationPrivate::QPostEventListLocker.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCoreApplicationPrivate::QPostEventListLocker'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def unlock(self) -> None:
      """
      Calls Qt's 'void
      QCoreApplicationPrivate::QPostEventListLocker::unlock()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcoreapplicationprivate-qposteventlistlocker.html
      """
      #  void QCoreApplicationPrivate::QPostEventListLocker::unlock()
      self.uglySide.call(
          'ritual_ZN23QCoreApplicationPrivate20QPostEventListLocker6unlockE'
          'v',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def initLocale() -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::initLocale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#initLocale
    """
    #  void QCoreApplicationPrivate::initLocale()
    Rituals.call('ritual_ZN23QCoreApplicationPrivate10initLocaleEv')

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def checkInstance(method: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QCoreApplicationPrivate::checkInstance(const char
    *method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#checkInstance

    Parameters
    ----------

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QCoreApplicationPrivate::checkInstance(const char *method)
    return Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate13checkInstanceEPKc',
        CuteMixin._bytesOf(method),
    )

  @staticmethod
  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sendThroughObjectEventFilters(
      a0: Optional[QObject],
      a1: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject
    #      *a0, QEvent *a1)
    return Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate29sendThroughObjectEventFiltersE'
        'P7QObjectP6QEvent',
        CuteMixin._addressOf(a0, 'QObject'), CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def notify_helper(a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCoreApplicationPrivate::notify_helper(QObject *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#notify_helper

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplicationPrivate::notify_helper(QObject *a0, QEvent *a1)
    return Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate13notify_helperEP7QObjectP6QEven'
        't',
        CuteMixin._addressOf(a0, 'QObject'), CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QEvent, bool)
  @overload(NoneType, bool)
  def setEventSpontaneous(e: Optional[QEvent], spontaneous: bool) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::setEventSpontaneous(QEvent *e,
    bool spontaneous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#setEventSpontaneous

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    spontaneous : bool
      Passed on as it is.
    """
    #  void QCoreApplicationPrivate::setEventSpontaneous(QEvent *e, bool
    #      spontaneous)
    Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate19setEventSpontaneousEP6QEventb',
        CuteMixin._addressOf(e), spontaneous,
    )

  @staticmethod
  @overload(QEvent)
  @overload(NoneType)
  def removePostedEvent(a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::removePostedEvent(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#removePostedEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoreApplicationPrivate::removePostedEvent(QEvent *a0)
    Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate17removePostedEventEP6QEvent',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  def mainThread() -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QCoreApplicationPrivate::mainThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#mainThread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QCoreApplicationPrivate::mainThread()
    address = Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate10mainThreadEv',
    )
    from . import QThread
    return QThread._cuteAt(address)

  @staticmethod
  @overload(QObject, int, QThreadData)
  @overload(QObject, int, NoneType)
  @overload(NoneType, int, QThreadData)
  @overload(NoneType, int, NoneType)
  def sendPostedEvents(
      receiver: Optional[QObject],
      event_type: int,
      data: Optional[QThreadData],
  ) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::sendPostedEvents(QObject
    *receiver, int event_type, QThreadData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#sendPostedEvents

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event_type : int
      Passed on as it is.

    data : Optional[QThreadData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoreApplicationPrivate::sendPostedEvents(QObject *receiver, int
    #      event_type, QThreadData *data)
    Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate16sendPostedEventsEP7QObjectiP11'
        'QThreadData',
        CuteMixin._addressOf(receiver, 'QObject'), event_type,
        CuteMixin._addressOf(data),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def checkReceiverThread(receiver: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::checkReceiverThread(QObject
    *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#checkReceiverThread

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoreApplicationPrivate::checkReceiverThread(QObject *receiver)
    Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate19checkReceiverThreadEP7QObject',
        CuteMixin._addressOf(receiver, 'QObject'),
    )

  @staticmethod
  @overload(QTranslator)
  @overload(NoneType)
  def isTranslatorInstalled(translator: Optional[QTranslator]) -> bool:
    """
    Calls Qt's 'bool
    QCoreApplicationPrivate::isTranslatorInstalled(QTranslator *translator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#isTranslatorInstalled

    Parameters
    ----------

    translator : Optional[QTranslator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplicationPrivate::isTranslatorInstalled(QTranslator
    #      *translator)
    return Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate21isTranslatorInstalledEP11QTran'
        'slator',
        CuteMixin._addressOf(translator),
    )

  @staticmethod
  @overload(int)
  def testAttribute(flag: int) -> bool:
    """
    Calls Qt's 'bool QCoreApplicationPrivate::testAttribute(uint flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#testAttribute

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  bool QCoreApplicationPrivate::testAttribute(uint flag)
    return Rituals.call(
        'ritual_ZN23QCoreApplicationPrivate13testAttributeEj', flag,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoreApplicationPrivate'

  #  A C++ QCoreApplicationPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoreApplicationPrivate'

  #  The functions Qt calls itself that QCoreApplicationPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'addQtOptions': (
          'void '
          'QCoreApplicationPrivate::addQtOptions(QList<QCommandLineOption> '
          '*)',
      ),
  }

  #  The functions Qt calls itself that QCoreApplicationPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createEventDispatcher': (
          ('_ZN23QCoreApplicationPrivate21createEventDispatcherEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'eventDispatcherReady': (
          ('_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'compressEvent': (
          ('_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjectP1'
           '4QPostEventList',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'address', 'QtCore:QPostEventList'),
           )),
      ),
      'canQuitAutomatically': (
          ('_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'quit': (
          ('_ZN23QCoreApplicationPrivate4quitEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def appName(self) -> str:
    """
    Calls Qt's 'QString QCoreApplicationPrivate::appName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#appName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplicationPrivate::appName() const
    return self.uglySide.call(
        'ritual_ZNK23QCoreApplicationPrivate7appNameEv',
    )

  def appVersion(self) -> str:
    """
    Calls Qt's 'QString QCoreApplicationPrivate::appVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#appVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplicationPrivate::appVersion() const
    return self.uglySide.call(
        'ritual_ZNK23QCoreApplicationPrivate10appVersionEv',
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

  @overload(list)
  def __init__(self, aargv: list) -> None:
    """
    Notes what was given, for Qt's
    'QCoreApplicationPrivate::QCoreApplicationPrivate(int &aargc, char
    **aargv)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html

    Parameters
    ----------

    aargv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.
    """
    #  QCoreApplicationPrivate::QCoreApplicationPrivate(int &aargc, char
    #      **aargv)
    self._noteCreation(QCoreApplicationPrivate, lambda: Rituals.call(
        'ritual_ZN23QCoreApplicationPrivateC1ERiPPc',
        *self._startTextsOf(aargv),
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

  def q_func(self) -> Optional[QCoreApplication]:
    """
    Calls Qt's 'QCoreApplication *QCoreApplicationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#q_func

    Returns
    -------

    Optional[QCoreApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreApplication *QCoreApplicationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QCoreApplicationPrivate6q_funcEv',
    )
    from . import QCoreApplication
    return QCoreApplication._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplicationprivate.html#init
    """
    #  void QCoreApplicationPrivate::init()
    self.uglySide.call('ritual_ZN23QCoreApplicationPrivate4initEv')

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sendThroughApplicationEventFilters(
      self,
      a0: Optional[QObject],
      a1: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QCoreApplicationPrivate::sendThroughApplicationEventFilters(QObject *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplicationPrivate::sendThroughApplicationEventFilters(
    #      QObject *a0, QEvent *a1)
    return self.uglySide.call(
        'ritual_ZN23QCoreApplicationPrivate34sendThroughApplicationEventFil'
        'tersEP7QObjectP6QEvent',
        self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  def createEventDispatcher(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::createEventDispatcher()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#createEventDispatcher
    """
    #  void QCoreApplicationPrivate::createEventDispatcher()
    ritual = 'ritual_ZN23QCoreApplicationPrivate21createEventDispatcherEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QCoreApplicationPrivate21createEventDispatcherEv')
    self.uglySide.call(ritual)

  def eventDispatcherReady(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::eventDispatcherReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#eventDispatcherReady
    """
    #  void QCoreApplicationPrivate::eventDispatcherReady()
    ritual = 'ritual_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv')
    self.uglySide.call(ritual)

  @overload(QEvent, QObject, QPostEventList)
  @overload(QEvent, QObject, NoneType)
  @overload(QEvent, NoneType, QPostEventList)
  @overload(QEvent, NoneType, NoneType)
  @overload(NoneType, QObject, QPostEventList)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QPostEventList)
  @overload(NoneType, NoneType, NoneType)
  def compressEvent(
      self,
      event: Optional[QEvent],
      receiver: Optional[QObject],
      postedEvents: Optional[QPostEventList],
  ) -> bool:
    """
    Calls Qt's 'bool QCoreApplicationPrivate::compressEvent(QEvent *event,
    QObject *receiver, QPostEventList *postedEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#compressEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    postedEvents : Optional[QPostEventList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplicationPrivate::compressEvent(QEvent *event, QObject
    #      *receiver, QPostEventList *postedEvents)
    ritual = (
        'ritual_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjec'
        'tP14QPostEventList')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7'
          'QObjectP14QPostEventList')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(receiver, 'QObject'),
        self._addressOf(postedEvents),
    )

  def ref(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplicationprivate.html#ref
    """
    #  void QCoreApplicationPrivate::ref()
    self.uglySide.call('ritual_ZN23QCoreApplicationPrivate3refEv')

  def deref(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplicationprivate.html#deref
    """
    #  void QCoreApplicationPrivate::deref()
    self.uglySide.call('ritual_ZN23QCoreApplicationPrivate5derefEv')

  def canQuitAutomatically(self) -> bool:
    """
    Calls Qt's 'bool QCoreApplicationPrivate::canQuitAutomatically()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#canQuitAutomatically
    """
    #  bool QCoreApplicationPrivate::canQuitAutomatically()
    ritual = 'ritual_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv')
    return self.uglySide.call(ritual)

  def quitAutomatically(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::quitAutomatically()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#quitAutomatically
    """
    #  void QCoreApplicationPrivate::quitAutomatically()
    self.uglySide.call(
        'ritual_ZN23QCoreApplicationPrivate17quitAutomaticallyEv',
    )

  def quit(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplicationprivate.html#quit
    """
    #  void QCoreApplicationPrivate::quit()
    ritual = 'ritual_ZN23QCoreApplicationPrivate4quitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QCoreApplicationPrivate4quitEv'
    self.uglySide.call(ritual)

  def cleanupThreadData(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::cleanupThreadData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#cleanupThreadData
    """
    #  void QCoreApplicationPrivate::cleanupThreadData()
    self.uglySide.call(
        'ritual_ZN23QCoreApplicationPrivate17cleanupThreadDataEv',
    )

  def execCleanup(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::execCleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html#execCleanup
    """
    #  void QCoreApplicationPrivate::execCleanup()
    self.uglySide.call('ritual_ZN23QCoreApplicationPrivate11execCleanupEv')

  def processCommandLineArguments(self) -> None:
    """
    Calls Qt's 'void QCoreApplicationPrivate::processCommandLineArguments()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplicationprivate.html
    """
    #  void QCoreApplicationPrivate::processCommandLineArguments()
    self.uglySide.call(
        'ritual_ZN23QCoreApplicationPrivate27processCommandLineArgumentsEv',
    )

  @staticmethod
  def addQtOptions(*__, **_) -> Never:
    """
    Qt's 'void
    QCoreApplicationPrivate::addQtOptions(QList<QCommandLineOption>
    *options)': names 'QList<QCommandLineOption>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QCoreApplicationPrivate.addQtOptions' has no cute function yet. "
        "Qt's 'void "
        "QCoreApplicationPrivate::addQtOptions(QList<QCommandLineOption> "
        "*options)': names 'QList<QCommandLineOption>', which has no cute "
        "class yet.")

  @staticmethod
  def lockThreadPostEventList(*__, **_) -> Never:
    """
    Qt's 'QPostEventListLocker
    QCoreApplicationPrivate::lockThreadPostEventList(QObject *object)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCoreApplicationPrivate.lockThreadPostEventList' has no cute "
        "function yet. Qt's 'QPostEventListLocker "
        "QCoreApplicationPrivate::lockThreadPostEventList(QObject "
        "*object)': gives a type Python has no way to take yet.")
