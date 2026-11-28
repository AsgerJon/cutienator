"""
QRemoteObjectHostBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectHostBasePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QRemoteObjectNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QRemoteObjectHostBase, QRemoteObjectReplica
  from . import QReplicaImplementationInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QRemoteObjectReplica = WAIT['QRemoteObjectReplica']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectHostBasePrivate(QRemoteObjectNodePrivate):
  """
  The cute side of Qt's QRemoteObjectHostBasePrivate: a plain Python object
  standing in front of one C++ QRemoteObjectHostBasePrivate.

  It is built on the cute 'QRemoteObjectNodePrivate', as Qt's
  QRemoteObjectHostBasePrivate is built on Qt's QRemoteObjectNodePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectHostBasePrivate that has a ritual and
  that Python can call so far, 2 names in all: 'handleNewAcquire', 'q_func'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectHostBasePrivate::~QRemoteObjectHostBasePrivate()': the
    destructor: Python never removes a C++ QRemoteObjectHostBasePrivate.
  - Qt's 'const QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func()
    const': takes in Python what 'QRemoteObjectHostBase
    *QRemoteObjectHostBasePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QRemoteObjectSourceBase.

  What to expect
  --------------

  - The C++ QRemoteObjectHostBasePrivate is created at the first use, not by
    'QRemoteObjectHostBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectHostBasePrivate.
  - Each name of Qt's QRemoteObjectHostBasePrivate that has no cute function
    yet, '__init__', 'setHostUrlBaseImpl', holds a function that raises
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
  __qt_class__ = 'QRemoteObjectHostBasePrivate'

  #  A C++ QRemoteObjectHostBasePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectHostBasePrivate'

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
    Qt's 'QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate()':
    leans on 'QRemoteObjectSourceBase::qobjectPropertyOffset', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostBasePrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate()': "
        "leans on 'QRemoteObjectSourceBase::qobjectPropertyOffset', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(QMetaObject, QRemoteObjectReplica, str)
  @overload(QMetaObject, NoneType, str)
  @overload(NoneType, QRemoteObjectReplica, str)
  @overload(NoneType, NoneType, str)
  def handleNewAcquire(
      self,
      meta: Optional[QMetaObject],
      instance: Optional[QRemoteObjectReplica],
      name: str,
  ) -> Optional[QReplicaImplementationInterface]:
    """
    Calls Qt's 'QReplicaImplementationInterface
    *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject *meta,
    QRemoteObjectReplica *instance, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbaseprivate.html#handleNewAcquire

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QReplicaImplementationInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QReplicaImplementationInterface
    #      *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject
    #      *meta, QRemoteObjectReplica *instance, const QString &name)
    address = self.uglySide.call(
        'ritual_ZN28QRemoteObjectHostBasePrivate16handleNewAcquireEPK11QMet'
        'aObjectP20QRemoteObjectReplicaRK7QString',
        self._addressOf(meta, 'QMetaObject'), self._addressOf(instance),
        name,
    )
    from . import QReplicaImplementationInterface
    return QReplicaImplementationInterface._cuteAt(address)

  def q_func(self) -> Optional[QRemoteObjectHostBase]:
    """
    Calls Qt's 'QRemoteObjectHostBase
    *QRemoteObjectHostBasePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbaseprivate.html#q_func

    Returns
    -------

    Optional[QRemoteObjectHostBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QRemoteObjectHostBasePrivate6q_funcEv',
    )
    from . import QRemoteObjectHostBase
    return QRemoteObjectHostBase._cuteAt(address)

  @staticmethod
  def setHostUrlBaseImpl(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectHostBasePrivate::setHostUrlBaseImpl(const QUrl
    &hostAddress, QRemoteObjectHostBase::AllowedSchemas allowedSchemas)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    's_managedTypesMutex'.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostBasePrivate.setHostUrlBaseImpl' has no cute "
        "function yet. Qt's 'bool "
        "QRemoteObjectHostBasePrivate::setHostUrlBaseImpl(const QUrl "
        "&hostAddress, QRemoteObjectHostBase::AllowedSchemas "
        "allowedSchemas)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 's_managedTypesMutex'.")
