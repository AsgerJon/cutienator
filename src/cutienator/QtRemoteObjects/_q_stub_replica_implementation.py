"""
QStubReplicaImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QStubReplicaImplementation to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QMetaObject
from . import QRemoteObjectReplica, QReplicaImplementationInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectNode, QRemoteObjectPendingCall
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QStubReplicaImplementation(QReplicaImplementationInterface):
  """
  The cute side of Qt's QStubReplicaImplementation: a plain Python object
  standing in front of one C++ QStubReplicaImplementation.

  It is built on the cute 'QReplicaImplementationInterface', as Qt's
  QStubReplicaImplementation is built on Qt's
  QReplicaImplementationInterface, and has everything that class has.

  C++ hands a QStubReplicaImplementation around as a copy, so every C++
  QStubReplicaImplementation behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QStubReplicaImplementation that has a ritual and
  that Python can call so far, 8 names in all: 'getProperty', 'setProperty',
  'isInitialized', 'state', 'waitForSource', 'node', '_q_send',
  '_q_sendWithReply'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStubReplicaImplementation::~QStubReplicaImplementation()': the
    destructor: Python removes its C++ QStubReplicaImplementation by it, and
    has no other use for it.
  - Qt's 'void QStubReplicaImplementation::setProperties(QVariantList &&a0)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QStubReplicaImplementation is created at the first use, not by
    'QStubReplicaImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStubReplicaImplementation back gives a copy the
    ritual made for Python, in a new cute QStubReplicaImplementation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStubReplicaImplementation'

  #  Qt's '~QStubReplicaImplementation()'. Naming it makes this a value
  #  class: Python owns every C++ QStubReplicaImplementation behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QStubReplicaImplementationD1Ev'

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
    Calls Qt's 'const QVariant QStubReplicaImplementation::getProperty(int i)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#getProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant QStubReplicaImplementation::getProperty(int i) const
    address = self.uglySide.call(
        'ritual_ZNK26QStubReplicaImplementation11getPropertyEi', i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QStubReplicaImplementation::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#isInitialized
    """
    #  bool QStubReplicaImplementation::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK26QStubReplicaImplementation13isInitializedEv',
    )

  def state(self) -> QRemoteObjectReplica.State:
    """
    Calls Qt's 'QRemoteObjectReplica::State
    QStubReplicaImplementation::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#state

    Returns
    -------

    QRemoteObjectReplica.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRemoteObjectReplica.State(number)' gives.
    """
    #  QRemoteObjectReplica::State QStubReplicaImplementation::state() const
    return QRemoteObjectReplica.State(self.uglySide.call(
        'ritual_ZNK26QStubReplicaImplementation5stateEv',
    ))

  def node(self) -> Optional[QRemoteObjectNode]:
    """
    Calls Qt's 'QRemoteObjectNode *QStubReplicaImplementation::node() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#node

    Returns
    -------

    Optional[QRemoteObjectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNode *QStubReplicaImplementation::node() const
    address = self.uglySide.call(
        'ritual_ZNK26QStubReplicaImplementation4nodeEv',
    )
    from . import QRemoteObjectNode
    return QRemoteObjectNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, i: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QStubReplicaImplementation::setProperty(int i, const
    QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#setProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QStubReplicaImplementation::setProperty(int i, const QVariant
    #      &a1)
    self.uglySide.call(
        'ritual_ZN26QStubReplicaImplementation11setPropertyEiRK8QVariant',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QStubReplicaImplementation::QStubReplicaImplementation()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html
    """
    #  QStubReplicaImplementation::QStubReplicaImplementation()
    self._noteCreation(QStubReplicaImplementation, lambda: Rituals.call(
        'ritual_ZN26QStubReplicaImplementationC1Ev',
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
  def waitForSource(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QStubReplicaImplementation::waitForSource(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#waitForSource

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QStubReplicaImplementation::waitForSource(int a0)
    return self.uglySide.call(
        'ritual_ZN26QStubReplicaImplementation13waitForSourceEi', a0,
    )

  @overload(QMetaObject.Call, int, QList[QVariant])
  def _q_send(
      self,
      call: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QStubReplicaImplementation::_q_send(QMetaObject::Call
    call, int index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#_q_send

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
    #  void QStubReplicaImplementation::_q_send(QMetaObject::Call call, int
    #      index, const QVariantList &args)
    self.uglySide.call(
        'ritual_ZN26QStubReplicaImplementation7_q_sendEN11QMetaObject4CallE'
        'iRK5QListI8QVariantE',
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
    QStubReplicaImplementation::_q_sendWithReply(QMetaObject::Call call, int
    index, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstubreplicaimplementation.html#_q_sendWithReply

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
    #      QStubReplicaImplementation::_q_sendWithReply(QMetaObject::Call
    #      call, int index, const QVariantList &args)
    address = self.uglySide.call(
        'ritual_ZN26QStubReplicaImplementation16_q_sendWithReplyEN11QMetaOb'
        'ject4CallEiRK5QListI8QVariantE',
        call.value, index, self._valueOf(args),
    )
    from . import QRemoteObjectPendingCall
    return QRemoteObjectPendingCall._cuteOwning(address)
