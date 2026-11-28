"""
QLottieSolidLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieSolidLayer to be private: it declares the class in a
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
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottieSolidLayer(QLottieLayer):
  """
  The cute side of Qt's QLottieSolidLayer: a plain Python object standing in
  front of one C++ QLottieSolidLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottieSolidLayer is built
  on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottieSolidLayer around as a copy, so every C++
  QLottieSolidLayer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieSolidLayer that has a ritual and that Python
  can call so far, 3 names in all: 'clone', 'parse', 'color'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieSolidLayer::render(QLottieRenderer &render) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieSolidLayer::~QLottieSolidLayer()': the destructor: Python
    removes its C++ QLottieSolidLayer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieSolidLayer is created at the first use, not by
    'QLottieSolidLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieSolidLayer back gives a copy the ritual made
    for Python, in a new cute QLottieSolidLayer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieSolidLayer'

  #  Qt's '~QLottieSolidLayer()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieSolidLayer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QLottieSolidLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieSolidLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiesolidlayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieSolidLayer::clone() const
    ritual = 'ritual_ZNK17QLottieSolidLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QLottieSolidLayer5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QLottieSolidLayer::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiesolidlayer.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLottieSolidLayer::color() const
    address = self.uglySide.call('ritual_ZNK17QLottieSolidLayer5colorEv')
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLottieSolidLayer::QLottieSolidLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiesolidlayer.html#QLottieSolidLayer
    """
    #  QLottieSolidLayer::QLottieSolidLayer()
    self._noteCreation(QLottieSolidLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieSolidLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieSolidLayer) -> None:
    """
    Notes what was given, for Qt's
    'QLottieSolidLayer::QLottieSolidLayer(const QLottieSolidLayer &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiesolidlayer.html#QLottieSolidLayer

    Parameters
    ----------

    other : QLottieSolidLayer
      Passed on as a value: Qt reads the C++ QLottieSolidLayer, which stays
      Python's own.
    """
    #  QLottieSolidLayer::QLottieSolidLayer(const QLottieSolidLayer &other)
    self._noteCreation(QLottieSolidLayer, lambda: Rituals.call(
        'ritual_ZN17QLottieSolidLayerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'int QLottieSolidLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiesolidlayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieSolidLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN17QLottieSolidLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QLottieSolidLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))
