"""
Qt3DInput::QAxisAccumulator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qaxisaccumulator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAxisAccumulator(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DInput::QAxisAccumulator: a plain Python object
  standing in front of one C++ Qt3DInput::QAxisAccumulator.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DInput::QAxisAccumulator is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAxisAccumulator that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'sourceAxis', 'sourceAxisType', 'value', 'velocity', 'scale',
  'setSourceAxis', 'setSourceAxisType', 'setScale', 'sourceAxisChanged',
  'sourceAxisTypeChanged', 'valueChanged', 'velocityChanged', 'scaleChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAxisAccumulator::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QAxisAccumulator::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAxisAccumulator::~QAxisAccumulator()': the destructor:
    Python never removes a C++ Qt3DInput::QAxisAccumulator.
  - Qt's 'const QAxisAccumulatorPrivate
    *Qt3DInput::QAxisAccumulator::d_func() const': takes in Python what
    'QAxisAccumulatorPrivate *Qt3DInput::QAxisAccumulator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAxisAccumulator is created at the first use, not by
    'Qt3DInput::QAxisAccumulator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAxisAccumulator.
  - Qt tells when it has removed the C++ Qt3DInput::QAxisAccumulator. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DInput::QAxisAccumulator, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SourceAxisType(CuteNum):
    """
    The enum 'Qt3DInput::QAxisAccumulator::SourceAxisType' of Qt, with the 2
    names Qt gives in it.
    """

    Velocity = Kee[int](0)
    Acceleration = Kee[int](1)

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
    Calls Qt's 'QString Qt3DInput::QAxisAccumulator::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#tr

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
    #  QString Qt3DInput::QAxisAccumulator::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAxisAccumulator'

  #  A C++ Qt3DInput::QAxisAccumulator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAxisAccumulator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QAxisAccumulator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAxisAccumulator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceAxis(self) -> Optional[Qt3DInput.QAxis]:
    """
    Calls Qt's 'Qt3DInput::QAxis *Qt3DInput::QAxisAccumulator::sourceAxis()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#sourceAxis

    Returns
    -------

    Optional[Qt3DInput.QAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DInput::QAxis *Qt3DInput::QAxisAccumulator::sourceAxis() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator10sourceAxisEv',
    )
    return Qt3DInput.QAxis._cuteAt(address)

  def sourceAxisType(self) -> SourceAxisType:
    """
    Calls Qt's 'SourceAxisType Qt3DInput::QAxisAccumulator::sourceAxisType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#sourceAxisType

    Returns
    -------

    SourceAxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SourceAxisType(number)'
      gives.
    """
    #  SourceAxisType Qt3DInput::QAxisAccumulator::sourceAxisType() const
    return QAxisAccumulator.SourceAxisType(self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator14sourceAxisTypeEv',
    ))

  def value(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QAxisAccumulator::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#value
    """
    #  float Qt3DInput::QAxisAccumulator::value() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator5valueEv',
    )

  def velocity(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QAxisAccumulator::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#velocity
    """
    #  float Qt3DInput::QAxisAccumulator::velocity() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator8velocityEv',
    )

  def scale(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QAxisAccumulator::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#scale
    """
    #  float Qt3DInput::QAxisAccumulator::scale() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QAxisAccumulator5scaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QAxis'])
  @overload(NoneType)
  def setSourceAxis(self, sourceAxis: Optional[Qt3DInput.QAxis]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAxisAccumulator::setSourceAxis(Qt3DInput::QAxis
    *sourceAxis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#setSourceAxis

    Parameters
    ----------

    sourceAxis : Optional[Qt3DInput.QAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAxisAccumulator::setSourceAxis(Qt3DInput::QAxis
    #      *sourceAxis)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator13setSourceAxisEPNS_5QAxisE',
        self._addressOf(sourceAxis),
    )

  @overload(SourceAxisType)
  def setSourceAxisType(self, sourceAxisType: SourceAxisType) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAxisAccumulator::setSourceAxisType(QAxisAccumulator::
    SourceAxisType sourceAxisType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#setSourceAxisType

    Parameters
    ----------

    sourceAxisType : SourceAxisType
      Passed on as its number.
    """
    #  void Qt3DInput::QAxisAccumulator::setSourceAxisType(QAxisAccumulator::
    #      SourceAxisType sourceAxisType)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator17setSourceAxisTypeENS0_14Sou'
        'rceAxisTypeE',
        sourceAxisType.value,
    )

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulator::setScale(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulator::setScale(float scale)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator8setScaleEf', scale,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAxisAccumulator::QAxisAccumulator(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#QAxisAccumulator

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QAxisAccumulator::QAxisAccumulator(Qt3DCore::QNode *parent)
    self._noteCreation(QAxisAccumulator, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulatorC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QAxis'])
  @overload(NoneType)
  def sourceAxisChanged(self, sourceAxis: Optional[Qt3DInput.QAxis]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAxisAccumulator::sourceAxisChanged(Qt3DInput::QAxis
    *sourceAxis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#sourceAxisChanged

    Parameters
    ----------

    sourceAxis : Optional[Qt3DInput.QAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAxisAccumulator::sourceAxisChanged(Qt3DInput::QAxis
    #      *sourceAxis)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator17sourceAxisChangedEPNS_5QAxi'
        'sE',
        self._addressOf(sourceAxis),
    )

  @overload(SourceAxisType)
  def sourceAxisTypeChanged(self, sourceAxisType: SourceAxisType) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAxisAccumulator::sourceAxisTypeChanged(QAxisAccumulator::
    SourceAxisType sourceAxisType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html

    Parameters
    ----------

    sourceAxisType : SourceAxisType
      Passed on as its number.
    """
    #  void Qt3DInput::QAxisAccumulator::sourceAxisTypeChanged(
    #      QAxisAccumulator::SourceAxisType sourceAxisType)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator21sourceAxisTypeChangedENS0_1'
        '4SourceAxisTypeE',
        sourceAxisType.value,
    )

  @overload(float)
  def valueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulator::valueChanged(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#valueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulator::valueChanged(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator12valueChangedEf', value,
    )

  @overload(float)
  def velocityChanged(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulator::velocityChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#velocityChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulator::velocityChanged(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator15velocityChangedEf', value,
    )

  @overload(float)
  def scaleChanged(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulator::scaleChanged(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#scaleChanged

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulator::scaleChanged(float scale)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator12scaleChangedEf', scale,
    )

  def d_func(self) -> Optional[Qt3DInput.QAxisAccumulatorPrivate]:
    """
    Calls Qt's 'QAxisAccumulatorPrivate
    *Qt3DInput::QAxisAccumulator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulator.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAxisAccumulatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAxisAccumulatorPrivate *Qt3DInput::QAxisAccumulator::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput16QAxisAccumulator6d_funcEv',
    )
    return Qt3DInput.QAxisAccumulatorPrivate._cuteAt(address)
