"""
QProxyStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qproxystyle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QProxyStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCommonStylePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QProxyStyle


class QProxyStylePrivate(QCommonStylePrivate):
  """
  The cute side of Qt's QProxyStylePrivate: a plain Python object standing in
  front of one C++ QProxyStylePrivate.

  It is built on the cute 'QCommonStylePrivate', as Qt's QProxyStylePrivate
  is built on Qt's QCommonStylePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProxyStylePrivate that has a ritual and that Python
  can call so far, 2 names in all: 'q_func', 'ensureBaseStyle'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QProxyStyle *QProxyStylePrivate::q_func() const': takes in
    Python what 'QProxyStyle *QProxyStylePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QProxyStylePrivate is created at the first use, not by
    'QProxyStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProxyStylePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProxyStylePrivate'

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
    Notes what was given, for Qt's
    'QProxyStylePrivate::QProxyStylePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxystyleprivate.html#QProxyStylePrivate
    """
    #  QProxyStylePrivate::QProxyStylePrivate()
    self._noteCreation(QProxyStylePrivate, lambda: Rituals.call(
        'ritual_ZN18QProxyStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QProxyStyle]:
    """
    Calls Qt's 'QProxyStyle *QProxyStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyleprivate.html#q_func

    Returns
    -------

    Optional[QProxyStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProxyStyle *QProxyStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QProxyStylePrivate6q_funcEv')
    from . import QProxyStyle
    return QProxyStyle._cuteAt(address)

  def ensureBaseStyle(self) -> None:
    """
    Calls Qt's 'void QProxyStylePrivate::ensureBaseStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxystyleprivate.html#ensureBaseStyle
    """
    #  void QProxyStylePrivate::ensureBaseStyle() const
    self.uglySide.call('ritual_ZNK18QProxyStylePrivate15ensureBaseStyleEv')
