"""
QAbstractSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractslider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QMetaObject
from ._q_widget import QWidget
from ._q_abstract_slider_slider_action import SliderAction

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSlider(QWidget):
  """
  The cute side of Qt's QAbstractSlider: a plain Python object standing in
  front of one C++ QAbstractSlider.

  It is built on the cute 'QWidget', as Qt's QAbstractSlider is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSlider that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'orientation',
  'setMinimum', 'minimum', 'setMaximum', 'maximum', 'setSingleStep',
  'singleStep', 'setPageStep', 'pageStep', 'setTracking', 'hasTracking',
  'setSliderDown', 'isSliderDown', 'setSliderPosition', 'sliderPosition',
  'setInvertedAppearance', 'invertedAppearance', 'setInvertedControls',
  'invertedControls', 'value', 'triggerAction', 'setValue', 'setOrientation',
  'setRange'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractSlider::~QAbstractSlider()': the destructor: Python never
    removes a C++ QAbstractSlider.

  What has no ritual
  ------------------

  23 of the 51 functions Qt declares: 9 protected; 6 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QAbstractSlider is created at the first use, not by
    'QAbstractSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSlider.
  - Qt tells when it has removed the C++ QAbstractSlider. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractSlider, and the names Qt has for the
  #  combinations of its flags enums.
  SliderAction = SliderAction

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
    Calls Qt's 'QString QAbstractSlider::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#tr

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
    #  QString QAbstractSlider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractSlider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSlider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractSlider::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSlider::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSlider10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QAbstractSlider::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QAbstractSlider::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QAbstractSlider11orientationEv',
    ))

  def minimum(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#minimum
    """
    #  int QAbstractSlider::minimum() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider7minimumEv')

  def maximum(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#maximum
    """
    #  int QAbstractSlider::maximum() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider7maximumEv')

  def singleStep(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::singleStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#singleStep
    """
    #  int QAbstractSlider::singleStep() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider10singleStepEv')

  def pageStep(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::pageStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#pageStep
    """
    #  int QAbstractSlider::pageStep() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider8pageStepEv')

  def hasTracking(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSlider::hasTracking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#hasTracking
    """
    #  bool QAbstractSlider::hasTracking() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider11hasTrackingEv')

  def isSliderDown(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSlider::isSliderDown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#isSliderDown
    """
    #  bool QAbstractSlider::isSliderDown() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider12isSliderDownEv')

  def sliderPosition(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::sliderPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#sliderPosition
    """
    #  int QAbstractSlider::sliderPosition() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractSlider14sliderPositionEv',
    )

  def invertedAppearance(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSlider::invertedAppearance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#invertedAppearance
    """
    #  bool QAbstractSlider::invertedAppearance() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractSlider18invertedAppearanceEv',
    )

  def invertedControls(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSlider::invertedControls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#invertedControls
    """
    #  bool QAbstractSlider::invertedControls() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractSlider16invertedControlsEv',
    )

  def value(self) -> int:
    """
    Calls Qt's 'int QAbstractSlider::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#value
    """
    #  int QAbstractSlider::value() const
    return self.uglySide.call('ritual_ZNK15QAbstractSlider5valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMinimum(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setMinimum(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setMinimum

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setMinimum(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider10setMinimumEi', a0)

  @overload(int)
  def setMaximum(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setMaximum(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setMaximum

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setMaximum(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider10setMaximumEi', a0)

  @overload(int)
  def setSingleStep(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setSingleStep(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setSingleStep

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setSingleStep(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider13setSingleStepEi', a0)

  @overload(int)
  def setPageStep(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setPageStep(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setPageStep

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setPageStep(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider11setPageStepEi', a0)

  @overload(bool)
  def setTracking(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setTracking(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setTracking

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractSlider::setTracking(bool enable)
    self.uglySide.call('ritual_ZN15QAbstractSlider11setTrackingEb', enable)

  @overload(bool)
  def setSliderDown(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setSliderDown(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setSliderDown

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractSlider::setSliderDown(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider13setSliderDownEb', a0)

  @overload(int)
  def setSliderPosition(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setSliderPosition(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#setSliderPosition

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setSliderPosition(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider17setSliderPositionEi', a0)

  @overload(bool)
  def setInvertedAppearance(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setInvertedAppearance(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#setInvertedAppearance

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractSlider::setInvertedAppearance(bool a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider21setInvertedAppearanceEb', a0,
    )

  @overload(bool)
  def setInvertedControls(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setInvertedControls(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#setInvertedControls

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractSlider::setInvertedControls(bool a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider19setInvertedControlsEb', a0,
    )

  @overload(int)
  def setValue(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setValue(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setValue(int a0)
    self.uglySide.call('ritual_ZN15QAbstractSlider8setValueEi', a0)

  @overload(Qt.Orientation)
  def setOrientation(self, a0: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setOrientation(Qt::Orientation a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#setOrientation

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractSlider::setOrientation(Qt::Orientation a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider14setOrientationEN2Qt11OrientationE',
        a0.value,
    )

  @overload(int, int)
  def setRange(self, min: int, max: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setRange(int min, int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#setRange

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.
    """
    #  void QAbstractSlider::setRange(int min, int max)
    self.uglySide.call('ritual_ZN15QAbstractSlider8setRangeEii', min, max)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QAbstractSlider::QAbstractSlider(QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#QAbstractSlider

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractSlider::QAbstractSlider(QWidget *parent)
    self._noteCreation(QAbstractSlider, lambda: Rituals.call(
        'ritual_ZN15QAbstractSliderC1EP7QWidget', self._addressOf(parent),
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

  @overload(SliderAction)
  def triggerAction(self, action: SliderAction) -> None:
    """
    Calls Qt's 'void QAbstractSlider::triggerAction(SliderAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#triggerAction

    Parameters
    ----------

    action : SliderAction
      Passed on as its number.
    """
    #  void QAbstractSlider::triggerAction(SliderAction action)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider13triggerActionENS_12SliderActionE',
        action.value,
    )
