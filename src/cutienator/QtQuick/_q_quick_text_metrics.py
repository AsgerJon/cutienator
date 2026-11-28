"""
QQuickTextMetrics binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextmetrics_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextMetrics to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickText

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


class QQuickTextMetrics(QObject):
  """
  The cute side of Qt's QQuickTextMetrics: a plain Python object standing in
  front of one C++ QQuickTextMetrics.

  It is built on the cute 'QObject', as Qt's QQuickTextMetrics is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextMetrics that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'text', 'setText', 'elide', 'setElide', 'elideWidth', 'setElideWidth',
  'advanceWidth', 'boundingRect', 'width', 'height', 'tightBoundingRect',
  'elidedText', 'renderType', 'setRenderType', 'fontChanged', 'textChanged',
  'elideChanged', 'elideWidthChanged', 'metricsChanged', 'renderTypeChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextMetrics::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTextMetrics::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextMetrics is created at the first use, not by
    'QQuickTextMetrics(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextMetrics.
  - Qt tells when it has removed the C++ QQuickTextMetrics. Every call on the
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
    Calls Qt's 'QString QQuickTextMetrics::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#tr

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
    #  QString QQuickTextMetrics::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickTextMetrics2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextMetrics'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextMetrics::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextMetrics::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextMetrics::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextMetrics::font() const
    address = self.uglySide.call('ritual_ZNK17QQuickTextMetrics4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickTextMetrics::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextMetrics::text() const
    return self.uglySide.call('ritual_ZNK17QQuickTextMetrics4textEv')

  def elide(self) -> Qt.TextElideMode:
    """
    Calls Qt's 'Qt::TextElideMode QQuickTextMetrics::elide() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#elide

    Returns
    -------

    Qt.TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextElideMode(number)'
      gives.
    """
    #  Qt::TextElideMode QQuickTextMetrics::elide() const
    return Qt.TextElideMode(self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics5elideEv',
    ))

  def elideWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextMetrics::elideWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#elideWidth
    """
    #  qreal QQuickTextMetrics::elideWidth() const
    return self.uglySide.call('ritual_ZNK17QQuickTextMetrics10elideWidthEv')

  def advanceWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextMetrics::advanceWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#advanceWidth
    """
    #  qreal QQuickTextMetrics::advanceWidth() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics12advanceWidthEv',
    )

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextMetrics::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextMetrics::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextMetrics::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#width
    """
    #  qreal QQuickTextMetrics::width() const
    return self.uglySide.call('ritual_ZNK17QQuickTextMetrics5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextMetrics::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#height
    """
    #  qreal QQuickTextMetrics::height() const
    return self.uglySide.call('ritual_ZNK17QQuickTextMetrics6heightEv')

  def tightBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextMetrics::tightBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#tightBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextMetrics::tightBoundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics17tightBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def elidedText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextMetrics::elidedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#elidedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextMetrics::elidedText() const
    return self.uglySide.call('ritual_ZNK17QQuickTextMetrics10elidedTextEv')

  def renderType(self) -> QQuickText.RenderType:
    """
    Calls Qt's 'QQuickText::RenderType QQuickTextMetrics::renderType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#renderType

    Returns
    -------

    QQuickText.RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickText.RenderType(number)' gives.
    """
    #  QQuickText::RenderType QQuickTextMetrics::renderType() const
    return QQuickText.RenderType(self.uglySide.call(
        'ritual_ZNK17QQuickTextMetrics10renderTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextMetrics::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN17QQuickTextMetrics7setFontERK5QFont', self._valueOf(font),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextMetrics::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickTextMetrics7setTextERK7QString', text,
    )

  @overload(Qt.TextElideMode)
  def setElide(self, elide: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::setElide(Qt::TextElideMode elide)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#setElide

    Parameters
    ----------

    elide : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QQuickTextMetrics::setElide(Qt::TextElideMode elide)
    self.uglySide.call(
        'ritual_ZN17QQuickTextMetrics8setElideEN2Qt13TextElideModeE',
        elide.value,
    )

  @overload(float)
  def setElideWidth(self, elideWidth: float) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::setElideWidth(qreal elideWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#setElideWidth

    Parameters
    ----------

    elideWidth : float
      Passed on as it is.
    """
    #  void QQuickTextMetrics::setElideWidth(qreal elideWidth)
    self.uglySide.call(
        'ritual_ZN17QQuickTextMetrics13setElideWidthEd', elideWidth,
    )

  @overload(QQuickText.RenderType)
  def setRenderType(self, renderType: QQuickText.RenderType) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::setRenderType(QQuickText::RenderType
    renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#setRenderType

    Parameters
    ----------

    renderType : QQuickText.RenderType
      Passed on as its number.
    """
    #  void QQuickTextMetrics::setRenderType(QQuickText::RenderType
    #      renderType)
    self.uglySide.call(
        'ritual_ZN17QQuickTextMetrics13setRenderTypeEN10QQuickText10RenderT'
        'ypeE',
        renderType.value,
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
    'QQuickTextMetrics::QQuickTextMetrics(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#QQuickTextMetrics

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextMetrics::QQuickTextMetrics(QObject *parent)
    self._noteCreation(QQuickTextMetrics, lambda: Rituals.call(
        'ritual_ZN17QQuickTextMetricsC1EP7QObject',
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

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#fontChanged
    """
    #  void QQuickTextMetrics::fontChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics11fontChangedEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextmetrics.html#textChanged
    """
    #  void QQuickTextMetrics::textChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics11textChangedEv')

  def elideChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::elideChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#elideChanged
    """
    #  void QQuickTextMetrics::elideChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics12elideChangedEv')

  def elideWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::elideWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#elideWidthChanged
    """
    #  void QQuickTextMetrics::elideWidthChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics17elideWidthChangedEv')

  def metricsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::metricsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#metricsChanged
    """
    #  void QQuickTextMetrics::metricsChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics14metricsChangedEv')

  def renderTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextMetrics::renderTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextmetrics.html#renderTypeChanged
    """
    #  void QQuickTextMetrics::renderTypeChanged()
    self.uglySide.call('ritual_ZN17QQuickTextMetrics17renderTypeChangedEv')
