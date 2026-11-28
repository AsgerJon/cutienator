"""
QOpcUaInternalDataTypeNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuainternaldatatypenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpcUaInternalDataTypeNode to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant


class QOpcUaInternalDataTypeNode(QObject):
  """
  The cute side of Qt's QOpcUaInternalDataTypeNode: a plain Python object
  standing in front of one C++ QOpcUaInternalDataTypeNode.

  It is built on the cute 'QObject', as Qt's QOpcUaInternalDataTypeNode is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaInternalDataTypeNode that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'definition',
  'isAbstract', 'name', 'nodeId', 'initializeFinished'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaInternalDataTypeNode::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QOpcUaInternalDataTypeNode::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const std::vector<std::unique_ptr<QOpcUaInternalDataTypeNode>>
    &QOpcUaInternalDataTypeNode::children() const': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 3 leans on 'QOpcUaInternalDataTypeNode;
  2 not a gap; 2 forbidden; 1 leans on 'vtable for
  QOpcUaInternalDataTypeNode', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QOpcUaInternalDataTypeNode is created at the first use, not by
    'QOpcUaInternalDataTypeNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaInternalDataTypeNode.
  - Qt tells when it has removed the C++ QOpcUaInternalDataTypeNode. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaInternalDataTypeNode that has no cute function
    yet, '__init__', 'handleFinished', 'initialize', holds a function that
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
  __qt_class__ = 'QOpcUaInternalDataTypeNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaInternalDataTypeNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaInternalDataTypeNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaInternalDataTypeNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def definition(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaInternalDataTypeNode::definition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#definition

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaInternalDataTypeNode::definition() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaInternalDataTypeNode10definitionEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isAbstract(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaInternalDataTypeNode::isAbstract() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#isAbstract
    """
    #  bool QOpcUaInternalDataTypeNode::isAbstract() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaInternalDataTypeNode10isAbstractEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QOpcUaInternalDataTypeNode::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaInternalDataTypeNode::name() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaInternalDataTypeNode4nameEv',
    )

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaInternalDataTypeNode::nodeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaInternalDataTypeNode::nodeId() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaInternalDataTypeNode6nodeIdEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QOpcUaInternalDataTypeNode::QOpcUaInternalDataTypeNode(QOpcUaClient
    *client)': leans on 'vtable for QOpcUaInternalDataTypeNode', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaInternalDataTypeNode.__init__' has no cute function yet. "
        "Qt's "
        "'QOpcUaInternalDataTypeNode::QOpcUaInternalDataTypeNode(QOpcUaClien"
        "t *client)': leans on 'vtable for QOpcUaInternalDataTypeNode', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(bool)
  def initializeFinished(self, success: bool) -> None:
    """
    Calls Qt's 'void QOpcUaInternalDataTypeNode::initializeFinished(bool
    success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuainternaldatatypenode.html#initializeFinished

    Parameters
    ----------

    success : bool
      Passed on as it is.
    """
    #  void QOpcUaInternalDataTypeNode::initializeFinished(bool success)
    self.uglySide.call(
        'ritual_ZN26QOpcUaInternalDataTypeNode18initializeFinishedEb',
        success,
    )

  @staticmethod
  def handleFinished(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaInternalDataTypeNode::handleFinished(bool success)':
    leans on 'QOpcUaInternalDataTypeNode::initializeFinished(bool)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaInternalDataTypeNode.handleFinished' has no cute function "
        "yet. Qt's 'void QOpcUaInternalDataTypeNode::handleFinished(bool "
        "success)': leans on "
        "'QOpcUaInternalDataTypeNode::initializeFinished(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaInternalDataTypeNode::initialize(const QString
    &nodeId)': leans on 'QOpcUaInternalDataTypeNode::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaInternalDataTypeNode.initialize' has no cute function yet. "
        "Qt's 'bool QOpcUaInternalDataTypeNode::initialize(const QString "
        "&nodeId)': leans on "
        "'QOpcUaInternalDataTypeNode::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
