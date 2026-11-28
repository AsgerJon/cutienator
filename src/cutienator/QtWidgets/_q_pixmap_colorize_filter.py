"""
QPixmapColorizeFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapColorizeFilter to be private: it declares the class in a
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


class QPixmapColorizeFilter(QPixmapFilter):
  """
  The cute side of Qt's QPixmapColorizeFilter: a plain Python object standing
  in front of one C++ QPixmapColorizeFilter.

  It is built on the cute 'QPixmapFilter', as Qt's QPixmapColorizeFilter is
  built on Qt's QPixmapFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapColorizeFilter that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'setColor',
  'color', 'setStrength', 'strength', 'draw'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPixmapColorizeFilter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPixmapColorizeFilter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPixmapColorizeFilterPrivate *QPixmapColorizeFilter::d_func()':
    gives 'QPixmapColorizeFilterPrivate', which has no cute class yet.
  - Qt's 'const QPixmapColorizeFilterPrivate *QPixmapColorizeFilter::d_func()
    const': gives 'QPixmapColorizeFilterPrivate', which has no cute class
    yet.
  - Qt's 'QPixmapColorizeFilter::~QPixmapColorizeFilter()': the destructor:
    Python never removes a C++ QPixmapColorizeFilter.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPixmapColorizeFilter is created at the first use, not by
    'QPixmapColorizeFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapColorizeFilter.
  - Qt tells when it has removed the C++ QPixmapColorizeFilter. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPixmapColorizeFilter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#tr

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
    #  QString QPixmapColorizeFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPixmapColorizeFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapColorizeFilter'

  #  A C++ QPixmapColorizeFilter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapColorizeFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapColorizeFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapColorizeFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPixmapColorizeFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QPixmapColorizeFilter::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPixmapColorizeFilter::color() const
    address = self.uglySide.call('ritual_ZNK21QPixmapColorizeFilter5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strength(self) -> float:
    """
    Calls Qt's 'qreal QPixmapColorizeFilter::strength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#strength
    """
    #  qreal QPixmapColorizeFilter::strength() const
    return self.uglySide.call('ritual_ZNK21QPixmapColorizeFilter8strengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPixmapColorizeFilter::setColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPixmapColorizeFilter::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN21QPixmapColorizeFilter8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void QPixmapColorizeFilter::setStrength(qreal strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#setStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void QPixmapColorizeFilter::setStrength(qreal strength)
    self.uglySide.call(
        'ritual_ZN21QPixmapColorizeFilter11setStrengthEd', strength,
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
    'QPixmapColorizeFilter::QPixmapColorizeFilter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#QPixmapColorizeFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPixmapColorizeFilter::QPixmapColorizeFilter(QObject *parent)
    self._noteCreation(QPixmapColorizeFilter, lambda: Rituals.call(
        'ritual_ZN21QPixmapColorizeFilterC1EP7QObject',
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
    Calls Qt's 'void QPixmapColorizeFilter::draw(QPainter *painter, const
    QPointF &dest, const QPixmap &src, const QRectF &srcRect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcolorizefilter.html#draw

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
    #  void QPixmapColorizeFilter::draw(QPainter *painter, const QPointF
    #      &dest, const QPixmap &src, const QRectF &srcRect) const
    if srcRect is None:
      from ..QtCore import QRectF
      srcRect = QRectF()
    ritual = (
        'ritual_ZNK21QPixmapColorizeFilter4drawEP8QPainterRK7QPointFRK7QPix'
        'mapRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPixmapColorizeFilter4drawEP8QPainterRK7QPointFR'
          'K7QPixmapRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(dest, 'QPointF'),
        self._valueOf(src), self._valueOf(srcRect),
    )
