"""
QLottieFillEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiefilleffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieFillEffect to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottieFillEffect(QLottieBase):
  """
  The cute side of Qt's QLottieFillEffect: a plain Python object standing in
  front of one C++ QLottieFillEffect.

  It is built on the cute 'QLottieBase', as Qt's QLottieFillEffect is built
  on Qt's QLottieBase, and has everything that class has.

  C++ hands a QLottieFillEffect around as a copy, so every C++
  QLottieFillEffect behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieFillEffect that has a ritual and that Python
  can call so far, 5 names in all: 'clone', 'construct', 'updateProperties',
  'color', 'opacity'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieFillEffect::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieFillEffect::~QLottieFillEffect()': the destructor: Python
    removes its C++ QLottieFillEffect by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieFillEffect is created at the first use, not by
    'QLottieFillEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieFillEffect back gives a copy the ritual made
    for Python, in a new cute QLottieFillEffect.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieFillEffect'

  #  A C++ QLottieFillEffect Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieFillEffect'

  #  Qt's '~QLottieFillEffect()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieFillEffect behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QLottieFillEffectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieFillEffect::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefilleffect.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieFillEffect::clone() const
    ritual = 'ritual_ZNK17QLottieFillEffect5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QLottieFillEffect5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QLottieFillEffect::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefilleffect.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLottieFillEffect::color() const
    address = self.uglySide.call('ritual_ZNK17QLottieFillEffect5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieFillEffect::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefilleffect.html#opacity
    """
    #  qreal QLottieFillEffect::opacity() const
    return self.uglySide.call('ritual_ZNK17QLottieFillEffect7opacityEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLottieFillEffect::QLottieFillEffect()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefilleffect.html#QLottieFillEffect
    """
    #  QLottieFillEffect::QLottieFillEffect()
    self._noteCreation(QLottieFillEffect, lambda: Rituals.call(
        'ritual_ZN17QLottieFillEffectC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieFillEffect) -> None:
    """
    Notes what was given, for Qt's
    'QLottieFillEffect::QLottieFillEffect(const QLottieFillEffect &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefilleffect.html#QLottieFillEffect

    Parameters
    ----------

    other : QLottieFillEffect
      Passed on as a value: Qt reads the C++ QLottieFillEffect, which stays
      Python's own.
    """
    #  QLottieFillEffect::QLottieFillEffect(const QLottieFillEffect &other)
    self._noteCreation(QLottieFillEffect, lambda: Rituals.call(
        'ritual_ZN17QLottieFillEffectC1ERKS_', self._valueOf(other),
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
  def construct(self, definition: QJsonObject) -> None:
    """
    Calls Qt's 'void QLottieFillEffect::construct(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefilleffect.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QLottieFillEffect::construct(const QJsonObject &definition)
    self.uglySide.call(
        'ritual_ZN17QLottieFillEffect9constructERK11QJsonObject',
        self._valueOf(definition),
    )

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieFillEffect::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefilleffect.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieFillEffect::updateProperties(int frame)
    ritual = 'ritual_ZN17QLottieFillEffect16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QLottieFillEffect16updatePropertiesEi'
    self.uglySide.call(ritual, frame)
