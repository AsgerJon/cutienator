"""
QPixmapBlurFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapBlurFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGraphicsBlurEffect, QPixmapFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmapBlurFilter(QPixmapFilter):
  """
  The cute side of Qt's QPixmapBlurFilter: a plain Python object standing in
  front of one C++ QPixmapBlurFilter.

  It is built on the cute 'QPixmapFilter', as Qt's QPixmapBlurFilter is built
  on Qt's QPixmapFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapBlurFilter that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'setRadius',
  'setBlurHints', 'radius', 'blurHints', 'boundingRectFor', 'draw'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPixmapBlurFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPixmapBlurFilter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPixmapBlurFilterPrivate *QPixmapBlurFilter::d_func()': gives
    'QPixmapBlurFilterPrivate', which has no cute class yet.
  - Qt's 'const QPixmapBlurFilterPrivate *QPixmapBlurFilter::d_func() const':
    gives 'QPixmapBlurFilterPrivate', which has no cute class yet.
  - Qt's 'QPixmapBlurFilter::~QPixmapBlurFilter()': the destructor: Python
    never removes a C++ QPixmapBlurFilter.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPixmapBlurFilter is created at the first use, not by
    'QPixmapBlurFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapBlurFilter.
  - Qt tells when it has removed the C++ QPixmapBlurFilter. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPixmapBlurFilter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#tr

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
    #  QString QPixmapBlurFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QPixmapBlurFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapBlurFilter'

  #  A C++ QPixmapBlurFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapBlurFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapBlurFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapBlurFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QPixmapBlurFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QPixmapBlurFilter::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#radius
    """
    #  qreal QPixmapBlurFilter::radius() const
    return self.uglySide.call('ritual_ZNK17QPixmapBlurFilter6radiusEv')

  def blurHints(self) -> QGraphicsBlurEffect.BlurHints:
    """
    Calls Qt's 'QGraphicsBlurEffect::BlurHints QPixmapBlurFilter::blurHints()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#blurHints

    Returns
    -------

    QGraphicsBlurEffect.BlurHints
      The value standing for the combination Qt gave back.
    """
    #  QGraphicsBlurEffect::BlurHints QPixmapBlurFilter::blurHints() const
    return QGraphicsBlurEffect.BlurHints(self.uglySide.call(
        'ritual_ZNK17QPixmapBlurFilter9blurHintsEv',
    ))

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QPixmapBlurFilter::boundingRectFor(const QRectF &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapblurfilter.html#boundingRectFor

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
    #  QRectF QPixmapBlurFilter::boundingRectFor(const QRectF &rect) const
    ritual = 'ritual_ZNK17QPixmapBlurFilter15boundingRectForERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPixmapBlurFilter15boundingRectForERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QPixmapBlurFilter::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QPixmapBlurFilter::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN17QPixmapBlurFilter9setRadiusEd', radius)

  @overload(QGraphicsBlurEffect.BlurHints)
  def setBlurHints(self, hints: QGraphicsBlurEffect.BlurHints) -> None:
    """
    Calls Qt's 'void
    QPixmapBlurFilter::setBlurHints(QGraphicsBlurEffect::BlurHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapblurfilter.html#setBlurHints

    Parameters
    ----------

    hints : QGraphicsBlurEffect.BlurHints
      Passed on as its number.
    """
    #  void QPixmapBlurFilter::setBlurHints(QGraphicsBlurEffect::BlurHints
    #      hints)
    self.uglySide.call(
        'ritual_ZN17QPixmapBlurFilter12setBlurHintsE6QFlagsIN19QGraphicsBlu'
        'rEffect8BlurHintEE',
        hints.value,
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
    'QPixmapBlurFilter::QPixmapBlurFilter(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapblurfilter.html#QPixmapBlurFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPixmapBlurFilter::QPixmapBlurFilter(QObject *parent)
    self._noteCreation(QPixmapBlurFilter, lambda: Rituals.call(
        'ritual_ZN17QPixmapBlurFilterC1EP7QObject',
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
      painter: Optional[QPainter],
      dest: QPointF,
      src: QPixmap,
      srcRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapBlurFilter::draw(QPainter *painter, const QPointF
    &dest, const QPixmap &src, const QRectF &srcRect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapblurfilter.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dest : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    src : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    srcRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QPixmapBlurFilter::draw(QPainter *painter, const QPointF &dest,
    #      const QPixmap &src, const QRectF &srcRect) const
    if srcRect is None:
      from ..QtCore import QRectF
      srcRect = QRectF()
    ritual = (
        'ritual_ZNK17QPixmapBlurFilter4drawEP8QPainterRK7QPointFRK7QPixmapR'
        'K6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QPixmapBlurFilter4drawEP8QPainterRK7QPointFRK7QP'
          'ixmapRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(dest, 'QPointF'),
        self._valueOf(src), self._valueOf(srcRect),
    )
