"""
Qt3DInput::QButtonAxisInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qbuttonaxisinput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QButtonAxisInput(Qt3DInput.QAbstractAxisInput):
  """
  The cute side of Qt's Qt3DInput::QButtonAxisInput: a plain Python object
  standing in front of one C++ Qt3DInput::QButtonAxisInput.

  It is built on the cute 'Qt3DInput::QAbstractAxisInput', as Qt's
  Qt3DInput::QButtonAxisInput is built on Qt's Qt3DInput::QAbstractAxisInput,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QButtonAxisInput that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr', 'scale',
  'acceleration', 'deceleration', 'setScale', 'setAcceleration',
  'setDeceleration', 'scaleChanged', 'accelerationChanged',
  'decelerationChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QButtonAxisInput::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QButtonAxisInput::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QButtonAxisInput::~QButtonAxisInput()': the destructor:
    Python never removes a C++ Qt3DInput::QButtonAxisInput.
  - Qt's 'QList<int> Qt3DInput::QButtonAxisInput::buttons() const': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DInput::QButtonAxisInput::setButtons(const QList<int>
    &buttons)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DInput::QButtonAxisInput::buttonsChanged(const QList<int>
    &buttons)': takes a type Python has no way to hand over yet.
  - Qt's 'const QButtonAxisInputPrivate
    *Qt3DInput::QButtonAxisInput::d_func() const': takes in Python what
    'QButtonAxisInputPrivate *Qt3DInput::QButtonAxisInput::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QButtonAxisInput is created at the first use, not by
    'Qt3DInput::QButtonAxisInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QButtonAxisInput.
  - Qt tells when it has removed the C++ Qt3DInput::QButtonAxisInput. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QButtonAxisInput that has no cute function
    yet, 'buttons', 'buttonsChanged', 'setButtons', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DInput::QButtonAxisInput::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#tr

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
    #  QString Qt3DInput::QButtonAxisInput::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QButtonAxisInput'

  #  A C++ Qt3DInput::QButtonAxisInput Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QButtonAxisInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QButtonAxisInput::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QButtonAxisInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QButtonAxisInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scale(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QButtonAxisInput::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#scale
    """
    #  float Qt3DInput::QButtonAxisInput::scale() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QButtonAxisInput5scaleEv',
    )

  def acceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QButtonAxisInput::acceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#acceleration
    """
    #  float Qt3DInput::QButtonAxisInput::acceleration() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QButtonAxisInput12accelerationEv',
    )

  def deceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QButtonAxisInput::deceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#deceleration
    """
    #  float Qt3DInput::QButtonAxisInput::deceleration() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QButtonAxisInput12decelerationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::setScale(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::setScale(float scale)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput8setScaleEf', scale,
    )

  @overload(float)
  def setAcceleration(self, acceleration: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::setAcceleration(float
    acceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#setAcceleration

    Parameters
    ----------

    acceleration : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::setAcceleration(float acceleration)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput15setAccelerationEf',
        acceleration,
    )

  @overload(float)
  def setDeceleration(self, deceleration: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::setDeceleration(float
    deceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#setDeceleration

    Parameters
    ----------

    deceleration : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::setDeceleration(float deceleration)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput15setDecelerationEf',
        deceleration,
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
    'Qt3DInput::QButtonAxisInput::QButtonAxisInput(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#QButtonAxisInput

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QButtonAxisInput::QButtonAxisInput(Qt3DCore::QNode *parent)
    self._noteCreation(QButtonAxisInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInputC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def scaleChanged(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::scaleChanged(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#scaleChanged

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::scaleChanged(float scale)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput12scaleChangedEf', scale,
    )

  @overload(float)
  def accelerationChanged(self, acceleration: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::accelerationChanged(float
    acceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html

    Parameters
    ----------

    acceleration : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::accelerationChanged(float
    #      acceleration)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput19accelerationChangedEf',
        acceleration,
    )

  @overload(float)
  def decelerationChanged(self, deceleration: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QButtonAxisInput::decelerationChanged(float
    deceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html

    Parameters
    ----------

    deceleration : float
      Passed on as it is.
    """
    #  void Qt3DInput::QButtonAxisInput::decelerationChanged(float
    #      deceleration)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput19decelerationChangedEf',
        deceleration,
    )

  def d_func(self) -> Optional[Qt3DInput.QButtonAxisInputPrivate]:
    """
    Calls Qt's 'QButtonAxisInputPrivate
    *Qt3DInput::QButtonAxisInput::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qbuttonaxisinput.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QButtonAxisInputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QButtonAxisInputPrivate *Qt3DInput::QButtonAxisInput::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput16QButtonAxisInput6d_funcEv',
    )
    return Qt3DInput.QButtonAxisInputPrivate._cuteAt(address)

  @staticmethod
  def buttons(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DInput::QButtonAxisInput::buttons() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QButtonAxisInput.buttons' has no cute function yet. "
        "Qt's 'QList<int> Qt3DInput::QButtonAxisInput::buttons() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def buttonsChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QButtonAxisInput::buttonsChanged(const QList<int>
    &buttons)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QButtonAxisInput.buttonsChanged' has no cute function "
        "yet. Qt's 'void Qt3DInput::QButtonAxisInput::buttonsChanged(const "
        "QList<int> &buttons)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setButtons(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QButtonAxisInput::setButtons(const QList<int>
    &buttons)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QButtonAxisInput.setButtons' has no cute function yet. "
        "Qt's 'void Qt3DInput::QButtonAxisInput::setButtons(const "
        "QList<int> &buttons)': takes a type Python has no way to hand over "
        "yet.")
