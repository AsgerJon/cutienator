"""
QQuickTextNodeEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickTextNodeEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QTextCharFormat, QTextFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QBrush, QColor, QGlyphRun, QImage, QTextBlock
  from ..QtGui import QTextDocument, QTextFrame, QTextLine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QImage = WAIT['QImage']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFrame = WAIT['QTextFrame']
  QTextLine = WAIT['QTextLine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextNodeEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickTextNodeEngine: a plain Python object standing
  in front of one C++ QQuickTextNodeEngine.

  C++ hands a QQuickTextNodeEngine around as a copy, so every C++
  QQuickTextNodeEngine behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickTextNodeEngine that has a ritual and that
  Python can call so far, 19 names in all: 'hasContents', 'addTextBlock',
  'currentLine', 'setCurrentLine', 'setCurrentTextDirection', 'addBorder',
  'addFrameDecorations', 'addImage', 'addTextObject', 'addSelectedGlyphs',
  'addUnselectedGlyphs', 'addGlyphsInRange', 'setSelectionColor',
  'setSelectedTextColor', 'setTextColor', 'setAnchorColor', 'setPosition',
  'setDevicePixelRatio', 'processCurrentLine'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QQuickTextNodeEngine::addText(const QTextBlock &block, const
    QTextCharFormat &charFormat, const QColor &textColor, const
    QVarLengthArray<QTextLayout::FormatRange> &colorChanges, int textPos, int
    fragmentEnd, int selectionStart, int selectionEnd)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QQuickTextNodeEngine::addGlyphsForRanges(const
    QVarLengthArray<QTextLayout::FormatRange> &ranges, int start, int end,
    int selectionStart, int selectionEnd)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQuickTextNodeEngine::addTextDecorations(QSpan<const
    TextDecoration> textDecorations, qreal offset, qreal thickness)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQuickTextNodeEngine::mergeFormats(QTextLayout *textLayout,
    QVarLengthArray<QTextLayout::FormatRange> *mergedFormats)': names
    'QVarLengthArray<QTextLayout::FormatRange>', which has no cute class yet.
  - Qt's 'QQuickTextNodeEngine::~QQuickTextNodeEngine()': the destructor:
    Python removes its C++ QQuickTextNodeEngine by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickTextNodeEngine.

  What to expect
  --------------

  - The C++ QQuickTextNodeEngine is created at the first use, not by
    'QQuickTextNodeEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickTextNodeEngine back gives a copy the ritual
    made for Python, in a new cute QQuickTextNodeEngine.
  - Each name of Qt's QQuickTextNodeEngine that has no cute function yet,
    'addGlyphsForRanges', 'addText', 'addTextDecorations', 'addToSceneGraph',
    'mergeFormats', 'mergeProcessedNodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickTextNodeEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Decoration(CuteFlags):
    """
    The flags enum 'QQuickTextNodeEngine::Decoration' of Qt, with the 5 names
    Qt gives in it. Qt names the type of its combinations
    'QQuickTextNodeEngine::Decorations'.
    """

    NoDecoration = 0x0
    Underline = 0x1
    Overline = 0x2
    StrikeOut = 0x4
    Background = 0x8

  Decorations = Decoration

  class SelectionState(CuteNum):
    """
    The enum 'QQuickTextNodeEngine::SelectionState' of Qt, with the 2 names
    Qt gives in it.
    """

    Unselected = Kee[int](0)
    Selected = Kee[int](1)

  #  The classes Qt writes inside QQuickTextNodeEngine, each a class in here
  #  as in C++.

  class BinaryTreeNode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextNodeEngine::BinaryTreeNode: a plain
    Python object standing in front of one C++
    QQuickTextNodeEngine::BinaryTreeNode.

    C++ hands a QQuickTextNodeEngine::BinaryTreeNode around as a copy, so
    every C++ QQuickTextNodeEngine::BinaryTreeNode behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickTextNodeEngine::BinaryTreeNode yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const QRectF
      &brect, const QImage &i, SelectionState selState, qreal a)': names the
      enum 'QQuickTextNodeEngine::SelectionState', whose class cannot be
      named here.
    - Qt's 'QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const
      QGlyphRun &g, SelectionState selState, const QRectF &brect, const
      Decorations &decs, QTextCharFormat::UnderlineStyle us, const QColor &c,
      const QColor &bc, const QColor &dc, const QPointF &pos, qreal a)':
      names the enum 'QQuickTextNodeEngine::SelectionState', whose class
      cannot be named here.
    - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
      QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QRectF &rect,
      const QImage &image, qreal ascent, SelectionState selectionState)':
      names 'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>',
      which has no cute class yet.
    - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
      QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QGlyphRun
      &glyphRun, SelectionState selectionState, Decorations decorations,
      QTextCharFormat::UnderlineStyle underlineStyle, const QColor
      &textColor, const QColor &backgroundColor, const QColor
      &underlineColor, const QPointF &position)': names
      'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', which has
      no cute class yet.
    - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
      QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const BinaryTreeNode
      &binaryTreeNode)': names
      'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', which has
      no cute class yet.
    - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::inOrder(const
      QVarLengthArray<BinaryTreeNode, 16> &binaryTree, QVarLengthArray<int>
      *sortedIndexes, int currentIndex)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QQuickTextNodeEngine::BinaryTreeNode::~BinaryTreeNode()': the
      destructor: Python removes its C++ QQuickTextNodeEngine::BinaryTreeNode
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextNodeEngine::BinaryTreeNode is created at the first
      use, not by 'QQuickTextNodeEngine::BinaryTreeNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextNodeEngine::BinaryTreeNode back gives a
      copy the ritual made for Python, in a new cute
      QQuickTextNodeEngine::BinaryTreeNode.
    - Each name of Qt's QQuickTextNodeEngine::BinaryTreeNode that has no cute
      function yet, 'inOrder', 'insert', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextNodeEngine::BinaryTreeNode'

    #  Qt's '~QQuickTextNodeEngine::BinaryTreeNode()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QQuickTextNodeEngine::BinaryTreeNode behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeD1Ev'

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
      'QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktextnodeengine-binarytreenode.html
      """
      #  QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode()
      self._noteCreation(
          QQuickTextNodeEngine.BinaryTreeNode, lambda: Rituals.call(
              'ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeC1Ev',
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

    @staticmethod
    def inOrder(*__, **_) -> Never:
      """
      Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::inOrder(const
      QVarLengthArray<BinaryTreeNode, 16> &binaryTree, QVarLengthArray<int>
      *sortedIndexes, int currentIndex)': takes a type Python has no way to
      hand over yet.
      """
      raise NotImplementedError(
          "'QQuickTextNodeEngine.BinaryTreeNode.inOrder' has no cute "
          "function yet. Qt's 'void "
          "QQuickTextNodeEngine::BinaryTreeNode::inOrder(const "
          "QVarLengthArray<BinaryTreeNode, 16> &binaryTree, "
          "QVarLengthArray<int> *sortedIndexes, int currentIndex)': takes a "
          "type Python has no way to hand over yet.")

    @staticmethod
    def insert(*__, **_) -> Never:
      """
      - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
        QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QRectF &rect,
        const QImage &image, qreal ascent, SelectionState selectionState)':
        names 'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>',
        which has no cute class yet.
      - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
        QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QGlyphRun
        &glyphRun, SelectionState selectionState, Decorations decorations,
        QTextCharFormat::UnderlineStyle underlineStyle, const QColor
        &textColor, const QColor &backgroundColor, const QColor
        &underlineColor, const QPointF &position)': names
        'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', which
        has no cute class yet.
      - Qt's 'void QQuickTextNodeEngine::BinaryTreeNode::insert(
        QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const BinaryTreeNode
        &binaryTreeNode)': names
        'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', which
        has no cute class yet.
      """
      raise NotImplementedError(
          "'QQuickTextNodeEngine.BinaryTreeNode.insert' has no cute "
          "function yet. Qt's 'void "
          "QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<Bina"
          "ryTreeNode, 16> *binaryTree, const QRectF &rect, const QImage "
          "&image, qreal ascent, SelectionState selectionState)': names "
          "'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', "
          "which has no cute class yet. Qt's 'void "
          "QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<Bina"
          "ryTreeNode, 16> *binaryTree, const QGlyphRun &glyphRun, "
          "SelectionState selectionState, Decorations decorations, "
          "QTextCharFormat::UnderlineStyle underlineStyle, const QColor "
          "&textColor, const QColor &backgroundColor, const QColor "
          "&underlineColor, const QPointF &position)': names "
          "'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', "
          "which has no cute class yet. Qt's 'void "
          "QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<Bina"
          "ryTreeNode, 16> *binaryTree, const BinaryTreeNode "
          "&binaryTreeNode)': names "
          "'QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16>', "
          "which has no cute class yet.")

  class BinaryTreeNodeKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextNodeEngine::BinaryTreeNodeKey: a plain
    Python object standing in front of one C++
    QQuickTextNodeEngine::BinaryTreeNodeKey.

    C++ hands a QQuickTextNodeEngine::BinaryTreeNodeKey around as a copy, so
    every C++ QQuickTextNodeEngine::BinaryTreeNodeKey behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickTextNodeEngine::BinaryTreeNodeKey that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextNodeEngine::BinaryTreeNodeKey::BinaryTreeNodeKey(
      BinaryTreeNode *node)': names 'QQuickTextNodeEngine::BinaryTreeNode',
      which stands beside this class inside 'QQuickTextNodeEngine' and cannot
      be named from here.
    - Qt's 'QQuickTextNodeEngine::BinaryTreeNodeKey::~BinaryTreeNodeKey()':
      the destructor: Python removes its C++
      QQuickTextNodeEngine::BinaryTreeNodeKey by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQuickTextNodeEngine::BinaryTreeNodeKey is created at the first
      use, not by 'QQuickTextNodeEngine::BinaryTreeNodeKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextNodeEngine::BinaryTreeNodeKey back gives
      a copy the ritual made for Python, in a new cute
      QQuickTextNodeEngine::BinaryTreeNodeKey.
    - Each name of Qt's QQuickTextNodeEngine::BinaryTreeNodeKey that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextNodeEngine::BinaryTreeNodeKey'

    #  Qt's '~QQuickTextNodeEngine::BinaryTreeNodeKey()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickTextNodeEngine::BinaryTreeNodeKey behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN20QQuickTextNodeEngine17BinaryTreeNodeKeyD1Ev')

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

    @overload(THIS)
    def __eq__(
        self,
        otherKey: QQuickTextNodeEngine.BinaryTreeNodeKey,
    ) -> bool:
      """
      Calls Qt's 'bool
      QQuickTextNodeEngine::BinaryTreeNodeKey::operator==(const
      BinaryTreeNodeKey &otherKey) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktextnodeengine-binarytreenodekey.html

      Parameters
      ----------

      otherKey : QQuickTextNodeEngine.BinaryTreeNodeKey
        Passed on as a value: Qt reads the C++
        QQuickTextNodeEngine::BinaryTreeNodeKey, which stays Python's own.
      """
      #  bool QQuickTextNodeEngine::BinaryTreeNodeKey::operator==(const
      #      BinaryTreeNodeKey &otherKey) const
      return self.uglySide.call(
          'ritual_ZNK20QQuickTextNodeEngine17BinaryTreeNodeKeyeqERKS0_',
          self._valueOf(otherKey),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQuickTextNodeEngine::BinaryTreeNodeKey::BinaryTreeNodeKey(
      BinaryTreeNode *node)': names 'QQuickTextNodeEngine::BinaryTreeNode',
      which stands beside this class inside 'QQuickTextNodeEngine' and cannot
      be named from here.
      """
      raise NotImplementedError(
          "'QQuickTextNodeEngine.BinaryTreeNodeKey.__init__' has no cute "
          "function yet. Qt's "
          "'QQuickTextNodeEngine::BinaryTreeNodeKey::BinaryTreeNodeKey(Binar"
          "yTreeNode *node)': names 'QQuickTextNodeEngine::BinaryTreeNode', "
          "which stands beside this class inside 'QQuickTextNodeEngine' and "
          "cannot be named from here.")

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextNodeEngine'

  #  Qt's '~QQuickTextNodeEngine()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickTextNodeEngine behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickTextNodeEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasContents(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextNodeEngine::hasContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#hasContents
    """
    #  bool QQuickTextNodeEngine::hasContents() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickTextNodeEngine11hasContentsEv',
    )

  def currentLine(self) -> QTextLine:
    """
    Calls Qt's 'QTextLine QQuickTextNodeEngine::currentLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#currentLine

    Returns
    -------

    QTextLine
      A new cute QTextLine around the copy Qt gave back. Python owns it.
    """
    #  QTextLine QQuickTextNodeEngine::currentLine() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTextNodeEngine11currentLineEv',
    )
    from ..QtGui import QTextLine
    return QTextLine._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextLine)
  def setCurrentLine(self, currentLine: QTextLine) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setCurrentLine(const QTextLine
    &currentLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setCurrentLine

    Parameters
    ----------

    currentLine : QTextLine
      Passed on as a value: Qt reads the C++ QTextLine, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setCurrentLine(const QTextLine
    #      &currentLine)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine14setCurrentLineERK9QTextLine',
        self._valueOf(currentLine),
    )

  @overload(Qt.LayoutDirection)
  def setCurrentTextDirection(
      self,
      textDirection: Qt.LayoutDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTextNodeEngine::setCurrentTextDirection(Qt::LayoutDirection
    textDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setCurrentTextDirection

    Parameters
    ----------

    textDirection : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickTextNodeEngine::setCurrentTextDirection(Qt::LayoutDirection
    #      textDirection)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine23setCurrentTextDirectionEN2Qt15Lay'
        'outDirectionE',
        textDirection.value,
    )

  @overload(QColor)
  def setSelectionColor(self, selectionColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setSelectionColor(const QColor
    &selectionColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setSelectionColor

    Parameters
    ----------

    selectionColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setSelectionColor(const QColor
    #      &selectionColor)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine17setSelectionColorERK6QColor',
        self._valueOf(selectionColor),
    )

  @overload(QColor)
  def setSelectedTextColor(self, selectedTextColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setSelectedTextColor(const QColor
    &selectedTextColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setSelectedTextColor

    Parameters
    ----------

    selectedTextColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setSelectedTextColor(const QColor
    #      &selectedTextColor)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine20setSelectedTextColorERK6QColor',
        self._valueOf(selectedTextColor),
    )

  @overload(QColor)
  def setTextColor(self, textColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setTextColor(const QColor
    &textColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setTextColor

    Parameters
    ----------

    textColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setTextColor(const QColor &textColor)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine12setTextColorERK6QColor',
        self._valueOf(textColor),
    )

  @overload(QColor)
  def setAnchorColor(self, anchorColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setAnchorColor(const QColor
    &anchorColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setAnchorColor

    Parameters
    ----------

    anchorColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setAnchorColor(const QColor &anchorColor)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine14setAnchorColorERK6QColor',
        self._valueOf(anchorColor),
    )

  @overload(QPointF)
  def setPosition(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setPosition(const QPointF
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::setPosition(const QPointF &position)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine11setPositionERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  @overload(float)
  def setDevicePixelRatio(self, dpr: float) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::setDevicePixelRatio(qreal dpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#setDevicePixelRatio

    Parameters
    ----------

    dpr : float
      Passed on as it is.
    """
    #  void QQuickTextNodeEngine::setDevicePixelRatio(qreal dpr)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine19setDevicePixelRatioEd', dpr,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTextNodeEngine::QQuickTextNodeEngine()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#QQuickTextNodeEngine
    """
    #  QQuickTextNodeEngine::QQuickTextNodeEngine()
    self._noteCreation(QQuickTextNodeEngine, lambda: Rituals.call(
        'ritual_ZN20QQuickTextNodeEngineC1Ev',
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

  @overload(QTextDocument, QTextBlock, QPointF, QColor, QColor, int, int)
  @overload(NoneType, QTextBlock, QPointF, QColor, QColor, int, int)
  @overload(
      QTextDocument, QTextBlock, QPointF, QColor, QColor, int, int, QRectF,
  )
  @overload(NoneType, QTextBlock, QPointF, QColor, QColor, int, int, QRectF)
  def addTextBlock(
      self,
      a0: Optional[QTextDocument],
      a1: QTextBlock,
      position: QPointF,
      textColor: QColor,
      anchorColor: QColor,
      selectionStart: int,
      selectionEnd: int,
      viewport: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addTextBlock(QTextDocument *a0,
    const QTextBlock &a1, const QPointF &position, const QColor &textColor,
    const QColor &anchorColor, int selectionStart, int selectionEnd, const
    QRectF &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addTextBlock

    Parameters
    ----------

    a0 : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    anchorColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.

    viewport : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTextNodeEngine::addTextBlock(QTextDocument *a0, const
    #      QTextBlock &a1, const QPointF &position, const QColor &textColor,
    #      const QColor &anchorColor, int selectionStart, int selectionEnd,
    #      const QRectF &viewport)
    if viewport is None:
      from ..QtCore import QRectF
      viewport = QRectF()
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine12addTextBlockEP13QTextDocumentRK10'
        'QTextBlockRK7QPointFRK6QColorSA_iiRK6QRectF',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(position,
        'QPointF'), self._valueOf(textColor), self._valueOf(anchorColor),
        selectionStart, selectionEnd, self._valueOf(viewport),
    )

  @overload(QRectF, float, QTextFrameFormat.BorderStyle, QBrush)
  def addBorder(
      self,
      rect: QRectF,
      border: float,
      borderStyle: QTextFrameFormat.BorderStyle,
      borderBrush: QBrush,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addBorder(const QRectF &rect,
    qreal border, QTextFrameFormat::BorderStyle borderStyle, const QBrush
    &borderBrush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addBorder

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    border : float
      Passed on as it is.

    borderStyle : QTextFrameFormat.BorderStyle
      Passed on as its number.

    borderBrush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::addBorder(const QRectF &rect, qreal border,
    #      QTextFrameFormat::BorderStyle borderStyle, const QBrush
    #      &borderBrush)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine9addBorderERK6QRectFdN16QTextFrameF'
        'ormat11BorderStyleERK6QBrush',
        self._valueOf(rect), border, borderStyle.value,
        self._valueOf(borderBrush),
    )

  @overload(QTextDocument, QTextFrame)
  @overload(QTextDocument, NoneType)
  @overload(NoneType, QTextFrame)
  @overload(NoneType, NoneType)
  def addFrameDecorations(
      self,
      document: Optional[QTextDocument],
      frame: Optional[QTextFrame],
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addFrameDecorations(QTextDocument
    *document, QTextFrame *frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addFrameDecorations

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextNodeEngine::addFrameDecorations(QTextDocument
    #      *document, QTextFrame *frame)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine19addFrameDecorationsEP13QTextDocum'
        'entP10QTextFrame',
        self._addressOf(document), self._addressOf(frame),
    )

  @overload(QRectF, QImage, float, SelectionState, QTextFrameFormat.Position)
  def addImage(
      self,
      rect: QRectF,
      image: QImage,
      ascent: float,
      selectionState: SelectionState,
      layoutPosition: QTextFrameFormat.Position,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addImage(const QRectF &rect, const
    QImage &image, qreal ascent, SelectionState selectionState,
    QTextFrameFormat::Position layoutPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextnodeengine.html#addImage

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    ascent : float
      Passed on as it is.

    selectionState : SelectionState
      Passed on as its number.

    layoutPosition : QTextFrameFormat.Position
      Passed on as its number.
    """
    #  void QQuickTextNodeEngine::addImage(const QRectF &rect, const QImage
    #      &image, qreal ascent, SelectionState selectionState,
    #      QTextFrameFormat::Position layoutPosition)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine8addImageERK6QRectFRK6QImagedNS_14S'
        'electionStateEN16QTextFrameFormat8PositionE',
        self._valueOf(rect), self._valueOf(image), ascent,
        selectionState.value, layoutPosition.value,
    )

  @overload(
      QTextBlock, QPointF, QTextCharFormat, SelectionState, QTextDocument,
      int,
  )
  @overload(
      QTextBlock, QPointF, QTextCharFormat, SelectionState, NoneType, int,
  )
  @overload(
      QTextBlock, QPointF, QTextCharFormat, SelectionState, QTextDocument,
      int, QTextFrameFormat.Position,
  )
  @overload(
      QTextBlock, QPointF, QTextCharFormat, SelectionState, NoneType, int,
      QTextFrameFormat.Position,
  )
  def addTextObject(
      self,
      block: QTextBlock,
      position: QPointF,
      format: QTextCharFormat,
      selectionState: SelectionState,
      textDocument: Optional[QTextDocument],
      pos: int,
      layoutPosition: QTextFrameFormat.Position = (
          QTextFrameFormat.Position.InFlow),
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addTextObject(const QTextBlock
    &block, const QPointF &position, const QTextCharFormat &format,
    SelectionState selectionState, QTextDocument *textDocument, int pos,
    QTextFrameFormat::Position layoutPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addTextObject

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.

    selectionState : SelectionState
      Passed on as its number.

    textDocument : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    layoutPosition : QTextFrameFormat.Position
      Passed on as its number. May be left out, as in Qt: it is then
      QTextFrameFormat.Position.InFlow.
    """
    #  void QQuickTextNodeEngine::addTextObject(const QTextBlock &block,
    #      const QPointF &position, const QTextCharFormat &format,
    #      SelectionState selectionState, QTextDocument *textDocument, int
    #      pos, QTextFrameFormat::Position layoutPosition)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine13addTextObjectERK10QTextBlockRK7QP'
        'ointFRK15QTextCharFormatNS_14SelectionStateEP13QTextDocumentiN16QT'
        'extFrameFormat8PositionE',
        self._valueOf(block), self._valueOf(position, 'QPointF'),
        self._valueOf(format), selectionState.value,
        self._addressOf(textDocument), pos, layoutPosition.value,
    )

  @overload(QGlyphRun)
  def addSelectedGlyphs(self, glyphRun: QGlyphRun) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addSelectedGlyphs(const QGlyphRun
    &glyphRun)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addSelectedGlyphs

    Parameters
    ----------

    glyphRun : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::addSelectedGlyphs(const QGlyphRun
    #      &glyphRun)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine17addSelectedGlyphsERK9QGlyphRun',
        self._valueOf(glyphRun),
    )

  @overload(QGlyphRun)
  def addUnselectedGlyphs(self, glyphRun: QGlyphRun) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addUnselectedGlyphs(const
    QGlyphRun &glyphRun)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addUnselectedGlyphs

    Parameters
    ----------

    glyphRun : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QQuickTextNodeEngine::addUnselectedGlyphs(const QGlyphRun
    #      &glyphRun)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine19addUnselectedGlyphsERK9QGlyphRun',
        self._valueOf(glyphRun),
    )

  @overload(
      int, int, QTextCharFormat.UnderlineStyle, QColor, QColor, QColor, int,
      int,
  )
  def addGlyphsInRange(
      self,
      rangeStart: int,
      rangeEnd: int,
      underlineStyle: QTextCharFormat.UnderlineStyle,
      color: QColor,
      backgroundColor: QColor,
      underlineColor: QColor,
      selectionStart: int,
      selectionEnd: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::addGlyphsInRange(int rangeStart,
    int rangeEnd, QTextCharFormat::UnderlineStyle underlineStyle, const
    QColor &color, const QColor &backgroundColor, const QColor
    &underlineColor, int selectionStart, int selectionEnd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#addGlyphsInRange

    Parameters
    ----------

    rangeStart : int
      Passed on as it is.

    rangeEnd : int
      Passed on as it is.

    underlineStyle : QTextCharFormat.UnderlineStyle
      Passed on as its number.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    backgroundColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    underlineColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    selectionStart : int
      Passed on as it is.

    selectionEnd : int
      Passed on as it is.
    """
    #  void QQuickTextNodeEngine::addGlyphsInRange(int rangeStart, int
    #      rangeEnd, QTextCharFormat::UnderlineStyle underlineStyle, const
    #      QColor &color, const QColor &backgroundColor, const QColor
    #      &underlineColor, int selectionStart, int selectionEnd)
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine16addGlyphsInRangeEiiN15QTextCharFo'
        'rmat14UnderlineStyleERK6QColorS4_S4_ii',
        rangeStart, rangeEnd, underlineStyle.value, self._valueOf(color),
        self._valueOf(backgroundColor), self._valueOf(underlineColor),
        selectionStart, selectionEnd,
    )

  def processCurrentLine(self) -> None:
    """
    Calls Qt's 'void QQuickTextNodeEngine::processCurrentLine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextnodeengine.html#processCurrentLine
    """
    #  void QQuickTextNodeEngine::processCurrentLine()
    self.uglySide.call(
        'ritual_ZN20QQuickTextNodeEngine18processCurrentLineEv',
    )

  @staticmethod
  def addGlyphsForRanges(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextNodeEngine::addGlyphsForRanges(const
    QVarLengthArray<QTextLayout::FormatRange> &ranges, int start, int end,
    int selectionStart, int selectionEnd)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.addGlyphsForRanges' has no cute function "
        "yet. Qt's 'void QQuickTextNodeEngine::addGlyphsForRanges(const "
        "QVarLengthArray<QTextLayout::FormatRange> &ranges, int start, int "
        "end, int selectionStart, int selectionEnd)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def addText(*__, **_) -> Never:
    """
    Qt's 'int QQuickTextNodeEngine::addText(const QTextBlock &block, const
    QTextCharFormat &charFormat, const QColor &textColor, const
    QVarLengthArray<QTextLayout::FormatRange> &colorChanges, int textPos, int
    fragmentEnd, int selectionStart, int selectionEnd)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.addText' has no cute function yet. Qt's 'int "
        "QQuickTextNodeEngine::addText(const QTextBlock &block, const "
        "QTextCharFormat &charFormat, const QColor &textColor, const "
        "QVarLengthArray<QTextLayout::FormatRange> &colorChanges, int "
        "textPos, int fragmentEnd, int selectionStart, int selectionEnd)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def addTextDecorations(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextNodeEngine::addTextDecorations(QSpan<const
    TextDecoration> textDecorations, qreal offset, qreal thickness)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.addTextDecorations' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextNodeEngine::addTextDecorations(QSpan<const "
        "TextDecoration> textDecorations, qreal offset, qreal thickness)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def addToSceneGraph(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextNodeEngine::addToSceneGraph(QSGInternalTextNode
    *parent, QSGInternalTextNode::RecycleBin *recycleBin,
    QQuickText::TextStyle style, const QColor &styleColor)': leans on
    'QQuickTextNodeEngine::mergeProcessedNodes(
    QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode*, 8ll>*,
    QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode*, 8ll>*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.addToSceneGraph' has no cute function yet. "
        "Qt's 'void "
        "QQuickTextNodeEngine::addToSceneGraph(QSGInternalTextNode *parent, "
        "QSGInternalTextNode::RecycleBin *recycleBin, QQuickText::TextStyle "
        "style, const QColor &styleColor)': leans on "
        "'QQuickTextNodeEngine::mergeProcessedNodes(QVarLengthArray<QQuickTe"
        "xtNodeEngine::BinaryTreeNode*, 8ll>*, "
        "QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode*, 8ll>*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def mergeFormats(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextNodeEngine::mergeFormats(QTextLayout *textLayout,
    QVarLengthArray<QTextLayout::FormatRange> *mergedFormats)': names
    'QVarLengthArray<QTextLayout::FormatRange>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.mergeFormats' has no cute function yet. Qt's "
        "'void QQuickTextNodeEngine::mergeFormats(QTextLayout *textLayout, "
        "QVarLengthArray<QTextLayout::FormatRange> *mergedFormats)': names "
        "'QVarLengthArray<QTextLayout::FormatRange>', which has no cute "
        "class yet.")

  @staticmethod
  def mergeProcessedNodes(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTextNodeEngine::mergeProcessedNodes(QVarLengthArray<BinaryTreeNode
    *, 8> *regularNodes, QVarLengthArray<BinaryTreeNode *, 8> *imageNodes)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: static assertion failed due to requirement
    'QtPrivate::type_dependent_false<QQuickTextNodeEngine::
    BinaryTreeNodeKey>()': The key type must have a qHash overload or a
    std::hash specialization.
    """
    raise NotImplementedError(
        "'QQuickTextNodeEngine.mergeProcessedNodes' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextNodeEngine::mergeProcessedNodes(QVarLengthArray<BinaryTre"
        "eNode *, 8> *regularNodes, QVarLengthArray<BinaryTreeNode *, 8> "
        "*imageNodes)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: static assertion "
        "failed due to requirement "
        "'QtPrivate::type_dependent_false<QQuickTextNodeEngine::BinaryTreeNo"
        "deKey>()': The key type must have a qHash overload or a std::hash "
        "specialization.")
