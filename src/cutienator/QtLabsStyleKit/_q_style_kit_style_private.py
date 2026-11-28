"""
QStyleKitStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qstylekitstyle_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QStyleKitStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtWidgets import QCommonStylePrivate, QStyle
from . import QQSK, QQStyleKitReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QObject, QRect, QRectF, QSize
  from ..QtGui import QFont, QPainter, QPalette
  from ..QtWidgets import QWidget
  from . import QQStyleKitDelegateProperties, QQStyleKitImageProperties
  from . import QQStyleKitStyle, QStyleKitStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QMargins = WAIT['QMargins']
  QObject = WAIT['QObject']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QQStyleKitDelegateProperties = WAIT['QQStyleKitDelegateProperties']
  QQStyleKitImageProperties = WAIT['QQStyleKitImageProperties']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleKitStylePrivate(QCommonStylePrivate):
  """
  The cute side of Qt's QStyleKitStylePrivate: a plain Python object standing
  in front of one C++ QStyleKitStylePrivate.

  It is built on the cute 'QCommonStylePrivate', as Qt's
  QStyleKitStylePrivate is built on Qt's QCommonStylePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleKitStylePrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'effectiveStyle',
  'unsetStyleFont', 'setStyleFont', 'unsetStylePalette', 'setStylePalette',
  'cleanupWidgetReader', 'onWidgetDestroyed', 'ensureSharedReader',
  'ensureSubElementReader', 'cleanupSubElements', 'clearAllSubElements',
  'resolvedStateFor', 'clearMetricsCache', 'drawStyledItemContents',
  'drawStyledItemImage', 'getAlignedRectInContainer'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStyleKitStyle *QStyleKitStylePrivate::q_func() const': takes
    in Python what 'QStyleKitStyle *QStyleKitStylePrivate::q_func()' takes.
  - Qt's 'SubElementKey QStyleKitStylePrivate::subElementKeyForOption(const
    QStyleOption *opt, const QWidget *widget)': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  15 of the 35 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QStyleKitStylePrivate; 3 leans on 'QQStyleKitDelegateProperties*
  QQStyleKitPropertyGroup; 1 leans on 'QQStyleKitIndicatorProperties.

  What to expect
  --------------

  - The C++ QStyleKitStylePrivate is created at the first use, not by
    'QStyleKitStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleKitStylePrivate.
  - Each name of Qt's QStyleKitStylePrivate that has no cute function yet,
    'drawControlIndicator', 'drawControlText', 'drawStyledItemRect',
    'ensureDefaultStyle', 'loadStyle', 'metricsFor', 'metricsForReader',
    'readerForWidget', 'refreshStyleFont', 'refreshStylePalette', 'resolve',
    'resolveLayout', 'resolveSubElement', 'startSubElementTransition',
    'subElementKeyForOption', 'updateStyle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleKitStylePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def effectiveStyle(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QStyleKitStylePrivate::effectiveStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#effectiveStyle

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QStyleKitStylePrivate::effectiveStyle() const
    address = self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate14effectiveStyleEv',
    )
    from . import QQStyleKitStyle
    return QQStyleKitStyle._cuteAt(address)

  def ensureSharedReader(self) -> Optional[QQStyleKitReader]:
    """
    Calls Qt's 'QQStyleKitReader *QStyleKitStylePrivate::ensureSharedReader()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#ensureSharedReader

    Returns
    -------

    Optional[QQStyleKitReader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitReader *QStyleKitStylePrivate::ensureSharedReader() const
    address = self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate18ensureSharedReaderEv',
    )
    return QQStyleKitReader._cuteAt(address)

  def ensureSubElementReader(self) -> Optional[QQStyleKitReader]:
    """
    Calls Qt's 'QQStyleKitReader
    *QStyleKitStylePrivate::ensureSubElementReader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#ensureSubElementReader

    Returns
    -------

    Optional[QQStyleKitReader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitReader *QStyleKitStylePrivate::ensureSubElementReader()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate22ensureSubElementReaderEv',
    )
    return QQStyleKitReader._cuteAt(address)

  @overload(QQStyleKitReader.ControlType, QStyle.State)
  @overload(QQStyleKitReader.ControlType, QStyle.State, QWidget)
  @overload(QQStyleKitReader.ControlType, QStyle.State, NoneType)
  def resolvedStateFor(
      self,
      type: QQStyleKitReader.ControlType,
      state: QStyle.State,
      widget: Optional[QWidget] = None,
  ) -> QQSK.State:
    """
    Calls Qt's 'QQSK::State
    QStyleKitStylePrivate::resolvedStateFor(QQStyleKitReader::ControlType
    type, QStyle::State state, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#resolvedStateFor

    Parameters
    ----------

    type : QQStyleKitReader.ControlType
      Passed on as its number.

    state : QStyle.State
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QQSK.State
      The value standing for the combination Qt gave back.
    """
    #  QQSK::State QStyleKitStylePrivate::resolvedStateFor(QQStyleKitReader::
    #      ControlType type, QStyle::State state, const QWidget *widget)
    #      const
    return QQSK.State(self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate16resolvedStateForEN16QQStyleKitR'
        'eader11ControlTypeE6QFlagsIN6QStyle9StateFlagEEPK7QWidget',
        type.value, state.value, self._addressOf(widget),
    ))

  @overload(QRect, QSize, int, QMargins, QMargins)
  def getAlignedRectInContainer(
      self,
      container: QRect,
      indicatorSize: QSize,
      alignment: int,
      padding: QMargins,
      indicatorMargins: QMargins,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyleKitStylePrivate::getAlignedRectInContainer(const
    QRect &container, const QSize &indicatorSize, uint alignment, const
    QMargins &padding, const QMargins &indicatorMargins) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html

    Parameters
    ----------

    container : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    indicatorSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    alignment : int
      Passed on as it is.

    padding : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    indicatorMargins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyleKitStylePrivate::getAlignedRectInContainer(const QRect
    #      &container, const QSize &indicatorSize, uint alignment, const
    #      QMargins &padding, const QMargins &indicatorMargins) const
    address = self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate25getAlignedRectInContainerERK5QR'
        'ectRK5QSizejRK8QMarginsS8_',
        self._valueOf(container), self._valueOf(indicatorSize), alignment,
        self._valueOf(padding, 'QMargins'), self._valueOf(indicatorMargins,
        'QMargins'),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, QFont)
  @overload(NoneType, QFont)
  def setStyleFont(
      self,
      widget: Optional[QWidget],
      styleFont: QFont,
  ) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::setStyleFont(QWidget *widget,
    const QFont &styleFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#setStyleFont

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QStyleKitStylePrivate::setStyleFont(QWidget *widget, const QFont
    #      &styleFont)
    self.uglySide.call(
        'ritual_ZN21QStyleKitStylePrivate12setStyleFontEP7QWidgetRK5QFont',
        self._addressOf(widget), self._valueOf(styleFont),
    )

  @overload(QWidget, QPalette)
  @overload(NoneType, QPalette)
  def setStylePalette(
      self,
      widget: Optional[QWidget],
      stylePalette: QPalette,
  ) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::setStylePalette(QWidget *widget,
    const QPalette &stylePalette) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#setStylePalette

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stylePalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QStyleKitStylePrivate::setStylePalette(QWidget *widget, const
    #      QPalette &stylePalette) const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate15setStylePaletteEP7QWidgetRK8QPa'
        'lette',
        self._addressOf(widget), self._valueOf(stylePalette),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QStyleKitStylePrivate::QStyleKitStylePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#QStyleKitStylePrivate
    """
    #  QStyleKitStylePrivate::QStyleKitStylePrivate()
    self._noteCreation(QStyleKitStylePrivate, lambda: Rituals.call(
        'ritual_ZN21QStyleKitStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QStyleKitStyle]:
    """
    Calls Qt's 'QStyleKitStyle *QStyleKitStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyleprivate.html#q_func

    Returns
    -------

    Optional[QStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleKitStyle *QStyleKitStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QStyleKitStylePrivate6q_funcEv')
    from . import QStyleKitStyle
    return QStyleKitStyle._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def unsetStyleFont(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::unsetStyleFont(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#unsetStyleFont

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::unsetStyleFont(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QStyleKitStylePrivate14unsetStyleFontEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def unsetStylePalette(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::unsetStylePalette(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#unsetStylePalette

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::unsetStylePalette(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QStyleKitStylePrivate17unsetStylePaletteEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def cleanupWidgetReader(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::cleanupWidgetReader(const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#cleanupWidgetReader

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::cleanupWidgetReader(const QWidget *widget)
    #      const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate19cleanupWidgetReaderEPK7QWidget',
        self._addressOf(widget),
    )

  @overload(QObject)
  @overload(NoneType)
  def onWidgetDestroyed(self, w: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::onWidgetDestroyed(QObject *w)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#onWidgetDestroyed

    Parameters
    ----------

    w : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::onWidgetDestroyed(QObject *w) const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate17onWidgetDestroyedEP7QObject',
        self._addressOf(w, 'QObject'),
    )

  @overload(QWidget)
  @overload(NoneType)
  def cleanupSubElements(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::cleanupSubElements(const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#cleanupSubElements

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::cleanupSubElements(const QWidget *widget)
    #      const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate18cleanupSubElementsEPK7QWidget',
        self._addressOf(widget),
    )

  def clearAllSubElements(self) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::clearAllSubElements() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#clearAllSubElements
    """
    #  void QStyleKitStylePrivate::clearAllSubElements() const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate19clearAllSubElementsEv',
    )

  def clearMetricsCache(self) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::clearMetricsCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#clearMetricsCache
    """
    #  void QStyleKitStylePrivate::clearMetricsCache()
    self.uglySide.call(
        'ritual_ZN21QStyleKitStylePrivate17clearMetricsCacheEv',
    )

  @overload(QQStyleKitDelegateProperties, QRectF, QPainter)
  @overload(QQStyleKitDelegateProperties, QRectF, NoneType)
  @overload(NoneType, QRectF, QPainter)
  @overload(NoneType, QRectF, NoneType)
  def drawStyledItemContents(
      self,
      a0: Optional[QQStyleKitDelegateProperties],
      rect: QRectF,
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::drawStyledItemContents(const
    QQStyleKitDelegateProperties *a0, const QRectF &rect, QPainter *p)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#drawStyledItemContents

    Parameters
    ----------

    a0 : Optional[QQStyleKitDelegateProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::drawStyledItemContents(const
    #      QQStyleKitDelegateProperties *a0, const QRectF &rect, QPainter *p)
    #      const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate22drawStyledItemContentsEPK28QQSt'
        'yleKitDelegatePropertiesRK6QRectFP8QPainter',
        self._addressOf(a0), self._valueOf(rect), self._addressOf(p),
    )

  @overload(QQStyleKitImageProperties, QRectF, float, QPainter)
  @overload(QQStyleKitImageProperties, QRectF, float, NoneType)
  @overload(NoneType, QRectF, float, QPainter)
  @overload(NoneType, QRectF, float, NoneType)
  def drawStyledItemImage(
      self,
      image: Optional[QQStyleKitImageProperties],
      rect: QRectF,
      opacity: float,
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QStyleKitStylePrivate::drawStyledItemImage(const
    QQStyleKitImageProperties *image, const QRectF &rect, qreal opacity,
    QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyleprivate.html#drawStyledItemImage

    Parameters
    ----------

    image : Optional[QQStyleKitImageProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    opacity : float
      Passed on as it is.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStylePrivate::drawStyledItemImage(const
    #      QQStyleKitImageProperties *image, const QRectF &rect, qreal
    #      opacity, QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK21QStyleKitStylePrivate19drawStyledItemImageEPK25QQStyle'
        'KitImagePropertiesRK6QRectFdP8QPainter',
        self._addressOf(image), self._valueOf(rect), opacity,
        self._addressOf(p),
    )

  @staticmethod
  def drawControlIndicator(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::drawControlIndicator(const
    QQStyleKitDelegateProperties *indicator, const QRectF &rect, QPainter *p)
    const': leans on 'QQStyleKitIndicatorProperties::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.drawControlIndicator' has no cute function "
        "yet. Qt's 'void QStyleKitStylePrivate::drawControlIndicator(const "
        "QQStyleKitDelegateProperties *indicator, const QRectF &rect, "
        "QPainter *p) const': leans on "
        "'QQStyleKitIndicatorProperties::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def drawControlText(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::drawControlText(const
    QQStyleKitTextProperties *textProps, const QFont &font, const QRect
    &rect, const QString &text, uint textFlags, QPainter *p, Qt::Alignment
    defaultAlignment) const': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'resolvedAlignment'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.drawControlText' has no cute function yet. "
        "Qt's 'void QStyleKitStylePrivate::drawControlText(const "
        "QQStyleKitTextProperties *textProps, const QFont &font, const "
        "QRect &rect, const QString &text, uint textFlags, QPainter *p, "
        "Qt::Alignment defaultAlignment) const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'resolvedAlignment'.")

  @staticmethod
  def drawStyledItemRect(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::drawStyledItemRect(const
    QQStyleKitDelegateProperties *a0, const QRectF &rect, QPainter *p)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'applyDelegateTransform'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.drawStyledItemRect' has no cute function "
        "yet. Qt's 'void QStyleKitStylePrivate::drawStyledItemRect(const "
        "QQStyleKitDelegateProperties *a0, const QRectF &rect, QPainter *p) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'applyDelegateTransform'.")

  @staticmethod
  def ensureDefaultStyle(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitStyle *QStyleKitStylePrivate::ensureDefaultStyle()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcStyleKit'; did you mean
    'QQStyleKit'?.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.ensureDefaultStyle' has no cute function "
        "yet. Qt's 'QQStyleKitStyle "
        "*QStyleKitStylePrivate::ensureDefaultStyle()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcStyleKit'; did you mean "
        "'QQStyleKit'?.")

  @staticmethod
  def loadStyle(*__, **_) -> Never:
    """
    Qt's 'bool QStyleKitStylePrivate::loadStyle()': leans on
    'QStyleKitStylePrivate::refreshStyleFont(QWidget*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.loadStyle' has no cute function yet. Qt's "
        "'bool QStyleKitStylePrivate::loadStyle()': leans on "
        "'QStyleKitStylePrivate::refreshStyleFont(QWidget*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def metricsFor(*__, **_) -> Never:
    """
    Qt's 'const ControlMetrics
    &QStyleKitStylePrivate::metricsFor(QQStyleKitReader::ControlType type,
    QQSK::State state) const': leans on 'QQStyleKitDelegateProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperties>(
    QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.metricsFor' has no cute function yet. Qt's "
        "'const ControlMetrics "
        "&QStyleKitStylePrivate::metricsFor(QQStyleKitReader::ControlType "
        "type, QQSK::State state) const': leans on "
        "'QQStyleKitDelegateProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperti"
        "es>(QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def metricsForReader(*__, **_) -> Never:
    """
    Qt's 'ControlMetrics
    QStyleKitStylePrivate::metricsForReader(QQStyleKitReader *reader) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'elementMargins'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.metricsForReader' has no cute function yet. "
        "Qt's 'ControlMetrics "
        "QStyleKitStylePrivate::metricsForReader(QQStyleKitReader *reader) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'elementMargins'.")

  @staticmethod
  def readerForWidget(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitReader *QStyleKitStylePrivate::readerForWidget(const
    QWidget *widget) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'controlTypeForWidget'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.readerForWidget' has no cute function yet. "
        "Qt's 'QQStyleKitReader "
        "*QStyleKitStylePrivate::readerForWidget(const QWidget *widget) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'controlTypeForWidget'.")

  @staticmethod
  def refreshStyleFont(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::refreshStyleFont(QWidget *widget)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'controlTypeForWidget'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.refreshStyleFont' has no cute function yet. "
        "Qt's 'void QStyleKitStylePrivate::refreshStyleFont(QWidget "
        "*widget)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'controlTypeForWidget'.")

  @staticmethod
  def refreshStylePalette(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::refreshStylePalette(QWidget *widget)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'containerWidget'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.refreshStylePalette' has no cute function "
        "yet. Qt's 'void QStyleKitStylePrivate::refreshStylePalette(QWidget "
        "*widget)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'containerWidget'.")

  @staticmethod
  def resolve(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitResolved QStyleKitStylePrivate::resolve(const QWidget *w,
    QQStyleKitReader::ControlType type, QStyle::State state) const': leans on
    'QStyleKitStylePrivate::readerForWidget(QWidget const*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.resolve' has no cute function yet. Qt's "
        "'QQStyleKitResolved QStyleKitStylePrivate::resolve(const QWidget "
        "*w, QQStyleKitReader::ControlType type, QStyle::State state) "
        "const': leans on 'QStyleKitStylePrivate::readerForWidget(QWidget "
        "const*) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def resolveLayout(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitLayoutResolved
    QStyleKitStylePrivate::resolveLayout(QQStyleKitReader::ControlType type,
    QStyle::State state) const': leans on 'QQStyleKitDelegateProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperties>(
    QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.resolveLayout' has no cute function yet. "
        "Qt's 'QQStyleKitLayoutResolved "
        "QStyleKitStylePrivate::resolveLayout(QQStyleKitReader::ControlType "
        "type, QStyle::State state) const': leans on "
        "'QQStyleKitDelegateProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperti"
        "es>(QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def resolveSubElement(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitResolved QStyleKitStylePrivate::resolveSubElement(const
    QWidget *w, const QStyleOption *opt, QQStyleKitReader::ControlType type,
    QStyle::State state, bool track) const': leans on
    'QQStyleKitDelegateProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperties>(
    QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.resolveSubElement' has no cute function "
        "yet. Qt's 'QQStyleKitResolved "
        "QStyleKitStylePrivate::resolveSubElement(const QWidget *w, const "
        "QStyleOption *opt, QQStyleKitReader::ControlType type, "
        "QStyle::State state, bool track) const': leans on "
        "'QQStyleKitDelegateProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperti"
        "es>(QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def startSubElementTransition(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitReader
    *QStyleKitStylePrivate::startSubElementTransition(const SubElementKey
    &key, QQStyleKitReader::ControlType type, QQSK::State fromState,
    QQSK::State toState, QQuickTransition *transition) const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'paintTarget'.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.startSubElementTransition' has no cute "
        "function yet. Qt's 'QQStyleKitReader "
        "*QStyleKitStylePrivate::startSubElementTransition(const "
        "SubElementKey &key, QQStyleKitReader::ControlType type, "
        "QQSK::State fromState, QQSK::State toState, QQuickTransition "
        "*transition) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'paintTarget'.")

  @staticmethod
  def subElementKeyForOption(*__, **_) -> Never:
    """
    Qt's 'SubElementKey QStyleKitStylePrivate::subElementKeyForOption(const
    QStyleOption *opt, const QWidget *widget)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.subElementKeyForOption' has no cute "
        "function yet. Qt's 'SubElementKey "
        "QStyleKitStylePrivate::subElementKeyForOption(const QStyleOption "
        "*opt, const QWidget *widget)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def updateStyle(*__, **_) -> Never:
    """
    Qt's 'void QStyleKitStylePrivate::updateStyle()': leans on
    'QStyleKitStylePrivate::refreshStyleFont(QWidget*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QStyleKitStylePrivate.updateStyle' has no cute function yet. Qt's "
        "'void QStyleKitStylePrivate::updateStyle()': leans on "
        "'QStyleKitStylePrivate::refreshStyleFont(QWidget*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
