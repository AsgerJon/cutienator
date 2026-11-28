"""
QLottieStroke binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiestroke_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieStroke to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject
  from ..QtGui import QColor, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieStroke(QLottieShape):
  """
  The cute side of Qt's QLottieStroke: a plain Python object standing in
  front of one C++ QLottieStroke.

  It is built on the cute 'QLottieShape', as Qt's QLottieStroke is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieStroke around as a copy, so every C++ QLottieStroke
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieStroke that has a ritual and that Python can
  call so far, 7 names in all: 'clone', 'updateProperties', 'parse', 'pen',
  'opacity', 'getColor', 'updateDashPattern'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieStroke::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty4D<QVector4D> QLottieStroke::colorProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieStroke::opacityProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieStroke::widthProperty() const': gives
    a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieStroke::dashOffsetProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieStroke::~QLottieStroke()': the destructor: Python removes
    its C++ QLottieStroke by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieStroke is created at the first use, not by
    'QLottieStroke(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieStroke back gives a copy the ritual made for
    Python, in a new cute QLottieStroke.
  - Each name of Qt's QLottieStroke that has no cute function yet,
    'colorProperty', 'dashOffsetProperty', 'opacityProperty',
    'widthProperty', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QLottieStroke'

  #  A C++ QLottieStroke Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieStroke'

  #  The functions Qt calls itself that QLottieStroke is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'pen': (
          ('_ZNK13QLottieStroke3penEv',
           ('address', 'value', 'QtGui:QPen'),
           ()),
      ),
  }

  #  Qt's '~QLottieStroke()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieStroke behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QLottieStrokeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieStroke::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieStroke::clone() const
    ritual = 'ritual_ZNK13QLottieStroke5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QLottieStroke5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QLottieStroke::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QLottieStroke::pen() const
    ritual = 'ritual_ZNK13QLottieStroke3penEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QLottieStroke3penEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieStroke::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#opacity
    """
    #  qreal QLottieStroke::opacity() const
    return self.uglySide.call('ritual_ZNK13QLottieStroke7opacityEv')

  def getColor(self) -> QColor:
    """
    Calls Qt's 'QColor QLottieStroke::getColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#getColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLottieStroke::getColor() const
    address = self.uglySide.call('ritual_ZNK13QLottieStroke8getColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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
  def __init__(self, other: QLottieStroke) -> None:
    """
    Notes what was given, for Qt's 'QLottieStroke::QLottieStroke(const
    QLottieStroke &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#QLottieStroke

    Parameters
    ----------

    other : QLottieStroke
      Passed on as a value: Qt reads the C++ QLottieStroke, which stays
      Python's own.
    """
    #  QLottieStroke::QLottieStroke(const QLottieStroke &other)
    self._noteCreation(QLottieStroke, lambda: Rituals.call(
        'ritual_ZN13QLottieStrokeC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieStroke::QLottieStroke(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#QLottieStroke

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieStroke::QLottieStroke(QLottieBase *parent)
    self._noteCreation(QLottieStroke, lambda: Rituals.call(
        'ritual_ZN13QLottieStrokeC1EP11QLottieBase', self._addressOf(parent),
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
    Calls Qt's 'void QLottieStroke::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiestroke.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieStroke::updateProperties(int frame)
    ritual = 'ritual_ZN13QLottieStroke16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QLottieStroke16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieStroke::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiestroke.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieStroke::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN13QLottieStroke5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QLottieStroke5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  def updateDashPattern(self) -> None:
    """
    Calls Qt's 'void QLottieStroke::updateDashPattern()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiestroke.html#updateDashPattern
    """
    #  void QLottieStroke::updateDashPattern()
    self.uglySide.call('ritual_ZN13QLottieStroke17updateDashPatternEv')

  @staticmethod
  def colorProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty4D<QVector4D> QLottieStroke::colorProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieStroke.colorProperty' has no cute function yet. Qt's "
        "'QLottieProperty4D<QVector4D> QLottieStroke::colorProperty() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def dashOffsetProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieStroke::dashOffsetProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieStroke.dashOffsetProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieStroke::dashOffsetProperty() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def opacityProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieStroke::opacityProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieStroke.opacityProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieStroke::opacityProperty() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def widthProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieStroke::widthProperty() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieStroke.widthProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieStroke::widthProperty() const': "
        "gives a type Python has no way to take yet.")
