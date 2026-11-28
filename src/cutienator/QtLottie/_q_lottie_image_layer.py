"""
QLottieImageLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieImageLayer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QLottieImageLayer(QLottieLayer):
  """
  The cute side of Qt's QLottieImageLayer: a plain Python object standing in
  front of one C++ QLottieImageLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottieImageLayer is built
  on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottieImageLayer around as a copy, so every C++
  QLottieImageLayer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieImageLayer that has a ritual and that Python
  can call so far, 2 names in all: 'clone', 'parse'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieImageLayer::render(QLottieRenderer &render) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieImageLayer::~QLottieImageLayer()': the destructor: Python
    removes its C++ QLottieImageLayer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieImageLayer is created at the first use, not by
    'QLottieImageLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieImageLayer back gives a copy the ritual made
    for Python, in a new cute QLottieImageLayer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieImageLayer'

  #  A C++ QLottieImageLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieImageLayer'

  #  Qt's '~QLottieImageLayer()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieImageLayer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QLottieImageLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieImageLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimagelayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieImageLayer::clone() const
    ritual = 'ritual_ZNK17QLottieImageLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QLottieImageLayer5cloneEv'
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
    Notes what was given, for Qt's 'QLottieImageLayer::QLottieImageLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieimagelayer.html#QLottieImageLayer
    """
    #  QLottieImageLayer::QLottieImageLayer()
    self._noteCreation(QLottieImageLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieImageLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieImageLayer) -> None:
    """
    Notes what was given, for Qt's
    'QLottieImageLayer::QLottieImageLayer(const QLottieImageLayer &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieimagelayer.html#QLottieImageLayer

    Parameters
    ----------

    other : QLottieImageLayer
      Passed on as a value: Qt reads the C++ QLottieImageLayer, which stays
      Python's own.
    """
    #  QLottieImageLayer::QLottieImageLayer(const QLottieImageLayer &other)
    self._noteCreation(QLottieImageLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieImageLayerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'int QLottieImageLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimagelayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieImageLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN17QLottieImageLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QLottieImageLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))
