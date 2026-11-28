"""
QIconLoaderEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QIconLoaderEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QIcon, QIconEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QIconLoaderEngineEntry, QPainter, QPixmap, QThemeIconInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QThemeIconInfo = WAIT['QThemeIconInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIconLoaderEngine(QIconEngine):
  """
  The cute side of Qt's QIconLoaderEngine: a plain Python object standing in
  front of one C++ QIconLoaderEngine.

  It is built on the cute 'QIconEngine', as Qt's QIconLoaderEngine is built
  on Qt's QIconEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIconLoaderEngine that has a ritual and that Python
  can call so far, 11 names in all: 'paint', 'pixmap', 'actualSize', 'clone',
  'iconName', 'isNull', 'scaledPixmap', 'availableSizes', 'entryForSize',
  'key', 'hasIcon'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconLoaderEngine::~QIconLoaderEngine()': the destructor: Python
    never removes a C++ QIconLoaderEngine.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QIconLoaderEngine is created at the first use, not by
    'QIconLoaderEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIconLoaderEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QThemeIconInfo, QSize)
  @overload(QThemeIconInfo, QSize, int)
  def entryForSize(
      info: QThemeIconInfo,
      size: QSize,
      scale: int = 1,
  ) -> Optional[QIconLoaderEngineEntry]:
    """
    Calls Qt's 'QIconLoaderEngineEntry *QIconLoaderEngine::entryForSize(const
    QThemeIconInfo &info, const QSize &size, int scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloaderengine.html#entryForSize

    Parameters
    ----------

    info : QThemeIconInfo
      Passed on as a value: Qt reads the C++ QThemeIconInfo, which stays
      Python's own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    scale : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    Optional[QIconLoaderEngineEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconLoaderEngineEntry *QIconLoaderEngine::entryForSize(const
    #      QThemeIconInfo &info, const QSize &size, int scale)
    address = Rituals.call(
        'ritual_ZN17QIconLoaderEngine12entryForSizeERK14QThemeIconInfoRK5QS'
        'izei',
        CuteMixin._valueOf(info), CuteMixin._valueOf(size), scale,
    )
    from . import QIconLoaderEngineEntry
    return QIconLoaderEngineEntry._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconLoaderEngine'

  #  A C++ QIconLoaderEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIconLoaderEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QIconLoaderEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QIconLoaderEngine::clone() const
    ritual = 'ritual_ZNK17QIconLoaderEngine5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QIconLoaderEngine5cloneEv'
    address = self.uglySide.call(ritual)
    return QIconEngine._cuteAt(address)

  def key(self) -> str:
    """
    Calls Qt's 'QString QIconLoaderEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconLoaderEngine::key() const
    ritual = 'ritual_ZNK17QIconLoaderEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QIconLoaderEngine3keyEv'
    return self.uglySide.call(ritual)

  def hasIcon(self) -> bool:
    """
    Calls Qt's 'bool QIconLoaderEngine::hasIcon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#hasIcon
    """
    #  bool QIconLoaderEngine::hasIcon() const
    return self.uglySide.call('ritual_ZNK17QIconLoaderEngine7hasIconEv')

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
  @overload(str)
  def __init__(self, iconName: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QIconLoaderEngine::QIconLoaderEngine(const QString &iconName)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloaderengine.html#QIconLoaderEngine

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QIconLoaderEngine::QIconLoaderEngine(const QString &iconName)
    self._noteCreation(QIconLoaderEngine, lambda: Rituals.call(
        'ritual_ZN17QIconLoaderEngineC1ERK7QString', iconName,
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
    Calls Qt's 'void QIconLoaderEngine::paint(QPainter *painter, const QRect
    &rect, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#paint

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
    #  void QIconLoaderEngine::paint(QPainter *painter, const QRect &rect,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QIconLoaderEngine5paintEP8QPainterRK5QRectN5QIcon4ModeE'
        'NS5_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconLoaderEngine5paintEP8QPainterRK5QRectN5QIcon'
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
    Calls Qt's 'QPixmap QIconLoaderEngine::pixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#pixmap

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
    #  QPixmap QIconLoaderEngine::pixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN17QIconLoaderEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5Stat'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconLoaderEngine6pixmapERK5QSizeN5QIcon4ModeENS3'
          '_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QIconLoaderEngine::actualSize(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#actualSize

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
    #  QSize QIconLoaderEngine::actualSize(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state)
    ritual = (
        'ritual_ZN17QIconLoaderEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_'
        '5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconLoaderEngine10actualSizeERK5QSizeN5QIcon4Mod'
          'eENS3_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QIconLoaderEngine::iconName()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconLoaderEngine::iconName()
    ritual = 'ritual_ZN17QIconLoaderEngine8iconNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconLoaderEngine8iconNameEv'
    return self.uglySide.call(ritual)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QIconLoaderEngine::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloaderengine.html#isNull
    """
    #  bool QIconLoaderEngine::isNull()
    ritual = 'ritual_ZN17QIconLoaderEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconLoaderEngine6isNullEv'
    return self.uglySide.call(ritual)

  @overload(QSize, QIcon.Mode, QIcon.State, float)
  def scaledPixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
      scale: float,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state, qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloaderengine.html#scaledPixmap

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
    #  QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state, qreal scale)
    ritual = (
        'ritual_ZN17QIconLoaderEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS'
        '3_5StateEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconLoaderEngine12scaledPixmapERK5QSizeN5QIcon4M'
          'odeENS3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QIcon.Mode, QIcon.State)
  def availableSizes(
      self,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QIconLoaderEngine::availableSizes(QIcon::Mode
    mode, QIcon::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloaderengine.html#availableSizes

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
    #  QList<QSize> QIconLoaderEngine::availableSizes(QIcon::Mode mode,
    #      QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN17QIconLoaderEngine14availableSizesEN5QIcon4ModeENS0_5Sta'
        'teE',
        mode.value, state.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)
