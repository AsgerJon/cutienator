"""
QGraphicsTransformPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicstransform_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsTransformPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGraphicsItem, QGraphicsTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsTransformPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsTransformPrivate: a plain Python object
  standing in front of one C++ QGraphicsTransformPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGraphicsTransformPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsTransformPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'setItem', 'updateItem'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsTransform *QGraphicsTransformPrivate::q_func()
    const': takes in Python what 'QGraphicsTransform
    *QGraphicsTransformPrivate::q_func()' takes.
  - Qt's 'QGraphicsTransformPrivate::~QGraphicsTransformPrivate()': the
    destructor: Python never removes a C++ QGraphicsTransformPrivate.

  What to expect
  --------------

  - The C++ QGraphicsTransformPrivate is created at the first use, not by
    'QGraphicsTransformPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsTransformPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsItem)
  @overload(NoneType)
  def updateItem(item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsTransformPrivate::updateItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstransformprivate.html#updateItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTransformPrivate::updateItem(QGraphicsItem *item)
    Rituals.call(
        'ritual_ZN25QGraphicsTransformPrivate10updateItemEP13QGraphicsItem',
        CuteMixin._addressOf(item, 'QGraphicsItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsTransformPrivate'

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

  @overload(QGraphicsItem)
  @overload(NoneType)
  def setItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsTransformPrivate::setItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstransformprivate.html#setItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTransformPrivate::setItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN25QGraphicsTransformPrivate7setItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
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
    'QGraphicsTransformPrivate::QGraphicsTransformPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstransformprivate.html
    """
    #  QGraphicsTransformPrivate::QGraphicsTransformPrivate()
    self._noteCreation(QGraphicsTransformPrivate, lambda: Rituals.call(
        'ritual_ZN25QGraphicsTransformPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsTransform]:
    """
    Calls Qt's 'QGraphicsTransform *QGraphicsTransformPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstransformprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsTransform *QGraphicsTransformPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QGraphicsTransformPrivate6q_funcEv',
    )
    from . import QGraphicsTransform
    return QGraphicsTransform._cuteAt(address)
