"""
QOpcUaQualifiedName binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaqualifiedname.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QOpcUaQualifiedName(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaQualifiedName: a plain Python object standing
  in front of one C++ QOpcUaQualifiedName.

  C++ hands a QOpcUaQualifiedName around as a copy, so every C++
  QOpcUaQualifiedName behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaQualifiedName that has a ritual and that
  Python can call so far, 6 names in all: '__eq__', 'name', 'setName',
  'namespaceIndex', 'setNamespaceIndex', '__rlshift__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaQualifiedName &QOpcUaQualifiedName::operator=(const
    QOpcUaQualifiedName &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaQualifiedName::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaQualifiedName::~QOpcUaQualifiedName()': the destructor:
    Python removes its C++ QOpcUaQualifiedName by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaQualifiedName is created at the first use, not by
    'QOpcUaQualifiedName(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaQualifiedName back gives a copy the ritual made
    for Python, in a new cute QOpcUaQualifiedName.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaQualifiedName'

  #  Qt's '~QOpcUaQualifiedName()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaQualifiedName behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaQualifiedNameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QOpcUaQualifiedName::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaqualifiedname.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaQualifiedName::name() const
    return self.uglySide.call('ritual_ZNK19QOpcUaQualifiedName4nameEv')

  def namespaceIndex(self) -> int:
    """
    Calls Qt's 'quint16 QOpcUaQualifiedName::namespaceIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#namespaceIndex
    """
    #  quint16 QOpcUaQualifiedName::namespaceIndex() const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaQualifiedName14namespaceIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QOpcUaQualifiedName::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaqualifiedname.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaQualifiedName::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QOpcUaQualifiedName7setNameERK7QString', name,
    )

  @overload(int)
  def setNamespaceIndex(self, namespaceIndex: int) -> None:
    """
    Calls Qt's 'void QOpcUaQualifiedName::setNamespaceIndex(quint16
    namespaceIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#setNamespaceIndex

    Parameters
    ----------

    namespaceIndex : int
      Passed on as it is.
    """
    #  void QOpcUaQualifiedName::setNamespaceIndex(quint16 namespaceIndex)
    self.uglySide.call(
        'ritual_ZN19QOpcUaQualifiedName17setNamespaceIndexEt',
        namespaceIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaQualifiedName) -> bool:
    """
    Calls Qt's 'bool QOpcUaQualifiedName::operator==(const
    QOpcUaQualifiedName &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#operator==

    Parameters
    ----------

    rhs : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.
    """
    #  bool QOpcUaQualifiedName::operator==(const QOpcUaQualifiedName &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaQualifiedNameeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QOpcUaQualifiedName
    &qn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QOpcUaQualifiedName &qn)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QOpcUaQualifiedName',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QOpcUaQualifiedName::QOpcUaQualifiedName()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#QOpcUaQualifiedName
    """
    #  QOpcUaQualifiedName::QOpcUaQualifiedName()
    self._noteCreation(QOpcUaQualifiedName, lambda: Rituals.call(
        'ritual_ZN19QOpcUaQualifiedNameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaQualifiedName) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaQualifiedName::QOpcUaQualifiedName(const QOpcUaQualifiedName
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#QOpcUaQualifiedName

    Parameters
    ----------

    a0 : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.
    """
    #  QOpcUaQualifiedName::QOpcUaQualifiedName(const QOpcUaQualifiedName
    #      &a0)
    self._noteCreation(QOpcUaQualifiedName, lambda: Rituals.call(
        'ritual_ZN19QOpcUaQualifiedNameC1ERKS_', self._valueOf(a0),
    ))

  @overload(int, str)
  def __init__(self, namespaceIndex: int, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaQualifiedName::QOpcUaQualifiedName(quint16 namespaceIndex, const
    QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaqualifiedname.html#QOpcUaQualifiedName

    Parameters
    ----------

    namespaceIndex : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaQualifiedName::QOpcUaQualifiedName(quint16 namespaceIndex, const
    #      QString &name)
    self._noteCreation(QOpcUaQualifiedName, lambda: Rituals.call(
        'ritual_ZN19QOpcUaQualifiedNameC1EtRK7QString', namespaceIndex, name,
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


#  Qt's 'QList<QOpcUaQualifiedName>': the list of QOpcUaQualifiedName, which
#  'QList[QOpcUaQualifiedName]' gives. It is made here, so that there is one
#  as soon as there can be a QOpcUaQualifiedName.
QList.createKind(
    QOpcUaQualifiedName, 'value',
    make='ritual_list_make_QOpcUaQualifiedName',
    add='ritual_list_add_QOpcUaQualifiedName',
    size='ritual_list_size_QOpcUaQualifiedName',
    at='ritual_list_at_QOpcUaQualifiedName',
    drop='ritual_list_drop_QOpcUaQualifiedName',
)
