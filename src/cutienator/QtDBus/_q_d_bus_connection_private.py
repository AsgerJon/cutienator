"""
QDBusConnectionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusConnectionPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QDBusConnection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QTimerEvent, QVariant
  from . import QDBusError, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusError = WAIT['QDBusError']
  QDBusMessage = WAIT['QDBusMessage']
  QEvent = WAIT['QEvent']
  QMetaObject = WAIT['QMetaObject']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusConnectionPrivate(QObject):
  """
  The cute side of Qt's QDBusConnectionPrivate: a plain Python object
  standing in front of one C++ QDBusConnectionPrivate.

  It is built on the cute 'QObject', as Qt's QDBusConnectionPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusConnectionPrivate that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject',
  'shouldWatchService', 'unregisterObject', 'registerService',
  'unregisterService', 'postEventToThread', 'isServiceRegisteredByThread',
  'timerEvent', 'setDispatchEnabled', 'doDispatch', 'socketRead',
  'socketWrite', 'objectDestroyed', 'relaySignal',
  'serviceOwnerChangedNoLock', 'registerServiceNoLock',
  'unregisterServiceNoLock', 'handleDBusDisconnection',
  'dispatchStatusChanged', 'spyHooksFinished', 'serviceOwnerChanged',
  'callWithCallbackFailed', 'connectionCapabilities', 'd', 'q'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusConnectionPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusConnectionPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QDBusConnectionPrivate::collectAllObjects(ObjectTreeNode
    &node, QSet<QObject *> &set)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QDBusConnectionPrivate::messageNeedsSending(QDBusPendingCallPrivate
    *pcall, void *msg, int timeout)': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  51 of the 80 functions Qt declares: 23 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 15 leans on
  'QDBusConnectionPrivate; 3 leans on 'qdbus_resolve_me(char const*)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken; 3 leans on 'qDBusPropertyGet(QDBusConnectionPrivate; 2 not
  a gap; 2 leans on 'qDBusParametersForMethod(QMetaMethod const&,
  QList<QMetaType>&, QString&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 the compiler refuses
  its ritual as it would be written here; 1 leans on
  'qDBusCreateAdaptorConnector(QObject*)', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken; 1 leans on
  'QDBusConnectionManager.

  What to expect
  --------------

  - The C++ QDBusConnectionPrivate is created at the first use, not by
    'QDBusConnectionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusConnectionPrivate.
  - Qt tells when it has removed the C++ QDBusConnectionPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusConnectionPrivate that has no cute function yet,
    '__init__', 'activateCall', 'activateInternalFilters', 'activateObject',
    'activateSignal', 'addSignalHook', 'addSignalHookImpl', 'checkThread',
    'closeConnection', 'collectAllObjects', 'connectRelay', 'connectSignal',
    'createBusService', 'deliverCall', 'disconnectRelay', 'disconnectSignal',
    'enableDispatchDelayed', 'findMetaObject', 'findSlot', 'getNameOwner',
    'getNameOwnerNoCache', 'handleAuthentication', 'handleError',
    'handleMessage', 'handleObjectCall', 'handleSignal',
    'messageNeedsSending', 'prepareHook', 'prepareReply',
    'processFinishedCall', 'registerObject', 'removeSignalHook',
    'removeSignalHookImpl', 'removeSignalHookNoLock', 'send', 'sendError',
    'sendInternal', 'sendWithReply', 'sendWithReplyAsync',
    'sendWithReplyLocal', 'setConnection', 'setPeer', 'setServer',
    'unwatchService', 'watchForDBusDisconnection', 'watchService', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDBusConnectionPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ConnectionMode(CuteNum):
    """
    The enum 'QDBusConnectionPrivate::ConnectionMode' of Qt, with the 4 names
    Qt gives in it.
    """

    InvalidMode = Kee[int](0)
    ServerMode = Kee[int](1)
    ClientMode = Kee[int](2)
    PeerMode = Kee[int](3)

  class TreeNodeType(CuteNum):
    """
    The enum 'QDBusConnectionPrivate::TreeNodeType' of Qt, with the 2 names
    Qt gives in it.
    """

    Object = Kee[int](0)
    VirtualObject = Kee[int](16777216)

  #  The classes Qt writes inside QDBusConnectionPrivate, each a class in
  #  here as in C++.

  class ArgMatchRules(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusConnectionPrivate::ArgMatchRules: a plain
    Python object standing in front of one C++
    QDBusConnectionPrivate::ArgMatchRules.

    C++ hands a QDBusConnectionPrivate::ArgMatchRules around as a copy, so
    every C++ QDBusConnectionPrivate::ArgMatchRules behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QDBusConnectionPrivate::ArgMatchRules that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusConnectionPrivate::ArgMatchRules::~ArgMatchRules()': the
      destructor: Python removes its C++
      QDBusConnectionPrivate::ArgMatchRules by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QDBusConnectionPrivate::ArgMatchRules is created at the first
      use, not by 'QDBusConnectionPrivate::ArgMatchRules(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusConnectionPrivate::ArgMatchRules back gives a
      copy the ritual made for Python, in a new cute
      QDBusConnectionPrivate::ArgMatchRules.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusConnectionPrivate::ArgMatchRules'

    #  Qt's '~QDBusConnectionPrivate::ArgMatchRules()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QDBusConnectionPrivate::ArgMatchRules behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QDBusConnectionPrivate13ArgMatchRulesD1Ev')

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

    @overload(THIS)
    def __eq__(self, other: QDBusConnectionPrivate.ArgMatchRules) -> bool:
      """
      Calls Qt's 'bool
      QDBusConnectionPrivate::ArgMatchRules::operator==(const ArgMatchRules
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-argmatchrules.html

      Parameters
      ----------

      other : QDBusConnectionPrivate.ArgMatchRules
        Passed on as a value: Qt reads the C++
        QDBusConnectionPrivate::ArgMatchRules, which stays Python's own.
      """
      #  bool QDBusConnectionPrivate::ArgMatchRules::operator==(const
      #      ArgMatchRules &other) const
      return self.uglySide.call(
          'ritual_ZNK22QDBusConnectionPrivate13ArgMatchRuleseqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class ObjectTreeNode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusConnectionPrivate::ObjectTreeNode: a plain
    Python object standing in front of one C++
    QDBusConnectionPrivate::ObjectTreeNode.

    C++ hands a QDBusConnectionPrivate::ObjectTreeNode around as a copy, so
    every C++ QDBusConnectionPrivate::ObjectTreeNode behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QDBusConnectionPrivate::ObjectTreeNode that has a
    ritual and that Python can call so far, 2 names in all: '__lt__',
    'isActive'. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'bool
      QDBusConnectionPrivate::ObjectTreeNode::operator<(QStringView other)
      const': takes in Python what 'bool
      QDBusConnectionPrivate::ObjectTreeNode::operator<(const QString &other)
      const' takes.
    - Qt's 'QDBusConnectionPrivate::ObjectTreeNode::~ObjectTreeNode()': the
      destructor: Python removes its C++
      QDBusConnectionPrivate::ObjectTreeNode by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QDBusConnectionPrivate::ObjectTreeNode is created at the first
      use, not by 'QDBusConnectionPrivate::ObjectTreeNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusConnectionPrivate::ObjectTreeNode back gives a
      copy the ritual made for Python, in a new cute
      QDBusConnectionPrivate::ObjectTreeNode.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusConnectionPrivate::ObjectTreeNode'

    #  Qt's '~QDBusConnectionPrivate::ObjectTreeNode()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QDBusConnectionPrivate::ObjectTreeNode behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isActive(self) -> bool:
      """
      Calls Qt's 'bool QDBusConnectionPrivate::ObjectTreeNode::isActive()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-objecttreenode.html
      """
      #  bool QDBusConnectionPrivate::ObjectTreeNode::isActive() const
      return self.uglySide.call(
          'ritual_ZNK22QDBusConnectionPrivate14ObjectTreeNode8isActiveEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def __lt__(self, other: str) -> bool:
      """
      Calls Qt's 'bool
      QDBusConnectionPrivate::ObjectTreeNode::operator<(const QString &other)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-objecttreenode.html

      Parameters
      ----------

      other : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QDBusConnectionPrivate::ObjectTreeNode::operator<(const QString
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK22QDBusConnectionPrivate14ObjectTreeNodeltERK7QString',
          other,
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-objecttreenode.html
      """
      #  QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode()
      self._noteCreation(
          QDBusConnectionPrivate.ObjectTreeNode, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeC1Ev',
          ))

    @overload(str)
    def __init__(self, n: str) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode(const QString
      &n)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-objecttreenode.html

      Parameters
      ----------

      n : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode(const QString
      #      &n)
      self._noteCreation(
          QDBusConnectionPrivate.ObjectTreeNode, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeC1ERK7QStri'
              'ng',
              n,
          ))

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

  class SignalHook(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusConnectionPrivate::SignalHook: a plain Python
    object standing in front of one C++ QDBusConnectionPrivate::SignalHook.

    C++ hands a QDBusConnectionPrivate::SignalHook around as a copy, so every
    C++ QDBusConnectionPrivate::SignalHook behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QDBusConnectionPrivate::SignalHook yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusConnectionPrivate::SignalHook::~SignalHook()': the
      destructor: Python removes its C++ QDBusConnectionPrivate::SignalHook
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QDBusConnectionPrivate::SignalHook is created at the first use,
      not by 'QDBusConnectionPrivate::SignalHook(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusConnectionPrivate::SignalHook back gives a
      copy the ritual made for Python, in a new cute
      QDBusConnectionPrivate::SignalHook.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusConnectionPrivate::SignalHook'

    #  Qt's '~QDBusConnectionPrivate::SignalHook()'. Naming it makes this a
    #  value class: Python owns every C++ QDBusConnectionPrivate::SignalHook
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QDBusConnectionPrivate10SignalHookD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::SignalHook::SignalHook()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-signalhook.html
      """
      #  QDBusConnectionPrivate::SignalHook::SignalHook()
      self._noteCreation(
          QDBusConnectionPrivate.SignalHook, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate10SignalHookC1Ev',
          ))

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

  class WatchedServiceData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusConnectionPrivate::WatchedServiceData: a plain
    Python object standing in front of one C++
    QDBusConnectionPrivate::WatchedServiceData.

    C++ hands a QDBusConnectionPrivate::WatchedServiceData around as a copy,
    so every C++ QDBusConnectionPrivate::WatchedServiceData behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QDBusConnectionPrivate::WatchedServiceData yet. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QDBusConnectionPrivate::WatchedServiceData::~WatchedServiceData()':
      the destructor: Python removes its C++
      QDBusConnectionPrivate::WatchedServiceData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDBusConnectionPrivate::WatchedServiceData is created at the
      first use, not by 'QDBusConnectionPrivate::WatchedServiceData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusConnectionPrivate::WatchedServiceData back
      gives a copy the ritual made for Python, in a new cute
      QDBusConnectionPrivate::WatchedServiceData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusConnectionPrivate::WatchedServiceData'

    #  Qt's '~QDBusConnectionPrivate::WatchedServiceData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QDBusConnectionPrivate::WatchedServiceData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-watchedservicedata.html
      """
      #  QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData()
      self._noteCreation(
          QDBusConnectionPrivate.WatchedServiceData, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataC1Ev',
          ))

    @overload(str)
    @overload(str, int)
    def __init__(self, owner: str, refcount: int = 0) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData(const
      QString &owner, int refcount)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-watchedservicedata.html

      Parameters
      ----------

      owner : str
        Passed on as it is: a QString is made of it for the call.

      refcount : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData(const
      #      QString &owner, int refcount)
      self._noteCreation(
          QDBusConnectionPrivate.WatchedServiceData, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataC1ERK7Q'
              'Stringi',
              owner, refcount,
          ))

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

  class Watcher(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusConnectionPrivate::Watcher: a plain Python
    object standing in front of one C++ QDBusConnectionPrivate::Watcher.

    C++ hands a QDBusConnectionPrivate::Watcher around as a copy, so every
    C++ QDBusConnectionPrivate::Watcher behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QDBusConnectionPrivate::Watcher yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusConnectionPrivate::Watcher::~Watcher()': the destructor:
      Python removes its C++ QDBusConnectionPrivate::Watcher by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QDBusConnectionPrivate::Watcher is created at the first use,
      not by 'QDBusConnectionPrivate::Watcher(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusConnectionPrivate::Watcher back gives a copy
      the ritual made for Python, in a new cute
      QDBusConnectionPrivate::Watcher.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusConnectionPrivate::Watcher'

    #  Qt's '~QDBusConnectionPrivate::Watcher()'. Naming it makes this a
    #  value class: Python owns every C++ QDBusConnectionPrivate::Watcher
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QDBusConnectionPrivate7WatcherD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDBusConnectionPrivate::Watcher::Watcher()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusconnectionprivate-watcher.html#Watcher
      """
      #  QDBusConnectionPrivate::Watcher::Watcher()
      self._noteCreation(
          QDBusConnectionPrivate.Watcher, lambda: Rituals.call(
              'ritual_ZN22QDBusConnectionPrivate7WatcherC1Ev',
          ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDBusConnection)
  def d(q: QDBusConnection) -> Optional[QDBusConnectionPrivate]:
    """
    Calls Qt's 'QDBusConnectionPrivate *QDBusConnectionPrivate::d(const
    QDBusConnection &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnectionprivate.html#d

    Parameters
    ----------

    q : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    Returns
    -------

    Optional[QDBusConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusConnectionPrivate *QDBusConnectionPrivate::d(const
    #      QDBusConnection &q)
    address = Rituals.call(
        'ritual_ZN22QDBusConnectionPrivate1dERK15QDBusConnection',
        CuteMixin._valueOf(q),
    )
    return QDBusConnectionPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def q(connection: Optional[QDBusConnectionPrivate]) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection
    QDBusConnectionPrivate::q(QDBusConnectionPrivate *connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnectionprivate.html#q

    Parameters
    ----------

    connection : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnectionPrivate::q(QDBusConnectionPrivate
    #      *connection)
    address = Rituals.call(
        'ritual_ZN22QDBusConnectionPrivate1qEPS_',
        CuteMixin._addressOf(connection),
    )
    return QDBusConnection._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusConnectionPrivate'

  #  A C++ QDBusConnectionPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusConnectionPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusConnectionPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusConnectionPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusConnectionPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def connectionCapabilities(self) -> QDBusConnection.ConnectionCapabilities:
    """
    Calls Qt's 'QDBusConnection::ConnectionCapabilities
    QDBusConnectionPrivate::connectionCapabilities() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#connectionCapabilities

    Returns
    -------

    QDBusConnection.ConnectionCapabilities
      The value standing for the combination Qt gave back.
    """
    #  QDBusConnection::ConnectionCapabilities
    #      QDBusConnectionPrivate::connectionCapabilities() const
    return QDBusConnection.ConnectionCapabilities(self.uglySide.call(
        'ritual_ZNK22QDBusConnectionPrivate22connectionCapabilitiesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDispatchEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::setDispatchEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#setDispatchEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusConnectionPrivate::setDispatchEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate18setDispatchEnabledEb', enable,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate::QDBusConnectionPrivate()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: no member named 'isDebugging' in the global namespace.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.__init__' has no cute function yet. Qt's "
        "'QDBusConnectionPrivate::QDBusConnectionPrivate()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: no member named 'isDebugging' in the global "
        "namespace.")

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

  @overload(str)
  def shouldWatchService(self, service: str) -> bool:
    """
    Calls Qt's 'bool QDBusConnectionPrivate::shouldWatchService(const QString
    &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#shouldWatchService

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDBusConnectionPrivate::shouldWatchService(const QString
    #      &service)
    return self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString',
        service,
    )

  @overload(str, QDBusConnection.UnregisterMode)
  def unregisterObject(
      self,
      path: str,
      mode: QDBusConnection.UnregisterMode,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::unregisterObject(const QString
    &path, QDBusConnection::UnregisterMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#unregisterObject

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    mode : QDBusConnection.UnregisterMode
      Passed on as its number.
    """
    #  void QDBusConnectionPrivate::unregisterObject(const QString &path,
    #      QDBusConnection::UnregisterMode mode)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate16unregisterObjectERK7QStringN15Q'
        'DBusConnection14UnregisterModeE',
        path, mode.value,
    )

  @overload(str)
  def registerService(self, serviceName: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::registerService(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#registerService

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::registerService(const QString
    #      &serviceName)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate15registerServiceERK7QString',
        serviceName,
    )

  @overload(str)
  def unregisterService(self, serviceName: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::unregisterService(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#unregisterService

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::unregisterService(const QString
    #      &serviceName)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate17unregisterServiceERK7QString',
        serviceName,
    )

  @overload(int, QObject, QEvent)
  @overload(int, QObject, NoneType)
  @overload(int, NoneType, QEvent)
  @overload(int, NoneType, NoneType)
  def postEventToThread(
      self,
      action: int,
      target: Optional[QObject],
      event: Optional[QEvent],
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::postEventToThread(int action,
    QObject *target, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#postEventToThread

    Parameters
    ----------

    action : int
      Passed on as it is.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusConnectionPrivate::postEventToThread(int action, QObject
    #      *target, QEvent *event)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate17postEventToThreadEiP7QObjectP6Q'
        'Event',
        action, self._addressOf(target, 'QObject'), self._addressOf(event),
    )

  @overload(str)
  def isServiceRegisteredByThread(self, serviceName: str) -> bool:
    """
    Calls Qt's 'bool
    QDBusConnectionPrivate::isServiceRegisteredByThread(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDBusConnectionPrivate::isServiceRegisteredByThread(const QString
    #      &serviceName)
    return self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate27isServiceRegisteredByThreadERK7'
        'QString',
        serviceName,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate10timerEventEP11QTimerEvent',
        self._addressOf(e),
    )

  def doDispatch(self) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::doDispatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#doDispatch
    """
    #  void QDBusConnectionPrivate::doDispatch()
    self.uglySide.call('ritual_ZN22QDBusConnectionPrivate10doDispatchEv')

  @overload(int)
  def socketRead(self, a0: int) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::socketRead(qintptr a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#socketRead

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QDBusConnectionPrivate::socketRead(qintptr a0)
    self.uglySide.call('ritual_ZN22QDBusConnectionPrivate10socketReadEx', a0)

  @overload(int)
  def socketWrite(self, a0: int) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::socketWrite(qintptr a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#socketWrite

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QDBusConnectionPrivate::socketWrite(qintptr a0)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate11socketWriteEx', a0,
    )

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::objectDestroyed(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#objectDestroyed

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusConnectionPrivate::objectDestroyed(QObject *o)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate15objectDestroyedEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  @overload(QObject, QMetaObject, int, QList[QVariant])
  @overload(QObject, NoneType, int, QList[QVariant])
  @overload(NoneType, QMetaObject, int, QList[QVariant])
  @overload(NoneType, NoneType, int, QList[QVariant])
  def relaySignal(
      self,
      obj: Optional[QObject],
      a1: Optional[QMetaObject],
      signalId: int,
      args: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::relaySignal(QObject *obj, const
    QMetaObject *a1, int signalId, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#relaySignal

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signalId : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusConnectionPrivate::relaySignal(QObject *obj, const
    #      QMetaObject *a1, int signalId, const QVariantList &args)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate11relaySignalEP7QObjectPK11QMetaO'
        'bjectiRK5QListI8QVariantE',
        self._addressOf(obj, 'QObject'), self._addressOf(a1, 'QMetaObject'),
        signalId, self._valueOf(args),
    )

  @overload(str, str, str)
  def serviceOwnerChangedNoLock(
      self,
      name: str,
      oldOwner: str,
      newOwner: str,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::serviceOwnerChangedNoLock(const
    QString &name, const QString &oldOwner, const QString &newOwner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    oldOwner : str
      Passed on as it is: a QString is made of it for the call.

    newOwner : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::serviceOwnerChangedNoLock(const QString
    #      &name, const QString &oldOwner, const QString &newOwner)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate25serviceOwnerChangedNoLockERK7QS'
        'tringS2_S2_',
        name, oldOwner, newOwner,
    )

  @overload(str)
  def registerServiceNoLock(self, serviceName: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::registerServiceNoLock(const
    QString &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#registerServiceNoLock

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::registerServiceNoLock(const QString
    #      &serviceName)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate21registerServiceNoLockERK7QStrin'
        'g',
        serviceName,
    )

  @overload(str)
  def unregisterServiceNoLock(self, serviceName: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::unregisterServiceNoLock(const
    QString &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::unregisterServiceNoLock(const QString
    #      &serviceName)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate23unregisterServiceNoLockERK7QStr'
        'ing',
        serviceName,
    )

  def handleDBusDisconnection(self) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::handleDBusDisconnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html
    """
    #  void QDBusConnectionPrivate::handleDBusDisconnection()
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate23handleDBusDisconnectionEv',
    )

  def dispatchStatusChanged(self) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::dispatchStatusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#dispatchStatusChanged
    """
    #  void QDBusConnectionPrivate::dispatchStatusChanged()
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate21dispatchStatusChangedEv',
    )

  @overload(QDBusMessage)
  def spyHooksFinished(self, msg: QDBusMessage) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::spyHooksFinished(const
    QDBusMessage &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#spyHooksFinished

    Parameters
    ----------

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QDBusConnectionPrivate::spyHooksFinished(const QDBusMessage &msg)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate16spyHooksFinishedERK12QDBusMessa'
        'ge',
        self._valueOf(msg),
    )

  @overload(str, str, str)
  def serviceOwnerChanged(
      self,
      name: str,
      oldOwner: str,
      newOwner: str,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::serviceOwnerChanged(const
    QString &name, const QString &oldOwner, const QString &newOwner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#serviceOwnerChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    oldOwner : str
      Passed on as it is: a QString is made of it for the call.

    newOwner : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionPrivate::serviceOwnerChanged(const QString &name,
    #      const QString &oldOwner, const QString &newOwner)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate19serviceOwnerChangedERK7QStringS'
        '2_S2_',
        name, oldOwner, newOwner,
    )

  @overload(QDBusError, QDBusMessage)
  def callWithCallbackFailed(
      self,
      error: QDBusError,
      message: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionPrivate::callWithCallbackFailed(const
    QDBusError &error, const QDBusMessage &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionprivate.html#callWithCallbackFailed

    Parameters
    ----------

    error : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QDBusConnectionPrivate::callWithCallbackFailed(const QDBusError
    #      &error, const QDBusMessage &message)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionPrivate22callWithCallbackFailedERK10QDBu'
        'sErrorRK12QDBusMessage',
        self._valueOf(error), self._valueOf(message),
    )

  @staticmethod
  def activateCall(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::activateCall(QObject *object,
    QDBusConnection::RegisterOptions flags, const QDBusMessage &msg)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no member named 'findSlot' in the global namespace.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.activateCall' has no cute function yet. "
        "Qt's 'bool QDBusConnectionPrivate::activateCall(QObject *object, "
        "QDBusConnection::RegisterOptions flags, const QDBusMessage &msg)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no member named 'findSlot' in the "
        "global namespace.")

  @staticmethod
  def activateInternalFilters(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::activateInternalFilters(const
    ObjectTreeNode &node, const QDBusMessage &msg)': leans on
    'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&,
    QDBusMessage const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.activateInternalFilters' has no cute "
        "function yet. Qt's 'bool "
        "QDBusConnectionPrivate::activateInternalFilters(const "
        "ObjectTreeNode &node, const QDBusMessage &msg)': leans on "
        "'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&, "
        "QDBusMessage const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def activateObject(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::activateObject(ObjectTreeNode &node,
    const QDBusMessage &msg, int pathStartPos)': leans on
    'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&,
    QDBusMessage const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.activateObject' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::activateObject(ObjectTreeNode "
        "&node, const QDBusMessage &msg, int pathStartPos)': leans on "
        "'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&, "
        "QDBusMessage const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def activateSignal(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::activateSignal(const SignalHook &hook,
    const QDBusMessage &msg)': leans on
    'QDBusConnectionPrivate::deliverCall(QObject*, QDBusMessage const&,
    QList<QMetaType> const&, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.activateSignal' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::activateSignal(const SignalHook "
        "&hook, const QDBusMessage &msg)': leans on "
        "'QDBusConnectionPrivate::deliverCall(QObject*, QDBusMessage "
        "const&, QList<QMetaType> const&, int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def addSignalHook(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::addSignalHook(const QString &key,
    const SignalHook &hook)': leans on
    'QDBusConnectionPrivate::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.addSignalHook' has no cute function yet. "
        "Qt's 'bool QDBusConnectionPrivate::addSignalHook(const QString "
        "&key, const SignalHook &hook)': leans on "
        "'QDBusConnectionPrivate::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def addSignalHookImpl(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::addSignalHookImpl(const QString &key,
    const SignalHook &hook)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'qDBusDebug'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.addSignalHookImpl' has no cute function "
        "yet. Qt's 'bool QDBusConnectionPrivate::addSignalHookImpl(const "
        "QString &key, const SignalHook &hook)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qDBusDebug'.")

  @staticmethod
  def checkThread(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::checkThread()': leans on
    'QDBusConnectionManager::instance()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.checkThread' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::checkThread()': leans on "
        "'QDBusConnectionManager::instance()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def closeConnection(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::closeConnection()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'server_slot'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.closeConnection' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::closeConnection()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'server_slot'.")

  @staticmethod
  def collectAllObjects(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::collectAllObjects(ObjectTreeNode
    &node, QSet<QObject *> &set)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.collectAllObjects' has no cute function "
        "yet. Qt's 'void "
        "QDBusConnectionPrivate::collectAllObjects(ObjectTreeNode &node, "
        "QSet<QObject *> &set)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def connectRelay(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::connectRelay(const QString &service,
    const QString &path, const QString &interface, QDBusAbstractInterface
    *receiver, const QMetaMethod &signal)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'dbusIntegration'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.connectRelay' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::connectRelay(const QString "
        "&service, const QString &path, const QString &interface, "
        "QDBusAbstractInterface *receiver, const QMetaMethod &signal)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'dbusIntegration'.")

  @staticmethod
  def connectSignal(*__, **_) -> Never:
    """
    - Qt's 'bool QDBusConnectionPrivate::connectSignal(const QString
      &service, const QString &path, const QString &interface, const QString
      &name, const ArgMatchRules &argumentMatch, const QString &signature,
      QObject *receiver, const char *slot)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file: use
      of undeclared identifier 'dbusIntegration'.
    - Qt's 'bool QDBusConnectionPrivate::connectSignal(const QString
      &service, const QString &path, const QString &interface, const QString
      &name, const QStringList &argumentMatch, const QString &signature,
      QObject *receiver, const char *slot)': leans on
      'QDBusConnectionPrivate::connectSignal(QString const&, QString const&,
      QString const&, QString const&, QDBusConnectionPrivate::ArgMatchRules
      const&, QString const&, QObject*, char const*)', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.connectSignal' has no cute function yet. "
        "Qt's 'bool QDBusConnectionPrivate::connectSignal(const QString "
        "&service, const QString &path, const QString &interface, const "
        "QString &name, const ArgMatchRules &argumentMatch, const QString "
        "&signature, QObject *receiver, const char *slot)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'dbusIntegration'. Qt's 'bool "
        "QDBusConnectionPrivate::connectSignal(const QString &service, "
        "const QString &path, const QString &interface, const QString "
        "&name, const QStringList &argumentMatch, const QString &signature, "
        "QObject *receiver, const char *slot)': leans on "
        "'QDBusConnectionPrivate::connectSignal(QString const&, QString "
        "const&, QString const&, QString const&, "
        "QDBusConnectionPrivate::ArgMatchRules const&, QString const&, "
        "QObject*, char const*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createBusService(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::createBusService()': leans on
    'QDBusConnectionPrivate::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.createBusService' has no cute function "
        "yet. Qt's 'void QDBusConnectionPrivate::createBusService()': leans "
        "on 'QDBusConnectionPrivate::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def deliverCall(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::deliverCall(QObject *object, const
    QDBusMessage &msg, const QList<QMetaType> &metaTypes, int slotIdx)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qDBusDebug'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.deliverCall' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::deliverCall(QObject *object, "
        "const QDBusMessage &msg, const QList<QMetaType> &metaTypes, int "
        "slotIdx)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qDBusDebug'.")

  @staticmethod
  def disconnectRelay(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::disconnectRelay(const QString
    &service, const QString &path, const QString &interface,
    QDBusAbstractInterface *receiver, const QMetaMethod &signal)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'dbusIntegration'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.disconnectRelay' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::disconnectRelay(const QString "
        "&service, const QString &path, const QString &interface, "
        "QDBusAbstractInterface *receiver, const QMetaMethod &signal)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'dbusIntegration'.")

  @staticmethod
  def disconnectSignal(*__, **_) -> Never:
    """
    - Qt's 'bool QDBusConnectionPrivate::disconnectSignal(const QString
      &service, const QString &path, const QString &interface, const QString
      &name, const ArgMatchRules &argumentMatch, const QString &signature,
      QObject *receiver, const char *slot)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file: use
      of undeclared identifier 'dbusIntegration'.
    - Qt's 'bool QDBusConnectionPrivate::disconnectSignal(const QString
      &service, const QString &path, const QString &interface, const QString
      &name, const QStringList &argumentMatch, const QString &signature,
      QObject *receiver, const char *slot)': leans on
      'QDBusConnectionPrivate::disconnectSignal(QString const&, QString
      const&, QString const&, QString const&,
      QDBusConnectionPrivate::ArgMatchRules const&, QString const&, QObject*,
      char const*)', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.disconnectSignal' has no cute function "
        "yet. Qt's 'bool QDBusConnectionPrivate::disconnectSignal(const "
        "QString &service, const QString &path, const QString &interface, "
        "const QString &name, const ArgMatchRules &argumentMatch, const "
        "QString &signature, QObject *receiver, const char *slot)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'dbusIntegration'. Qt's 'bool "
        "QDBusConnectionPrivate::disconnectSignal(const QString &service, "
        "const QString &path, const QString &interface, const QString "
        "&name, const QStringList &argumentMatch, const QString &signature, "
        "QObject *receiver, const char *slot)': leans on "
        "'QDBusConnectionPrivate::disconnectSignal(QString const&, QString "
        "const&, QString const&, QString const&, "
        "QDBusConnectionPrivate::ArgMatchRules const&, QString const&, "
        "QObject*, char const*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def enableDispatchDelayed(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::enableDispatchDelayed(QObject
    *context)': leans on 'QDBusConnectionPrivate::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.enableDispatchDelayed' has no cute "
        "function yet. Qt's 'void "
        "QDBusConnectionPrivate::enableDispatchDelayed(QObject *context)': "
        "leans on 'QDBusConnectionPrivate::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def findMetaObject(*__, **_) -> Never:
    """
    Qt's 'QDBusMetaObject *QDBusConnectionPrivate::findMetaObject(const
    QString &service, const QString &path, const QString &interface,
    QDBusError &error)': leans on
    'QDBusConnectionPrivate::sendWithReply(QDBusMessage const&,
    QDBus::CallMode, int)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.findMetaObject' has no cute function yet. "
        "Qt's 'QDBusMetaObject "
        "*QDBusConnectionPrivate::findMetaObject(const QString &service, "
        "const QString &path, const QString &interface, QDBusError "
        "&error)': leans on "
        "'QDBusConnectionPrivate::sendWithReply(QDBusMessage const&, "
        "QDBus::CallMode, int)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def findSlot(*__, **_) -> Never:
    """
    Qt's 'int QDBusConnectionPrivate::findSlot(QObject *obj, const QByteArray
    &normalizedName, QList<QMetaType> &params, QString &errorMsg)': leans on
    'qDBusParametersForMethod(QMetaMethod const&, QList<QMetaType>&,
    QString&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.findSlot' has no cute function yet. Qt's "
        "'int QDBusConnectionPrivate::findSlot(QObject *obj, const "
        "QByteArray &normalizedName, QList<QMetaType> &params, QString "
        "&errorMsg)': leans on 'qDBusParametersForMethod(QMetaMethod "
        "const&, QList<QMetaType>&, QString&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def getNameOwner(*__, **_) -> Never:
    """
    Qt's 'QString QDBusConnectionPrivate::getNameOwner(const QString
    &service)': leans on 'qdbus_resolve_me(char const*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.getNameOwner' has no cute function yet. "
        "Qt's 'QString QDBusConnectionPrivate::getNameOwner(const QString "
        "&service)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def getNameOwnerNoCache(*__, **_) -> Never:
    """
    Qt's 'QString QDBusConnectionPrivate::getNameOwnerNoCache(const QString
    &service)': leans on 'qdbus_resolve_me(char const*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.getNameOwnerNoCache' has no cute function "
        "yet. Qt's 'QString "
        "QDBusConnectionPrivate::getNameOwnerNoCache(const QString "
        "&service)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleAuthentication(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::handleAuthentication()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: no member named 'connectionCapabilities' in the global
    namespace.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.handleAuthentication' has no cute function "
        "yet. Qt's 'void QDBusConnectionPrivate::handleAuthentication()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no member named "
        "'connectionCapabilities' in the global namespace.")

  @staticmethod
  def handleError(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::handleError(const QDBusErrorInternal
    &error)': leans on 'qdbus_resolve_me(char const*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.handleError' has no cute function yet. "
        "Qt's 'bool QDBusConnectionPrivate::handleError(const "
        "QDBusErrorInternal &error)': leans on 'qdbus_resolve_me(char "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def handleMessage(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::handleMessage(const QDBusMessage
    &msg)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'qDBusDebug'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.handleMessage' has no cute function yet. "
        "Qt's 'bool QDBusConnectionPrivate::handleMessage(const "
        "QDBusMessage &msg)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qDBusDebug'.")

  @staticmethod
  def handleObjectCall(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::handleObjectCall(const QDBusMessage
    &message)': leans on
    'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&,
    QDBusMessage const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.handleObjectCall' has no cute function "
        "yet. Qt's 'void QDBusConnectionPrivate::handleObjectCall(const "
        "QDBusMessage &message)': leans on "
        "'qDBusPropertyGet(QDBusConnectionPrivate::ObjectTreeNode const&, "
        "QDBusMessage const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def handleSignal(*__, **_) -> Never:
    """
    - Qt's 'void QDBusConnectionPrivate::handleSignal(const QString &key,
      const QDBusMessage &msg)': leans on
      'QDBusConnectionPrivate::deliverCall(QObject*, QDBusMessage const&,
      QList<QMetaType> const&, int)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'void QDBusConnectionPrivate::handleSignal(const QDBusMessage
      &msg)': leans on 'QDBusConnectionPrivate::deliverCall(QObject*,
      QDBusMessage const&, QList<QMetaType> const&, int)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.handleSignal' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::handleSignal(const QString "
        "&key, const QDBusMessage &msg)': leans on "
        "'QDBusConnectionPrivate::deliverCall(QObject*, QDBusMessage "
        "const&, QList<QMetaType> const&, int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QDBusConnectionPrivate::handleSignal(const "
        "QDBusMessage &msg)': leans on "
        "'QDBusConnectionPrivate::deliverCall(QObject*, QDBusMessage "
        "const&, QList<QMetaType> const&, int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def messageNeedsSending(*__, **_) -> Never:
    """
    Qt's 'void
    QDBusConnectionPrivate::messageNeedsSending(QDBusPendingCallPrivate
    *pcall, void *msg, int timeout)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.messageNeedsSending' has no cute function "
        "yet. Qt's 'void "
        "QDBusConnectionPrivate::messageNeedsSending(QDBusPendingCallPrivate"
        " *pcall, void *msg, int timeout)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def prepareHook(*__, **_) -> Never:
    """
    Qt's 'bool
    QDBusConnectionPrivate::prepareHook(QDBusConnectionPrivate::SignalHook
    &hook, QString &key, const QString &service, const QString &path, const
    QString &interface, const QString &name, const ArgMatchRules &argMatch,
    QObject *receiver, const char *signal, int minMIdx, bool buildSignature,
    QString &errorMsg)': leans on 'qDBusParametersForMethod(QMetaMethod
    const&, QList<QMetaType>&, QString&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.prepareHook' has no cute function yet. "
        "Qt's 'bool "
        "QDBusConnectionPrivate::prepareHook(QDBusConnectionPrivate::SignalH"
        "ook &hook, QString &key, const QString &service, const QString "
        "&path, const QString &interface, const QString &name, const "
        "ArgMatchRules &argMatch, QObject *receiver, const char *signal, "
        "int minMIdx, bool buildSignature, QString &errorMsg)': leans on "
        "'qDBusParametersForMethod(QMetaMethod const&, QList<QMetaType>&, "
        "QString&)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def prepareReply(*__, **_) -> Never:
    """
    Qt's 'QDBusCallDeliveryEvent
    *QDBusConnectionPrivate::prepareReply(QDBusConnectionPrivate *target,
    QObject *object, int idx, const QList<QMetaType> &metaTypes, const
    QDBusMessage &msg)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'DIRECT_DELIVERY'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.prepareReply' has no cute function yet. "
        "Qt's 'QDBusCallDeliveryEvent "
        "*QDBusConnectionPrivate::prepareReply(QDBusConnectionPrivate "
        "*target, QObject *object, int idx, const QList<QMetaType> "
        "&metaTypes, const QDBusMessage &msg)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'DIRECT_DELIVERY'.")

  @staticmethod
  def processFinishedCall(*__, **_) -> Never:
    """
    Qt's 'void
    QDBusConnectionPrivate::processFinishedCall(QDBusPendingCallPrivate
    *call)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'qDBusDebug'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.processFinishedCall' has no cute function "
        "yet. Qt's 'void "
        "QDBusConnectionPrivate::processFinishedCall(QDBusPendingCallPrivate"
        " *call)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qDBusDebug'.")

  @staticmethod
  def registerObject(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::registerObject(const ObjectTreeNode
    *node)': leans on 'qDBusCreateAdaptorConnector(QObject*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.registerObject' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::registerObject(const "
        "ObjectTreeNode *node)': leans on "
        "'qDBusCreateAdaptorConnector(QObject*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeSignalHook(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::removeSignalHook(const QString &key,
    const SignalHook &hook)': leans on
    'QDBusConnectionPrivate::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.removeSignalHook' has no cute function "
        "yet. Qt's 'bool QDBusConnectionPrivate::removeSignalHook(const "
        "QString &key, const SignalHook &hook)': leans on "
        "'QDBusConnectionPrivate::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeSignalHookImpl(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::removeSignalHookImpl(const QString
    &key, const SignalHook &hook)': leans on
    'QDBusConnectionPrivate::removeSignalHookNoLock(QMultiHash<QString,
    QDBusConnectionPrivate::SignalHook>::iterator)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.removeSignalHookImpl' has no cute function "
        "yet. Qt's 'bool QDBusConnectionPrivate::removeSignalHookImpl(const "
        "QString &key, const SignalHook &hook)': leans on "
        "'QDBusConnectionPrivate::removeSignalHookNoLock(QMultiHash<QString,"
        " QDBusConnectionPrivate::SignalHook>::iterator)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def removeSignalHookNoLock(*__, **_) -> Never:
    """
    Qt's 'SignalHookHash::Iterator
    QDBusConnectionPrivate::removeSignalHookNoLock(SignalHookHash::Iterator
    it)': the compiler refuses its ritual as it would be written here: use of
    undeclared identifier 'SignalHookHash'; did you mean
    'CuteQDBusConnectionPrivate::SignalHookHash'?.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.removeSignalHookNoLock' has no cute "
        "function yet. Qt's 'SignalHookHash::Iterator "
        "QDBusConnectionPrivate::removeSignalHookNoLock(SignalHookHash::Iter"
        "ator it)': the compiler refuses its ritual as it would be written "
        "here: use of undeclared identifier 'SignalHookHash'; did you mean "
        "'CuteQDBusConnectionPrivate::SignalHookHash'?.")

  @staticmethod
  def send(*__, **_) -> Never:
    """
    Qt's 'bool QDBusConnectionPrivate::send(const QDBusMessage &message)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'dbusIntegration'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.send' has no cute function yet. Qt's 'bool "
        "QDBusConnectionPrivate::send(const QDBusMessage &message)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'dbusIntegration'.")

  @staticmethod
  def sendError(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::sendError(const QDBusMessage &msg,
    QDBusError::ErrorType code)': leans on
    'QDBusConnectionPrivate::send(QDBusMessage const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.sendError' has no cute function yet. Qt's "
        "'void QDBusConnectionPrivate::sendError(const QDBusMessage &msg, "
        "QDBusError::ErrorType code)': leans on "
        "'QDBusConnectionPrivate::send(QDBusMessage const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def sendInternal(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::sendInternal(QDBusPendingCallPrivate
    *pcall, void *msg, int timeout)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qDBusResultReceived'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.sendInternal' has no cute function yet. "
        "Qt's 'void "
        "QDBusConnectionPrivate::sendInternal(QDBusPendingCallPrivate "
        "*pcall, void *msg, int timeout)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qDBusResultReceived'.")

  @staticmethod
  def sendWithReply(*__, **_) -> Never:
    """
    Qt's 'QDBusMessage QDBusConnectionPrivate::sendWithReply(const
    QDBusMessage &message, QDBus::CallMode mode, int timeout)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'QDBusBlockingCallWatcher'; did you mean
    'QDBusPendingCallWatcher'?.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.sendWithReply' has no cute function yet. "
        "Qt's 'QDBusMessage QDBusConnectionPrivate::sendWithReply(const "
        "QDBusMessage &message, QDBus::CallMode mode, int timeout)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name "
        "'QDBusBlockingCallWatcher'; did you mean "
        "'QDBusPendingCallWatcher'?.")

  @staticmethod
  def sendWithReplyAsync(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingCallPrivate
    *QDBusConnectionPrivate::sendWithReplyAsync(const QDBusMessage &message,
    QObject *receiver, const char *returnMethod, const char *errorMethod, int
    timeout)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'dbusIntegration'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.sendWithReplyAsync' has no cute function "
        "yet. Qt's 'QDBusPendingCallPrivate "
        "*QDBusConnectionPrivate::sendWithReplyAsync(const QDBusMessage "
        "&message, QObject *receiver, const char *returnMethod, const char "
        "*errorMethod, int timeout)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'dbusIntegration'.")

  @staticmethod
  def sendWithReplyLocal(*__, **_) -> Never:
    """
    Qt's 'QDBusMessage QDBusConnectionPrivate::sendWithReplyLocal(const
    QDBusMessage &message)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'qDBusDebug'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.sendWithReplyLocal' has no cute function "
        "yet. Qt's 'QDBusMessage "
        "QDBusConnectionPrivate::sendWithReplyLocal(const QDBusMessage "
        "&message)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qDBusDebug'.")

  @staticmethod
  def setConnection(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::setConnection(DBusConnection
    *connection, const QDBusErrorInternal &error)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'qDBusAddWatch'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.setConnection' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::setConnection(DBusConnection "
        "*connection, const QDBusErrorInternal &error)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qDBusAddWatch'.")

  @staticmethod
  def setPeer(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::setPeer(DBusConnection *connection,
    const QDBusErrorInternal &error)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qDBusAddWatch'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.setPeer' has no cute function yet. Qt's "
        "'void QDBusConnectionPrivate::setPeer(DBusConnection *connection, "
        "const QDBusErrorInternal &error)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qDBusAddWatch'.")

  @staticmethod
  def setServer(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::setServer(QDBusServer *object,
    DBusServer *server, const QDBusErrorInternal &error)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'server_slot'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.setServer' has no cute function yet. Qt's "
        "'void QDBusConnectionPrivate::setServer(QDBusServer *object, "
        "DBusServer *server, const QDBusErrorInternal &error)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'server_slot'.")

  @staticmethod
  def unwatchService(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::unwatchService(const QString &service,
    QDBusServiceWatcher::WatchMode mode, QObject *obj, const char *member)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'matchArgsForService'.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.unwatchService' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::unwatchService(const QString "
        "&service, QDBusServiceWatcher::WatchMode mode, QObject *obj, const "
        "char *member)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'matchArgsForService'.")

  @staticmethod
  def watchForDBusDisconnection(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::watchForDBusDisconnection()': leans on
    'QDBusConnectionPrivate::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.watchForDBusDisconnection' has no cute "
        "function yet. Qt's 'void "
        "QDBusConnectionPrivate::watchForDBusDisconnection()': leans on "
        "'QDBusConnectionPrivate::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def watchService(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionPrivate::watchService(const QString &service,
    QDBusServiceWatcher::WatchMode mode, QObject *obj, const char *member)':
    leans on 'QDBusConnectionPrivate::connectSignal(QString const&, QString
    const&, QString const&, QString const&,
    QDBusConnectionPrivate::ArgMatchRules const&, QString const&, QObject*,
    char const*)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionPrivate.watchService' has no cute function yet. "
        "Qt's 'void QDBusConnectionPrivate::watchService(const QString "
        "&service, QDBusServiceWatcher::WatchMode mode, QObject *obj, const "
        "char *member)': leans on "
        "'QDBusConnectionPrivate::connectSignal(QString const&, QString "
        "const&, QString const&, QString const&, "
        "QDBusConnectionPrivate::ArgMatchRules const&, QString const&, "
        "QObject*, char const*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
