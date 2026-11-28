"""
QLottieGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiegroup_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieGroup to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QLottieTrimPath
  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QLottieTrimPath = WAIT['QLottieTrimPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieGroup(QLottieShape):
  """
  The cute side of Qt's QLottieGroup: a plain Python object standing in front
  of one C++ QLottieGroup.

  It is built on the cute 'QLottieShape', as Qt's QLottieGroup is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieGroup around as a copy, so every C++ QLottieGroup behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieGroup that has a ritual and that Python can
  call so far, 5 names in all: 'clone', 'updateProperties', 'parse',
  'acceptsTrim', 'applyTrim'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieGroup::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QLottieGroup::~QLottieGroup()': the destructor: Python removes its
    C++ QLottieGroup by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieGroup is created at the first use, not by
    'QLottieGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieGroup back gives a copy the ritual made for
    Python, in a new cute QLottieGroup.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieGroup'

  #  A C++ QLottieGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieGroup'

  #  Qt's '~QLottieGroup()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieGroup behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieGroupD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieGroup::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieGroup::clone() const
    ritual = 'ritual_ZNK12QLottieGroup5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieGroup5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieGroup::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#acceptsTrim
    """
    #  bool QLottieGroup::acceptsTrim() const
    ritual = 'ritual_ZNK12QLottieGroup11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieGroup11acceptsTrimEv'
    return self.uglySide.call(ritual)

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
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieGroup::QLottieGroup(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#QLottieGroup

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieGroup::QLottieGroup(QLottieBase *parent)
    self._noteCreation(QLottieGroup, lambda: Rituals.call(
        'ritual_ZN12QLottieGroupC1EP11QLottieBase', self._addressOf(parent),
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
    Calls Qt's 'void QLottieGroup::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieGroup::updateProperties(int frame)
    ritual = 'ritual_ZN12QLottieGroup16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieGroup16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieGroup::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieGroup::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN12QLottieGroup5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieGroup5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(QLottieTrimPath)
  def applyTrim(self, trimmer: QLottieTrimPath) -> None:
    """
    Calls Qt's 'void QLottieGroup::applyTrim(const QLottieTrimPath
    &trimmer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegroup.html#applyTrim

    Parameters
    ----------

    trimmer : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  void QLottieGroup::applyTrim(const QLottieTrimPath &trimmer)
    ritual = 'ritual_ZN12QLottieGroup9applyTrimERK15QLottieTrimPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieGroup9applyTrimERK15QLottieTrimPath'
    self.uglySide.call(ritual, self._valueOf(trimmer))
