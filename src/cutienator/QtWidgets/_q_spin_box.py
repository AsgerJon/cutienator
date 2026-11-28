"""
QSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractSpinBox, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpinBox(QAbstractSpinBox):
  """
  The cute side of Qt's QSpinBox: a plain Python object standing in front of
  one C++ QSpinBox.

  It is built on the cute 'QAbstractSpinBox', as Qt's QSpinBox is built on
  Qt's QAbstractSpinBox, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpinBox that has a ritual and that Python can call
  so far, 25 names in all: 'metaObject', 'tr', 'value', 'prefix',
  'setPrefix', 'suffix', 'setSuffix', 'cleanText', 'singleStep',
  'setSingleStep', 'minimum', 'setMinimum', 'maximum', 'setMaximum',
  'setRange', 'stepType', 'setStepType', 'displayIntegerBase',
  'setDisplayIntegerBase', 'event', 'valueFromText', 'textFromValue',
  'setValue', 'valueChanged', 'textChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSpinBox::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QSpinBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSpinBox::~QSpinBox()': the destructor: Python never removes a C++
    QSpinBox.
  - Qt's 'QValidator::State QSpinBox::validate(QString &input, int &pos)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSpinBox::fixup(QString &str) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSpinBoxPrivate *QSpinBox::d_func()': gives 'QSpinBoxPrivate',
    which has no cute class yet.
  - Qt's 'const QSpinBoxPrivate *QSpinBox::d_func() const': gives
    'QSpinBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSpinBox is created at the first use, not by 'QSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpinBox.
  - Qt tells when it has removed the C++ QSpinBox. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QSpinBox::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#tr

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
    #  QString QSpinBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QSpinBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpinBox'

  #  A C++ QSpinBox Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpinBox'

  #  The functions Qt calls itself that QSpinBox is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'valueFromText': (
          ('_ZNK8QSpinBox13valueFromTextERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'textFromValue': (
          ('_ZNK8QSpinBox13textFromValueEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QSpinBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSpinBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QSpinBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> int:
    """
    Calls Qt's 'int QSpinBox::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#value
    """
    #  int QSpinBox::value() const
    return self.uglySide.call('ritual_ZNK8QSpinBox5valueEv')

  def prefix(self) -> str:
    """
    Calls Qt's 'QString QSpinBox::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpinBox::prefix() const
    return self.uglySide.call('ritual_ZNK8QSpinBox6prefixEv')

  def suffix(self) -> str:
    """
    Calls Qt's 'QString QSpinBox::suffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#suffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpinBox::suffix() const
    return self.uglySide.call('ritual_ZNK8QSpinBox6suffixEv')

  def cleanText(self) -> str:
    """
    Calls Qt's 'QString QSpinBox::cleanText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#cleanText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpinBox::cleanText() const
    return self.uglySide.call('ritual_ZNK8QSpinBox9cleanTextEv')

  def singleStep(self) -> int:
    """
    Calls Qt's 'int QSpinBox::singleStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#singleStep
    """
    #  int QSpinBox::singleStep() const
    return self.uglySide.call('ritual_ZNK8QSpinBox10singleStepEv')

  def minimum(self) -> int:
    """
    Calls Qt's 'int QSpinBox::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#minimum
    """
    #  int QSpinBox::minimum() const
    return self.uglySide.call('ritual_ZNK8QSpinBox7minimumEv')

  def maximum(self) -> int:
    """
    Calls Qt's 'int QSpinBox::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#maximum
    """
    #  int QSpinBox::maximum() const
    return self.uglySide.call('ritual_ZNK8QSpinBox7maximumEv')

  def stepType(self) -> QAbstractSpinBox.StepType:
    """
    Calls Qt's 'StepType QSpinBox::stepType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#stepType

    Returns
    -------

    QAbstractSpinBox.StepType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSpinBox.StepType(number)' gives.
    """
    #  StepType QSpinBox::stepType() const
    return QAbstractSpinBox.StepType(self.uglySide.call(
        'ritual_ZNK8QSpinBox8stepTypeEv',
    ))

  def displayIntegerBase(self) -> int:
    """
    Calls Qt's 'int QSpinBox::displayIntegerBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#displayIntegerBase
    """
    #  int QSpinBox::displayIntegerBase() const
    return self.uglySide.call('ritual_ZNK8QSpinBox18displayIntegerBaseEv')

  @overload(str)
  def valueFromText(self, text: str) -> int:
    """
    Calls Qt's 'int QSpinBox::valueFromText(const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#valueFromText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QSpinBox::valueFromText(const QString &text) const
    ritual = 'ritual_ZNK8QSpinBox13valueFromTextERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSpinBox13valueFromTextERK7QString'
    return self.uglySide.call(ritual, text)

  @overload(int)
  def textFromValue(self, val: int) -> str:
    """
    Calls Qt's 'QString QSpinBox::textFromValue(int val) const'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#textFromValue

    Parameters
    ----------

    val : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpinBox::textFromValue(int val) const
    ritual = 'ritual_ZNK8QSpinBox13textFromValueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSpinBox13textFromValueEi'
    return self.uglySide.call(ritual, val)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QSpinBox::setPrefix(const QString &prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSpinBox::setPrefix(const QString &prefix)
    self.uglySide.call('ritual_ZN8QSpinBox9setPrefixERK7QString', prefix)

  @overload(str)
  def setSuffix(self, suffix: str) -> None:
    """
    Calls Qt's 'void QSpinBox::setSuffix(const QString &suffix)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setSuffix

    Parameters
    ----------

    suffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSpinBox::setSuffix(const QString &suffix)
    self.uglySide.call('ritual_ZN8QSpinBox9setSuffixERK7QString', suffix)

  @overload(int)
  def setSingleStep(self, val: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setSingleStep(int val)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setSingleStep

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  void QSpinBox::setSingleStep(int val)
    self.uglySide.call('ritual_ZN8QSpinBox13setSingleStepEi', val)

  @overload(int)
  def setMinimum(self, min: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setMinimum(int min)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setMinimum

    Parameters
    ----------

    min : int
      Passed on as it is.
    """
    #  void QSpinBox::setMinimum(int min)
    self.uglySide.call('ritual_ZN8QSpinBox10setMinimumEi', min)

  @overload(int)
  def setMaximum(self, max: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setMaximum(int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setMaximum

    Parameters
    ----------

    max : int
      Passed on as it is.
    """
    #  void QSpinBox::setMaximum(int max)
    self.uglySide.call('ritual_ZN8QSpinBox10setMaximumEi', max)

  @overload(int, int)
  def setRange(self, min: int, max: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setRange(int min, int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setRange

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.
    """
    #  void QSpinBox::setRange(int min, int max)
    self.uglySide.call('ritual_ZN8QSpinBox8setRangeEii', min, max)

  @overload(QAbstractSpinBox.StepType)
  def setStepType(self, stepType: QAbstractSpinBox.StepType) -> None:
    """
    Calls Qt's 'void QSpinBox::setStepType(StepType stepType)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setStepType

    Parameters
    ----------

    stepType : QAbstractSpinBox.StepType
      Passed on as its number.
    """
    #  void QSpinBox::setStepType(StepType stepType)
    self.uglySide.call(
        'ritual_ZN8QSpinBox11setStepTypeEN16QAbstractSpinBox8StepTypeE',
        stepType.value,
    )

  @overload(int)
  def setDisplayIntegerBase(self, base: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setDisplayIntegerBase(int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspinbox.html#setDisplayIntegerBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QSpinBox::setDisplayIntegerBase(int base)
    self.uglySide.call('ritual_ZN8QSpinBox21setDisplayIntegerBaseEi', base)

  @overload(int)
  def setValue(self, val: int) -> None:
    """
    Calls Qt's 'void QSpinBox::setValue(int val)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#setValue

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  void QSpinBox::setValue(int val)
    self.uglySide.call('ritual_ZN8QSpinBox8setValueEi', val)

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
    Notes what was given, for Qt's 'QSpinBox::QSpinBox(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#QSpinBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSpinBox::QSpinBox(QWidget *parent)
    self._noteCreation(QSpinBox, lambda: Rituals.call(
        'ritual_ZN8QSpinBoxC1EP7QWidget', self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSpinBox::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSpinBox::event(QEvent *event)
    ritual = 'ritual_ZN8QSpinBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSpinBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def valueChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QSpinBox::valueChanged(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#valueChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSpinBox::valueChanged(int a0)
    self.uglySide.call('ritual_ZN8QSpinBox12valueChangedEi', a0)

  @overload(str)
  def textChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QSpinBox::textChanged(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qspinbox.html#textChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSpinBox::textChanged(const QString &a0)
    self.uglySide.call('ritual_ZN8QSpinBox11textChangedERK7QString', a0)
