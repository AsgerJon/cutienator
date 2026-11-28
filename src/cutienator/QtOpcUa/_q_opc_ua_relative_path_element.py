"""
QOpcUaRelativePathElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuarelativepathelement.h, Qt 6.12.0. Changes made here are
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
  from . import QOpcUaQualifiedName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaQualifiedName = WAIT['QOpcUaQualifiedName']


class QOpcUaRelativePathElement(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaRelativePathElement: a plain Python object
  standing in front of one C++ QOpcUaRelativePathElement.

  C++ hands a QOpcUaRelativePathElement around as a copy, so every C++
  QOpcUaRelativePathElement behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaRelativePathElement that has a ritual and that
  Python can call so far, 10 names in all: 'referenceTypeId',
  'setReferenceTypeId', 'isInverse', 'setIsInverse', 'includeSubtypes',
  'setIncludeSubtypes', 'targetName', 'setTargetName', '__eq__', '__ne__'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaRelativePathElement
    &QOpcUaRelativePathElement::operator=(const QOpcUaRelativePathElement
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaRelativePathElement::~QOpcUaRelativePathElement()': the
    destructor: Python removes its C++ QOpcUaRelativePathElement by it, and
    has no other use for it.
  - Qt's 'QVariant QOpcUaRelativePathElement::operator QVariant() const': an
    operator Python has no name for.

  What to expect
  --------------

  - The C++ QOpcUaRelativePathElement is created at the first use, not by
    'QOpcUaRelativePathElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaRelativePathElement back gives a copy the
    ritual made for Python, in a new cute QOpcUaRelativePathElement.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaRelativePathElement'

  #  Qt's '~QOpcUaRelativePathElement()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaRelativePathElement behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaRelativePathElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def referenceTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaRelativePathElement::referenceTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#referenceTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaRelativePathElement::referenceTypeId() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaRelativePathElement15referenceTypeIdEv',
    )

  def isInverse(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaRelativePathElement::isInverse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#isInverse
    """
    #  bool QOpcUaRelativePathElement::isInverse() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaRelativePathElement9isInverseEv',
    )

  def includeSubtypes(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaRelativePathElement::includeSubtypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#includeSubtypes
    """
    #  bool QOpcUaRelativePathElement::includeSubtypes() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaRelativePathElement15includeSubtypesEv',
    )

  def targetName(self) -> QOpcUaQualifiedName:
    """
    Calls Qt's 'QOpcUaQualifiedName QOpcUaRelativePathElement::targetName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#targetName

    Returns
    -------

    QOpcUaQualifiedName
      A new cute QOpcUaQualifiedName around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaQualifiedName QOpcUaRelativePathElement::targetName() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaRelativePathElement10targetNameEv',
    )
    from . import QOpcUaQualifiedName
    return QOpcUaQualifiedName._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setReferenceTypeId(self, referenceTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaRelativePathElement::setReferenceTypeId(const
    QString &referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaRelativePathElement::setReferenceTypeId(const QString
    #      &referenceTypeId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaRelativePathElement18setReferenceTypeIdERK7QStrin'
        'g',
        referenceTypeId,
    )

  @overload(QOpcUa.ReferenceTypeId)
  def setReferenceTypeId(
      self,
      referenceTypeId: QOpcUa.ReferenceTypeId,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaRelativePathElement::setReferenceTypeId(QOpcUa::ReferenceTypeId
    referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : QOpcUa.ReferenceTypeId
      Passed on as its number.
    """
    #  void QOpcUaRelativePathElement::setReferenceTypeId(QOpcUa::
    #      ReferenceTypeId referenceTypeId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaRelativePathElement18setReferenceTypeIdEN6QOpcUa1'
        '5ReferenceTypeIdE',
        referenceTypeId.value,
    )

  @overload(bool)
  def setIsInverse(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void QOpcUaRelativePathElement::setIsInverse(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#setIsInverse

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void QOpcUaRelativePathElement::setIsInverse(bool isInverse)
    self.uglySide.call(
        'ritual_ZN25QOpcUaRelativePathElement12setIsInverseEb', isInverse,
    )

  @overload(bool)
  def setIncludeSubtypes(self, includeSubtypes: bool) -> None:
    """
    Calls Qt's 'void QOpcUaRelativePathElement::setIncludeSubtypes(bool
    includeSubtypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#setIncludeSubtypes

    Parameters
    ----------

    includeSubtypes : bool
      Passed on as it is.
    """
    #  void QOpcUaRelativePathElement::setIncludeSubtypes(bool
    #      includeSubtypes)
    self.uglySide.call(
        'ritual_ZN25QOpcUaRelativePathElement18setIncludeSubtypesEb',
        includeSubtypes,
    )

  @overload(QOpcUaQualifiedName)
  def setTargetName(self, targetName: QOpcUaQualifiedName) -> None:
    """
    Calls Qt's 'void QOpcUaRelativePathElement::setTargetName(const
    QOpcUaQualifiedName &targetName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#setTargetName

    Parameters
    ----------

    targetName : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.
    """
    #  void QOpcUaRelativePathElement::setTargetName(const
    #      QOpcUaQualifiedName &targetName)
    self.uglySide.call(
        'ritual_ZN25QOpcUaRelativePathElement13setTargetNameERK19QOpcUaQual'
        'ifiedName',
        self._valueOf(targetName),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaRelativePathElement) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaRelativePathElement &lhs, const
    QOpcUaRelativePathElement &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#operator==

    Parameters
    ----------

    rhs : QOpcUaRelativePathElement
      Passed on as a value: Qt reads the C++ QOpcUaRelativePathElement, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaRelativePathElement &lhs, const
    #      QOpcUaRelativePathElement &rhs)
    return Rituals.call(
        'ritual_ZeqRK25QOpcUaRelativePathElementS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaRelativePathElement) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaRelativePathElement &lhs, const
    QOpcUaRelativePathElement &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaRelativePathElement
      Passed on as a value: Qt reads the C++ QOpcUaRelativePathElement, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaRelativePathElement &lhs, const
    #      QOpcUaRelativePathElement &rhs)
    return Rituals.call(
        'ritual_ZneRK25QOpcUaRelativePathElementS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaRelativePathElement::QOpcUaRelativePathElement()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html
    """
    #  QOpcUaRelativePathElement::QOpcUaRelativePathElement()
    self._noteCreation(QOpcUaRelativePathElement, lambda: Rituals.call(
        'ritual_ZN25QOpcUaRelativePathElementC1Ev',
    ))

  @overload(QOpcUaQualifiedName, str)
  def __init__(self, target: QOpcUaQualifiedName, refType: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    QOpcUaQualifiedName &target, const QString &refType)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html

    Parameters
    ----------

    target : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.

    refType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    #      QOpcUaQualifiedName &target, const QString &refType)
    self._noteCreation(QOpcUaRelativePathElement, lambda: Rituals.call(
        'ritual_ZN25QOpcUaRelativePathElementC1ERK19QOpcUaQualifiedNameRK7Q'
        'String',
        self._valueOf(target), refType,
    ))

  @overload(QOpcUaQualifiedName, QOpcUa.ReferenceTypeId)
  def __init__(
      self,
      target: QOpcUaQualifiedName,
      refType: QOpcUa.ReferenceTypeId,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    QOpcUaQualifiedName &target, QOpcUa::ReferenceTypeId refType)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html

    Parameters
    ----------

    target : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.

    refType : QOpcUa.ReferenceTypeId
      Passed on as its number.
    """
    #  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    #      QOpcUaQualifiedName &target, QOpcUa::ReferenceTypeId refType)
    self._noteCreation(QOpcUaRelativePathElement, lambda: Rituals.call(
        'ritual_ZN25QOpcUaRelativePathElementC1ERK19QOpcUaQualifiedNameN6QO'
        'pcUa15ReferenceTypeIdE',
        self._valueOf(target), refType.value,
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaRelativePathElement) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    QOpcUaRelativePathElement &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuarelativepathelement.html

    Parameters
    ----------

    a0 : QOpcUaRelativePathElement
      Passed on as a value: Qt reads the C++ QOpcUaRelativePathElement, which
      stays Python's own.
    """
    #  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
    #      QOpcUaRelativePathElement &a0)
    self._noteCreation(QOpcUaRelativePathElement, lambda: Rituals.call(
        'ritual_ZN25QOpcUaRelativePathElementC1ERKS_', self._valueOf(a0),
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


#  Qt's 'QList<QOpcUaRelativePathElement>': the list of
#  QOpcUaRelativePathElement, which 'QList[QOpcUaRelativePathElement]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QOpcUaRelativePathElement.
QList.createKind(
    QOpcUaRelativePathElement, 'value',
    make='ritual_list_make_QOpcUaRelativePathElement',
    add='ritual_list_add_QOpcUaRelativePathElement',
    size='ritual_list_size_QOpcUaRelativePathElement',
    at='ritual_list_at_QOpcUaRelativePathElement',
    drop='ritual_list_drop_QOpcUaRelativePathElement',
)
