"""
QSvgFilterContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgFilterContainer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtSvg, QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QImage, QPainter
  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgRectF = WAIT['QSvgRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgFilterContainer(QSvgStructureNode):
  """
  The cute side of Qt's QSvgFilterContainer: a plain Python object standing
  in front of one C++ QSvgFilterContainer.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgFilterContainer is
  built on Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFilterContainer that has a ritual and that
  Python can call so far, 8 names in all: 'type', 'applyFilter',
  'setSupported', 'supported', 'filterRegion', 'rect', 'filterUnits',
  'primitiveUnits'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFilterContainer::~QSvgFilterContainer()': the destructor:
    Python never removes a C++ QSvgFilterContainer.
  - Qt's 'void QSvgFilterContainer::drawCommand(QPainter *a0, QSvgExtraStates
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgFilterContainer::shouldDrawNode(QPainter *a0,
    QSvgExtraStates &a1) const': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QSvgFilterContainer is created at the first use, not by
    'QSvgFilterContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFilterContainer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFilterContainer'

  #  A C++ QSvgFilterContainer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFilterContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgFilterContainer::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfiltercontainer.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgFilterContainer::type() const
    ritual = 'ritual_ZNK19QSvgFilterContainer4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSvgFilterContainer4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(QImage, QPainter, QRectF)
  @overload(QImage, NoneType, QRectF)
  def applyFilter(
      self,
      buffer: QImage,
      p: Optional[QPainter],
      bounds: QRectF,
  ) -> QImage:
    """
    Calls Qt's 'QImage QSvgFilterContainer::applyFilter(const QImage &buffer,
    QPainter *p, const QRectF &bounds) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#applyFilter

    Parameters
    ----------

    buffer : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSvgFilterContainer::applyFilter(const QImage &buffer, QPainter
    #      *p, const QRectF &bounds) const
    address = self.uglySide.call(
        'ritual_ZNK19QSvgFilterContainer11applyFilterERK6QImageP8QPainterRK'
        '6QRectF',
        self._valueOf(buffer), self._addressOf(p), self._valueOf(bounds),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def supported(self) -> bool:
    """
    Calls Qt's 'bool QSvgFilterContainer::supported() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfiltercontainer.html#supported
    """
    #  bool QSvgFilterContainer::supported() const
    return self.uglySide.call('ritual_ZNK19QSvgFilterContainer9supportedEv')

  @overload(QRectF)
  def filterRegion(self, itemBounds: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgFilterContainer::filterRegion(const QRectF
    &itemBounds) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#filterRegion

    Parameters
    ----------

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgFilterContainer::filterRegion(const QRectF &itemBounds)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QSvgFilterContainer12filterRegionERK6QRectF',
        self._valueOf(itemBounds),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def rect(self) -> QSvgRectF:
    """
    Calls Qt's 'QSvgRectF QSvgFilterContainer::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfiltercontainer.html#rect

    Returns
    -------

    QSvgRectF
      A new cute QSvgRectF around the copy Qt gave back. Python owns it.
    """
    #  QSvgRectF QSvgFilterContainer::rect() const
    address = self.uglySide.call('ritual_ZNK19QSvgFilterContainer4rectEv')
    from . import QSvgRectF
    return QSvgRectF._cuteOwning(address)

  def filterUnits(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgFilterContainer::filterUnits() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#filterUnits

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgFilterContainer::filterUnits() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK19QSvgFilterContainer11filterUnitsEv',
    ))

  def primitiveUnits(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgFilterContainer::primitiveUnits()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#primitiveUnits

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgFilterContainer::primitiveUnits() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK19QSvgFilterContainer14primitiveUnitsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSupported(self, supported: bool) -> None:
    """
    Calls Qt's 'void QSvgFilterContainer::setSupported(bool supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#setSupported

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void QSvgFilterContainer::setSupported(bool supported)
    self.uglySide.call(
        'ritual_ZN19QSvgFilterContainer12setSupportedEb', supported,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgNode, QSvgRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  @overload(NoneType, QSvgRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QSvgRectF,
      filterUnits: QtSvg.UnitTypes,
      primitiveUnits: QtSvg.UnitTypes,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSvgFilterContainer::QSvgFilterContainer(QSvgNode *parent, const
    QSvgRectF &bounds, QtSvg::UnitTypes filterUnits, QtSvg::UnitTypes
    primitiveUnits)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfiltercontainer.html#QSvgFilterContainer

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QSvgRectF
      Passed on as a value: Qt reads the C++ QSvgRectF, which stays Python's
      own.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  QSvgFilterContainer::QSvgFilterContainer(QSvgNode *parent, const
    #      QSvgRectF &bounds, QtSvg::UnitTypes filterUnits, QtSvg::UnitTypes
    #      primitiveUnits)
    self._noteCreation(QSvgFilterContainer, lambda: Rituals.call(
        'ritual_ZN19QSvgFilterContainerC1EP8QSvgNodeRK9QSvgRectFN5QtSvg9Uni'
        'tTypesES6_',
        self._addressOf(parent), self._valueOf(bounds), filterUnits.value,
        primitiveUnits.value,
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
