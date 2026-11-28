"""
QtMetaContainerPrivate::QMetaAssociationInterface binding of the Qt C++
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


class QMetaAssociationInterface(QtMetaContainerPrivate.QMetaContainerInterface):
  """
  The cute side of Qt's QtMetaContainerPrivate::QMetaAssociationInterface: a
  plain Python object standing in front of one C++
  QtMetaContainerPrivate::QMetaAssociationInterface.

  It is built on the cute 'QtMetaContainerPrivate::QMetaContainerInterface',
  as Qt's QtMetaContainerPrivate::QMetaAssociationInterface is built on Qt's
  QtMetaContainerPrivate::QMetaContainerInterface, and has everything that
  class has.

  C++ hands a QtMetaContainerPrivate::QMetaAssociationInterface around as a
  copy, so every C++ QtMetaContainerPrivate::QMetaAssociationInterface behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMetaContainerPrivate::QMetaAssociationInterface yet.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::QMetaAssociationInterface::
    ~QMetaAssociationInterface()': the destructor: Python removes its C++
    QtMetaContainerPrivate::QMetaAssociationInterface by it, and has no other
    use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::QMetaAssociationInterface is created at
    the first use, not by
    'QtMetaContainerPrivate::QMetaAssociationInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::QMetaAssociationInterface
    back gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::QMetaAssociationInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaContainerPrivate::QMetaAssociationInterface'

  #  Qt's '~QtMetaContainerPrivate::QMetaAssociationInterface()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMetaContainerPrivate::QMetaAssociationInterface behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate25QMetaAssociationInterfaceD1Ev')

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
    'QtMetaContainerPrivate::QMetaAssociationInterface::
    QMetaAssociationInterface()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-qmetaassociationinterface.html
    """
    #  QtMetaContainerPrivate::QMetaAssociationInterface::
    #      QMetaAssociationInterface()
    self._noteCreation(QMetaAssociationInterface, lambda: Rituals.call(
        'ritual_ZN22QtMetaContainerPrivate25QMetaAssociationInterfaceC1Ev',
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
