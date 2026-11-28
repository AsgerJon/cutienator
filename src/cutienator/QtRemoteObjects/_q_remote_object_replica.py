"""
QRemoteObjectReplica binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectreplica.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMetaObject, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVariant
  from . import QRemoteObjectNode, QRemoteObjectPendingCall
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRemoteObjectNode = WAIT['QRemoteObjectNode']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectReplica(QObject):
  """
  The cute side of Qt's QRemoteObjectReplica: a plain Python object standing
  in front of one C++ QRemoteObjectReplica.

  It is built on the cute 'QObject', as Qt's QRemoteObjectReplica is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectReplica that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'isReplicaValid', 'waitForSource', 'isInitialized', 'state', 'node',
  'setNode', 'initialized', 'notified', 'stateChanged', 'initialize', 'send',
  'sendWithReply', 'setChild', 'propAsVariant', 'persistProperties',
  'retrieveProperties', 'initializeNode'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectReplica::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QRemoteObjectReplica::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectReplica::~QRemoteObjectReplica()': the destructor:
    Python never removes a C++ QRemoteObjectReplica.
  - Qt's 'QRemoteObjectReplica::QRemoteObjectReplica(ConstructorType t)':
    names the enum 'QRemoteObjectReplica::ConstructorType', whose class
    cannot be named here.
  - Qt's 'QRemoteObjectReplica::QRemoteObjectReplica(QObjectPrivate &dptr,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRemoteObjectReplica::setProperties(QVariantList &&a0)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectReplica is created at the first use, not by
    'QRemoteObjectReplica(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectReplica.
  - Qt tells when it has removed the C++ QRemoteObjectReplica. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectReplica that has no cute function yet,
    '__init__', 'setProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRemoteObjectReplica, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QRemoteObjectReplica::State' of Qt, with the 5 names Qt gives
    in it.
    """

    Uninitialized = Kee[int](0)
    Default = Kee[int](1)
    Valid = Kee[int](2)
    Suspect = Kee[int](3)
    SignatureMismatch = Kee[int](4)

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
    Calls Qt's 'QString QRemoteObjectReplica::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#tr

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
    #  QString QRemoteObjectReplica::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QRemoteObjectReplica2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectReplica'

  #  A C++ QRemoteObjectReplica Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectReplica'

  #  The functions Qt calls itself that QRemoteObjectReplica is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setNode': (
          ('_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtRemoteObjects:QRemoteObjectNode'),
           )),
      ),
      'initialize': (
          ('_ZN20QRemoteObjectReplica10initializeEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectReplica::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectReplica::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def isReplicaValid(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplica::isReplicaValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#isReplicaValid
    """
    #  bool QRemoteObjectReplica::isReplicaValid() const
    return self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica14isReplicaValidEv',
    )

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplica::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#isInitialized
    """
    #  bool QRemoteObjectReplica::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica13isInitializedEv',
    )

  def state(self) -> State:
    """
    Calls Qt's 'State QRemoteObjectReplica::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QRemoteObjectReplica::state() const
    return QRemoteObjectReplica.State(self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica5stateEv',
    ))

  def node(self) -> Optional[QRemoteObjectNode]:
    """
    Calls Qt's 'QRemoteObjectNode *QRemoteObjectReplica::node() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#node

    Returns
    -------

    Optional[QRemoteObjectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNode *QRemoteObjectReplica::node() const
    address = self.uglySide.call('ritual_ZNK20QRemoteObjectReplica4nodeEv')
    from . import QRemoteObjectNode
    return QRemoteObjectNode._cuteAt(address)

  @overload(int)
  def propAsVariant(self, i: int) -> QVariant:
    """
    Calls Qt's 'const QVariant QRemoteObjectReplica::propAsVariant(int i)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#propAsVariant

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant QRemoteObjectReplica::propAsVariant(int i) const
    address = self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica13propAsVariantEi', i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str, QByteArray)
  def retrieveProperties(
      self,
      repName: str,
      repSig: QByteArray,
  ) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QRemoteObjectReplica::retrieveProperties(const
    QString &repName, const QByteArray &repSig) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#retrieveProperties

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QRemoteObjectReplica::retrieveProperties(const QString
    #      &repName, const QByteArray &repSig) const
    address = self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica18retrievePropertiesERK7QStringRK1'
        '0QByteArray',
        repName, self._valueOf(repSig),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRemoteObjectNode)
  @overload(NoneType)
  def setNode(self, node: Optional[QRemoteObjectNode]) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#setNode

    Parameters
    ----------

    node : Optional[QRemoteObjectNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
    ritual = 'ritual_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(int, QVariant)
  def setChild(self, i: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::setChild(int i, const QVariant
    &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#setChild

    Parameters
    ----------

    i : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QRemoteObjectReplica::setChild(int i, const QVariant &a1)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica8setChildEiRK8QVariant',
        i, self._valueOf(a1),
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
    - Qt's 'QRemoteObjectReplica::QRemoteObjectReplica(ConstructorType t)':
      names the enum 'QRemoteObjectReplica::ConstructorType', whose class
      cannot be named here.
    - Qt's 'QRemoteObjectReplica::QRemoteObjectReplica(QObjectPrivate &dptr,
      QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectReplica.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectReplica::QRemoteObjectReplica(ConstructorType t)': "
        "names the enum 'QRemoteObjectReplica::ConstructorType', whose "
        "class cannot be named here. Qt's "
        "'QRemoteObjectReplica::QRemoteObjectReplica(QObjectPrivate &dptr, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  @overload()
  @overload(int)
  def waitForSource(self, timeout: int = 30000) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplica::waitForSource(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#waitForSource

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QRemoteObjectReplica::waitForSource(int timeout)
    return self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica13waitForSourceEi', timeout,
    )

  def initialized(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::initialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#initialized
    """
    #  void QRemoteObjectReplica::initialized()
    self.uglySide.call('ritual_ZN20QRemoteObjectReplica11initializedEv')

  def notified(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::notified()'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#notified
    """
    #  void QRemoteObjectReplica::notified()
    self.uglySide.call('ritual_ZN20QRemoteObjectReplica8notifiedEv')

  @overload(State, State)
  def stateChanged(self, state: State, oldState: State) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::stateChanged(State state, State
    oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#stateChanged

    Parameters
    ----------

    state : State
      Passed on as its number.

    oldState : State
      Passed on as its number.
    """
    #  void QRemoteObjectReplica::stateChanged(State state, State oldState)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica12stateChangedENS_5StateES0_',
        state.value, oldState.value,
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#initialize
    """
    #  void QRemoteObjectReplica::initialize()
    ritual = 'ritual_ZN20QRemoteObjectReplica10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QRemoteObjectReplica10initializeEv'
    self.uglySide.call(ritual)

  @overload(QMetaObject.Call, int, QList[QVariant])
  def send(
      self,
      call: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::send(QMetaObject::Call call, int
    index, const QVariantList &args)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectreplica.html#send

    Parameters
    ----------

    call : QMetaObject.Call
      Passed on as its number.

    index : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QRemoteObjectReplica::send(QMetaObject::Call call, int index,
    #      const QVariantList &args)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica4sendEN11QMetaObject4CallEiRK5QList'
        'I8QVariantE',
        call.value, index, self._valueOf(args),
    )

  @overload(QMetaObject.Call, int, QList[QVariant])
  def sendWithReply(
      self,
      call: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
  ) -> QRemoteObjectPendingCall:
    """
    Calls Qt's 'QRemoteObjectPendingCall
    QRemoteObjectReplica::sendWithReply(QMetaObject::Call call, int index,
    const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#sendWithReply

    Parameters
    ----------

    call : QMetaObject.Call
      Passed on as its number.

    index : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QRemoteObjectPendingCall
      A new cute QRemoteObjectPendingCall around the copy Qt gave back.
      Python owns it.
    """
    #  QRemoteObjectPendingCall
    #      QRemoteObjectReplica::sendWithReply(QMetaObject::Call call, int
    #      index, const QVariantList &args)
    address = self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica13sendWithReplyEN11QMetaObject4Call'
        'EiRK5QListI8QVariantE',
        call.value, index, self._valueOf(args),
    )
    from . import QRemoteObjectPendingCall
    return QRemoteObjectPendingCall._cuteOwning(address)

  @overload(str, QByteArray, QList[QVariant])
  def persistProperties(
      self,
      repName: str,
      repSig: QByteArray,
      props: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::persistProperties(const QString
    &repName, const QByteArray &repSig, const QVariantList &props) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#persistProperties

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    props : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QRemoteObjectReplica::persistProperties(const QString &repName,
    #      const QByteArray &repSig, const QVariantList &props) const
    self.uglySide.call(
        'ritual_ZNK20QRemoteObjectReplica17persistPropertiesERK7QStringRK10'
        'QByteArrayRK5QListI8QVariantE',
        repName, self._valueOf(repSig), self._valueOf(props),
    )

  @overload(QRemoteObjectNode)
  @overload(NoneType)
  @overload(QRemoteObjectNode, str)
  @overload(NoneType, str)
  def initializeNode(
      self,
      node: Optional[QRemoteObjectNode],
      name: str = '',
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplica::initializeNode(QRemoteObjectNode
    *node, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplica.html#initializeNode

    Parameters
    ----------

    node : Optional[QRemoteObjectNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QRemoteObjectReplica::initializeNode(QRemoteObjectNode *node,
    #      const QString &name)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectReplica14initializeNodeEP17QRemoteObjectNo'
        'deRK7QString',
        self._addressOf(node), name,
    )

  @staticmethod
  def setProperties(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectReplica::setProperties(QVariantList &&a0)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectReplica.setProperties' has no cute function yet. "
        "Qt's 'void QRemoteObjectReplica::setProperties(QVariantList "
        "&&a0)': takes a type Python has no way to hand over yet.")
