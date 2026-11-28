"""
QLottieNullLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieNullLayer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieLayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottieNullLayer(QLottieLayer):
  """
  The cute side of Qt's QLottieNullLayer: a plain Python object standing in
  front of one C++ QLottieNullLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottieNullLayer is built
  on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottieNullLayer around as a copy, so every C++
  QLottieNullLayer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieNullLayer that has a ritual and that Python
  can call so far, 2 names in all: 'clone', 'parse'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieNullLayer::render(QLottieRenderer &render) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieNullLayer::~QLottieNullLayer()': the destructor: Python
    removes its C++ QLottieNullLayer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieNullLayer is created at the first use, not by
    'QLottieNullLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieNullLayer back gives a copy the ritual made
    for Python, in a new cute QLottieNullLayer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieNullLayer'

  #  A C++ QLottieNullLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieNullLayer'

  #  Qt's '~QLottieNullLayer()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieNullLayer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QLottieNullLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieNullLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottienulllayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieNullLayer::clone() const
    ritual = 'ritual_ZNK16QLottieNullLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QLottieNullLayer5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

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
    Notes what was given, for Qt's 'QLottieNullLayer::QLottieNullLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottienulllayer.html#QLottieNullLayer
    """
    #  QLottieNullLayer::QLottieNullLayer()
    self._noteCreation(QLottieNullLayer, lambda: Rituals.call(
        'ritual_ZN16QLottieNullLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieNullLayer) -> None:
    """
    Notes what was given, for Qt's 'QLottieNullLayer::QLottieNullLayer(const
    QLottieNullLayer &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottienulllayer.html#QLottieNullLayer

    Parameters
    ----------

    other : QLottieNullLayer
      Passed on as a value: Qt reads the C++ QLottieNullLayer, which stays
      Python's own.
    """
    #  QLottieNullLayer::QLottieNullLayer(const QLottieNullLayer &other)
    self._noteCreation(QLottieNullLayer, lambda: Rituals.call(
        'ritual_ZN16QLottieNullLayerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'int QLottieNullLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottienulllayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieNullLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN16QLottieNullLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QLottieNullLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))
