"""
QQStyleKitImageProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitImageProperties to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQSK, QQStyleKitPropertyGroup
from ..QtQuick import QQuickImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QColor
  from . import QQStyleKitControlProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQStyleKitControlProperties = WAIT['QQStyleKitControlProperties']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitImageProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitImageProperties: a plain Python object
  standing in front of one C++ QQStyleKitImageProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitImageProperties is built on Qt's QQStyleKitPropertyGroup, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitImageProperties that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'color', 'setColor', 'fillMode', 'setFillMode',
  'sourceChanged', 'colorChanged', 'fillModeChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitImageProperties::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQStyleKitImageProperties::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitImageProperties::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQStyleKitImageProperties is created at the first use, not by
    'QQStyleKitImageProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitImageProperties.
  - Qt tells when it has removed the C++ QQStyleKitImageProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitImageProperties that has no cute function
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
    Calls Qt's 'QString QQStyleKitImageProperties::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitimageproperties.html#tr

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
    #  QString QQStyleKitImageProperties::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQStyleKitImageProperties2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitImageProperties'

  #  A C++ QQStyleKitImageProperties Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitImageProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitImageProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitImageProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQStyleKitImageProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQStyleKitImageProperties::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQStyleKitImageProperties::source() const
    address = self.uglySide.call(
        'ritual_ZNK25QQStyleKitImageProperties6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQStyleKitImageProperties::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQStyleKitImageProperties::color() const
    address = self.uglySide.call(
        'ritual_ZNK25QQStyleKitImageProperties5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fillMode(self) -> QQuickImage.FillMode:
    """
    Calls Qt's 'QQuickImage::FillMode QQStyleKitImageProperties::fillMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#fillMode

    Returns
    -------

    QQuickImage.FillMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickImage.FillMode(number)' gives.
    """
    #  QQuickImage::FillMode QQStyleKitImageProperties::fillMode() const
    return QQuickImage.FillMode(self.uglySide.call(
        'ritual_ZNK25QQStyleKitImageProperties8fillModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQStyleKitImageProperties::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQStyleKitImageProperties::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQStyleKitImageProperties::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQStyleKitImageProperties::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickImage.FillMode)
  def setFillMode(self, fillMode: QQuickImage.FillMode) -> None:
    """
    Calls Qt's 'void
    QQStyleKitImageProperties::setFillMode(QQuickImage::FillMode fillMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#setFillMode

    Parameters
    ----------

    fillMode : QQuickImage.FillMode
      Passed on as its number.
    """
    #  void QQStyleKitImageProperties::setFillMode(QQuickImage::FillMode
    #      fillMode)
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties11setFillModeEN11QQuickImage8F'
        'illModeE',
        fillMode.value,
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
    'QQStyleKitImageProperties::QQStyleKitImageProperties(QQSK::PropertyGroup
    group, QQStyleKitControlProperties *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html

    Parameters
    ----------

    group : QQSK.PropertyGroup
      Passed on as its number.

    parent : Optional[QQStyleKitControlProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitImageProperties::QQStyleKitImageProperties(QQSK::
    #      PropertyGroup group, QQStyleKitControlProperties *parent)
    self._noteCreation(QQStyleKitImageProperties, lambda: Rituals.call(
        'ritual_ZN25QQStyleKitImagePropertiesC1EN4QQSK13PropertyGroupEP27QQ'
        'StyleKitControlProperties',
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitImageProperties::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#sourceChanged
    """
    #  void QQStyleKitImageProperties::sourceChanged()
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties13sourceChangedEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitImageProperties::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#colorChanged
    """
    #  void QQStyleKitImageProperties::colorChanged()
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties12colorChangedEv',
    )

  def fillModeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitImageProperties::fillModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitimageproperties.html#fillModeChanged
    """
    #  void QQStyleKitImageProperties::fillModeChanged()
    self.uglySide.call(
        'ritual_ZN25QQStyleKitImageProperties15fillModeChangedEv',
    )

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitImageProperties::emitGlobally': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitImageProperties.emitGlobally' has no cute function yet. "
        "Qt's 'QQStyleKitImageProperties::emitGlobally': a template: a "
        "pattern and no single function.")
