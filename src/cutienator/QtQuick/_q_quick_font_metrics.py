"""
QQuickFontMetrics binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickfontmetrics_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFontMetrics to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontMetrics(QObject):
  """
  The cute side of Qt's QQuickFontMetrics: a plain Python object standing in
  front of one C++ QQuickFontMetrics.

  It is built on the cute 'QObject', as Qt's QQuickFontMetrics is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontMetrics that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'ascent', 'descent', 'capitalHeight', 'height', 'leading', 'lineSpacing',
  'minimumLeftBearing', 'minimumRightBearing', 'maximumCharacterWidth',
  'xHeight', 'averageCharacterWidth', 'underlinePosition',
  'overlinePosition', 'strikeOutPosition', 'lineWidth', 'advanceWidth',
  'boundingRect', 'tightBoundingRect', 'elidedText', 'fontChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontMetrics::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFontMetrics::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFontMetrics is created at the first use, not by
    'QQuickFontMetrics(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontMetrics.
  - Qt tells when it has removed the C++ QQuickFontMetrics. Every call on the
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
    Calls Qt's 'QString QQuickFontMetrics::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#tr

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
    #  QString QQuickFontMetrics::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickFontMetrics2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontMetrics'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontMetrics::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontMetrics::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontMetrics::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontMetrics::font() const
    address = self.uglySide.call('ritual_ZNK17QQuickFontMetrics4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#ascent
    """
    #  qreal QQuickFontMetrics::ascent() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics6ascentEv')

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#descent
    """
    #  qreal QQuickFontMetrics::descent() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics7descentEv')

  def capitalHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::capitalHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#capitalHeight
    """
    #  qreal QQuickFontMetrics::capitalHeight() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics13capitalHeightEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#height
    """
    #  qreal QQuickFontMetrics::height() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics6heightEv')

  def leading(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#leading
    """
    #  qreal QQuickFontMetrics::leading() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics7leadingEv')

  def lineSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::lineSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#lineSpacing
    """
    #  qreal QQuickFontMetrics::lineSpacing() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics11lineSpacingEv')

  def minimumLeftBearing(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::minimumLeftBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#minimumLeftBearing
    """
    #  qreal QQuickFontMetrics::minimumLeftBearing() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics18minimumLeftBearingEv',
    )

  def minimumRightBearing(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::minimumRightBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#minimumRightBearing
    """
    #  qreal QQuickFontMetrics::minimumRightBearing() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics19minimumRightBearingEv',
    )

  def maximumCharacterWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::maximumCharacterWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#maximumCharacterWidth
    """
    #  qreal QQuickFontMetrics::maximumCharacterWidth() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics21maximumCharacterWidthEv',
    )

  def xHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#xHeight
    """
    #  qreal QQuickFontMetrics::xHeight() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics7xHeightEv')

  def averageCharacterWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::averageCharacterWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#averageCharacterWidth
    """
    #  qreal QQuickFontMetrics::averageCharacterWidth() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics21averageCharacterWidthEv',
    )

  def underlinePosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::underlinePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#underlinePosition
    """
    #  qreal QQuickFontMetrics::underlinePosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics17underlinePositionEv',
    )

  def overlinePosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::overlinePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#overlinePosition
    """
    #  qreal QQuickFontMetrics::overlinePosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics16overlinePositionEv',
    )

  def strikeOutPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::strikeOutPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#strikeOutPosition
    """
    #  qreal QQuickFontMetrics::strikeOutPosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics17strikeOutPositionEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#lineWidth
    """
    #  qreal QQuickFontMetrics::lineWidth() const
    return self.uglySide.call('ritual_ZNK17QQuickFontMetrics9lineWidthEv')

  @overload(str)
  def advanceWidth(self, text: str) -> float:
    """
    Calls Qt's 'qreal QQuickFontMetrics::advanceWidth(const QString &text)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#advanceWidth

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qreal QQuickFontMetrics::advanceWidth(const QString &text) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics12advanceWidthERK7QString', text,
    )

  @overload(str)
  def boundingRect(self, text: str) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickFontMetrics::boundingRect(const QString &text)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#boundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickFontMetrics::boundingRect(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics12boundingRectERK7QString', text,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str)
  def tightBoundingRect(self, text: str) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickFontMetrics::tightBoundingRect(const QString
    &text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#tightBoundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickFontMetrics::tightBoundingRect(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics17tightBoundingRectERK7QString', text,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, Qt.TextElideMode, float)
  @overload(str, Qt.TextElideMode, float, int)
  def elidedText(
      self,
      text: str,
      mode: Qt.TextElideMode,
      width: float,
      flags: int = 0,
  ) -> str:
    """
    Calls Qt's 'QString QQuickFontMetrics::elidedText(const QString &text,
    Qt::TextElideMode mode, qreal width, int flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#elidedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    mode : Qt.TextElideMode
      Passed on as its number.

    width : float
      Passed on as it is.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontMetrics::elidedText(const QString &text,
    #      Qt::TextElideMode mode, qreal width, int flags) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickFontMetrics10elidedTextERK7QStringN2Qt13TextElid'
        'eModeEdi',
        text, mode.value, width, flags,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontMetrics::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontMetrics::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN17QQuickFontMetrics7setFontERK5QFont', self._valueOf(font),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFontMetrics::QQuickFontMetrics(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontmetrics.html#QQuickFontMetrics

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontMetrics::QQuickFontMetrics(QObject *parent)
    self._noteCreation(QQuickFontMetrics, lambda: Rituals.call(
        'ritual_ZN17QQuickFontMetricsC1EP7QObject',
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

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontMetrics::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontmetrics.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontMetrics::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN17QQuickFontMetrics11fontChangedERK5QFont',
        self._valueOf(font),
    )
