"""
QAmbientLightReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qambientlightsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAmbientLightReading(QSensorReading):
  """
  The cute side of Qt's QAmbientLightReading: a plain Python object standing
  in front of one C++ QAmbientLightReading.

  It is built on the cute 'QSensorReading', as Qt's QAmbientLightReading is
  built on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAmbientLightReading that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'copyValuesFrom', 'lightLevel', 'setLightLevel'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAmbientLightReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAmbientLightReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAmbientLightReading::~QAmbientLightReading()': the destructor:
    Python never removes a C++ QAmbientLightReading.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAmbientLightReading is created at the first use, not by
    'QAmbientLightReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAmbientLightReading.
  - Qt tells when it has removed the C++ QAmbientLightReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAmbientLightReading, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LightLevel(CuteNum):
    """
    The enum 'QAmbientLightReading::LightLevel' of Qt, with the 6 names Qt
    gives in it.
    """

    Undefined = Kee[int](0)
    Dark = Kee[int](1)
    Twilight = Kee[int](2)
    Light = Kee[int](3)
    Bright = Kee[int](4)
    Sunny = Kee[int](5)

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
    Calls Qt's 'QString QAmbientLightReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientlightreading.html#tr

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
    #  QString QAmbientLightReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QAmbientLightReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAmbientLightReading'

  #  A C++ QAmbientLightReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAmbientLightReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAmbientLightReading::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambientlightreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAmbientLightReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QAmbientLightReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lightLevel(self) -> LightLevel:
    """
    Calls Qt's 'LightLevel QAmbientLightReading::lightLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambientlightreading.html#lightLevel

    Returns
    -------

    LightLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LightLevel(number)'
      gives.
    """
    #  LightLevel QAmbientLightReading::lightLevel() const
    return QAmbientLightReading.LightLevel(self.uglySide.call(
        'ritual_ZNK20QAmbientLightReading10lightLevelEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(LightLevel)
  def setLightLevel(self, lightLevel: LightLevel) -> None:
    """
    Calls Qt's 'void QAmbientLightReading::setLightLevel(LightLevel
    lightLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambientlightreading.html#setLightLevel

    Parameters
    ----------

    lightLevel : LightLevel
      Passed on as its number.
    """
    #  void QAmbientLightReading::setLightLevel(LightLevel lightLevel)
    self.uglySide.call(
        'ritual_ZN20QAmbientLightReading13setLightLevelENS_10LightLevelE',
        lightLevel.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAmbientLightReading::QAmbientLightReading(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qambientlightreading.html#QAmbientLightReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAmbientLightReading::QAmbientLightReading(QObject *parent)
    self._noteCreation(QAmbientLightReading, lambda: Rituals.call(
        'ritual_ZN20QAmbientLightReadingC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QSensorReading)
  @overload(NoneType)
  def copyValuesFrom(self, other: Optional[QSensorReading]) -> None:
    """
    Calls Qt's 'void QAmbientLightReading::copyValuesFrom(QSensorReading
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambientlightreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAmbientLightReading::copyValuesFrom(QSensorReading *other)
    ritual = (
        'ritual_ZN20QAmbientLightReading14copyValuesFromEP14QSensorReading')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAmbientLightReading14copyValuesFromEP14QSensorRe'
          'ading')
    self.uglySide.call(ritual, self._addressOf(other))
