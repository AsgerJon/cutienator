"""
QLottieShapeLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieshapelayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieShapeLayer to be private: it declares the class in a
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


class QLottieShapeLayer(QLottieLayer):
  """
  The cute side of Qt's QLottieShapeLayer: a plain Python object standing in
  front of one C++ QLottieShapeLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottieShapeLayer is built
  on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottieShapeLayer around as a copy, so every C++
  QLottieShapeLayer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieShapeLayer that has a ritual and that Python
  can call so far, 3 names in all: 'clone', 'updateProperties', 'parse'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieShapeLayer::render(QLottieRenderer &render) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieShapeLayer::~QLottieShapeLayer()': the destructor: Python
    removes its C++ QLottieShapeLayer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieShapeLayer is created at the first use, not by
    'QLottieShapeLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieShapeLayer back gives a copy the ritual made
    for Python, in a new cute QLottieShapeLayer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieShapeLayer'

  #  Qt's '~QLottieShapeLayer()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieShapeLayer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QLottieShapeLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieShapeLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapelayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieShapeLayer::clone() const
    ritual = 'ritual_ZNK17QLottieShapeLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QLottieShapeLayer5cloneEv'
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
    Notes what was given, for Qt's 'QLottieShapeLayer::QLottieShapeLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapelayer.html#QLottieShapeLayer
    """
    #  QLottieShapeLayer::QLottieShapeLayer()
    self._noteCreation(QLottieShapeLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieShapeLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieShapeLayer) -> None:
    """
    Notes what was given, for Qt's
    'QLottieShapeLayer::QLottieShapeLayer(const QLottieShapeLayer &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapelayer.html#QLottieShapeLayer

    Parameters
    ----------

    other : QLottieShapeLayer
      Passed on as a value: Qt reads the C++ QLottieShapeLayer, which stays
      Python's own.
    """
    #  QLottieShapeLayer::QLottieShapeLayer(const QLottieShapeLayer &other)
    self._noteCreation(QLottieShapeLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieShapeLayerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QLottieShapeLayer::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapelayer.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieShapeLayer::updateProperties(int frame)
    ritual = 'ritual_ZN17QLottieShapeLayer16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QLottieShapeLayer16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieShapeLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapelayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieShapeLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN17QLottieShapeLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QLottieShapeLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))
