"""
QProxyIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QProxyIconEngine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QIcon, QIconEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProxyIconEngine(QIconEngine):
  """
  The cute side of Qt's QProxyIconEngine: a plain Python object standing in
  front of one C++ QProxyIconEngine.

  It is built on the cute 'QIconEngine', as Qt's QProxyIconEngine is built on
  Qt's QIconEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProxyIconEngine that has a ritual and that Python
  can call so far, 12 names in all: 'paint', 'actualSize', 'pixmap',
  'addPixmap', 'addFile', 'key', 'clone', 'availableSizes', 'iconName',
  'isNull', 'scaledPixmap', 'proxiedEngine'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QProxyIconEngine::read(QDataStream &in)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QProxyIconEngine::write(QDataStream &out) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QProxyIconEngine::virtual_hook(int id, void *data)': names
    'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QProxyIconEngine is created at the first use, not by
    'QProxyIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProxyIconEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProxyIconEngine'

  #  A C++ QProxyIconEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProxyIconEngine'

  #  The functions Qt calls itself that QProxyIconEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'proxiedEngine': (
          ('_ZNK16QProxyIconEngine13proxiedEngineEv',
           ('address', 'address', 'QtGui:QIconEngine'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> str:
    """
    Calls Qt's 'QString QProxyIconEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProxyIconEngine::key() const
    ritual = 'ritual_ZNK16QProxyIconEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QProxyIconEngine3keyEv'
    return self.uglySide.call(ritual)

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QProxyIconEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QProxyIconEngine::clone() const
    ritual = 'ritual_ZNK16QProxyIconEngine5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QProxyIconEngine5cloneEv'
    address = self.uglySide.call(ritual)
    return QIconEngine._cuteAt(address)

  def proxiedEngine(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QProxyIconEngine::proxiedEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxyiconengine.html#proxiedEngine

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QProxyIconEngine::proxiedEngine() const
    address = self.uglySide.call(
        'ritual_ZNK16QProxyIconEngine13proxiedEngineEv',
    )
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
    Calls Qt's 'void QProxyIconEngine::paint(QPainter *painter, const QRect
    &rect, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#paint

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
    #  void QProxyIconEngine::paint(QPainter *painter, const QRect &rect,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeEN'
        'S5_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4'
          'ModeENS5_5StateE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), mode.value,
        state.value,
    )

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QProxyIconEngine::actualSize(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#actualSize

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
    #  QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state)
    ritual = (
        'ritual_ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5'
        'StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4Mode'
          'ENS3_5StateE')
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
    Calls Qt's 'QPixmap QProxyIconEngine::pixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#pixmap

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
    #  QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5State'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_'
          '5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QPixmap, QIcon.Mode, QIcon.State)
  def addPixmap(
      self,
      pixmap: QPixmap,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QProxyIconEngine::addPixmap(const QPixmap &pixmap,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#addPixmap

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
    #  void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
    #      mode, QIcon::State state)
    ritual = (
        'ritual_ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5'
        'StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4Mode'
          'ENS3_5StateE')
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
    Calls Qt's 'void QProxyIconEngine::addFile(const QString &fileName, const
    QSize &size, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#addFile

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
    #  void QProxyIconEngine::addFile(const QString &fileName, const QSize
    #      &size, QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4Mode'
        'ENS6_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIco'
          'n4ModeENS6_5StateE')
    self.uglySide.call(
        ritual, fileName, self._valueOf(size), mode.value, state.value,
    )

  @overload()
  @overload(QIcon.Mode)
  @overload(QIcon.Mode, QIcon.State)
  def availableSizes(
      self,
      mode: QIcon.Mode = QIcon.Mode.Normal,
      state: QIcon.State = QIcon.State.Off,
  ) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode
    mode, QIcon::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxyiconengine.html#availableSizes

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QIcon.Mode.Normal.

    state : QIcon.State
      Passed on as its number. May be left out, as in Qt: it is then
      QIcon.State.Off.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode mode,
    #      QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN16QProxyIconEngine14availableSizesEN5QIcon4ModeENS0_5Stat'
        'eE',
        mode.value, state.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QProxyIconEngine::iconName()'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProxyIconEngine::iconName()
    ritual = 'ritual_ZN16QProxyIconEngine8iconNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QProxyIconEngine8iconNameEv'
    return self.uglySide.call(ritual)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QProxyIconEngine::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#isNull
    """
    #  bool QProxyIconEngine::isNull()
    ritual = 'ritual_ZN16QProxyIconEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QProxyIconEngine6isNullEv'
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
    Calls Qt's 'QPixmap QProxyIconEngine::scaledPixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state, qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxyiconengine.html#scaledPixmap

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
    #  QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
    #      mode, QIcon::State state, qreal scale)
    ritual = (
        'ritual_ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3'
        '_5StateEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4Mo'
          'deENS3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)
