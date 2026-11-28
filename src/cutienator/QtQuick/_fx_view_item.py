"""
FxViewItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means FxViewItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickItemViewFxItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickItem, QQuickItemView, QQuickItemViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickItemView = WAIT['QQuickItemView']
  QQuickItemViewAttached = WAIT['QQuickItemViewAttached']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FxViewItem(QQuickItemViewFxItem):
  """
  The cute side of Qt's FxViewItem: a plain Python object standing in front
  of one C++ FxViewItem.

  It is built on the cute 'QQuickItemViewFxItem', as Qt's FxViewItem is built
  on Qt's QQuickItemViewFxItem, and has everything that class has.

  What exists
  -----------

  No function of Qt's FxViewItem yet. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ FxViewItem is created at the first use, not by 'FxViewItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FxViewItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FxViewItem'

  #  A C++ FxViewItem Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_FxViewItem'

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

  @overload(QQuickItem, QQuickItemView, bool, QQuickItemViewAttached)
  @overload(QQuickItem, QQuickItemView, bool, NoneType)
  @overload(QQuickItem, NoneType, bool, QQuickItemViewAttached)
  @overload(QQuickItem, NoneType, bool, NoneType)
  @overload(NoneType, QQuickItemView, bool, QQuickItemViewAttached)
  @overload(NoneType, QQuickItemView, bool, NoneType)
  @overload(NoneType, NoneType, bool, QQuickItemViewAttached)
  @overload(NoneType, NoneType, bool, NoneType)
  def __init__(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItemView],
      own: bool,
      attached: Optional[QQuickItemViewAttached],
  ) -> None:
    """
    Notes what was given, for Qt's 'FxViewItem::FxViewItem(QQuickItem *a0,
    QQuickItemView *a1, bool own, QQuickItemViewAttached *attached)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/fxviewitem.html#FxViewItem

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    own : bool
      Passed on as it is.

    attached : Optional[QQuickItemViewAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  FxViewItem::FxViewItem(QQuickItem *a0, QQuickItemView *a1, bool own,
    #      QQuickItemViewAttached *attached)
    self._noteCreation(FxViewItem, lambda: Rituals.call(
        'ritual_ZN10FxViewItemC1EP10QQuickItemP14QQuickItemViewbP22QQuickIt'
        'emViewAttached',
        self._addressOf(a0), self._addressOf(a1), own,
        self._addressOf(attached),
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
