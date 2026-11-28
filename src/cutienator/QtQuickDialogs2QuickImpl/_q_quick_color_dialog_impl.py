"""
QQuickColorDialogImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorDialogImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtGui import QColor
  from . import QQuickColorDialogImplAttached, QQuickColorDialogImplPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorDialogImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickColorDialogImpl: a plain Python object standing
  in front of one C++ QQuickColorDialogImpl.

  What exists
  -----------

  Every function of Qt's QQuickColorDialogImpl that has a ritual and that
  Python can call so far, 28 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'color', 'setColor', 'red', 'setRed', 'green',
  'setGreen', 'blue', 'setBlue', 'alpha', 'setAlpha', 'hue', 'setHue',
  'saturation', 'setSaturation', 'value', 'setValue', 'lightness',
  'setLightness', 'isHsl', 'setHsl', 'invokeEyeDropper', 'colorChanged',
  'specChanged', 'itemChange', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorDialogImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickColorDialogImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickColorDialogImpl::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QSharedPointer<QColorDialogOptions>
    QQuickColorDialogImpl::options() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QQuickColorDialogImpl::setOptions(const
    QSharedPointer<QColorDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QQuickColorDialogImplPrivate *QQuickColorDialogImpl::d_func()
    const': takes in Python what 'QQuickColorDialogImplPrivate
    *QQuickColorDialogImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickColorDialogImpl is created at the first use, not by
    'QQuickColorDialogImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorDialogImpl.
  - Qt tells when it has removed the C++ QQuickColorDialogImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickColorDialogImpl that has no cute function yet,
    'options', 'setOptions', holds a function that raises
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
    Calls Qt's 'QString QQuickColorDialogImpl::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#tr

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
    #  QString QQuickColorDialogImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickColorDialogImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickColorDialogImplAttached]:
    """
    Calls Qt's 'QQuickColorDialogImplAttached
    *QQuickColorDialogImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickColorDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImplAttached
    #      *QQuickColorDialogImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN21QQuickColorDialogImpl21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickColorDialogImplAttached
    return QQuickColorDialogImplAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorDialogImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColorDialogImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorDialogImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickColorDialogImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorDialogImpl::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorDialogImpl::color() const
    address = self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def red(self) -> int:
    """
    Calls Qt's 'int QQuickColorDialogImpl::red() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#red
    """
    #  int QQuickColorDialogImpl::red() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl3redEv')

  def green(self) -> int:
    """
    Calls Qt's 'int QQuickColorDialogImpl::green() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#green
    """
    #  int QQuickColorDialogImpl::green() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl5greenEv')

  def blue(self) -> int:
    """
    Calls Qt's 'int QQuickColorDialogImpl::blue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#blue
    """
    #  int QQuickColorDialogImpl::blue() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl4blueEv')

  def alpha(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorDialogImpl::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#alpha
    """
    #  qreal QQuickColorDialogImpl::alpha() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl5alphaEv')

  def hue(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorDialogImpl::hue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#hue
    """
    #  qreal QQuickColorDialogImpl::hue() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl3hueEv')

  def saturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorDialogImpl::saturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#saturation
    """
    #  qreal QQuickColorDialogImpl::saturation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickColorDialogImpl10saturationEv',
    )

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorDialogImpl::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#value
    """
    #  qreal QQuickColorDialogImpl::value() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl5valueEv')

  def lightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorDialogImpl::lightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#lightness
    """
    #  qreal QQuickColorDialogImpl::lightness() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickColorDialogImpl9lightnessEv',
    )

  def isHsl(self) -> bool:
    """
    Calls Qt's 'bool QQuickColorDialogImpl::isHsl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#isHsl
    """
    #  bool QQuickColorDialogImpl::isHsl() const
    return self.uglySide.call('ritual_ZNK21QQuickColorDialogImpl5isHslEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorDialogImpl::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN21QQuickColorDialogImpl8setColorERK6QColor',
        self._valueOf(c),
    )

  @overload(int)
  def setRed(self, red: int) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setRed(int red)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setRed

    Parameters
    ----------

    red : int
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setRed(int red)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl6setRedEi', red)

  @overload(int)
  def setGreen(self, green: int) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setGreen(int green)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setGreen

    Parameters
    ----------

    green : int
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setGreen(int green)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl8setGreenEi', green)

  @overload(int)
  def setBlue(self, blue: int) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setBlue(int blue)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setBlue

    Parameters
    ----------

    blue : int
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setBlue(int blue)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl7setBlueEi', blue)

  @overload(float)
  def setAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setAlpha(qreal alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setAlpha(qreal alpha)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl8setAlphaEd', alpha)

  @overload(float)
  def setHue(self, hue: float) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setHue(qreal hue)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setHue

    Parameters
    ----------

    hue : float
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setHue(qreal hue)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl6setHueEd', hue)

  @overload(float)
  def setSaturation(self, saturation: float) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setSaturation(qreal saturation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setSaturation

    Parameters
    ----------

    saturation : float
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setSaturation(qreal saturation)
    self.uglySide.call(
        'ritual_ZN21QQuickColorDialogImpl13setSaturationEd', saturation,
    )

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setValue(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setValue(qreal value)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl8setValueEd', value)

  @overload(float)
  def setLightness(self, lightness: float) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setLightness(qreal lightness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setLightness

    Parameters
    ----------

    lightness : float
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setLightness(qreal lightness)
    self.uglySide.call(
        'ritual_ZN21QQuickColorDialogImpl12setLightnessEd', lightness,
    )

  @overload(bool)
  def setHsl(self, hsl: bool) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::setHsl(bool hsl)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#setHsl

    Parameters
    ----------

    hsl : bool
      Passed on as it is.
    """
    #  void QQuickColorDialogImpl::setHsl(bool hsl)
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl6setHslEb', hsl)

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
    'QQuickColorDialogImpl::QQuickColorDialogImpl(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#QQuickColorDialogImpl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorDialogImpl::QQuickColorDialogImpl(QObject *parent)
    self._noteCreation(QQuickColorDialogImpl, lambda: Rituals.call(
        'ritual_ZN21QQuickColorDialogImplC1EP7QObject',
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

  def invokeEyeDropper(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::invokeEyeDropper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#invokeEyeDropper
    """
    #  void QQuickColorDialogImpl::invokeEyeDropper()
    self.uglySide.call(
        'ritual_ZN21QQuickColorDialogImpl16invokeEyeDropperEv',
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorDialogImpl::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN21QQuickColorDialogImpl12colorChangedERK6QColor',
        self._valueOf(color),
    )

  def specChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::specChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#specChanged
    """
    #  void QQuickColorDialogImpl::specChanged()
    self.uglySide.call('ritual_ZN21QQuickColorDialogImpl11specChangedEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImpl::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimpl.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickColorDialogImpl::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN21QQuickColorDialogImpl10itemChangeEN10QQuickItem10ItemCh'
        'angeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickColorDialogImpl10itemChangeEN10QQuickItem10'
          'ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickColorDialogImplPrivate]:
    """
    Calls Qt's 'QQuickColorDialogImplPrivate
    *QQuickColorDialogImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialogimpl.html#d_func

    Returns
    -------

    Optional[QQuickColorDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImplPrivate *QQuickColorDialogImpl::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickColorDialogImpl6d_funcEv')
    from . import QQuickColorDialogImplPrivate
    return QQuickColorDialogImplPrivate._cuteAt(address)

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QColorDialogOptions>
    QQuickColorDialogImpl::options() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickColorDialogImpl.options' has no cute function yet. Qt's "
        "'QSharedPointer<QColorDialogOptions> "
        "QQuickColorDialogImpl::options() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickColorDialogImpl::setOptions(const
    QSharedPointer<QColorDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickColorDialogImpl.setOptions' has no cute function yet. Qt's "
        "'void QQuickColorDialogImpl::setOptions(const "
        "QSharedPointer<QColorDialogOptions> &options)': takes a type "
        "Python has no way to hand over yet.")
