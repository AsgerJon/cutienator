"""
QQStyleKitShadowProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitShadowProperties to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQSK, QQStyleKitPropertyGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from . import QQStyleKitControlProperties
  from ..QtQml import QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQStyleKitControlProperties = WAIT['QQStyleKitControlProperties']
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitShadowProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitShadowProperties: a plain Python object
  standing in front of one C++ QQStyleKitShadowProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitShadowProperties is built on Qt's QQStyleKitPropertyGroup, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitShadowProperties that has a ritual and
  that Python can call so far, 26 names in all: 'metaObject', 'tr', 'color',
  'setColor', 'opacity', 'setOpacity', 'scale', 'setScale', 'verticalOffset',
  'setVerticalOffset', 'horizontalOffset', 'setHorizontalOffset', 'blur',
  'setBlur', 'visible', 'setVisible', 'delegate', 'setDelegate',
  'colorChanged', 'opacityChanged', 'scaleChanged', 'verticalOffsetChanged',
  'horizontalOffsetChanged', 'blurChanged', 'visibleChanged',
  'delegateChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitShadowProperties::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQStyleKitShadowProperties::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitShadowProperties::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQStyleKitShadowProperties is created at the first use, not by
    'QQStyleKitShadowProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitShadowProperties.
  - Qt tells when it has removed the C++ QQStyleKitShadowProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitShadowProperties that has no cute function
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
    Calls Qt's 'QString QQStyleKitShadowProperties::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#tr

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
    #  QString QQStyleKitShadowProperties::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQStyleKitShadowProperties2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitShadowProperties'

  #  A C++ QQStyleKitShadowProperties Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitShadowProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitShadowProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitShadowProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQStyleKitShadowProperties::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQStyleKitShadowProperties::color() const
    address = self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitShadowProperties::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#opacity
    """
    #  qreal QQStyleKitShadowProperties::opacity() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties7opacityEv',
    )

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitShadowProperties::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#scale
    """
    #  qreal QQStyleKitShadowProperties::scale() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties5scaleEv',
    )

  def verticalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitShadowProperties::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#verticalOffset
    """
    #  qreal QQStyleKitShadowProperties::verticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties14verticalOffsetEv',
    )

  def horizontalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitShadowProperties::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#horizontalOffset
    """
    #  qreal QQStyleKitShadowProperties::horizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties16horizontalOffsetEv',
    )

  def blur(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitShadowProperties::blur() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#blur
    """
    #  qreal QQStyleKitShadowProperties::blur() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties4blurEv',
    )

  def visible(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitShadowProperties::visible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#visible
    """
    #  bool QQStyleKitShadowProperties::visible() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties7visibleEv',
    )

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQStyleKitShadowProperties::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitShadowProperties::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK26QQStyleKitShadowProperties8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQStyleKitShadowProperties::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties8setColorE6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setOpacity(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setOpacity(qreal opacity)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties10setOpacityEd', opacity,
    )

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setScale(qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setScale(qreal scale)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties8setScaleEd', scale,
    )

  @overload(float)
  def setVerticalOffset(self, verticalOffset: float) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setVerticalOffset(qreal
    verticalOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setVerticalOffset

    Parameters
    ----------

    verticalOffset : float
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setVerticalOffset(qreal
    #      verticalOffset)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties17setVerticalOffsetEd',
        verticalOffset,
    )

  @overload(float)
  def setHorizontalOffset(self, horizontalOffset: float) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setHorizontalOffset(qreal
    horizontalOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html

    Parameters
    ----------

    horizontalOffset : float
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setHorizontalOffset(qreal
    #      horizontalOffset)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties19setHorizontalOffsetEd',
        horizontalOffset,
    )

  @overload(float)
  def setBlur(self, blur: float) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setBlur(qreal blur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setBlur

    Parameters
    ----------

    blur : float
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setBlur(qreal blur)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties7setBlurEd', blur,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQStyleKitShadowProperties::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties10setVisibleEb', visible,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitShadowProperties::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties11setDelegateEP13QQmlComponen'
        't',
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
    'QQStyleKitShadowProperties::QQStyleKitShadowProperties(QQSK::
    PropertyGroup group, QQStyleKitControlProperties *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html

    Parameters
    ----------

    group : QQSK.PropertyGroup
      Passed on as its number.

    parent : Optional[QQStyleKitControlProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitShadowProperties::QQStyleKitShadowProperties(QQSK::
    #      PropertyGroup group, QQStyleKitControlProperties *parent)
    self._noteCreation(QQStyleKitShadowProperties, lambda: Rituals.call(
        'ritual_ZN26QQStyleKitShadowPropertiesC1EN4QQSK13PropertyGroupEP27Q'
        'QStyleKitControlProperties',
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
    Calls Qt's 'void QQStyleKitShadowProperties::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#colorChanged
    """
    #  void QQStyleKitShadowProperties::colorChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties12colorChangedEv',
    )

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#opacityChanged
    """
    #  void QQStyleKitShadowProperties::opacityChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties14opacityChangedEv',
    )

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::scaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#scaleChanged
    """
    #  void QQStyleKitShadowProperties::scaleChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties12scaleChangedEv',
    )

  def verticalOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::verticalOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html
    """
    #  void QQStyleKitShadowProperties::verticalOffsetChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties21verticalOffsetChangedEv',
    )

  def horizontalOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::horizontalOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html
    """
    #  void QQStyleKitShadowProperties::horizontalOffsetChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties23horizontalOffsetChangedEv',
    )

  def blurChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::blurChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#blurChanged
    """
    #  void QQStyleKitShadowProperties::blurChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties11blurChangedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#visibleChanged
    """
    #  void QQStyleKitShadowProperties::visibleChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties14visibleChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitShadowProperties::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitshadowproperties.html#delegateChanged
    """
    #  void QQStyleKitShadowProperties::delegateChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitShadowProperties15delegateChangedEv',
    )

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitShadowProperties::emitGlobally': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitShadowProperties.emitGlobally' has no cute function "
        "yet. Qt's 'QQStyleKitShadowProperties::emitGlobally': a template: "
        "a pattern and no single function.")
