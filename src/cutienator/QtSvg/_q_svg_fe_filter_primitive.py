"""
QSvgFeFilterPrimitive binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgFeFilterPrimitive to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QtSvg, QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgFeFilterPrimitive(QSvgStructureNode):
  """
  The cute side of Qt's QSvgFeFilterPrimitive: a plain Python object standing
  in front of one C++ QSvgFeFilterPrimitive.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgFeFilterPrimitive
  is built on Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFeFilterPrimitive that has a ritual and that
  Python can call so far, 9 names in all: 'localSubRegion',
  'globalSubRegion', 'clipToTransformedBounds', 'apply',
  'requiresSourceAlpha', 'input', 'result', 'rect', 'castToFilterPrimitive'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFeFilterPrimitive::~QSvgFeFilterPrimitive()': the destructor:
    Python never removes a C++ QSvgFeFilterPrimitive.
  - Qt's 'void QSvgFeFilterPrimitive::drawCommand(QPainter *a0,
    QSvgExtraStates &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgFeFilterPrimitive::shouldDrawNode(QPainter *a0,
    QSvgExtraStates &a1) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QRectF QSvgFeFilterPrimitive::internalFastBounds(QPainter *a0,
    QSvgExtraStates &a1) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QRectF QSvgFeFilterPrimitive::internalBounds(QPainter *a0,
    QSvgExtraStates &a1) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QSvgFeFilterPrimitive is created at the first use, not by
    'QSvgFeFilterPrimitive(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFeFilterPrimitive.
  - Each name of Qt's QSvgFeFilterPrimitive that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSvgNode)
  @overload(NoneType)
  def castToFilterPrimitive(
      node: Optional[QSvgNode],
  ) -> Optional[QSvgFeFilterPrimitive]:
    """
    Calls Qt's 'const QSvgFeFilterPrimitive
    *QSvgFeFilterPrimitive::castToFilterPrimitive(const QSvgNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#castToFilterPrimitive

    Parameters
    ----------

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSvgFeFilterPrimitive]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSvgFeFilterPrimitive
    #      *QSvgFeFilterPrimitive::castToFilterPrimitive(const QSvgNode
    #      *node)
    address = Rituals.call(
        'ritual_ZN21QSvgFeFilterPrimitive21castToFilterPrimitiveEPK8QSvgNod'
        'e',
        CuteMixin._addressOf(node),
    )
    return QSvgFeFilterPrimitive._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFeFilterPrimitive'

  #  A C++ QSvgFeFilterPrimitive Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFeFilterPrimitive'

  #  The functions Qt calls itself that QSvgFeFilterPrimitive is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'apply': (
          'QImage QSvgFeFilterPrimitive::apply(const QMap<QString, QImage> '
          '&, QPainter *, const QRectF &, const QRectF &, '
          'QtSvg::UnitTypes, QtSvg::UnitTypes) const',
      ),
  }

  #  The functions Qt calls itself that QSvgFeFilterPrimitive is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'requiresSourceAlpha': (
          ('_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF, QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  def localSubRegion(
      self,
      itemBounds: QRectF,
      filterBounds: QRectF,
      primitiveUnits: QtSvg.UnitTypes,
      filterUnits: QtSvg.UnitTypes,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgFeFilterPrimitive::localSubRegion(const QRectF
    &itemBounds, const QRectF &filterBounds, QtSvg::UnitTypes primitiveUnits,
    QtSvg::UnitTypes filterUnits) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#localSubRegion

    Parameters
    ----------

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    filterBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgFeFilterPrimitive::localSubRegion(const QRectF &itemBounds,
    #      const QRectF &filterBounds, QtSvg::UnitTypes primitiveUnits,
    #      QtSvg::UnitTypes filterUnits) const
    address = self.uglySide.call(
        'ritual_ZNK21QSvgFeFilterPrimitive14localSubRegionERK6QRectFS2_N5Qt'
        'Svg9UnitTypesES4_',
        self._valueOf(itemBounds), self._valueOf(filterBounds),
        primitiveUnits.value, filterUnits.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPainter, QRectF, QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  @overload(NoneType, QRectF, QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  def globalSubRegion(
      self,
      p: Optional[QPainter],
      itemBounds: QRectF,
      filterBounds: QRectF,
      primitiveUnits: QtSvg.UnitTypes,
      filterUnits: QtSvg.UnitTypes,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgFeFilterPrimitive::globalSubRegion(QPainter *p,
    const QRectF &itemBounds, const QRectF &filterBounds, QtSvg::UnitTypes
    primitiveUnits, QtSvg::UnitTypes filterUnits) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#globalSubRegion

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    filterBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgFeFilterPrimitive::globalSubRegion(QPainter *p, const
    #      QRectF &itemBounds, const QRectF &filterBounds, QtSvg::UnitTypes
    #      primitiveUnits, QtSvg::UnitTypes filterUnits) const
    address = self.uglySide.call(
        'ritual_ZNK21QSvgFeFilterPrimitive15globalSubRegionEP8QPainterRK6QR'
        'ectFS4_N5QtSvg9UnitTypesES6_',
        self._addressOf(p), self._valueOf(itemBounds),
        self._valueOf(filterBounds), primitiveUnits.value, filterUnits.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(
      QMap[str, QImage], QPainter, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  @overload(
      QMap[str, QImage], NoneType, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  def apply(
      self,
      sources: QMap[str, QImage],
      p: Optional[QPainter],
      itemBounds: QRectF,
      filterBounds: QRectF,
      primitiveUnits: QtSvg.UnitTypes,
      filterUnits: QtSvg.UnitTypes,
  ) -> QImage:
    """
    Calls Qt's 'QImage QSvgFeFilterPrimitive::apply(const QMap<QString,
    QImage> &sources, QPainter *p, const QRectF &itemBounds, const QRectF
    &filterBounds, QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes
    filterUnits) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#apply

    Parameters
    ----------

    sources : QMap[str, QImage]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    filterBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSvgFeFilterPrimitive::apply(const QMap<QString, QImage>
    #      &sources, QPainter *p, const QRectF &itemBounds, const QRectF
    #      &filterBounds, QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes
    #      filterUnits) const
    address = self.uglySide.call(
        'ritual_ZNK21QSvgFeFilterPrimitive5applyERK4QMapI7QString6QImageEP8'
        'QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_',
        self._valueOf(sources), self._addressOf(p),
        self._valueOf(itemBounds), self._valueOf(filterBounds),
        primitiveUnits.value, filterUnits.value,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def requiresSourceAlpha(self) -> bool:
    """
    Calls Qt's 'bool QSvgFeFilterPrimitive::requiresSourceAlpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#requiresSourceAlpha
    """
    #  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
    ritual = 'ritual_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv'
    return self.uglySide.call(ritual)

  def input(self) -> str:
    """
    Calls Qt's 'QString QSvgFeFilterPrimitive::input() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#input

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgFeFilterPrimitive::input() const
    return self.uglySide.call('ritual_ZNK21QSvgFeFilterPrimitive5inputEv')

  def result(self) -> str:
    """
    Calls Qt's 'QString QSvgFeFilterPrimitive::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#result

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgFeFilterPrimitive::result() const
    return self.uglySide.call('ritual_ZNK21QSvgFeFilterPrimitive6resultEv')

  def rect(self) -> QSvgRectF:
    """
    Calls Qt's 'QSvgRectF QSvgFeFilterPrimitive::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#rect

    Returns
    -------

    QSvgRectF
      A new cute QSvgRectF around the copy Qt gave back. Python owns it.
    """
    #  QSvgRectF QSvgFeFilterPrimitive::rect() const
    address = self.uglySide.call('ritual_ZNK21QSvgFeFilterPrimitive4rectEv')
    from . import QSvgRectF
    return QSvgRectF._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSvgFeFilterPrimitive::QSvgFeFilterPrimitive(QSvgNode *parent,
    const QString &input, const QString &result, const QSvgRectF &rect)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSvgFeFilterPrimitive.__init__' has no cute function yet. Qt's "
        "'QSvgFeFilterPrimitive::QSvgFeFilterPrimitive(QSvgNode *parent, "
        "const QString &input, const QString &result, const QSvgRectF "
        "&rect)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(QImage, QPainter, QRectF)
  @overload(QImage, NoneType, QRectF)
  @overload(NoneType, QPainter, QRectF)
  @overload(NoneType, NoneType, QRectF)
  def clipToTransformedBounds(
      self,
      buffer: Optional[QImage],
      p: Optional[QPainter],
      localRect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QSvgFeFilterPrimitive::clipToTransformedBounds(QImage
    *buffer, QPainter *p, const QRectF &localRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfefilterprimitive.html#clipToTransformedBounds

    Parameters
    ----------

    buffer : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgFeFilterPrimitive::clipToTransformedBounds(QImage *buffer,
    #      QPainter *p, const QRectF &localRect) const
    self.uglySide.call(
        'ritual_ZNK21QSvgFeFilterPrimitive23clipToTransformedBoundsEP6QImag'
        'eP8QPainterRK6QRectF',
        self._addressOf(buffer), self._addressOf(p),
        self._valueOf(localRect),
    )
