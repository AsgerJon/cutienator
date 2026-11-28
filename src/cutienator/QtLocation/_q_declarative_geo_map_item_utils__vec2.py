"""
QDeclarativeGeoMapItemUtils::vec2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapItemUtils::vec2 to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtPositioning import QDoubleVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector2D = WAIT['QDoubleVector2D']


class vec2(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDeclarativeGeoMapItemUtils::vec2: a plain Python
  object standing in front of one C++ QDeclarativeGeoMapItemUtils::vec2.

  C++ hands a QDeclarativeGeoMapItemUtils::vec2 around as a copy, so every
  C++ QDeclarativeGeoMapItemUtils::vec2 behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapItemUtils::vec2 that has a ritual
  and that Python can call so far, 1 name in all: 'toDoubleVector2D'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'vec2 &QDeclarativeGeoMapItemUtils::vec2::operator=(const QPointF
    &p)': assignment: Python binds a name and has no operator for it.
  - Qt's 'vec2 &QDeclarativeGeoMapItemUtils::vec2::operator=(const
    QDoubleVector2D &p)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'QDeclarativeGeoMapItemUtils::vec2::~vec2()': the destructor: Python
    removes its C++ QDeclarativeGeoMapItemUtils::vec2 by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapItemUtils::vec2 is created at the first use,
    not by 'QDeclarativeGeoMapItemUtils::vec2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDeclarativeGeoMapItemUtils::vec2 back gives a copy
    the ritual made for Python, in a new cute
    QDeclarativeGeoMapItemUtils::vec2.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapItemUtils::vec2'

  #  Qt's '~QDeclarativeGeoMapItemUtils::vec2()'. Naming it makes this a
  #  value class: Python owns every C++ QDeclarativeGeoMapItemUtils::vec2
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QDeclarativeGeoMapItemUtils4vec2D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toDoubleVector2D(self) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QDeclarativeGeoMapItemUtils::vec2::toDoubleVector2D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemutils-vec2.html

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QDeclarativeGeoMapItemUtils::vec2::toDoubleVector2D()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapItemUtils4vec216toDoubleVector2DEv',
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDoubleVector2D)
  def __init__(self, p: QDoubleVector2D) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoMapItemUtils::vec2::vec2(const QDoubleVector2D &p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemutils-vec2.html#vec2

    Parameters
    ----------

    p : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDeclarativeGeoMapItemUtils::vec2::vec2(const QDoubleVector2D &p)
    self._noteCreation(vec2, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapItemUtils4vec2C1ERK15QDoubleVector2D',
        self._valueOf(p),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoMapItemUtils::vec2::vec2()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemutils-vec2.html#vec2
    """
    #  QDeclarativeGeoMapItemUtils::vec2::vec2()
    self._noteCreation(vec2, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapItemUtils4vec2C1Ev',
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
