"""
QPixmapIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qicon_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPixmapIconEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QIcon, QIconEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QPainter, QPixmap, QPixmapIconEngineEntry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPixmapIconEngineEntry = WAIT['QPixmapIconEngineEntry']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmapIconEngine(QIconEngine):
  """
  The cute side of Qt's QPixmapIconEngine: a plain Python object standing in
  front of one C++ QPixmapIconEngine.

  It is built on the cute 'QIconEngine', as Qt's QPixmapIconEngine is built
  on Qt's QIconEngine, and has everything that class has.

  C++ hands a QPixmapIconEngine around as a copy, so every C++
  QPixmapIconEngine behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPixmapIconEngine that has a ritual and that Python
  can call so far, 14 names in all: 'paint', 'pixmap', 'scaledPixmap',
  'bestMatch', 'actualSize', 'availableSizes', 'addPixmap', 'addFile',
  'isNull', 'key', 'clone', 'adjustSize', 'removePixmapEntry', 'tryMatch'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPixmapIconEngine::~QPixmapIconEngine()': the destructor: Python
    removes its C++ QPixmapIconEngine by it, and has no other use for it.
  - Qt's 'bool QPixmapIconEngine::read(QDataStream &in)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QPixmapIconEngine::write(QDataStream &out) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 written with the class 'QIcon', which
  declares it as well and stands first in it.

  What to expect
  --------------

  - The C++ QPixmapIconEngine is created at the first use, not by
    'QPixmapIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPixmapIconEngine back gives a copy the ritual made
    for Python, in a new cute QPixmapIconEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize, QSize)
  def adjustSize(expectedSize: QSize, size: QSize) -> QSize:
    """
    Calls Qt's 'QSize QPixmapIconEngine::adjustSize(const QSize
    &expectedSize, QSize size)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#adjustSize

    Parameters
    ----------

    expectedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapIconEngine::adjustSize(const QSize &expectedSize, QSize
    #      size)
    address = Rituals.call(
        'ritual_ZN17QPixmapIconEngine10adjustSizeERK5QSizeS0_',
        CuteMixin._valueOf(expectedSize), CuteMixin._valueOf(size),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapIconEngine'

  #  A C++ QPixmapIconEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapIconEngine'

  #  Qt's '~QPixmapIconEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QPixmapIconEngine behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QPixmapIconEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> str:
    """
    Calls Qt's 'QString QPixmapIconEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPixmapIconEngine::key() const
    ritual = 'ritual_ZNK17QPixmapIconEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPixmapIconEngine3keyEv'
    return self.uglySide.call(ritual)

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QPixmapIconEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QPixmapIconEngine::clone() const
    ritual = 'ritual_ZNK17QPixmapIconEngine5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPixmapIconEngine5cloneEv'
    address = self.uglySide.call(ritual)
    return QIconEngine._cuteAt(address)

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
    Notes what was given, for Qt's 'QPixmapIconEngine::QPixmapIconEngine()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengine.html#QPixmapIconEngine
    """
    #  QPixmapIconEngine::QPixmapIconEngine()
    self._noteCreation(QPixmapIconEngine, lambda: Rituals.call(
        'ritual_ZN17QPixmapIconEngineC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QPixmapIconEngine) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapIconEngine::QPixmapIconEngine(const QPixmapIconEngine &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengine.html#QPixmapIconEngine

    Parameters
    ----------

    a0 : QPixmapIconEngine
      Passed on as a value: Qt reads the C++ QPixmapIconEngine, which stays
      Python's own.
    """
    #  QPixmapIconEngine::QPixmapIconEngine(const QPixmapIconEngine &a0)
    self._noteCreation(QPixmapIconEngine, lambda: Rituals.call(
        'ritual_ZN17QPixmapIconEngineC1ERKS_', self._valueOf(a0),
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
    Calls Qt's 'void QPixmapIconEngine::paint(QPainter *painter, const QRect
    &rect, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#paint

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
    #  void QPixmapIconEngine::paint(QPainter *painter, const QRect &rect,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QPixmapIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeE'
        'NS5_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine5paintEP8QPainterRK5QRectN5QIcon'
          '4ModeENS5_5StateE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), mode.value,
        state.value,
    )

  @overload(QSize, QIcon.Mode, QIcon.State)
  def pixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmapIconEngine::pixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#pixmap

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
    #  QPixmap QPixmapIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN17QPixmapIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5Stat'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3'
          '_5StateE')
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
    Calls Qt's 'QPixmap QPixmapIconEngine::scaledPixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state, qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengine.html#scaledPixmap

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
    #  QPixmap QPixmapIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state, qreal scale)
    ritual = (
        'ritual_ZN17QPixmapIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS'
        '3_5StateEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine12scaledPixmapERK5QSizeN5QIcon4M'
          'odeENS3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, float, QIcon.Mode, QIcon.State)
  def bestMatch(
      self,
      size: QSize,
      scale: float,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> Optional[QPixmapIconEngineEntry]:
    """
    Calls Qt's 'QPixmapIconEngineEntry *QPixmapIconEngine::bestMatch(const
    QSize &size, qreal scale, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#bestMatch

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    scale : float
      Passed on as it is.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    Optional[QPixmapIconEngineEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPixmapIconEngineEntry *QPixmapIconEngine::bestMatch(const QSize
    #      &size, qreal scale, QIcon::Mode mode, QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN17QPixmapIconEngine9bestMatchERK5QSizedN5QIcon4ModeENS3_5'
        'StateE',
        self._valueOf(size), scale, mode.value, state.value,
    )
    from . import QPixmapIconEngineEntry
    return QPixmapIconEngineEntry._cuteAt(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapIconEngine::actualSize(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#actualSize

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
    #  QSize QPixmapIconEngine::actualSize(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QPixmapIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_'
        '5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine10actualSizeERK5QSizeN5QIcon4Mod'
          'eENS3_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QIcon.Mode, QIcon.State)
  def availableSizes(
      self,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QPixmapIconEngine::availableSizes(QIcon::Mode
    mode, QIcon::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengine.html#availableSizes

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QPixmapIconEngine::availableSizes(QIcon::Mode mode,
    #      QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN17QPixmapIconEngine14availableSizesEN5QIcon4ModeENS0_5Sta'
        'teE',
        mode.value, state.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  @overload(QPixmap, QIcon.Mode, QIcon.State)
  def addPixmap(
      self,
      pixmap: QPixmap,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QPixmapIconEngine::addPixmap(const QPixmap &pixmap,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#addPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QPixmapIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
    #      mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QPixmapIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_'
        '5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine9addPixmapERK7QPixmapN5QIcon4Mod'
          'eENS3_5StateE')
    self.uglySide.call(
        ritual, self._valueOf(pixmap), mode.value, state.value,
    )

  @overload(str, QSize, QIcon.Mode, QIcon.State)
  def addFile(
      self,
      fileName: str,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QPixmapIconEngine::addFile(const QString &fileName,
    const QSize &size, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#addFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QPixmapIconEngine::addFile(const QString &fileName, const QSize
    #      &size, QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QPixmapIconEngine7addFileERK7QStringRK5QSizeN5QIcon4Mod'
        'eENS6_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPixmapIconEngine7addFileERK7QStringRK5QSizeN5QIc'
          'on4ModeENS6_5StateE')
    self.uglySide.call(
        ritual, fileName, self._valueOf(size), mode.value, state.value,
    )

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPixmapIconEngine::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#isNull
    """
    #  bool QPixmapIconEngine::isNull()
    ritual = 'ritual_ZN17QPixmapIconEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPixmapIconEngine6isNullEv'
    return self.uglySide.call(ritual)

  @overload(QPixmapIconEngineEntry)
  @overload(NoneType)
  def removePixmapEntry(self, pe: Optional[QPixmapIconEngineEntry]) -> None:
    """
    Calls Qt's 'void
    QPixmapIconEngine::removePixmapEntry(QPixmapIconEngineEntry *pe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengine.html#removePixmapEntry

    Parameters
    ----------

    pe : Optional[QPixmapIconEngineEntry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapIconEngine::removePixmapEntry(QPixmapIconEngineEntry *pe)
    self.uglySide.call(
        'ritual_ZN17QPixmapIconEngine17removePixmapEntryEP22QPixmapIconEngi'
        'neEntry',
        self._addressOf(pe),
    )

  @overload(QSize, float, QIcon.Mode, QIcon.State)
  def tryMatch(
      self,
      size: QSize,
      scale: float,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> Optional[QPixmapIconEngineEntry]:
    """
    Calls Qt's 'QPixmapIconEngineEntry *QPixmapIconEngine::tryMatch(const
    QSize &size, qreal scale, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapiconengine.html#tryMatch

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    scale : float
      Passed on as it is.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    Optional[QPixmapIconEngineEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPixmapIconEngineEntry *QPixmapIconEngine::tryMatch(const QSize &size,
    #      qreal scale, QIcon::Mode mode, QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN17QPixmapIconEngine8tryMatchERK5QSizedN5QIcon4ModeENS3_5S'
        'tateE',
        self._valueOf(size), scale, mode.value, state.value,
    )
    from . import QPixmapIconEngineEntry
    return QPixmapIconEngineEntry._cuteAt(address)
