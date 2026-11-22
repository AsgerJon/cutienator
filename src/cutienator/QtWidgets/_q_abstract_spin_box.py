"""
QAbstractSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QTimerEvent, QVariant
  from ..QtGui import QCloseEvent, QContextMenuEvent, QFocusEvent, QHideEvent
  from ..QtGui import QKeyEvent, QMouseEvent, QPaintEvent, QResizeEvent
  from ..QtGui import QShowEvent, QWheelEvent
  from . import QStyleOptionSpinBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHideEvent = WAIT['QHideEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QStyleOptionSpinBox = WAIT['QStyleOptionSpinBox']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSpinBox(QWidget):
  """
  The cute side of Qt's QAbstractSpinBox: a plain Python object standing in
  front of one C++ QAbstractSpinBox.

  It is built on the cute 'QWidget', as Qt's QAbstractSpinBox is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSpinBox that has a ritual and that Python
  can call so far, 51 names in all: 'metaObject', 'tr', 'buttonSymbols',
  'setButtonSymbols', 'setCorrectionMode', 'correctionMode',
  'hasAcceptableInput', 'text', 'specialValueText', 'setSpecialValueText',
  'wrapping', 'setWrapping', 'setReadOnly', 'isReadOnly',
  'setKeyboardTracking', 'keyboardTracking', 'setAlignment', 'alignment',
  'setFrame', 'hasFrame', 'setAccelerated', 'isAccelerated',
  'setGroupSeparatorShown', 'isGroupSeparatorShown', 'sizeHint',
  'minimumSizeHint', 'interpretText', 'event', 'inputMethodQuery', 'stepBy',
  'stepUp', 'stepDown', 'selectAll', 'clear', 'resizeEvent', 'keyPressEvent',
  'keyReleaseEvent', 'wheelEvent', 'focusInEvent', 'focusOutEvent',
  'contextMenuEvent', 'changeEvent', 'closeEvent', 'hideEvent',
  'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'timerEvent',
  'paintEvent', 'showEvent', 'initStyleOption'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractSpinBox::~QAbstractSpinBox()': the destructor: Python
    never removes a C++ QAbstractSpinBox.

  What has no ritual
  ------------------

  16 of the 69 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 4 protected; 3 private; 2 a signal; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QAbstractSpinBox is created at the first use, not by
    'QAbstractSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSpinBox.
  - Qt tells when it has removed the C++ QAbstractSpinBox. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractSpinBox, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ButtonSymbols(CuteNum):
    """
    The enum 'QAbstractSpinBox::ButtonSymbols' of Qt, with the 3 names Qt
    gives in it.
    """

    UpDownArrows = Kee[int](0)
    PlusMinus = Kee[int](1)
    NoButtons = Kee[int](2)

  class CorrectionMode(CuteNum):
    """
    The enum 'QAbstractSpinBox::CorrectionMode' of Qt, with the 2 names Qt
    gives in it.
    """

    CorrectToPreviousValue = Kee[int](0)
    CorrectToNearestValue = Kee[int](1)

  class StepEnabledFlag(CuteFlags):
    """
    The flags enum 'QAbstractSpinBox::StepEnabledFlag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QAbstractSpinBox::StepEnabled'.
    """

    StepNone = 0x0
    StepUpEnabled = 0x1
    StepDownEnabled = 0x2

  StepEnabled = StepEnabledFlag

  class StepType(CuteNum):
    """
    The enum 'QAbstractSpinBox::StepType' of Qt, with the 2 names Qt gives in
    it.
    """

    DefaultStepType = Kee[int](0)
    AdaptiveDecimalStepType = Kee[int](1)

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
    Calls Qt's 'QString QAbstractSpinBox::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#tr

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
    #  QString QAbstractSpinBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QAbstractSpinBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSpinBox'

  #  A C++ QAbstractSpinBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSpinBox'

  #  The functions Qt calls itself that QAbstractSpinBox is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'validate': (
          'QValidator::State QAbstractSpinBox::validate(QString &, int &) '
          'const',
      ),
      'fixup': (
          'void QAbstractSpinBox::fixup(QString &) const',
      ),
      'stepEnabled': (
          'StepEnabled QAbstractSpinBox::stepEnabled() const',
      ),
  }

  #  The functions Qt calls itself that QAbstractSpinBox is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'stepBy': (
          ('_ZN16QAbstractSpinBox6stepByEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'clear': (
          ('_ZN16QAbstractSpinBox5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initStyleOption': (
          ('_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionSpinBox'),
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
    Calls Qt's 'const QMetaObject *QAbstractSpinBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSpinBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonSymbols(self) -> ButtonSymbols:
    """
    Calls Qt's 'ButtonSymbols QAbstractSpinBox::buttonSymbols() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#buttonSymbols

    Returns
    -------

    ButtonSymbols
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ButtonSymbols(number)'
      gives.
    """
    #  ButtonSymbols QAbstractSpinBox::buttonSymbols() const
    return QAbstractSpinBox.ButtonSymbols(self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox13buttonSymbolsEv',
    ))

  def correctionMode(self) -> CorrectionMode:
    """
    Calls Qt's 'CorrectionMode QAbstractSpinBox::correctionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#correctionMode

    Returns
    -------

    CorrectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CorrectionMode(number)'
      gives.
    """
    #  CorrectionMode QAbstractSpinBox::correctionMode() const
    return QAbstractSpinBox.CorrectionMode(self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox14correctionModeEv',
    ))

  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::hasAcceptableInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#hasAcceptableInput
    """
    #  bool QAbstractSpinBox::hasAcceptableInput() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox18hasAcceptableInputEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QAbstractSpinBox::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSpinBox::text() const
    return self.uglySide.call('ritual_ZNK16QAbstractSpinBox4textEv')

  def specialValueText(self) -> str:
    """
    Calls Qt's 'QString QAbstractSpinBox::specialValueText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#specialValueText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSpinBox::specialValueText() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox16specialValueTextEv',
    )

  def wrapping(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::wrapping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#wrapping
    """
    #  bool QAbstractSpinBox::wrapping() const
    return self.uglySide.call('ritual_ZNK16QAbstractSpinBox8wrappingEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#isReadOnly
    """
    #  bool QAbstractSpinBox::isReadOnly() const
    return self.uglySide.call('ritual_ZNK16QAbstractSpinBox10isReadOnlyEv')

  def keyboardTracking(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::keyboardTracking() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#keyboardTracking
    """
    #  bool QAbstractSpinBox::keyboardTracking() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox16keyboardTrackingEv',
    )

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QAbstractSpinBox::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QAbstractSpinBox::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox9alignmentEv',
    ))

  def hasFrame(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::hasFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#hasFrame
    """
    #  bool QAbstractSpinBox::hasFrame() const
    return self.uglySide.call('ritual_ZNK16QAbstractSpinBox8hasFrameEv')

  def isAccelerated(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::isAccelerated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#isAccelerated
    """
    #  bool QAbstractSpinBox::isAccelerated() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox13isAcceleratedEv',
    )

  def isGroupSeparatorShown(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::isGroupSeparatorShown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#isGroupSeparatorShown
    """
    #  bool QAbstractSpinBox::isGroupSeparatorShown() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstractSpinBox21isGroupSeparatorShownEv',
    )

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractSpinBox::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractSpinBox::sizeHint() const
    ritual = 'ritual_ZNK16QAbstractSpinBox8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAbstractSpinBox8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractSpinBox::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractSpinBox::minimumSizeHint() const
    ritual = 'ritual_ZNK16QAbstractSpinBox15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAbstractSpinBox15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, a0: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#inputMethodQuery

    Parameters
    ----------

    a0 : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
    #      const
    ritual = (
        'ritual_ZNK16QAbstractSpinBox16inputMethodQueryEN2Qt16InputMethodQu'
        'eryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QAbstractSpinBox16inputMethodQueryEN2Qt16InputMe'
          'thodQueryE')
    address = self.uglySide.call(ritual, a0.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ButtonSymbols)
  def setButtonSymbols(self, bs: ButtonSymbols) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setButtonSymbols(ButtonSymbols bs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setButtonSymbols

    Parameters
    ----------

    bs : ButtonSymbols
      Passed on as its number.
    """
    #  void QAbstractSpinBox::setButtonSymbols(ButtonSymbols bs)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox16setButtonSymbolsENS_13ButtonSymbolsE',
        bs.value,
    )

  @overload(CorrectionMode)
  def setCorrectionMode(self, cm: CorrectionMode) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setCorrectionMode(CorrectionMode cm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setCorrectionMode

    Parameters
    ----------

    cm : CorrectionMode
      Passed on as its number.
    """
    #  void QAbstractSpinBox::setCorrectionMode(CorrectionMode cm)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox17setCorrectionModeENS_14CorrectionMode'
        'E',
        cm.value,
    )

  @overload(str)
  def setSpecialValueText(self, txt: str) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setSpecialValueText(const QString
    &txt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setSpecialValueText

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSpinBox::setSpecialValueText(const QString &txt)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox19setSpecialValueTextERK7QString', txt,
    )

  @overload(bool)
  def setWrapping(self, w: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setWrapping(bool w)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#setWrapping

    Parameters
    ----------

    w : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setWrapping(bool w)
    self.uglySide.call('ritual_ZN16QAbstractSpinBox11setWrappingEb', w)

  @overload(bool)
  def setReadOnly(self, r: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setReadOnly(bool r)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#setReadOnly

    Parameters
    ----------

    r : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setReadOnly(bool r)
    self.uglySide.call('ritual_ZN16QAbstractSpinBox11setReadOnlyEb', r)

  @overload(bool)
  def setKeyboardTracking(self, kt: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setKeyboardTracking(bool kt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setKeyboardTracking

    Parameters
    ----------

    kt : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setKeyboardTracking(bool kt)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox19setKeyboardTrackingEb', kt,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, flag: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setAlignment(Qt::Alignment flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#setAlignment

    Parameters
    ----------

    flag : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractSpinBox::setAlignment(Qt::Alignment flag)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox12setAlignmentE6QFlagsIN2Qt13AlignmentF'
        'lagEE',
        flag.value,
    )

  @overload(bool)
  def setFrame(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setFrame(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#setFrame

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setFrame(bool a0)
    self.uglySide.call('ritual_ZN16QAbstractSpinBox8setFrameEb', a0)

  @overload(bool)
  def setAccelerated(self, on: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setAccelerated(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setAccelerated

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setAccelerated(bool on)
    self.uglySide.call('ritual_ZN16QAbstractSpinBox14setAcceleratedEb', on)

  @overload(bool)
  def setGroupSeparatorShown(self, shown: bool) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::setGroupSeparatorShown(bool shown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#setGroupSeparatorShown

    Parameters
    ----------

    shown : bool
      Passed on as it is.
    """
    #  void QAbstractSpinBox::setGroupSeparatorShown(bool shown)
    self.uglySide.call(
        'ritual_ZN16QAbstractSpinBox22setGroupSeparatorShownEb', shown,
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
    Notes what was given, for Qt's
    'QAbstractSpinBox::QAbstractSpinBox(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#QAbstractSpinBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractSpinBox::QAbstractSpinBox(QWidget *parent)
    self._noteCreation(QAbstractSpinBox, lambda: Rituals.call(
        'ritual_ZN16QAbstractSpinBoxC1EP7QWidget', self._addressOf(parent),
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

  def interpretText(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::interpretText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#interpretText
    """
    #  void QAbstractSpinBox::interpretText()
    self.uglySide.call('ritual_ZN16QAbstractSpinBox13interpretTextEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBox::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractSpinBox::event(QEvent *event)
    ritual = 'ritual_ZN16QAbstractSpinBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstractSpinBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def stepBy(self, steps: int) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::stepBy(int steps)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#stepBy

    Parameters
    ----------

    steps : int
      Passed on as it is.
    """
    #  void QAbstractSpinBox::stepBy(int steps)
    ritual = 'ritual_ZN16QAbstractSpinBox6stepByEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstractSpinBox6stepByEi'
    self.uglySide.call(ritual, steps)

  def stepUp(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::stepUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#stepUp
    """
    #  void QAbstractSpinBox::stepUp()
    self.uglySide.call('ritual_ZN16QAbstractSpinBox6stepUpEv')

  def stepDown(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::stepDown()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#stepDown
    """
    #  void QAbstractSpinBox::stepDown()
    self.uglySide.call('ritual_ZN16QAbstractSpinBox8stepDownEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#selectAll
    """
    #  void QAbstractSpinBox::selectAll()
    self.uglySide.call('ritual_ZN16QAbstractSpinBox9selectAllEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#clear
    """
    #  void QAbstractSpinBox::clear()
    ritual = 'ritual_ZN16QAbstractSpinBox5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstractSpinBox5clearEv'
    self.uglySide.call(ritual)

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox11resizeEventEP12QResizeEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox13keyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox15keyReleaseEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox10wheelEventEP11QWheelEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox13focusOutEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox16contextMenuEventEP17QContextMenuE'
        'vent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::changeEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox11changeEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, event: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::closeEvent(QCloseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#closeEvent

    Parameters
    ----------

    event : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox10closeEventEP11QCloseEvent',
        self._addressOf(event),
    )

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::hideEvent(QHideEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::hideEvent(QHideEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox9hideEventEP10QHideEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox15mousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox14mouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox10paintEventEP11QPaintEvent',
        self._addressOf(event),
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinbox.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::showEvent(QShowEvent *event)
    self.uglySide.call(
        'ritual_own_ZN16QAbstractSpinBox9showEventEP10QShowEvent',
        self._addressOf(event),
    )

  @overload(QStyleOptionSpinBox)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionSpinBox]) -> None:
    """
    Calls Qt's 'void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox
    *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinbox.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionSpinBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option)
    #      const
    self.uglySide.call(
        'ritual_own_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionS'
        'pinBox',
        self._addressOf(option),
    )
