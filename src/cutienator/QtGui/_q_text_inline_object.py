"""
QTextInlineObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import QTextEngine, QTextFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextEngine = WAIT['QTextEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextInlineObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextInlineObject: a plain Python object standing in
  front of one C++ QTextInlineObject.

  C++ hands a QTextInlineObject around as a copy, so every C++
  QTextInlineObject behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextInlineObject that has a ritual and that Python
  can call so far, 13 names in all: 'isValid', 'rect', 'width', 'ascent',
  'descent', 'height', 'textDirection', 'setWidth', 'setAscent',
  'setDescent', 'textPosition', 'formatIndex', 'format'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextInlineObject::~QTextInlineObject()': the destructor: Python
    removes its C++ QTextInlineObject by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextInlineObject is created at the first use, not by
    'QTextInlineObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextInlineObject back gives a copy the ritual made
    for Python, in a new cute QTextInlineObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextInlineObject'

  #  Qt's '~QTextInlineObject()'. Naming it makes this a value class: Python
  #  owns every C++ QTextInlineObject behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QTextInlineObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextInlineObject::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#isValid
    """
    #  bool QTextInlineObject::isValid() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject7isValidEv')

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QTextInlineObject::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextInlineObject::rect() const
    address = self.uglySide.call('ritual_ZNK17QTextInlineObject4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QTextInlineObject::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#width
    """
    #  qreal QTextInlineObject::width() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject5widthEv')

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QTextInlineObject::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#ascent
    """
    #  qreal QTextInlineObject::ascent() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject6ascentEv')

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QTextInlineObject::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#descent
    """
    #  qreal QTextInlineObject::descent() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject7descentEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QTextInlineObject::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#height
    """
    #  qreal QTextInlineObject::height() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject6heightEv')

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QTextInlineObject::textDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextinlineobject.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QTextInlineObject::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK17QTextInlineObject13textDirectionEv',
    ))

  def textPosition(self) -> int:
    """
    Calls Qt's 'int QTextInlineObject::textPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextinlineobject.html#textPosition
    """
    #  int QTextInlineObject::textPosition() const
    return self.uglySide.call(
        'ritual_ZNK17QTextInlineObject12textPositionEv',
    )

  def formatIndex(self) -> int:
    """
    Calls Qt's 'int QTextInlineObject::formatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#formatIndex
    """
    #  int QTextInlineObject::formatIndex() const
    return self.uglySide.call('ritual_ZNK17QTextInlineObject11formatIndexEv')

  def format(self) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QTextInlineObject::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#format

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QTextInlineObject::format() const
    address = self.uglySide.call('ritual_ZNK17QTextInlineObject6formatEv')
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QTextInlineObject::setWidth(qreal w)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#setWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QTextInlineObject::setWidth(qreal w)
    self.uglySide.call('ritual_ZN17QTextInlineObject8setWidthEd', w)

  @overload(float)
  def setAscent(self, a: float) -> None:
    """
    Calls Qt's 'void QTextInlineObject::setAscent(qreal a)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#setAscent

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QTextInlineObject::setAscent(qreal a)
    self.uglySide.call('ritual_ZN17QTextInlineObject9setAscentEd', a)

  @overload(float)
  def setDescent(self, d: float) -> None:
    """
    Calls Qt's 'void QTextInlineObject::setDescent(qreal d)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextinlineobject.html#setDescent

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  void QTextInlineObject::setDescent(qreal d)
    self.uglySide.call('ritual_ZN17QTextInlineObject10setDescentEd', d)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QTextEngine)
  @overload(int, NoneType)
  def __init__(self, i: int, e: Optional[QTextEngine]) -> None:
    """
    Notes what was given, for Qt's 'QTextInlineObject::QTextInlineObject(int
    i, QTextEngine *e)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextinlineobject.html#QTextInlineObject

    Parameters
    ----------

    i : int
      Passed on as it is.

    e : Optional[QTextEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextInlineObject::QTextInlineObject(int i, QTextEngine *e)
    self._noteCreation(QTextInlineObject, lambda: Rituals.call(
        'ritual_ZN17QTextInlineObjectC1EiP11QTextEngine',
        i, self._addressOf(e),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextInlineObject::QTextInlineObject()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextinlineobject.html#QTextInlineObject
    """
    #  QTextInlineObject::QTextInlineObject()
    self._noteCreation(QTextInlineObject, lambda: Rituals.call(
        'ritual_ZN17QTextInlineObjectC1Ev',
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
