"""
QOpcUaSimpleAttributeOperand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuasimpleattributeoperand.h, Qt 6.12.0. Changes made here are
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
  from typing import Never

  from . import QOpcUaQualifiedName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaQualifiedName = WAIT['QOpcUaQualifiedName']


class QOpcUaSimpleAttributeOperand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaSimpleAttributeOperand: a plain Python object
  standing in front of one C++ QOpcUaSimpleAttributeOperand.

  C++ hands a QOpcUaSimpleAttributeOperand around as a copy, so every C++
  QOpcUaSimpleAttributeOperand behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaSimpleAttributeOperand that has a ritual and
  that Python can call so far, 10 names in all: 'typeId', 'setTypeId',
  'browsePath', 'setBrowsePath', 'attributeId', 'setAttributeId',
  'indexRange', 'setIndexRange', '__eq__', '__ne__'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaSimpleAttributeOperand
    &QOpcUaSimpleAttributeOperand::operator=(const
    QOpcUaSimpleAttributeOperand &a0)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QVariant QOpcUaSimpleAttributeOperand::operator QVariant() const':
    an operator Python has no name for.
  - Qt's 'QOpcUaSimpleAttributeOperand::~QOpcUaSimpleAttributeOperand()': the
    destructor: Python removes its C++ QOpcUaSimpleAttributeOperand by it,
    and has no other use for it.
  - Qt's 'QList<QOpcUaQualifiedName>
    &QOpcUaSimpleAttributeOperand::browsePathRef()': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaSimpleAttributeOperand is created at the first use, not by
    'QOpcUaSimpleAttributeOperand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaSimpleAttributeOperand back gives a copy the
    ritual made for Python, in a new cute QOpcUaSimpleAttributeOperand.
  - Each name of Qt's QOpcUaSimpleAttributeOperand that has no cute function
    yet, 'browsePathRef', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaSimpleAttributeOperand'

  #  Qt's '~QOpcUaSimpleAttributeOperand()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaSimpleAttributeOperand behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QOpcUaSimpleAttributeOperandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaSimpleAttributeOperand::typeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#typeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaSimpleAttributeOperand::typeId() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaSimpleAttributeOperand6typeIdEv',
    )

  def browsePath(self) -> QList[QOpcUaQualifiedName]:
    """
    Calls Qt's 'QList<QOpcUaQualifiedName>
    QOpcUaSimpleAttributeOperand::browsePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#browsePath

    Returns
    -------

    QList[QOpcUaQualifiedName]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaQualifiedName> QOpcUaSimpleAttributeOperand::browsePath()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaSimpleAttributeOperand10browsePathEv',
    )
    from . import QOpcUaQualifiedName
    return QList[QOpcUaQualifiedName]._cuteOwning(address)

  def attributeId(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute
    QOpcUaSimpleAttributeOperand::attributeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#attributeId

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaSimpleAttributeOperand::attributeId()
    #      const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK28QOpcUaSimpleAttributeOperand11attributeIdEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaSimpleAttributeOperand::indexRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaSimpleAttributeOperand::indexRange() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaSimpleAttributeOperand10indexRangeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTypeId(self, typeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaSimpleAttributeOperand::setTypeId(const QString
    &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#setTypeId

    Parameters
    ----------

    typeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaSimpleAttributeOperand::setTypeId(const QString &typeId)
    self.uglySide.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperand9setTypeIdERK7QString',
        typeId,
    )

  @overload(QList[QOpcUaQualifiedName])
  def setBrowsePath(self, browsePath: QList[QOpcUaQualifiedName]) -> None:
    """
    Calls Qt's 'void QOpcUaSimpleAttributeOperand::setBrowsePath(const
    QList<QOpcUaQualifiedName> &browsePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#setBrowsePath

    Parameters
    ----------

    browsePath : QList[QOpcUaQualifiedName]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaSimpleAttributeOperand::setBrowsePath(const
    #      QList<QOpcUaQualifiedName> &browsePath)
    self.uglySide.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperand13setBrowsePathERK5QListI19'
        'QOpcUaQualifiedNameE',
        self._valueOf(browsePath),
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttributeId(self, attributeId: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void
    QOpcUaSimpleAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
    attributeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#setAttributeId

    Parameters
    ----------

    attributeId : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void
    #      QOpcUaSimpleAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
    #      attributeId)
    self.uglySide.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperand14setAttributeIdEN6QOpcUa13'
        'NodeAttributeE',
        attributeId.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaSimpleAttributeOperand::setIndexRange(const
    QString &indexRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaSimpleAttributeOperand::setIndexRange(const QString
    #      &indexRange)
    self.uglySide.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperand13setIndexRangeERK7QString',
        indexRange,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaSimpleAttributeOperand) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaSimpleAttributeOperand &lhs,
    const QOpcUaSimpleAttributeOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#operator==

    Parameters
    ----------

    rhs : QOpcUaSimpleAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaSimpleAttributeOperand,
      which stays Python's own.
    """
    #  bool operator==(const QOpcUaSimpleAttributeOperand &lhs, const
    #      QOpcUaSimpleAttributeOperand &rhs)
    return Rituals.call(
        'ritual_ZeqRK28QOpcUaSimpleAttributeOperandS1_',
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
  def __ne__(self, rhs: QOpcUaSimpleAttributeOperand) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaSimpleAttributeOperand &lhs,
    const QOpcUaSimpleAttributeOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaSimpleAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaSimpleAttributeOperand,
      which stays Python's own.
    """
    #  bool operator!=(const QOpcUaSimpleAttributeOperand &lhs, const
    #      QOpcUaSimpleAttributeOperand &rhs)
    return Rituals.call(
        'ritual_ZneRK28QOpcUaSimpleAttributeOperandS1_',
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
    'QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html
    """
    #  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand()
    self._noteCreation(QOpcUaSimpleAttributeOperand, lambda: Rituals.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperandC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaSimpleAttributeOperand) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const
    QOpcUaSimpleAttributeOperand &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html

    Parameters
    ----------

    a0 : QOpcUaSimpleAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaSimpleAttributeOperand,
      which stays Python's own.
    """
    #  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const
    #      QOpcUaSimpleAttributeOperand &a0)
    self._noteCreation(QOpcUaSimpleAttributeOperand, lambda: Rituals.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperandC1ERKS_', self._valueOf(a0),
    ))

  @overload(str, int, str)
  @overload(str, int, str, QOpcUa.NodeAttribute)
  def __init__(
      self,
      name: str,
      namespaceIndex: int,
      typeId: str,
      attributeId: QOpcUa.NodeAttribute = QOpcUa.NodeAttribute.Value,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const QString
    &name, quint16 namespaceIndex, const QString &typeId,
    QOpcUa::NodeAttribute attributeId)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    namespaceIndex : int
      Passed on as it is.

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    attributeId : QOpcUa.NodeAttribute
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.NodeAttribute.Value.
    """
    #  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const
    #      QString &name, quint16 namespaceIndex, const QString &typeId,
    #      QOpcUa::NodeAttribute attributeId)
    self._noteCreation(QOpcUaSimpleAttributeOperand, lambda: Rituals.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperandC1ERK7QStringtS2_N6QOpcUa13'
        'NodeAttributeE',
        name, namespaceIndex, typeId, attributeId.value,
    ))

  @overload(QOpcUa.NodeAttribute, str)
  def __init__(self, attributeId: QOpcUa.NodeAttribute, typeId: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(QOpcUa::
    NodeAttribute attributeId, const QString &typeId)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuasimpleattributeoperand.html

    Parameters
    ----------

    attributeId : QOpcUa.NodeAttribute
      Passed on as its number.

    typeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(
    #      QOpcUa::NodeAttribute attributeId, const QString &typeId)
    self._noteCreation(QOpcUaSimpleAttributeOperand, lambda: Rituals.call(
        'ritual_ZN28QOpcUaSimpleAttributeOperandC1EN6QOpcUa13NodeAttributeE'
        'RK7QString',
        attributeId.value, typeId,
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
  def browsePathRef(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUaQualifiedName>
    &QOpcUaSimpleAttributeOperand::browsePathRef()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaSimpleAttributeOperand.browsePathRef' has no cute function "
        "yet. Qt's 'QList<QOpcUaQualifiedName> "
        "&QOpcUaSimpleAttributeOperand::browsePathRef()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QOpcUaSimpleAttributeOperand>': the list of
#  QOpcUaSimpleAttributeOperand, which 'QList[QOpcUaSimpleAttributeOperand]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QOpcUaSimpleAttributeOperand.
QList.createKind(
    QOpcUaSimpleAttributeOperand, 'value',
    make='ritual_list_make_QOpcUaSimpleAttributeOperand',
    add='ritual_list_add_QOpcUaSimpleAttributeOperand',
    size='ritual_list_size_QOpcUaSimpleAttributeOperand',
    at='ritual_list_at_QOpcUaSimpleAttributeOperand',
    drop='ritual_list_drop_QOpcUaSimpleAttributeOperand',
)
