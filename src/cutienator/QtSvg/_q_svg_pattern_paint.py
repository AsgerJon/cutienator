"""
QSvgPatternPaint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgPatternPaint to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgPaintServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSvgPattern
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgPattern = WAIT['QSvgPattern']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgPatternPaint(QSvgPaintServer):
  """
  The cute side of Qt's QSvgPatternPaint: a plain Python object standing in
  front of one C++ QSvgPatternPaint.

  It is built on the cute 'QSvgPaintServer', as Qt's QSvgPatternPaint is
  built on Qt's QSvgPaintServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgPatternPaint that has a ritual and that Python
  can call so far, 2 names in all: 'type', 'patternNode'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgPatternPaint::~QSvgPatternPaint()': the destructor: Python
    never removes a C++ QSvgPatternPaint.
  - Qt's 'QBrush QSvgPatternPaint::brush(QPainter *a0, const QSvgNode *a1,
    QSvgExtraStates &a2)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgPatternPaint is created at the first use, not by
    'QSvgPatternPaint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgPatternPaint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgPatternPaint'

  #  A C++ QSvgPatternPaint Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgPatternPaint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgPaintServer.Type:
    """
    Calls Qt's 'Type QSvgPatternPaint::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpatternpaint.html#type

    Returns
    -------

    QSvgPaintServer.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgPaintServer.Type(number)' gives.
    """
    #  Type QSvgPatternPaint::type() const
    ritual = 'ritual_ZNK16QSvgPatternPaint4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSvgPatternPaint4typeEv'
    return QSvgPaintServer.Type(self.uglySide.call(ritual))

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

  @overload(QSvgPattern)
  @overload(NoneType)
  def __init__(self, pattern: Optional[QSvgPattern]) -> None:
    """
    Notes what was given, for Qt's
    'QSvgPatternPaint::QSvgPatternPaint(QSvgPattern *pattern)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgpatternpaint.html#QSvgPatternPaint

    Parameters
    ----------

    pattern : Optional[QSvgPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSvgPatternPaint::QSvgPatternPaint(QSvgPattern *pattern)
    self._noteCreation(QSvgPatternPaint, lambda: Rituals.call(
        'ritual_ZN16QSvgPatternPaintC1EP11QSvgPattern',
        self._addressOf(pattern),
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

  def patternNode(self) -> Optional[QSvgPattern]:
    """
    Calls Qt's 'QSvgPattern *QSvgPatternPaint::patternNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpatternpaint.html#patternNode

    Returns
    -------

    Optional[QSvgPattern]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgPattern *QSvgPatternPaint::patternNode()
    address = self.uglySide.call(
        'ritual_ZN16QSvgPatternPaint11patternNodeEv',
    )
    from . import QSvgPattern
    return QSvgPattern._cuteAt(address)
