"""
QSplashScreen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsplashscreen.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QColor
from ..QtCore import QMetaObject
from ..QtGui import QPixmap
from ..QtGui import QScreen
from ._q_widget import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplashScreen(QWidget):
  """
  The cute side of Qt's QSplashScreen: a plain Python object standing in
  front of one C++ QSplashScreen.

  It is built on the cute 'QWidget', as Qt's QSplashScreen is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplashScreen that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'setPixmap', 'pixmap',
  'finish', 'repaint', 'message', 'showMessage', 'clearMessage'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSplashScreen::~QSplashScreen()': the destructor: Python never
    removes a C++ QSplashScreen.

  What has no ritual
  ------------------

  12 of the 24 functions Qt declares: 3 private; 3 protected; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QSplashScreen is created at the first use, not by
    'QSplashScreen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplashScreen.
  - Qt tells when it has removed the C++ QSplashScreen. Every call on the
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
    Calls Qt's 'QString QSplashScreen::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#tr

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
    #  QString QSplashScreen::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSplashScreen2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplashScreen'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSplashScreen::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplashScreen::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSplashScreen10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'const QPixmap QSplashScreen::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  const QPixmap QSplashScreen::pixmap() const
    address = self.uglySide.call('ritual_ZNK13QSplashScreen6pixmapEv')
    return QPixmap._cuteOwning(address)

  def message(self) -> str:
    """
    Calls Qt's 'QString QSplashScreen::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSplashScreen::message() const
    return self.uglySide.call('ritual_ZNK13QSplashScreen7messageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPixmap)
  def setPixmap(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QSplashScreen::setPixmap(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#setPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QSplashScreen::setPixmap(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN13QSplashScreen9setPixmapERK7QPixmap',
        self._valueOf(pixmap),
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
  @overload(QPixmap)
  @overload(QPixmap, Qt.WindowFlags)
  def __init__(
      self,
      pixmap: Optional[QPixmap] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QSplashScreen::QSplashScreen(const
    QPixmap &pixmap, Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#QSplashScreen

    Parameters
    ----------

    pixmap : Optional[QPixmap]
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own. May be left out, as in Qt: a new 'QPixmap()' is then passed on.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QSplashScreen::QSplashScreen(const QPixmap &pixmap, Qt::WindowFlags f)
    if pixmap is None:
      pixmap = QPixmap()
    self._noteCreation(QSplashScreen, lambda: Rituals.call(
        'ritual_ZN13QSplashScreenC1ERK7QPixmap6QFlagsIN2Qt10WindowTypeEE',
        self._valueOf(pixmap), f.value,
    ))

  @overload(QScreen)
  @overload(NoneType)
  @overload(QScreen, QPixmap)
  @overload(NoneType, QPixmap)
  @overload(QScreen, QPixmap, Qt.WindowFlags)
  @overload(NoneType, QPixmap, Qt.WindowFlags)
  def __init__(
      self,
      screen: Optional[QScreen],
      pixmap: Optional[QPixmap] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QSplashScreen::QSplashScreen(QScreen
    *screen, const QPixmap &pixmap, Qt::WindowFlags f)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#QSplashScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pixmap : Optional[QPixmap]
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own. May be left out, as in Qt: a new 'QPixmap()' is then passed on.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QSplashScreen::QSplashScreen(QScreen *screen, const QPixmap &pixmap,
    #      Qt::WindowFlags f)
    if pixmap is None:
      pixmap = QPixmap()
    self._noteCreation(QSplashScreen, lambda: Rituals.call(
        'ritual_ZN13QSplashScreenC1EP7QScreenRK7QPixmap6QFlagsIN2Qt10Window'
        'TypeEE',
        self._addressOf(screen), self._valueOf(pixmap), f.value,
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

  @overload(QWidget)
  @overload(NoneType)
  def finish(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QSplashScreen::finish(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#finish

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplashScreen::finish(QWidget *w)
    self.uglySide.call(
        'ritual_ZN13QSplashScreen6finishEP7QWidget', self._addressOf(w),
    )

  def repaint(self) -> None:
    """
    Calls Qt's 'void QSplashScreen::repaint()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#repaint
    """
    #  void QSplashScreen::repaint()
    self.uglySide.call('ritual_ZN13QSplashScreen7repaintEv')

  @overload(str, int, QColor)
  def showMessage(self, message: str, alignment: int, color: QColor) -> None:
    """
    Calls Qt's 'void QSplashScreen::showMessage(const QString &message, int
    alignment, const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#showMessage

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    alignment : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSplashScreen::showMessage(const QString &message, int alignment,
    #      const QColor &color)
    self.uglySide.call(
        'ritual_ZN13QSplashScreen11showMessageERK7QStringiRK6QColor',
        message, alignment, self._valueOf(color),
    )

  def clearMessage(self) -> None:
    """
    Calls Qt's 'void QSplashScreen::clearMessage()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplashscreen.html#clearMessage
    """
    #  void QSplashScreen::clearMessage()
    self.uglySide.call('ritual_ZN13QSplashScreen12clearMessageEv')
