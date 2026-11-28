"""
QSGInternalTextNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsginternaltextnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGInternalTextNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QTextCharFormat
from . import QQuickText, QSGNode, QSGTextNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QColor, QGlyphRun, QImage, QTextDocument, QTextLayout
  from . import QSGGlyphNode, QSGInternalImageNode, QSGInternalRectangleNode
  from . import QSGRenderContext, QSGVisitableNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QImage = WAIT['QImage']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGRenderContext = WAIT['QSGRenderContext']
  QTextDocument = WAIT['QTextDocument']
  QTextLayout = WAIT['QTextLayout']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGInternalTextNode(QSGTextNode):
  """
  The cute side of Qt's QSGInternalTextNode: a plain Python object standing
  in front of one C++ QSGInternalTextNode.

  It is built on the cute 'QSGTextNode', as Qt's QSGInternalTextNode is built
  on Qt's QSGTextNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGInternalTextNode that has a ritual and that
  Python can call so far, 39 names in all: 'setColor', 'color',
  'setTextStyle', 'textStyle', 'setStyleColor', 'styleColor', 'setLinkColor',
  'linkColor', 'setSelectionColor', 'selectionColor',
  'setSelectionTextColor', 'selectionTextColor', 'setRenderTypeQuality',
  'renderTypeQuality', 'setRenderType', 'renderType',
  'containsUnscalableGlyphs', 'setFiltering', 'filtering', 'setViewport',
  'viewport', 'setDevicePixelRatio', 'setCursor', 'clearCursor',
  'addRectangleNode', 'addDecorationNode', 'addImage', 'clear', 'recycle',
  'addGlyphs', 'cursorNode', 'discardUnusedNodes', 'addTextLayout',
  'addTextDocument', 'doAddTextLayout', 'doAddTextDocument',
  'findOrCreateImageNode', 'findOrCreateGlyphNode',
  'findOrCreateRectangleNode'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGInternalTextNode::~QSGInternalTextNode()': the destructor:
    Python never removes a C++ QSGInternalTextNode.
  - Qt's 'std::pair<int, int> QSGInternalTextNode::renderedLineRange()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 45 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSGInternalTextNode is created at the first use, not by
    'QSGInternalTextNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGInternalTextNode.
  - Each name of Qt's QSGInternalTextNode that has no cute function yet,
    'isComplexRichText', 'renderedLineRange', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGInternalTextNode, each a class in here
  #  as in C++.

  class RecycleBin(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGInternalTextNode::RecycleBin: a plain Python
    object standing in front of one C++ QSGInternalTextNode::RecycleBin.

    What exists
    -----------

    Every function of Qt's QSGInternalTextNode::RecycleBin that has a ritual
    and that Python can call so far, 3 names in all: 'takeNextReusableNode',
    'stopReusing', 'peekNextReusableNode'. It can be made from Python, in 1
    way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGInternalTextNode::RecycleBin::~RecycleBin()': the destructor:
      Python never removes a C++ QSGInternalTextNode::RecycleBin.

    What has no ritual
    ------------------

    3 of the 8 functions Qt declares: 2 forbidden; 1 Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ QSGInternalTextNode::RecycleBin is created at the first use,
      not by 'QSGInternalTextNode::RecycleBin(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QSGInternalTextNode::RecycleBin.
    - Each name of Qt's QSGInternalTextNode::RecycleBin that has no cute
      function yet, 'takeNextReusableGlyphNode', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The enums Qt writes inside QSGInternalTextNode::RecycleBin, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class NodeType(CuteNum):
      """
      The enum 'QSGInternalTextNode::RecycleBin::NodeType' of Qt, with the 3
      names Qt gives in it.
      """

      GlyphNode = Kee[int](0)
      RectangleNode = Kee[int](1)
      ImageNode = Kee[int](2)

    #  The classes Qt writes inside QSGInternalTextNode::RecycleBin, each a
    #  class in here as in C++.

    class UnusedNode(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QSGInternalTextNode::RecycleBin::UnusedNode: a
      plain Python object standing in front of one C++
      QSGInternalTextNode::RecycleBin::UnusedNode.

      C++ hands a QSGInternalTextNode::RecycleBin::UnusedNode around as a
      copy, so every C++ QSGInternalTextNode::RecycleBin::UnusedNode behind a
      cute one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QSGInternalTextNode::RecycleBin::UnusedNode yet.
      None can be made from Python: one comes out of a function of another
      class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QSGInternalTextNode::RecycleBin::UnusedNode::~UnusedNode()':
        the destructor: Python removes its C++
        QSGInternalTextNode::RecycleBin::UnusedNode by it, and has no other
        use for it.

      What to expect
      --------------

      - The C++ QSGInternalTextNode::RecycleBin::UnusedNode is created at the
        first use, not by 'QSGInternalTextNode::RecycleBin::UnusedNode(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QSGInternalTextNode::RecycleBin::UnusedNode back
        gives a copy the ritual made for Python, in a new cute
        QSGInternalTextNode::RecycleBin::UnusedNode.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QSGInternalTextNode::RecycleBin::UnusedNode'

      #  Qt's '~QSGInternalTextNode::RecycleBin::UnusedNode()'. Naming it
      #  makes this a value class: Python owns every C++
      #  QSGInternalTextNode::RecycleBin::UnusedNode behind a cute one, and
      #  removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN19QSGInternalTextNode10RecycleBin10UnusedNodeD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGInternalTextNode::RecycleBin'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSGInternalTextNode::RecycleBin::RecycleBin()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsginternaltextnode-recyclebin.html#RecycleBin
      """
      #  QSGInternalTextNode::RecycleBin::RecycleBin()
      self._noteCreation(
          QSGInternalTextNode.RecycleBin, lambda: Rituals.call(
              'ritual_ZN19QSGInternalTextNode10RecycleBinC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(NodeType)
    def takeNextReusableNode(
        self,
        type: NodeType,
    ) -> Optional[QSGVisitableNode]:
      """
      Calls Qt's 'QSGVisitableNode
      *QSGInternalTextNode::RecycleBin::takeNextReusableNode(NodeType type)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsginternaltextnode-recyclebin.html

      Parameters
      ----------

      type : NodeType
        Passed on as its number.

      Returns
      -------

      Optional[QSGVisitableNode]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QSGVisitableNode
      #      *QSGInternalTextNode::RecycleBin::takeNextReusableNode(NodeType
      #      type)
      address = self.uglySide.call(
          'ritual_ZN19QSGInternalTextNode10RecycleBin20takeNextReusableNode'
          'ENS0_8NodeTypeE',
          type.value,
      )
      from . import QSGVisitableNode
      return QSGVisitableNode._cuteAt(address)

    def stopReusing(self) -> None:
      """
      Calls Qt's 'void QSGInternalTextNode::RecycleBin::stopReusing()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsginternaltextnode-recyclebin.html#stopReusing
      """
      #  void QSGInternalTextNode::RecycleBin::stopReusing()
      self.uglySide.call(
          'ritual_ZN19QSGInternalTextNode10RecycleBin11stopReusingEv',
      )

    @overload(NodeType)
    def peekNextReusableNode(self, type: NodeType) -> Optional[UnusedNode]:
      """
      Calls Qt's 'const UnusedNode
      *QSGInternalTextNode::RecycleBin::peekNextReusableNode(NodeType type)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsginternaltextnode-recyclebin.html

      Parameters
      ----------

      type : NodeType
        Passed on as its number.

      Returns
      -------

      Optional[UnusedNode]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  const UnusedNode
      #      *QSGInternalTextNode::RecycleBin::peekNextReusableNode(NodeType
      #      type)
      address = self.uglySide.call(
          'ritual_ZN19QSGInternalTextNode10RecycleBin20peekNextReusableNode'
          'ENS0_8NodeTypeE',
          type.value,
      )
      return QSGInternalTextNode.RecycleBin.UnusedNode._cuteAt(address)

    @staticmethod
    def takeNextReusableGlyphNode(*__, **_) -> Never:
      """
      Qt's 'QSGGlyphNode
      *QSGInternalTextNode::RecycleBin::takeNextReusableGlyphNode(
      QSGTextNode::RenderType renderType)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file: use
      of undeclared identifier 'lcTextRecycle'.
      """
      raise NotImplementedError(
          "'QSGInternalTextNode.RecycleBin.takeNextReusableGlyphNode' has "
          "no cute function yet. Qt's 'QSGGlyphNode "
          "*QSGInternalTextNode::RecycleBin::takeNextReusableGlyphNode(QSGTe"
          "xtNode::RenderType renderType)': Qt's library has no name for "
          "it, and its code in Qt's source does not compile apart from its "
          "file: use of undeclared identifier 'lcTextRecycle'.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGInternalTextNode'

  #  A C++ QSGInternalTextNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGInternalTextNode'

  #  The functions Qt calls itself that QSGInternalTextNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addDecorationNode': (
          ('_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN'
           '15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QColor'),
               ('int', 'enum', 'QtGui:QTextCharFormat.UnderlineStyle'),
               ('address', 'address',
                'QtQuick:QSGInternalTextNode.RecycleBin'),
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

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGInternalTextNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGInternalTextNode::color() const
    ritual = 'ritual_ZNK19QSGInternalTextNode5colorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode5colorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def styleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGInternalTextNode::styleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#styleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGInternalTextNode::styleColor() const
    ritual = 'ritual_ZNK19QSGInternalTextNode10styleColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode10styleColorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def linkColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGInternalTextNode::linkColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#linkColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGInternalTextNode::linkColor() const
    ritual = 'ritual_ZNK19QSGInternalTextNode9linkColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode9linkColorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGInternalTextNode::selectionColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#selectionColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGInternalTextNode::selectionColor() const
    ritual = 'ritual_ZNK19QSGInternalTextNode14selectionColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode14selectionColorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGInternalTextNode::selectionTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#selectionTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGInternalTextNode::selectionTextColor() const
    ritual = 'ritual_ZNK19QSGInternalTextNode18selectionTextColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode18selectionTextColorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def renderTypeQuality(self) -> int:
    """
    Calls Qt's 'int QSGInternalTextNode::renderTypeQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#renderTypeQuality
    """
    #  int QSGInternalTextNode::renderTypeQuality() const
    ritual = 'ritual_ZNK19QSGInternalTextNode17renderTypeQualityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode17renderTypeQualityEv'
    return self.uglySide.call(ritual)

  def renderType(self) -> QSGTextNode.RenderType:
    """
    Calls Qt's 'RenderType QSGInternalTextNode::renderType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#renderType

    Returns
    -------

    QSGTextNode.RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTextNode.RenderType(number)' gives.
    """
    #  RenderType QSGInternalTextNode::renderType() const
    ritual = 'ritual_ZNK19QSGInternalTextNode10renderTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode10renderTypeEv'
    return QSGTextNode.RenderType(self.uglySide.call(ritual))

  def containsUnscalableGlyphs(self) -> bool:
    """
    Calls Qt's 'bool QSGInternalTextNode::containsUnscalableGlyphs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#containsUnscalableGlyphs
    """
    #  bool QSGInternalTextNode::containsUnscalableGlyphs() const
    return self.uglySide.call(
        'ritual_ZNK19QSGInternalTextNode24containsUnscalableGlyphsEv',
    )

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGInternalTextNode::filtering()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGInternalTextNode::filtering() const
    ritual = 'ritual_ZNK19QSGInternalTextNode9filteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode9filteringEv'
    return QSGTexture.Filtering(self.uglySide.call(ritual))

  def viewport(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGInternalTextNode::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#viewport

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGInternalTextNode::viewport() const
    ritual = 'ritual_ZNK19QSGInternalTextNode8viewportEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGInternalTextNode8viewportEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorNode(self) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode *QSGInternalTextNode::cursorNode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#cursorNode

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode *QSGInternalTextNode::cursorNode() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGInternalTextNode10cursorNodeEv',
    )
    from . import QSGInternalRectangleNode
    return QSGInternalRectangleNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setColor(QColor color)
    ritual = 'ritual_ZN19QSGInternalTextNode8setColorE6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode8setColorE6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QSGTextNode.TextStyle)
  def setTextStyle(self, textStyle: QSGTextNode.TextStyle) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setTextStyle(TextStyle textStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setTextStyle

    Parameters
    ----------

    textStyle : QSGTextNode.TextStyle
      Passed on as its number.
    """
    #  void QSGInternalTextNode::setTextStyle(TextStyle textStyle)
    ritual = (
        'ritual_ZN19QSGInternalTextNode12setTextStyleEN11QSGTextNode9TextSt'
        'yleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode12setTextStyleEN11QSGTextNode9'
          'TextStyleE')
    self.uglySide.call(ritual, textStyle.value)

  @overload(QColor)
  def setStyleColor(self, styleColor: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setStyleColor(QColor styleColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setStyleColor

    Parameters
    ----------

    styleColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setStyleColor(QColor styleColor)
    ritual = 'ritual_ZN19QSGInternalTextNode13setStyleColorE6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode13setStyleColorE6QColor'
    self.uglySide.call(ritual, self._valueOf(styleColor))

  @overload(QColor)
  def setLinkColor(self, linkColor: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setLinkColor(QColor linkColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setLinkColor

    Parameters
    ----------

    linkColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setLinkColor(QColor linkColor)
    ritual = 'ritual_ZN19QSGInternalTextNode12setLinkColorE6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode12setLinkColorE6QColor'
    self.uglySide.call(ritual, self._valueOf(linkColor))

  @overload(QColor)
  def setSelectionColor(self, selectionColor: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setSelectionColor(QColor
    selectionColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setSelectionColor

    Parameters
    ----------

    selectionColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setSelectionColor(QColor selectionColor)
    ritual = 'ritual_ZN19QSGInternalTextNode17setSelectionColorE6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode17setSelectionColorE6QColor')
    self.uglySide.call(ritual, self._valueOf(selectionColor))

  @overload(QColor)
  def setSelectionTextColor(self, selectionTextColor: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setSelectionTextColor(QColor
    selectionTextColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setSelectionTextColor

    Parameters
    ----------

    selectionTextColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setSelectionTextColor(QColor
    #      selectionTextColor)
    ritual = 'ritual_ZN19QSGInternalTextNode21setSelectionTextColorE6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode21setSelectionTextColorE6QColo'
          'r')
    self.uglySide.call(ritual, self._valueOf(selectionTextColor))

  @overload(int)
  def setRenderTypeQuality(self, renderTypeQuality: int) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setRenderTypeQuality(int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setRenderTypeQuality

    Parameters
    ----------

    renderTypeQuality : int
      Passed on as it is.
    """
    #  void QSGInternalTextNode::setRenderTypeQuality(int renderTypeQuality)
    ritual = 'ritual_ZN19QSGInternalTextNode20setRenderTypeQualityEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode20setRenderTypeQualityEi'
    self.uglySide.call(ritual, renderTypeQuality)

  @overload(QSGTextNode.RenderType)
  def setRenderType(self, renderType: QSGTextNode.RenderType) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setRenderType(RenderType
    renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setRenderType

    Parameters
    ----------

    renderType : QSGTextNode.RenderType
      Passed on as its number.
    """
    #  void QSGInternalTextNode::setRenderType(RenderType renderType)
    ritual = (
        'ritual_ZN19QSGInternalTextNode13setRenderTypeEN11QSGTextNode10Rend'
        'erTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode13setRenderTypeEN11QSGTextNode'
          '10RenderTypeE')
    self.uglySide.call(ritual, renderType.value)

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGInternalTextNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN19QSGInternalTextNode12setFilteringEN10QSGTexture9Filteri'
        'ngE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode12setFilteringEN10QSGTexture9F'
          'ilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QRectF)
  def setViewport(self, viewport: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setViewport(const QRectF
    &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setViewport

    Parameters
    ----------

    viewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalTextNode::setViewport(const QRectF &viewport)
    ritual = 'ritual_ZN19QSGInternalTextNode11setViewportERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode11setViewportERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(viewport))

  @overload(float)
  def setDevicePixelRatio(self, dpr: float) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setDevicePixelRatio(qreal dpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#setDevicePixelRatio

    Parameters
    ----------

    dpr : float
      Passed on as it is.
    """
    #  void QSGInternalTextNode::setDevicePixelRatio(qreal dpr)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode19setDevicePixelRatioEd', dpr,
    )

  @overload(QRectF, QColor, RecycleBin)
  @overload(QRectF, QColor, NoneType)
  def setCursor(
      self,
      rect: QRectF,
      color: QColor,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::setCursor(const QRectF &rect, const
    QColor &color, RecycleBin *recycleBin)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#setCursor

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::setCursor(const QRectF &rect, const QColor
    #      &color, RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode9setCursorERK6QRectFRK6QColorPNS_10R'
        'ecycleBinE',
        self._valueOf(rect), self._valueOf(color),
        self._addressOf(recycleBin),
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, renderContext: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGInternalTextNode::QSGInternalTextNode(QSGRenderContext
    *renderContext)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#QSGInternalTextNode

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGInternalTextNode::QSGInternalTextNode(QSGRenderContext
    #      *renderContext)
    self._noteCreation(QSGInternalTextNode, lambda: Rituals.call(
        'ritual_ZN19QSGInternalTextNodeC1EP16QSGRenderContext',
        self._addressOf(renderContext),
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

  def textStyle(self) -> QSGTextNode.TextStyle:
    """
    Calls Qt's 'TextStyle QSGInternalTextNode::textStyle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#textStyle

    Returns
    -------

    QSGTextNode.TextStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTextNode.TextStyle(number)' gives.
    """
    #  TextStyle QSGInternalTextNode::textStyle()
    ritual = 'ritual_ZN19QSGInternalTextNode9textStyleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode9textStyleEv'
    return QSGTextNode.TextStyle(self.uglySide.call(ritual))

  def clearCursor(self) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::clearCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#clearCursor
    """
    #  void QSGInternalTextNode::clearCursor()
    self.uglySide.call('ritual_ZN19QSGInternalTextNode11clearCursorEv')

  @overload(QRectF, QColor, RecycleBin)
  @overload(QRectF, QColor, NoneType)
  def addRectangleNode(
      self,
      rect: QRectF,
      color: QColor,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::addRectangleNode(const QRectF
    &rect, const QColor &color, RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#addRectangleNode

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::addRectangleNode(const QRectF &rect, const
    #      QColor &color, RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode16addRectangleNodeERK6QRectFRK6QColo'
        'rPNS_10RecycleBinE',
        self._valueOf(rect), self._valueOf(color),
        self._addressOf(recycleBin),
    )

  @overload(QRectF, QColor, QTextCharFormat.UnderlineStyle, RecycleBin)
  @overload(QRectF, QColor, QTextCharFormat.UnderlineStyle, NoneType)
  def addDecorationNode(
      self,
      rect: QRectF,
      color: QColor,
      style: QTextCharFormat.UnderlineStyle,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::addDecorationNode(const QRectF
    &rect, const QColor &color, QTextCharFormat::UnderlineStyle style,
    RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#addDecorationNode

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    style : QTextCharFormat.UnderlineStyle
      Passed on as its number.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::addDecorationNode(const QRectF &rect, const
    #      QColor &color, QTextCharFormat::UnderlineStyle style, RecycleBin
    #      *recycleBin)
    ritual = (
        'ritual_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QCol'
        'orN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFR'
          'K6QColorN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE')
    self.uglySide.call(
        ritual,
        self._valueOf(rect), self._valueOf(color), style.value,
        self._addressOf(recycleBin),
    )

  @overload(QRectF, QImage, RecycleBin)
  @overload(QRectF, QImage, NoneType)
  def addImage(
      self,
      rect: QRectF,
      image: QImage,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::addImage(const QRectF &rect, const
    QImage &image, RecycleBin *recycleBin)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#addImage

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::addImage(const QRectF &rect, const QImage
    #      &image, RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode8addImageERK6QRectFRK6QImagePNS_10Re'
        'cycleBinE',
        self._valueOf(rect), self._valueOf(image),
        self._addressOf(recycleBin),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#clear
    """
    #  void QSGInternalTextNode::clear()
    ritual = 'ritual_ZN19QSGInternalTextNode5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGInternalTextNode5clearEv'
    self.uglySide.call(ritual)

  @overload(RecycleBin)
  @overload(NoneType)
  def recycle(self, recycleBin: Optional[RecycleBin]) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::recycle(RecycleBin *recycleBin)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#recycle

    Parameters
    ----------

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::recycle(RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode7recycleEPNS_10RecycleBinE',
        self._addressOf(recycleBin),
    )

  @overload(QPointF, QGlyphRun, QColor, RecycleBin)
  @overload(QPointF, QGlyphRun, QColor, NoneType)
  @overload(QPointF, QGlyphRun, QColor, RecycleBin, QQuickText.TextStyle)
  @overload(QPointF, QGlyphRun, QColor, NoneType, QQuickText.TextStyle)
  @overload(
      QPointF, QGlyphRun, QColor, RecycleBin, QQuickText.TextStyle, QColor,
  )
  @overload(
      QPointF, QGlyphRun, QColor, NoneType, QQuickText.TextStyle, QColor,
  )
  @overload(
      QPointF, QGlyphRun, QColor, RecycleBin, QQuickText.TextStyle, QColor,
      QSGNode,
  )
  @overload(
      QPointF, QGlyphRun, QColor, RecycleBin, QQuickText.TextStyle, QColor,
      NoneType,
  )
  @overload(
      QPointF, QGlyphRun, QColor, NoneType, QQuickText.TextStyle, QColor,
      QSGNode,
  )
  @overload(
      QPointF, QGlyphRun, QColor, NoneType, QQuickText.TextStyle, QColor,
      NoneType,
  )
  def addGlyphs(
      self,
      position: QPointF,
      glyphs: QGlyphRun,
      color: QColor,
      recycleBin: Optional[RecycleBin],
      style: QQuickText.TextStyle = QQuickText.TextStyle.Normal,
      styleColor: Optional[QColor] = None,
      parentNode: Optional[QSGNode] = None,
  ) -> Optional[QSGGlyphNode]:
    """
    Calls Qt's 'QSGGlyphNode *QSGInternalTextNode::addGlyphs(const QPointF
    &position, const QGlyphRun &glyphs, const QColor &color, RecycleBin
    *recycleBin, QQuickText::TextStyle style, const QColor &styleColor,
    QSGNode *parentNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternaltextnode.html#addGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : QQuickText.TextStyle
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickText.TextStyle.Normal.

    styleColor : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.

    parentNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QSGGlyphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGlyphNode *QSGInternalTextNode::addGlyphs(const QPointF &position,
    #      const QGlyphRun &glyphs, const QColor &color, RecycleBin
    #      *recycleBin, QQuickText::TextStyle style, const QColor
    #      &styleColor, QSGNode *parentNode)
    if styleColor is None:
      from ..QtGui import QColor
      styleColor = QColor()
    address = self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode9addGlyphsERK7QPointFRK9QGlyphRunRK6'
        'QColorPNS_10RecycleBinEN10QQuickText9TextStyleES8_P7QSGNode',
        self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
        self._valueOf(color), self._addressOf(recycleBin), style.value,
        self._valueOf(styleColor), self._addressOf(parentNode, 'QSGNode'),
    )
    from . import QSGGlyphNode
    return QSGGlyphNode._cuteAt(address)

  @overload(RecycleBin)
  @overload(NoneType)
  def discardUnusedNodes(self, recycleBin: Optional[RecycleBin]) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::discardUnusedNodes(RecycleBin
    *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#discardUnusedNodes

    Parameters
    ----------

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::discardUnusedNodes(RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode18discardUnusedNodesEPNS_10RecycleBi'
        'nE',
        self._addressOf(recycleBin),
    )

  @overload(QPointF, QTextLayout, RecycleBin)
  @overload(QPointF, QTextLayout, NoneType)
  @overload(QPointF, NoneType, RecycleBin)
  @overload(QPointF, NoneType, NoneType)
  @overload(QPointF, QTextLayout, RecycleBin, int)
  @overload(QPointF, QTextLayout, NoneType, int)
  @overload(QPointF, NoneType, RecycleBin, int)
  @overload(QPointF, NoneType, NoneType, int)
  @overload(QPointF, QTextLayout, RecycleBin, int, int)
  @overload(QPointF, QTextLayout, NoneType, int, int)
  @overload(QPointF, NoneType, RecycleBin, int, int)
  @overload(QPointF, NoneType, NoneType, int, int)
  @overload(QPointF, QTextLayout, RecycleBin, int, int, int)
  @overload(QPointF, QTextLayout, NoneType, int, int, int)
  @overload(QPointF, NoneType, RecycleBin, int, int, int)
  @overload(QPointF, NoneType, NoneType, int, int, int)
  @overload(QPointF, QTextLayout, RecycleBin, int, int, int, int)
  @overload(QPointF, QTextLayout, NoneType, int, int, int, int)
  @overload(QPointF, NoneType, RecycleBin, int, int, int, int)
  @overload(QPointF, NoneType, NoneType, int, int, int, int)
  def addTextLayout(
      self,
      position: QPointF,
      layout: Optional[QTextLayout],
      recycleBin: Optional[RecycleBin],
      selectionStart: int = -1,
      selectionCount: int = -1,
      lineStart: int = 0,
      lineCount: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::addTextLayout(QPointF position,
    QTextLayout *layout, RecycleBin *recycleBin, int selectionStart, int
    selectionCount, int lineStart, int lineCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#addTextLayout

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    layout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    selectionCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    lineStart : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    lineCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QSGInternalTextNode::addTextLayout(QPointF position, QTextLayout
    #      *layout, RecycleBin *recycleBin, int selectionStart, int
    #      selectionCount, int lineStart, int lineCount)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode13addTextLayoutE7QPointFP11QTextLayo'
        'utPNS_10RecycleBinEiiii',
        self._valueOf(position, 'QPointF'), self._addressOf(layout),
        self._addressOf(recycleBin), selectionStart, selectionCount,
        lineStart, lineCount,
    )

  @overload(QPointF, QTextDocument, RecycleBin)
  @overload(QPointF, QTextDocument, NoneType)
  @overload(QPointF, NoneType, RecycleBin)
  @overload(QPointF, NoneType, NoneType)
  @overload(QPointF, QTextDocument, RecycleBin, int)
  @overload(QPointF, QTextDocument, NoneType, int)
  @overload(QPointF, NoneType, RecycleBin, int)
  @overload(QPointF, NoneType, NoneType, int)
  @overload(QPointF, QTextDocument, RecycleBin, int, int)
  @overload(QPointF, QTextDocument, NoneType, int, int)
  @overload(QPointF, NoneType, RecycleBin, int, int)
  @overload(QPointF, NoneType, NoneType, int, int)
  def addTextDocument(
      self,
      position: QPointF,
      document: Optional[QTextDocument],
      recycleBin: Optional[RecycleBin],
      selectionStart: int = -1,
      selectionCount: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::addTextDocument(QPointF position,
    QTextDocument *document, RecycleBin *recycleBin, int selectionStart, int
    selectionCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#addTextDocument

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    selectionCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QSGInternalTextNode::addTextDocument(QPointF position,
    #      QTextDocument *document, RecycleBin *recycleBin, int
    #      selectionStart, int selectionCount)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode15addTextDocumentE7QPointFP13QTextDo'
        'cumentPNS_10RecycleBinEii',
        self._valueOf(position, 'QPointF'), self._addressOf(document),
        self._addressOf(recycleBin), selectionStart, selectionCount,
    )

  @overload(QPointF, QTextLayout, int, int, int, int, RecycleBin)
  @overload(QPointF, QTextLayout, int, int, int, int, NoneType)
  @overload(QPointF, NoneType, int, int, int, int, RecycleBin)
  @overload(QPointF, NoneType, int, int, int, int, NoneType)
  def doAddTextLayout(
      self,
      position: QPointF,
      textLayout: Optional[QTextLayout],
      selectionStart: int,
      selectionEnd: int,
      lineStart: int,
      lineCount: int,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::doAddTextLayout(QPointF position,
    QTextLayout *textLayout, int selectionStart, int selectionEnd, int
    lineStart, int lineCount, RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#doAddTextLayout

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textLayout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.

    lineStart : int
      Passed on as it is.

    lineCount : int
      Passed on as it is.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::doAddTextLayout(QPointF position,
    #      QTextLayout *textLayout, int selectionStart, int selectionEnd, int
    #      lineStart, int lineCount, RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11QTextLa'
        'youtiiiiPNS_10RecycleBinE',
        self._valueOf(position, 'QPointF'), self._addressOf(textLayout),
        selectionStart, selectionEnd, lineStart, lineCount,
        self._addressOf(recycleBin),
    )

  @overload(QPointF, QTextLayout, int, int, int, int)
  @overload(QPointF, NoneType, int, int, int, int)
  def doAddTextLayout(
      self,
      position: QPointF,
      textLayout: Optional[QTextLayout],
      selectionStart: int,
      selectionEnd: int,
      lineStart: int,
      lineCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::doAddTextLayout(QPointF position,
    QTextLayout *textLayout, int selectionStart, int selectionEnd, int
    lineStart, int lineCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#doAddTextLayout

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textLayout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.

    lineStart : int
      Passed on as it is.

    lineCount : int
      Passed on as it is.
    """
    #  void QSGInternalTextNode::doAddTextLayout(QPointF position,
    #      QTextLayout *textLayout, int selectionStart, int selectionEnd, int
    #      lineStart, int lineCount)
    ritual = (
        'ritual_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11QTextLa'
        'youtiiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11Q'
          'TextLayoutiiii')
    self.uglySide.call(
        ritual,
        self._valueOf(position, 'QPointF'), self._addressOf(textLayout),
        selectionStart, selectionEnd, lineStart, lineCount,
    )

  @overload(QPointF, QTextDocument, int, int, RecycleBin)
  @overload(QPointF, QTextDocument, int, int, NoneType)
  @overload(QPointF, NoneType, int, int, RecycleBin)
  @overload(QPointF, NoneType, int, int, NoneType)
  def doAddTextDocument(
      self,
      position: QPointF,
      textDocument: Optional[QTextDocument],
      selectionStart: int,
      selectionEnd: int,
      recycleBin: Optional[RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::doAddTextDocument(QPointF position,
    QTextDocument *textDocument, int selectionStart, int selectionEnd,
    RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#doAddTextDocument

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textDocument : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalTextNode::doAddTextDocument(QPointF position,
    #      QTextDocument *textDocument, int selectionStart, int selectionEnd,
    #      RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP13QText'
        'DocumentiiPNS_10RecycleBinE',
        self._valueOf(position, 'QPointF'), self._addressOf(textDocument),
        selectionStart, selectionEnd, self._addressOf(recycleBin),
    )

  @overload(QPointF, QTextDocument, int, int)
  @overload(QPointF, NoneType, int, int)
  def doAddTextDocument(
      self,
      position: QPointF,
      textDocument: Optional[QTextDocument],
      selectionStart: int,
      selectionEnd: int,
  ) -> None:
    """
    Calls Qt's 'void QSGInternalTextNode::doAddTextDocument(QPointF position,
    QTextDocument *textDocument, int selectionStart, int selectionEnd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#doAddTextDocument

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textDocument : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.
    """
    #  void QSGInternalTextNode::doAddTextDocument(QPointF position,
    #      QTextDocument *textDocument, int selectionStart, int selectionEnd)
    ritual = (
        'ritual_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP13QText'
        'Documentii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP1'
          '3QTextDocumentii')
    self.uglySide.call(
        ritual,
        self._valueOf(position, 'QPointF'), self._addressOf(textDocument),
        selectionStart, selectionEnd,
    )

  @overload(RecycleBin)
  @overload(NoneType)
  def findOrCreateImageNode(
      self,
      recycleBin: Optional[RecycleBin],
  ) -> Optional[QSGInternalImageNode]:
    """
    Calls Qt's 'QSGInternalImageNode
    *QSGInternalTextNode::findOrCreateImageNode(RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#findOrCreateImageNode

    Parameters
    ----------

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGInternalImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalImageNode
    #      *QSGInternalTextNode::findOrCreateImageNode(RecycleBin
    #      *recycleBin)
    address = self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode21findOrCreateImageNodeEPNS_10Recycl'
        'eBinE',
        self._addressOf(recycleBin),
    )
    from . import QSGInternalImageNode
    return QSGInternalImageNode._cuteAt(address)

  @overload(QSGTextNode.RenderType, RecycleBin, QSGNode)
  @overload(QSGTextNode.RenderType, RecycleBin, NoneType)
  @overload(QSGTextNode.RenderType, NoneType, QSGNode)
  @overload(QSGTextNode.RenderType, NoneType, NoneType)
  def findOrCreateGlyphNode(
      self,
      renderType: QSGTextNode.RenderType,
      recycleBin: Optional[RecycleBin],
      parentNode: Optional[QSGNode],
  ) -> Optional[QSGGlyphNode]:
    """
    Calls Qt's 'QSGGlyphNode
    *QSGInternalTextNode::findOrCreateGlyphNode(RenderType renderType,
    RecycleBin *recycleBin, QSGNode *parentNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#findOrCreateGlyphNode

    Parameters
    ----------

    renderType : QSGTextNode.RenderType
      Passed on as its number.

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGGlyphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGlyphNode *QSGInternalTextNode::findOrCreateGlyphNode(RenderType
    #      renderType, RecycleBin *recycleBin, QSGNode *parentNode)
    address = self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode21findOrCreateGlyphNodeEN11QSGTextNo'
        'de10RenderTypeEPNS_10RecycleBinEP7QSGNode',
        renderType.value, self._addressOf(recycleBin),
        self._addressOf(parentNode, 'QSGNode'),
    )
    from . import QSGGlyphNode
    return QSGGlyphNode._cuteAt(address)

  @overload(RecycleBin)
  @overload(NoneType)
  def findOrCreateRectangleNode(
      self,
      recycleBin: Optional[RecycleBin],
  ) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode
    *QSGInternalTextNode::findOrCreateRectangleNode(RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternaltextnode.html#findOrCreateRectangleNode

    Parameters
    ----------

    recycleBin : Optional[RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode
    #      *QSGInternalTextNode::findOrCreateRectangleNode(RecycleBin
    #      *recycleBin)
    address = self.uglySide.call(
        'ritual_ZN19QSGInternalTextNode25findOrCreateRectangleNodeEPNS_10Re'
        'cycleBinE',
        self._addressOf(recycleBin),
    )
    from . import QSGInternalRectangleNode
    return QSGInternalRectangleNode._cuteAt(address)

  @staticmethod
  def isComplexRichText(*__, **_) -> Never:
    """
    Qt's 'bool QSGInternalTextNode::isComplexRichText(QTextDocument *a0)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QSGInternalTextNode.isComplexRichText' has no cute function yet. "
        "Qt's 'bool QSGInternalTextNode::isComplexRichText(QTextDocument "
        "*a0)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def renderedLineRange(*__, **_) -> Never:
    """
    Qt's 'std::pair<int, int> QSGInternalTextNode::renderedLineRange()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGInternalTextNode.renderedLineRange' has no cute function yet. "
        "Qt's 'std::pair<int, int> QSGInternalTextNode::renderedLineRange() "
        "const': gives a type Python has no way to take yet.")
