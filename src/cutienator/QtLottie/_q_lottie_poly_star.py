"""
QLottiePolyStar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiepolystar_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottiePolyStar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieSpatialProperty
  from ..QtCore import QJsonObject, QPointF
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottiePolyStar(QLottieShape):
  """
  The cute side of Qt's QLottiePolyStar: a plain Python object standing in
  front of one C++ QLottiePolyStar.

  It is built on the cute 'QLottieShape', as Qt's QLottiePolyStar is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottiePolyStar around as a copy, so every C++ QLottiePolyStar
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottiePolyStar that has a ritual and that Python
  can call so far, 14 names in all: 'clone', 'parse', 'updateProperties',
  'acceptsTrim', 'position', 'outerRadius', 'innerRadius', 'startAngle',
  'pointCount', 'isPolygonModeEnabled', 'isAnimated', 'positionProperty',
  'fallbackPath', 'buildPath'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottiePolyStar::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QLottieProperty<qreal>
    &QLottiePolyStar::outerRadiusProperty() const': gives a type Python has
    no way to take yet.
  - Qt's 'const QLottieProperty<qreal>
    &QLottiePolyStar::innerRadiusProperty() const': gives a type Python has
    no way to take yet.
  - Qt's 'QLottiePolyStar::~QLottiePolyStar()': the destructor: Python
    removes its C++ QLottiePolyStar by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottiePolyStar is created at the first use, not by
    'QLottiePolyStar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottiePolyStar back gives a copy the ritual made for
    Python, in a new cute QLottiePolyStar.
  - Each name of Qt's QLottiePolyStar that has no cute function yet,
    'innerRadiusProperty', 'outerRadiusProperty', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottiePolyStar'

  #  A C++ QLottiePolyStar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottiePolyStar'

  #  Qt's '~QLottiePolyStar()'. Naming it makes this a value class: Python
  #  owns every C++ QLottiePolyStar behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QLottiePolyStarD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottiePolyStar::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottiePolyStar::clone() const
    ritual = 'ritual_ZNK15QLottiePolyStar5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottiePolyStar5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottiePolyStar::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#acceptsTrim
    """
    #  bool QLottiePolyStar::acceptsTrim() const
    ritual = 'ritual_ZNK15QLottiePolyStar11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottiePolyStar11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottiePolyStar::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottiePolyStar::position() const
    address = self.uglySide.call('ritual_ZNK15QLottiePolyStar8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def outerRadius(self) -> float:
    """
    Calls Qt's 'qreal QLottiePolyStar::outerRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#outerRadius
    """
    #  qreal QLottiePolyStar::outerRadius() const
    return self.uglySide.call('ritual_ZNK15QLottiePolyStar11outerRadiusEv')

  def innerRadius(self) -> float:
    """
    Calls Qt's 'qreal QLottiePolyStar::innerRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#innerRadius
    """
    #  qreal QLottiePolyStar::innerRadius() const
    return self.uglySide.call('ritual_ZNK15QLottiePolyStar11innerRadiusEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QLottiePolyStar::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#startAngle
    """
    #  qreal QLottiePolyStar::startAngle() const
    return self.uglySide.call('ritual_ZNK15QLottiePolyStar10startAngleEv')

  def pointCount(self) -> int:
    """
    Calls Qt's 'int QLottiePolyStar::pointCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#pointCount
    """
    #  int QLottiePolyStar::pointCount() const
    return self.uglySide.call('ritual_ZNK15QLottiePolyStar10pointCountEv')

  def isPolygonModeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLottiePolyStar::isPolygonModeEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiepolystar.html#isPolygonModeEnabled
    """
    #  bool QLottiePolyStar::isPolygonModeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QLottiePolyStar20isPolygonModeEnabledEv',
    )

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QLottiePolyStar::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#isAnimated
    """
    #  bool QLottiePolyStar::isAnimated() const
    ritual = 'ritual_ZNK15QLottiePolyStar10isAnimatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottiePolyStar10isAnimatedEv'
    return self.uglySide.call(ritual)

  def positionProperty(self) -> QLottieSpatialProperty:
    """
    Calls Qt's 'const QLottieSpatialProperty
    &QLottiePolyStar::positionProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiepolystar.html#positionProperty

    Returns
    -------

    QLottieSpatialProperty
      A new cute QLottieSpatialProperty around the copy Qt gave back. Python
      owns it.
    """
    #  const QLottieSpatialProperty &QLottiePolyStar::positionProperty()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QLottiePolyStar16positionPropertyEv',
    )
    from . import QLottieSpatialProperty
    return QLottieSpatialProperty._cuteOwning(address)

  def fallbackPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QLottiePolyStar::fallbackPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#fallbackPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QLottiePolyStar::fallbackPath() const
    ritual = 'ritual_ZNK15QLottiePolyStar12fallbackPathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottiePolyStar12fallbackPathEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QLottiePolyStar) -> None:
    """
    Notes what was given, for Qt's 'QLottiePolyStar::QLottiePolyStar(const
    QLottiePolyStar &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiepolystar.html#QLottiePolyStar

    Parameters
    ----------

    other : QLottiePolyStar
      Passed on as a value: Qt reads the C++ QLottiePolyStar, which stays
      Python's own.
    """
    #  QLottiePolyStar::QLottiePolyStar(const QLottiePolyStar &other)
    self._noteCreation(QLottiePolyStar, lambda: Rituals.call(
        'ritual_ZN15QLottiePolyStarC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottiePolyStar::QLottiePolyStar(QLottieBase *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiepolystar.html#QLottiePolyStar

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottiePolyStar::QLottiePolyStar(QLottieBase *parent)
    self._noteCreation(QLottiePolyStar, lambda: Rituals.call(
        'ritual_ZN15QLottiePolyStarC1EP11QLottieBase',
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottiePolyStar::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottiePolyStar::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN15QLottiePolyStar5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottiePolyStar5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottiePolyStar::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiepolystar.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottiePolyStar::updateProperties(int frame)
    ritual = 'ritual_ZN15QLottiePolyStar16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottiePolyStar16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  def buildPath(self) -> None:
    """
    Calls Qt's 'void QLottiePolyStar::buildPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiepolystar.html#buildPath
    """
    #  void QLottiePolyStar::buildPath()
    self.uglySide.call('ritual_ZN15QLottiePolyStar9buildPathEv')

  @staticmethod
  def innerRadiusProperty(*__, **_) -> Never:
    """
    Qt's 'const QLottieProperty<qreal>
    &QLottiePolyStar::innerRadiusProperty() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QLottiePolyStar.innerRadiusProperty' has no cute function yet. "
        "Qt's 'const QLottieProperty<qreal> "
        "&QLottiePolyStar::innerRadiusProperty() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def outerRadiusProperty(*__, **_) -> Never:
    """
    Qt's 'const QLottieProperty<qreal>
    &QLottiePolyStar::outerRadiusProperty() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QLottiePolyStar.outerRadiusProperty' has no cute function yet. "
        "Qt's 'const QLottieProperty<qreal> "
        "&QLottiePolyStar::outerRadiusProperty() const': gives a type "
        "Python has no way to take yet.")
