"""
QOpcUaAttributeOperand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaattributeoperand.h, Qt 6.12.0. Changes made here are lost.
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

  from . import QOpcUaRelativePathElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaRelativePathElement = WAIT['QOpcUaRelativePathElement']


class QOpcUaAttributeOperand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaAttributeOperand: a plain Python object
  standing in front of one C++ QOpcUaAttributeOperand.

  C++ hands a QOpcUaAttributeOperand around as a copy, so every C++
  QOpcUaAttributeOperand behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaAttributeOperand that has a ritual and that
  Python can call so far, 12 names in all: 'nodeId', 'setNodeId', 'alias',
  'setAlias', 'browsePath', 'setBrowsePath', 'attributeId', 'setAttributeId',
  'indexRange', 'setIndexRange', '__eq__', '__ne__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaAttributeOperand &QOpcUaAttributeOperand::operator=(const
    QOpcUaAttributeOperand &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaAttributeOperand::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaAttributeOperand::~QOpcUaAttributeOperand()': the destructor:
    Python removes its C++ QOpcUaAttributeOperand by it, and has no other use
    for it.
  - Qt's 'QList<QOpcUaRelativePathElement>
    &QOpcUaAttributeOperand::browsePathRef()': gives a type Python has no way
    to take yet.

  What to expect
  --------------

  - The C++ QOpcUaAttributeOperand is created at the first use, not by
    'QOpcUaAttributeOperand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaAttributeOperand back gives a copy the ritual
    made for Python, in a new cute QOpcUaAttributeOperand.
  - Each name of Qt's QOpcUaAttributeOperand that has no cute function yet,
    'browsePathRef', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaAttributeOperand'

  #  Qt's '~QOpcUaAttributeOperand()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaAttributeOperand behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QOpcUaAttributeOperandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAttributeOperand::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaattributeoperand.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAttributeOperand::nodeId() const
    return self.uglySide.call('ritual_ZNK22QOpcUaAttributeOperand6nodeIdEv')

  def alias(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAttributeOperand::alias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaattributeoperand.html#alias

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAttributeOperand::alias() const
    return self.uglySide.call('ritual_ZNK22QOpcUaAttributeOperand5aliasEv')

  def browsePath(self) -> QList[QOpcUaRelativePathElement]:
    """
    Calls Qt's 'QList<QOpcUaRelativePathElement>
    QOpcUaAttributeOperand::browsePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#browsePath

    Returns
    -------

    QList[QOpcUaRelativePathElement]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaRelativePathElement> QOpcUaAttributeOperand::browsePath()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QOpcUaAttributeOperand10browsePathEv',
    )
    from . import QOpcUaRelativePathElement
    return QList[QOpcUaRelativePathElement]._cuteOwning(address)

  def attributeId(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute QOpcUaAttributeOperand::attributeId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#attributeId

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaAttributeOperand::attributeId() const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK22QOpcUaAttributeOperand11attributeIdEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAttributeOperand::indexRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAttributeOperand::indexRange() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaAttributeOperand10indexRangeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaAttributeOperand::setNodeId(const QString
    &nodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAttributeOperand::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAttributeOperand9setNodeIdERK7QString', nodeId,
    )

  @overload(str)
  def setAlias(self, alias: str) -> None:
    """
    Calls Qt's 'void QOpcUaAttributeOperand::setAlias(const QString &alias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#setAlias

    Parameters
    ----------

    alias : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAttributeOperand::setAlias(const QString &alias)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAttributeOperand8setAliasERK7QString', alias,
    )

  @overload(QList[QOpcUaRelativePathElement])
  def setBrowsePath(
      self,
      browsePath: QList[QOpcUaRelativePathElement],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaAttributeOperand::setBrowsePath(const
    QList<QOpcUaRelativePathElement> &browsePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#setBrowsePath

    Parameters
    ----------

    browsePath : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaAttributeOperand::setBrowsePath(const
    #      QList<QOpcUaRelativePathElement> &browsePath)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAttributeOperand13setBrowsePathERK5QListI25QOpcUa'
        'RelativePathElementE',
        self._valueOf(browsePath),
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttributeId(self, attributeId: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void
    QOpcUaAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
    attributeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#setAttributeId

    Parameters
    ----------

    attributeId : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void QOpcUaAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
    #      attributeId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAttributeOperand14setAttributeIdEN6QOpcUa13NodeAt'
        'tributeE',
        attributeId.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaAttributeOperand::setIndexRange(const QString
    &indexRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAttributeOperand::setIndexRange(const QString &indexRange)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAttributeOperand13setIndexRangeERK7QString',
        indexRange,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaAttributeOperand) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaAttributeOperand &lhs, const
    QOpcUaAttributeOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#operator==

    Parameters
    ----------

    rhs : QOpcUaAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaAttributeOperand, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaAttributeOperand &lhs, const
    #      QOpcUaAttributeOperand &rhs)
    return Rituals.call(
        'ritual_ZeqRK22QOpcUaAttributeOperandS1_',
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
  def __ne__(self, rhs: QOpcUaAttributeOperand) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaAttributeOperand &lhs, const
    QOpcUaAttributeOperand &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaAttributeOperand, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaAttributeOperand &lhs, const
    #      QOpcUaAttributeOperand &rhs)
    return Rituals.call(
        'ritual_ZneRK22QOpcUaAttributeOperandS1_',
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
    'QOpcUaAttributeOperand::QOpcUaAttributeOperand()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#QOpcUaAttributeOperand
    """
    #  QOpcUaAttributeOperand::QOpcUaAttributeOperand()
    self._noteCreation(QOpcUaAttributeOperand, lambda: Rituals.call(
        'ritual_ZN22QOpcUaAttributeOperandC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaAttributeOperand) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAttributeOperand::QOpcUaAttributeOperand(const
    QOpcUaAttributeOperand &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaattributeoperand.html#QOpcUaAttributeOperand

    Parameters
    ----------

    a0 : QOpcUaAttributeOperand
      Passed on as a value: Qt reads the C++ QOpcUaAttributeOperand, which
      stays Python's own.
    """
    #  QOpcUaAttributeOperand::QOpcUaAttributeOperand(const
    #      QOpcUaAttributeOperand &a0)
    self._noteCreation(QOpcUaAttributeOperand, lambda: Rituals.call(
        'ritual_ZN22QOpcUaAttributeOperandC1ERKS_', self._valueOf(a0),
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
    Qt's 'QList<QOpcUaRelativePathElement>
    &QOpcUaAttributeOperand::browsePathRef()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaAttributeOperand.browsePathRef' has no cute function yet. "
        "Qt's 'QList<QOpcUaRelativePathElement> "
        "&QOpcUaAttributeOperand::browsePathRef()': gives a type Python has "
        "no way to take yet.")
