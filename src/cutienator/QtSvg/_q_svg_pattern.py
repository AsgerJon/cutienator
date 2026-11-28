"""
QSvgPattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgPattern to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtSvg, QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QTransform
  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSvgRectF = WAIT['QSvgRectF']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgPattern(QSvgStructureNode):
  """
  The cute side of Qt's QSvgPattern: a plain Python object standing in front
  of one C++ QSvgPattern.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgPattern is built
  on Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgPattern that has a ritual and that Python can
  call so far, 6 names in all: 'type', 'appliedTransform', 'transform',
  'rect', 'viewBox', 'contentUnits'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgPattern::~QSvgPattern()': the destructor: Python never removes
    a C++ QSvgPattern.
  - Qt's 'void QSvgPattern::drawCommand(QPainter *a0, QSvgExtraStates &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgPattern::shouldDrawNode(QPainter *a0, QSvgExtraStates &a1)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QImage QSvgPattern::patternImage(QPainter *p, QSvgExtraStates
    &states, const QSvgNode *patternElement)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QImage QSvgPattern::renderPattern(QSize size, std::pair<qreal,
    qreal> contentScale, const QSvgExtraStates &states)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QSvgPattern::calculateAppliedTransform(QTransform
    &worldTransform, QRectF peLocalBB, QSize imageSize)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgPattern is created at the first use, not by
    'QSvgPattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgPattern.
  - Each name of Qt's QSvgPattern that has no cute function yet,
    'calculateAppliedTransform', 'patternImage', 'renderPattern', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgPattern'

  #  A C++ QSvgPattern Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgPattern'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgPattern::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgPattern::type() const
    ritual = 'ritual_ZNK11QSvgPattern4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgPattern4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def appliedTransform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QSvgPattern::appliedTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#appliedTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QSvgPattern::appliedTransform() const
    address = self.uglySide.call(
        'ritual_ZNK11QSvgPattern16appliedTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QSvgPattern::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QSvgPattern::transform() const
    address = self.uglySide.call('ritual_ZNK11QSvgPattern9transformEv')
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def rect(self) -> QSvgRectF:
    """
    Calls Qt's 'const QSvgRectF &QSvgPattern::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#rect

    Returns
    -------

    QSvgRectF
      A new cute QSvgRectF around the copy Qt gave back. Python owns it.
    """
    #  const QSvgRectF &QSvgPattern::rect() const
    address = self.uglySide.call('ritual_ZNK11QSvgPattern4rectEv')
    from . import QSvgRectF
    return QSvgRectF._cuteOwning(address)

  def viewBox(self) -> QRectF:
    """
    Calls Qt's 'const QRectF &QSvgPattern::viewBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#viewBox

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  const QRectF &QSvgPattern::viewBox() const
    address = self.uglySide.call('ritual_ZNK11QSvgPattern7viewBoxEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def contentUnits(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgPattern::contentUnits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#contentUnits

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgPattern::contentUnits() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK11QSvgPattern12contentUnitsEv',
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

  @overload(QSvgNode, QSvgRectF, QRectF, QtSvg.UnitTypes, QTransform)
  @overload(NoneType, QSvgRectF, QRectF, QtSvg.UnitTypes, QTransform)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QSvgRectF,
      viewBox: QRectF,
      contentUnits: QtSvg.UnitTypes,
      transform: QTransform,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgPattern::QSvgPattern(QSvgNode
    *parent, QSvgRectF bounds, QRectF viewBox, QtSvg::UnitTypes contentUnits,
    QTransform transform)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpattern.html#QSvgPattern

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QSvgRectF
      Passed on as a value: Qt reads the C++ QSvgRectF, which stays Python's
      own.

    viewBox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    contentUnits : QtSvg.UnitTypes
      Passed on as its number.

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QSvgPattern::QSvgPattern(QSvgNode *parent, QSvgRectF bounds, QRectF
    #      viewBox, QtSvg::UnitTypes contentUnits, QTransform transform)
    self._noteCreation(QSvgPattern, lambda: Rituals.call(
        'ritual_ZN11QSvgPatternC1EP8QSvgNode9QSvgRectF6QRectFN5QtSvg9UnitTy'
        'pesE10QTransform',
        self._addressOf(parent), self._valueOf(bounds),
        self._valueOf(viewBox), contentUnits.value, self._valueOf(transform),
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

  @staticmethod
  def calculateAppliedTransform(*__, **_) -> Never:
    """
    Qt's 'void QSvgPattern::calculateAppliedTransform(QTransform
    &worldTransform, QRectF peLocalBB, QSize imageSize)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgPattern.calculateAppliedTransform' has no cute function yet. "
        "Qt's 'void QSvgPattern::calculateAppliedTransform(QTransform "
        "&worldTransform, QRectF peLocalBB, QSize imageSize)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def patternImage(*__, **_) -> Never:
    """
    Qt's 'QImage QSvgPattern::patternImage(QPainter *p, QSvgExtraStates
    &states, const QSvgNode *patternElement)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgPattern.patternImage' has no cute function yet. Qt's 'QImage "
        "QSvgPattern::patternImage(QPainter *p, QSvgExtraStates &states, "
        "const QSvgNode *patternElement)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def renderPattern(*__, **_) -> Never:
    """
    Qt's 'QImage QSvgPattern::renderPattern(QSize size, std::pair<qreal,
    qreal> contentScale, const QSvgExtraStates &states)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgPattern.renderPattern' has no cute function yet. Qt's 'QImage "
        "QSvgPattern::renderPattern(QSize size, std::pair<qreal, qreal> "
        "contentScale, const QSvgExtraStates &states)': takes a type Python "
        "has no way to hand over yet.")
