"""
QOpcUaBrowsePathTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuabrowsepathtarget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaExpandedNodeId
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']


class QOpcUaBrowsePathTarget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaBrowsePathTarget: a plain Python object
  standing in front of one C++ QOpcUaBrowsePathTarget.

  C++ hands a QOpcUaBrowsePathTarget around as a copy, so every C++
  QOpcUaBrowsePathTarget behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaBrowsePathTarget that has a ritual and that
  Python can call so far, 6 names in all: '__eq__', 'targetId',
  'setTargetId', 'remainingPathIndex', 'setRemainingPathIndex',
  'isFullyResolved'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaBrowsePathTarget &QOpcUaBrowsePathTarget::operator=(const
    QOpcUaBrowsePathTarget &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaBrowsePathTarget::~QOpcUaBrowsePathTarget()': the destructor:
    Python removes its C++ QOpcUaBrowsePathTarget by it, and has no other use
    for it.
  - Qt's 'QOpcUaExpandedNodeId &QOpcUaBrowsePathTarget::targetIdRef()': gives
    a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaBrowsePathTarget is created at the first use, not by
    'QOpcUaBrowsePathTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaBrowsePathTarget back gives a copy the ritual
    made for Python, in a new cute QOpcUaBrowsePathTarget.
  - Each name of Qt's QOpcUaBrowsePathTarget that has no cute function yet,
    'targetIdRef', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QOpcUaBrowsePathTarget'

  #  Qt's '~QOpcUaBrowsePathTarget()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaBrowsePathTarget behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QOpcUaBrowsePathTargetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def targetId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId QOpcUaBrowsePathTarget::targetId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#targetId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaBrowsePathTarget::targetId() const
    address = self.uglySide.call(
        'ritual_ZNK22QOpcUaBrowsePathTarget8targetIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def remainingPathIndex(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaBrowsePathTarget::remainingPathIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#remainingPathIndex
    """
    #  quint32 QOpcUaBrowsePathTarget::remainingPathIndex() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaBrowsePathTarget18remainingPathIndexEv',
    )

  def isFullyResolved(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaBrowsePathTarget::isFullyResolved() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#isFullyResolved
    """
    #  bool QOpcUaBrowsePathTarget::isFullyResolved() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaBrowsePathTarget15isFullyResolvedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaExpandedNodeId)
  def setTargetId(self, targetId: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaBrowsePathTarget::setTargetId(const
    QOpcUaExpandedNodeId &targetId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#setTargetId

    Parameters
    ----------

    targetId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaBrowsePathTarget::setTargetId(const QOpcUaExpandedNodeId
    #      &targetId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaBrowsePathTarget11setTargetIdERK20QOpcUaExpandedN'
        'odeId',
        self._valueOf(targetId),
    )

  @overload(int)
  def setRemainingPathIndex(self, remainingPathIndex: int) -> None:
    """
    Calls Qt's 'void QOpcUaBrowsePathTarget::setRemainingPathIndex(quint32
    remainingPathIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#setRemainingPathIndex

    Parameters
    ----------

    remainingPathIndex : int
      Passed on as it is.
    """
    #  void QOpcUaBrowsePathTarget::setRemainingPathIndex(quint32
    #      remainingPathIndex)
    self.uglySide.call(
        'ritual_ZN22QOpcUaBrowsePathTarget21setRemainingPathIndexEj',
        remainingPathIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaBrowsePathTarget) -> bool:
    """
    Calls Qt's 'bool QOpcUaBrowsePathTarget::operator==(const
    QOpcUaBrowsePathTarget &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#operator==

    Parameters
    ----------

    rhs : QOpcUaBrowsePathTarget
      Passed on as a value: Qt reads the C++ QOpcUaBrowsePathTarget, which
      stays Python's own.
    """
    #  bool QOpcUaBrowsePathTarget::operator==(const QOpcUaBrowsePathTarget
    #      &rhs) const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaBrowsePathTargeteqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    'QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#QOpcUaBrowsePathTarget
    """
    #  QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget()
    self._noteCreation(QOpcUaBrowsePathTarget, lambda: Rituals.call(
        'ritual_ZN22QOpcUaBrowsePathTargetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaBrowsePathTarget) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget(const
    QOpcUaBrowsePathTarget &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowsepathtarget.html#QOpcUaBrowsePathTarget

    Parameters
    ----------

    a0 : QOpcUaBrowsePathTarget
      Passed on as a value: Qt reads the C++ QOpcUaBrowsePathTarget, which
      stays Python's own.
    """
    #  QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget(const
    #      QOpcUaBrowsePathTarget &a0)
    self._noteCreation(QOpcUaBrowsePathTarget, lambda: Rituals.call(
        'ritual_ZN22QOpcUaBrowsePathTargetC1ERKS_', self._valueOf(a0),
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
  def targetIdRef(*__, **_) -> Never:
    """
    Qt's 'QOpcUaExpandedNodeId &QOpcUaBrowsePathTarget::targetIdRef()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaBrowsePathTarget.targetIdRef' has no cute function yet. "
        "Qt's 'QOpcUaExpandedNodeId "
        "&QOpcUaBrowsePathTarget::targetIdRef()': gives a type Python has "
        "no way to take yet.")


#  Qt's 'QList<QOpcUaBrowsePathTarget>': the list of QOpcUaBrowsePathTarget,
#  which 'QList[QOpcUaBrowsePathTarget]' gives. It is made here, so that
#  there is one as soon as there can be a QOpcUaBrowsePathTarget.
QList.createKind(
    QOpcUaBrowsePathTarget, 'value',
    make='ritual_list_make_QOpcUaBrowsePathTarget',
    add='ritual_list_add_QOpcUaBrowsePathTarget',
    size='ritual_list_size_QOpcUaBrowsePathTarget',
    at='ritual_list_at_QOpcUaBrowsePathTarget',
    drop='ritual_list_drop_QOpcUaBrowsePathTarget',
)
