"""
QDoubleSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractSpinBox, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDoubleSpinBox(QAbstractSpinBox):
  """
  The cute side of Qt's QDoubleSpinBox: a plain Python object standing in
  front of one C++ QDoubleSpinBox.

  It is built on the cute 'QAbstractSpinBox', as Qt's QDoubleSpinBox is built
  on Qt's QAbstractSpinBox, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDoubleSpinBox that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'value', 'prefix',
  'setPrefix', 'suffix', 'setSuffix', 'cleanText', 'singleStep',
  'setSingleStep', 'minimum', 'setMinimum', 'maximum', 'setMaximum',
  'setRange', 'stepType', 'setStepType', 'decimals', 'setDecimals',
  'valueFromText', 'textFromValue', 'setValue'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDoubleSpinBox::~QDoubleSpinBox()': the destructor: Python never
    removes a C++ QDoubleSpinBox.

  What has no ritual
  ------------------

  12 of the 36 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QDoubleSpinBox is created at the first use, not by
    'QDoubleSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDoubleSpinBox.
  - Qt tells when it has removed the C++ QDoubleSpinBox. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDoubleSpinBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#tr

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
    #  QString QDoubleSpinBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QDoubleSpinBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDoubleSpinBox'

  #  A C++ QDoubleSpinBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDoubleSpinBox'

  #  The functions Qt calls itself that QDoubleSpinBox is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'valueFromText': (
          ('_ZNK14QDoubleSpinBox13valueFromTextERK7QString',
           ('double', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'textFromValue': (
          ('_ZNK14QDoubleSpinBox13textFromValueEd',
           ('address', 'text', ''),
           (
               ('double', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QDoubleSpinBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDoubleSpinBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QDoubleSpinBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> float:
    """
    Calls Qt's 'double QDoubleSpinBox::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#value
    """
    #  double QDoubleSpinBox::value() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox5valueEv')

  def prefix(self) -> str:
    """
    Calls Qt's 'QString QDoubleSpinBox::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDoubleSpinBox::prefix() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox6prefixEv')

  def suffix(self) -> str:
    """
    Calls Qt's 'QString QDoubleSpinBox::suffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#suffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDoubleSpinBox::suffix() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox6suffixEv')

  def cleanText(self) -> str:
    """
    Calls Qt's 'QString QDoubleSpinBox::cleanText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#cleanText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDoubleSpinBox::cleanText() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox9cleanTextEv')

  def singleStep(self) -> float:
    """
    Calls Qt's 'double QDoubleSpinBox::singleStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#singleStep
    """
    #  double QDoubleSpinBox::singleStep() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox10singleStepEv')

  def minimum(self) -> float:
    """
    Calls Qt's 'double QDoubleSpinBox::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#minimum
    """
    #  double QDoubleSpinBox::minimum() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox7minimumEv')

  def maximum(self) -> float:
    """
    Calls Qt's 'double QDoubleSpinBox::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#maximum
    """
    #  double QDoubleSpinBox::maximum() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox7maximumEv')

  def stepType(self) -> QAbstractSpinBox.StepType:
    """
    Calls Qt's 'StepType QDoubleSpinBox::stepType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#stepType

    Returns
    -------

    QAbstractSpinBox.StepType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSpinBox.StepType(number)' gives.
    """
    #  StepType QDoubleSpinBox::stepType() const
    return QAbstractSpinBox.StepType(self.uglySide.call(
        'ritual_ZNK14QDoubleSpinBox8stepTypeEv',
    ))

  def decimals(self) -> int:
    """
    Calls Qt's 'int QDoubleSpinBox::decimals() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#decimals
    """
    #  int QDoubleSpinBox::decimals() const
    return self.uglySide.call('ritual_ZNK14QDoubleSpinBox8decimalsEv')

  @overload(str)
  def valueFromText(self, text: str) -> float:
    """
    Calls Qt's 'double QDoubleSpinBox::valueFromText(const QString &text)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#valueFromText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  double QDoubleSpinBox::valueFromText(const QString &text) const
    ritual = 'ritual_ZNK14QDoubleSpinBox13valueFromTextERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QDoubleSpinBox13valueFromTextERK7QString'
    return self.uglySide.call(ritual, text)

  @overload(float)
  def textFromValue(self, val: float) -> str:
    """
    Calls Qt's 'QString QDoubleSpinBox::textFromValue(double val) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#textFromValue

    Parameters
    ----------

    val : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDoubleSpinBox::textFromValue(double val) const
    ritual = 'ritual_ZNK14QDoubleSpinBox13textFromValueEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QDoubleSpinBox13textFromValueEd'
    return self.uglySide.call(ritual, val)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setPrefix(const QString &prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDoubleSpinBox::setPrefix(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN14QDoubleSpinBox9setPrefixERK7QString', prefix,
    )

  @overload(str)
  def setSuffix(self, suffix: str) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setSuffix(const QString &suffix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setSuffix

    Parameters
    ----------

    suffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDoubleSpinBox::setSuffix(const QString &suffix)
    self.uglySide.call(
        'ritual_ZN14QDoubleSpinBox9setSuffixERK7QString', suffix,
    )

  @overload(float)
  def setSingleStep(self, val: float) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setSingleStep(double val)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setSingleStep

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setSingleStep(double val)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox13setSingleStepEd', val)

  @overload(float)
  def setMinimum(self, min: float) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setMinimum(double min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setMinimum

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setMinimum(double min)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox10setMinimumEd', min)

  @overload(float)
  def setMaximum(self, max: float) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setMaximum(double max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setMaximum

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setMaximum(double max)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox10setMaximumEd', max)

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setRange(double min, double max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setRange(double min, double max)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox8setRangeEdd', min, max)

  @overload(QAbstractSpinBox.StepType)
  def setStepType(self, stepType: QAbstractSpinBox.StepType) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setStepType(StepType stepType)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setStepType

    Parameters
    ----------

    stepType : QAbstractSpinBox.StepType
      Passed on as its number.
    """
    #  void QDoubleSpinBox::setStepType(StepType stepType)
    self.uglySide.call(
        'ritual_ZN14QDoubleSpinBox11setStepTypeEN16QAbstractSpinBox8StepTyp'
        'eE',
        stepType.value,
    )

  @overload(int)
  def setDecimals(self, prec: int) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setDecimals(int prec)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setDecimals

    Parameters
    ----------

    prec : int
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setDecimals(int prec)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox11setDecimalsEi', prec)

  @overload(float)
  def setValue(self, val: float) -> None:
    """
    Calls Qt's 'void QDoubleSpinBox::setValue(double val)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#setValue

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  void QDoubleSpinBox::setValue(double val)
    self.uglySide.call('ritual_ZN14QDoubleSpinBox8setValueEd', val)

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
    Notes what was given, for Qt's 'QDoubleSpinBox::QDoubleSpinBox(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdoublespinbox.html#QDoubleSpinBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDoubleSpinBox::QDoubleSpinBox(QWidget *parent)
    self._noteCreation(QDoubleSpinBox, lambda: Rituals.call(
        'ritual_ZN14QDoubleSpinBoxC1EP7QWidget', self._addressOf(parent),
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
