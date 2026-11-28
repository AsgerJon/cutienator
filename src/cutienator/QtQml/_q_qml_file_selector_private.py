"""
QQmlFileSelectorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlfileselector_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlFileSelectorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlFileSelector


class QQmlFileSelectorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQmlFileSelectorPrivate: a plain Python object
  standing in front of one C++ QQmlFileSelectorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlFileSelectorPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlFileSelectorPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'deleteSelectorIfOwned'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlFileSelector *QQmlFileSelectorPrivate::q_func() const':
    takes in Python what 'QQmlFileSelector
    *QQmlFileSelectorPrivate::q_func()' takes.
  - Qt's 'QQmlFileSelectorPrivate::~QQmlFileSelectorPrivate()': the
    destructor: Python never removes a C++ QQmlFileSelectorPrivate.

  What to expect
  --------------

  - The C++ QQmlFileSelectorPrivate is created at the first use, not by
    'QQmlFileSelectorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFileSelectorPrivate.
  """

  #  The enums Qt writes inside QQmlFileSelectorPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Owned(CuteNum, scoped=True):
    """
    The enum 'QQmlFileSelectorPrivate::Owned' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFileSelectorPrivate'

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
    'QQmlFileSelectorPrivate::QQmlFileSelectorPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselectorprivate.html
    """
    #  QQmlFileSelectorPrivate::QQmlFileSelectorPrivate()
    self._noteCreation(QQmlFileSelectorPrivate, lambda: Rituals.call(
        'ritual_ZN23QQmlFileSelectorPrivateC1Ev',
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

  def q_func(self) -> Optional[QQmlFileSelector]:
    """
    Calls Qt's 'QQmlFileSelector *QQmlFileSelectorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselectorprivate.html#q_func

    Returns
    -------

    Optional[QQmlFileSelector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFileSelector *QQmlFileSelectorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QQmlFileSelectorPrivate6q_funcEv',
    )
    from . import QQmlFileSelector
    return QQmlFileSelector._cuteAt(address)

  def deleteSelectorIfOwned(self) -> None:
    """
    Calls Qt's 'void QQmlFileSelectorPrivate::deleteSelectorIfOwned()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselectorprivate.html#deleteSelectorIfOwned
    """
    #  void QQmlFileSelectorPrivate::deleteSelectorIfOwned()
    self.uglySide.call(
        'ritual_ZN23QQmlFileSelectorPrivate21deleteSelectorIfOwnedEv',
    )
