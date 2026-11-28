"""
QFontIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfonticonengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFontIconEngine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QIcon, QIconEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QFont, QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontIconEngine(QIconEngine):
  """
  The cute side of Qt's QFontIconEngine: a plain Python object standing in
  front of one C++ QFontIconEngine.

  It is built on the cute 'QIconEngine', as Qt's QFontIconEngine is built on
  Qt's QIconEngine, and has everything that class has.

  C++ hands a QFontIconEngine around as a copy, so every C++ QFontIconEngine
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontIconEngine that has a ritual and that Python
  can call so far, 12 names in all: 'iconName', 'isNull', 'key', 'clone',
  'availableSizes', 'actualSize', 'pixmap', 'scaledPixmap', 'paint',
  'string', 'glyph', 'calculateCacheKey'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontIconEngine::~QFontIconEngine()': the destructor: Python
    removes its C++ QFontIconEngine by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QFontIconEngine is created at the first use, not by
    'QFontIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontIconEngine back gives a copy the ritual made for
    Python, in a new cute QFontIconEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIcon.Mode, QIcon.State)
  def calculateCacheKey(mode: QIcon.Mode, state: QIcon.State) -> int:
    """
    Calls Qt's 'quint64 QFontIconEngine::calculateCacheKey(QIcon::Mode mode,
    QIcon::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfonticonengine.html#calculateCacheKey

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  quint64 QFontIconEngine::calculateCacheKey(QIcon::Mode mode,
    #      QIcon::State state)
    return Rituals.call(
        'ritual_ZN15QFontIconEngine17calculateCacheKeyEN5QIcon4ModeENS0_5St'
        'ateE',
        mode.value, state.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontIconEngine'

  #  A C++ QFontIconEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontIconEngine'

  #  The functions Qt calls itself that QFontIconEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'string': (
          ('_ZNK15QFontIconEngine6stringEv',
           ('address', 'text', ''),
           ()),
      ),
      'glyph': (
          ('_ZNK15QFontIconEngine5glyphEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
  }

  #  Qt's '~QFontIconEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QFontIconEngine behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QFontIconEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> str:
    """
    Calls Qt's 'QString QFontIconEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontIconEngine::key() const
    ritual = 'ritual_ZNK15QFontIconEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QFontIconEngine3keyEv'
    return self.uglySide.call(ritual)

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QFontIconEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QFontIconEngine::clone() const
    ritual = 'ritual_ZNK15QFontIconEngine5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QFontIconEngine5cloneEv'
    address = self.uglySide.call(ritual)
    return QIconEngine._cuteAt(address)

  def string(self) -> str:
    """
    Calls Qt's 'QString QFontIconEngine::string() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#string

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontIconEngine::string() const
    ritual = 'ritual_ZNK15QFontIconEngine6stringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QFontIconEngine6stringEv'
    return self.uglySide.call(ritual)

  def glyph(self) -> int:
    """
    Calls Qt's 'glyph_t QFontIconEngine::glyph() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#glyph
    """
    #  glyph_t QFontIconEngine::glyph() const
    ritual = 'ritual_ZNK15QFontIconEngine5glyphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QFontIconEngine5glyphEv'
    return self.uglySide.call(ritual)

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

  @overload(str, QFont)
  def __init__(self, iconName: str, font: QFont) -> None:
    """
    Notes what was given, for Qt's 'QFontIconEngine::QFontIconEngine(const
    QString &iconName, const QFont &font)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfonticonengine.html#QFontIconEngine

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QFontIconEngine::QFontIconEngine(const QString &iconName, const QFont
    #      &font)
    self._noteCreation(QFontIconEngine, lambda: Rituals.call(
        'ritual_ZN15QFontIconEngineC1ERK7QStringRK5QFont',
        iconName, self._valueOf(font),
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

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QFontIconEngine::iconName()'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontIconEngine::iconName()
    ritual = 'ritual_ZN15QFontIconEngine8iconNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QFontIconEngine8iconNameEv'
    return self.uglySide.call(ritual)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QFontIconEngine::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#isNull
    """
    #  bool QFontIconEngine::isNull()
    ritual = 'ritual_ZN15QFontIconEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QFontIconEngine6isNullEv'
    return self.uglySide.call(ritual)

  @overload(QIcon.Mode, QIcon.State)
  def availableSizes(self, a0: QIcon.Mode, a1: QIcon.State) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QFontIconEngine::availableSizes(QIcon::Mode a0,
    QIcon::State a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfonticonengine.html#availableSizes

    Parameters
    ----------

    a0 : QIcon.Mode
      Passed on as its number.

    a1 : QIcon.State
      Passed on as its number.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QFontIconEngine::availableSizes(QIcon::Mode a0,
    #      QIcon::State a1)
    address = self.uglySide.call(
        'ritual_ZN15QFontIconEngine14availableSizesEN5QIcon4ModeENS0_5State'
        'E',
        a0.value, a1.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QFontIconEngine::actualSize(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#actualSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFontIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN15QFontIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5S'
        'tateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QFontIconEngine10actualSizeERK5QSizeN5QIcon4ModeE'
          'NS3_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def pixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QFontIconEngine::pixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#pixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QFontIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN15QFontIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QFontIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5'
          'StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State, float)
  def scaledPixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
      scale: float,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QFontIconEngine::scaledPixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state, qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#scaledPixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    scale : float
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QFontIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state, qreal scale)
    ritual = (
        'ritual_ZN15QFontIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_'
        '5StateEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QFontIconEngine12scaledPixmapERK5QSizeN5QIcon4Mod'
          'eENS3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QPainter, QRect, QIcon.Mode, QIcon.State)
  @overload(NoneType, QRect, QIcon.Mode, QIcon.State)
  def paint(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QFontIconEngine::paint(QPainter *painter, const QRect
    &rect, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qfonticonengine.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QFontIconEngine::paint(QPainter *painter, const QRect &rect,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN15QFontIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS'
        '5_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QFontIconEngine5paintEP8QPainterRK5QRectN5QIcon4M'
          'odeENS5_5StateE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), mode.value,
        state.value,
    )
