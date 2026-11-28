"""
QQuickAnchorLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnchorLine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickAnchors

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchorLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAnchorLine: a plain Python object standing in
  front of one C++ QQuickAnchorLine.

  C++ hands a QQuickAnchorLine around as a copy, so every C++
  QQuickAnchorLine behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuickAnchorLine yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickAnchorLine::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickAnchorLine::~QQuickAnchorLine()': the destructor: Python
    removes its C++ QQuickAnchorLine by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnchorLine is created at the first use, not by
    'QQuickAnchorLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickAnchorLine back gives a copy the ritual made
    for Python, in a new cute QQuickAnchorLine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchorLine'

  #  Qt's '~QQuickAnchorLine()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickAnchorLine behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQuickAnchorLineD1Ev'

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
    Notes what was given, for Qt's 'QQuickAnchorLine::QQuickAnchorLine()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorline.html#QQuickAnchorLine
    """
    #  QQuickAnchorLine::QQuickAnchorLine()
    self._noteCreation(QQuickAnchorLine, lambda: Rituals.call(
        'ritual_ZN16QQuickAnchorLineC1Ev',
    ))

  @overload(QQuickItem, QQuickAnchors.Anchor)
  @overload(NoneType, QQuickAnchors.Anchor)
  def __init__(
      self,
      i: Optional[QQuickItem],
      l: QQuickAnchors.Anchor,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnchorLine::QQuickAnchorLine(QQuickItem *i, QQuickAnchors::Anchor
    l)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorline.html#QQuickAnchorLine

    Parameters
    ----------

    i : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    l : QQuickAnchors.Anchor
      Passed on as its number.
    """
    #  QQuickAnchorLine::QQuickAnchorLine(QQuickItem *i,
    #      QQuickAnchors::Anchor l)
    self._noteCreation(QQuickAnchorLine, lambda: Rituals.call(
        'ritual_ZN16QQuickAnchorLineC1EP10QQuickItemN13QQuickAnchors6Anchor'
        'E',
        self._addressOf(i), l.value,
    ))

  @overload(QQuickItem, int)
  @overload(NoneType, int)
  def __init__(self, i: Optional[QQuickItem], l: int) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnchorLine::QQuickAnchorLine(QQuickItem *i, uint l)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorline.html#QQuickAnchorLine

    Parameters
    ----------

    i : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    l : int
      Passed on as it is.
    """
    #  QQuickAnchorLine::QQuickAnchorLine(QQuickItem *i, uint l)
    self._noteCreation(QQuickAnchorLine, lambda: Rituals.call(
        'ritual_ZN16QQuickAnchorLineC1EP10QQuickItemj',
        self._addressOf(i), l,
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
