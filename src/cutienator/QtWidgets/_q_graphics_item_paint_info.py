"""
QGraphicsItemPaintInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsItemPaintInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGraphicsItemPaintInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsItemPaintInfo: a plain Python object
  standing in front of one C++ QGraphicsItemPaintInfo.

  C++ hands a QGraphicsItemPaintInfo around as a copy, so every C++
  QGraphicsItemPaintInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QGraphicsItemPaintInfo yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsItemPaintInfo::QGraphicsItemPaintInfo(const QTransform
    *const xform1, const QTransform *const xform2, const QTransform *const
    xform3, QRegion *r, QWidget *w, QStyleOptionGraphicsItem *opt, QPainter
    *p, qreal o, bool b1, bool b2)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QGraphicsItemPaintInfo::~QGraphicsItemPaintInfo()': the destructor:
    Python removes its C++ QGraphicsItemPaintInfo by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QGraphicsItemPaintInfo is created at the first use, not by
    'QGraphicsItemPaintInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsItemPaintInfo back gives a copy the ritual
    made for Python, in a new cute QGraphicsItemPaintInfo.
  - Each name of Qt's QGraphicsItemPaintInfo that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItemPaintInfo'

  #  Qt's '~QGraphicsItemPaintInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QGraphicsItemPaintInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QGraphicsItemPaintInfoD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphicsItemPaintInfo::QGraphicsItemPaintInfo(const QTransform
    *const xform1, const QTransform *const xform2, const QTransform *const
    xform3, QRegion *r, QWidget *w, QStyleOptionGraphicsItem *opt, QPainter
    *p, qreal o, bool b1, bool b2)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemPaintInfo.__init__' has no cute function yet. Qt's "
        "'QGraphicsItemPaintInfo::QGraphicsItemPaintInfo(const QTransform "
        "*const xform1, const QTransform *const xform2, const QTransform "
        "*const xform3, QRegion *r, QWidget *w, QStyleOptionGraphicsItem "
        "*opt, QPainter *p, qreal o, bool b1, bool b2)': takes a type "
        "Python has no way to hand over yet.")

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
