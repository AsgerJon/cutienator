"""
QLottieRepeater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottierepeater_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieRepeater to be private: it declares the class in a header
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
  from typing import Optional

  from . import QLottieRepeaterTransform
  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieRepeater(QLottieShape):
  """
  The cute side of Qt's QLottieRepeater: a plain Python object standing in
  front of one C++ QLottieRepeater.

  It is built on the cute 'QLottieShape', as Qt's QLottieRepeater is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieRepeater around as a copy, so every C++ QLottieRepeater
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRepeater that has a ritual and that Python
  can call so far, 6 names in all: 'clone', 'construct', 'updateProperties',
  'copies', 'offset', 'transform'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieRepeater::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieRepeater::~QLottieRepeater()': the destructor: Python
    removes its C++ QLottieRepeater by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieRepeater is created at the first use, not by
    'QLottieRepeater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRepeater back gives a copy the ritual made for
    Python, in a new cute QLottieRepeater.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieRepeater'

  #  A C++ QLottieRepeater Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRepeater'

  #  Qt's '~QLottieRepeater()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieRepeater behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QLottieRepeaterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieRepeater::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierepeater.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieRepeater::clone() const
    ritual = 'ritual_ZNK15QLottieRepeater5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottieRepeater5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def copies(self) -> int:
    """
    Calls Qt's 'int QLottieRepeater::copies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierepeater.html#copies
    """
    #  int QLottieRepeater::copies() const
    return self.uglySide.call('ritual_ZNK15QLottieRepeater6copiesEv')

  def offset(self) -> float:
    """
    Calls Qt's 'qreal QLottieRepeater::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierepeater.html#offset
    """
    #  qreal QLottieRepeater::offset() const
    return self.uglySide.call('ritual_ZNK15QLottieRepeater6offsetEv')

  def transform(self) -> QLottieRepeaterTransform:
    """
    Calls Qt's 'const QLottieRepeaterTransform &QLottieRepeater::transform()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierepeater.html#transform

    Returns
    -------

    QLottieRepeaterTransform
      A new cute QLottieRepeaterTransform around the copy Qt gave back.
      Python owns it.
    """
    #  const QLottieRepeaterTransform &QLottieRepeater::transform() const
    address = self.uglySide.call('ritual_ZNK15QLottieRepeater9transformEv')
    from . import QLottieRepeaterTransform
    return QLottieRepeaterTransform._cuteOwning(address)

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
    Notes what was given, for Qt's 'QLottieRepeater::QLottieRepeater()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeater.html#QLottieRepeater
    """
    #  QLottieRepeater::QLottieRepeater()
    self._noteCreation(QLottieRepeater, lambda: Rituals.call(
        'ritual_ZN15QLottieRepeaterC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieRepeater) -> None:
    """
    Notes what was given, for Qt's 'QLottieRepeater::QLottieRepeater(const
    QLottieRepeater &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeater.html#QLottieRepeater

    Parameters
    ----------

    other : QLottieRepeater
      Passed on as a value: Qt reads the C++ QLottieRepeater, which stays
      Python's own.
    """
    #  QLottieRepeater::QLottieRepeater(const QLottieRepeater &other)
    self._noteCreation(QLottieRepeater, lambda: Rituals.call(
        'ritual_ZN15QLottieRepeaterC1ERKS_', self._valueOf(other),
    ))

  @overload(QJsonObject)
  @overload(QJsonObject, QLottieBase)
  @overload(QJsonObject, NoneType)
  def __init__(
      self,
      definition: QJsonObject,
      parent: Optional[QLottieBase] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLottieRepeater::QLottieRepeater(const
    QJsonObject &definition, QLottieBase *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeater.html#QLottieRepeater

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieRepeater::QLottieRepeater(const QJsonObject &definition,
    #      QLottieBase *parent)
    self._noteCreation(QLottieRepeater, lambda: Rituals.call(
        'ritual_ZN15QLottieRepeaterC1ERK11QJsonObjectP11QLottieBase',
        self._valueOf(definition), self._addressOf(parent),
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
    Calls Qt's 'void QLottieRepeater::construct(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierepeater.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QLottieRepeater::construct(const QJsonObject &definition)
    self.uglySide.call(
        'ritual_ZN15QLottieRepeater9constructERK11QJsonObject',
        self._valueOf(definition),
    )

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieRepeater::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeater.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieRepeater::updateProperties(int frame)
    ritual = 'ritual_ZN15QLottieRepeater16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieRepeater16updatePropertiesEi'
    self.uglySide.call(ritual, frame)
