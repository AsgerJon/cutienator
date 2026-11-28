"""
QEventLoopPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventloop_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QEventLoopPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEventLoop


class QEventLoopPrivate(QObjectPrivate):
  """
  The cute side of Qt's QEventLoopPrivate: a plain Python object standing in
  front of one C++ QEventLoopPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QEventLoopPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEventLoopPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'ref', 'deref'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QEventLoop *QEventLoopPrivate::q_func() const': takes in
    Python what 'QEventLoop *QEventLoopPrivate::q_func()' takes.
  - Qt's 'QEventLoopPrivate::~QEventLoopPrivate()': the destructor: Python
    never removes a C++ QEventLoopPrivate.

  What to expect
  --------------

  - The C++ QEventLoopPrivate is created at the first use, not by
    'QEventLoopPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventLoopPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventLoopPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QEventLoopPrivate::QEventLoopPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventloopprivate.html#QEventLoopPrivate
    """
    #  QEventLoopPrivate::QEventLoopPrivate()
    self._noteCreation(QEventLoopPrivate, lambda: Rituals.call(
        'ritual_ZN17QEventLoopPrivateC1Ev',
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

  def q_func(self) -> Optional[QEventLoop]:
    """
    Calls Qt's 'QEventLoop *QEventLoopPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloopprivate.html#q_func

    Returns
    -------

    Optional[QEventLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventLoop *QEventLoopPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QEventLoopPrivate6q_funcEv')
    from . import QEventLoop
    return QEventLoop._cuteAt(address)

  def ref(self) -> None:
    """
    Calls Qt's 'void QEventLoopPrivate::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloopprivate.html#ref
    """
    #  void QEventLoopPrivate::ref()
    self.uglySide.call('ritual_ZN17QEventLoopPrivate3refEv')

  def deref(self) -> None:
    """
    Calls Qt's 'void QEventLoopPrivate::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloopprivate.html#deref
    """
    #  void QEventLoopPrivate::deref()
    self.uglySide.call('ritual_ZN17QEventLoopPrivate5derefEv')
