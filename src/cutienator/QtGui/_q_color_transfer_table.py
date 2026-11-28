"""
QColorTransferTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortransfertable_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColorTransferTable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QColorTransferFunction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorTransferFunction = WAIT['QColorTransferFunction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColorTransferTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTransferTable: a plain Python object standing
  in front of one C++ QColorTransferTable.

  C++ hands a QColorTransferTable around as a copy, so every C++
  QColorTransferTable behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorTransferTable that has a ritual and that
  Python can call so far, 9 names in all: 'isEmpty', 'isIdentity',
  'checkValidity', 'checkInvertibility', 'apply', 'applyInverse',
  'asColorTransferFunction', '__ne__', '__eq__'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTransferTable::QColorTransferTable(uint32_t size, const
    QList<uint8_t> &table, Type type)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QColorTransferTable::QColorTransferTable(uint32_t size, const
    QList<uint16_t> &table, Type type)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QColorTransferTable::~QColorTransferTable()': the destructor:
    Python removes its C++ QColorTransferTable by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QColorTransferTable is created at the first use, not by
    'QColorTransferTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTransferTable back gives a copy the ritual made
    for Python, in a new cute QColorTransferTable.
  - Each name of Qt's QColorTransferTable that has no cute function yet,
    'inverseLookup', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QColorTransferTable, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QColorTransferTable::Type' of Qt, with the 2 names Qt gives in
    it.
    """

    TwoWay = Kee[int](0)
    OneWay = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTransferTable'

  #  Qt's '~QColorTransferTable()'. Naming it makes this a value class:
  #  Python owns every C++ QColorTransferTable behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QColorTransferTableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferTable::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransfertable.html#isEmpty
    """
    #  bool QColorTransferTable::isEmpty() const
    return self.uglySide.call('ritual_ZNK19QColorTransferTable7isEmptyEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferTable::isIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#isIdentity
    """
    #  bool QColorTransferTable::isIdentity() const
    return self.uglySide.call(
        'ritual_ZNK19QColorTransferTable10isIdentityEv',
    )

  def checkValidity(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferTable::checkValidity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#checkValidity
    """
    #  bool QColorTransferTable::checkValidity() const
    return self.uglySide.call(
        'ritual_ZNK19QColorTransferTable13checkValidityEv',
    )

  def checkInvertibility(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferTable::checkInvertibility() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#checkInvertibility
    """
    #  bool QColorTransferTable::checkInvertibility() const
    return self.uglySide.call(
        'ritual_ZNK19QColorTransferTable18checkInvertibilityEv',
    )

  @overload(float)
  def apply(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTransferTable::apply(float x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransfertable.html#apply

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferTable::apply(float x) const
    return self.uglySide.call('ritual_ZNK19QColorTransferTable5applyEf', x)

  @overload(float)
  @overload(float, float)
  def applyInverse(self, x: float, resultLargerThan: float = 0.0) -> float:
    """
    Calls Qt's 'float QColorTransferTable::applyInverse(float x, float
    resultLargerThan) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#applyInverse

    Parameters
    ----------

    x : float
      Passed on as it is.

    resultLargerThan : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  float QColorTransferTable::applyInverse(float x, float
    #      resultLargerThan) const
    return self.uglySide.call(
        'ritual_ZNK19QColorTransferTable12applyInverseEff',
        x, resultLargerThan,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __ne__(self, t2: QColorTransferTable) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorTransferTable &t1, const
    QColorTransferTable &t2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#operator!=

    Parameters
    ----------

    t2 : QColorTransferTable
      Passed on as a value: Qt reads the C++ QColorTransferTable, which stays
      Python's own.
    """
    #  bool operator!=(const QColorTransferTable &t1, const
    #      QColorTransferTable &t2)
    return Rituals.call(
        'ritual_ZneRK19QColorTransferTableS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(t2),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, t2: QColorTransferTable) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorTransferTable &t1, const
    QColorTransferTable &t2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#operator==

    Parameters
    ----------

    t2 : QColorTransferTable
      Passed on as a value: Qt reads the C++ QColorTransferTable, which stays
      Python's own.
    """
    #  bool operator==(const QColorTransferTable &t1, const
    #      QColorTransferTable &t2)
    return Rituals.call(
        'ritual_ZeqRK19QColorTransferTableS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(t2),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QColorTransferTable::QColorTransferTable()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#QColorTransferTable
    """
    #  QColorTransferTable::QColorTransferTable()
    self._noteCreation(QColorTransferTable, lambda: Rituals.call(
        'ritual_ZN19QColorTransferTableC1Ev',
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

  @overload(QColorTransferFunction)
  @overload(NoneType)
  def asColorTransferFunction(
      self,
      transferFn: Optional[QColorTransferFunction],
  ) -> bool:
    """
    Calls Qt's 'bool
    QColorTransferTable::asColorTransferFunction(QColorTransferFunction
    *transferFn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfertable.html#asColorTransferFunction

    Parameters
    ----------

    transferFn : Optional[QColorTransferFunction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QColorTransferTable::asColorTransferFunction(
    #      QColorTransferFunction *transferFn)
    return self.uglySide.call(
        'ritual_ZN19QColorTransferTable23asColorTransferFunctionEP22QColorT'
        'ransferFunction',
        self._addressOf(transferFn),
    )

  @staticmethod
  def inverseLookup(*__, **_) -> Never:
    """
    Qt's 'QColorTransferTable::inverseLookup': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QColorTransferTable.inverseLookup' has no cute function yet. Qt's "
        "'QColorTransferTable::inverseLookup': a template: a pattern and no "
        "single function.")
