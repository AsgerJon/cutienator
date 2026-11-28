"""
QRemoteObjectReplicaImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectReplicaImplementation to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QMetaObject, QObject
from . import QRemoteObjectReplica, QReplicaImplementationInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectNode, QRemoteObjectPendingCall
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectPendingCall = WAIT['QRemoteObjectPendingCall']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectReplicaImplementation(QObject, QReplicaImplementationInterface):
  """
  The cute side of Qt's QRemoteObjectReplicaImplementation: a plain Python
  object standing in front of one C++ QRemoteObjectReplicaImplementation.

  It is built on the cute 'QObject', as Qt's
  QRemoteObjectReplicaImplementation is built on Qt's QObject, and has
  everything that class has. It is built on the cute
  'QReplicaImplementationInterface' as well, as Qt's
  QRemoteObjectReplicaImplementation is built on Qt's
  QReplicaImplementationInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectReplicaImplementation that has a ritual
  and that Python can call so far, 17 names in all:
  'needsDynamicInitialization', 'getProperty', 'setProperty',
  'isShortCircuit', 'isInitialized', 'state', 'setState', 'waitForSource',
  'waitForFinished', 'notifyAboutReply', 'configurePrivate',
  'emitInitialized', 'emitNotified', 'node', '_q_send', '_q_sendWithReply',
  'setDynamicMetaObject'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QRemoteObjectReplicaImplementation::~QRemoteObjectReplicaImplementation(
    )': the destructor: Python never removes a C++
    QRemoteObjectReplicaImplementation.
  - Qt's 'void QRemoteObjectReplicaImplementation::setProperties(QVariantList
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectReplicaImplementation::setDynamicProperties(QVariantList
    &&values)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QRemoteObjectReplicaImplementation is created at the first use,
    not by 'QRemoteObjectReplicaImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectReplicaImplementation.
  - Qt tells when it has removed the C++ QRemoteObjectReplicaImplementation.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectReplicaImplementation that has no cute
    function yet, '__init__', 'setDynamicProperties', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectReplicaImplementation'

  #  Qt's QRemoteObjectReplicaImplementation is built on more than one class.
  #  The part of a C++ QRemoteObjectReplicaImplementation that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QReplicaImplementationInterface':
          'ritual_cast_QRemoteObjectReplicaImplementation_QReplicaImplementationInterface',
  }

  #  A C++ QRemoteObjectReplicaImplementation Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectReplicaImplementation'

  #  The functions Qt calls itself that QRemoteObjectReplicaImplementation is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setDynamicProperties': (
          'void '
          'QRemoteObjectReplicaImplementation::setDynamicProperties(QVarian'
          'tList &&)',
      ),
  }

  #  The functions Qt calls itself that QRemoteObjectReplicaImplementation is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isShortCircuit': (
          ('_ZNK34QRemoteObjectReplicaImplementation14isShortCircuitEv',
           ('bool', 'number', ''),
           ()),
      ),
      'waitForFinished': (
          ('_ZN34QRemoteObjectReplicaImplementation15waitForFinishedERK24QR'
           'emoteObjectPendingCalli',
           ('bool', 'number', ''),
           (
               ('address', 'value',
                'QtRemoteObjects:QRemoteObjectPendingCall'),
               ('int', 'number', ''),
           )),
      ),
      'notifyAboutReply': (
          ('_ZN34QRemoteObjectReplicaImplementation16notifyAboutReplyEiRK8Q'
           'Variant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'configurePrivate': (
          ('_ZN34QRemoteObjectReplicaImplementation16configurePrivateEP20QR'
           'emoteObjectReplica',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectReplica'),
           )),
      ),
      'setDynamicMetaObject': (
          ('_ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEP'
           'K11QMetaObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMetaObject'),
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

  def needsDynamicInitialization(self) -> bool:
    """
    Calls Qt's 'bool
    QRemoteObjectReplicaImplementation::needsDynamicInitialization() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html
    """
    #  bool QRemoteObjectReplicaImplementation::needsDynamicInitialization()
    #      const
    return self.uglySide.call(
        'ritual_ZNK34QRemoteObjectReplicaImplementation26needsDynamicInitia'
        'lizationEv',
    )

  @overload(int)
  def getProperty(self, i: int) -> QVariant:
    """
    Calls Qt's 'const QVariant
    QRemoteObjectReplicaImplementation::getProperty(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant QRemoteObjectReplicaImplementation::getProperty(int i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QRemoteObjectReplicaImplementation11getPropertyEi', i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isShortCircuit(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplicaImplementation::isShortCircuit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html
    """
    #  bool QRemoteObjectReplicaImplementation::isShortCircuit() const
    return self.uglySide.call(
        'ritual_ZNK34QRemoteObjectReplicaImplementation14isShortCircuitEv',
    )

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplicaImplementation::isInitialized()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html
    """
    #  bool QRemoteObjectReplicaImplementation::isInitialized() const
    ritual = (
        'ritual_ZNK34QRemoteObjectReplicaImplementation13isInitializedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QRemoteObjectReplicaImplementation13isInitialize'
          'dEv')
    return self.uglySide.call(ritual)

  def state(self) -> QRemoteObjectReplica.State:
    """
    Calls Qt's 'QRemoteObjectReplica::State
    QRemoteObjectReplicaImplementation::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html#state

    Returns
    -------

    QRemoteObjectReplica.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRemoteObjectReplica.State(number)' gives.
    """
    #  QRemoteObjectReplica::State
    #      QRemoteObjectReplicaImplementation::state() const
    ritual = 'ritual_ZNK34QRemoteObjectReplicaImplementation5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK34QRemoteObjectReplicaImplementation5stateEv'
    return QRemoteObjectReplica.State(self.uglySide.call(ritual))

  def node(self) -> Optional[QRemoteObjectNode]:
    """
    Calls Qt's 'QRemoteObjectNode *QRemoteObjectReplicaImplementation::node()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html#node

    Returns
    -------

    Optional[QRemoteObjectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNode *QRemoteObjectReplicaImplementation::node() const
    ritual = 'ritual_ZNK34QRemoteObjectReplicaImplementation4nodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK34QRemoteObjectReplicaImplementation4nodeEv'
    address = self.uglySide.call(ritual)
    from . import QRemoteObjectNode
    return QRemoteObjectNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, i: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplicaImplementation::setProperty(int i,
    const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    i : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QRemoteObjectReplicaImplementation::setProperty(int i, const
    #      QVariant &a1)
    self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation11setPropertyEiRK8QVa'
        'riant',
        i, self._valueOf(a1),
    )

  @overload(QRemoteObjectReplica.State)
  def setState(self, state: QRemoteObjectReplica.State) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectReplicaImplementation::setState(QRemoteObjectReplica::State
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html#setState

    Parameters
    ----------

    state : QRemoteObjectReplica.State
      Passed on as its number.
    """
    #  void QRemoteObjectReplicaImplementation::setState(
    #      QRemoteObjectReplica::State state)
    self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation8setStateEN20QRemoteO'
        'bjectReplica5StateE',
        state.value,
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def setDynamicMetaObject(self, meta: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectReplicaImplementation::setDynamicMetaObject(const
    QMetaObject *meta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const
    #      QMetaObject *meta)
    ritual = (
        'ritual_ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjec'
        'tEPK11QMetaObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QRemoteObjectReplicaImplementation20setDynamicMet'
          'aObjectEPK11QMetaObject')
    self.uglySide.call(ritual, self._addressOf(meta, 'QMetaObject'))

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
    Qt's
    'QRemoteObjectReplicaImplementation::QRemoteObjectReplicaImplementation(
    const QString &name, const QMetaObject *a1, QRemoteObjectNode *a2)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QRemoteObjectReplicaImplementation.__init__' has no cute function "
        "yet. Qt's "
        "'QRemoteObjectReplicaImplementation::QRemoteObjectReplicaImplementa"
        "tion(const QString &name, const QMetaObject *a1, QRemoteObjectNode "
        "*a2)': the class is abstract, so C++ cannot make one, and the C++ "
        "class of ours does not fill in every function it leaves open.")

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
  def waitForSource(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectReplicaImplementation::waitForSource(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QRemoteObjectReplicaImplementation::waitForSource(int a0)
    ritual = 'ritual_ZN34QRemoteObjectReplicaImplementation13waitForSourceEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QRemoteObjectReplicaImplementation13waitForSource'
          'Ei')
    return self.uglySide.call(ritual, a0)

  @overload(QRemoteObjectPendingCall, int)
  def waitForFinished(self, a0: QRemoteObjectPendingCall, a1: int) -> bool:
    """
    Calls Qt's 'bool
    QRemoteObjectReplicaImplementation::waitForFinished(const
    QRemoteObjectPendingCall &a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    a0 : QRemoteObjectPendingCall
      Passed on as a value: Qt reads the C++ QRemoteObjectPendingCall, which
      stays Python's own.

    a1 : int
      Passed on as it is.
    """
    #  bool QRemoteObjectReplicaImplementation::waitForFinished(const
    #      QRemoteObjectPendingCall &a0, int a1)
    ritual = (
        'ritual_ZN34QRemoteObjectReplicaImplementation15waitForFinishedERK2'
        '4QRemoteObjectPendingCalli')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QRemoteObjectReplicaImplementation15waitForFinish'
          'edERK24QRemoteObjectPendingCalli')
    return self.uglySide.call(
        ritual, self._valueOf(a0, 'QRemoteObjectPendingCall'), a1,
    )

  @overload(int, QVariant)
  def notifyAboutReply(self, a0: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplicaImplementation::notifyAboutReply(int
    a0, const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QRemoteObjectReplicaImplementation::notifyAboutReply(int a0,
    #      const QVariant &a1)
    ritual = (
        'ritual_ZN34QRemoteObjectReplicaImplementation16notifyAboutReplyEiR'
        'K8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QRemoteObjectReplicaImplementation16notifyAboutRe'
          'plyEiRK8QVariant')
    self.uglySide.call(ritual, a0, self._valueOf(a1))

  @overload(QRemoteObjectReplica)
  @overload(NoneType)
  def configurePrivate(self, a0: Optional[QRemoteObjectReplica]) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectReplicaImplementation::configurePrivate(QRemoteObjectReplica
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectReplicaImplementation::configurePrivate(
    #      QRemoteObjectReplica *a0)
    ritual = (
        'ritual_ZN34QRemoteObjectReplicaImplementation16configurePrivateEP2'
        '0QRemoteObjectReplica')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QRemoteObjectReplicaImplementation16configurePriv'
          'ateEP20QRemoteObjectReplica')
    self.uglySide.call(ritual, self._addressOf(a0))

  def emitInitialized(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplicaImplementation::emitInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html
    """
    #  void QRemoteObjectReplicaImplementation::emitInitialized()
    self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation15emitInitializedEv',
    )

  def emitNotified(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectReplicaImplementation::emitNotified()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html
    """
    #  void QRemoteObjectReplicaImplementation::emitNotified()
    self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation12emitNotifiedEv',
    )

  @overload(QMetaObject.Call, int, QList[QVariant])
  def _q_send(
      self,
      call: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectReplicaImplementation::_q_send(QMetaObject::Call call, int
    index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html#_q_send

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
    #  void QRemoteObjectReplicaImplementation::_q_send(QMetaObject::Call
    #      call, int index, const QVariantList &args)
    self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation7_q_sendEN11QMetaObje'
        'ct4CallEiRK5QListI8QVariantE',
        call.value, index, self._valueOf(args),
    )

  @overload(QMetaObject.Call, int, QList[QVariant])
  def _q_sendWithReply(
      self,
      call: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
  ) -> QRemoteObjectPendingCall:
    """
    Calls Qt's 'QRemoteObjectPendingCall
    QRemoteObjectReplicaImplementation::_q_sendWithReply(QMetaObject::Call
    call, int index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectreplicaimplementation.html

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
    #      QRemoteObjectReplicaImplementation::_q_sendWithReply(
    #      QMetaObject::Call call, int index, const QVariantList &args)
    address = self.uglySide.call(
        'ritual_ZN34QRemoteObjectReplicaImplementation16_q_sendWithReplyEN1'
        '1QMetaObject4CallEiRK5QListI8QVariantE',
        call.value, index, self._valueOf(args),
    )
    from . import QRemoteObjectPendingCall
    return QRemoteObjectPendingCall._cuteOwning(address)

  @staticmethod
  def setDynamicProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectReplicaImplementation::setDynamicProperties(QVariantList
    &&values)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectReplicaImplementation.setDynamicProperties' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectReplicaImplementation::setDynamicProperties(QVariantLi"
        "st &&values)': takes a type Python has no way to hand over yet.")
