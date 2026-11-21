"""
QToolTip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtooltip.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QRect
  from ..QtGui import QFont, QPalette
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolTip(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QToolTip: a plain Python object standing in front of
  one C++ QToolTip.

  C++ hands a QToolTip around as a copy, so every C++ QToolTip behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QToolTip that has a ritual and that Python can call
  so far, 8 names in all: 'showText', 'hideText', 'isVisible', 'text',
  'palette', 'setPalette', 'font', 'setFont'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolTip::~QToolTip()': the destructor: Python removes its C++
    QToolTip by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QToolTip is created at the first use, not by 'QToolTip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QToolTip back gives a copy the ritual made for
    Python, in a new cute QToolTip.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPoint, str)
  @overload(QPoint, str, QWidget)
  @overload(QPoint, str, NoneType)
  @overload(QPoint, str, QWidget, QRect)
  @overload(QPoint, str, NoneType, QRect)
  @overload(QPoint, str, QWidget, QRect, int)
  @overload(QPoint, str, NoneType, QRect, int)
  def showText(
      pos: QPoint,
      text: str,
      w: Optional[QWidget] = None,
      rect: Optional[QRect] = None,
      msecShowTime: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QToolTip::showText(const QPoint &pos, const QString
    &text, QWidget *w, const QRect &rect, int msecShowTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#showText

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    msecShowTime : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QToolTip::showText(const QPoint &pos, const QString &text,
    #      QWidget *w, const QRect &rect, int msecShowTime)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    Rituals.call(
        'ritual_ZN8QToolTip8showTextERK6QPointRK7QStringP7QWidgetRK5QRecti',
        CuteMixin._valueOf(pos), text, CuteMixin._addressOf(w),
        CuteMixin._valueOf(rect), msecShowTime,
    )

  @staticmethod
  def hideText() -> None:
    """
    Calls Qt's 'void QToolTip::hideText()'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#hideText
    """
    #  void QToolTip::hideText()
    Rituals.call('ritual_ZN8QToolTip8hideTextEv')

  @staticmethod
  def isVisible() -> bool:
    """
    Calls Qt's 'bool QToolTip::isVisible()'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#isVisible
    """
    #  bool QToolTip::isVisible()
    return Rituals.call('ritual_ZN8QToolTip9isVisibleEv')

  @staticmethod
  def text() -> str:
    """
    Calls Qt's 'QString QToolTip::text()'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QToolTip::text()
    return Rituals.call('ritual_ZN8QToolTip4textEv')

  @staticmethod
  def palette() -> QPalette:
    """
    Calls Qt's 'QPalette QToolTip::palette()'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QToolTip::palette()
    address = Rituals.call('ritual_ZN8QToolTip7paletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @staticmethod
  @overload(QPalette)
  def setPalette(a0: QPalette) -> None:
    """
    Calls Qt's 'void QToolTip::setPalette(const QPalette &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#setPalette

    Parameters
    ----------

    a0 : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QToolTip::setPalette(const QPalette &a0)
    Rituals.call(
        'ritual_ZN8QToolTip10setPaletteERK8QPalette', CuteMixin._valueOf(a0),
    )

  @staticmethod
  def font() -> QFont:
    """
    Calls Qt's 'QFont QToolTip::font()'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QToolTip::font()
    address = Rituals.call('ritual_ZN8QToolTip4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(QFont)
  def setFont(a0: QFont) -> None:
    """
    Calls Qt's 'void QToolTip::setFont(const QFont &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtooltip.html#setFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QToolTip::setFont(const QFont &a0)
    Rituals.call(
        'ritual_ZN8QToolTip7setFontERK5QFont', CuteMixin._valueOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolTip'

  #  Qt's '~QToolTip()'. Naming it makes this a value class: Python owns
  #  every C++ QToolTip behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QToolTipD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
