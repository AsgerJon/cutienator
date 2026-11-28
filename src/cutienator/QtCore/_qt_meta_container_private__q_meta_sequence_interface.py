"""
QtMetaContainerPrivate::QMetaSequenceInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QtMetaContainerPrivate


class QMetaSequenceInterface(QtMetaContainerPrivate.QMetaContainerInterface):
  """
  The cute side of Qt's QtMetaContainerPrivate::QMetaSequenceInterface: a
  plain Python object standing in front of one C++
  QtMetaContainerPrivate::QMetaSequenceInterface.

  It is built on the cute 'QtMetaContainerPrivate::QMetaContainerInterface',
  as Qt's QtMetaContainerPrivate::QMetaSequenceInterface is built on Qt's
  QtMetaContainerPrivate::QMetaContainerInterface, and has everything that
  class has.

  C++ hands a QtMetaContainerPrivate::QMetaSequenceInterface around as a
  copy, so every C++ QtMetaContainerPrivate::QMetaSequenceInterface behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMetaContainerPrivate::QMetaSequenceInterface yet. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtMetaContainerPrivate::QMetaSequenceInterface::~QMetaSequenceInterface(
    )': the destructor: Python removes its C++
    QtMetaContainerPrivate::QMetaSequenceInterface by it, and has no other
    use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::QMetaSequenceInterface is created at the
    first use, not by 'QtMetaContainerPrivate::QMetaSequenceInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::QMetaSequenceInterface back
    gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::QMetaSequenceInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaContainerPrivate::QMetaSequenceInterface'

  #  Qt's '~QtMetaContainerPrivate::QMetaSequenceInterface()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMetaContainerPrivate::QMetaSequenceInterface behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate22QMetaSequenceInterfaceD1Ev')

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
    'QtMetaContainerPrivate::QMetaSequenceInterface::QMetaSequenceInterface(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-qmetasequenceinterface.html
    """
    #  QtMetaContainerPrivate::QMetaSequenceInterface::
    #      QMetaSequenceInterface()
    self._noteCreation(QMetaSequenceInterface, lambda: Rituals.call(
        'ritual_ZN22QtMetaContainerPrivate22QMetaSequenceInterfaceC1Ev',
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
