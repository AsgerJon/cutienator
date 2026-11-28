"""
QQStyleKitDelegateProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitDelegateProperties to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQSK, QQStyleKitPropertyGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from . import QQStyleKitBorderProperties, QQStyleKitControlProperties
  from . import QQStyleKitImageProperties, QQStyleKitShadowProperties
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickGradient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQStyleKitControlProperties = WAIT['QQStyleKitControlProperties']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickGradient = WAIT['QQuickGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitDelegateProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitDelegateProperties: a plain Python object
  standing in front of one C++ QQStyleKitDelegateProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitDelegateProperties is built on Qt's QQStyleKitPropertyGroup, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitDelegateProperties that has a ritual and
  that Python can call so far, 87 names in all: 'metaObject', 'tr', 'radius',
  'setRadius', 'topLeftRadius', 'setTopLeftRadius', 'topRightRadius',
  'setTopRightRadius', 'bottomLeftRadius', 'setBottomLeftRadius',
  'bottomRightRadius', 'setBottomRightRadius', 'scale', 'setScale',
  'rotation', 'setRotation', 'width', 'setWidth', 'height', 'setHeight',
  'minimumWidth', 'setMinimumWidth', 'minimumHeight', 'setMinimumHeight',
  'fillWidth', 'setFillWidth', 'fillHeight', 'setFillHeight', 'margins',
  'setMargins', 'leftMargin', 'setLeftMargin', 'rightMargin',
  'setRightMargin', 'topMargin', 'setTopMargin', 'bottomMargin',
  'setBottomMargin', 'alignment', 'setAlignment', 'opacity', 'setOpacity',
  'color', 'setColor', 'visible', 'setVisible', 'clip', 'setClip',
  'gradient', 'setGradient', 'data', 'setData', 'delegate', 'setDelegate',
  'image', 'border', 'shadow', 'colorChanged', 'radiusChanged',
  'topLeftRadiusChanged', 'topRightRadiusChanged', 'bottomLeftRadiusChanged',
  'bottomRightRadiusChanged', 'scaleChanged', 'rotationChanged',
  'visibleChanged', 'clipChanged', 'borderChanged', 'shadowChanged',
  'imageChanged', 'gradientChanged', 'colorImageChanged', 'widthChanged',
  'heightChanged', 'minimumWidthChanged', 'minimumHeightChanged',
  'marginsChanged', 'leftMarginChanged', 'rightMarginChanged',
  'topMarginChanged', 'bottomMarginChanged', 'alignmentChanged',
  'opacityChanged', 'dataChanged', 'delegateChanged', 'fillWidthChanged',
  'fillHeightChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitDelegateProperties::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitDelegateProperties::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitDelegateProperties::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 94 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQStyleKitDelegateProperties is created at the first use, not by
    'QQStyleKitDelegateProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitDelegateProperties.
  - Qt tells when it has removed the C++ QQStyleKitDelegateProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitDelegateProperties that has no cute function
    yet, 'emitGlobally', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQStyleKitDelegateProperties::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#tr

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
    #  QString QQStyleKitDelegateProperties::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQStyleKitDelegateProperties2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitDelegateProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitDelegateProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitDelegateProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#radius
    """
    #  qreal QQStyleKitDelegateProperties::radius() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties6radiusEv',
    )

  def topLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::topLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#topLeftRadius
    """
    #  qreal QQStyleKitDelegateProperties::topLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties13topLeftRadiusEv',
    )

  def topRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#topRightRadius
    """
    #  qreal QQStyleKitDelegateProperties::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::bottomLeftRadius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#bottomLeftRadius
    """
    #  qreal QQStyleKitDelegateProperties::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::bottomRightRadius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  qreal QQStyleKitDelegateProperties::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties17bottomRightRadiusEv',
    )

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#scale
    """
    #  qreal QQStyleKitDelegateProperties::scale() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties5scaleEv',
    )

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#rotation
    """
    #  qreal QQStyleKitDelegateProperties::rotation() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties8rotationEv',
    )

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#width
    """
    #  qreal QQStyleKitDelegateProperties::width() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties5widthEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#height
    """
    #  qreal QQStyleKitDelegateProperties::height() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties6heightEv',
    )

  def minimumWidth(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::minimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#minimumWidth
    """
    #  qreal QQStyleKitDelegateProperties::minimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties12minimumWidthEv',
    )

  def minimumHeight(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::minimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#minimumHeight
    """
    #  qreal QQStyleKitDelegateProperties::minimumHeight() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties13minimumHeightEv',
    )

  def fillWidth(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitDelegateProperties::fillWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#fillWidth
    """
    #  bool QQStyleKitDelegateProperties::fillWidth() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties9fillWidthEv',
    )

  def fillHeight(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitDelegateProperties::fillHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#fillHeight
    """
    #  bool QQStyleKitDelegateProperties::fillHeight() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties10fillHeightEv',
    )

  def margins(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::margins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#margins
    """
    #  qreal QQStyleKitDelegateProperties::margins() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties7marginsEv',
    )

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::leftMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#leftMargin
    """
    #  qreal QQStyleKitDelegateProperties::leftMargin() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties10leftMarginEv',
    )

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::rightMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#rightMargin
    """
    #  qreal QQStyleKitDelegateProperties::rightMargin() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties11rightMarginEv',
    )

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::topMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#topMargin
    """
    #  qreal QQStyleKitDelegateProperties::topMargin() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties9topMarginEv',
    )

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::bottomMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#bottomMargin
    """
    #  qreal QQStyleKitDelegateProperties::bottomMargin() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties12bottomMarginEv',
    )

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQStyleKitDelegateProperties::alignment()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQStyleKitDelegateProperties::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties9alignmentEv',
    ))

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitDelegateProperties::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#opacity
    """
    #  qreal QQStyleKitDelegateProperties::opacity() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties7opacityEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQStyleKitDelegateProperties::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQStyleKitDelegateProperties::color() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def visible(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitDelegateProperties::visible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#visible
    """
    #  bool QQStyleKitDelegateProperties::visible() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties7visibleEv',
    )

  def clip(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitDelegateProperties::clip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#clip
    """
    #  bool QQStyleKitDelegateProperties::clip() const
    return self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties4clipEv',
    )

  def gradient(self) -> Optional[QQuickGradient]:
    """
    Calls Qt's 'QQuickGradient *QQStyleKitDelegateProperties::gradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#gradient

    Returns
    -------

    Optional[QQuickGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGradient *QQStyleKitDelegateProperties::gradient() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties8gradientEv',
    )
    from ..QtQuick import QQuickGradient
    return QQuickGradient._cuteAt(address)

  def data(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQStyleKitDelegateProperties::data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#data

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQStyleKitDelegateProperties::data() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties4dataEv',
    )
    return QObject._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQStyleKitDelegateProperties::delegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitDelegateProperties::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def image(self) -> Optional[QQStyleKitImageProperties]:
    """
    Calls Qt's 'QQStyleKitImageProperties
    *QQStyleKitDelegateProperties::image() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#image

    Returns
    -------

    Optional[QQStyleKitImageProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitImageProperties *QQStyleKitDelegateProperties::image() const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties5imageEv',
    )
    from . import QQStyleKitImageProperties
    return QQStyleKitImageProperties._cuteAt(address)

  def border(self) -> Optional[QQStyleKitBorderProperties]:
    """
    Calls Qt's 'QQStyleKitBorderProperties
    *QQStyleKitDelegateProperties::border() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#border

    Returns
    -------

    Optional[QQStyleKitBorderProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitBorderProperties *QQStyleKitDelegateProperties::border()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties6borderEv',
    )
    from . import QQStyleKitBorderProperties
    return QQStyleKitBorderProperties._cuteAt(address)

  def shadow(self) -> Optional[QQStyleKitShadowProperties]:
    """
    Calls Qt's 'QQStyleKitShadowProperties
    *QQStyleKitDelegateProperties::shadow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#shadow

    Returns
    -------

    Optional[QQStyleKitShadowProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitShadowProperties *QQStyleKitDelegateProperties::shadow()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQStyleKitDelegateProperties6shadowEv',
    )
    from . import QQStyleKitShadowProperties
    return QQStyleKitShadowProperties._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties9setRadiusEd', radius,
    )

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setTopLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties16setTopLeftRadiusEd',
        radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setTopRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties17setTopRightRadiusEd',
        radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setBottomLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties19setBottomLeftRadiusEd',
        radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setBottomRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties20setBottomRightRadiusEd',
        radius,
    )

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setScale(qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setScale(qreal scale)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties8setScaleEd', scale,
    )

  @overload(float)
  def setRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setRotation(qreal
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setRotation(qreal rotation)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties11setRotationEd', rotation,
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties8setWidthEd', width,
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties9setHeightEd', height,
    )

  @overload(float)
  def setMinimumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setMinimumWidth(qreal
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setMinimumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setMinimumWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties15setMinimumWidthEd', width,
    )

  @overload(float)
  def setMinimumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setMinimumHeight(qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setMinimumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setMinimumHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties16setMinimumHeightEd',
        height,
    )

  @overload(bool)
  def setFillWidth(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setFillWidth(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setFillWidth

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setFillWidth(bool fill)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12setFillWidthEb', fill,
    )

  @overload(bool)
  def setFillHeight(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setFillHeight(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setFillHeight

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setFillHeight(bool fill)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13setFillHeightEb', fill,
    )

  @overload(float)
  def setMargins(self, margins: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setMargins(qreal
    margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setMargins

    Parameters
    ----------

    margins : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setMargins(qreal margins)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties10setMarginsEd', margins,
    )

  @overload(float)
  def setLeftMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setLeftMargin(qreal
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setLeftMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setLeftMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13setLeftMarginEd', margin,
    )

  @overload(float)
  def setRightMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setRightMargin(qreal
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setRightMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setRightMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties14setRightMarginEd', margin,
    )

  @overload(float)
  def setTopMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setTopMargin(qreal
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setTopMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setTopMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12setTopMarginEd', margin,
    )

  @overload(float)
  def setBottomMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setBottomMargin(qreal
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setBottomMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setBottomMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties15setBottomMarginEd', margin,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QQStyleKitDelegateProperties::setAlignment(Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12setAlignmentE6QFlagsIN2Qt'
        '13AlignmentFlagEE',
        alignment.value,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setOpacity(qreal
    opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setOpacity(qreal opacity)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties10setOpacityEd', opacity,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQStyleKitDelegateProperties::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties10setVisibleEb', visible,
    )

  @overload(bool)
  def setClip(self, clip: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setClip(bool clip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setClip

    Parameters
    ----------

    clip : bool
      Passed on as it is.
    """
    #  void QQStyleKitDelegateProperties::setClip(bool clip)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties7setClipEb', clip,
    )

  @overload(QQuickGradient)
  @overload(NoneType)
  def setGradient(self, gradient: Optional[QQuickGradient]) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setGradient(QQuickGradient
    *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setGradient

    Parameters
    ----------

    gradient : Optional[QQuickGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitDelegateProperties::setGradient(QQuickGradient
    #      *gradient)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties11setGradientEP14QQuickGrad'
        'ient',
        self._addressOf(gradient),
    )

  @overload(QObject)
  @overload(NoneType)
  def setData(self, data: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setData(QObject *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setData

    Parameters
    ----------

    data : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitDelegateProperties::setData(QObject *data)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties7setDataEP7QObject',
        self._addressOf(data, 'QObject'),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitDelegateProperties::setDelegate(QQmlComponent
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties11setDelegateEP13QQmlCompon'
        'ent',
        self._addressOf(delegate),
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

  @overload(QQSK.PropertyGroup)
  @overload(QQSK.PropertyGroup, QQStyleKitControlProperties)
  @overload(QQSK.PropertyGroup, NoneType)
  def __init__(
      self,
      group: QQSK.PropertyGroup,
      parent: Optional[QQStyleKitControlProperties] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQStyleKitDelegateProperties::QQStyleKitDelegateProperties(QQSK::
    PropertyGroup group, QQStyleKitControlProperties *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html

    Parameters
    ----------

    group : QQSK.PropertyGroup
      Passed on as its number.

    parent : Optional[QQStyleKitControlProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitDelegateProperties::QQStyleKitDelegateProperties(QQSK::
    #      PropertyGroup group, QQStyleKitControlProperties *parent)
    self._noteCreation(QQStyleKitDelegateProperties, lambda: Rituals.call(
        'ritual_ZN28QQStyleKitDelegatePropertiesC1EN4QQSK13PropertyGroupEP2'
        '7QQStyleKitControlProperties',
        group.value, self._addressOf(parent),
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

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#colorChanged
    """
    #  void QQStyleKitDelegateProperties::colorChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12colorChangedEv',
    )

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#radiusChanged
    """
    #  void QQStyleKitDelegateProperties::radiusChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13radiusChangedEv',
    )

  def topLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::topLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::topLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties20topLeftRadiusChangedEv',
    )

  def topRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::topRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::topRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties21topRightRadiusChangedEv',
    )

  def bottomLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void
    QQStyleKitDelegateProperties::bottomLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::bottomLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties23bottomLeftRadiusChangedEv',
    )

  def bottomRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void
    QQStyleKitDelegateProperties::bottomRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::bottomRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties24bottomRightRadiusChangedE'
        'v',
    )

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::scaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#scaleChanged
    """
    #  void QQStyleKitDelegateProperties::scaleChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12scaleChangedEv',
    )

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#rotationChanged
    """
    #  void QQStyleKitDelegateProperties::rotationChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties15rotationChangedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#visibleChanged
    """
    #  void QQStyleKitDelegateProperties::visibleChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties14visibleChangedEv',
    )

  def clipChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::clipChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#clipChanged
    """
    #  void QQStyleKitDelegateProperties::clipChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties11clipChangedEv',
    )

  def borderChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::borderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#borderChanged
    """
    #  void QQStyleKitDelegateProperties::borderChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13borderChangedEv',
    )

  def shadowChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::shadowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#shadowChanged
    """
    #  void QQStyleKitDelegateProperties::shadowChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13shadowChangedEv',
    )

  def imageChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::imageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#imageChanged
    """
    #  void QQStyleKitDelegateProperties::imageChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12imageChangedEv',
    )

  def gradientChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::gradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#gradientChanged
    """
    #  void QQStyleKitDelegateProperties::gradientChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties15gradientChangedEv',
    )

  def colorImageChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::colorImageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::colorImageChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties17colorImageChangedEv',
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#widthChanged
    """
    #  void QQStyleKitDelegateProperties::widthChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties12widthChangedEv',
    )

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#heightChanged
    """
    #  void QQStyleKitDelegateProperties::heightChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties13heightChangedEv',
    )

  def minimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::minimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::minimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties19minimumWidthChangedEv',
    )

  def minimumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::minimumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::minimumHeightChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties20minimumHeightChangedEv',
    )

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::marginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#marginsChanged
    """
    #  void QQStyleKitDelegateProperties::marginsChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties14marginsChangedEv',
    )

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::leftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::leftMarginChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties17leftMarginChangedEv',
    )

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::rightMarginChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties18rightMarginChangedEv',
    )

  def topMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::topMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#topMarginChanged
    """
    #  void QQStyleKitDelegateProperties::topMarginChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties16topMarginChangedEv',
    )

  def bottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::bottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::bottomMarginChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties19bottomMarginChangedEv',
    )

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#alignmentChanged
    """
    #  void QQStyleKitDelegateProperties::alignmentChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties16alignmentChangedEv',
    )

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#opacityChanged
    """
    #  void QQStyleKitDelegateProperties::opacityChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties14opacityChangedEv',
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#dataChanged
    """
    #  void QQStyleKitDelegateProperties::dataChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties11dataChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#delegateChanged
    """
    #  void QQStyleKitDelegateProperties::delegateChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties15delegateChangedEv',
    )

  def fillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::fillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html#fillWidthChanged
    """
    #  void QQStyleKitDelegateProperties::fillWidthChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties16fillWidthChangedEv',
    )

  def fillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateProperties::fillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegateproperties.html
    """
    #  void QQStyleKitDelegateProperties::fillHeightChanged()
    self.uglySide.call(
        'ritual_ZN28QQStyleKitDelegateProperties17fillHeightChangedEv',
    )

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitDelegateProperties::emitGlobally': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateProperties.emitGlobally' has no cute function "
        "yet. Qt's 'QQStyleKitDelegateProperties::emitGlobally': a "
        "template: a pattern and no single function.")
