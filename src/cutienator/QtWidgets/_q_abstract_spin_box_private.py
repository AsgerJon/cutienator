"""
QAbstractSpinBoxPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractspinbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractSpinBoxPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QStyle, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QVariant
  from . import QAbstractSpinBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QVariant = WAIT['QVariant']


class QAbstractSpinBoxPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QAbstractSpinBoxPrivate: a plain Python object
  standing in front of one C++ QAbstractSpinBoxPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QAbstractSpinBoxPrivate
  is built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSpinBoxPrivate that has a ritual and that
  Python can call so far, 20 names in all: 'q_func', 'init', 'reset',
  'specialValue', 'getZeroVariant', 'setRange', 'bound', 'roundValue',
  'updateEdit', 'textFromValue', 'valueFromText', 'editorTextChanged',
  'editorCursorPositionChanged', 'newHoverControl', 'updateHoverControl',
  'clearCache', 'updateEditFieldGeometry', 'variantCompare', 'variantBound',
  'calculateAdaptiveDecimalStep'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractSpinBox *QAbstractSpinBoxPrivate::q_func() const':
    takes in Python what 'QAbstractSpinBox
    *QAbstractSpinBoxPrivate::q_func()' takes.
  - Qt's 'QAbstractSpinBoxPrivate::~QAbstractSpinBoxPrivate()': the
    destructor: Python never removes a C++ QAbstractSpinBoxPrivate.
  - Qt's 'QString QAbstractSpinBoxPrivate::stripped(const QString &text, int
    *pos) const': takes a number to change where it is.
  - Qt's 'void QAbstractSpinBoxPrivate::setValue(const QVariant &val,
    EmitPolicy ep, bool updateEdit)': names the enum 'EmitPolicy', whose
    class cannot be named here.
  - Qt's 'void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, const
    QVariant &old)': names the enum 'EmitPolicy', whose class cannot be named
    here.
  - Qt's 'void QAbstractSpinBoxPrivate::interpret(EmitPolicy ep)': names the
    enum 'EmitPolicy', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QAbstractSpinBoxPrivate.

  What to expect
  --------------

  - The C++ QAbstractSpinBoxPrivate is created at the first use, not by
    'QAbstractSpinBoxPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSpinBoxPrivate.
  - Each name of Qt's QAbstractSpinBoxPrivate that has no cute function yet,
    '__init__', 'emitSignals', 'interpret', 'setValue', 'stripped',
    'updateState', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant, QVariant)
  def variantCompare(arg1: QVariant, arg2: QVariant) -> int:
    """
    Calls Qt's 'int QAbstractSpinBoxPrivate::variantCompare(const QVariant
    &arg1, const QVariant &arg2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#variantCompare

    Parameters
    ----------

    arg1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    arg2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  int QAbstractSpinBoxPrivate::variantCompare(const QVariant &arg1,
    #      const QVariant &arg2)
    return Rituals.call(
        'ritual_ZN23QAbstractSpinBoxPrivate14variantCompareERK8QVariantS2_',
        CuteMixin._valueOf(arg1), CuteMixin._valueOf(arg2),
    )

  @staticmethod
  @overload(QVariant, QVariant, QVariant)
  def variantBound(
      min: QVariant,
      value: QVariant,
      max: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractSpinBoxPrivate::variantBound(const QVariant
    &min, const QVariant &value, const QVariant &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#variantBound

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::variantBound(const QVariant &min,
    #      const QVariant &value, const QVariant &max)
    address = Rituals.call(
        'ritual_ZN23QAbstractSpinBoxPrivate12variantBoundERK8QVariantS2_S2_',
        CuteMixin._valueOf(min), CuteMixin._valueOf(value),
        CuteMixin._valueOf(max),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSpinBoxPrivate'

  #  A C++ QAbstractSpinBoxPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSpinBoxPrivate'

  #  The functions Qt calls itself that QAbstractSpinBoxPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'emitSignals': (
          'void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy, const '
          'QVariant &)',
      ),
      'interpret': (
          'void QAbstractSpinBoxPrivate::interpret(EmitPolicy)',
      ),
  }

  #  The functions Qt calls itself that QAbstractSpinBoxPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'getZeroVariant': (
          ('_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'setRange': (
          ('_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'bound': (
          ('_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'number', ''),
           )),
      ),
      'roundValue': (
          ('_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'updateEdit': (
          ('_ZN23QAbstractSpinBoxPrivate10updateEditEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'textFromValue': (
          ('_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'valueFromText': (
          ('_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
           )),
      ),
      'editorCursorPositionChanged': (
          ('_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'newHoverControl': (
          ('_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint',
           ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'clearCache': (
          ('_ZNK23QAbstractSpinBoxPrivate10clearCacheEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateEditFieldGeometry': (
          ('_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'calculateAdaptiveDecimalStep': (
          ('_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi',
           ('address', 'value', 'QtCore:QVariant'),
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

  def specialValue(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBoxPrivate::specialValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#specialValue
    """
    #  bool QAbstractSpinBoxPrivate::specialValue() const
    return self.uglySide.call(
        'ritual_ZNK23QAbstractSpinBoxPrivate12specialValueEv',
    )

  def getZeroVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractSpinBoxPrivate::getZeroVariant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#getZeroVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::getZeroVariant() const
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  @overload(QVariant, QVariant)
  @overload(QVariant, QVariant, int)
  def bound(
      self,
      val: QVariant,
      old: Optional[QVariant] = None,
      steps: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val,
    const QVariant &old, int steps) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinboxprivate.html#bound

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    old : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    steps : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const
    #      QVariant &old, int steps) const
    if old is None:
      from ..QtCore import QVariant
      old = QVariant()
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i')
    address = self.uglySide.call(
        ritual, self._valueOf(val), self._valueOf(old), steps,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def roundValue(self, val: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant
    &val) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#roundValue

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant &val)
    #      const
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant')
    address = self.uglySide.call(ritual, self._valueOf(val))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def textFromValue(self, n: QVariant) -> str:
    """
    Calls Qt's 'QString QAbstractSpinBoxPrivate::textFromValue(const QVariant
    &n) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#textFromValue

    Parameters
    ----------

    n : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSpinBoxPrivate::textFromValue(const QVariant &n)
    #      const
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVaria'
          'nt')
    return self.uglySide.call(ritual, self._valueOf(n))

  @overload(str)
  def valueFromText(self, input: str) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractSpinBoxPrivate::valueFromText(const QString
    &input) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#valueFromText

    Parameters
    ----------

    input : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::valueFromText(const QString &input)
    #      const
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QStrin'
          'g')
    address = self.uglySide.call(ritual, input)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def calculateAdaptiveDecimalStep(self, steps: int) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int steps) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html

    Parameters
    ----------

    steps : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int
    #      steps) const
    ritual = (
        'ritual_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepE'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecima'
          'lStepEi')
    address = self.uglySide.call(ritual, steps)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractSpinBoxPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    ritual = 'ritual_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_')
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

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
    Qt's 'QAbstractSpinBoxPrivate::QAbstractSpinBoxPrivate()': leans on
    'QAbstractSpinBoxPrivate::interpret(EmitPolicy)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstractSpinBoxPrivate::QAbstractSpinBoxPrivate()': leans on "
        "'QAbstractSpinBoxPrivate::interpret(EmitPolicy)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QAbstractSpinBox]:
    """
    Calls Qt's 'QAbstractSpinBox *QAbstractSpinBoxPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#q_func

    Returns
    -------

    Optional[QAbstractSpinBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSpinBox *QAbstractSpinBoxPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QAbstractSpinBoxPrivate6q_funcEv',
    )
    from . import QAbstractSpinBox
    return QAbstractSpinBox._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinboxprivate.html#init
    """
    #  void QAbstractSpinBoxPrivate::init()
    self.uglySide.call('ritual_ZN23QAbstractSpinBoxPrivate4initEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractspinboxprivate.html#reset
    """
    #  void QAbstractSpinBoxPrivate::reset()
    self.uglySide.call('ritual_ZN23QAbstractSpinBoxPrivate5resetEv')

  def updateEdit(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::updateEdit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#updateEdit
    """
    #  void QAbstractSpinBoxPrivate::updateEdit()
    ritual = 'ritual_ZN23QAbstractSpinBoxPrivate10updateEditEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QAbstractSpinBoxPrivate10updateEditEv'
    self.uglySide.call(ritual)

  @overload(str)
  def editorTextChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::editorTextChanged(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#editorTextChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSpinBoxPrivate::editorTextChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN23QAbstractSpinBoxPrivate17editorTextChangedERK7QString',
        a0,
    )

  @overload(int, int)
  def editorCursorPositionChanged(self, oldpos: int, newpos: int) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int
    oldpos, int newpos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html

    Parameters
    ----------

    oldpos : int
      Passed on as it is.

    newpos : int
      Passed on as it is.
    """
    #  void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int oldpos,
    #      int newpos)
    ritual = (
        'ritual_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChan'
          'gedEii')
    self.uglySide.call(ritual, oldpos, newpos)

  @overload(QPoint)
  def newHoverControl(self, pos: QPoint) -> QStyle.SubControl:
    """
    Calls Qt's 'QStyle::SubControl
    QAbstractSpinBoxPrivate::newHoverControl(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#newHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  QStyle::SubControl QAbstractSpinBoxPrivate::newHoverControl(const
    #      QPoint &pos)
    ritual = 'ritual_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoin'
          't')
    return QStyle.SubControl(self.uglySide.call(ritual, self._valueOf(pos)))

  @overload(QPoint)
  def updateHoverControl(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QAbstractSpinBoxPrivate::updateHoverControl(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#updateHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QAbstractSpinBoxPrivate::updateHoverControl(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN23QAbstractSpinBoxPrivate18updateHoverControlERK6QPoint',
        self._valueOf(pos),
    )

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::clearCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html#clearCache
    """
    #  void QAbstractSpinBoxPrivate::clearCache() const
    ritual = 'ritual_ZNK23QAbstractSpinBoxPrivate10clearCacheEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAbstractSpinBoxPrivate10clearCacheEv'
    self.uglySide.call(ritual)

  def updateEditFieldGeometry(self) -> None:
    """
    Calls Qt's 'void QAbstractSpinBoxPrivate::updateEditFieldGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractspinboxprivate.html
    """
    #  void QAbstractSpinBoxPrivate::updateEditFieldGeometry()
    ritual = 'ritual_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryE'
          'v')
    self.uglySide.call(ritual)

  @staticmethod
  def emitSignals(*__, **_) -> Never:
    """
    Qt's 'void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, const
    QVariant &old)': names the enum 'EmitPolicy', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.emitSignals' has no cute function yet. "
        "Qt's 'void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, "
        "const QVariant &old)': names the enum 'EmitPolicy', whose class "
        "cannot be named here.")

  @staticmethod
  def interpret(*__, **_) -> Never:
    """
    Qt's 'void QAbstractSpinBoxPrivate::interpret(EmitPolicy ep)': names the
    enum 'EmitPolicy', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.interpret' has no cute function yet. Qt's "
        "'void QAbstractSpinBoxPrivate::interpret(EmitPolicy ep)': names "
        "the enum 'EmitPolicy', whose class cannot be named here.")

  @staticmethod
  def setValue(*__, **_) -> Never:
    """
    Qt's 'void QAbstractSpinBoxPrivate::setValue(const QVariant &val,
    EmitPolicy ep, bool updateEdit)': names the enum 'EmitPolicy', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.setValue' has no cute function yet. Qt's "
        "'void QAbstractSpinBoxPrivate::setValue(const QVariant &val, "
        "EmitPolicy ep, bool updateEdit)': names the enum 'EmitPolicy', "
        "whose class cannot be named here.")

  @staticmethod
  def stripped(*__, **_) -> Never:
    """
    Qt's 'QString QAbstractSpinBoxPrivate::stripped(const QString &text, int
    *pos) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.stripped' has no cute function yet. Qt's "
        "'QString QAbstractSpinBoxPrivate::stripped(const QString &text, "
        "int *pos) const': takes a number to change where it is.")

  @staticmethod
  def updateState(*__, **_) -> Never:
    """
    Qt's 'void QAbstractSpinBoxPrivate::updateState(bool up, bool
    fromKeyboard)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: no matching literal operator
    for call to 'operator""ms' with argument of type 'unsigned long long' or
    'const char *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QAbstractSpinBoxPrivate.updateState' has no cute function yet. "
        "Qt's 'void QAbstractSpinBoxPrivate::updateState(bool up, bool "
        "fromKeyboard)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: no matching "
        "literal operator for call to 'operator\"\"ms' with argument of "
        "type 'unsigned long long' or 'const char *', and no matching "
        "literal operator template.")
