"""
QQmlGuardedContextData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlguardedcontextdata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlGuardedContextData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QQmlGuardedContextData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlGuardedContextData: a plain Python object
  standing in front of one C++ QQmlGuardedContextData.

  What exists
  -----------

  Every function of Qt's QQmlGuardedContextData that has a ritual and that
  Python can call so far, 4 names in all: 'isNull', 'next', 'reset',
  'unlink'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlGuardedContextData::~QQmlGuardedContextData()': the destructor:
    Python never removes a C++ QQmlGuardedContextData.
  - Qt's
    'QQmlGuardedContextData::QQmlGuardedContextData(QQmlGuardedContextData
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlGuardedContextData
    &QQmlGuardedContextData::operator=(QQmlGuardedContextData &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlGuardedContextData::QQmlGuardedContextData(
    QQmlRefPointer<QQmlContextData> data)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlGuardedContextData
    &QQmlGuardedContextData::operator=(QQmlRefPointer<QQmlContextData> d)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlGuardedContextData::contextData() const': gives a type Python has no
    way to take yet.
  - Qt's 'void
    QQmlGuardedContextData::setContextData(QQmlRefPointer<QQmlContextData>
    contextData)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlRefPointer<QQmlContextData>
    &QQmlGuardedContextData::operator const QQmlRefPointer<QQmlContextData>
    &() const': an operator Python has no name for.
  - Qt's 'QQmlContextData &QQmlGuardedContextData::operator*() const': an
    operator Python has no name for.
  - Qt's 'QQmlContextData *QQmlGuardedContextData::operator->() const': an
    operator Python has no name for.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlGuardedContextData is created at the first use, not by
    'QQmlGuardedContextData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGuardedContextData.
  - Each name of Qt's QQmlGuardedContextData that has no cute function yet,
    'contextData', 'setContextData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGuardedContextData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlGuardedContextData::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardedcontextdata.html#isNull
    """
    #  bool QQmlGuardedContextData::isNull() const
    return self.uglySide.call('ritual_ZNK22QQmlGuardedContextData6isNullEv')

  def next(self) -> Optional[QQmlGuardedContextData]:
    """
    Calls Qt's 'QQmlGuardedContextData *QQmlGuardedContextData::next()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardedcontextdata.html#next

    Returns
    -------

    Optional[QQmlGuardedContextData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGuardedContextData *QQmlGuardedContextData::next() const
    address = self.uglySide.call('ritual_ZNK22QQmlGuardedContextData4nextEv')
    return QQmlGuardedContextData._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGuardedContextData::QQmlGuardedContextData()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlguardedcontextdata.html#QQmlGuardedContextData
    """
    #  QQmlGuardedContextData::QQmlGuardedContextData()
    self._noteCreation(QQmlGuardedContextData, lambda: Rituals.call(
        'ritual_ZN22QQmlGuardedContextDataC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QQmlGuardedContextData::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardedcontextdata.html#reset
    """
    #  void QQmlGuardedContextData::reset()
    self.uglySide.call('ritual_ZN22QQmlGuardedContextData5resetEv')

  def unlink(self) -> None:
    """
    Calls Qt's 'void QQmlGuardedContextData::unlink()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardedcontextdata.html#unlink
    """
    #  void QQmlGuardedContextData::unlink()
    self.uglySide.call('ritual_ZN22QQmlGuardedContextData6unlinkEv')

  @staticmethod
  def contextData(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlGuardedContextData::contextData() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlGuardedContextData.contextData' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlGuardedContextData::contextData() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setContextData(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlGuardedContextData::setContextData(QQmlRefPointer<QQmlContextData>
    contextData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlGuardedContextData.setContextData' has no cute function yet. "
        "Qt's 'void "
        "QQmlGuardedContextData::setContextData(QQmlRefPointer<QQmlContextDa"
        "ta> contextData)': takes a type Python has no way to hand over yet."
    )
