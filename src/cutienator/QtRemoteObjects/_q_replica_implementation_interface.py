"""
QReplicaImplementationInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QReplicaImplementationInterface to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList, QMetaObject
from . import QRemoteObjectReplica

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectNode, QRemoteObjectPendingCall
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QReplicaImplementationInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QReplicaImplementationInterface: a plain Python
  object standing in front of one C++ QReplicaImplementationInterface.

  What exists
  -----------

  Every function of Qt's QReplicaImplementationInterface that has a ritual
  and that Python can call so far, 8 names in all: 'getProperty',
  'setProperty', 'isInitialized', 'state', 'waitForSource', 'node',
  '_q_send', '_q_sendWithReply'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QReplicaImplementationInterface::~QReplicaImplementationInterface()':
    the destructor: Python never removes a C++
    QReplicaImplementationInterface.
  - Qt's 'void QReplicaImplementationInterface::setProperties(QVariantList
    &&a0)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QReplicaImplementationInterface is created at the first use, not
    by 'QReplicaImplementationInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QReplicaImplementationInterface.
  - Each name of Qt's QReplicaImplementationInterface that has no cute
    function yet, 'setProperties', holds a function that raises
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
  __qt_class__ = 'QReplicaImplementationInterface'

  #  A C++ QReplicaImplementationInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QReplicaImplementationInterface'

  #  The functions Qt calls itself that QReplicaImplementationInterface is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setProperties': (
          'void '
          'QReplicaImplementationInterface::setProperties(QVariantList &&)',
      ),
      '_q_send': (
          'void '
          'QReplicaImplementationInterface::_q_send(QMetaObject::Call, '
          'int, const QVariantList &)',
      ),
      '_q_sendWithReply': (
          'QRemoteObjectPendingCall '
          'QReplicaImplementationInterface::_q_sendWithReply(QMetaObject::C'
          'all, int, const QVariantList &)',
      ),
  }

  #  The functions Qt calls itself that QReplicaImplementationInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'getProperty': (
          ('_ZNK31QReplicaImplementationInterface11getPropertyEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'setProperty': (
          ('_ZN31QReplicaImplementationInterface11setPropertyEiRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'isInitialized': (
          ('_ZNK31QReplicaImplementationInterface13isInitializedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'state': (
          ('_ZNK31QReplicaImplementationInterface5stateEv',
           ('int', 'enum', 'QtRemoteObjects:QRemoteObjectReplica.State'),
           ()),
      ),
      'waitForSource': (
          ('_ZN31QReplicaImplementationInterface13waitForSourceEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'node': (
          ('_ZNK31QReplicaImplementationInterface4nodeEv',
           ('address', 'address', 'QtRemoteObjects:QRemoteObjectNode'),
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

  @overload(int)
  def getProperty(self, i: int) -> QVariant:
    """
    Calls Qt's 'const QVariant
    QReplicaImplementationInterface::getProperty(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#getProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant QReplicaImplementationInterface::getProperty(int i)
    #      const
    address = self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZNK31QReplicaImplementationInterface11getPropertyEi',
        i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QReplicaImplementationInterface::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#isInitialized
    """
    #  bool QReplicaImplementationInterface::isInitialized() const
    return self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZNK31QReplicaImplementationInterface13isInitializedEv',
    )

  def state(self) -> QRemoteObjectReplica.State:
    """
    Calls Qt's 'QRemoteObjectReplica::State
    QReplicaImplementationInterface::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#state

    Returns
    -------

    QRemoteObjectReplica.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRemoteObjectReplica.State(number)' gives.
    """
    #  QRemoteObjectReplica::State QReplicaImplementationInterface::state()
    #      const
    return QRemoteObjectReplica.State(self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZNK31QReplicaImplementationInterface5stateEv',
    ))

  def node(self) -> Optional[QRemoteObjectNode]:
    """
    Calls Qt's 'QRemoteObjectNode *QReplicaImplementationInterface::node()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#node

    Returns
    -------

    Optional[QRemoteObjectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNode *QReplicaImplementationInterface::node() const
    address = self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZNK31QReplicaImplementationInterface4nodeEv',
    )
    from . import QRemoteObjectNode
    return QRemoteObjectNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, i: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QReplicaImplementationInterface::setProperty(int i,
    const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#setProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QReplicaImplementationInterface::setProperty(int i, const
    #      QVariant &a1)
    self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZN31QReplicaImplementationInterface11setPropertyEiRK8QVaria'
        'nt',
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
    Calls Qt's 'bool QReplicaImplementationInterface::waitForSource(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#waitForSource

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QReplicaImplementationInterface::waitForSource(int a0)
    return self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZN31QReplicaImplementationInterface13waitForSourceEi',
        a0,
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
    QReplicaImplementationInterface::_q_send(QMetaObject::Call call, int
    index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html#_q_send

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
    #  void QReplicaImplementationInterface::_q_send(QMetaObject::Call call,
    #      int index, const QVariantList &args)
    self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZN31QReplicaImplementationInterface7_q_sendEN11QMetaObject4'
        'CallEiRK5QListI8QVariantE',
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
    QReplicaImplementationInterface::_q_sendWithReply(QMetaObject::Call call,
    int index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreplicaimplementationinterface.html

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
    #      QReplicaImplementationInterface::_q_sendWithReply(QMetaObject::
    #      Call call, int index, const QVariantList &args)
    address = self._callAs(
        'QReplicaImplementationInterface',
        'ritual_ZN31QReplicaImplementationInterface16_q_sendWithReplyEN11QM'
        'etaObject4CallEiRK5QListI8QVariantE',
        call.value, index, self._valueOf(args),
    )
    from . import QRemoteObjectPendingCall
    return QRemoteObjectPendingCall._cuteOwning(address)

  @staticmethod
  def setProperties(*__, **_) -> Never:
    """
    Qt's 'void QReplicaImplementationInterface::setProperties(QVariantList
    &&a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QReplicaImplementationInterface.setProperties' has no cute "
        "function yet. Qt's 'void "
        "QReplicaImplementationInterface::setProperties(QVariantList "
        "&&a0)': takes a type Python has no way to hand over yet.")
