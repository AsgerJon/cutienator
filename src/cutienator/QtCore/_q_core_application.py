"""
QCoreApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcoreapplication.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ._qt import Qt
from ._q_event import QEvent
from ._q_event_loop import QEventLoop
from ._q_meta_object import QMetaObject
from ._q_object import QObject
from ._q_translator import QTranslator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoreApplication(QObject):
  """
  The cute side of Qt's QCoreApplication: a plain Python object standing in
  front of one C++ QCoreApplication.

  It is built on the cute 'QObject', as Qt's QCoreApplication is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoreApplication that has a ritual and that Python
  can call so far, 37 names in all: 'metaObject', 'tr', 'setAttribute',
  'testAttribute', 'setOrganizationDomain', 'organizationDomain',
  'setOrganizationName', 'organizationName', 'setApplicationName',
  'applicationName', 'setApplicationVersion', 'applicationVersion',
  'setSetuidAllowed', 'isSetuidAllowed', 'instance', 'instanceExists',
  'exec', 'processEvents', 'sendEvent', 'postEvent', 'sendPostedEvents',
  'removePostedEvents', 'notify', 'startingUp', 'closingDown',
  'applicationDirPath', 'applicationFilePath', 'applicationPid',
  'addLibraryPath', 'removeLibraryPath', 'installTranslator',
  'removeTranslator', 'translate', 'isQuitLockEnabled', 'setQuitLockEnabled',
  'quit', 'exit'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoreApplication::~QCoreApplication()': the destructor: Python
    never removes a C++ QCoreApplication.
  - Qt's 'void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
    flags, QDeadlineTimer deadline)': names 'QDeadlineTimer', which has no
    cute class yet.
  - Qt's 'QAbstractEventDispatcher *QCoreApplication::eventDispatcher()':
    gives 'QAbstractEventDispatcher', which has no cute class yet.
  - Qt's 'void QCoreApplication::setEventDispatcher(QAbstractEventDispatcher
    *eventDispatcher)': names 'QAbstractEventDispatcher', which has no cute
    class yet.
  - Qt's 'Qt::PermissionStatus QCoreApplication::checkPermission(const
    QPermission &permission)': names 'QPermission', which has no cute class
    yet.
  - Qt's 'void
    QCoreApplication::installNativeEventFilter(QAbstractNativeEventFilter
    *filterObj)': names 'QAbstractNativeEventFilter', which has no cute class
    yet.
  - Qt's 'void
    QCoreApplication::removeNativeEventFilter(QAbstractNativeEventFilter
    *filterObj)': names 'QAbstractNativeEventFilter', which has no cute class
    yet.

  What has no ritual
  ------------------

  27 of the 73 functions Qt declares: 7 private; 5 takes or gives a type that
  cannot be passed yet; 5 a signal; 4 a template; 4 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QCoreApplication is created by 'QCoreApplication(...)' at once,
    since nearly every other object of Qt can only be made after it.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoreApplication.
  - Qt tells when it has removed the C++ QCoreApplication. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QCoreApplication::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#tr

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
    #  QString QCoreApplication::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QCoreApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Qt.ApplicationAttribute)
  @overload(Qt.ApplicationAttribute, bool)
  def setAttribute(
      attribute: Qt.ApplicationAttribute,
      on: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QCoreApplication::setAttribute(Qt::ApplicationAttribute
    attribute, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#setAttribute

    Parameters
    ----------

    attribute : Qt.ApplicationAttribute
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QCoreApplication::setAttribute(Qt::ApplicationAttribute
    #      attribute, bool on)
    Rituals.call(
        'ritual_ZN16QCoreApplication12setAttributeEN2Qt20ApplicationAttribu'
        'teEb',
        attribute.value, on,
    )

  @staticmethod
  @overload(Qt.ApplicationAttribute)
  def testAttribute(attribute: Qt.ApplicationAttribute) -> bool:
    """
    Calls Qt's 'bool QCoreApplication::testAttribute(Qt::ApplicationAttribute
    attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#testAttribute

    Parameters
    ----------

    attribute : Qt.ApplicationAttribute
      Passed on as its number.
    """
    #  bool QCoreApplication::testAttribute(Qt::ApplicationAttribute
    #      attribute)
    return Rituals.call(
        'ritual_ZN16QCoreApplication13testAttributeEN2Qt20ApplicationAttrib'
        'uteE',
        attribute.value,
    )

  @staticmethod
  @overload(str)
  def setOrganizationDomain(orgDomain: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::setOrganizationDomain(const QString
    &orgDomain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setOrganizationDomain

    Parameters
    ----------

    orgDomain : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::setOrganizationDomain(const QString &orgDomain)
    Rituals.call(
        'ritual_ZN16QCoreApplication21setOrganizationDomainERK7QString',
        orgDomain,
    )

  @staticmethod
  def organizationDomain() -> str:
    """
    Calls Qt's 'QString QCoreApplication::organizationDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#organizationDomain

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::organizationDomain()
    return Rituals.call('ritual_ZN16QCoreApplication18organizationDomainEv')

  @staticmethod
  @overload(str)
  def setOrganizationName(orgName: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::setOrganizationName(const QString
    &orgName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setOrganizationName

    Parameters
    ----------

    orgName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::setOrganizationName(const QString &orgName)
    Rituals.call(
        'ritual_ZN16QCoreApplication19setOrganizationNameERK7QString',
        orgName,
    )

  @staticmethod
  def organizationName() -> str:
    """
    Calls Qt's 'QString QCoreApplication::organizationName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#organizationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::organizationName()
    return Rituals.call('ritual_ZN16QCoreApplication16organizationNameEv')

  @staticmethod
  @overload(str)
  def setApplicationName(application: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::setApplicationName(const QString
    &application)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setApplicationName

    Parameters
    ----------

    application : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::setApplicationName(const QString &application)
    Rituals.call(
        'ritual_ZN16QCoreApplication18setApplicationNameERK7QString',
        application,
    )

  @staticmethod
  def applicationName() -> str:
    """
    Calls Qt's 'QString QCoreApplication::applicationName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#applicationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::applicationName()
    return Rituals.call('ritual_ZN16QCoreApplication15applicationNameEv')

  @staticmethod
  @overload(str)
  def setApplicationVersion(version: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::setApplicationVersion(const QString
    &version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setApplicationVersion

    Parameters
    ----------

    version : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::setApplicationVersion(const QString &version)
    Rituals.call(
        'ritual_ZN16QCoreApplication21setApplicationVersionERK7QString',
        version,
    )

  @staticmethod
  def applicationVersion() -> str:
    """
    Calls Qt's 'QString QCoreApplication::applicationVersion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#applicationVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::applicationVersion()
    return Rituals.call('ritual_ZN16QCoreApplication18applicationVersionEv')

  @staticmethod
  @overload(bool)
  def setSetuidAllowed(allow: bool) -> None:
    """
    Calls Qt's 'void QCoreApplication::setSetuidAllowed(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setSetuidAllowed

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QCoreApplication::setSetuidAllowed(bool allow)
    Rituals.call('ritual_ZN16QCoreApplication16setSetuidAllowedEb', allow)

  @staticmethod
  def isSetuidAllowed() -> bool:
    """
    Calls Qt's 'bool QCoreApplication::isSetuidAllowed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#isSetuidAllowed
    """
    #  bool QCoreApplication::isSetuidAllowed()
    return Rituals.call('ritual_ZN16QCoreApplication15isSetuidAllowedEv')

  @staticmethod
  def instance() -> Optional[QCoreApplication]:
    """
    Calls Qt's 'QCoreApplication *QCoreApplication::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#instance

    Returns
    -------

    Optional[QCoreApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreApplication *QCoreApplication::instance()
    address = Rituals.call('ritual_ZN16QCoreApplication8instanceEv')
    return QCoreApplication._cuteAt(address)

  @staticmethod
  def instanceExists() -> bool:
    """
    Calls Qt's 'bool QCoreApplication::instanceExists()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#instanceExists
    """
    #  bool QCoreApplication::instanceExists()
    return Rituals.call('ritual_ZN16QCoreApplication14instanceExistsEv')

  @staticmethod
  def exec() -> int:
    """
    Calls Qt's 'int QCoreApplication::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#exec
    """
    #  int QCoreApplication::exec()
    return Rituals.call('ritual_ZN16QCoreApplication4execEv')

  @staticmethod
  @overload()
  @overload(QEventLoop.ProcessEventsFlags)
  def processEvents(
      flags: QEventLoop.ProcessEventsFlags = (
          QEventLoop.ProcessEventsFlags.AllEvents),
  ) -> None:
    """
    Calls Qt's 'void
    QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QEventLoop.ProcessEventsFlags.AllEvents.
    """
    #  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
    #      flags)
    Rituals.call(
        'ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17'
        'ProcessEventsFlagEE',
        flags.value,
    )

  @staticmethod
  @overload(QEventLoop.ProcessEventsFlags, int)
  def processEvents(
      flags: QEventLoop.ProcessEventsFlags,
      maxtime: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags flags, int
    maxtime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.

    maxtime : int
      Passed on as it is.
    """
    #  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
    #      flags, int maxtime)
    Rituals.call(
        'ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17'
        'ProcessEventsFlagEEi',
        flags.value, maxtime,
    )

  @staticmethod
  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sendEvent(
      receiver: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QCoreApplication::sendEvent(QObject *receiver, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#sendEvent

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplication::sendEvent(QObject *receiver, QEvent *event)
    return Rituals.call(
        'ritual_ZN16QCoreApplication9sendEventEP7QObjectP6QEvent',
        CuteMixin._addressOf(receiver), CuteMixin._addressOf(event),
    )

  @staticmethod
  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  @overload(QObject, QEvent, int)
  @overload(QObject, NoneType, int)
  @overload(NoneType, QEvent, int)
  @overload(NoneType, NoneType, int)
  def postEvent(
      receiver: Optional[QObject],
      event: Optional[QEvent],
      priority: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QCoreApplication::postEvent(QObject *receiver, QEvent
    *event, int priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#postEvent

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    priority : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCoreApplication::postEvent(QObject *receiver, QEvent *event, int
    #      priority)
    Rituals.call(
        'ritual_ZN16QCoreApplication9postEventEP7QObjectP6QEventi',
        CuteMixin._addressOf(receiver), CuteMixin._addressOf(event),
        priority,
    )

  @staticmethod
  @overload()
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, int)
  @overload(NoneType, int)
  def sendPostedEvents(
      receiver: Optional[QObject] = None,
      event_type: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QCoreApplication::sendPostedEvents(QObject *receiver,
    int event_type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#sendPostedEvents

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    event_type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCoreApplication::sendPostedEvents(QObject *receiver, int
    #      event_type)
    Rituals.call(
        'ritual_ZN16QCoreApplication16sendPostedEventsEP7QObjecti',
        CuteMixin._addressOf(receiver), event_type,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, int)
  @overload(NoneType, int)
  def removePostedEvents(
      receiver: Optional[QObject],
      eventType: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QCoreApplication::removePostedEvents(QObject *receiver,
    int eventType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#removePostedEvents

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    eventType : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCoreApplication::removePostedEvents(QObject *receiver, int
    #      eventType)
    Rituals.call(
        'ritual_ZN16QCoreApplication18removePostedEventsEP7QObjecti',
        CuteMixin._addressOf(receiver), eventType,
    )

  @staticmethod
  def startingUp() -> bool:
    """
    Calls Qt's 'bool QCoreApplication::startingUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#startingUp
    """
    #  bool QCoreApplication::startingUp()
    return Rituals.call('ritual_ZN16QCoreApplication10startingUpEv')

  @staticmethod
  def closingDown() -> bool:
    """
    Calls Qt's 'bool QCoreApplication::closingDown()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#closingDown
    """
    #  bool QCoreApplication::closingDown()
    return Rituals.call('ritual_ZN16QCoreApplication11closingDownEv')

  @staticmethod
  def applicationDirPath() -> str:
    """
    Calls Qt's 'QString QCoreApplication::applicationDirPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#applicationDirPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::applicationDirPath()
    return Rituals.call('ritual_ZN16QCoreApplication18applicationDirPathEv')

  @staticmethod
  def applicationFilePath() -> str:
    """
    Calls Qt's 'QString QCoreApplication::applicationFilePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#applicationFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::applicationFilePath()
    return Rituals.call('ritual_ZN16QCoreApplication19applicationFilePathEv')

  @staticmethod
  def applicationPid() -> int:
    """
    Calls Qt's 'qint64 QCoreApplication::applicationPid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#applicationPid
    """
    #  qint64 QCoreApplication::applicationPid()
    return Rituals.call('ritual_ZN16QCoreApplication14applicationPidEv')

  @staticmethod
  @overload(str)
  def addLibraryPath(a0: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::addLibraryPath(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#addLibraryPath

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::addLibraryPath(const QString &a0)
    Rituals.call(
        'ritual_ZN16QCoreApplication14addLibraryPathERK7QString', a0,
    )

  @staticmethod
  @overload(str)
  def removeLibraryPath(a0: str) -> None:
    """
    Calls Qt's 'void QCoreApplication::removeLibraryPath(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#removeLibraryPath

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoreApplication::removeLibraryPath(const QString &a0)
    Rituals.call(
        'ritual_ZN16QCoreApplication17removeLibraryPathERK7QString', a0,
    )

  @staticmethod
  @overload(QTranslator)
  @overload(NoneType)
  def installTranslator(messageFile: Optional[QTranslator]) -> bool:
    """
    Calls Qt's 'bool QCoreApplication::installTranslator(QTranslator
    *messageFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#installTranslator

    Parameters
    ----------

    messageFile : Optional[QTranslator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplication::installTranslator(QTranslator *messageFile)
    return Rituals.call(
        'ritual_ZN16QCoreApplication17installTranslatorEP11QTranslator',
        CuteMixin._addressOf(messageFile),
    )

  @staticmethod
  @overload(QTranslator)
  @overload(NoneType)
  def removeTranslator(messageFile: Optional[QTranslator]) -> bool:
    """
    Calls Qt's 'bool QCoreApplication::removeTranslator(QTranslator
    *messageFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#removeTranslator

    Parameters
    ----------

    messageFile : Optional[QTranslator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplication::removeTranslator(QTranslator *messageFile)
    return Rituals.call(
        'ritual_ZN16QCoreApplication16removeTranslatorEP11QTranslator',
        CuteMixin._addressOf(messageFile),
    )

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, str)
  @overload(str, str, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  @overload(str, str, str, int)
  @overload(str, str, NoneType, int)
  @overload(str, NoneType, str, int)
  @overload(str, NoneType, NoneType, int)
  @overload(NoneType, str, str, int)
  @overload(NoneType, str, NoneType, int)
  @overload(NoneType, NoneType, str, int)
  @overload(NoneType, NoneType, NoneType, int)
  def translate(
      context: Optional[str],
      key: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QCoreApplication::translate(const char *context,
    const char *key, const char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#translate

    Parameters
    ----------

    context : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    key : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoreApplication::translate(const char *context, const char
    #      *key, const char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN16QCoreApplication9translateEPKcS1_S1_i',
        CuteMixin._bytesOf(context), CuteMixin._bytesOf(key),
        CuteMixin._bytesOf(disambiguation), n,
    )

  @staticmethod
  def isQuitLockEnabled() -> bool:
    """
    Calls Qt's 'bool QCoreApplication::isQuitLockEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#isQuitLockEnabled
    """
    #  bool QCoreApplication::isQuitLockEnabled()
    return Rituals.call('ritual_ZN16QCoreApplication17isQuitLockEnabledEv')

  @staticmethod
  @overload(bool)
  def setQuitLockEnabled(enabled: bool) -> None:
    """
    Calls Qt's 'void QCoreApplication::setQuitLockEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#setQuitLockEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCoreApplication::setQuitLockEnabled(bool enabled)
    Rituals.call(
        'ritual_ZN16QCoreApplication18setQuitLockEnabledEb', enabled,
    )

  @staticmethod
  def quit() -> None:
    """
    Calls Qt's 'void QCoreApplication::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#quit
    """
    #  void QCoreApplication::quit()
    Rituals.call('ritual_ZN16QCoreApplication4quitEv')

  @staticmethod
  @overload()
  @overload(int)
  def exit(retcode: int = 0) -> None:
    """
    Calls Qt's 'void QCoreApplication::exit(int retcode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#exit

    Parameters
    ----------

    retcode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCoreApplication::exit(int retcode)
    Rituals.call('ritual_ZN16QCoreApplication4exitEi', retcode)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoreApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoreApplication::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoreApplication::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QCoreApplication10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

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
  @overload(list, int)
  def __init__(self, argv: list, a2: int = 396288) -> None:
    """
    Calls Qt's 'QCoreApplication::QCoreApplication(int &argc, char **argv,
    int a2)' at once: nearly every other object of Qt can only be made after
    the application.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreapplication.html#QCoreApplication

    Parameters
    ----------

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.

    a2 : int
      Passed on as it is. May be left out, as in Qt: it is then 396288.
    """
    #  QCoreApplication::QCoreApplication(int &argc, char **argv, int a2)
    self._noteCreation(QCoreApplication, lambda: Rituals.call(
        'ritual_ZN16QCoreApplicationC1ERiPPci',
        *self._startTextsOf(argv), a2,
    ))
    self._getUglySide()

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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def notify(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCoreApplication::notify(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreapplication.html#notify

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoreApplication::notify(QObject *a0, QEvent *a1)
    return self.uglySide.call(
        'ritual_ZN16QCoreApplication6notifyEP7QObjectP6QEvent',
        self._addressOf(a0), self._addressOf(a1),
    )
