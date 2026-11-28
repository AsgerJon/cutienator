"""
QLottieEllipse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieellipse_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieEllipse to be private: it declares the class in a header
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
  from ..QtCore import QJsonObject, QPointF, QSizeF
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieEllipse(QLottieShape):
  """
  The cute side of Qt's QLottieEllipse: a plain Python object standing in
  front of one C++ QLottieEllipse.

  It is built on the cute 'QLottieShape', as Qt's QLottieEllipse is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieEllipse around as a copy, so every C++ QLottieEllipse
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieEllipse that has a ritual and that Python can
  call so far, 9 names in all: 'clone', 'updateProperties', 'parse',
  'acceptsTrim', 'position', 'size', 'isAnimated', 'fallbackPath',
  'positionProperty'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieEllipse::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QLottieProperty2D<QSizeF> &QLottieEllipse::sizeProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieEllipse::~QLottieEllipse()': the destructor: Python removes
    its C++ QLottieEllipse by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieEllipse is created at the first use, not by
    'QLottieEllipse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieEllipse back gives a copy the ritual made for
    Python, in a new cute QLottieEllipse.
  - Each name of Qt's QLottieEllipse that has no cute function yet,
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
  __qt_class__ = 'QLottieEllipse'

  #  A C++ QLottieEllipse Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieEllipse'

  #  Qt's '~QLottieEllipse()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieEllipse behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QLottieEllipseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieEllipse::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieEllipse::clone() const
    ritual = 'ritual_ZNK14QLottieEllipse5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieEllipse5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieEllipse::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#acceptsTrim
    """
    #  bool QLottieEllipse::acceptsTrim() const
    ritual = 'ritual_ZNK14QLottieEllipse11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieEllipse11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieEllipse::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieEllipse::position() const
    address = self.uglySide.call('ritual_ZNK14QLottieEllipse8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QLottieEllipse::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QLottieEllipse::size() const
    address = self.uglySide.call('ritual_ZNK14QLottieEllipse4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QLottieEllipse::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#isAnimated
    """
    #  bool QLottieEllipse::isAnimated() const
    ritual = 'ritual_ZNK14QLottieEllipse10isAnimatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieEllipse10isAnimatedEv'
    return self.uglySide.call(ritual)

  def fallbackPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QLottieEllipse::fallbackPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#fallbackPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QLottieEllipse::fallbackPath() const
    ritual = 'ritual_ZNK14QLottieEllipse12fallbackPathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieEllipse12fallbackPathEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def positionProperty(self) -> QLottieSpatialProperty:
    """
    Calls Qt's 'const QLottieSpatialProperty
    &QLottieEllipse::positionProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieellipse.html#positionProperty

    Returns
    -------

    QLottieSpatialProperty
      A new cute QLottieSpatialProperty around the copy Qt gave back. Python
      owns it.
    """
    #  const QLottieSpatialProperty &QLottieEllipse::positionProperty() const
    address = self.uglySide.call(
        'ritual_ZNK14QLottieEllipse16positionPropertyEv',
    )
    from . import QLottieSpatialProperty
    return QLottieSpatialProperty._cuteOwning(address)

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
  def __init__(self, other: QLottieEllipse) -> None:
    """
    Notes what was given, for Qt's 'QLottieEllipse::QLottieEllipse(const
    QLottieEllipse &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#QLottieEllipse

    Parameters
    ----------

    other : QLottieEllipse
      Passed on as a value: Qt reads the C++ QLottieEllipse, which stays
      Python's own.
    """
    #  QLottieEllipse::QLottieEllipse(const QLottieEllipse &other)
    self._noteCreation(QLottieEllipse, lambda: Rituals.call(
        'ritual_ZN14QLottieEllipseC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieEllipse::QLottieEllipse(QLottieBase *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#QLottieEllipse

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieEllipse::QLottieEllipse(QLottieBase *parent)
    self._noteCreation(QLottieEllipse, lambda: Rituals.call(
        'ritual_ZN14QLottieEllipseC1EP11QLottieBase',
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

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieEllipse::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieellipse.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieEllipse::updateProperties(int frame)
    ritual = 'ritual_ZN14QLottieEllipse16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QLottieEllipse16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieEllipse::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieellipse.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieEllipse::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN14QLottieEllipse5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QLottieEllipse5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def sizeProperty(*__, **_) -> Never:
    """
    Qt's 'const QLottieProperty2D<QSizeF> &QLottieEllipse::sizeProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieEllipse.sizeProperty' has no cute function yet. Qt's "
        "'const QLottieProperty2D<QSizeF> &QLottieEllipse::sizeProperty() "
        "const': gives a type Python has no way to take yet.")
