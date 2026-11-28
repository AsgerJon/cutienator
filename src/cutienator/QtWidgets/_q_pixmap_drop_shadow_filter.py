"""
QPixmapDropShadowFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapDropShadowFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPixmapFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QColor, QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmapDropShadowFilter(QPixmapFilter):
  """
  The cute side of Qt's QPixmapDropShadowFilter: a plain Python object
  standing in front of one C++ QPixmapDropShadowFilter.

  It is built on the cute 'QPixmapFilter', as Qt's QPixmapDropShadowFilter is
  built on Qt's QPixmapFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapDropShadowFilter that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'boundingRectFor', 'draw', 'blurRadius', 'setBlurRadius', 'color',
  'setColor', 'offset', 'setOffset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPixmapDropShadowFilter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPixmapDropShadowFilter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPixmapDropShadowFilterPrivate *QPixmapDropShadowFilter::d_func()':
    gives 'QPixmapDropShadowFilterPrivate', which has no cute class yet.
  - Qt's 'const QPixmapDropShadowFilterPrivate
    *QPixmapDropShadowFilter::d_func() const': gives
    'QPixmapDropShadowFilterPrivate', which has no cute class yet.
  - Qt's 'QPixmapDropShadowFilter::~QPixmapDropShadowFilter()': the
    destructor: Python never removes a C++ QPixmapDropShadowFilter.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPixmapDropShadowFilter is created at the first use, not by
    'QPixmapDropShadowFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapDropShadowFilter.
  - Qt tells when it has removed the C++ QPixmapDropShadowFilter. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPixmapDropShadowFilter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPixmapDropShadowFilter::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QPixmapDropShadowFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapDropShadowFilter'

  #  A C++ QPixmapDropShadowFilter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapDropShadowFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapDropShadowFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapDropShadowFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPixmapDropShadowFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QPixmapDropShadowFilter::boundingRectFor(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#boundingRectFor

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPixmapDropShadowFilter::boundingRectFor(const QRectF &rect)
    #      const
    ritual = 'ritual_ZNK23QPixmapDropShadowFilter15boundingRectForERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QPixmapDropShadowFilter15boundingRectForERK6QRec'
          'tF')
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def blurRadius(self) -> float:
    """
    Calls Qt's 'qreal QPixmapDropShadowFilter::blurRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#blurRadius
    """
    #  qreal QPixmapDropShadowFilter::blurRadius() const
    return self.uglySide.call(
        'ritual_ZNK23QPixmapDropShadowFilter10blurRadiusEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QPixmapDropShadowFilter::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPixmapDropShadowFilter::color() const
    address = self.uglySide.call(
        'ritual_ZNK23QPixmapDropShadowFilter5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPixmapDropShadowFilter::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPixmapDropShadowFilter::offset() const
    address = self.uglySide.call(
        'ritual_ZNK23QPixmapDropShadowFilter6offsetEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBlurRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QPixmapDropShadowFilter::setBlurRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#setBlurRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QPixmapDropShadowFilter::setBlurRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QPixmapDropShadowFilter13setBlurRadiusEd', radius,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPixmapDropShadowFilter::setColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPixmapDropShadowFilter::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN23QPixmapDropShadowFilter8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QPointF)
  def setOffset(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QPixmapDropShadowFilter::setOffset(const QPointF
    &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#setOffset

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPixmapDropShadowFilter::setOffset(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN23QPixmapDropShadowFilter9setOffsetERK7QPointF',
        self._valueOf(offset, 'QPointF'),
    )

  @overload(float, float)
  def setOffset(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QPixmapDropShadowFilter::setOffset(qreal dx, qreal dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#setOffset

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QPixmapDropShadowFilter::setOffset(qreal dx, qreal dy)
    self.uglySide.call(
        'ritual_ZN23QPixmapDropShadowFilter9setOffsetEdd', dx, dy,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapDropShadowFilter::QPixmapDropShadowFilter(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPixmapDropShadowFilter::QPixmapDropShadowFilter(QObject *parent)
    self._noteCreation(QPixmapDropShadowFilter, lambda: Rituals.call(
        'ritual_ZN23QPixmapDropShadowFilterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QPainter, QPointF, QPixmap)
  @overload(NoneType, QPointF, QPixmap)
  @overload(QPainter, QPointF, QPixmap, QRectF)
  @overload(NoneType, QPointF, QPixmap, QRectF)
  def draw(
      self,
      p: Optional[QPainter],
      pos: QPointF,
      px: QPixmap,
      src: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapDropShadowFilter::draw(QPainter *p, const QPointF
    &pos, const QPixmap &px, const QRectF &src) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapdropshadowfilter.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    px : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    src : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QPixmapDropShadowFilter::draw(QPainter *p, const QPointF &pos,
    #      const QPixmap &px, const QRectF &src) const
    if src is None:
      from ..QtCore import QRectF
      src = QRectF()
    ritual = (
        'ritual_ZNK23QPixmapDropShadowFilter4drawEP8QPainterRK7QPointFRK7QP'
        'ixmapRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QPixmapDropShadowFilter4drawEP8QPainterRK7QPoint'
          'FRK7QPixmapRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(p), self._valueOf(pos, 'QPointF'), self._valueOf(px),
        self._valueOf(src),
    )
