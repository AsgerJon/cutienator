"""
QQuickTextEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextEditPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from . import QQuickImplicitSizeItemPrivate, QQuickTextEdit

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from ..QtGui import QContextMenuEvent, QFocusEvent
  from . import QQuickItem, QSGInternalTextNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextEditPrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickTextEditPrivate: a plain Python object standing
  in front of one C++ QQuickTextEditPrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickTextEditPrivate is built on Qt's QQuickImplicitSizeItemPrivate, and
  has everything that class has. Qt's QQuickTextEditPrivate is built on Qt's
  QAccessible::ActivationObserver as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickTextEditPrivate that has a ritual and that
  Python can call so far, 28 names in all: 'q_func', 'get', 'init',
  'resetInputMethod', 'updateDefaultTextOption', 'onDocumentStatusChanged',
  'determineHorizontalAlignment', 'setHAlign', 'mirrorChange',
  'transformChanged', 'getImplicitWidth', 'textDirection',
  'isLinkHoveredConnected', 'updateMouseCursorShape',
  'setNativeCursorEnabled', 'handleContextMenuEvent', 'handleFocusEvent',
  'createTextNode', 'effectiveInputMethodHints',
  'accessibilityActiveChanged', 'accessibleRole', 'padding', 'setTopPadding',
  'setLeftPadding', 'setRightPadding', 'setBottomPadding',
  'isImplicitResizeEnabled', 'setImplicitResizeEnabled'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextEdit *QQuickTextEditPrivate::q_func() const': takes
    in Python what 'QQuickTextEdit *QQuickTextEditPrivate::q_func()' takes.
  - Qt's 'QQuickTextEditPrivate::~QQuickTextEditPrivate()': the destructor:
    Python never removes a C++ QQuickTextEditPrivate.
  - Qt's 'void
    QQuickTextEditPrivate::addCurrentTextNodeToRoot(QQuickTextNodeEngine *a0,
    QSGTransformNode *a1, QSGInternalTextNode *a2, TextNodeIterator &a3, int
    startPos)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 33 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickTextEditPrivate is created at the first use, not by
    'QQuickTextEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextEditPrivate.
  - Each name of Qt's QQuickTextEditPrivate that has no cute function yet,
    'addCurrentTextNodeToRoot', 'relayoutDocument', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickTextEditPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class UpdateType(CuteNum):
    """
    The enum 'QQuickTextEditPrivate::UpdateType' of Qt, with the 4 names Qt
    gives in it.
    """

    UpdateNone = Kee[int](0)
    UpdateOnlyPreprocess = Kee[int](1)
    UpdatePaintNode = Kee[int](2)
    UpdateAll = Kee[int](3)

  #  The classes Qt writes inside QQuickTextEditPrivate, each a class in here
  #  as in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextEditPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickTextEditPrivate::ExtraData.

    C++ hands a QQuickTextEditPrivate::ExtraData around as a copy, so every
    C++ QQuickTextEditPrivate::ExtraData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickTextEditPrivate::ExtraData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextEditPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickTextEditPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextEditPrivate::ExtraData is created at the first use,
      not by 'QQuickTextEditPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextEditPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuickTextEditPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextEditPrivate::ExtraData'

    #  Qt's '~QQuickTextEditPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTextEditPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuickTextEditPrivate9ExtraDataD1Ev'

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
      'QQuickTextEditPrivate::ExtraData::ExtraData()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-extradata.html#ExtraData
      """
      #  QQuickTextEditPrivate::ExtraData::ExtraData()
      self._noteCreation(
          QQuickTextEditPrivate.ExtraData, lambda: Rituals.call(
              'ritual_ZN21QQuickTextEditPrivate9ExtraDataC1Ev',
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

  class Node(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextEditPrivate::Node: a plain Python object
    standing in front of one C++ QQuickTextEditPrivate::Node.

    C++ hands a QQuickTextEditPrivate::Node around as a copy, so every C++
    QQuickTextEditPrivate::Node behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQuickTextEditPrivate::Node that has a ritual and
    that Python can call so far, 6 names in all: 'textNode', 'moveStartPos',
    'startPos', 'setDirty', 'dirty', '__rlshift__'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextEditPrivate::Node::~Node()': the destructor: Python
      removes its C++ QQuickTextEditPrivate::Node by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickTextEditPrivate::Node is created at the first use, not by
      'QQuickTextEditPrivate::Node(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextEditPrivate::Node back gives a copy the
      ritual made for Python, in a new cute QQuickTextEditPrivate::Node.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDebug = WAIT['QDebug']
      QSGInternalTextNode = WAIT['QSGInternalTextNode']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextEditPrivate::Node'

    #  Qt's '~QQuickTextEditPrivate::Node()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickTextEditPrivate::Node behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuickTextEditPrivate4NodeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def textNode(self) -> Optional[QSGInternalTextNode]:
      """
      Calls Qt's 'QSGInternalTextNode
      *QQuickTextEditPrivate::Node::textNode() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#textNode

      Returns
      -------

      Optional[QSGInternalTextNode]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QSGInternalTextNode *QQuickTextEditPrivate::Node::textNode() const
      address = self.uglySide.call(
          'ritual_ZNK21QQuickTextEditPrivate4Node8textNodeEv',
      )
      from . import QSGInternalTextNode
      return QSGInternalTextNode._cuteAt(address)

    def startPos(self) -> int:
      """
      Calls Qt's 'int QQuickTextEditPrivate::Node::startPos() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#startPos
      """
      #  int QQuickTextEditPrivate::Node::startPos() const
      return self.uglySide.call(
          'ritual_ZNK21QQuickTextEditPrivate4Node8startPosEv',
      )

    def dirty(self) -> bool:
      """
      Calls Qt's 'bool QQuickTextEditPrivate::Node::dirty() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#dirty
      """
      #  bool QQuickTextEditPrivate::Node::dirty() const
      return self.uglySide.call(
          'ritual_ZNK21QQuickTextEditPrivate4Node5dirtyEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def setDirty(self) -> None:
      """
      Calls Qt's 'void QQuickTextEditPrivate::Node::setDirty()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#setDirty
      """
      #  void QQuickTextEditPrivate::Node::setDirty()
      self.uglySide.call('ritual_ZN21QQuickTextEditPrivate4Node8setDirtyEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QDebug)
    def __rlshift__(self, a0: QDebug) -> QDebug:
      """
      Calls Qt's 'QDebug operator<<(QDebug a0, const Node &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#operator<<

      Parameters
      ----------

      a0 : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug operator<<(QDebug a0, const Node &a1)
      address = Rituals.call(
          'ritual_Zls6QDebugRKN21QQuickTextEditPrivate4NodeE',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    @overload.fallback
    def __rlshift__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    @overload(int, QSGInternalTextNode)
    @overload(int, NoneType)
    def __init__(
        self,
        startPos: int,
        node: Optional[QSGInternalTextNode] = None,
    ) -> None:
      """
      Notes what was given, for Qt's 'QQuickTextEditPrivate::Node::Node(int
      startPos, QSGInternalTextNode *node)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#Node

      Parameters
      ----------

      startPos : int
        Passed on as it is.

      node : Optional[QSGInternalTextNode]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.
      """
      #  QQuickTextEditPrivate::Node::Node(int startPos, QSGInternalTextNode
      #      *node)
      self._noteCreation(QQuickTextEditPrivate.Node, lambda: Rituals.call(
          'ritual_ZN21QQuickTextEditPrivate4NodeC1EiP19QSGInternalTextNode',
          startPos, self._addressOf(node),
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

    @overload(int)
    def moveStartPos(self, delta: int) -> None:
      """
      Calls Qt's 'void QQuickTextEditPrivate::Node::moveStartPos(int delta)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktexteditprivate-node.html#moveStartPos

      Parameters
      ----------

      delta : int
        Passed on as it is.
      """
      #  void QQuickTextEditPrivate::Node::moveStartPos(int delta)
      self.uglySide.call(
          'ritual_ZN21QQuickTextEditPrivate4Node12moveStartPosEi', delta,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTextEdit)
  @overload(NoneType)
  def get(item: Optional[QQuickTextEdit]) -> Optional[QQuickTextEditPrivate]:
    """
    Calls Qt's 'QQuickTextEditPrivate
    *QQuickTextEditPrivate::get(QQuickTextEdit *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexteditprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickTextEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextEditPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextEditPrivate *QQuickTextEditPrivate::get(QQuickTextEdit
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickTextEditPrivate3getEP14QQuickTextEdit',
        CuteMixin._addressOf(item),
    )
    return QQuickTextEditPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextEditPrivate'

  #  A C++ QQuickTextEditPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextEditPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEditPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#getImplicitWidth
    """
    #  qreal QQuickTextEditPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK21QQuickTextEditPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTextEditPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def textDirection(self, text: str) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QQuickTextEditPrivate::textDirection(const QString &text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#textDirection

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickTextEditPrivate::textDirection(const QString
    #      &text) const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK21QQuickTextEditPrivate13textDirectionERK7QString', text,
    ))

  def effectiveInputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints
    QQuickTextEditPrivate::effectiveInputMethodHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints
    #      QQuickTextEditPrivate::effectiveInputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK21QQuickTextEditPrivate25effectiveInputMethodHintsEv',
    ))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickTextEditPrivate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickTextEditPrivate::accessibleRole() const
    ritual = 'ritual_ZNK21QQuickTextEditPrivate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTextEditPrivate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEditPrivate::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexteditprivate.html#padding
    """
    #  qreal QQuickTextEditPrivate::padding() const
    return self.uglySide.call('ritual_ZNK21QQuickTextEditPrivate7paddingEv')

  def isImplicitResizeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEditPrivate::isImplicitResizeEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#isImplicitResizeEnabled
    """
    #  bool QQuickTextEditPrivate::isImplicitResizeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTextEditPrivate23isImplicitResizeEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTextEdit.HAlignment)
  @overload(QQuickTextEdit.HAlignment, bool)
  def setHAlign(
      self,
      a0: QQuickTextEdit.HAlignment,
      forceAlign: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextEditPrivate::setHAlign(QQuickTextEdit::HAlignment a0, bool
    forceAlign)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setHAlign

    Parameters
    ----------

    a0 : QQuickTextEdit.HAlignment
      Passed on as its number.

    forceAlign : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQuickTextEditPrivate::setHAlign(QQuickTextEdit::HAlignment a0,
    #      bool forceAlign)
    return self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate9setHAlignEN14QQuickTextEdit10HAli'
        'gnmentEb',
        a0.value, forceAlign,
    )

  @overload(bool)
  def setNativeCursorEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setNativeCursorEnabled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setNativeCursorEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextEditPrivate::setNativeCursorEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate22setNativeCursorEnabledEb', a0,
    )

  @overload(float)
  @overload(float, bool)
  def setTopPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setTopPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setTopPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextEditPrivate::setTopPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate13setTopPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setLeftPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setLeftPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextEditPrivate::setLeftPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate14setLeftPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setRightPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setRightPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextEditPrivate::setRightPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate15setRightPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setBottomPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#setBottomPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextEditPrivate::setBottomPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate16setBottomPaddingEdb',
        value, reset,
    )

  @overload(bool)
  def setImplicitResizeEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::setImplicitResizeEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextEditPrivate::setImplicitResizeEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate24setImplicitResizeEnabledEb',
        enabled,
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
    'QQuickTextEditPrivate::QQuickTextEditPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#QQuickTextEditPrivate
    """
    #  QQuickTextEditPrivate::QQuickTextEditPrivate()
    self._noteCreation(QQuickTextEditPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuickTextEditPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTextEdit]:
    """
    Calls Qt's 'QQuickTextEdit *QQuickTextEditPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexteditprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextEdit *QQuickTextEditPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickTextEditPrivate6q_funcEv')
    return QQuickTextEdit._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexteditprivate.html#init
    """
    #  void QQuickTextEditPrivate::init()
    self.uglySide.call('ritual_ZN21QQuickTextEditPrivate4initEv')

  def resetInputMethod(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::resetInputMethod()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#resetInputMethod
    """
    #  void QQuickTextEditPrivate::resetInputMethod()
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate16resetInputMethodEv',
    )

  def updateDefaultTextOption(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::updateDefaultTextOption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#updateDefaultTextOption
    """
    #  void QQuickTextEditPrivate::updateDefaultTextOption()
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate23updateDefaultTextOptionEv',
    )

  def onDocumentStatusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::onDocumentStatusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#onDocumentStatusChanged
    """
    #  void QQuickTextEditPrivate::onDocumentStatusChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate23onDocumentStatusChangedEv',
    )

  def determineHorizontalAlignment(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEditPrivate::determineHorizontalAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html
    """
    #  bool QQuickTextEditPrivate::determineHorizontalAlignment()
    return self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate28determineHorizontalAlignmentEv',
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#mirrorChange
    """
    #  void QQuickTextEditPrivate::mirrorChange()
    ritual = 'ritual_ZN21QQuickTextEditPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickTextEditPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def transformChanged(self, transformedItem: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickTextEditPrivate::transformChanged(QQuickItem
    *transformedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#transformChanged

    Parameters
    ----------

    transformedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextEditPrivate::transformChanged(QQuickItem
    #      *transformedItem)
    ritual = (
        'ritual_ZN21QQuickTextEditPrivate16transformChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextEditPrivate16transformChangedEP10QQuick'
          'Item')
    return self.uglySide.call(ritual, self._addressOf(transformedItem))

  def isLinkHoveredConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEditPrivate::isLinkHoveredConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#isLinkHoveredConnected
    """
    #  bool QQuickTextEditPrivate::isLinkHoveredConnected()
    return self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate22isLinkHoveredConnectedEv',
    )

  def updateMouseCursorShape(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::updateMouseCursorShape()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#updateMouseCursorShape
    """
    #  void QQuickTextEditPrivate::updateMouseCursorShape()
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate22updateMouseCursorShapeEv',
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#handleContextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent
    #      *event)
    ritual = (
        'ritual_ZN21QQuickTextEditPrivate22handleContextMenuEventEP17QConte'
        'xtMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextEditPrivate22handleContextMenuEventEP17'
          'QContextMenuEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def handleFocusEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::handleFocusEvent(QFocusEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#handleFocusEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEditPrivate::handleFocusEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate16handleFocusEventEP11QFocusEvent',
        self._addressOf(event),
    )

  def createTextNode(self) -> Optional[QSGInternalTextNode]:
    """
    Calls Qt's 'QSGInternalTextNode
    *QQuickTextEditPrivate::createTextNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html#createTextNode

    Returns
    -------

    Optional[QSGInternalTextNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalTextNode *QQuickTextEditPrivate::createTextNode()
    address = self.uglySide.call(
        'ritual_ZN21QQuickTextEditPrivate14createTextNodeEv',
    )
    from . import QSGInternalTextNode
    return QSGInternalTextNode._cuteAt(address)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEditPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditprivate.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickTextEditPrivate::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN21QQuickTextEditPrivate26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextEditPrivate26accessibilityActiveChanged'
          'Eb')
    self.uglySide.call(ritual, active)

  @staticmethod
  def addCurrentTextNodeToRoot(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTextEditPrivate::addCurrentTextNodeToRoot(QQuickTextNodeEngine *a0,
    QSGTransformNode *a1, QSGInternalTextNode *a2, TextNodeIterator &a3, int
    startPos)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextEditPrivate.addCurrentTextNodeToRoot' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextEditPrivate::addCurrentTextNodeToRoot(QQuickTextNodeEngin"
        "e *a0, QSGTransformNode *a1, QSGInternalTextNode *a2, "
        "TextNodeIterator &a3, int startPos)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def relayoutDocument(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextEditPrivate::relayoutDocument()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickTextEditPrivate.relayoutDocument' has no cute function yet. "
        "Qt's 'void QQuickTextEditPrivate::relayoutDocument()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
