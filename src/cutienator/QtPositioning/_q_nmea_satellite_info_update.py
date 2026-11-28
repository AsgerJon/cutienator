"""
QNmeaSatelliteInfoUpdate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QNmeaSatelliteInfoUpdate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList
from . import QGeoSatelliteInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNmeaSatelliteInfoUpdate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNmeaSatelliteInfoUpdate: a plain Python object
  standing in front of one C++ QNmeaSatelliteInfoUpdate.

  C++ hands a QNmeaSatelliteInfoUpdate around as a copy, so every C++
  QNmeaSatelliteInfoUpdate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNmeaSatelliteInfoUpdate that has a ritual and that
  Python can call so far, 9 names in all: 'allSatellitesInUse',
  'allSatellitesInView', 'setSatellitesInView', 'consume', 'isFresh',
  'clear', 'isValid', 'calculateValidInUse', 'calculateValidInView'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QNmeaSatelliteInfoUpdate::setSatellitesInUse(QGeoSatelliteInfo::
    SatelliteSystem system, const QList<int> &inUse)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QNmeaSatelliteInfoUpdate::~QNmeaSatelliteInfoUpdate()': the
    destructor: Python removes its C++ QNmeaSatelliteInfoUpdate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QNmeaSatelliteInfoUpdate is created at the first use, not by
    'QNmeaSatelliteInfoUpdate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNmeaSatelliteInfoUpdate back gives a copy the ritual
    made for Python, in a new cute QNmeaSatelliteInfoUpdate.
  - Each name of Qt's QNmeaSatelliteInfoUpdate that has no cute function yet,
    'setSatellitesInUse', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSatelliteInfoUpdate'

  #  Qt's '~QNmeaSatelliteInfoUpdate()'. Naming it makes this a value class:
  #  Python owns every C++ QNmeaSatelliteInfoUpdate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QNmeaSatelliteInfoUpdateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def allSatellitesInUse(self) -> QList[QGeoSatelliteInfo]:
    """
    Calls Qt's 'QList<QGeoSatelliteInfo>
    QNmeaSatelliteInfoUpdate::allSatellitesInUse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#allSatellitesInUse

    Returns
    -------

    QList[QGeoSatelliteInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoSatelliteInfo>
    #      QNmeaSatelliteInfoUpdate::allSatellitesInUse() const
    address = self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate18allSatellitesInUseEv',
    )
    return QList[QGeoSatelliteInfo]._cuteOwning(address)

  def allSatellitesInView(self) -> QList[QGeoSatelliteInfo]:
    """
    Calls Qt's 'QList<QGeoSatelliteInfo>
    QNmeaSatelliteInfoUpdate::allSatellitesInView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#allSatellitesInView

    Returns
    -------

    QList[QGeoSatelliteInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoSatelliteInfo>
    #      QNmeaSatelliteInfoUpdate::allSatellitesInView() const
    address = self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate19allSatellitesInViewEv',
    )
    return QList[QGeoSatelliteInfo]._cuteOwning(address)

  def isFresh(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoUpdate::isFresh() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#isFresh
    """
    #  bool QNmeaSatelliteInfoUpdate::isFresh() const
    return self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate7isFreshEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoUpdate::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#isValid
    """
    #  bool QNmeaSatelliteInfoUpdate::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate7isValidEv',
    )

  def calculateValidInUse(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoUpdate::calculateValidInUse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#calculateValidInUse
    """
    #  bool QNmeaSatelliteInfoUpdate::calculateValidInUse() const
    return self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate19calculateValidInUseEv',
    )

  def calculateValidInView(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoUpdate::calculateValidInView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#calculateValidInView
    """
    #  bool QNmeaSatelliteInfoUpdate::calculateValidInView() const
    return self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoUpdate20calculateValidInViewEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoSatelliteInfo.SatelliteSystem, QList[QGeoSatelliteInfo])
  def setSatellitesInView(
      self,
      system: QGeoSatelliteInfo.SatelliteSystem,
      inView: QList[QGeoSatelliteInfo],
  ) -> None:
    """
    Calls Qt's 'void
    QNmeaSatelliteInfoUpdate::setSatellitesInView(QGeoSatelliteInfo::
    SatelliteSystem system, const QList<QGeoSatelliteInfo> &inView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#setSatellitesInView

    Parameters
    ----------

    system : QGeoSatelliteInfo.SatelliteSystem
      Passed on as its number.

    inView : QList[QGeoSatelliteInfo]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNmeaSatelliteInfoUpdate::setSatellitesInView(QGeoSatelliteInfo::
    #      SatelliteSystem system, const QList<QGeoSatelliteInfo> &inView)
    self.uglySide.call(
        'ritual_ZN24QNmeaSatelliteInfoUpdate19setSatellitesInViewEN17QGeoSa'
        'telliteInfo15SatelliteSystemERK5QListIS0_E',
        system.value, self._valueOf(inView),
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

  def consume(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoUpdate::consume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#consume
    """
    #  void QNmeaSatelliteInfoUpdate::consume()
    self.uglySide.call('ritual_ZN24QNmeaSatelliteInfoUpdate7consumeEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoUpdate::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfoupdate.html#clear
    """
    #  void QNmeaSatelliteInfoUpdate::clear()
    self.uglySide.call('ritual_ZN24QNmeaSatelliteInfoUpdate5clearEv')

  @staticmethod
  def setSatellitesInUse(*__, **_) -> Never:
    """
    Qt's 'bool
    QNmeaSatelliteInfoUpdate::setSatellitesInUse(QGeoSatelliteInfo::
    SatelliteSystem system, const QList<int> &inUse)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoUpdate.setSatellitesInUse' has no cute function "
        "yet. Qt's 'bool "
        "QNmeaSatelliteInfoUpdate::setSatellitesInUse(QGeoSatelliteInfo::Sat"
        "elliteSystem system, const QList<int> &inUse)': takes a type "
        "Python has no way to hand over yet.")
