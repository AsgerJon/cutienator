"""
QOpcUaReferenceDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuareferencedescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaExpandedNodeId, QOpcUaLocalizedText
  from . import QOpcUaQualifiedName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']
  QOpcUaQualifiedName = WAIT['QOpcUaQualifiedName']


class QOpcUaReferenceDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaReferenceDescription: a plain Python object
  standing in front of one C++ QOpcUaReferenceDescription.

  C++ hands a QOpcUaReferenceDescription around as a copy, so every C++
  QOpcUaReferenceDescription behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaReferenceDescription that has a ritual and
  that Python can call so far, 14 names in all: 'refTypeId', 'setRefTypeId',
  'targetNodeId', 'setTargetNodeId', 'browseName', 'setBrowseName',
  'displayName', 'setDisplayName', 'nodeClass', 'setNodeClass',
  'setIsForwardReference', 'isForwardReference', 'setTypeDefinition',
  'typeDefinition'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaReferenceDescription
    &QOpcUaReferenceDescription::operator=(const QOpcUaReferenceDescription
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaReferenceDescription::~QOpcUaReferenceDescription()': the
    destructor: Python removes its C++ QOpcUaReferenceDescription by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaReferenceDescription is created at the first use, not by
    'QOpcUaReferenceDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaReferenceDescription back gives a copy the
    ritual made for Python, in a new cute QOpcUaReferenceDescription.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaReferenceDescription'

  #  Qt's '~QOpcUaReferenceDescription()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaReferenceDescription behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QOpcUaReferenceDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def refTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaReferenceDescription::refTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#refTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaReferenceDescription::refTypeId() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription9refTypeIdEv',
    )

  def targetNodeId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId
    QOpcUaReferenceDescription::targetNodeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#targetNodeId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaReferenceDescription::targetNodeId() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription12targetNodeIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def browseName(self) -> QOpcUaQualifiedName:
    """
    Calls Qt's 'QOpcUaQualifiedName QOpcUaReferenceDescription::browseName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#browseName

    Returns
    -------

    QOpcUaQualifiedName
      A new cute QOpcUaQualifiedName around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaQualifiedName QOpcUaReferenceDescription::browseName() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription10browseNameEv',
    )
    from . import QOpcUaQualifiedName
    return QOpcUaQualifiedName._cuteOwning(address)

  def displayName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaReferenceDescription::displayName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#displayName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaReferenceDescription::displayName() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription11displayNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def nodeClass(self) -> QOpcUa.NodeClass:
    """
    Calls Qt's 'QOpcUa::NodeClass QOpcUaReferenceDescription::nodeClass()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#nodeClass

    Returns
    -------

    QOpcUa.NodeClass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.NodeClass(number)'
      gives.
    """
    #  QOpcUa::NodeClass QOpcUaReferenceDescription::nodeClass() const
    return QOpcUa.NodeClass(self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription9nodeClassEv',
    ))

  def isForwardReference(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaReferenceDescription::isForwardReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#isForwardReference
    """
    #  bool QOpcUaReferenceDescription::isForwardReference() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription18isForwardReferenceEv',
    )

  def typeDefinition(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId
    QOpcUaReferenceDescription::typeDefinition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#typeDefinition

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaReferenceDescription::typeDefinition()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaReferenceDescription14typeDefinitionEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setRefTypeId(self, refTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setRefTypeId(const QString
    &refTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setRefTypeId

    Parameters
    ----------

    refTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaReferenceDescription::setRefTypeId(const QString
    #      &refTypeId)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription12setRefTypeIdERK7QString',
        refTypeId,
    )

  @overload(QOpcUaExpandedNodeId)
  def setTargetNodeId(self, targetNodeId: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setTargetNodeId(const
    QOpcUaExpandedNodeId &targetNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setTargetNodeId

    Parameters
    ----------

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaReferenceDescription::setTargetNodeId(const
    #      QOpcUaExpandedNodeId &targetNodeId)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription15setTargetNodeIdERK20QOpcUaE'
        'xpandedNodeId',
        self._valueOf(targetNodeId),
    )

  @overload(QOpcUaQualifiedName)
  def setBrowseName(self, browseName: QOpcUaQualifiedName) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setBrowseName(const
    QOpcUaQualifiedName &browseName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setBrowseName

    Parameters
    ----------

    browseName : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.
    """
    #  void QOpcUaReferenceDescription::setBrowseName(const
    #      QOpcUaQualifiedName &browseName)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription13setBrowseNameERK19QOpcUaQua'
        'lifiedName',
        self._valueOf(browseName),
    )

  @overload(QOpcUaLocalizedText)
  def setDisplayName(self, displayName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setDisplayName(const
    QOpcUaLocalizedText &displayName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setDisplayName

    Parameters
    ----------

    displayName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaReferenceDescription::setDisplayName(const
    #      QOpcUaLocalizedText &displayName)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription14setDisplayNameERK19QOpcUaLo'
        'calizedText',
        self._valueOf(displayName),
    )

  @overload(QOpcUa.NodeClass)
  def setNodeClass(self, nodeClass: QOpcUa.NodeClass) -> None:
    """
    Calls Qt's 'void
    QOpcUaReferenceDescription::setNodeClass(QOpcUa::NodeClass nodeClass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setNodeClass

    Parameters
    ----------

    nodeClass : QOpcUa.NodeClass
      Passed on as its number.
    """
    #  void QOpcUaReferenceDescription::setNodeClass(QOpcUa::NodeClass
    #      nodeClass)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription12setNodeClassEN6QOpcUa9NodeC'
        'lassE',
        nodeClass.value,
    )

  @overload(bool)
  def setIsForwardReference(self, isForwardReference: bool) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setIsForwardReference(bool
    isForwardReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html

    Parameters
    ----------

    isForwardReference : bool
      Passed on as it is.
    """
    #  void QOpcUaReferenceDescription::setIsForwardReference(bool
    #      isForwardReference)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription21setIsForwardReferenceEb',
        isForwardReference,
    )

  @overload(QOpcUaExpandedNodeId)
  def setTypeDefinition(self, typeDefinition: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaReferenceDescription::setTypeDefinition(const
    QOpcUaExpandedNodeId &typeDefinition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html#setTypeDefinition

    Parameters
    ----------

    typeDefinition : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaReferenceDescription::setTypeDefinition(const
    #      QOpcUaExpandedNodeId &typeDefinition)
    self.uglySide.call(
        'ritual_ZN26QOpcUaReferenceDescription17setTypeDefinitionERK20QOpcU'
        'aExpandedNodeId',
        self._valueOf(typeDefinition),
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
    'QOpcUaReferenceDescription::QOpcUaReferenceDescription()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html
    """
    #  QOpcUaReferenceDescription::QOpcUaReferenceDescription()
    self._noteCreation(QOpcUaReferenceDescription, lambda: Rituals.call(
        'ritual_ZN26QOpcUaReferenceDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaReferenceDescription) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaReferenceDescription::QOpcUaReferenceDescription(const
    QOpcUaReferenceDescription &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareferencedescription.html

    Parameters
    ----------

    other : QOpcUaReferenceDescription
      Passed on as a value: Qt reads the C++ QOpcUaReferenceDescription,
      which stays Python's own.
    """
    #  QOpcUaReferenceDescription::QOpcUaReferenceDescription(const
    #      QOpcUaReferenceDescription &other)
    self._noteCreation(QOpcUaReferenceDescription, lambda: Rituals.call(
        'ritual_ZN26QOpcUaReferenceDescriptionC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QOpcUaReferenceDescription>': the list of
#  QOpcUaReferenceDescription, which 'QList[QOpcUaReferenceDescription]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QOpcUaReferenceDescription.
QList.createKind(
    QOpcUaReferenceDescription, 'value',
    make='ritual_list_make_QOpcUaReferenceDescription',
    add='ritual_list_add_QOpcUaReferenceDescription',
    size='ritual_list_size_QOpcUaReferenceDescription',
    at='ritual_list_at_QOpcUaReferenceDescription',
    drop='ritual_list_drop_QOpcUaReferenceDescription',
)
