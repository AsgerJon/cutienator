"""
QOpcUaGenericStructHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuagenericstructhandler.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QOpcUaClient, QOpcUaEnumDefinition
  from . import QOpcUaGenericStructHandlerPrivate, QOpcUaGenericStructValue
  from . import QOpcUaStructureDefinition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaClient = WAIT['QOpcUaClient']
  QOpcUaEnumDefinition = WAIT['QOpcUaEnumDefinition']
  QOpcUaStructureDefinition = WAIT['QOpcUaStructureDefinition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaGenericStructHandler(QObject):
  """
  The cute side of Qt's QOpcUaGenericStructHandler: a plain Python object
  standing in front of one C++ QOpcUaGenericStructHandler.

  It is built on the cute 'QObject', as Qt's QOpcUaGenericStructHandler is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaGenericStructHandler that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject', 'tr', 'd_func',
  'initialize', 'createGenericStructValueForTypeId',
  'structureDefinitionForBinaryEncodingId', 'structureDefinitionForTypeId',
  'enumDefinitionForTypeId', 'typeNameForBinaryEncodingId',
  'typeNameForTypeId', 'isAbstractTypeId', 'addCustomStructureDefinition',
  'addCustomEnumDefinition', 'initialized', 'dataTypeKindForTypeId',
  'typeIdForBinaryEncodingId', 'initializedChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaGenericStructHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QOpcUaGenericStructHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QOpcUaGenericStructHandlerPrivate
    *QOpcUaGenericStructHandler::d_func() const': takes in Python what
    'QOpcUaGenericStructHandlerPrivate *QOpcUaGenericStructHandler::d_func()'
    takes.
  - Qt's 'QOpcUaGenericStructHandler::~QOpcUaGenericStructHandler()': the
    destructor: Python never removes a C++ QOpcUaGenericStructHandler.
  - Qt's 'std::optional<QOpcUaGenericStructValue>
    QOpcUaGenericStructHandler::decode(const QOpcUaExtensionObject
    &extensionObject) const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QOpcUaExtensionObject>
    QOpcUaGenericStructHandler::encode(const QOpcUaGenericStructValue
    &value)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpcUaGenericStructHandler is created at the first use, not by
    'QOpcUaGenericStructHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaGenericStructHandler.
  - Qt tells when it has removed the C++ QOpcUaGenericStructHandler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaGenericStructHandler that has no cute function
    yet, 'decode', 'encode', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaGenericStructHandler, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DataTypeKind(CuteNum, scoped=True):
    """
    The enum 'QOpcUaGenericStructHandler::DataTypeKind' of Qt, with the 4
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Struct = Kee[int](1)
    Enum = Kee[int](2)
    Other = Kee[int](3)

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
    Calls Qt's 'QString QOpcUaGenericStructHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#tr

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
    #  QString QOpcUaGenericStructHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QOpcUaGenericStructHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaGenericStructHandler'

  #  A C++ QOpcUaGenericStructHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaGenericStructHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaGenericStructHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaGenericStructHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def structureDefinitionForBinaryEncodingId(
      self,
      id: str,
  ) -> QOpcUaStructureDefinition:
    """
    Calls Qt's 'QOpcUaStructureDefinition
    QOpcUaGenericStructHandler::structureDefinitionForBinaryEncodingId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
    #  QOpcUaStructureDefinition QOpcUaGenericStructHandler::
    #      structureDefinitionForBinaryEncodingId(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler38structureDefinitionForBina'
        'ryEncodingIdERK7QString',
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
    QOpcUaGenericStructHandler::structureDefinitionForTypeId(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
    #      QOpcUaGenericStructHandler::structureDefinitionForTypeId(const
    #      QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler28structureDefinitionForType'
        'IdERK7QString',
        id,
    )
    from . import QOpcUaStructureDefinition
    return QOpcUaStructureDefinition._cuteOwning(address)

  @overload(str)
  def enumDefinitionForTypeId(self, id: str) -> QOpcUaEnumDefinition:
    """
    Calls Qt's 'QOpcUaEnumDefinition
    QOpcUaGenericStructHandler::enumDefinitionForTypeId(const QString &id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
    #      QOpcUaGenericStructHandler::enumDefinitionForTypeId(const QString
    #      &id) const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler23enumDefinitionForTypeIdERK'
        '7QString',
        id,
    )
    from . import QOpcUaEnumDefinition
    return QOpcUaEnumDefinition._cuteOwning(address)

  @overload(str)
  def typeNameForBinaryEncodingId(self, id: str) -> str:
    """
    Calls Qt's 'QString
    QOpcUaGenericStructHandler::typeNameForBinaryEncodingId(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructHandler::typeNameForBinaryEncodingId(const
    #      QString &id) const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler27typeNameForBinaryEncodingI'
        'dERK7QString',
        id,
    )

  @overload(str)
  def typeNameForTypeId(self, id: str) -> str:
    """
    Calls Qt's 'QString QOpcUaGenericStructHandler::typeNameForTypeId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#typeNameForTypeId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructHandler::typeNameForTypeId(const QString
    #      &id) const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler17typeNameForTypeIdERK7QStri'
        'ng',
        id,
    )

  @overload(str)
  def isAbstractTypeId(self, id: str) -> bool:
    """
    Calls Qt's 'bool QOpcUaGenericStructHandler::isAbstractTypeId(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#isAbstractTypeId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpcUaGenericStructHandler::isAbstractTypeId(const QString &id)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler16isAbstractTypeIdERK7QStrin'
        'g',
        id,
    )

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaGenericStructHandler::initialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#initialized
    """
    #  bool QOpcUaGenericStructHandler::initialized() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler11initializedEv',
    )

  @overload(str)
  def dataTypeKindForTypeId(self, id: str) -> DataTypeKind:
    """
    Calls Qt's 'DataTypeKind
    QOpcUaGenericStructHandler::dataTypeKindForTypeId(const QString &id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    DataTypeKind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DataTypeKind(number)'
      gives.
    """
    #  DataTypeKind QOpcUaGenericStructHandler::dataTypeKindForTypeId(const
    #      QString &id) const
    return QOpcUaGenericStructHandler.DataTypeKind(self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler21dataTypeKindForTypeIdERK7Q'
        'String',
        id,
    ))

  @overload(str)
  def typeIdForBinaryEncodingId(self, id: str) -> str:
    """
    Calls Qt's 'QString
    QOpcUaGenericStructHandler::typeIdForBinaryEncodingId(const QString &id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructHandler::typeIdForBinaryEncodingId(const
    #      QString &id) const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaGenericStructHandler25typeIdForBinaryEncodingIdE'
        'RK7QString',
        id,
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
  @overload(QOpcUaClient, QObject)
  @overload(QOpcUaClient, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      client: Optional[QOpcUaClient],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaGenericStructHandler::QOpcUaGenericStructHandler(QOpcUaClient
    *client, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

    Parameters
    ----------

    client : Optional[QOpcUaClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpcUaGenericStructHandler::QOpcUaGenericStructHandler(QOpcUaClient
    #      *client, QObject *parent)
    self._noteCreation(QOpcUaGenericStructHandler, lambda: Rituals.call(
        'ritual_ZN26QOpcUaGenericStructHandlerC1EP12QOpcUaClientP7QObject',
        self._addressOf(client), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QOpcUaGenericStructHandlerPrivate]:
    """
    Calls Qt's 'QOpcUaGenericStructHandlerPrivate
    *QOpcUaGenericStructHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#d_func

    Returns
    -------

    Optional[QOpcUaGenericStructHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaGenericStructHandlerPrivate
    #      *QOpcUaGenericStructHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler6d_funcEv',
    )
    from . import QOpcUaGenericStructHandlerPrivate
    return QOpcUaGenericStructHandlerPrivate._cuteAt(address)

  def initialize(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaGenericStructHandler::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#initialize
    """
    #  bool QOpcUaGenericStructHandler::initialize()
    return self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler10initializeEv',
    )

  @overload(str)
  def createGenericStructValueForTypeId(
      self,
      typeId: str,
  ) -> QOpcUaGenericStructValue:
    """
    Calls Qt's 'QOpcUaGenericStructValue
    QOpcUaGenericStructHandler::createGenericStructValueForTypeId(const
    QString &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
    #  QOpcUaGenericStructValue
    #      QOpcUaGenericStructHandler::createGenericStructValueForTypeId(
    #      const QString &typeId)
    address = self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler33createGenericStructValueFor'
        'TypeIdERK7QString',
        typeId,
    )
    from . import QOpcUaGenericStructValue
    return QOpcUaGenericStructValue._cuteOwning(address)

  @overload(QOpcUaStructureDefinition, str, str)
  @overload(QOpcUaStructureDefinition, str, str, QOpcUa.IsAbstract)
  def addCustomStructureDefinition(
      self,
      definition: QOpcUaStructureDefinition,
      typeId: str,
      name: str,
      isAbstract: QOpcUa.IsAbstract = QOpcUa.IsAbstract.NotAbstract,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaGenericStructHandler::addCustomStructureDefinition(const
    QOpcUaStructureDefinition &definition, const QString &typeId, const
    QString &name, QOpcUa::IsAbstract isAbstract)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.IsAbstract.NotAbstract.
    """
    #  bool QOpcUaGenericStructHandler::addCustomStructureDefinition(const
    #      QOpcUaStructureDefinition &definition, const QString &typeId,
    #      const QString &name, QOpcUa::IsAbstract isAbstract)
    return self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler28addCustomStructureDefinitio'
        'nERK25QOpcUaStructureDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE',
        self._valueOf(definition), typeId, name, isAbstract.value,
    )

  @overload(QOpcUaEnumDefinition, str, str)
  @overload(QOpcUaEnumDefinition, str, str, QOpcUa.IsAbstract)
  def addCustomEnumDefinition(
      self,
      definition: QOpcUaEnumDefinition,
      typeId: str,
      name: str,
      isAbstract: QOpcUa.IsAbstract = QOpcUa.IsAbstract.NotAbstract,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaGenericStructHandler::addCustomEnumDefinition(const
    QOpcUaEnumDefinition &definition, const QString &typeId, const QString
    &name, QOpcUa::IsAbstract isAbstract)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html

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
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.IsAbstract.NotAbstract.
    """
    #  bool QOpcUaGenericStructHandler::addCustomEnumDefinition(const
    #      QOpcUaEnumDefinition &definition, const QString &typeId, const
    #      QString &name, QOpcUa::IsAbstract isAbstract)
    return self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler23addCustomEnumDefinitionERK2'
        '0QOpcUaEnumDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE',
        self._valueOf(definition), typeId, name, isAbstract.value,
    )

  @overload(bool)
  def initializedChanged(self, initialized: bool) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructHandler::initializedChanged(bool
    initialized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructhandler.html#initializedChanged

    Parameters
    ----------

    initialized : bool
      Passed on as it is.
    """
    #  void QOpcUaGenericStructHandler::initializedChanged(bool initialized)
    self.uglySide.call(
        'ritual_ZN26QOpcUaGenericStructHandler18initializedChangedEb',
        initialized,
    )

  @staticmethod
  def decode(*__, **_) -> Never:
    """
    Qt's 'std::optional<QOpcUaGenericStructValue>
    QOpcUaGenericStructHandler::decode(const QOpcUaExtensionObject
    &extensionObject) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandler.decode' has no cute function yet. Qt's "
        "'std::optional<QOpcUaGenericStructValue> "
        "QOpcUaGenericStructHandler::decode(const QOpcUaExtensionObject "
        "&extensionObject) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def encode(*__, **_) -> Never:
    """
    Qt's 'std::optional<QOpcUaExtensionObject>
    QOpcUaGenericStructHandler::encode(const QOpcUaGenericStructValue
    &value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructHandler.encode' has no cute function yet. Qt's "
        "'std::optional<QOpcUaExtensionObject> "
        "QOpcUaGenericStructHandler::encode(const QOpcUaGenericStructValue "
        "&value)': gives a type Python has no way to take yet.")
