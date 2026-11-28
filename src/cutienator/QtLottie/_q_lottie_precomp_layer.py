"""
QLottiePrecompLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieprecomplayer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottiePrecompLayer to be private: it declares the class in a
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
  from typing import Never, Optional

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottiePrecompLayer(QLottieLayer):
  """
  The cute side of Qt's QLottiePrecompLayer: a plain Python object standing
  in front of one C++ QLottiePrecompLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottiePrecompLayer is
  built on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottiePrecompLayer around as a copy, so every C++
  QLottiePrecompLayer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottiePrecompLayer that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'updateProperties',
  'parse', 'refId'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottiePrecompLayer::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty<qreal> QLottiePrecompLayer::timeRemapProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottiePrecompLayer::~QLottiePrecompLayer()': the destructor:
    Python removes its C++ QLottiePrecompLayer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottiePrecompLayer is created at the first use, not by
    'QLottiePrecompLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottiePrecompLayer back gives a copy the ritual made
    for Python, in a new cute QLottiePrecompLayer.
  - Each name of Qt's QLottiePrecompLayer that has no cute function yet,
    'timeRemapProperty', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottiePrecompLayer'

  #  Qt's '~QLottiePrecompLayer()'. Naming it makes this a value class:
  #  Python owns every C++ QLottiePrecompLayer behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QLottiePrecompLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottiePrecompLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomplayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottiePrecompLayer::clone() const
    ritual = 'ritual_ZNK19QLottiePrecompLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QLottiePrecompLayer5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def refId(self) -> str:
    """
    Calls Qt's 'QString QLottiePrecompLayer::refId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomplayer.html#refId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLottiePrecompLayer::refId() const
    return self.uglySide.call('ritual_ZNK19QLottiePrecompLayer5refIdEv')

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
    Notes what was given, for Qt's
    'QLottiePrecompLayer::QLottiePrecompLayer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomplayer.html#QLottiePrecompLayer
    """
    #  QLottiePrecompLayer::QLottiePrecompLayer()
    self._noteCreation(QLottiePrecompLayer, lambda: Rituals.call(
        'ritual_ZN19QLottiePrecompLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottiePrecompLayer) -> None:
    """
    Notes what was given, for Qt's
    'QLottiePrecompLayer::QLottiePrecompLayer(const QLottiePrecompLayer
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomplayer.html#QLottiePrecompLayer

    Parameters
    ----------

    other : QLottiePrecompLayer
      Passed on as a value: Qt reads the C++ QLottiePrecompLayer, which stays
      Python's own.
    """
    #  QLottiePrecompLayer::QLottiePrecompLayer(const QLottiePrecompLayer
    #      &other)
    self._noteCreation(QLottiePrecompLayer, lambda: Rituals.call(
        'ritual_ZN19QLottiePrecompLayerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QLottiePrecompLayer::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomplayer.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottiePrecompLayer::updateProperties(int frame)
    ritual = 'ritual_ZN19QLottiePrecompLayer16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QLottiePrecompLayer16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottiePrecompLayer::parse(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomplayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottiePrecompLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN19QLottiePrecompLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QLottiePrecompLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def timeRemapProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottiePrecompLayer::timeRemapProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottiePrecompLayer.timeRemapProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> "
        "QLottiePrecompLayer::timeRemapProperty() const': gives a type "
        "Python has no way to take yet.")
