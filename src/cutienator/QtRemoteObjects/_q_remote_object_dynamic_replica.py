"""
QRemoteObjectDynamicReplica binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectdynamicreplica.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRemoteObjectReplica

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QRemoteObjectNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectNode = WAIT['QRemoteObjectNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectDynamicReplica(QRemoteObjectReplica):
  """
  The cute side of Qt's QRemoteObjectDynamicReplica: a plain Python object
  standing in front of one C++ QRemoteObjectDynamicReplica.

  It is built on the cute 'QRemoteObjectReplica', as Qt's
  QRemoteObjectDynamicReplica is built on Qt's QRemoteObjectReplica, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectDynamicReplica that has a ritual and
  that Python can call so far, 1 name in all: 'metaObject'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectDynamicReplica::~QRemoteObjectDynamicReplica()': the
    destructor: Python never removes a C++ QRemoteObjectDynamicReplica.
  - Qt's 'void *QRemoteObjectDynamicReplica::qt_metacast(const char *name)':
    one of Qt's own inner workings.
  - Qt's 'int QRemoteObjectDynamicReplica::qt_metacall(QMetaObject::Call
    call, int id, void **argv)': one of Qt's own inner workings.

  What to expect
  --------------

  - The C++ QRemoteObjectDynamicReplica is created at the first use, not by
    'QRemoteObjectDynamicReplica(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectDynamicReplica.
  - Qt tells when it has removed the C++ QRemoteObjectDynamicReplica. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectDynamicReplica'

  #  A C++ QRemoteObjectDynamicReplica Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectDynamicReplica'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectDynamicReplica::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectdynamicreplica.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectDynamicReplica::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QRemoteObjectDynamicReplica10metaObjectEv',
    )
    from ..QtCore import QMetaObject
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectdynamicreplica.html
    """
    #  QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica()
    self._noteCreation(QRemoteObjectDynamicReplica, lambda: Rituals.call(
        'ritual_ZN27QRemoteObjectDynamicReplicaC1Ev',
    ))

  @overload(QRemoteObjectNode, str)
  @overload(NoneType, str)
  def __init__(self, node: Optional[QRemoteObjectNode], name: str) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica(
    QRemoteObjectNode *node, const QString &name)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectdynamicreplica.html

    Parameters
    ----------

    node : Optional[QRemoteObjectNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica(
    #      QRemoteObjectNode *node, const QString &name)
    self._noteCreation(QRemoteObjectDynamicReplica, lambda: Rituals.call(
        'ritual_ZN27QRemoteObjectDynamicReplicaC1EP17QRemoteObjectNodeRK7QS'
        'tring',
        self._addressOf(node), name,
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
