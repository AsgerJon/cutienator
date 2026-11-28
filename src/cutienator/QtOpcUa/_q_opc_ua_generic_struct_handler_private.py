"""
QOpcUaGenericStructHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuagenericstructhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpcUaGenericStructHandlerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QOpcUa, QOpcUaGenericStructHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpcUaClient, QOpcUaEnumDefinition, QOpcUaGenericStructValue
  from . import QOpcUaInternalDataTypeNode, QOpcUaStructureDefinition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaClient = WAIT['QOpcUaClient']
  QOpcUaEnumDefinition = WAIT['QOpcUaEnumDefinition']
  QOpcUaInternalDataTypeNode = WAIT['QOpcUaInternalDataTypeNode']
  QOpcUaStructureDefinition = WAIT['QOpcUaStructureDefinition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaGenericStructHandlerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpcUaGenericStructHandlerPrivate: a plain Python
  object standing in front of one C++ QOpcUaGenericStructHandlerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QOpcUaGenericStructHandlerPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaGenericStructHandlerPrivate that has a ritual
  and that Python can call so far, 19 names in all: 'q_func',
  'createGenericStructValueForTypeId',
  'structureDefinitionForBinaryEncodingId', 'structureDefinitionForTypeId',
  'enumDefinitionForTypeId', 'typeNameForBinaryEncodingId',
  'typeNameForTypeId', 'dataTypeKindForTypeId', 'typeIdForBinaryEncodingId',
  'isAbstractTypeId', 'handleFinished', 'addCustomStructureDefinition',
  'addCustomEnumDefinition', 'initialized', 'handleInitializeFinished',
  'processDataTypeRecursive', 'processStructRecursive',
  'processEnumRecursive', 'processSubtypeOfKnownTypeRecursive'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpcUaGenericStructHandler
    *QOpcUaGenericStructHandlerPrivate::q_func() const': takes in Python what
    'QOpcUaGenericStructHandler *QOpcUaGenericStructHandlerPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  12 of the 33 functions Qt declares: 3 leans on 'QByteArray
  QOpcUaBinaryDataEncoding; 3 leans on 'bool QOpcUaBinaryDataEncoding; 2
  forbidden; 2 a template; 1 cannot be called and cannot be called through
  the meta-object and cannot be copied; 1 leans on
  'QOpcUaInternalDataTypeNode.

  What to expect
  --------------

  - The C++ QOpcUaGenericStructHandlerPrivate is created at the first use,
    not by 'QOpcUaGenericStructHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaGenericStructHandlerPrivate.
  - Each name of Qt's QOpcUaGenericStructHandlerPrivate that has no cute
    function yet, 'decode', 'decodeArrayOrScalar',
    'decodeKnownTypesInternal', 'decodeStructInternal', 'encode',
    'encodeArrayOrScalar', 'encodeKnownTypesInternal',
    'encodeStructInternal', 'initialize', 'initializeFinished', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaGenericStructHandlerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def structureDefinitionForBinaryEncodingId(
      self,
      id: str,
  ) -> QOpcUaStructureDefinition:
    """
    Calls Qt's 'QOpcUaStructureDefinition QOpcUaGenericStructHandlerPrivate::
    structureDefinitionForBinaryEncodingId(const QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QOpcUaStructureDefinition
      A new cute QOpcUaStructureDefinition around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaStructureDefinition QOpcUaGenericStructHandlerPrivate::
    #      structureDefinitionForBinaryEncodingId(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate38structureDefinition'
        'ForBinaryEncodingIdERK7QString',
        id,
    )
    from . import QOpcUaStructureDefinition
    return QOpcUaStructureDefinition._cuteOwning(address)

  @overload(str)
  def structureDefinitionForTypeId(
      self,
      id: str,
  ) -> QOpcUaStructureDefinition:
    """
    Calls Qt's 'QOpcUaStructureDefinition
    QOpcUaGenericStructHandlerPrivate::structureDefinitionForTypeId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QOpcUaStructureDefinition
      A new cute QOpcUaStructureDefinition around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaStructureDefinition
    #      QOpcUaGenericStructHandlerPrivate::structureDefinitionForTypeId(
    #      const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate28structureDefinition'
        'ForTypeIdERK7QString',
        id,
    )
    from . import QOpcUaStructureDefinition
    return QOpcUaStructureDefinition._cuteOwning(address)

  @overload(str)
  def enumDefinitionForTypeId(self, id: str) -> QOpcUaEnumDefinition:
    """
    Calls Qt's 'QOpcUaEnumDefinition
    QOpcUaGenericStructHandlerPrivate::enumDefinitionForTypeId(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QOpcUaEnumDefinition
      A new cute QOpcUaEnumDefinition around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaEnumDefinition
    #      QOpcUaGenericStructHandlerPrivate::enumDefinitionForTypeId(const
    #      QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate23enumDefinitionForTy'
        'peIdERK7QString',
        id,
    )
    from . import QOpcUaEnumDefinition
    return QOpcUaEnumDefinition._cuteOwning(address)

  @overload(str)
  def typeNameForBinaryEncodingId(self, id: str) -> str:
    """
    Calls Qt's 'QString
    QOpcUaGenericStructHandlerPrivate::typeNameForBinaryEncodingId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QOpcUaGenericStructHandlerPrivate::typeNameForBinaryEncodingId(
    #      const QString &id) const
    return self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate27typeNameForBinaryEn'
        'codingIdERK7QString',
        id,
    )

  @overload(str)
  def typeNameForTypeId(self, id: str) -> str:
    """
    Calls Qt's 'QString
    QOpcUaGenericStructHandlerPrivate::typeNameForTypeId(const QString &id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructHandlerPrivate::typeNameForTypeId(const
    #      QString &id) const
    return self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate17typeNameForTypeIdER'
        'K7QString',
        id,
    )

  @overload(str)
  def dataTypeKindForTypeId(
      self,
      id: str,
  ) -> QOpcUaGenericStructHandler.DataTypeKind:
    """
    Calls Qt's 'QOpcUaGenericStructHandler::DataTypeKind
    QOpcUaGenericStructHandlerPrivate::dataTypeKindForTypeId(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QOpcUaGenericStructHandler.DataTypeKind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaGenericStructHandler.DataTypeKind(number)' gives.
    """
    #  QOpcUaGenericStructHandler::DataTypeKind
    #      QOpcUaGenericStructHandlerPrivate::dataTypeKindForTypeId(const
    #      QString &id) const
    return QOpcUaGenericStructHandler.DataTypeKind(self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate21dataTypeKindForType'
        'IdERK7QString',
        id,
    ))

  @overload(str)
  def typeIdForBinaryEncodingId(self, id: str) -> str:
    """
    Calls Qt's 'QString
    QOpcUaGenericStructHandlerPrivate::typeIdForBinaryEncodingId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QOpcUaGenericStructHandlerPrivate::typeIdForBinaryEncodingId(const
    #      QString &id) const
    return self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate25typeIdForBinaryEnco'
        'dingIdERK7QString',
        id,
    )

  @overload(str)
  def isAbstractTypeId(self, id: str) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaGenericStructHandlerPrivate::isAbstractTypeId(const QString &id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpcUaGenericStructHandlerPrivate::isAbstractTypeId(const QString
    #      &id) const
    return self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate16isAbstractTypeIdERK'
        '7QString',
        id,
    )

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaGenericStructHandlerPrivate::initialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html#initialized
    """
    #  bool QOpcUaGenericStructHandlerPrivate::initialized() const
    return self.uglySide.call(
        'ritual_ZNK33QOpcUaGenericStructHandlerPrivate11initializedEv',
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

  @overload(QOpcUaClient)
  @overload(NoneType)
  def __init__(self, client: Optional[QOpcUaClient]) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaGenericStructHandlerPrivate::QOpcUaGenericStructHandlerPrivate(
    QOpcUaClient *client)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    client : Optional[QOpcUaClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaGenericStructHandlerPrivate::
    #      QOpcUaGenericStructHandlerPrivate(QOpcUaClient *client)
    self._noteCreation(
        QOpcUaGenericStructHandlerPrivate, lambda: Rituals.call(
            'ritual_ZN33QOpcUaGenericStructHandlerPrivateC1EP12QOpcUaClient',
            self._addressOf(client),
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

  def q_func(self) -> Optional[QOpcUaGenericStructHandler]:
    """
    Calls Qt's 'QOpcUaGenericStructHandler
    *QOpcUaGenericStructHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html#q_func

    Returns
    -------

    Optional[QOpcUaGenericStructHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaGenericStructHandler
    #      *QOpcUaGenericStructHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate6q_funcEv',
    )
    return QOpcUaGenericStructHandler._cuteAt(address)

  @overload(str)
  def createGenericStructValueForTypeId(
      self,
      typeId: str,
  ) -> QOpcUaGenericStructValue:
    """
    Calls Qt's 'QOpcUaGenericStructValue
    QOpcUaGenericStructHandlerPrivate::createGenericStructValueForTypeId(
    const QString &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QOpcUaGenericStructValue
      A new cute QOpcUaGenericStructValue around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaGenericStructValue QOpcUaGenericStructHandlerPrivate::
    #      createGenericStructValueForTypeId(const QString &typeId)
    address = self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate33createGenericStructV'
        'alueForTypeIdERK7QString',
        typeId,
    )
    from . import QOpcUaGenericStructValue
    return QOpcUaGenericStructValue._cuteOwning(address)

  @overload(bool)
  def handleFinished(self, success: bool) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructHandlerPrivate::handleFinished(bool
    success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    success : bool
      Passed on as it is.
    """
    #  void QOpcUaGenericStructHandlerPrivate::handleFinished(bool success)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate14handleFinishedEb',
        success,
    )

  @overload(QOpcUaStructureDefinition, str, str, QOpcUa.IsAbstract)
  def addCustomStructureDefinition(
      self,
      definition: QOpcUaStructureDefinition,
      typeId: str,
      name: str,
      isAbstract: QOpcUa.IsAbstract,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaGenericStructHandlerPrivate::addCustomStructureDefinition(const
    QOpcUaStructureDefinition &definition, const QString &typeId, const
    QString &name, QOpcUa::IsAbstract isAbstract)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    definition : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    isAbstract : QOpcUa.IsAbstract
      Passed on as its number.
    """
    #  bool QOpcUaGenericStructHandlerPrivate::addCustomStructureDefinition(
    #      const QOpcUaStructureDefinition &definition, const QString
    #      &typeId, const QString &name, QOpcUa::IsAbstract isAbstract)
    return self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate28addCustomStructureDe'
        'finitionERK25QOpcUaStructureDefinitionRK7QStringS5_N6QOpcUa10IsAbs'
        'tractE',
        self._valueOf(definition), typeId, name, isAbstract.value,
    )

  @overload(QOpcUaEnumDefinition, str, str, QOpcUa.IsAbstract)
  def addCustomEnumDefinition(
      self,
      definition: QOpcUaEnumDefinition,
      typeId: str,
      name: str,
      isAbstract: QOpcUa.IsAbstract,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaGenericStructHandlerPrivate::addCustomEnumDefinition(const
    QOpcUaEnumDefinition &definition, const QString &typeId, const QString
    &name, QOpcUa::IsAbstract isAbstract)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    definition : QOpcUaEnumDefinition
      Passed on as a value: Qt reads the C++ QOpcUaEnumDefinition, which
      stays Python's own.

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    isAbstract : QOpcUa.IsAbstract
      Passed on as its number.
    """
    #  bool QOpcUaGenericStructHandlerPrivate::addCustomEnumDefinition(const
    #      QOpcUaEnumDefinition &definition, const QString &typeId, const
    #      QString &name, QOpcUa::IsAbstract isAbstract)
    return self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate23addCustomEnumDefinit'
        'ionERK20QOpcUaEnumDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE',
        self._valueOf(definition), typeId, name, isAbstract.value,
    )

  @overload(bool)
  def handleInitializeFinished(self, success: bool) -> None:
    """
    Calls Qt's 'void
    QOpcUaGenericStructHandlerPrivate::handleInitializeFinished(bool
    success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    success : bool
      Passed on as it is.
    """
    #  void QOpcUaGenericStructHandlerPrivate::handleInitializeFinished(bool
    #      success)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate24handleInitializeFini'
        'shedEb',
        success,
    )

  @overload(QOpcUaInternalDataTypeNode)
  @overload(NoneType)
  def processDataTypeRecursive(
      self,
      node: Optional[QOpcUaInternalDataTypeNode],
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaGenericStructHandlerPrivate::processDataTypeRecursive(
    QOpcUaInternalDataTypeNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    node : Optional[QOpcUaInternalDataTypeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaGenericStructHandlerPrivate::processDataTypeRecursive(
    #      QOpcUaInternalDataTypeNode *node)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate24processDataTypeRecur'
        'siveEP26QOpcUaInternalDataTypeNode',
        self._addressOf(node),
    )

  @overload(QOpcUaInternalDataTypeNode)
  @overload(NoneType)
  def processStructRecursive(
      self,
      node: Optional[QOpcUaInternalDataTypeNode],
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaGenericStructHandlerPrivate::processStructRecursive(
    QOpcUaInternalDataTypeNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    node : Optional[QOpcUaInternalDataTypeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaGenericStructHandlerPrivate::processStructRecursive(
    #      QOpcUaInternalDataTypeNode *node)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate22processStructRecursi'
        'veEP26QOpcUaInternalDataTypeNode',
        self._addressOf(node),
    )

  @overload(QOpcUaInternalDataTypeNode)
  @overload(NoneType)
  def processEnumRecursive(
      self,
      node: Optional[QOpcUaInternalDataTypeNode],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructHandlerPrivate::processEnumRecursive(
    QOpcUaInternalDataTypeNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    node : Optional[QOpcUaInternalDataTypeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaGenericStructHandlerPrivate::processEnumRecursive(
    #      QOpcUaInternalDataTypeNode *node)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate20processEnumRecursive'
        'EP26QOpcUaInternalDataTypeNode',
        self._addressOf(node),
    )

  @overload(QOpcUaInternalDataTypeNode, str)
  @overload(NoneType, str)
  def processSubtypeOfKnownTypeRecursive(
      self,
      node: Optional[QOpcUaInternalDataTypeNode],
      id: str,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaGenericStructHandlerPrivate::processSubtypeOfKnownTypeRecursive(
    QOpcUaInternalDataTypeNode *node, const QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandlerprivate.html

    Parameters
    ----------

    node : Optional[QOpcUaInternalDataTypeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaGenericStructHandlerPrivate::
    #      processSubtypeOfKnownTypeRecursive(QOpcUaInternalDataTypeNode
    #      *node, const QString &id)
    self.uglySide.call(
        'ritual_ZN33QOpcUaGenericStructHandlerPrivate34processSubtypeOfKnow'
        'nTypeRecursiveEP26QOpcUaInternalDataTypeNodeRK7QString',
        self._addressOf(node), id,
    )

  @staticmethod
  def decode(*__, **_) -> Never:
    """
    Qt's 'QOpcUaGenericStructValue
    QOpcUaGenericStructHandlerPrivate::decode(const QOpcUaExtensionObject
    &extensionObject, bool &success) const': leans on 'QByteArray
    QOpcUaBinaryDataEncoding::decode<QByteArray,
    (QOpcUa::Types)4294967295>(bool&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.decode' has no cute function "
        "yet. Qt's 'QOpcUaGenericStructValue "
        "QOpcUaGenericStructHandlerPrivate::decode(const "
        "QOpcUaExtensionObject &extensionObject, bool &success) const': "
        "leans on 'QByteArray QOpcUaBinaryDataEncoding::decode<QByteArray, "
        "(QOpcUa::Types)4294967295>(bool&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def decodeArrayOrScalar(*__, **_) -> Never:
    """
    Qt's 'QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.decodeArrayOrScalar' has no "
        "cute function yet. Qt's "
        "'QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar': a "
        "template: a pattern and no single function.")

  @staticmethod
  def decodeKnownTypesInternal(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QOpcUaGenericStructHandlerPrivate::decodeKnownTypesInternal(
    QOpcUaBinaryDataEncoding &decoder, const QString &dataTypeId, qint32
    valueRank, bool &success, int currentDepth) const': leans on 'QByteArray
    QOpcUaBinaryDataEncoding::decode<QByteArray,
    (QOpcUa::Types)4294967295>(bool&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.decodeKnownTypesInternal' has "
        "no cute function yet. Qt's 'QVariant "
        "QOpcUaGenericStructHandlerPrivate::decodeKnownTypesInternal(QOpcUaB"
        "inaryDataEncoding &decoder, const QString &dataTypeId, qint32 "
        "valueRank, bool &success, int currentDepth) const': leans on "
        "'QByteArray QOpcUaBinaryDataEncoding::decode<QByteArray, "
        "(QOpcUa::Types)4294967295>(bool&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def decodeStructInternal(*__, **_) -> Never:
    """
    Qt's 'QOpcUaGenericStructValue
    QOpcUaGenericStructHandlerPrivate::decodeStructInternal(
    QOpcUaBinaryDataEncoding &decoder, const QString &dataTypeId, bool
    &success, int currentDepth) const': leans on 'QByteArray
    QOpcUaBinaryDataEncoding::decode<QByteArray,
    (QOpcUa::Types)4294967295>(bool&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.decodeStructInternal' has no "
        "cute function yet. Qt's 'QOpcUaGenericStructValue "
        "QOpcUaGenericStructHandlerPrivate::decodeStructInternal(QOpcUaBinar"
        "yDataEncoding &decoder, const QString &dataTypeId, bool &success, "
        "int currentDepth) const': leans on 'QByteArray "
        "QOpcUaBinaryDataEncoding::decode<QByteArray, "
        "(QOpcUa::Types)4294967295>(bool&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def encode(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaGenericStructHandlerPrivate::encode(const
    QOpcUaGenericStructValue &value, QOpcUaExtensionObject &output)': leans
    on 'bool QOpcUaBinaryDataEncoding::encode<QByteArray,
    (QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.encode' has no cute function "
        "yet. Qt's 'bool QOpcUaGenericStructHandlerPrivate::encode(const "
        "QOpcUaGenericStructValue &value, QOpcUaExtensionObject &output)': "
        "leans on 'bool QOpcUaBinaryDataEncoding::encode<QByteArray, "
        "(QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def encodeArrayOrScalar(*__, **_) -> Never:
    """
    Qt's 'QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.encodeArrayOrScalar' has no "
        "cute function yet. Qt's "
        "'QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar': a "
        "template: a pattern and no single function.")

  @staticmethod
  def encodeKnownTypesInternal(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaGenericStructHandlerPrivate::encodeKnownTypesInternal(
    QOpcUaBinaryDataEncoding &encoder, const QVariant &value, qint32
    valueRank, const QString &dataTypeId)': leans on 'bool
    QOpcUaBinaryDataEncoding::encode<QByteArray,
    (QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.encodeKnownTypesInternal' has "
        "no cute function yet. Qt's 'bool "
        "QOpcUaGenericStructHandlerPrivate::encodeKnownTypesInternal(QOpcUaB"
        "inaryDataEncoding &encoder, const QVariant &value, qint32 "
        "valueRank, const QString &dataTypeId)': leans on 'bool "
        "QOpcUaBinaryDataEncoding::encode<QByteArray, "
        "(QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def encodeStructInternal(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaGenericStructHandlerPrivate::encodeStructInternal(
    QOpcUaBinaryDataEncoding &encoder, const QOpcUaGenericStructValue
    &value)': leans on 'bool QOpcUaBinaryDataEncoding::encode<QByteArray,
    (QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.encodeStructInternal' has no "
        "cute function yet. Qt's 'bool "
        "QOpcUaGenericStructHandlerPrivate::encodeStructInternal(QOpcUaBinar"
        "yDataEncoding &encoder, const QOpcUaGenericStructValue &value)': "
        "leans on 'bool QOpcUaBinaryDataEncoding::encode<QByteArray, "
        "(QOpcUa::Types)4294967295>(QByteArray const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaGenericStructHandlerPrivate::initialize()': leans on
    'QOpcUaInternalDataTypeNode::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.initialize' has no cute "
        "function yet. Qt's 'bool "
        "QOpcUaGenericStructHandlerPrivate::initialize()': leans on "
        "'QOpcUaInternalDataTypeNode::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def initializeFinished(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaGenericStructHandlerPrivate::initializeFinished(bool
    success)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandlerPrivate.initializeFinished' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaGenericStructHandlerPrivate::initializeFinished(bool "
        "success)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
