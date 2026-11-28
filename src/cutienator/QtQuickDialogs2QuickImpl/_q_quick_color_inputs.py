"""
QQuickColorInputs binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolorinputs_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorInputs to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorInputs(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickColorInputs: a plain Python object standing in
  front of one C++ QQuickColorInputs.

  What exists
  -----------

  Every function of Qt's QQuickColorInputs that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'currentMode',
  'setCurrentMode', 'delegate', 'setDelegate', 'color', 'setColor', 'red',
  'green', 'blue', 'alpha', 'hue', 'hslSaturation', 'hsvSaturation', 'value',
  'lightness', 'showAlpha', 'setShowAlpha', 'colorChanged', 'colorModified',
  'hslChanged', 'showAlphaChanged', 'currentModeChanged', 'delegateChanged',
  'componentComplete'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorInputs::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickColorInputs::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickColorInputsPrivate *QQuickColorInputs::d_func()': gives
    'QQuickColorInputsPrivate', which has no cute class yet.
  - Qt's 'const QQuickColorInputsPrivate *QQuickColorInputs::d_func() const':
    gives 'QQuickColorInputsPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickColorInputs is created at the first use, not by
    'QQuickColorInputs(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorInputs.
  - Qt tells when it has removed the C++ QQuickColorInputs. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickColorInputs, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'QQuickColorInputs::Mode' of Qt, with the 4 names Qt gives in
    it.
    """

    Hex = Kee[int](0)
    Rgb = Kee[int](1)
    Hsv = Kee[int](2)
    Hsl = Kee[int](3)

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
    Calls Qt's 'QString QQuickColorInputs::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#tr

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
    #  QString QQuickColorInputs::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickColorInputs2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorInputs'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColorInputs::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorInputs::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickColorInputs10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentMode(self) -> Mode:
    """
    Calls Qt's 'Mode QQuickColorInputs::currentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#currentMode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QQuickColorInputs::currentMode() const
    return QQuickColorInputs.Mode(self.uglySide.call(
        'ritual_ZNK17QQuickColorInputs11currentModeEv',
    ))

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickColorInputs::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickColorInputs::delegate() const
    address = self.uglySide.call('ritual_ZNK17QQuickColorInputs8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorInputs::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorInputs::color() const
    address = self.uglySide.call('ritual_ZNK17QQuickColorInputs5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def red(self) -> int:
    """
    Calls Qt's 'int QQuickColorInputs::red() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#red
    """
    #  int QQuickColorInputs::red() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs3redEv')

  def green(self) -> int:
    """
    Calls Qt's 'int QQuickColorInputs::green() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#green
    """
    #  int QQuickColorInputs::green() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs5greenEv')

  def blue(self) -> int:
    """
    Calls Qt's 'int QQuickColorInputs::blue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#blue
    """
    #  int QQuickColorInputs::blue() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs4blueEv')

  def alpha(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#alpha
    """
    #  qreal QQuickColorInputs::alpha() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs5alphaEv')

  def hue(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::hue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#hue
    """
    #  qreal QQuickColorInputs::hue() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs3hueEv')

  def hslSaturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::hslSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#hslSaturation
    """
    #  qreal QQuickColorInputs::hslSaturation() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickColorInputs13hslSaturationEv',
    )

  def hsvSaturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::hsvSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#hsvSaturation
    """
    #  qreal QQuickColorInputs::hsvSaturation() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickColorInputs13hsvSaturationEv',
    )

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#value
    """
    #  qreal QQuickColorInputs::value() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs5valueEv')

  def lightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorInputs::lightness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#lightness
    """
    #  qreal QQuickColorInputs::lightness() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs9lightnessEv')

  def showAlpha(self) -> bool:
    """
    Calls Qt's 'bool QQuickColorInputs::showAlpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#showAlpha
    """
    #  bool QQuickColorInputs::showAlpha() const
    return self.uglySide.call('ritual_ZNK17QQuickColorInputs9showAlphaEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Mode)
  def setCurrentMode(self, mode: Mode) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::setCurrentMode(Mode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#setCurrentMode

    Parameters
    ----------

    mode : Mode
      Passed on as its number.
    """
    #  void QQuickColorInputs::setCurrentMode(Mode mode)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs14setCurrentModeENS_4ModeE', mode.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorInputs::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorInputs::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs8setColorERK6QColor', self._valueOf(c),
    )

  @overload(bool)
  def setShowAlpha(self, showAlpha: bool) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::setShowAlpha(bool showAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#setShowAlpha

    Parameters
    ----------

    showAlpha : bool
      Passed on as it is.
    """
    #  void QQuickColorInputs::setShowAlpha(bool showAlpha)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs12setShowAlphaEb', showAlpha,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorInputs::QQuickColorInputs(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#QQuickColorInputs

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorInputs::QQuickColorInputs(QQuickItem *parent)
    self._noteCreation(QQuickColorInputs, lambda: Rituals.call(
        'ritual_ZN17QQuickColorInputsC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QColor)
  def colorChanged(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::colorChanged(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#colorChanged

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorInputs::colorChanged(const QColor &c)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs12colorChangedERK6QColor',
        self._valueOf(c),
    )

  @overload(QColor)
  def colorModified(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::colorModified(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#colorModified

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorInputs::colorModified(const QColor &c)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs13colorModifiedERK6QColor',
        self._valueOf(c),
    )

  def hslChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::hslChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorinputs.html#hslChanged
    """
    #  void QQuickColorInputs::hslChanged()
    self.uglySide.call('ritual_ZN17QQuickColorInputs10hslChangedEv')

  @overload(bool)
  def showAlphaChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::showAlphaChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#showAlphaChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickColorInputs::showAlphaChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN17QQuickColorInputs16showAlphaChangedEb', a0,
    )

  def currentModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::currentModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#currentModeChanged
    """
    #  void QQuickColorInputs::currentModeChanged()
    self.uglySide.call('ritual_ZN17QQuickColorInputs18currentModeChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#delegateChanged
    """
    #  void QQuickColorInputs::delegateChanged()
    self.uglySide.call('ritual_ZN17QQuickColorInputs15delegateChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickColorInputs::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorinputs.html#componentComplete
    """
    #  void QQuickColorInputs::componentComplete()
    ritual = 'ritual_ZN17QQuickColorInputs17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickColorInputs17componentCompleteEv'
    self.uglySide.call(ritual)
