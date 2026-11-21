"""
QLocationPermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QLocationPermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocationPermission: a plain Python object standing
  in front of one C++ QLocationPermission.

  C++ hands a QLocationPermission around as a copy, so every C++
  QLocationPermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLocationPermission that has a ritual and that
  Python can call so far, 4 names in all: 'setAccuracy', 'accuracy',
  'setAvailability', 'availability'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLocationPermission::~QLocationPermission()': the destructor:
    Python removes its C++ QLocationPermission by it, and has no other use
    for it.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QLocationPermission is created at the first use, not by
    'QLocationPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocationPermission back gives a copy the ritual made
    for Python, in a new cute QLocationPermission.
  """

  #  The enums Qt writes inside QLocationPermission, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Accuracy(CuteNum):
    """
    The enum 'QLocationPermission::Accuracy' of Qt, with the 2 names Qt gives
    in it.
    """

    Approximate = Kee[int](0)
    Precise = Kee[int](1)

  class Availability(CuteNum):
    """
    The enum 'QLocationPermission::Availability' of Qt, with the 2 names Qt
    gives in it.
    """

    WhenInUse = Kee[int](0)
    Always = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocationPermission'

  #  Qt's '~QLocationPermission()'. Naming it makes this a value class:
  #  Python owns every C++ QLocationPermission behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QLocationPermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def accuracy(self) -> Accuracy:
    """
    Calls Qt's 'Accuracy QLocationPermission::accuracy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationpermission.html#accuracy

    Returns
    -------

    Accuracy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Accuracy(number)' gives.
    """
    #  Accuracy QLocationPermission::accuracy() const
    return QLocationPermission.Accuracy(self.uglySide.call(
        'ritual_ZNK19QLocationPermission8accuracyEv',
    ))

  def availability(self) -> Availability:
    """
    Calls Qt's 'Availability QLocationPermission::availability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationpermission.html#availability

    Returns
    -------

    Availability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Availability(number)'
      gives.
    """
    #  Availability QLocationPermission::availability() const
    return QLocationPermission.Availability(self.uglySide.call(
        'ritual_ZNK19QLocationPermission12availabilityEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Accuracy)
  def setAccuracy(self, accuracy: Accuracy) -> None:
    """
    Calls Qt's 'void QLocationPermission::setAccuracy(Accuracy accuracy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationpermission.html#setAccuracy

    Parameters
    ----------

    accuracy : Accuracy
      Passed on as its number.
    """
    #  void QLocationPermission::setAccuracy(Accuracy accuracy)
    self.uglySide.call(
        'ritual_ZN19QLocationPermission11setAccuracyENS_8AccuracyE',
        accuracy.value,
    )

  @overload(Availability)
  def setAvailability(self, availability: Availability) -> None:
    """
    Calls Qt's 'void QLocationPermission::setAvailability(Availability
    availability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationpermission.html#setAvailability

    Parameters
    ----------

    availability : Availability
      Passed on as its number.
    """
    #  void QLocationPermission::setAvailability(Availability availability)
    self.uglySide.call(
        'ritual_ZN19QLocationPermission15setAvailabilityENS_12AvailabilityE',
        availability.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QLocationPermission::QLocationPermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationpermission.html#QLocationPermission
    """
    #  QLocationPermission::QLocationPermission()
    self._noteCreation(QLocationPermission, lambda: Rituals.call(
        'ritual_ZN19QLocationPermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLocationPermission) -> None:
    """
    Notes what was given, for Qt's
    'QLocationPermission::QLocationPermission(const QLocationPermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationpermission.html#QLocationPermission

    Parameters
    ----------

    other : QLocationPermission
      Passed on as a value: Qt reads the C++ QLocationPermission, which stays
      Python's own.
    """
    #  QLocationPermission::QLocationPermission(const QLocationPermission
    #      &other)
    self._noteCreation(QLocationPermission, lambda: Rituals.call(
        'ritual_ZN19QLocationPermissionC1ERKS_', self._valueOf(other),
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
