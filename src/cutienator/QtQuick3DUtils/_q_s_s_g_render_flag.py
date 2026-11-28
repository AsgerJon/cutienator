"""
QSSGRenderFlag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGRenderFlag to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGRenderFlag(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderFlag: a plain Python object standing in
  front of one C++ QSSGRenderFlag.

  C++ hands a QSSGRenderFlag around as a copy, so every C++ QSSGRenderFlag
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderFlag that has a ritual and that Python can
  call so far, 7 names in all: 'value', 'setValue', 'clearFlags', 'setFlag',
  'isSet', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'quint32 QSSGRenderFlag::operator unsigned int() const': an operator
    Python has no name for.
  - Qt's 'QSSGRenderFlag::~QSSGRenderFlag()': the destructor: Python removes
    its C++ QSSGRenderFlag by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderFlag is created at the first use, not by
    'QSSGRenderFlag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderFlag back gives a copy the ritual made for
    Python, in a new cute QSSGRenderFlag.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderFlag'

  #  Qt's '~QSSGRenderFlag()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGRenderFlag behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSSGRenderFlagD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderFlag::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#value
    """
    #  quint32 QSSGRenderFlag::value() const
    return self.uglySide.call('ritual_ZNK14QSSGRenderFlag5valueEv')

  @overload(int)
  def isSet(self, v: int) -> bool:
    """
    Calls Qt's 'bool QSSGRenderFlag::isSet(quint32 v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#isSet

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  bool QSSGRenderFlag::isSet(quint32 v) const
    return self.uglySide.call('ritual_ZNK14QSSGRenderFlag5isSetEj', v)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setValue(self, v: int) -> None:
    """
    Calls Qt's 'void QSSGRenderFlag::setValue(quint32 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#setValue

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  void QSSGRenderFlag::setValue(quint32 v)
    self.uglySide.call('ritual_ZN14QSSGRenderFlag8setValueEj', v)

  @overload(int)
  @overload(int, bool)
  def setFlag(self, v: int, on: bool = True) -> None:
    """
    Calls Qt's 'void QSSGRenderFlag::setFlag(quint32 v, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#setFlag

    Parameters
    ----------

    v : int
      Passed on as it is.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSSGRenderFlag::setFlag(quint32 v, bool on)
    self.uglySide.call('ritual_ZN14QSSGRenderFlag7setFlagEjb', v, on)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QSSGRenderFlag) -> bool:
    """
    Calls Qt's 'bool operator==(const QSSGRenderFlag &a, const QSSGRenderFlag
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#operator==

    Parameters
    ----------

    b : QSSGRenderFlag
      Passed on as a value: Qt reads the C++ QSSGRenderFlag, which stays
      Python's own.
    """
    #  bool operator==(const QSSGRenderFlag &a, const QSSGRenderFlag &b)
    return Rituals.call(
        'ritual_ZeqRK14QSSGRenderFlagS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QSSGRenderFlag) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSSGRenderFlag &a, const QSSGRenderFlag
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#operator!=

    Parameters
    ----------

    b : QSSGRenderFlag
      Passed on as a value: Qt reads the C++ QSSGRenderFlag, which stays
      Python's own.
    """
    #  bool operator!=(const QSSGRenderFlag &a, const QSSGRenderFlag &b)
    return Rituals.call(
        'ritual_ZneRK14QSSGRenderFlagS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    Notes what was given, for Qt's 'QSSGRenderFlag::QSSGRenderFlag()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#QSSGRenderFlag
    """
    #  QSSGRenderFlag::QSSGRenderFlag()
    self._noteCreation(QSSGRenderFlag, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderFlagC1Ev',
    ))

  @overload(int)
  def __init__(self, v: int) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderFlag::QSSGRenderFlag(quint32
    v)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#QSSGRenderFlag

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  QSSGRenderFlag::QSSGRenderFlag(quint32 v)
    self._noteCreation(QSSGRenderFlag, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderFlagC1Ej', v,
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

  @overload()
  @overload(int)
  def clearFlags(self, v: int = 4294967295) -> None:
    """
    Calls Qt's 'void QSSGRenderFlag::clearFlags(quint32 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderflag.html#clearFlags

    Parameters
    ----------

    v : int
      Passed on as it is. May be left out, as in Qt: it is then 4294967295.
    """
    #  void QSSGRenderFlag::clearFlags(quint32 v)
    self.uglySide.call('ritual_ZN14QSSGRenderFlag10clearFlagsEj', v)
