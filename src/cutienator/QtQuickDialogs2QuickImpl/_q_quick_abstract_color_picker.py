"""
QQuickAbstractColorPicker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractColorPicker to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QColor
  from ..QtQuick import QQuickItem
  from . import QQuickAbstractColorPickerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractColorPicker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAbstractColorPicker: a plain Python object
  standing in front of one C++ QQuickAbstractColorPicker.

  What exists
  -----------

  Every function of Qt's QQuickAbstractColorPicker that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr', 'color',
  'setColor', 'hue', 'setHue', 'saturation', 'setSaturation', 'value',
  'setValue', 'lightness', 'setLightness', 'alpha', 'setAlpha', 'isPressed',
  'setPressed', 'handle', 'setHandle', 'implicitHandleWidth',
  'implicitHandleHeight', 'colorChanged', 'pressedChanged', 'handleChanged',
  'implicitHandleWidthChanged', 'implicitHandleHeightChanged', 'colorPicked',
  'colorAt', 'componentComplete', 'updateColor', 'd_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAbstractColorPicker::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickAbstractColorPicker::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickAbstractColorPicker::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickAbstractColorPicker::~QQuickAbstractColorPicker()': the
    destructor: Python never removes a C++ QQuickAbstractColorPicker.
  - Qt's 'QQuickAbstractColorPicker::QQuickAbstractColorPicker(
    QQuickAbstractColorPickerPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QQuickAbstractColorPickerPrivate
    *QQuickAbstractColorPicker::d_func() const': takes in Python what
    'QQuickAbstractColorPickerPrivate *QQuickAbstractColorPicker::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickAbstractColorPicker is created at the first use, not by
    'QQuickAbstractColorPicker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractColorPicker.
  - Qt tells when it has removed the C++ QQuickAbstractColorPicker. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAbstractColorPicker that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuickAbstractColorPicker::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#tr

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
    #  QString QQuickAbstractColorPicker::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickAbstractColorPicker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractColorPicker'

  #  A C++ QQuickAbstractColorPicker Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractColorPicker'

  #  The functions Qt calls itself that QQuickAbstractColorPicker is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'colorAt': (
          ('_ZN25QQuickAbstractColorPicker7colorAtERK7QPointF',
           ('address', 'value', 'QtGui:QColor'),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAbstractColorPicker::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAbstractColorPicker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickAbstractColorPicker::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickAbstractColorPicker::color() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hue(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::hue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#hue
    """
    #  qreal QQuickAbstractColorPicker::hue() const
    return self.uglySide.call('ritual_ZNK25QQuickAbstractColorPicker3hueEv')

  def saturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::saturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#saturation
    """
    #  qreal QQuickAbstractColorPicker::saturation() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker10saturationEv',
    )

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#value
    """
    #  qreal QQuickAbstractColorPicker::value() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker5valueEv',
    )

  def lightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::lightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#lightness
    """
    #  qreal QQuickAbstractColorPicker::lightness() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker9lightnessEv',
    )

  def alpha(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::alpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#alpha
    """
    #  qreal QQuickAbstractColorPicker::alpha() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker5alphaEv',
    )

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractColorPicker::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#isPressed
    """
    #  bool QQuickAbstractColorPicker::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker9isPressedEv',
    )

  def handle(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAbstractColorPicker::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#handle

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAbstractColorPicker::handle() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker6handleEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def implicitHandleWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::implicitHandleWidth()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#implicitHandleWidth
    """
    #  qreal QQuickAbstractColorPicker::implicitHandleWidth() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker19implicitHandleWidthEv',
    )

  def implicitHandleHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractColorPicker::implicitHandleHeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html
    """
    #  qreal QQuickAbstractColorPicker::implicitHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAbstractColorPicker20implicitHandleHeightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickAbstractColorPicker::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker8setColorERK6QColor',
        self._valueOf(c),
    )

  @overload(float)
  def setHue(self, hue: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setHue(qreal hue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setHue

    Parameters
    ----------

    hue : float
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setHue(qreal hue)
    self.uglySide.call('ritual_ZN25QQuickAbstractColorPicker6setHueEd', hue)

  @overload(float)
  def setSaturation(self, saturation: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setSaturation(qreal
    saturation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setSaturation

    Parameters
    ----------

    saturation : float
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setSaturation(qreal saturation)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker13setSaturationEd', saturation,
    )

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setValue(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setValue(qreal value)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker8setValueEd', value,
    )

  @overload(float)
  def setLightness(self, lightness: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setLightness(qreal
    lightness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setLightness

    Parameters
    ----------

    lightness : float
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setLightness(qreal lightness)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker12setLightnessEd', lightness,
    )

  @overload(float)
  def setAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setAlpha(qreal alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setAlpha(qreal alpha)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker8setAlphaEd', alpha,
    )

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickAbstractColorPicker::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker10setPressedEb', pressed,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setHandle(self, handle: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::setHandle(QQuickItem
    *handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#setHandle

    Parameters
    ----------

    handle : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractColorPicker::setHandle(QQuickItem *handle)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker9setHandleEP10QQuickItem',
        self._addressOf(handle),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickAbstractColorPicker::QQuickAbstractColorPicker(
    QQuickAbstractColorPickerPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAbstractColorPicker.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickAbstractColorPicker::QQuickAbstractColorPicker(QQuickAbstrac"
        "tColorPickerPrivate &dd, QQuickItem *parent)': takes a type Python "
        "has no way to hand over yet.")

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

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickAbstractColorPicker::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker12colorChangedERK6QColor',
        self._valueOf(color),
    )

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#pressedChanged
    """
    #  void QQuickAbstractColorPicker::pressedChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker14pressedChangedEv',
    )

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::handleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#handleChanged
    """
    #  void QQuickAbstractColorPicker::handleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker13handleChangedEv',
    )

  def implicitHandleWidthChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractColorPicker::implicitHandleWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html
    """
    #  void QQuickAbstractColorPicker::implicitHandleWidthChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker26implicitHandleWidthChangedEv',
    )

  def implicitHandleHeightChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractColorPicker::implicitHandleHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html
    """
    #  void QQuickAbstractColorPicker::implicitHandleHeightChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker27implicitHandleHeightChangedE'
        'v',
    )

  @overload(QColor)
  def colorPicked(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::colorPicked(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#colorPicked

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickAbstractColorPicker::colorPicked(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker11colorPickedERK6QColor',
        self._valueOf(color),
    )

  @overload(QPointF)
  def colorAt(self, pos: QPointF) -> QColor:
    """
    Calls Qt's 'QColor QQuickAbstractColorPicker::colorAt(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#colorAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickAbstractColorPicker::colorAt(const QPointF &pos)
    address = self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker7colorAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#componentComplete
    """
    #  void QQuickAbstractColorPicker::componentComplete()
    ritual = 'ritual_ZN25QQuickAbstractColorPicker17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickAbstractColorPicker17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload(QPointF)
  def updateColor(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPicker::updateColor(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#updateColor

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickAbstractColorPicker::updateColor(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker11updateColorERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  def d_func(self) -> Optional[QQuickAbstractColorPickerPrivate]:
    """
    Calls Qt's 'QQuickAbstractColorPickerPrivate
    *QQuickAbstractColorPicker::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpicker.html#d_func

    Returns
    -------

    Optional[QQuickAbstractColorPickerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractColorPickerPrivate *QQuickAbstractColorPicker::d_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickAbstractColorPicker6d_funcEv',
    )
    from . import QQuickAbstractColorPickerPrivate
    return QQuickAbstractColorPickerPrivate._cuteAt(address)
