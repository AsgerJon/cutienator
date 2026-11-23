"""
QOperatingSystemVersionUnexported binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QOperatingSystemVersionBase


class QOperatingSystemVersionUnexported(QOperatingSystemVersionBase):
  """
  The cute side of Qt's QOperatingSystemVersionUnexported: a plain Python
  object standing in front of one C++ QOperatingSystemVersionUnexported.

  It is built on the cute 'QOperatingSystemVersionBase', as Qt's
  QOperatingSystemVersionUnexported is built on Qt's
  QOperatingSystemVersionBase, and has everything that class has.

  C++ hands a QOperatingSystemVersionUnexported around as a copy, so every
  C++ QOperatingSystemVersionUnexported behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QOperatingSystemVersionUnexported yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOperatingSystemVersionUnexported::~QOperatingSystemVersionUnexported(
    )': the destructor: Python removes its C++
    QOperatingSystemVersionUnexported by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOperatingSystemVersionUnexported is created at the first use,
    not by 'QOperatingSystemVersionUnexported(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOperatingSystemVersionUnexported back gives a copy
    the ritual made for Python, in a new cute
    QOperatingSystemVersionUnexported.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOperatingSystemVersionUnexported'

  #  Qt's '~QOperatingSystemVersionUnexported()'. Naming it makes this a
  #  value class: Python owns every C++ QOperatingSystemVersionUnexported
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QOperatingSystemVersionUnexportedD1Ev'

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

  @overload(QOperatingSystemVersionBase)
  def __init__(self, other: QOperatingSystemVersionBase) -> None:
    """
    Notes what was given, for Qt's
    'QOperatingSystemVersionUnexported::QOperatingSystemVersionUnexported(
    QOperatingSystemVersionBase other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionunexported.html

    Parameters
    ----------

    other : QOperatingSystemVersionBase
      Passed on as a value: Qt reads the C++ QOperatingSystemVersionBase,
      which stays Python's own.
    """
    #  QOperatingSystemVersionUnexported::
    #      QOperatingSystemVersionUnexported(QOperatingSystemVersionBase
    #      other)
    self._noteCreation(
        QOperatingSystemVersionUnexported, lambda: Rituals.call(
            'ritual_ZN33QOperatingSystemVersionUnexportedC1E27QOperatingSys'
            'temVersionBase',
            self._valueOf(other),
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
