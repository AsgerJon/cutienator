"""
QSvgVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgvisitor_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgVisitor to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSvgAnimateNode, QSvgDefs, QSvgDocument, QSvgEllipse
  from . import QSvgFeFilterPrimitive, QSvgFilterContainer, QSvgG, QSvgImage
  from . import QSvgLine, QSvgMarker, QSvgMask, QSvgNode, QSvgPath
  from . import QSvgPattern, QSvgPolygon, QSvgPolyline, QSvgRect
  from . import QSvgStructureNode, QSvgSwitch, QSvgSymbol, QSvgText
  from . import QSvgTspan, QSvgUse, QSvgVideo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgAnimateNode = WAIT['QSvgAnimateNode']
  QSvgDefs = WAIT['QSvgDefs']
  QSvgDocument = WAIT['QSvgDocument']
  QSvgEllipse = WAIT['QSvgEllipse']
  QSvgFeFilterPrimitive = WAIT['QSvgFeFilterPrimitive']
  QSvgFilterContainer = WAIT['QSvgFilterContainer']
  QSvgG = WAIT['QSvgG']
  QSvgImage = WAIT['QSvgImage']
  QSvgLine = WAIT['QSvgLine']
  QSvgMarker = WAIT['QSvgMarker']
  QSvgMask = WAIT['QSvgMask']
  QSvgNode = WAIT['QSvgNode']
  QSvgPath = WAIT['QSvgPath']
  QSvgPattern = WAIT['QSvgPattern']
  QSvgPolygon = WAIT['QSvgPolygon']
  QSvgPolyline = WAIT['QSvgPolyline']
  QSvgRect = WAIT['QSvgRect']
  QSvgStructureNode = WAIT['QSvgStructureNode']
  QSvgSwitch = WAIT['QSvgSwitch']
  QSvgSymbol = WAIT['QSvgSymbol']
  QSvgText = WAIT['QSvgText']
  QSvgTspan = WAIT['QSvgTspan']
  QSvgUse = WAIT['QSvgUse']
  QSvgVideo = WAIT['QSvgVideo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgVisitor: a plain Python object standing in front
  of one C++ QSvgVisitor.

  What exists
  -----------

  Every function of Qt's QSvgVisitor that has a ritual and that Python can
  call so far, 36 names in all: 'traverse', 'visitNode',
  'visitStructureNodeStart', 'visitStructureNodeEnd', 'visitAnimateNode',
  'visitEllipseNode', 'visitImageNode', 'visitLineNode', 'visitPathNode',
  'visitPolygonNode', 'visitPolylineNode', 'visitRectNode', 'visitTextNode',
  'visitTspanNode', 'visitUseNode', 'visitVideoNode',
  'visitDocumentNodeStart', 'visitDocumentNodeEnd', 'visitGroupNodeStart',
  'visitGroupNodeEnd', 'visitDefsNodeStart', 'visitDefsNodeEnd',
  'visitSwitchNodeStart', 'visitSwitchNodeEnd', 'visitMaskNodeStart',
  'visitMaskNodeEnd', 'visitSymbolNodeStart', 'visitSymbolNodeEnd',
  'visitMarkerNodeStart', 'visitMarkerNodeEnd', 'visitPatternNodeStart',
  'visitPatternNodeEnd', 'visitFilterNodeStart', 'visitFilterNodeEnd',
  'visitFeFilterPrimitiveNodeStart', 'visitFeFilterPrimitiveNodeEnd'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgVisitor::~QSvgVisitor()': the destructor: Python never removes
    a C++ QSvgVisitor.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSvgVisitor is created at the first use, not by
    'QSvgVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgVisitor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgVisitor'

  #  A C++ QSvgVisitor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgVisitor'

  #  The functions Qt calls itself that QSvgVisitor is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'traverse': (
          ('_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgStructureNode'),
           )),
          ('_ZN11QSvgVisitor8traverseEPK8QSvgNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgNode'),
           )),
      ),
      'visitNode': (
          ('_ZN11QSvgVisitor9visitNodeEPK8QSvgNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgNode'),
           )),
      ),
      'visitStructureNodeStart': (
          ('_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStructureNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgStructureNode'),
           )),
      ),
      'visitStructureNodeEnd': (
          ('_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStructureNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgStructureNode'),
           )),
      ),
      'visitAnimateNode': (
          ('_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgAnimateNode'),
           )),
      ),
      'visitEllipseNode': (
          ('_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgEllipse'),
           )),
      ),
      'visitImageNode': (
          ('_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgImage'),
           )),
      ),
      'visitLineNode': (
          ('_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgLine'),
           )),
      ),
      'visitPathNode': (
          ('_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgPath'),
           )),
      ),
      'visitPolygonNode': (
          ('_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgPolygon'),
           )),
      ),
      'visitPolylineNode': (
          ('_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgPolyline'),
           )),
      ),
      'visitRectNode': (
          ('_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgRect'),
           )),
      ),
      'visitTextNode': (
          ('_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgText'),
           )),
      ),
      'visitTspanNode': (
          ('_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgTspan'),
           )),
      ),
      'visitUseNode': (
          ('_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgUse'),
           )),
      ),
      'visitVideoNode': (
          ('_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgVideo'),
           )),
      ),
      'visitDocumentNodeStart': (
          ('_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocument',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgDocument'),
           )),
      ),
      'visitDocumentNodeEnd': (
          ('_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocument',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgDocument'),
           )),
      ),
      'visitGroupNodeStart': (
          ('_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgG'),
           )),
      ),
      'visitGroupNodeEnd': (
          ('_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgG'),
           )),
      ),
      'visitDefsNodeStart': (
          ('_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgDefs'),
           )),
      ),
      'visitDefsNodeEnd': (
          ('_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgDefs'),
           )),
      ),
      'visitSwitchNodeStart': (
          ('_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgSwitch'),
           )),
      ),
      'visitSwitchNodeEnd': (
          ('_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgSwitch'),
           )),
      ),
      'visitMaskNodeStart': (
          ('_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgMask'),
           )),
      ),
      'visitMaskNodeEnd': (
          ('_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgMask'),
           )),
      ),
      'visitSymbolNodeStart': (
          ('_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgSymbol'),
           )),
      ),
      'visitSymbolNodeEnd': (
          ('_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgSymbol'),
           )),
      ),
      'visitMarkerNodeStart': (
          ('_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgMarker'),
           )),
      ),
      'visitMarkerNodeEnd': (
          ('_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgMarker'),
           )),
      ),
      'visitPatternNodeStart': (
          ('_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPattern',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgPattern'),
           )),
      ),
      'visitPatternNodeEnd': (
          ('_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgPattern'),
           )),
      ),
      'visitFilterNodeStart': (
          ('_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterContainer',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgFilterContainer'),
           )),
      ),
      'visitFilterNodeEnd': (
          ('_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterContainer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgFilterContainer'),
           )),
      ),
      'visitFeFilterPrimitiveNodeStart': (
          ('_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21QSvgFeFil'
           'terPrimitive',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSvg:QSvgFeFilterPrimitive'),
           )),
      ),
      'visitFeFilterPrimitiveNodeEnd': (
          ('_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QSvgFeFilte'
           'rPrimitive',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgFeFilterPrimitive'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSvgVisitor::QSvgVisitor()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#QSvgVisitor
    """
    #  QSvgVisitor::QSvgVisitor()
    self._noteCreation(QSvgVisitor, lambda: Rituals.call(
        'ritual_ZN11QSvgVisitorC1Ev',
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

  @overload(QSvgStructureNode)
  @overload(NoneType)
  def traverse(self, node: Optional[QSvgStructureNode]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::traverse(const QSvgStructureNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#traverse

    Parameters
    ----------

    node : Optional[QSvgStructureNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::traverse(const QSvgStructureNode *node)
    ritual = 'ritual_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgNode)
  def traverse(self, node: Optional[QSvgNode]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::traverse(const QSvgNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#traverse

    Parameters
    ----------

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::traverse(const QSvgNode *node)
    ritual = 'ritual_ZN11QSvgVisitor8traverseEPK8QSvgNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor8traverseEPK8QSvgNode'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgNode)
  @overload(NoneType)
  def visitNode(self, a0: Optional[QSvgNode]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitNode(const QSvgNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitNode

    Parameters
    ----------

    a0 : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitNode(const QSvgNode *a0)
    ritual = 'ritual_ZN11QSvgVisitor9visitNodeEPK8QSvgNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor9visitNodeEPK8QSvgNode'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgStructureNode)
  @overload(NoneType)
  def visitStructureNodeStart(
      self,
      node: Optional[QSvgStructureNode],
  ) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitStructureNodeStart(const
    QSvgStructureNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitStructureNodeStart

    Parameters
    ----------

    node : Optional[QSvgStructureNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitStructureNodeStart(const QSvgStructureNode
    #      *node)
    ritual = (
        'ritual_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStructureN'
        'ode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStru'
          'ctureNode')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgStructureNode)
  @overload(NoneType)
  def visitStructureNodeEnd(self, a0: Optional[QSvgStructureNode]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitStructureNodeEnd(const
    QSvgStructureNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitStructureNodeEnd

    Parameters
    ----------

    a0 : Optional[QSvgStructureNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitStructureNodeEnd(const QSvgStructureNode *a0)
    ritual = (
        'ritual_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStructureNod'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStruct'
          'ureNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgAnimateNode)
  @overload(NoneType)
  def visitAnimateNode(self, node: Optional[QSvgAnimateNode]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitAnimateNode(const QSvgAnimateNode
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitAnimateNode

    Parameters
    ----------

    node : Optional[QSvgAnimateNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitAnimateNode(const QSvgAnimateNode *node)
    ritual = 'ritual_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgEllipse)
  @overload(NoneType)
  def visitEllipseNode(self, node: Optional[QSvgEllipse]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitEllipseNode(const QSvgEllipse *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitEllipseNode

    Parameters
    ----------

    node : Optional[QSvgEllipse]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitEllipseNode(const QSvgEllipse *node)
    ritual = 'ritual_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgImage)
  @overload(NoneType)
  def visitImageNode(self, node: Optional[QSvgImage]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitImageNode(const QSvgImage *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitImageNode

    Parameters
    ----------

    node : Optional[QSvgImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitImageNode(const QSvgImage *node)
    ritual = 'ritual_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgLine)
  @overload(NoneType)
  def visitLineNode(self, node: Optional[QSvgLine]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitLineNode(const QSvgLine *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitLineNode

    Parameters
    ----------

    node : Optional[QSvgLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitLineNode(const QSvgLine *node)
    ritual = 'ritual_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgPath)
  @overload(NoneType)
  def visitPathNode(self, node: Optional[QSvgPath]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitPathNode(const QSvgPath *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitPathNode

    Parameters
    ----------

    node : Optional[QSvgPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitPathNode(const QSvgPath *node)
    ritual = 'ritual_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgPolygon)
  @overload(NoneType)
  def visitPolygonNode(self, node: Optional[QSvgPolygon]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitPolygonNode(const QSvgPolygon *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitPolygonNode

    Parameters
    ----------

    node : Optional[QSvgPolygon]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitPolygonNode(const QSvgPolygon *node)
    ritual = 'ritual_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgPolyline)
  @overload(NoneType)
  def visitPolylineNode(self, node: Optional[QSvgPolyline]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitPolylineNode(const QSvgPolyline
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitPolylineNode

    Parameters
    ----------

    node : Optional[QSvgPolyline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitPolylineNode(const QSvgPolyline *node)
    ritual = 'ritual_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgRect)
  @overload(NoneType)
  def visitRectNode(self, node: Optional[QSvgRect]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitRectNode(const QSvgRect *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitRectNode

    Parameters
    ----------

    node : Optional[QSvgRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitRectNode(const QSvgRect *node)
    ritual = 'ritual_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgText)
  @overload(NoneType)
  def visitTextNode(self, node: Optional[QSvgText]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitTextNode(const QSvgText *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitTextNode

    Parameters
    ----------

    node : Optional[QSvgText]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitTextNode(const QSvgText *node)
    ritual = 'ritual_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgTspan)
  @overload(NoneType)
  def visitTspanNode(self, node: Optional[QSvgTspan]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitTspanNode(const QSvgTspan *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitTspanNode

    Parameters
    ----------

    node : Optional[QSvgTspan]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitTspanNode(const QSvgTspan *node)
    ritual = 'ritual_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgUse)
  @overload(NoneType)
  def visitUseNode(self, node: Optional[QSvgUse]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitUseNode(const QSvgUse *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitUseNode

    Parameters
    ----------

    node : Optional[QSvgUse]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitUseNode(const QSvgUse *node)
    ritual = 'ritual_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgVideo)
  @overload(NoneType)
  def visitVideoNode(self, node: Optional[QSvgVideo]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitVideoNode(const QSvgVideo *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitVideoNode

    Parameters
    ----------

    node : Optional[QSvgVideo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitVideoNode(const QSvgVideo *node)
    ritual = 'ritual_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgDocument)
  @overload(NoneType)
  def visitDocumentNodeStart(self, node: Optional[QSvgDocument]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitDocumentNodeStart(const QSvgDocument
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitDocumentNodeStart

    Parameters
    ----------

    node : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitDocumentNodeStart(const QSvgDocument *node)
    ritual = (
        'ritual_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocument')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocum'
          'ent')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgDocument)
  @overload(NoneType)
  def visitDocumentNodeEnd(self, node: Optional[QSvgDocument]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitDocumentNodeEnd(const QSvgDocument
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitDocumentNodeEnd

    Parameters
    ----------

    node : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitDocumentNodeEnd(const QSvgDocument *node)
    ritual = 'ritual_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocument'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocumen'
          't')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgG)
  @overload(NoneType)
  def visitGroupNodeStart(self, node: Optional[QSvgG]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitGroupNodeStart(const QSvgG *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitGroupNodeStart

    Parameters
    ----------

    node : Optional[QSvgG]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitGroupNodeStart(const QSvgG *node)
    ritual = 'ritual_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG'
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgG)
  @overload(NoneType)
  def visitGroupNodeEnd(self, node: Optional[QSvgG]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitGroupNodeEnd(const QSvgG *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitGroupNodeEnd

    Parameters
    ----------

    node : Optional[QSvgG]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitGroupNodeEnd(const QSvgG *node)
    ritual = 'ritual_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgDefs)
  @overload(NoneType)
  def visitDefsNodeStart(self, node: Optional[QSvgDefs]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitDefsNodeStart(const QSvgDefs *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitDefsNodeStart

    Parameters
    ----------

    node : Optional[QSvgDefs]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitDefsNodeStart(const QSvgDefs *node)
    ritual = 'ritual_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs'
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgDefs)
  @overload(NoneType)
  def visitDefsNodeEnd(self, node: Optional[QSvgDefs]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitDefsNodeEnd(const QSvgDefs *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitDefsNodeEnd

    Parameters
    ----------

    node : Optional[QSvgDefs]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitDefsNodeEnd(const QSvgDefs *node)
    ritual = 'ritual_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgSwitch)
  @overload(NoneType)
  def visitSwitchNodeStart(self, node: Optional[QSvgSwitch]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitSwitchNodeStart(const QSvgSwitch
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitSwitchNodeStart

    Parameters
    ----------

    node : Optional[QSvgSwitch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitSwitchNodeStart(const QSvgSwitch *node)
    ritual = 'ritual_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgSwitch)
  @overload(NoneType)
  def visitSwitchNodeEnd(self, node: Optional[QSvgSwitch]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitSwitchNodeEnd(const QSvgSwitch
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitSwitchNodeEnd

    Parameters
    ----------

    node : Optional[QSvgSwitch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitSwitchNodeEnd(const QSvgSwitch *node)
    ritual = 'ritual_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgMask)
  @overload(NoneType)
  def visitMaskNodeStart(self, node: Optional[QSvgMask]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitMaskNodeStart(const QSvgMask *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitMaskNodeStart

    Parameters
    ----------

    node : Optional[QSvgMask]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitMaskNodeStart(const QSvgMask *node)
    ritual = 'ritual_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask'
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgMask)
  @overload(NoneType)
  def visitMaskNodeEnd(self, node: Optional[QSvgMask]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitMaskNodeEnd(const QSvgMask *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgvisitor.html#visitMaskNodeEnd

    Parameters
    ----------

    node : Optional[QSvgMask]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitMaskNodeEnd(const QSvgMask *node)
    ritual = 'ritual_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask'
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgSymbol)
  @overload(NoneType)
  def visitSymbolNodeStart(self, node: Optional[QSvgSymbol]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitSymbolNodeStart(const QSvgSymbol
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitSymbolNodeStart

    Parameters
    ----------

    node : Optional[QSvgSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitSymbolNodeStart(const QSvgSymbol *node)
    ritual = 'ritual_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgSymbol)
  @overload(NoneType)
  def visitSymbolNodeEnd(self, node: Optional[QSvgSymbol]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitSymbolNodeEnd(const QSvgSymbol
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitSymbolNodeEnd

    Parameters
    ----------

    node : Optional[QSvgSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitSymbolNodeEnd(const QSvgSymbol *node)
    ritual = 'ritual_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgMarker)
  @overload(NoneType)
  def visitMarkerNodeStart(self, a0: Optional[QSvgMarker]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitMarkerNodeStart(const QSvgMarker
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitMarkerNodeStart

    Parameters
    ----------

    a0 : Optional[QSvgMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitMarkerNodeStart(const QSvgMarker *a0)
    ritual = 'ritual_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgMarker)
  @overload(NoneType)
  def visitMarkerNodeEnd(self, a0: Optional[QSvgMarker]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitMarkerNodeEnd(const QSvgMarker *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitMarkerNodeEnd

    Parameters
    ----------

    a0 : Optional[QSvgMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitMarkerNodeEnd(const QSvgMarker *a0)
    ritual = 'ritual_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgPattern)
  @overload(NoneType)
  def visitPatternNodeStart(self, a0: Optional[QSvgPattern]) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitPatternNodeStart(const QSvgPattern
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitPatternNodeStart

    Parameters
    ----------

    a0 : Optional[QSvgPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitPatternNodeStart(const QSvgPattern *a0)
    ritual = 'ritual_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPattern'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPatter'
          'n')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgPattern)
  @overload(NoneType)
  def visitPatternNodeEnd(self, a0: Optional[QSvgPattern]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitPatternNodeEnd(const QSvgPattern
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitPatternNodeEnd

    Parameters
    ----------

    a0 : Optional[QSvgPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitPatternNodeEnd(const QSvgPattern *a0)
    ritual = 'ritual_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSvgFilterContainer)
  @overload(NoneType)
  def visitFilterNodeStart(
      self,
      node: Optional[QSvgFilterContainer],
  ) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitFilterNodeStart(const
    QSvgFilterContainer *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitFilterNodeStart

    Parameters
    ----------

    node : Optional[QSvgFilterContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitFilterNodeStart(const QSvgFilterContainer
    #      *node)
    ritual = (
        'ritual_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterContain'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterC'
          'ontainer')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgFilterContainer)
  @overload(NoneType)
  def visitFilterNodeEnd(self, node: Optional[QSvgFilterContainer]) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitFilterNodeEnd(const
    QSvgFilterContainer *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitFilterNodeEnd

    Parameters
    ----------

    node : Optional[QSvgFilterContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitFilterNodeEnd(const QSvgFilterContainer *node)
    ritual = (
        'ritual_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterContainer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterCon'
          'tainer')
    self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgFeFilterPrimitive)
  @overload(NoneType)
  def visitFeFilterPrimitiveNodeStart(
      self,
      node: Optional[QSvgFeFilterPrimitive],
  ) -> bool:
    """
    Calls Qt's 'bool QSvgVisitor::visitFeFilterPrimitiveNodeStart(const
    QSvgFeFilterPrimitive *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitFeFilterPrimitiveNodeStart

    Parameters
    ----------

    node : Optional[QSvgFeFilterPrimitive]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgVisitor::visitFeFilterPrimitiveNodeStart(const
    #      QSvgFeFilterPrimitive *node)
    ritual = (
        'ritual_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21QSvgFe'
        'FilterPrimitive')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21'
          'QSvgFeFilterPrimitive')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(QSvgFeFilterPrimitive)
  @overload(NoneType)
  def visitFeFilterPrimitiveNodeEnd(
      self,
      node: Optional[QSvgFeFilterPrimitive],
  ) -> None:
    """
    Calls Qt's 'void QSvgVisitor::visitFeFilterPrimitiveNodeEnd(const
    QSvgFeFilterPrimitive *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgvisitor.html#visitFeFilterPrimitiveNodeEnd

    Parameters
    ----------

    node : Optional[QSvgFeFilterPrimitive]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgVisitor::visitFeFilterPrimitiveNodeEnd(const
    #      QSvgFeFilterPrimitive *node)
    ritual = (
        'ritual_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QSvgFeFi'
        'lterPrimitive')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QS'
          'vgFeFilterPrimitive')
    self.uglySide.call(ritual, self._addressOf(node))
