"""
QtROSequentialContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtROSequentialContainer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QtROSequentialContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtROSequentialContainer: a plain Python object
  standing in front of one C++ QtROSequentialContainer.

  C++ hands a QtROSequentialContainer around as a copy, so every C++
  QtROSequentialContainer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtROSequentialContainer that has a ritual and that
  Python can call so far, 1 name in all: 'setValueType'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtROSequentialContainer::~QtROSequentialContainer()': the
    destructor: Python removes its C++ QtROSequentialContainer by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QtROSequentialContainer is created at the first use, not by
    'QtROSequentialContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtROSequentialContainer back gives a copy the ritual
    made for Python, in a new cute QtROSequentialContainer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROSequentialContainer'

  #  Qt's '~QtROSequentialContainer()'. Naming it makes this a value class:
  #  Python owns every C++ QtROSequentialContainer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QtROSequentialContainerD1Ev'

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

  @overload(QByteArray)
  def setValueType(self, valueTypeName: QByteArray) -> None:
    """
    Calls Qt's 'void QtROSequentialContainer::setValueType(const QByteArray
    &valueTypeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtrosequentialcontainer.html#setValueType

    Parameters
    ----------

    valueTypeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtROSequentialContainer::setValueType(const QByteArray
    #      &valueTypeName)
    self.uglySide.call(
        'ritual_ZN23QtROSequentialContainer12setValueTypeERK10QByteArray',
        self._valueOf(valueTypeName),
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
    'QtROSequentialContainer::QtROSequentialContainer()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtrosequentialcontainer.html
    """
    #  QtROSequentialContainer::QtROSequentialContainer()
    self._noteCreation(QtROSequentialContainer, lambda: Rituals.call(
        'ritual_ZN23QtROSequentialContainerC1Ev',
    ))

  @overload(WAIT['QtMetaContainerPrivate.Sequence'])
  def __init__(self, lst: QtMetaContainerPrivate.Sequence) -> None:
    """
    Notes what was given, for Qt's
    'QtROSequentialContainer::QtROSequentialContainer(const
    QMetaSequence::Iterable &lst)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtrosequentialcontainer.html

    Parameters
    ----------

    lst : QtMetaContainerPrivate.Sequence
      Passed on as a value: Qt reads the C++
      QtMetaContainerPrivate::Sequence, which stays Python's own.
    """
    #  QtROSequentialContainer::QtROSequentialContainer(const
    #      QMetaSequence::Iterable &lst)
    self._noteCreation(QtROSequentialContainer, lambda: Rituals.call(
        'ritual_ZN23QtROSequentialContainerC1ERKN22QtMetaContainerPrivate8S'
        'equenceE',
        self._valueOf(lst),
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
