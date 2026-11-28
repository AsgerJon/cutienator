"""
QPlaceResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPlaceSearchResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlace, QPlaceResultPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlace = WAIT['QPlace']


class QPlaceResult(QPlaceSearchResult):
  """
  The cute side of Qt's QPlaceResult: a plain Python object standing in front
  of one C++ QPlaceResult.

  It is built on the cute 'QPlaceSearchResult', as Qt's QPlaceResult is built
  on Qt's QPlaceSearchResult, and has everything that class has.

  C++ hands a QPlaceResult around as a copy, so every C++ QPlaceResult behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceResult that has a ritual and that Python can
  call so far, 7 names in all: 'distance', 'setDistance', 'place',
  'setPlace', 'isSponsored', 'setSponsored', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceResult::~QPlaceResult()': the destructor: Python removes its
    C++ QPlaceResult by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 leans on
  'QSharedDataPointer<QPlaceSearchResultPrivate>.

  What to expect
  --------------

  - The C++ QPlaceResult is created at the first use, not by
    'QPlaceResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceResult back gives a copy the ritual made for
    Python, in a new cute QPlaceResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceResult'

  #  Qt's '~QPlaceResult()'. Naming it makes this a value class: Python owns
  #  every C++ QPlaceResult behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QPlaceResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QPlaceResult::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#distance
    """
    #  qreal QPlaceResult::distance() const
    return self.uglySide.call('ritual_ZNK12QPlaceResult8distanceEv')

  def place(self) -> QPlace:
    """
    Calls Qt's 'QPlace QPlaceResult::place() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#place

    Returns
    -------

    QPlace
      A new cute QPlace around the copy Qt gave back. Python owns it.
    """
    #  QPlace QPlaceResult::place() const
    address = self.uglySide.call('ritual_ZNK12QPlaceResult5placeEv')
    from . import QPlace
    return QPlace._cuteOwning(address)

  def isSponsored(self) -> bool:
    """
    Calls Qt's 'bool QPlaceResult::isSponsored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#isSponsored
    """
    #  bool QPlaceResult::isSponsored() const
    return self.uglySide.call('ritual_ZNK12QPlaceResult11isSponsoredEv')

  def d_func(self) -> Optional[QPlaceResultPrivate]:
    """
    Calls Qt's 'const QPlaceResultPrivate *QPlaceResult::d_func() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#d_func

    Returns
    -------

    Optional[QPlaceResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlaceResultPrivate *QPlaceResult::d_func() const
    address = self.uglySide.call('ritual_ZNK12QPlaceResult6d_funcEv')
    from . import QPlaceResultPrivate
    return QPlaceResultPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QPlaceResult::setDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QPlaceResult::setDistance(qreal distance)
    self.uglySide.call('ritual_ZN12QPlaceResult11setDistanceEd', distance)

  @overload(QPlace)
  def setPlace(self, place: QPlace) -> None:
    """
    Calls Qt's 'void QPlaceResult::setPlace(const QPlace &place)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#setPlace

    Parameters
    ----------

    place : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  void QPlaceResult::setPlace(const QPlace &place)
    self.uglySide.call(
        'ritual_ZN12QPlaceResult8setPlaceERK6QPlace', self._valueOf(place),
    )

  @overload(bool)
  def setSponsored(self, sponsored: bool) -> None:
    """
    Calls Qt's 'void QPlaceResult::setSponsored(bool sponsored)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#setSponsored

    Parameters
    ----------

    sponsored : bool
      Passed on as it is.
    """
    #  void QPlaceResult::setSponsored(bool sponsored)
    self.uglySide.call('ritual_ZN12QPlaceResult12setSponsoredEb', sponsored)

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
    Notes what was given, for Qt's 'QPlaceResult::QPlaceResult()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#QPlaceResult
    """
    #  QPlaceResult::QPlaceResult()
    self._noteCreation(QPlaceResult, lambda: Rituals.call(
        'ritual_ZN12QPlaceResultC1Ev',
    ))

  @overload(QPlaceSearchResult)
  def __init__(self, other: QPlaceSearchResult) -> None:
    """
    Notes what was given, for Qt's 'QPlaceResult::QPlaceResult(const
    QPlaceSearchResult &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresult.html#QPlaceResult

    Parameters
    ----------

    other : QPlaceSearchResult
      Passed on as a value: Qt reads the C++ QPlaceSearchResult, which stays
      Python's own.
    """
    #  QPlaceResult::QPlaceResult(const QPlaceSearchResult &other)
    self._noteCreation(QPlaceResult, lambda: Rituals.call(
        'ritual_ZN12QPlaceResultC1ERK18QPlaceSearchResult',
        self._valueOf(other),
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
