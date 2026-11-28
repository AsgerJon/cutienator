"""
QPixmapFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapFilter to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

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


class QPixmapFilter(QObject):
  """
  The cute side of Qt's QPixmapFilter: a plain Python object standing in
  front of one C++ QPixmapFilter.

  It is built on the cute 'QObject', as Qt's QPixmapFilter is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapFilter that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'type', 'boundingRectFor',
  'draw'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPixmapFilter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPixmapFilter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPixmapFilterPrivate *QPixmapFilter::d_func()': gives
    'QPixmapFilterPrivate', which has no cute class yet.
  - Qt's 'const QPixmapFilterPrivate *QPixmapFilter::d_func() const': gives
    'QPixmapFilterPrivate', which has no cute class yet.
  - Qt's 'QPixmapFilter::~QPixmapFilter()': the destructor: Python never
    removes a C++ QPixmapFilter.
  - Qt's 'QPixmapFilter::QPixmapFilter(QPixmapFilterPrivate &d, FilterType
    type, QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPixmapFilter is created at the first use, not by
    'QPixmapFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapFilter.
  - Qt tells when it has removed the C++ QPixmapFilter. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPixmapFilter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FilterType(CuteNum):
    """
    The enum 'QPixmapFilter::FilterType' of Qt, with the 5 names Qt gives in
    it.
    """

    ConvolutionFilter = Kee[int](0)
    ColorizeFilter = Kee[int](1)
    DropShadowFilter = Kee[int](2)
    BlurFilter = Kee[int](3)
    UserFilter = Kee[int](1024)

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
    Calls Qt's 'QString QPixmapFilter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#tr

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
    #  QString QPixmapFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPixmapFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapFilter'

  #  A C++ QPixmapFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapFilter'

  #  The functions Qt calls itself that QPixmapFilter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'boundingRectFor': (
          ('_ZNK13QPixmapFilter15boundingRectForERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'draw': (
          ('_ZNK13QPixmapFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRect'
           'F',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapFilter::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPixmapFilter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> FilterType:
    """
    Calls Qt's 'FilterType QPixmapFilter::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#type

    Returns
    -------

    FilterType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterType(number)'
      gives.
    """
    #  FilterType QPixmapFilter::type() const
    return QPixmapFilter.FilterType(self.uglySide.call(
        'ritual_ZNK13QPixmapFilter4typeEv',
    ))

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QPixmapFilter::boundingRectFor(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#boundingRectFor

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
    #  QRectF QPixmapFilter::boundingRectFor(const QRectF &rect) const
    ritual = 'ritual_ZNK13QPixmapFilter15boundingRectForERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPixmapFilter15boundingRectForERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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

  @overload(FilterType, QObject)
  @overload(FilterType, NoneType)
  def __init__(self, type: FilterType, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QPixmapFilter::QPixmapFilter(FilterType
    type, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#QPixmapFilter

    Parameters
    ----------

    type : FilterType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPixmapFilter::QPixmapFilter(FilterType type, QObject *parent)
    self._noteCreation(QPixmapFilter, lambda: Rituals.call(
        'ritual_ZN13QPixmapFilterC1ENS_10FilterTypeEP7QObject',
        type.value, self._addressOf(parent, 'QObject'),
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
      p: QPointF,
      src: QPixmap,
      srcRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapFilter::draw(QPainter *painter, const QPointF &p,
    const QPixmap &src, const QRectF &srcRect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapfilter.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    src : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    srcRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QPixmapFilter::draw(QPainter *painter, const QPointF &p, const
    #      QPixmap &src, const QRectF &srcRect) const
    if srcRect is None:
      from ..QtCore import QRectF
      srcRect = QRectF()
    self.uglySide.call(
        'ritual_ZNK13QPixmapFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QR'
        'ectF',
        self._addressOf(painter), self._valueOf(p, 'QPointF'),
        self._valueOf(src), self._valueOf(srcRect),
    )
