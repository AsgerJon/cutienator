"""
QtPrivate::QStringViewArg binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QtPrivate


class QStringViewArg(QtPrivate.ArgBase):
  """
  The cute side of Qt's QtPrivate::QStringViewArg: a plain Python object
  standing in front of one C++ QtPrivate::QStringViewArg.

  It is built on the cute 'QtPrivate::ArgBase', as Qt's
  QtPrivate::QStringViewArg is built on Qt's QtPrivate::ArgBase, and has
  everything that class has.

  C++ hands a QtPrivate::QStringViewArg around as a copy, so every C++
  QtPrivate::QStringViewArg behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtPrivate::QStringViewArg yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::QStringViewArg::~QStringViewArg()': the destructor:
    Python removes its C++ QtPrivate::QStringViewArg by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QStringViewArg is created at the first use, not by
    'QtPrivate::QStringViewArg(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QStringViewArg back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QStringViewArg.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QStringViewArg'

  #  Qt's '~QtPrivate::QStringViewArg()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::QStringViewArg behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate14QStringViewArgD1Ev'

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
    'QtPrivate::QStringViewArg::QStringViewArg()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qstringviewarg.html#QStringViewArg
    """
    #  QtPrivate::QStringViewArg::QStringViewArg()
    self._noteCreation(QStringViewArg, lambda: Rituals.call(
        'ritual_ZN9QtPrivate14QStringViewArgC1Ev',
    ))

  @overload(str)
  def __init__(self, v: str) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QStringViewArg::QStringViewArg(QStringView v)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qstringviewarg.html#QStringViewArg

    Parameters
    ----------

    v : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QtPrivate::QStringViewArg::QStringViewArg(QStringView v)
    self._noteCreation(QStringViewArg, lambda: Rituals.call(
        'ritual_ZN9QtPrivate14QStringViewArgC1E11QStringView', v,
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
