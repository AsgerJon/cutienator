"""
QQStyleKitBorderProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitBorderProperties to be private: it declares the class
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQStyleKitControlProperties = WAIT['QQStyleKitControlProperties']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitBorderProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitBorderProperties: a plain Python object
  standing in front of one C++ QQStyleKitBorderProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitBorderProperties is built on Qt's QQStyleKitPropertyGroup, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitBorderProperties that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'width',
  'setWidth', 'color', 'setColor', 'widthChanged', 'colorChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitBorderProperties::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQStyleKitBorderProperties::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitBorderProperties::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQStyleKitBorderProperties is created at the first use, not by
    'QQStyleKitBorderProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitBorderProperties.
  - Qt tells when it has removed the C++ QQStyleKitBorderProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitBorderProperties that has no cute function
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
    Calls Qt's 'QString QQStyleKitBorderProperties::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitborderproperties.html#tr

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
    #  QString QQStyleKitBorderProperties::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQStyleKitBorderProperties2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitBorderProperties'

  #  A C++ QQStyleKitBorderProperties Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitBorderProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitBorderProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitBorderProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQStyleKitBorderProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitBorderProperties::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#width
    """
    #  qreal QQStyleKitBorderProperties::width() const
    return self.uglySide.call(
        'ritual_ZNK26QQStyleKitBorderProperties5widthEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQStyleKitBorderProperties::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQStyleKitBorderProperties::color() const
    address = self.uglySide.call(
        'ritual_ZNK26QQStyleKitBorderProperties5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQStyleKitBorderProperties::setWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQStyleKitBorderProperties::setWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitBorderProperties8setWidthEd', width,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQStyleKitBorderProperties::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQStyleKitBorderProperties::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN26QQStyleKitBorderProperties8setColorERK6QColor',
        self._valueOf(color),
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
    'QQStyleKitBorderProperties::QQStyleKitBorderProperties(QQSK::
    PropertyGroup group, QQStyleKitControlProperties *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html

    Parameters
    ----------

    group : QQSK.PropertyGroup
      Passed on as its number.

    parent : Optional[QQStyleKitControlProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitBorderProperties::QQStyleKitBorderProperties(QQSK::
    #      PropertyGroup group, QQStyleKitControlProperties *parent)
    self._noteCreation(QQStyleKitBorderProperties, lambda: Rituals.call(
        'ritual_ZN26QQStyleKitBorderPropertiesC1EN4QQSK13PropertyGroupEP27Q'
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

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitBorderProperties::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#widthChanged
    """
    #  void QQStyleKitBorderProperties::widthChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitBorderProperties12widthChangedEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitBorderProperties::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitborderproperties.html#colorChanged
    """
    #  void QQStyleKitBorderProperties::colorChanged()
    self.uglySide.call(
        'ritual_ZN26QQStyleKitBorderProperties12colorChangedEv',
    )

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitBorderProperties::emitGlobally': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitBorderProperties.emitGlobally' has no cute function "
        "yet. Qt's 'QQStyleKitBorderProperties::emitGlobally': a template: "
        "a pattern and no single function.")
