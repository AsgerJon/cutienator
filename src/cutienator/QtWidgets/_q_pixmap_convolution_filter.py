"""
QPixmapConvolutionFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapConvolutionFilter to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class QPixmapConvolutionFilter(QPixmapFilter):
  """
  The cute side of Qt's QPixmapConvolutionFilter: a plain Python object
  standing in front of one C++ QPixmapConvolutionFilter.

  It is built on the cute 'QPixmapFilter', as Qt's QPixmapConvolutionFilter
  is built on Qt's QPixmapFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapConvolutionFilter that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'boundingRectFor', 'draw', 'rows', 'columns'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPixmapConvolutionFilter::~QPixmapConvolutionFilter()': the
    destructor: Python never removes a C++ QPixmapConvolutionFilter.

  What has no ritual
  ------------------

  8 of the 16 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QPixmapConvolutionFilter is created at the first use, not by
    'QPixmapConvolutionFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapConvolutionFilter.
  - Qt tells when it has removed the C++ QPixmapConvolutionFilter. Every call
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
    Calls Qt's 'QString QPixmapConvolutionFilter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#tr

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
    #  QString QPixmapConvolutionFilter::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QPixmapConvolutionFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapConvolutionFilter'

  #  A C++ QPixmapConvolutionFilter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapConvolutionFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapConvolutionFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapConvolutionFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QPixmapConvolutionFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QPixmapConvolutionFilter::boundingRectFor(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#boundingRectFor

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
    #  QRectF QPixmapConvolutionFilter::boundingRectFor(const QRectF &rect)
    #      const
    ritual = (
        'ritual_ZNK24QPixmapConvolutionFilter15boundingRectForERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPixmapConvolutionFilter15boundingRectForERK6QRe'
          'ctF')
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def rows(self) -> int:
    """
    Calls Qt's 'int QPixmapConvolutionFilter::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#rows
    """
    #  int QPixmapConvolutionFilter::rows() const
    return self.uglySide.call('ritual_ZNK24QPixmapConvolutionFilter4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QPixmapConvolutionFilter::columns() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#columns
    """
    #  int QPixmapConvolutionFilter::columns() const
    return self.uglySide.call(
        'ritual_ZNK24QPixmapConvolutionFilter7columnsEv',
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapConvolutionFilter::QPixmapConvolutionFilter(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPixmapConvolutionFilter::QPixmapConvolutionFilter(QObject *parent)
    self._noteCreation(QPixmapConvolutionFilter, lambda: Rituals.call(
        'ritual_ZN24QPixmapConvolutionFilterC1EP7QObject',
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
    Calls Qt's 'void QPixmapConvolutionFilter::draw(QPainter *painter, const
    QPointF &dest, const QPixmap &src, const QRectF &srcRect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapconvolutionfilter.html#draw

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
    #  void QPixmapConvolutionFilter::draw(QPainter *painter, const QPointF
    #      &dest, const QPixmap &src, const QRectF &srcRect) const
    if srcRect is None:
      from ..QtCore import QRectF
      srcRect = QRectF()
    ritual = (
        'ritual_ZNK24QPixmapConvolutionFilter4drawEP8QPainterRK7QPointFRK7Q'
        'PixmapRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPixmapConvolutionFilter4drawEP8QPainterRK7QPoin'
          'tFRK7QPixmapRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(dest), self._valueOf(src),
        self._valueOf(srcRect),
    )
