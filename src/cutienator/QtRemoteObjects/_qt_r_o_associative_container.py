"""
QtROAssociativeContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtROAssociativeContainer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QtMetaContainerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QtROAssociativeContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtROAssociativeContainer: a plain Python object
  standing in front of one C++ QtROAssociativeContainer.

  C++ hands a QtROAssociativeContainer around as a copy, so every C++
  QtROAssociativeContainer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtROAssociativeContainer that has a ritual and that
  Python can call so far, 1 name in all: 'setTypes'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtROAssociativeContainer::~QtROAssociativeContainer()': the
    destructor: Python removes its C++ QtROAssociativeContainer by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QtROAssociativeContainer is created at the first use, not by
    'QtROAssociativeContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtROAssociativeContainer back gives a copy the ritual
    made for Python, in a new cute QtROAssociativeContainer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROAssociativeContainer'

  #  Qt's '~QtROAssociativeContainer()'. Naming it makes this a value class:
  #  Python owns every C++ QtROAssociativeContainer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QtROAssociativeContainerD1Ev'

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

  @overload(QByteArray, QByteArray)
  def setTypes(
      self,
      keyTypeName: QByteArray,
      valueTypeName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QtROAssociativeContainer::setTypes(const QByteArray
    &keyTypeName, const QByteArray &valueTypeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroassociativecontainer.html#setTypes

    Parameters
    ----------

    keyTypeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    valueTypeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtROAssociativeContainer::setTypes(const QByteArray &keyTypeName,
    #      const QByteArray &valueTypeName)
    self.uglySide.call(
        'ritual_ZN24QtROAssociativeContainer8setTypesERK10QByteArrayS2_',
        self._valueOf(keyTypeName), self._valueOf(valueTypeName),
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
    Notes what was given, for Qt's
    'QtROAssociativeContainer::QtROAssociativeContainer()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroassociativecontainer.html
    """
    #  QtROAssociativeContainer::QtROAssociativeContainer()
    self._noteCreation(QtROAssociativeContainer, lambda: Rituals.call(
        'ritual_ZN24QtROAssociativeContainerC1Ev',
    ))

  @overload(WAIT['QtMetaContainerPrivate.Association'])
  def __init__(self, map: QtMetaContainerPrivate.Association) -> None:
    """
    Notes what was given, for Qt's
    'QtROAssociativeContainer::QtROAssociativeContainer(const
    QMetaAssociation::Iterable &map)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroassociativecontainer.html

    Parameters
    ----------

    map : QtMetaContainerPrivate.Association
      Passed on as a value: Qt reads the C++
      QtMetaContainerPrivate::Association, which stays Python's own.
    """
    #  QtROAssociativeContainer::QtROAssociativeContainer(const
    #      QMetaAssociation::Iterable &map)
    self._noteCreation(QtROAssociativeContainer, lambda: Rituals.call(
        'ritual_ZN24QtROAssociativeContainerC1ERKN22QtMetaContainerPrivate1'
        '1AssociationE',
        self._valueOf(map),
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
