"""
QTextItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from . import QTextItemRenderFlag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFont


class QTextItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextItem: a plain Python object standing in front of
  one C++ QTextItem.

  C++ hands a QTextItem around as a copy, so every C++ QTextItem behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextItem that has a ritual and that Python can call
  so far, 6 names in all: 'descent', 'ascent', 'width', 'renderFlags',
  'text', 'font'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextItem::~QTextItem()': the destructor: Python removes its C++
    QTextItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextItem is created at the first use, not by 'QTextItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextItem back gives a copy the ritual made for
    Python, in a new cute QTextItem.
  """

  #  The enums Qt writes inside QTextItem, and the names Qt has for the
  #  combinations of its flags enums.
  RenderFlag = QTextItemRenderFlag
  RenderFlags = QTextItemRenderFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextItem'

  #  Qt's '~QTextItem()'. Naming it makes this a value class: Python owns
  #  every C++ QTextItem behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QTextItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QTextItem::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#descent
    """
    #  qreal QTextItem::descent() const
    return self.uglySide.call('ritual_ZNK9QTextItem7descentEv')

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QTextItem::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#ascent
    """
    #  qreal QTextItem::ascent() const
    return self.uglySide.call('ritual_ZNK9QTextItem6ascentEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QTextItem::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#width
    """
    #  qreal QTextItem::width() const
    return self.uglySide.call('ritual_ZNK9QTextItem5widthEv')

  def renderFlags(self) -> RenderFlags:
    """
    Calls Qt's 'RenderFlags QTextItem::renderFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#renderFlags

    Returns
    -------

    RenderFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderFlags QTextItem::renderFlags() const
    return QTextItem.RenderFlags(self.uglySide.call(
        'ritual_ZNK9QTextItem11renderFlagsEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QTextItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextItem::text() const
    return self.uglySide.call('ritual_ZNK9QTextItem4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QTextItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextItem::font() const
    address = self.uglySide.call('ritual_ZNK9QTextItem4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

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
