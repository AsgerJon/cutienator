"""
QSvgNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgnode_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QRectF
  from ..QtGui import QImage, QPainter
  from . import QSvgDocument, QSvgExtraStates
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgDocument = WAIT['QSvgDocument']
  QSvgExtraStates = WAIT['QSvgExtraStates']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgNode: a plain Python object standing in front of
  one C++ QSvgNode.

  What exists
  -----------

  Every function of Qt's QSvgNode that has a ritual and that Python can call
  so far, 48 names in all: 'separateFillStroke', 'applyMaskToBuffer',
  'applyBufferToCanvas', 'parent', 'isDescendantOf', 'styleProperty',
  'document', 'type', 'typeName', 'bounds', 'setRequiredFeatures',
  'requiredFeatures', 'setRequiredExtensions', 'requiredExtensions',
  'setRequiredLanguages', 'requiredLanguages', 'setRequiredFormats',
  'requiredFormats', 'setRequiredFonts', 'requiredFonts', 'setVisible',
  'isVisible', 'setDisplayMode', 'displayMode', 'nodeId', 'setNodeId',
  'xmlClass', 'setXmlClass', 'maskId', 'setMaskId', 'hasMask', 'filterId',
  'setFilterId', 'hasFilter', 'markerStartId', 'setMarkerStartId',
  'hasMarkerStart', 'markerMidId', 'setMarkerMidId', 'hasMarkerMid',
  'markerEndId', 'setMarkerEndId', 'hasMarkerEnd', 'hasAnyMarker',
  'requiresGroupRendering', 'filterRegion', 'strokeWidth', 'initPainter'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgNode::~QSvgNode()': the destructor: Python never removes a C++
    QSvgNode.
  - Qt's 'void QSvgNode::draw(QPainter *p, QSvgExtraStates &states)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::fillThenStroke(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'QImage QSvgNode::drawIntoBuffer(QPainter *p, QSvgExtraStates
    &states, const QRect &boundsRect)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSvgNode::drawWithMask(QPainter *p, QSvgExtraStates &states,
    const QImage &mask, const QRect &boundsRect)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSvgNode::applyStyle(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::applyStyleRecursive(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::revertStyle(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::revertStyleRecursive(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::applyAnimatedStyle(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgNode::revertAnimatedStyle(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgNode::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgNode::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgNode::bounds(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgNode::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRectF QSvgNode::decoratedBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgNode::shouldDrawNode(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QSvgStaticStyle &QSvgNode::style() const': gives a type
    Python has no way to take yet.
  - Qt's 'QRectF QSvgNode::boundsOnStroke(QPainter *p, const QPainterPath
    &path, qreal width, BoundsMode mode)': names the enum
    'QSvgNode::BoundsMode', whose class cannot be named here.

  What has no ritual
  ------------------

  4 of the 72 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QSvgNode is created at the first use, not by 'QSvgNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgNode.
  - Each name of Qt's QSvgNode that has no cute function yet, '__init__',
    'appendStyleProperty', 'applyAnimatedStyle', 'applyStyle',
    'applyStyleRecursive', 'boundsOnStroke', 'decoratedBounds',
    'decoratedInternalBounds', 'draw', 'drawCommand', 'drawIntoBuffer',
    'drawWithMask', 'fillThenStroke', 'internalBounds', 'internalFastBounds',
    'revertAnimatedStyle', 'revertStyle', 'revertStyleRecursive',
    'shouldDrawNode', 'style', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSvgNode, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class DisplayMode(CuteNum):
    """
    The enum 'QSvgNode::DisplayMode' of Qt, with the 18 names Qt gives in it.
    """

    InlineMode = Kee[int](0)
    BlockMode = Kee[int](1)
    ListItemMode = Kee[int](2)
    RunInMode = Kee[int](3)
    CompactMode = Kee[int](4)
    MarkerMode = Kee[int](5)
    TableMode = Kee[int](6)
    InlineTableMode = Kee[int](7)
    TableRowGroupMode = Kee[int](8)
    TableHeaderGroupMode = Kee[int](9)
    TableFooterGroupMode = Kee[int](10)
    TableRowMode = Kee[int](11)
    TableColumnGroupMode = Kee[int](12)
    TableColumnMode = Kee[int](13)
    TableCellMode = Kee[int](14)
    TableCaptionMode = Kee[int](15)
    NoneMode = Kee[int](16)
    InheritMode = Kee[int](17)

  class Type(CuteNum):
    """The enum 'QSvgNode::Type' of Qt, with the 34 names Qt gives in it."""

    Doc = Kee[int](0)
    Group = Kee[int](1)
    Defs = Kee[int](2)
    Switch = Kee[int](3)
    AnimateColor = Kee[int](4)
    AnimateTransform = Kee[int](5)
    Circle = Kee[int](6)
    Ellipse = Kee[int](7)
    Image = Kee[int](8)
    Line = Kee[int](9)
    Path = Kee[int](10)
    Polygon = Kee[int](11)
    Polyline = Kee[int](12)
    Rect = Kee[int](13)
    Text = Kee[int](14)
    Textarea = Kee[int](15)
    Tspan = Kee[int](16)
    Use = Kee[int](17)
    Video = Kee[int](18)
    Mask = Kee[int](19)
    Symbol = Kee[int](20)
    Marker = Kee[int](21)
    Pattern = Kee[int](22)
    Filter = Kee[int](23)
    FeMerge = Kee[int](24)
    FeMergenode = Kee[int](25)
    FeColormatrix = Kee[int](26)
    FeGaussianblur = Kee[int](27)
    FeOffset = Kee[int](28)
    FeComposite = Kee[int](29)
    FeFlood = Kee[int](30)
    FeBlend = Kee[int](31)
    FeUnsupported = Kee[int](32)
    Font = Kee[int](33)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPainter)
  @overload(NoneType)
  def strokeWidth(p: Optional[QPainter]) -> float:
    """
    Calls Qt's 'qreal QSvgNode::strokeWidth(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#strokeWidth

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QSvgNode::strokeWidth(QPainter *p)
    return Rituals.call(
        'ritual_ZN8QSvgNode11strokeWidthEP8QPainter',
        CuteMixin._addressOf(p),
    )

  @staticmethod
  @overload(QPainter)
  @overload(NoneType)
  def initPainter(p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSvgNode::initPainter(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#initPainter

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgNode::initPainter(QPainter *p)
    Rituals.call(
        'ritual_ZN8QSvgNode11initPainterEP8QPainter',
        CuteMixin._addressOf(p),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgNode'

  #  A C++ QSvgNode Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgNode'

  #  The functions Qt calls itself that QSvgNode is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'drawCommand': (
          'void QSvgNode::drawCommand(QPainter *, QSvgExtraStates &)',
      ),
      'internalFastBounds': (
          'QRectF QSvgNode::internalFastBounds(QPainter *, QSvgExtraStates '
          '&) const',
      ),
      'internalBounds': (
          'QRectF QSvgNode::internalBounds(QPainter *, QSvgExtraStates &) '
          'const',
      ),
      'decoratedInternalBounds': (
          'QRectF QSvgNode::decoratedInternalBounds(QPainter *, '
          'QSvgExtraStates &) const',
      ),
      'decoratedBounds': (
          'QRectF QSvgNode::decoratedBounds(QPainter *, QSvgExtraStates &) '
          'const',
      ),
      'shouldDrawNode': (
          'bool QSvgNode::shouldDrawNode(QPainter *, QSvgExtraStates &) '
          'const',
      ),
  }

  #  The functions Qt calls itself that QSvgNode is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'separateFillStroke': (
          ('_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraState'
           's',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtSvg:QSvgExtraStates'),
           )),
      ),
      'type': (
          ('_ZNK8QSvgNode4typeEv',
           ('int', 'enum', 'QtSvg:QSvgNode.Type'),
           ()),
      ),
      'requiresGroupRendering': (
          ('_ZNK8QSvgNode22requiresGroupRenderingEv',
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

  @overload(QPainter, QSvgExtraStates)
  @overload(NoneType, QSvgExtraStates)
  def separateFillStroke(
      self,
      a0: Optional[QPainter],
      a1: QSvgExtraStates,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgNode::separateFillStroke(const QPainter *a0, const
    QSvgExtraStates &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgNode::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraSt'
        'ates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgE'
          'xtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def parent(self) -> Optional[QSvgNode]:
    """
    Calls Qt's 'QSvgNode *QSvgNode::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#parent

    Returns
    -------

    Optional[QSvgNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgNode *QSvgNode::parent() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode6parentEv')
    return QSvgNode._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def isDescendantOf(self, parent: Optional[QSvgNode]) -> bool:
    """
    Calls Qt's 'bool QSvgNode::isDescendantOf(const QSvgNode *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#isDescendantOf

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgNode::isDescendantOf(const QSvgNode *parent) const
    return self.uglySide.call(
        'ritual_ZNK8QSvgNode14isDescendantOfEPKS_', self._addressOf(parent),
    )

  @overload(QSvgStyleProperty.Type)
  def styleProperty(
      self,
      type: QSvgStyleProperty.Type,
  ) -> Optional[QSvgStyleProperty]:
    """
    Calls Qt's 'QSvgStyleProperty
    *QSvgNode::styleProperty(QSvgStyleProperty::Type type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#styleProperty

    Parameters
    ----------

    type : QSvgStyleProperty.Type
      Passed on as its number.

    Returns
    -------

    Optional[QSvgStyleProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgStyleProperty *QSvgNode::styleProperty(QSvgStyleProperty::Type
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK8QSvgNode13stylePropertyEN17QSvgStyleProperty4TypeE',
        type.value,
    )
    return QSvgStyleProperty._cuteAt(address)

  def document(self) -> Optional[QSvgDocument]:
    """
    Calls Qt's 'QSvgDocument *QSvgNode::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#document

    Returns
    -------

    Optional[QSvgDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgDocument *QSvgNode::document() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode8documentEv')
    from . import QSvgDocument
    return QSvgDocument._cuteAt(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QSvgNode::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSvgNode::type() const
    return QSvgNode.Type(self.uglySide.call('ritual_ZNK8QSvgNode4typeEv'))

  def typeName(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QSvgNode::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#typeName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QSvgNode::typeName() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode8typeNameEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @overload(QSvgDocument)
  @overload(NoneType)
  def bounds(self, doc: Optional[QSvgDocument]) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgNode::bounds(const QSvgDocument *doc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#bounds

    Parameters
    ----------

    doc : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgNode::bounds(const QSvgDocument *doc) const
    address = self.uglySide.call(
        'ritual_ZNK8QSvgNode6boundsEPK12QSvgDocument', self._addressOf(doc),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def requiredFeatures(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QSvgNode::requiredFeatures() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#requiredFeatures

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QSvgNode::requiredFeatures() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode16requiredFeaturesEv')
    return QStringList._cuteOwning(address)

  def requiredExtensions(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QSvgNode::requiredExtensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#requiredExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QSvgNode::requiredExtensions() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode18requiredExtensionsEv')
    return QStringList._cuteOwning(address)

  def requiredLanguages(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QSvgNode::requiredLanguages() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#requiredLanguages

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QSvgNode::requiredLanguages() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode17requiredLanguagesEv')
    return QStringList._cuteOwning(address)

  def requiredFormats(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QSvgNode::requiredFormats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#requiredFormats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QSvgNode::requiredFormats() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode15requiredFormatsEv')
    return QStringList._cuteOwning(address)

  def requiredFonts(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QSvgNode::requiredFonts() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#requiredFonts

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QSvgNode::requiredFonts() const
    address = self.uglySide.call('ritual_ZNK8QSvgNode13requiredFontsEv')
    return QStringList._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#isVisible
    """
    #  bool QSvgNode::isVisible() const
    return self.uglySide.call('ritual_ZNK8QSvgNode9isVisibleEv')

  def displayMode(self) -> DisplayMode:
    """
    Calls Qt's 'DisplayMode QSvgNode::displayMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#displayMode

    Returns
    -------

    DisplayMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DisplayMode(number)'
      gives.
    """
    #  DisplayMode QSvgNode::displayMode() const
    return QSvgNode.DisplayMode(self.uglySide.call(
        'ritual_ZNK8QSvgNode11displayModeEv',
    ))

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::nodeId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode6nodeIdEv')

  def xmlClass(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::xmlClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#xmlClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::xmlClass() const
    return self.uglySide.call('ritual_ZNK8QSvgNode8xmlClassEv')

  def maskId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::maskId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#maskId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::maskId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode6maskIdEv')

  def hasMask(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasMask
    """
    #  bool QSvgNode::hasMask() const
    return self.uglySide.call('ritual_ZNK8QSvgNode7hasMaskEv')

  def filterId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::filterId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#filterId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::filterId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode8filterIdEv')

  def hasFilter(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasFilter
    """
    #  bool QSvgNode::hasFilter() const
    return self.uglySide.call('ritual_ZNK8QSvgNode9hasFilterEv')

  def markerStartId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::markerStartId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#markerStartId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::markerStartId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode13markerStartIdEv')

  def hasMarkerStart(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasMarkerStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasMarkerStart
    """
    #  bool QSvgNode::hasMarkerStart() const
    return self.uglySide.call('ritual_ZNK8QSvgNode14hasMarkerStartEv')

  def markerMidId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::markerMidId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#markerMidId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::markerMidId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode11markerMidIdEv')

  def hasMarkerMid(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasMarkerMid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasMarkerMid
    """
    #  bool QSvgNode::hasMarkerMid() const
    return self.uglySide.call('ritual_ZNK8QSvgNode12hasMarkerMidEv')

  def markerEndId(self) -> str:
    """
    Calls Qt's 'QString QSvgNode::markerEndId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#markerEndId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgNode::markerEndId() const
    return self.uglySide.call('ritual_ZNK8QSvgNode11markerEndIdEv')

  def hasMarkerEnd(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasMarkerEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasMarkerEnd
    """
    #  bool QSvgNode::hasMarkerEnd() const
    return self.uglySide.call('ritual_ZNK8QSvgNode12hasMarkerEndEv')

  def hasAnyMarker(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::hasAnyMarker() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#hasAnyMarker
    """
    #  bool QSvgNode::hasAnyMarker() const
    return self.uglySide.call('ritual_ZNK8QSvgNode12hasAnyMarkerEv')

  def requiresGroupRendering(self) -> bool:
    """
    Calls Qt's 'bool QSvgNode::requiresGroupRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgnode.html#requiresGroupRendering
    """
    #  bool QSvgNode::requiresGroupRendering() const
    ritual = 'ritual_ZNK8QSvgNode22requiresGroupRenderingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgNode22requiresGroupRenderingEv'
    return self.uglySide.call(ritual)

  @overload(QSvgDocument, QRectF)
  @overload(NoneType, QRectF)
  def filterRegion(
      self,
      doc: Optional[QSvgDocument],
      bounds: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgNode::filterRegion(const QSvgDocument *doc, QRectF
    bounds) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#filterRegion

    Parameters
    ----------

    doc : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgNode::filterRegion(const QSvgDocument *doc, QRectF bounds)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8QSvgNode12filterRegionEPK12QSvgDocument6QRectF',
        self._addressOf(doc), self._valueOf(bounds),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setRequiredFeatures(self, lst: QStringList) -> None:
    """
    Calls Qt's 'void QSvgNode::setRequiredFeatures(const QStringList &lst)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setRequiredFeatures

    Parameters
    ----------

    lst : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgNode::setRequiredFeatures(const QStringList &lst)
    self.uglySide.call(
        'ritual_ZN8QSvgNode19setRequiredFeaturesERK5QListI7QStringE',
        self._valueOf(lst),
    )

  @overload(QStringList)
  def setRequiredExtensions(self, lst: QStringList) -> None:
    """
    Calls Qt's 'void QSvgNode::setRequiredExtensions(const QStringList
    &lst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgnode.html#setRequiredExtensions

    Parameters
    ----------

    lst : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgNode::setRequiredExtensions(const QStringList &lst)
    self.uglySide.call(
        'ritual_ZN8QSvgNode21setRequiredExtensionsERK5QListI7QStringE',
        self._valueOf(lst),
    )

  @overload(QStringList)
  def setRequiredLanguages(self, lst: QStringList) -> None:
    """
    Calls Qt's 'void QSvgNode::setRequiredLanguages(const QStringList &lst)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setRequiredLanguages

    Parameters
    ----------

    lst : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgNode::setRequiredLanguages(const QStringList &lst)
    self.uglySide.call(
        'ritual_ZN8QSvgNode20setRequiredLanguagesERK5QListI7QStringE',
        self._valueOf(lst),
    )

  @overload(QStringList)
  def setRequiredFormats(self, lst: QStringList) -> None:
    """
    Calls Qt's 'void QSvgNode::setRequiredFormats(const QStringList &lst)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setRequiredFormats

    Parameters
    ----------

    lst : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgNode::setRequiredFormats(const QStringList &lst)
    self.uglySide.call(
        'ritual_ZN8QSvgNode18setRequiredFormatsERK5QListI7QStringE',
        self._valueOf(lst),
    )

  @overload(QStringList)
  def setRequiredFonts(self, lst: QStringList) -> None:
    """
    Calls Qt's 'void QSvgNode::setRequiredFonts(const QStringList &lst)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setRequiredFonts

    Parameters
    ----------

    lst : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgNode::setRequiredFonts(const QStringList &lst)
    self.uglySide.call(
        'ritual_ZN8QSvgNode16setRequiredFontsERK5QListI7QStringE',
        self._valueOf(lst),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QSvgNode::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QSvgNode::setVisible(bool visible)
    self.uglySide.call('ritual_ZN8QSvgNode10setVisibleEb', visible)

  @overload(DisplayMode)
  def setDisplayMode(self, display: DisplayMode) -> None:
    """
    Calls Qt's 'void QSvgNode::setDisplayMode(DisplayMode display)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setDisplayMode

    Parameters
    ----------

    display : DisplayMode
      Passed on as its number.
    """
    #  void QSvgNode::setDisplayMode(DisplayMode display)
    self.uglySide.call(
        'ritual_ZN8QSvgNode14setDisplayModeENS_11DisplayModeE',
        display.value,
    )

  @overload(str)
  def setNodeId(self, i: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setNodeId(const QString &i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setNodeId

    Parameters
    ----------

    i : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setNodeId(const QString &i)
    self.uglySide.call('ritual_ZN8QSvgNode9setNodeIdERK7QString', i)

  @overload(str)
  def setXmlClass(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setXmlClass(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setXmlClass

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setXmlClass(const QString &str)
    self.uglySide.call('ritual_ZN8QSvgNode11setXmlClassERK7QString', str)

  @overload(str)
  def setMaskId(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setMaskId(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setMaskId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setMaskId(const QString &str)
    self.uglySide.call('ritual_ZN8QSvgNode9setMaskIdERK7QString', str)

  @overload(str)
  def setFilterId(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setFilterId(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setFilterId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setFilterId(const QString &str)
    self.uglySide.call('ritual_ZN8QSvgNode11setFilterIdERK7QString', str)

  @overload(str)
  def setMarkerStartId(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setMarkerStartId(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setMarkerStartId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setMarkerStartId(const QString &str)
    self.uglySide.call(
        'ritual_ZN8QSvgNode16setMarkerStartIdERK7QString', str,
    )

  @overload(str)
  def setMarkerMidId(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setMarkerMidId(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setMarkerMidId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setMarkerMidId(const QString &str)
    self.uglySide.call('ritual_ZN8QSvgNode14setMarkerMidIdERK7QString', str)

  @overload(str)
  def setMarkerEndId(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgNode::setMarkerEndId(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#setMarkerEndId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgNode::setMarkerEndId(const QString &str)
    self.uglySide.call('ritual_ZN8QSvgNode14setMarkerEndIdERK7QString', str)

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
    Qt's 'QSvgNode::QSvgNode(QSvgNode *parent)': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QSvgNode.__init__' has no cute function yet. Qt's "
        "'QSvgNode::QSvgNode(QSvgNode *parent)': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(QImage, QImage)
  @overload(NoneType, QImage)
  def applyMaskToBuffer(self, proxy: Optional[QImage], mask: QImage) -> None:
    """
    Calls Qt's 'void QSvgNode::applyMaskToBuffer(QImage *proxy, const QImage
    &mask) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#applyMaskToBuffer

    Parameters
    ----------

    proxy : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mask : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSvgNode::applyMaskToBuffer(QImage *proxy, const QImage &mask)
    #      const
    self.uglySide.call(
        'ritual_ZNK8QSvgNode17applyMaskToBufferEP6QImageRKS0_',
        self._addressOf(proxy), self._valueOf(mask),
    )

  @overload(QPainter, QImage)
  @overload(NoneType, QImage)
  def applyBufferToCanvas(
      self,
      p: Optional[QPainter],
      proxy: QImage,
  ) -> None:
    """
    Calls Qt's 'void QSvgNode::applyBufferToCanvas(QPainter *p, const QImage
    &proxy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgnode.html#applyBufferToCanvas

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    proxy : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSvgNode::applyBufferToCanvas(QPainter *p, const QImage &proxy)
    #      const
    self.uglySide.call(
        'ritual_ZNK8QSvgNode19applyBufferToCanvasEP8QPainterRK6QImage',
        self._addressOf(p), self._valueOf(proxy),
    )

  @staticmethod
  def appendStyleProperty(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::appendStyleProperty(QSvgStylePropertyPtr prop)': the
    compiler refuses its ritual as it would be written here: call to deleted
    constructor of 'QSvgStylePropertyPtr' (aka
    'std::unique_ptr<QSvgStyleProperty>').
    """
    raise NotImplementedError(
        "'QSvgNode.appendStyleProperty' has no cute function yet. Qt's "
        "'void QSvgNode::appendStyleProperty(QSvgStylePropertyPtr prop)': "
        "the compiler refuses its ritual as it would be written here: call "
        "to deleted constructor of 'QSvgStylePropertyPtr' (aka "
        "'std::unique_ptr<QSvgStyleProperty>').")

  @staticmethod
  def applyAnimatedStyle(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::applyAnimatedStyle(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.applyAnimatedStyle' has no cute function yet. Qt's 'void "
        "QSvgNode::applyAnimatedStyle(QPainter *p, QSvgExtraStates &states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def applyStyle(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::applyStyle(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.applyStyle' has no cute function yet. Qt's 'void "
        "QSvgNode::applyStyle(QPainter *p, QSvgExtraStates &states) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def applyStyleRecursive(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::applyStyleRecursive(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.applyStyleRecursive' has no cute function yet. Qt's "
        "'void QSvgNode::applyStyleRecursive(QPainter *p, QSvgExtraStates "
        "&states) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def boundsOnStroke(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgNode::boundsOnStroke(QPainter *p, const QPainterPath
    &path, qreal width, BoundsMode mode)': names the enum
    'QSvgNode::BoundsMode', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSvgNode.boundsOnStroke' has no cute function yet. Qt's 'QRectF "
        "QSvgNode::boundsOnStroke(QPainter *p, const QPainterPath &path, "
        "qreal width, BoundsMode mode)': names the enum "
        "'QSvgNode::BoundsMode', whose class cannot be named here.")

  @staticmethod
  def decoratedBounds(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgNode::decoratedBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.decoratedBounds' has no cute function yet. Qt's 'QRectF "
        "QSvgNode::decoratedBounds(QPainter *p, QSvgExtraStates &states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def decoratedInternalBounds(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgNode::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.decoratedInternalBounds' has no cute function yet. Qt's "
        "'QRectF QSvgNode::decoratedInternalBounds(QPainter *p, "
        "QSvgExtraStates &states) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def draw(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::draw(QPainter *p, QSvgExtraStates &states)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.draw' has no cute function yet. Qt's 'void "
        "QSvgNode::draw(QPainter *p, QSvgExtraStates &states)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def drawCommand(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.drawCommand' has no cute function yet. Qt's 'void "
        "QSvgNode::drawCommand(QPainter *p, QSvgExtraStates &states)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def drawIntoBuffer(*__, **_) -> Never:
    """
    Qt's 'QImage QSvgNode::drawIntoBuffer(QPainter *p, QSvgExtraStates
    &states, const QRect &boundsRect)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.drawIntoBuffer' has no cute function yet. Qt's 'QImage "
        "QSvgNode::drawIntoBuffer(QPainter *p, QSvgExtraStates &states, "
        "const QRect &boundsRect)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def drawWithMask(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::drawWithMask(QPainter *p, QSvgExtraStates &states,
    const QImage &mask, const QRect &boundsRect)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.drawWithMask' has no cute function yet. Qt's 'void "
        "QSvgNode::drawWithMask(QPainter *p, QSvgExtraStates &states, const "
        "QImage &mask, const QRect &boundsRect)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def fillThenStroke(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::fillThenStroke(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.fillThenStroke' has no cute function yet. Qt's 'void "
        "QSvgNode::fillThenStroke(QPainter *p, QSvgExtraStates &states)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def internalBounds(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgNode::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.internalBounds' has no cute function yet. Qt's 'QRectF "
        "QSvgNode::internalBounds(QPainter *p, QSvgExtraStates &states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def internalFastBounds(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgNode::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.internalFastBounds' has no cute function yet. Qt's "
        "'QRectF QSvgNode::internalFastBounds(QPainter *p, QSvgExtraStates "
        "&states) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def revertAnimatedStyle(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::revertAnimatedStyle(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.revertAnimatedStyle' has no cute function yet. Qt's "
        "'void QSvgNode::revertAnimatedStyle(QPainter *p, QSvgExtraStates "
        "&states) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def revertStyle(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::revertStyle(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.revertStyle' has no cute function yet. Qt's 'void "
        "QSvgNode::revertStyle(QPainter *p, QSvgExtraStates &states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def revertStyleRecursive(*__, **_) -> Never:
    """
    Qt's 'void QSvgNode::revertStyleRecursive(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.revertStyleRecursive' has no cute function yet. Qt's "
        "'void QSvgNode::revertStyleRecursive(QPainter *p, QSvgExtraStates "
        "&states) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def shouldDrawNode(*__, **_) -> Never:
    """
    Qt's 'bool QSvgNode::shouldDrawNode(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgNode.shouldDrawNode' has no cute function yet. Qt's 'bool "
        "QSvgNode::shouldDrawNode(QPainter *p, QSvgExtraStates &states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def style(*__, **_) -> Never:
    """
    Qt's 'const QSvgStaticStyle &QSvgNode::style() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgNode.style' has no cute function yet. Qt's 'const "
        "QSvgStaticStyle &QSvgNode::style() const': gives a type Python has "
        "no way to take yet.")
