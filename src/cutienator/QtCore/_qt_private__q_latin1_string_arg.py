"""
QtPrivate::QLatin1StringArg binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class QLatin1StringArg(QtPrivate.ArgBase):
  """
  The cute side of Qt's QtPrivate::QLatin1StringArg: a plain Python object
  standing in front of one C++ QtPrivate::QLatin1StringArg.

  It is built on the cute 'QtPrivate::ArgBase', as Qt's
  QtPrivate::QLatin1StringArg is built on Qt's QtPrivate::ArgBase, and has
  everything that class has.

  C++ hands a QtPrivate::QLatin1StringArg around as a copy, so every C++
  QtPrivate::QLatin1StringArg behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QtPrivate::QLatin1StringArg yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::QLatin1StringArg::~QLatin1StringArg()': the destructor:
    Python removes its C++ QtPrivate::QLatin1StringArg by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QLatin1StringArg is created at the first use, not by
    'QtPrivate::QLatin1StringArg(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QLatin1StringArg back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QLatin1StringArg.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QLatin1StringArg'

  #  Qt's '~QtPrivate::QLatin1StringArg()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::QLatin1StringArg behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate16QLatin1StringArgD1Ev'

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
    'QtPrivate::QLatin1StringArg::QLatin1StringArg()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qlatin1stringarg.html#QLatin1StringArg
    """
    #  QtPrivate::QLatin1StringArg::QLatin1StringArg()
    self._noteCreation(QLatin1StringArg, lambda: Rituals.call(
        'ritual_ZN9QtPrivate16QLatin1StringArgC1Ev',
    ))

  @overload(QLatin1String)
  def __init__(self, v: QLatin1String) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QLatin1StringArg::QLatin1StringArg(QLatin1StringView v)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qlatin1stringarg.html#QLatin1StringArg

    Parameters
    ----------

    v : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QtPrivate::QLatin1StringArg::QLatin1StringArg(QLatin1StringView v)
    self._noteCreation(QLatin1StringArg, lambda: Rituals.call(
        'ritual_ZN9QtPrivate16QLatin1StringArgC1E13QLatin1String',
        self._valueOf(v),
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
