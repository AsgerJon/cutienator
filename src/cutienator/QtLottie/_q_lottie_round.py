"""
QLottieRound binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieround_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieRound to be private: it declares the class in a header it
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
  from typing import Optional

  from ..QtCore import QJsonObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieRound(QLottieShape):
  """
  The cute side of Qt's QLottieRound: a plain Python object standing in front
  of one C++ QLottieRound.

  It is built on the cute 'QLottieShape', as Qt's QLottieRound is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieRound around as a copy, so every C++ QLottieRound behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRound that has a ritual and that Python can
  call so far, 6 names in all: 'clone', 'parse', 'updateProperties',
  'acceptsTrim', 'position', 'radius'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieRound::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QLottieRound::~QLottieRound()': the destructor: Python removes its
    C++ QLottieRound by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieRound is created at the first use, not by
    'QLottieRound(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRound back gives a copy the ritual made for
    Python, in a new cute QLottieRound.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieRound'

  #  A C++ QLottieRound Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRound'

  #  Qt's '~QLottieRound()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieRound behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieRoundD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieRound::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieRound::clone() const
    ritual = 'ritual_ZNK12QLottieRound5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieRound5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieRound::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#acceptsTrim
    """
    #  bool QLottieRound::acceptsTrim() const
    ritual = 'ritual_ZNK12QLottieRound11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieRound11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieRound::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieRound::position() const
    address = self.uglySide.call('ritual_ZNK12QLottieRound8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QLottieRound::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#radius
    """
    #  qreal QLottieRound::radius() const
    return self.uglySide.call('ritual_ZNK12QLottieRound6radiusEv')

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
  def __init__(self, other: QLottieRound) -> None:
    """
    Notes what was given, for Qt's 'QLottieRound::QLottieRound(const
    QLottieRound &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#QLottieRound

    Parameters
    ----------

    other : QLottieRound
      Passed on as a value: Qt reads the C++ QLottieRound, which stays
      Python's own.
    """
    #  QLottieRound::QLottieRound(const QLottieRound &other)
    self._noteCreation(QLottieRound, lambda: Rituals.call(
        'ritual_ZN12QLottieRoundC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieRound::QLottieRound(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#QLottieRound

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieRound::QLottieRound(QLottieBase *parent)
    self._noteCreation(QLottieRound, lambda: Rituals.call(
        'ritual_ZN12QLottieRoundC1EP11QLottieBase', self._addressOf(parent),
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
    Calls Qt's 'int QLottieRound::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieRound::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN12QLottieRound5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieRound5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieRound::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieround.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieRound::updateProperties(int frame)
    ritual = 'ritual_ZN12QLottieRound16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieRound16updatePropertiesEi'
    self.uglySide.call(ritual, frame)
