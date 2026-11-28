"""
QQmlGuardImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlguard_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlGuardImpl to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGuardImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlGuardImpl: a plain Python object standing in
  front of one C++ QQmlGuardImpl.

  What exists
  -----------

  Every function of Qt's QQmlGuardImpl that has a ritual and that Python can
  call so far, 4 names in all: 'addGuard', 'remGuard', 'setObject', 'isNull'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlGuardImpl::QQmlGuardImpl(const QQmlGuardImpl &a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlGuardImpl::~QQmlGuardImpl()': the destructor: Python never
    removes a C++ QQmlGuardImpl.

  What to expect
  --------------

  - The C++ QQmlGuardImpl is created at the first use, not by
    'QQmlGuardImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGuardImpl.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGuardImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlGuardImpl::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#isNull
    """
    #  bool QQmlGuardImpl::isNull() const
    return self.uglySide.call('ritual_ZNK13QQmlGuardImpl6isNullEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, g: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlGuardImpl::setObject(QObject *g)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#setObject

    Parameters
    ----------

    g : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlGuardImpl::setObject(QObject *g)
    self.uglySide.call(
        'ritual_ZN13QQmlGuardImpl9setObjectEP7QObject',
        self._addressOf(g, 'QObject'),
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
    Notes what was given, for Qt's 'QQmlGuardImpl::QQmlGuardImpl()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#QQmlGuardImpl
    """
    #  QQmlGuardImpl::QQmlGuardImpl()
    self._noteCreation(QQmlGuardImpl, lambda: Rituals.call(
        'ritual_ZN13QQmlGuardImplC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, a0: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QQmlGuardImpl::QQmlGuardImpl(QObject
    *a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#QQmlGuardImpl

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlGuardImpl::QQmlGuardImpl(QObject *a0)
    self._noteCreation(QQmlGuardImpl, lambda: Rituals.call(
        'ritual_ZN13QQmlGuardImplC1EP7QObject',
        self._addressOf(a0, 'QObject'),
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

  def addGuard(self) -> None:
    """
    Calls Qt's 'void QQmlGuardImpl::addGuard()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#addGuard
    """
    #  void QQmlGuardImpl::addGuard()
    self.uglySide.call('ritual_ZN13QQmlGuardImpl8addGuardEv')

  def remGuard(self) -> None:
    """
    Calls Qt's 'void QQmlGuardImpl::remGuard()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguardimpl.html#remGuard
    """
    #  void QQmlGuardImpl::remGuard()
    self.uglySide.call('ritual_ZN13QQmlGuardImpl8remGuardEv')
