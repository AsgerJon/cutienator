"""
QOpcUaNodeCreationAttributes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuanodecreationattributes.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']
  QVariant = WAIT['QVariant']


class QOpcUaNodeCreationAttributes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaNodeCreationAttributes: a plain Python object
  standing in front of one C++ QOpcUaNodeCreationAttributes.

  C++ hands a QOpcUaNodeCreationAttributes around as a copy, so every C++
  QOpcUaNodeCreationAttributes behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaNodeCreationAttributes that has a ritual and
  that Python can call so far, 56 names in all: 'accessLevel',
  'setAccessLevel', 'hasAccessLevel', 'hasArrayDimensions',
  'containsNoLoops', 'setContainsNoLoops', 'hasContainsNoLoops',
  'dataTypeId', 'setDataTypeId', 'hasDataTypeId', 'description',
  'setDescription', 'hasDescription', 'displayName', 'setDisplayName',
  'hasDisplayName', 'eventNotifier', 'setEventNotifier', 'hasEventNotifier',
  'executable', 'setExecutable', 'hasExecutable', 'historizing',
  'setHistorizing', 'hasHistorizing', 'inverseName', 'setInverseName',
  'hasInverseName', 'isAbstract', 'setIsAbstract', 'hasIsAbstract',
  'minimumSamplingInterval', 'setMinimumSamplingInterval',
  'hasMinimumSamplingInterval', 'symmetric', 'setSymmetric', 'hasSymmetric',
  'userAccessLevel', 'setUserAccessLevel', 'hasUserAccessLevel',
  'userExecutable', 'setUserExecutable', 'hasUserExecutable',
  'userWriteMask', 'setUserWriteMask', 'hasUserWriteMask', 'valueRank',
  'setValueRank', 'hasValueRank', 'writeMask', 'setWriteMask',
  'hasWriteMask', 'value', 'setValue', 'hasValue', 'valueType'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaNodeCreationAttributes
    &QOpcUaNodeCreationAttributes::operator=(const
    QOpcUaNodeCreationAttributes &rhs)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QOpcUaNodeCreationAttributes::~QOpcUaNodeCreationAttributes()': the
    destructor: Python removes its C++ QOpcUaNodeCreationAttributes by it,
    and has no other use for it.
  - Qt's 'QList<quint32> QOpcUaNodeCreationAttributes::arrayDimensions()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QOpcUaNodeCreationAttributes::setArrayDimensions(const
    QList<quint32> &arrayDimensions)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QOpcUaNodeCreationAttributes is created at the first use, not by
    'QOpcUaNodeCreationAttributes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaNodeCreationAttributes back gives a copy the
    ritual made for Python, in a new cute QOpcUaNodeCreationAttributes.
  - Each name of Qt's QOpcUaNodeCreationAttributes that has no cute function
    yet, 'arrayDimensions', 'setArrayDimensions', holds a function that
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
  __qt_class__ = 'QOpcUaNodeCreationAttributes'

  #  Qt's '~QOpcUaNodeCreationAttributes()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaNodeCreationAttributes behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QOpcUaNodeCreationAttributesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def accessLevel(self) -> QOpcUa.AccessLevel:
    """
    Calls Qt's 'QOpcUa::AccessLevel
    QOpcUaNodeCreationAttributes::accessLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#accessLevel

    Returns
    -------

    QOpcUa.AccessLevel
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::AccessLevel QOpcUaNodeCreationAttributes::accessLevel() const
    return QOpcUa.AccessLevel(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes11accessLevelEv',
    ))

  def hasAccessLevel(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasAccessLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasAccessLevel
    """
    #  bool QOpcUaNodeCreationAttributes::hasAccessLevel() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14hasAccessLevelEv',
    )

  def hasArrayDimensions(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasArrayDimensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  bool QOpcUaNodeCreationAttributes::hasArrayDimensions() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes18hasArrayDimensionsEv',
    )

  def containsNoLoops(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::containsNoLoops() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#containsNoLoops
    """
    #  bool QOpcUaNodeCreationAttributes::containsNoLoops() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes15containsNoLoopsEv',
    )

  def hasContainsNoLoops(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasContainsNoLoops()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  bool QOpcUaNodeCreationAttributes::hasContainsNoLoops() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes18hasContainsNoLoopsEv',
    )

  def dataTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaNodeCreationAttributes::dataTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#dataTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaNodeCreationAttributes::dataTypeId() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes10dataTypeIdEv',
    )

  def hasDataTypeId(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasDataTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasDataTypeId
    """
    #  bool QOpcUaNodeCreationAttributes::hasDataTypeId() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes13hasDataTypeIdEv',
    )

  def description(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText
    QOpcUaNodeCreationAttributes::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#description

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::description() const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes11descriptionEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def hasDescription(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasDescription
    """
    #  bool QOpcUaNodeCreationAttributes::hasDescription() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14hasDescriptionEv',
    )

  def displayName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText
    QOpcUaNodeCreationAttributes::displayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#displayName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::displayName() const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes11displayNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def hasDisplayName(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasDisplayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasDisplayName
    """
    #  bool QOpcUaNodeCreationAttributes::hasDisplayName() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14hasDisplayNameEv',
    )

  def eventNotifier(self) -> QOpcUa.EventNotifier:
    """
    Calls Qt's 'QOpcUa::EventNotifier
    QOpcUaNodeCreationAttributes::eventNotifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#eventNotifier

    Returns
    -------

    QOpcUa.EventNotifier
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::EventNotifier QOpcUaNodeCreationAttributes::eventNotifier()
    #      const
    return QOpcUa.EventNotifier(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes13eventNotifierEv',
    ))

  def hasEventNotifier(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasEventNotifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasEventNotifier
    """
    #  bool QOpcUaNodeCreationAttributes::hasEventNotifier() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes16hasEventNotifierEv',
    )

  def executable(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::executable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#executable
    """
    #  bool QOpcUaNodeCreationAttributes::executable() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes10executableEv',
    )

  def hasExecutable(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasExecutable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasExecutable
    """
    #  bool QOpcUaNodeCreationAttributes::hasExecutable() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes13hasExecutableEv',
    )

  def historizing(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::historizing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#historizing
    """
    #  bool QOpcUaNodeCreationAttributes::historizing() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes11historizingEv',
    )

  def hasHistorizing(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasHistorizing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasHistorizing
    """
    #  bool QOpcUaNodeCreationAttributes::hasHistorizing() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14hasHistorizingEv',
    )

  def inverseName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText
    QOpcUaNodeCreationAttributes::inverseName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#inverseName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::inverseName() const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes11inverseNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def hasInverseName(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasInverseName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasInverseName
    """
    #  bool QOpcUaNodeCreationAttributes::hasInverseName() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14hasInverseNameEv',
    )

  def isAbstract(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::isAbstract() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#isAbstract
    """
    #  bool QOpcUaNodeCreationAttributes::isAbstract() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes10isAbstractEv',
    )

  def hasIsAbstract(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasIsAbstract() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasIsAbstract
    """
    #  bool QOpcUaNodeCreationAttributes::hasIsAbstract() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes13hasIsAbstractEv',
    )

  def minimumSamplingInterval(self) -> float:
    """
    Calls Qt's 'double
    QOpcUaNodeCreationAttributes::minimumSamplingInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  double QOpcUaNodeCreationAttributes::minimumSamplingInterval() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes23minimumSamplingIntervalE'
        'v',
    )

  def hasMinimumSamplingInterval(self) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaNodeCreationAttributes::hasMinimumSamplingInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  bool QOpcUaNodeCreationAttributes::hasMinimumSamplingInterval() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes26hasMinimumSamplingInterv'
        'alEv',
    )

  def symmetric(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::symmetric() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#symmetric
    """
    #  bool QOpcUaNodeCreationAttributes::symmetric() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes9symmetricEv',
    )

  def hasSymmetric(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasSymmetric() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasSymmetric
    """
    #  bool QOpcUaNodeCreationAttributes::hasSymmetric() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes12hasSymmetricEv',
    )

  def userAccessLevel(self) -> QOpcUa.AccessLevel:
    """
    Calls Qt's 'QOpcUa::AccessLevel
    QOpcUaNodeCreationAttributes::userAccessLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#userAccessLevel

    Returns
    -------

    QOpcUa.AccessLevel
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::AccessLevel QOpcUaNodeCreationAttributes::userAccessLevel()
    #      const
    return QOpcUa.AccessLevel(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes15userAccessLevelEv',
    ))

  def hasUserAccessLevel(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasUserAccessLevel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  bool QOpcUaNodeCreationAttributes::hasUserAccessLevel() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes18hasUserAccessLevelEv',
    )

  def userExecutable(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::userExecutable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#userExecutable
    """
    #  bool QOpcUaNodeCreationAttributes::userExecutable() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes14userExecutableEv',
    )

  def hasUserExecutable(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasUserExecutable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  bool QOpcUaNodeCreationAttributes::hasUserExecutable() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes17hasUserExecutableEv',
    )

  def userWriteMask(self) -> QOpcUa.WriteMask:
    """
    Calls Qt's 'QOpcUa::WriteMask
    QOpcUaNodeCreationAttributes::userWriteMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#userWriteMask

    Returns
    -------

    QOpcUa.WriteMask
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::WriteMask QOpcUaNodeCreationAttributes::userWriteMask() const
    return QOpcUa.WriteMask(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes13userWriteMaskEv',
    ))

  def hasUserWriteMask(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasUserWriteMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasUserWriteMask
    """
    #  bool QOpcUaNodeCreationAttributes::hasUserWriteMask() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes16hasUserWriteMaskEv',
    )

  def valueRank(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaNodeCreationAttributes::valueRank() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#valueRank
    """
    #  qint32 QOpcUaNodeCreationAttributes::valueRank() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes9valueRankEv',
    )

  def hasValueRank(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasValueRank() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasValueRank
    """
    #  bool QOpcUaNodeCreationAttributes::hasValueRank() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes12hasValueRankEv',
    )

  def writeMask(self) -> QOpcUa.WriteMask:
    """
    Calls Qt's 'QOpcUa::WriteMask QOpcUaNodeCreationAttributes::writeMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#writeMask

    Returns
    -------

    QOpcUa.WriteMask
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::WriteMask QOpcUaNodeCreationAttributes::writeMask() const
    return QOpcUa.WriteMask(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes9writeMaskEv',
    ))

  def hasWriteMask(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasWriteMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasWriteMask
    """
    #  bool QOpcUaNodeCreationAttributes::hasWriteMask() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes12hasWriteMaskEv',
    )

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaNodeCreationAttributes::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaNodeCreationAttributes::value() const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes5valueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def hasValue(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributes::hasValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#hasValue
    """
    #  bool QOpcUaNodeCreationAttributes::hasValue() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes8hasValueEv',
    )

  def valueType(self) -> QOpcUa.Types:
    """
    Calls Qt's 'QOpcUa::Types QOpcUaNodeCreationAttributes::valueType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#valueType

    Returns
    -------

    QOpcUa.Types
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.Types(number)'
      gives.
    """
    #  QOpcUa::Types QOpcUaNodeCreationAttributes::valueType() const
    return QOpcUa.Types(self.uglySide.call(
        'ritual_ZNK28QOpcUaNodeCreationAttributes9valueTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUa.AccessLevel)
  def setAccessLevel(self, accessLevel: QOpcUa.AccessLevel) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setAccessLevel(QOpcUa::AccessLevel
    accessLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setAccessLevel

    Parameters
    ----------

    accessLevel : QOpcUa.AccessLevel
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributes::setAccessLevel(QOpcUa::AccessLevel
    #      accessLevel)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes14setAccessLevelE6QFlagsIN6'
        'QOpcUa14AccessLevelBitEE',
        accessLevel.value,
    )

  @overload(bool)
  def setContainsNoLoops(self, containsNoLoops: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setContainsNoLoops(bool
    containsNoLoops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html

    Parameters
    ----------

    containsNoLoops : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setContainsNoLoops(bool
    #      containsNoLoops)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes18setContainsNoLoopsEb',
        containsNoLoops,
    )

  @overload(str)
  def setDataTypeId(self, dataTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setDataTypeId(const
    QString &dataTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setDataTypeId

    Parameters
    ----------

    dataTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaNodeCreationAttributes::setDataTypeId(const QString
    #      &dataTypeId)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes13setDataTypeIdERK7QString',
        dataTypeId,
    )

  @overload(QOpcUaLocalizedText)
  def setDescription(self, description: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setDescription(const
    QOpcUaLocalizedText &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setDescription

    Parameters
    ----------

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaNodeCreationAttributes::setDescription(const
    #      QOpcUaLocalizedText &description)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes14setDescriptionERK19QOpcUa'
        'LocalizedText',
        self._valueOf(description),
    )

  @overload(QOpcUaLocalizedText)
  def setDisplayName(self, displayName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setDisplayName(const
    QOpcUaLocalizedText &displayName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setDisplayName

    Parameters
    ----------

    displayName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaNodeCreationAttributes::setDisplayName(const
    #      QOpcUaLocalizedText &displayName)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes14setDisplayNameERK19QOpcUa'
        'LocalizedText',
        self._valueOf(displayName),
    )

  @overload(QOpcUa.EventNotifier)
  def setEventNotifier(self, eventNotifier: QOpcUa.EventNotifier) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setEventNotifier(QOpcUa::EventNotifier
    eventNotifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setEventNotifier

    Parameters
    ----------

    eventNotifier : QOpcUa.EventNotifier
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributes::setEventNotifier(QOpcUa::
    #      EventNotifier eventNotifier)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes16setEventNotifierE6QFlagsI'
        'N6QOpcUa16EventNotifierBitEE',
        eventNotifier.value,
    )

  @overload(bool)
  def setExecutable(self, executable: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setExecutable(bool
    executable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setExecutable

    Parameters
    ----------

    executable : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setExecutable(bool executable)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes13setExecutableEb',
        executable,
    )

  @overload(bool)
  def setHistorizing(self, historizing: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setHistorizing(bool
    historizing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setHistorizing

    Parameters
    ----------

    historizing : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setHistorizing(bool historizing)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes14setHistorizingEb',
        historizing,
    )

  @overload(QOpcUaLocalizedText)
  def setInverseName(self, inverseName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setInverseName(const
    QOpcUaLocalizedText &inverseName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setInverseName

    Parameters
    ----------

    inverseName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaNodeCreationAttributes::setInverseName(const
    #      QOpcUaLocalizedText &inverseName)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes14setInverseNameERK19QOpcUa'
        'LocalizedText',
        self._valueOf(inverseName),
    )

  @overload(bool)
  def setIsAbstract(self, isAbstract: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setIsAbstract(bool
    isAbstract)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setIsAbstract

    Parameters
    ----------

    isAbstract : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setIsAbstract(bool isAbstract)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes13setIsAbstractEb',
        isAbstract,
    )

  @overload(float)
  def setMinimumSamplingInterval(
      self,
      minimumSamplingInterval: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setMinimumSamplingInterval(double
    minimumSamplingInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html

    Parameters
    ----------

    minimumSamplingInterval : float
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setMinimumSamplingInterval(double
    #      minimumSamplingInterval)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes26setMinimumSamplingInterva'
        'lEd',
        minimumSamplingInterval,
    )

  @overload(bool)
  def setSymmetric(self, symmetric: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setSymmetric(bool
    symmetric)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setSymmetric

    Parameters
    ----------

    symmetric : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setSymmetric(bool symmetric)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes12setSymmetricEb', symmetric,
    )

  @overload(QOpcUa.AccessLevel)
  def setUserAccessLevel(self, userAccessLevel: QOpcUa.AccessLevel) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setUserAccessLevel(QOpcUa::AccessLevel
    userAccessLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html

    Parameters
    ----------

    userAccessLevel : QOpcUa.AccessLevel
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributes::setUserAccessLevel(QOpcUa::
    #      AccessLevel userAccessLevel)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes18setUserAccessLevelE6QFlag'
        'sIN6QOpcUa14AccessLevelBitEE',
        userAccessLevel.value,
    )

  @overload(bool)
  def setUserExecutable(self, userExecutable: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setUserExecutable(bool
    userExecutable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html

    Parameters
    ----------

    userExecutable : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setUserExecutable(bool
    #      userExecutable)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes17setUserExecutableEb',
        userExecutable,
    )

  @overload(QOpcUa.WriteMask)
  def setUserWriteMask(self, userWriteMask: QOpcUa.WriteMask) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setUserWriteMask(QOpcUa::WriteMask
    userWriteMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setUserWriteMask

    Parameters
    ----------

    userWriteMask : QOpcUa.WriteMask
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributes::setUserWriteMask(QOpcUa::WriteMask
    #      userWriteMask)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes16setUserWriteMaskE6QFlagsI'
        'N6QOpcUa12WriteMaskBitEE',
        userWriteMask.value,
    )

  @overload(int)
  def setValueRank(self, valueRank: int) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setValueRank(qint32
    valueRank)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setValueRank

    Parameters
    ----------

    valueRank : int
      Passed on as it is.
    """
    #  void QOpcUaNodeCreationAttributes::setValueRank(qint32 valueRank)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes12setValueRankEi', valueRank,
    )

  @overload(QOpcUa.WriteMask)
  def setWriteMask(self, writeMask: QOpcUa.WriteMask) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeCreationAttributes::setWriteMask(QOpcUa::WriteMask writeMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setWriteMask

    Parameters
    ----------

    writeMask : QOpcUa.WriteMask
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributes::setWriteMask(QOpcUa::WriteMask
    #      writeMask)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes12setWriteMaskE6QFlagsIN6QO'
        'pcUa12WriteMaskBitEE',
        writeMask.value,
    )

  @overload(QVariant)
  @overload(QVariant, QOpcUa.Types)
  def setValue(
      self,
      value: QVariant,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributes::setValue(const QVariant
    &value, QOpcUa::Types type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.
    """
    #  void QOpcUaNodeCreationAttributes::setValue(const QVariant &value,
    #      QOpcUa::Types type)
    self.uglySide.call(
        'ritual_ZN28QOpcUaNodeCreationAttributes8setValueERK8QVariantN6QOpc'
        'Ua5TypesE',
        self._valueOf(value), type.value,
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
    'QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html
    """
    #  QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes()
    self._noteCreation(QOpcUaNodeCreationAttributes, lambda: Rituals.call(
        'ritual_ZN28QOpcUaNodeCreationAttributesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaNodeCreationAttributes) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes(const
    QOpcUaNodeCreationAttributes &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributes.html

    Parameters
    ----------

    other : QOpcUaNodeCreationAttributes
      Passed on as a value: Qt reads the C++ QOpcUaNodeCreationAttributes,
      which stays Python's own.
    """
    #  QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes(const
    #      QOpcUaNodeCreationAttributes &other)
    self._noteCreation(QOpcUaNodeCreationAttributes, lambda: Rituals.call(
        'ritual_ZN28QOpcUaNodeCreationAttributesC1ERKS_',
        self._valueOf(other),
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

  @staticmethod
  def arrayDimensions(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QOpcUaNodeCreationAttributes::arrayDimensions()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaNodeCreationAttributes.arrayDimensions' has no cute "
        "function yet. Qt's 'QList<quint32> "
        "QOpcUaNodeCreationAttributes::arrayDimensions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setArrayDimensions(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaNodeCreationAttributes::setArrayDimensions(const
    QList<quint32> &arrayDimensions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNodeCreationAttributes.setArrayDimensions' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaNodeCreationAttributes::setArrayDimensions(const "
        "QList<quint32> &arrayDimensions)': takes a type Python has no way "
        "to hand over yet.")
