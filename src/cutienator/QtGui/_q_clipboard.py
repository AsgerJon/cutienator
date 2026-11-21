"""
QClipboard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qclipboard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData
  from . import QImage, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QMimeData = WAIT['QMimeData']
  QPixmap = WAIT['QPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QClipboard(QObject):
  """
  The cute side of Qt's QClipboard: a plain Python object standing in front
  of one C++ QClipboard.

  It is built on the cute 'QObject', as Qt's QClipboard is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QClipboard that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'clear',
  'supportsSelection', 'supportsFindBuffer', 'ownsSelection',
  'ownsClipboard', 'ownsFindBuffer', 'text', 'setText', 'mimeData',
  'setMimeData', 'image', 'pixmap', 'setImage', 'setPixmap'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  16 of the 32 functions Qt declares: 6 private; 4 a signal; 3 takes or gives
  a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QClipboard is created at the first use, not by 'QClipboard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QClipboard.
  - Qt tells when it has removed the C++ QClipboard. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QClipboard, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """The enum 'QClipboard::Mode' of Qt, with the 4 names Qt gives in it."""

    Clipboard = Kee[int](0)
    Selection = Kee[int](1)
    FindBuffer = Kee[int](2)
    LastMode = Kee[int](2)

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
    Calls Qt's 'QString QClipboard::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#tr

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
    #  QString QClipboard::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QClipboard2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QClipboard'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QClipboard::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QClipboard::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QClipboard10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def supportsSelection(self) -> bool:
    """
    Calls Qt's 'bool QClipboard::supportsSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#supportsSelection
    """
    #  bool QClipboard::supportsSelection() const
    return self.uglySide.call('ritual_ZNK10QClipboard17supportsSelectionEv')

  def supportsFindBuffer(self) -> bool:
    """
    Calls Qt's 'bool QClipboard::supportsFindBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#supportsFindBuffer
    """
    #  bool QClipboard::supportsFindBuffer() const
    return self.uglySide.call('ritual_ZNK10QClipboard18supportsFindBufferEv')

  def ownsSelection(self) -> bool:
    """
    Calls Qt's 'bool QClipboard::ownsSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#ownsSelection
    """
    #  bool QClipboard::ownsSelection() const
    return self.uglySide.call('ritual_ZNK10QClipboard13ownsSelectionEv')

  def ownsClipboard(self) -> bool:
    """
    Calls Qt's 'bool QClipboard::ownsClipboard() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#ownsClipboard
    """
    #  bool QClipboard::ownsClipboard() const
    return self.uglySide.call('ritual_ZNK10QClipboard13ownsClipboardEv')

  def ownsFindBuffer(self) -> bool:
    """
    Calls Qt's 'bool QClipboard::ownsFindBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#ownsFindBuffer
    """
    #  bool QClipboard::ownsFindBuffer() const
    return self.uglySide.call('ritual_ZNK10QClipboard14ownsFindBufferEv')

  @overload()
  @overload(Mode)
  def text(self, mode: Mode = Mode.Clipboard) -> str:
    """
    Calls Qt's 'QString QClipboard::text(Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#text

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QClipboard::text(Mode mode) const
    return self.uglySide.call(
        'ritual_ZNK10QClipboard4textENS_4ModeE', mode.value,
    )

  @overload()
  @overload(Mode)
  def mimeData(self, mode: Mode = Mode.Clipboard) -> Optional[QMimeData]:
    """
    Calls Qt's 'const QMimeData *QClipboard::mimeData(Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#mimeData

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMimeData *QClipboard::mimeData(Mode mode) const
    address = self.uglySide.call(
        'ritual_ZNK10QClipboard8mimeDataENS_4ModeE', mode.value,
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload()
  @overload(Mode)
  def image(self, mode: Mode = Mode.Clipboard) -> QImage:
    """
    Calls Qt's 'QImage QClipboard::image(Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#image

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QClipboard::image(Mode mode) const
    address = self.uglySide.call(
        'ritual_ZNK10QClipboard5imageENS_4ModeE', mode.value,
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload()
  @overload(Mode)
  def pixmap(self, mode: Mode = Mode.Clipboard) -> QPixmap:
    """
    Calls Qt's 'QPixmap QClipboard::pixmap(Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#pixmap

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QClipboard::pixmap(Mode mode) const
    address = self.uglySide.call(
        'ritual_ZNK10QClipboard6pixmapENS_4ModeE', mode.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, Mode)
  def setText(self, a0: str, mode: Mode = Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QClipboard::setText(const QString &a0, Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.
    """
    #  void QClipboard::setText(const QString &a0, Mode mode)
    self.uglySide.call(
        'ritual_ZN10QClipboard7setTextERK7QStringNS_4ModeE', a0, mode.value,
    )

  @overload(QMimeData)
  @overload(NoneType)
  @overload(QMimeData, Mode)
  @overload(NoneType, Mode)
  def setMimeData(
      self,
      data: Optional[QMimeData],
      mode: Mode = Mode.Clipboard,
  ) -> None:
    """
    Calls Qt's 'void QClipboard::setMimeData(QMimeData *data, Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#setMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.
    """
    #  void QClipboard::setMimeData(QMimeData *data, Mode mode)
    self.uglySide.call(
        'ritual_ZN10QClipboard11setMimeDataEP9QMimeDataNS_4ModeE',
        self._addressOf(data), mode.value,
    )

  @overload(QImage)
  @overload(QImage, Mode)
  def setImage(self, a0: QImage, mode: Mode = Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QClipboard::setImage(const QImage &a0, Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#setImage

    Parameters
    ----------

    a0 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.
    """
    #  void QClipboard::setImage(const QImage &a0, Mode mode)
    self.uglySide.call(
        'ritual_ZN10QClipboard8setImageERK6QImageNS_4ModeE',
        self._valueOf(a0), mode.value,
    )

  @overload(QPixmap)
  @overload(QPixmap, Mode)
  def setPixmap(self, a0: QPixmap, mode: Mode = Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QClipboard::setPixmap(const QPixmap &a0, Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#setPixmap

    Parameters
    ----------

    a0 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.
    """
    #  void QClipboard::setPixmap(const QPixmap &a0, Mode mode)
    self.uglySide.call(
        'ritual_ZN10QClipboard9setPixmapERK7QPixmapNS_4ModeE',
        self._valueOf(a0), mode.value,
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

  @overload()
  @overload(Mode)
  def clear(self, mode: Mode = Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QClipboard::clear(Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipboard.html#clear

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Clipboard.
    """
    #  void QClipboard::clear(Mode mode)
    self.uglySide.call('ritual_ZN10QClipboard5clearENS_4ModeE', mode.value)
