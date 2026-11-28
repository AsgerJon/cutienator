"""
QtMetaContainerPrivate::QMetaContainerInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QMetaContainerInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::QMetaContainerInterface: a
  plain Python object standing in front of one C++
  QtMetaContainerPrivate::QMetaContainerInterface.

  C++ hands a QtMetaContainerPrivate::QMetaContainerInterface around as a
  copy, so every C++ QtMetaContainerPrivate::QMetaContainerInterface behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMetaContainerPrivate::QMetaContainerInterface yet. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::QMetaContainerInterface::
    ~QMetaContainerInterface()': the destructor: Python removes its C++
    QtMetaContainerPrivate::QMetaContainerInterface by it, and has no other
    use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::QMetaContainerInterface is created at the
    first use, not by 'QtMetaContainerPrivate::QMetaContainerInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::QMetaContainerInterface back
    gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::QMetaContainerInterface.
  """

  #  The enums Qt writes inside
  #  QtMetaContainerPrivate::QMetaContainerInterface, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QtMetaContainerPrivate::QMetaContainerInterface::Position' of
    Qt, with the 3 names Qt gives in it.
    """

    AtBegin = Kee[int](0)
    AtEnd = Kee[int](1)
    Unspecified = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaContainerPrivate::QMetaContainerInterface'

  #  Qt's '~QtMetaContainerPrivate::QMetaContainerInterface()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMetaContainerPrivate::QMetaContainerInterface behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate23QMetaContainerInterfaceD1Ev')

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
    'QtMetaContainerPrivate::QMetaContainerInterface::
    QMetaContainerInterface()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-qmetacontainerinterface.html
    """
    #  QtMetaContainerPrivate::QMetaContainerInterface::
    #      QMetaContainerInterface()
    self._noteCreation(QMetaContainerInterface, lambda: Rituals.call(
        'ritual_ZN22QtMetaContainerPrivate23QMetaContainerInterfaceC1Ev',
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
