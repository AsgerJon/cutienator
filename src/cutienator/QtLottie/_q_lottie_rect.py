"""
QLottieRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottierect_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieRect to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieLiteral, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieSpatialProperty
  from ..QtCore import QJsonObject, QPointF, QSizeF, QVariant
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieRect(QLottieShape):
  """
  The cute side of Qt's QLottieRect: a plain Python object standing in front
  of one C++ QLottieRect.

  It is built on the cute 'QLottieShape', as Qt's QLottieRect is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieRect around as a copy, so every C++ QLottieRect behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRect that has a ritual and that Python can
  call so far, 11 names in all: 'clone', 'setProperty', 'updateProperties',
  'acceptsTrim', 'parse', 'position', 'size', 'roundness', 'isAnimated',
  'fallbackPath', 'positionProperty'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieRect::render(QLottieRenderer &renderer) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QLottieProperty2D<QSizeF> &QLottieRect::sizeProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieRect::~QLottieRect()': the destructor: Python removes its
    C++ QLottieRect by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QLottieRect is created at the first use, not by
    'QLottieRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRect back gives a copy the ritual made for
    Python, in a new cute QLottieRect.
  - Each name of Qt's QLottieRect that has no cute function yet,
    'sizeProperty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieRect'

  #  A C++ QLottieRect Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRect'

  #  Qt's '~QLottieRect()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieRect behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLottieRectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieRect::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieRect::clone() const
    ritual = 'ritual_ZNK11QLottieRect5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRect5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieRect::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#acceptsTrim
    """
    #  bool QLottieRect::acceptsTrim() const
    ritual = 'ritual_ZNK11QLottieRect11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRect11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieRect::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieRect::position() const
    address = self.uglySide.call('ritual_ZNK11QLottieRect8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QLottieRect::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QLottieRect::size() const
    address = self.uglySide.call('ritual_ZNK11QLottieRect4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def roundness(self) -> float:
    """
    Calls Qt's 'qreal QLottieRect::roundness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#roundness
    """
    #  qreal QLottieRect::roundness() const
    return self.uglySide.call('ritual_ZNK11QLottieRect9roundnessEv')

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QLottieRect::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#isAnimated
    """
    #  bool QLottieRect::isAnimated() const
    ritual = 'ritual_ZNK11QLottieRect10isAnimatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRect10isAnimatedEv'
    return self.uglySide.call(ritual)

  def fallbackPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QLottieRect::fallbackPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#fallbackPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QLottieRect::fallbackPath() const
    ritual = 'ritual_ZNK11QLottieRect12fallbackPathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRect12fallbackPathEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def positionProperty(self) -> QLottieSpatialProperty:
    """
    Calls Qt's 'const QLottieSpatialProperty &QLottieRect::positionProperty()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#positionProperty

    Returns
    -------

    QLottieSpatialProperty
      A new cute QLottieSpatialProperty around the copy Qt gave back. Python
      owns it.
    """
    #  const QLottieSpatialProperty &QLottieRect::positionProperty() const
    address = self.uglySide.call(
        'ritual_ZNK11QLottieRect16positionPropertyEv',
    )
    from . import QLottieSpatialProperty
    return QLottieSpatialProperty._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLottieLiteral.PropertyType, QVariant)
  def setProperty(
      self,
      propertyType: QLottieLiteral.PropertyType,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QLottieRect::setProperty(QLottieLiteral::PropertyType
    propertyType, QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#setProperty

    Parameters
    ----------

    propertyType : QLottieLiteral.PropertyType
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QLottieRect::setProperty(QLottieLiteral::PropertyType
    #      propertyType, QVariant value)
    ritual = (
        'ritual_ZN11QLottieRect11setPropertyEN14QLottieLiteral12PropertyTyp'
        'eE8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QLottieRect11setPropertyEN14QLottieLiteral12Prope'
          'rtyTypeE8QVariant')
    return self.uglySide.call(
        ritual, propertyType.value, self._valueOf(value),
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

  @overload(THIS)
  def __init__(self, other: QLottieRect) -> None:
    """
    Notes what was given, for Qt's 'QLottieRect::QLottieRect(const
    QLottieRect &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#QLottieRect

    Parameters
    ----------

    other : QLottieRect
      Passed on as a value: Qt reads the C++ QLottieRect, which stays
      Python's own.
    """
    #  QLottieRect::QLottieRect(const QLottieRect &other)
    self._noteCreation(QLottieRect, lambda: Rituals.call(
        'ritual_ZN11QLottieRectC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieRect::QLottieRect(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#QLottieRect

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieRect::QLottieRect(QLottieBase *parent)
    self._noteCreation(QLottieRect, lambda: Rituals.call(
        'ritual_ZN11QLottieRectC1EP11QLottieBase', self._addressOf(parent),
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

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieRect::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieRect::updateProperties(int frame)
    ritual = 'ritual_ZN11QLottieRect16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieRect16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieRect::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierect.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieRect::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN11QLottieRect5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieRect5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def sizeProperty(*__, **_) -> Never:
    """
    Qt's 'const QLottieProperty2D<QSizeF> &QLottieRect::sizeProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieRect.sizeProperty' has no cute function yet. Qt's 'const "
        "QLottieProperty2D<QSizeF> &QLottieRect::sizeProperty() const': "
        "gives a type Python has no way to take yet.")
