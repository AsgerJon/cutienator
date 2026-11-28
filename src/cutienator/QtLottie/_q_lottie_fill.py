"""
QLottieFill binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiefill_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieFill to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieFill(QLottieShape):
  """
  The cute side of Qt's QLottieFill: a plain Python object standing in front
  of one C++ QLottieFill.

  It is built on the cute 'QLottieShape', as Qt's QLottieFill is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieFill around as a copy, so every C++ QLottieFill behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieFill that has a ritual and that Python can
  call so far, 6 names in all: 'clone', 'updateProperties', 'parse', 'color',
  'opacity', 'fillRule'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieFill::render(QLottieRenderer &renderer) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QLottieProperty4D<QVector4D> QLottieFill::colorProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieFill::opacityProperty() const': gives
    a type Python has no way to take yet.
  - Qt's 'QLottieFill::~QLottieFill()': the destructor: Python removes its
    C++ QLottieFill by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieFill is created at the first use, not by
    'QLottieFill(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieFill back gives a copy the ritual made for
    Python, in a new cute QLottieFill.
  - Each name of Qt's QLottieFill that has no cute function yet,
    'colorProperty', 'opacityProperty', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieFill'

  #  A C++ QLottieFill Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieFill'

  #  Qt's '~QLottieFill()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieFill behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLottieFillD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieFill::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieFill::clone() const
    ritual = 'ritual_ZNK11QLottieFill5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieFill5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QLottieFill::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLottieFill::color() const
    address = self.uglySide.call('ritual_ZNK11QLottieFill5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieFill::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#opacity
    """
    #  qreal QLottieFill::opacity() const
    return self.uglySide.call('ritual_ZNK11QLottieFill7opacityEv')

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QLottieFill::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QLottieFill::fillRule() const
    return Qt.FillRule(self.uglySide.call(
        'ritual_ZNK11QLottieFill8fillRuleEv',
    ))

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
  def __init__(self, other: QLottieFill) -> None:
    """
    Notes what was given, for Qt's 'QLottieFill::QLottieFill(const
    QLottieFill &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#QLottieFill

    Parameters
    ----------

    other : QLottieFill
      Passed on as a value: Qt reads the C++ QLottieFill, which stays
      Python's own.
    """
    #  QLottieFill::QLottieFill(const QLottieFill &other)
    self._noteCreation(QLottieFill, lambda: Rituals.call(
        'ritual_ZN11QLottieFillC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieFill::QLottieFill(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#QLottieFill

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieFill::QLottieFill(QLottieBase *parent)
    self._noteCreation(QLottieFill, lambda: Rituals.call(
        'ritual_ZN11QLottieFillC1EP11QLottieBase', self._addressOf(parent),
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
    Calls Qt's 'void QLottieFill::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieFill::updateProperties(int frame)
    ritual = 'ritual_ZN11QLottieFill16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieFill16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieFill::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefill.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieFill::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN11QLottieFill5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieFill5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def colorProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty4D<QVector4D> QLottieFill::colorProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieFill.colorProperty' has no cute function yet. Qt's "
        "'QLottieProperty4D<QVector4D> QLottieFill::colorProperty() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def opacityProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieFill::opacityProperty() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieFill.opacityProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieFill::opacityProperty() const': "
        "gives a type Python has no way to take yet.")
