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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QTimerEvent
  from ..QtGui import QKeyEvent, QWheelEvent
  from . import QAbstractSliderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

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
  can call so far, 40 names in all: 'metaObject', 'tr', 'orientation',
  'setMinimum', 'minimum', 'setMaximum', 'maximum', 'setSingleStep',
  'singleStep', 'setPageStep', 'pageStep', 'setTracking', 'hasTracking',
  'setSliderDown', 'isSliderDown', 'setSliderPosition', 'sliderPosition',
  'setInvertedAppearance', 'invertedAppearance', 'setInvertedControls',
  'invertedControls', 'value', 'triggerAction', 'setValue', 'setOrientation',
  'setRange', 'valueChanged', 'sliderPressed', 'sliderMoved',
  'sliderReleased', 'rangeChanged', 'actionTriggered', 'event',
  'setRepeatAction', 'repeatAction', 'keyPressEvent', 'timerEvent',
  'wheelEvent', 'changeEvent', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSlider::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractSlider::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractSlider::~QAbstractSlider()': the destructor: Python never
    removes a C++ QAbstractSlider.
  - Qt's 'void QAbstractSlider::sliderChange(SliderChange change)': names the
    enum 'QAbstractSlider::SliderChange', whose class cannot be named here.
  - Qt's 'QAbstractSlider::QAbstractSlider(QAbstractSliderPrivate &dd,
    QWidget *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QAbstractSliderPrivate *QAbstractSlider::d_func() const':
    takes in Python what 'QAbstractSliderPrivate *QAbstractSlider::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 51 functions Qt declares: 2 not a gap; 2 forbidden.

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
  - Each name of Qt's QAbstractSlider that has no cute function yet,
    'sliderChange', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QAbstractSlider, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SliderAction(CuteNum):
    """
    The enum 'QAbstractSlider::SliderAction' of Qt, with the 8 names Qt gives
    in it.
    """

    SliderNoAction = Kee[int](0)
    SliderSingleStepAdd = Kee[int](1)
    SliderSingleStepSub = Kee[int](2)
    SliderPageStepAdd = Kee[int](3)
    SliderPageStepSub = Kee[int](4)
    SliderToMinimum = Kee[int](5)
    SliderToMaximum = Kee[int](6)
    SliderMove = Kee[int](7)

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

  #  A C++ QAbstractSlider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSlider'

  #  The functions Qt calls itself that QAbstractSlider is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'sliderChange': (
          'void QAbstractSlider::sliderChange(SliderChange)',
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
    from ..QtCore import QMetaObject
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

  def repeatAction(self) -> SliderAction:
    """
    Calls Qt's 'SliderAction QAbstractSlider::repeatAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#repeatAction

    Returns
    -------

    SliderAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SliderAction(number)'
      gives.
    """
    #  SliderAction QAbstractSlider::repeatAction() const
    return QAbstractSlider.SliderAction(self.uglySide.call(
        'ritual_ZNK15QAbstractSlider12repeatActionEv',
    ))

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

  @overload(SliderAction)
  @overload(SliderAction, int)
  @overload(SliderAction, int, int)
  def setRepeatAction(
      self,
      action: SliderAction,
      thresholdTime: int = 500,
      repeatTime: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSlider::setRepeatAction(SliderAction action,
    int thresholdTime, int repeatTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#setRepeatAction

    Parameters
    ----------

    action : SliderAction
      Passed on as its number.

    thresholdTime : int
      Passed on as it is. May be left out, as in Qt: it is then 500.

    repeatTime : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QAbstractSlider::setRepeatAction(SliderAction action, int
    #      thresholdTime, int repeatTime)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider15setRepeatActionENS_12SliderActionEii',
        action.value, thresholdTime, repeatTime,
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

  @overload(int)
  def valueChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::valueChanged(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#valueChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QAbstractSlider::valueChanged(int value)
    self.uglySide.call('ritual_ZN15QAbstractSlider12valueChangedEi', value)

  def sliderPressed(self) -> None:
    """
    Calls Qt's 'void QAbstractSlider::sliderPressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#sliderPressed
    """
    #  void QAbstractSlider::sliderPressed()
    self.uglySide.call('ritual_ZN15QAbstractSlider13sliderPressedEv')

  @overload(int)
  def sliderMoved(self, position: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::sliderMoved(int position)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#sliderMoved

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAbstractSlider::sliderMoved(int position)
    self.uglySide.call('ritual_ZN15QAbstractSlider11sliderMovedEi', position)

  def sliderReleased(self) -> None:
    """
    Calls Qt's 'void QAbstractSlider::sliderReleased()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#sliderReleased
    """
    #  void QAbstractSlider::sliderReleased()
    self.uglySide.call('ritual_ZN15QAbstractSlider14sliderReleasedEv')

  @overload(int, int)
  def rangeChanged(self, min: int, max: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::rangeChanged(int min, int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#rangeChanged

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.
    """
    #  void QAbstractSlider::rangeChanged(int min, int max)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider12rangeChangedEii', min, max,
    )

  @overload(int)
  def actionTriggered(self, action: int) -> None:
    """
    Calls Qt's 'void QAbstractSlider::actionTriggered(int action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractslider.html#actionTriggered

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QAbstractSlider::actionTriggered(int action)
    self.uglySide.call(
        'ritual_ZN15QAbstractSlider15actionTriggeredEi', action,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractSlider::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractSlider::event(QEvent *e)
    ritual = 'ritual_ZN15QAbstractSlider5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSlider5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSlider::keyPressEvent(QKeyEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#keyPressEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
    ritual = 'ritual_ZN15QAbstractSlider13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSlider13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSlider::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSlider::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN15QAbstractSlider10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSlider10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, e: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSlider::wheelEvent(QWheelEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#wheelEvent

    Parameters
    ----------

    e : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSlider::wheelEvent(QWheelEvent *e)
    ritual = 'ritual_ZN15QAbstractSlider10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSlider10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSlider::changeEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSlider::changeEvent(QEvent *e)
    ritual = 'ritual_ZN15QAbstractSlider11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSlider11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  def d_func(self) -> Optional[QAbstractSliderPrivate]:
    """
    Calls Qt's 'QAbstractSliderPrivate *QAbstractSlider::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractslider.html#d_func

    Returns
    -------

    Optional[QAbstractSliderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSliderPrivate *QAbstractSlider::d_func()
    address = self.uglySide.call('ritual_ZN15QAbstractSlider6d_funcEv')
    from . import QAbstractSliderPrivate
    return QAbstractSliderPrivate._cuteAt(address)

  @staticmethod
  def sliderChange(*__, **_) -> Never:
    """
    Qt's 'void QAbstractSlider::sliderChange(SliderChange change)': names the
    enum 'QAbstractSlider::SliderChange', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractSlider.sliderChange' has no cute function yet. Qt's "
        "'void QAbstractSlider::sliderChange(SliderChange change)': names "
        "the enum 'QAbstractSlider::SliderChange', whose class cannot be "
        "named here.")
