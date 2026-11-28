"""
QLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlabel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QContextMenuEvent, QFocusEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QMovie, QPaintEvent, QPicture, QPixmap
  from . import QLabelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QMovie = WAIT['QMovie']
  QPaintEvent = WAIT['QPaintEvent']
  QPicture = WAIT['QPicture']
  QPixmap = WAIT['QPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLabel(QFrame):
  """
  The cute side of Qt's QLabel: a plain Python object standing in front of
  one C++ QLabel.

  It is built on the cute 'QFrame', as Qt's QLabel is built on Qt's QFrame,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLabel that has a ritual and that Python can call so
  far, 51 names in all: 'metaObject', 'tr', 'text', 'pixmap', 'picture',
  'movie', 'textFormat', 'setTextFormat', 'alignment', 'setAlignment',
  'setWordWrap', 'wordWrap', 'indent', 'setIndent', 'margin', 'setMargin',
  'hasScaledContents', 'setScaledContents', 'sizeHint', 'minimumSizeHint',
  'setBuddy', 'buddy', 'heightForWidth', 'openExternalLinks',
  'setOpenExternalLinks', 'setTextInteractionFlags', 'textInteractionFlags',
  'setSelection', 'hasSelectedText', 'selectedText', 'selectionStart',
  'setText', 'setPixmap', 'setPicture', 'setMovie', 'setNum', 'clear',
  'linkActivated', 'linkHovered', 'event', 'keyPressEvent', 'paintEvent',
  'changeEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'contextMenuEvent', 'focusInEvent', 'focusOutEvent', 'focusNextPrevChild',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLabel::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QLabel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QLabel::~QLabel()': the destructor: Python never removes a C++
    QLabel.
  - Qt's 'QTextDocument::ResourceProvider QLabel::resourceProvider() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QLabel::setResourceProvider(const
    QTextDocument::ResourceProvider &provider)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QLabelPrivate *QLabel::d_func() const': takes in Python what
    'QLabelPrivate *QLabel::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 66 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLabel is created at the first use, not by 'QLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLabel.
  - Qt tells when it has removed the C++ QLabel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QLabel that has no cute function yet,
    'resourceProvider', 'setResourceProvider', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QLabel::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#tr

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
    #  QString QLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLabel'

  #  A C++ QLabel Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QLabel::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLabel::text() const
    return self.uglySide.call('ritual_ZNK6QLabel4textEv')

  @overload(Qt.ReturnByValueConstant)
  def pixmap(self, a0: Qt.ReturnByValueConstant) -> QPixmap:
    """
    Calls Qt's 'QPixmap QLabel::pixmap(Qt::ReturnByValueConstant a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#pixmap

    Parameters
    ----------

    a0 : Qt.ReturnByValueConstant
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QLabel::pixmap(Qt::ReturnByValueConstant a0) const
    address = self.uglySide.call(
        'ritual_ZNK6QLabel6pixmapEN2Qt21ReturnByValueConstantE', a0.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload()
  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QLabel::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QLabel::pixmap() const
    address = self.uglySide.call('ritual_ZNK6QLabel6pixmapEv')
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(Qt.ReturnByValueConstant)
  def picture(self, a0: Qt.ReturnByValueConstant) -> QPicture:
    """
    Calls Qt's 'QPicture QLabel::picture(Qt::ReturnByValueConstant a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#picture

    Parameters
    ----------

    a0 : Qt.ReturnByValueConstant
      Passed on as its number.

    Returns
    -------

    QPicture
      A new cute QPicture around the copy Qt gave back. Python owns it.
    """
    #  QPicture QLabel::picture(Qt::ReturnByValueConstant a0) const
    address = self.uglySide.call(
        'ritual_ZNK6QLabel7pictureEN2Qt21ReturnByValueConstantE', a0.value,
    )
    from ..QtGui import QPicture
    return QPicture._cuteOwning(address)

  @overload()
  def picture(self) -> QPicture:
    """
    Calls Qt's 'QPicture QLabel::picture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#picture

    Returns
    -------

    QPicture
      A new cute QPicture around the copy Qt gave back. Python owns it.
    """
    #  QPicture QLabel::picture() const
    address = self.uglySide.call('ritual_ZNK6QLabel7pictureEv')
    from ..QtGui import QPicture
    return QPicture._cuteOwning(address)

  def movie(self) -> Optional[QMovie]:
    """
    Calls Qt's 'QMovie *QLabel::movie() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#movie

    Returns
    -------

    Optional[QMovie]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMovie *QLabel::movie() const
    address = self.uglySide.call('ritual_ZNK6QLabel5movieEv')
    from ..QtGui import QMovie
    return QMovie._cuteAt(address)

  def textFormat(self) -> Qt.TextFormat:
    """
    Calls Qt's 'Qt::TextFormat QLabel::textFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#textFormat

    Returns
    -------

    Qt.TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextFormat(number)'
      gives.
    """
    #  Qt::TextFormat QLabel::textFormat() const
    return Qt.TextFormat(self.uglySide.call(
        'ritual_ZNK6QLabel10textFormatEv',
    ))

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QLabel::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QLabel::alignment() const
    return Qt.Alignment(self.uglySide.call('ritual_ZNK6QLabel9alignmentEv'))

  def wordWrap(self) -> bool:
    """
    Calls Qt's 'bool QLabel::wordWrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#wordWrap
    """
    #  bool QLabel::wordWrap() const
    return self.uglySide.call('ritual_ZNK6QLabel8wordWrapEv')

  def indent(self) -> int:
    """
    Calls Qt's 'int QLabel::indent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#indent
    """
    #  int QLabel::indent() const
    return self.uglySide.call('ritual_ZNK6QLabel6indentEv')

  def margin(self) -> int:
    """
    Calls Qt's 'int QLabel::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#margin
    """
    #  int QLabel::margin() const
    return self.uglySide.call('ritual_ZNK6QLabel6marginEv')

  def hasScaledContents(self) -> bool:
    """
    Calls Qt's 'bool QLabel::hasScaledContents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#hasScaledContents
    """
    #  bool QLabel::hasScaledContents() const
    return self.uglySide.call('ritual_ZNK6QLabel17hasScaledContentsEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLabel::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLabel::sizeHint() const
    ritual = 'ritual_ZNK6QLabel8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QLabel8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLabel::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLabel::minimumSizeHint() const
    ritual = 'ritual_ZNK6QLabel15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QLabel15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def buddy(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QLabel::buddy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#buddy

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QLabel::buddy() const
    address = self.uglySide.call('ritual_ZNK6QLabel5buddyEv')
    return QWidget._cuteAt(address)

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QLabel::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QLabel::heightForWidth(int a0) const
    ritual = 'ritual_ZNK6QLabel14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QLabel14heightForWidthEi'
    return self.uglySide.call(ritual, a0)

  def openExternalLinks(self) -> bool:
    """
    Calls Qt's 'bool QLabel::openExternalLinks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#openExternalLinks
    """
    #  bool QLabel::openExternalLinks() const
    return self.uglySide.call('ritual_ZNK6QLabel17openExternalLinksEv')

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags QLabel::textInteractionFlags()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QLabel::textInteractionFlags() const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK6QLabel20textInteractionFlagsEv',
    ))

  def hasSelectedText(self) -> bool:
    """
    Calls Qt's 'bool QLabel::hasSelectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#hasSelectedText
    """
    #  bool QLabel::hasSelectedText() const
    return self.uglySide.call('ritual_ZNK6QLabel15hasSelectedTextEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QLabel::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLabel::selectedText() const
    return self.uglySide.call('ritual_ZNK6QLabel12selectedTextEv')

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QLabel::selectionStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#selectionStart
    """
    #  int QLabel::selectionStart() const
    return self.uglySide.call('ritual_ZNK6QLabel14selectionStartEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.TextFormat)
  def setTextFormat(self, a0: Qt.TextFormat) -> None:
    """
    Calls Qt's 'void QLabel::setTextFormat(Qt::TextFormat a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setTextFormat

    Parameters
    ----------

    a0 : Qt.TextFormat
      Passed on as its number.
    """
    #  void QLabel::setTextFormat(Qt::TextFormat a0)
    self.uglySide.call(
        'ritual_ZN6QLabel13setTextFormatEN2Qt10TextFormatE', a0.value,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, a0: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QLabel::setAlignment(Qt::Alignment a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setAlignment

    Parameters
    ----------

    a0 : Qt.Alignment
      Passed on as its number.
    """
    #  void QLabel::setAlignment(Qt::Alignment a0)
    self.uglySide.call(
        'ritual_ZN6QLabel12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        a0.value,
    )

  @overload(bool)
  def setWordWrap(self, on: bool) -> None:
    """
    Calls Qt's 'void QLabel::setWordWrap(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setWordWrap

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QLabel::setWordWrap(bool on)
    self.uglySide.call('ritual_ZN6QLabel11setWordWrapEb', on)

  @overload(int)
  def setIndent(self, a0: int) -> None:
    """
    Calls Qt's 'void QLabel::setIndent(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setIndent

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLabel::setIndent(int a0)
    self.uglySide.call('ritual_ZN6QLabel9setIndentEi', a0)

  @overload(int)
  def setMargin(self, a0: int) -> None:
    """
    Calls Qt's 'void QLabel::setMargin(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setMargin

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLabel::setMargin(int a0)
    self.uglySide.call('ritual_ZN6QLabel9setMarginEi', a0)

  @overload(bool)
  def setScaledContents(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLabel::setScaledContents(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setScaledContents

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLabel::setScaledContents(bool a0)
    self.uglySide.call('ritual_ZN6QLabel17setScaledContentsEb', a0)

  @overload(QWidget)
  @overload(NoneType)
  def setBuddy(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLabel::setBuddy(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setBuddy

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::setBuddy(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN6QLabel8setBuddyEP7QWidget', self._addressOf(a0),
    )

  @overload(bool)
  def setOpenExternalLinks(self, open: bool) -> None:
    """
    Calls Qt's 'void QLabel::setOpenExternalLinks(bool open)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setOpenExternalLinks

    Parameters
    ----------

    open : bool
      Passed on as it is.
    """
    #  void QLabel::setOpenExternalLinks(bool open)
    self.uglySide.call('ritual_ZN6QLabel20setOpenExternalLinksEb', open)

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void QLabel::setTextInteractionFlags(Qt::TextInteractionFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabel.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QLabel::setTextInteractionFlags(Qt::TextInteractionFlags flags)
    self.uglySide.call(
        'ritual_ZN6QLabel23setTextInteractionFlagsE6QFlagsIN2Qt19TextIntera'
        'ctionFlagEE',
        flags.value,
    )

  @overload(int, int)
  def setSelection(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QLabel::setSelection(int a0, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setSelection

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QLabel::setSelection(int a0, int a1)
    self.uglySide.call('ritual_ZN6QLabel12setSelectionEii', a0, a1)

  @overload(str)
  def setText(self, a0: str) -> None:
    """
    Calls Qt's 'void QLabel::setText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLabel::setText(const QString &a0)
    self.uglySide.call('ritual_ZN6QLabel7setTextERK7QString', a0)

  @overload(QPixmap)
  def setPixmap(self, a0: QPixmap) -> None:
    """
    Calls Qt's 'void QLabel::setPixmap(const QPixmap &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setPixmap

    Parameters
    ----------

    a0 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QLabel::setPixmap(const QPixmap &a0)
    self.uglySide.call(
        'ritual_ZN6QLabel9setPixmapERK7QPixmap', self._valueOf(a0),
    )

  @overload(QPicture)
  def setPicture(self, a0: QPicture) -> None:
    """
    Calls Qt's 'void QLabel::setPicture(const QPicture &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setPicture

    Parameters
    ----------

    a0 : QPicture
      Passed on as a value: Qt reads the C++ QPicture, which stays Python's
      own.
    """
    #  void QLabel::setPicture(const QPicture &a0)
    self.uglySide.call(
        'ritual_ZN6QLabel10setPictureERK8QPicture', self._valueOf(a0),
    )

  @overload(QMovie)
  @overload(NoneType)
  def setMovie(self, movie: Optional[QMovie]) -> None:
    """
    Calls Qt's 'void QLabel::setMovie(QMovie *movie)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setMovie

    Parameters
    ----------

    movie : Optional[QMovie]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::setMovie(QMovie *movie)
    self.uglySide.call(
        'ritual_ZN6QLabel8setMovieEP6QMovie', self._addressOf(movie),
    )

  @overload(int)
  def setNum(self, a0: int) -> None:
    """
    Calls Qt's 'void QLabel::setNum(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setNum

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLabel::setNum(int a0)
    self.uglySide.call('ritual_ZN6QLabel6setNumEi', a0)

  @overload(float)
  def setNum(self, a0: float) -> None:
    """
    Calls Qt's 'void QLabel::setNum(double a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#setNum

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QLabel::setNum(double a0)
    self.uglySide.call('ritual_ZN6QLabel6setNumEd', a0)

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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QLabel::QLabel(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#QLabel

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QLabel::QLabel(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QLabel, lambda: Rituals.call(
        'ritual_ZN6QLabelC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  @overload(str, QWidget, Qt.WindowFlags)
  @overload(str, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      text: str,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QLabel::QLabel(const QString &text,
    QWidget *parent, Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#QLabel

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QLabel::QLabel(const QString &text, QWidget *parent, Qt::WindowFlags
    #      f)
    self._noteCreation(QLabel, lambda: Rituals.call(
        'ritual_ZN6QLabelC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        text, self._addressOf(parent), f.value,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QLabel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#clear
    """
    #  void QLabel::clear()
    self.uglySide.call('ritual_ZN6QLabel5clearEv')

  @overload(str)
  def linkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QLabel::linkActivated(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#linkActivated

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLabel::linkActivated(const QString &link)
    self.uglySide.call('ritual_ZN6QLabel13linkActivatedERK7QString', link)

  @overload(str)
  def linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QLabel::linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLabel::linkHovered(const QString &link)
    self.uglySide.call('ritual_ZN6QLabel11linkHoveredERK7QString', link)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QLabel::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLabel::event(QEvent *e)
    ritual = 'ritual_ZN6QLabel5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QLabel::keyPressEvent(QKeyEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#keyPressEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::keyPressEvent(QKeyEvent *ev)
    ritual = 'ritual_ZN6QLabel13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QLabel::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN6QLabel10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QLabel::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN6QLabel11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QLabel::mousePressEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#mousePressEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::mousePressEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN6QLabel15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QLabel::mouseMoveEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#mouseMoveEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::mouseMoveEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN6QLabel14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QLabel::mouseReleaseEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#mouseReleaseEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::mouseReleaseEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN6QLabel17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, ev: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QLabel::contextMenuEvent(QContextMenuEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#contextMenuEvent

    Parameters
    ----------

    ev : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::contextMenuEvent(QContextMenuEvent *ev)
    ritual = 'ritual_ZN6QLabel16contextMenuEventEP17QContextMenuEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel16contextMenuEventEP17QContextMenuEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, ev: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QLabel::focusInEvent(QFocusEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#focusInEvent

    Parameters
    ----------

    ev : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::focusInEvent(QFocusEvent *ev)
    ritual = 'ritual_ZN6QLabel12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, ev: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QLabel::focusOutEvent(QFocusEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#focusOutEvent

    Parameters
    ----------

    ev : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabel::focusOutEvent(QFocusEvent *ev)
    ritual = 'ritual_ZN6QLabel13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QLabel::focusNextPrevChild(bool next)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QLabel::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN6QLabel18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QLabel18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  def d_func(self) -> Optional[QLabelPrivate]:
    """
    Calls Qt's 'QLabelPrivate *QLabel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabel.html#d_func

    Returns
    -------

    Optional[QLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLabelPrivate *QLabel::d_func()
    address = self.uglySide.call('ritual_ZN6QLabel6d_funcEv')
    from . import QLabelPrivate
    return QLabelPrivate._cuteAt(address)

  @staticmethod
  def resourceProvider(*__, **_) -> Never:
    """
    Qt's 'QTextDocument::ResourceProvider QLabel::resourceProvider() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLabel.resourceProvider' has no cute function yet. Qt's "
        "'QTextDocument::ResourceProvider QLabel::resourceProvider() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setResourceProvider(*__, **_) -> Never:
    """
    Qt's 'void QLabel::setResourceProvider(const
    QTextDocument::ResourceProvider &provider)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QLabel.setResourceProvider' has no cute function yet. Qt's 'void "
        "QLabel::setResourceProvider(const QTextDocument::ResourceProvider "
        "&provider)': takes a type Python has no way to hand over yet.")
