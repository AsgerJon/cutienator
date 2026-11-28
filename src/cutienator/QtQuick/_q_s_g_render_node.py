"""
QSGRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgrendernode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QRectF
  from ..QtGui import QMatrix4x4, QRegion, QRhiCommandBuffer
  from ..QtGui import QRhiRenderTarget
  from . import QSGClipNode

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRenderNode(QSGNode):
  """
  The cute side of Qt's QSGRenderNode: a plain Python object standing in
  front of one C++ QSGRenderNode.

  It is built on the cute 'QSGNode', as Qt's QSGRenderNode is built on Qt's
  QSGNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRenderNode that has a ritual and that Python can
  call so far, 12 names in all: 'changedStates', 'prepare', 'render',
  'releaseResources', 'flags', 'rect', 'projectionMatrix', 'matrix',
  'clipList', 'inheritedOpacity', 'renderTarget', 'commandBuffer'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRenderNode::~QSGRenderNode()': the destructor: Python never
    removes a C++ QSGRenderNode.

  What to expect
  --------------

  - The C++ QSGRenderNode is created at the first use, not by
    'QSGRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRenderNode.
  """

  #  The enums Qt writes inside QSGRenderNode, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RenderingFlag(CuteFlags):
    """
    The flags enum 'QSGRenderNode::RenderingFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QSGRenderNode::RenderingFlags'.
    """

    BoundedRectRendering = 0x1
    DepthAwareRendering = 0x2
    OpaqueRendering = 0x4
    NoExternalRendering = 0x8

  RenderingFlags = RenderingFlag

  class StateFlag(CuteFlags):
    """
    The flags enum 'QSGRenderNode::StateFlag' of Qt, with the 8 names Qt
    gives in it. Qt names the type of its combinations
    'QSGRenderNode::StateFlags'.
    """

    DepthState = 0x1
    StencilState = 0x2
    ScissorState = 0x4
    ColorState = 0x8
    BlendState = 0x10
    CullState = 0x20
    ViewportState = 0x40
    RenderTargetState = 0x80

  StateFlags = StateFlag

  #  The classes Qt writes inside QSGRenderNode, each a class in here as in
  #  C++.

  class RenderState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGRenderNode::RenderState: a plain Python object
    standing in front of one C++ QSGRenderNode::RenderState.

    What exists
    -----------

    Every function of Qt's QSGRenderNode::RenderState that has a ritual and
    that Python can call so far, 6 names in all: 'projectionMatrix',
    'scissorRect', 'scissorEnabled', 'stencilValue', 'stencilEnabled',
    'clipRegion'. None can be made from Python: one comes out of a function
    of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGRenderNode::RenderState::~RenderState()': the destructor:
      Python never removes a C++ QSGRenderNode::RenderState.
    - Qt's 'void *QSGRenderNode::RenderState::get(const char *state) const':
      gives 'void', which has no cute class yet.

    What to expect
    --------------

    - The C++ QSGRenderNode::RenderState is created at the first use, not by
      'QSGRenderNode::RenderState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QSGRenderNode::RenderState.
    - Each name of Qt's QSGRenderNode::RenderState that has no cute function
      yet, 'get', holds a function that raises 'NotImplementedError', and its
      docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGRenderNode::RenderState'

    #  A C++ QSGRenderNode::RenderState Python makes is of a C++ class of
    #  ours, in which Python can take functions over. This ritual hands one
    #  over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QSGRenderNode_RenderState'

    #  The functions Qt calls itself that QSGRenderNode::RenderState is the
    #  first to declare and that cannot be handed to Python yet, each as Qt
    #  declares it. A class of a program that writes one of them anew is
    #  refused, since Qt would never call what it wrote; see
    #  'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'get': (
            'void *QSGRenderNode::RenderState::get(const char *) const',
        ),
    }

    #  The functions Qt calls itself that QSGRenderNode::RenderState is the
    #  first to declare. A class of a program built on it can write one anew,
    #  and Qt then calls that. For each name: the key C++ knows the function
    #  by, what it gives, and what it takes.
    __virtual_functions__ = {
        'projectionMatrix': (
            ('_ZNK13QSGRenderNode11RenderState16projectionMatrixEv',
             ('address', 'address', 'QtGui:QMatrix4x4'),
             ()),
        ),
        'scissorRect': (
            ('_ZNK13QSGRenderNode11RenderState11scissorRectEv',
             ('address', 'value', 'QtCore:QRect'),
             ()),
        ),
        'scissorEnabled': (
            ('_ZNK13QSGRenderNode11RenderState14scissorEnabledEv',
             ('bool', 'number', ''),
             ()),
        ),
        'stencilValue': (
            ('_ZNK13QSGRenderNode11RenderState12stencilValueEv',
             ('int', 'number', ''),
             ()),
        ),
        'stencilEnabled': (
            ('_ZNK13QSGRenderNode11RenderState14stencilEnabledEv',
             ('bool', 'number', ''),
             ()),
        ),
        'clipRegion': (
            ('_ZNK13QSGRenderNode11RenderState10clipRegionEv',
             ('address', 'address', 'QtGui:QRegion'),
             ()),
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def projectionMatrix(self) -> Optional[QMatrix4x4]:
      """
      Calls Qt's 'const QMatrix4x4
      *QSGRenderNode::RenderState::projectionMatrix() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#projectionMatrix

      Returns
      -------

      Optional[QMatrix4x4]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  const QMatrix4x4 *QSGRenderNode::RenderState::projectionMatrix()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState16projectionMatrixEv',
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteAt(address)

    def scissorRect(self) -> QRect:
      """
      Calls Qt's 'QRect QSGRenderNode::RenderState::scissorRect() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#scissorRect

      Returns
      -------

      QRect
        A new cute QRect around the copy Qt gave back. Python owns it.
      """
      #  QRect QSGRenderNode::RenderState::scissorRect() const
      address = self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState11scissorRectEv',
      )
      from ..QtCore import QRect
      return QRect._cuteOwning(address)

    def scissorEnabled(self) -> bool:
      """
      Calls Qt's 'bool QSGRenderNode::RenderState::scissorEnabled() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#scissorEnabled
      """
      #  bool QSGRenderNode::RenderState::scissorEnabled() const
      return self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState14scissorEnabledEv',
      )

    def stencilValue(self) -> int:
      """
      Calls Qt's 'int QSGRenderNode::RenderState::stencilValue() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#stencilValue
      """
      #  int QSGRenderNode::RenderState::stencilValue() const
      return self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState12stencilValueEv',
      )

    def stencilEnabled(self) -> bool:
      """
      Calls Qt's 'bool QSGRenderNode::RenderState::stencilEnabled() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#stencilEnabled
      """
      #  bool QSGRenderNode::RenderState::stencilEnabled() const
      return self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState14stencilEnabledEv',
      )

    def clipRegion(self) -> Optional[QRegion]:
      """
      Calls Qt's 'const QRegion *QSGRenderNode::RenderState::clipRegion()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrendernode-renderstate.html#clipRegion

      Returns
      -------

      Optional[QRegion]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  const QRegion *QSGRenderNode::RenderState::clipRegion() const
      address = self.uglySide.call(
          'ritual_ZNK13QSGRenderNode11RenderState10clipRegionEv',
      )
      from ..QtGui import QRegion
      return QRegion._cuteAt(address)

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
    def get(*__, **_) -> Never:
      """
      Qt's 'void *QSGRenderNode::RenderState::get(const char *state) const':
      gives 'void', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QSGRenderNode.RenderState.get' has no cute function yet. Qt's "
          "'void *QSGRenderNode::RenderState::get(const char *state) "
          "const': gives 'void', which has no cute class yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRenderNode'

  #  A C++ QSGRenderNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRenderNode'

  #  The functions Qt calls itself that QSGRenderNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'changedStates': (
          ('_ZNK13QSGRenderNode13changedStatesEv',
           ('int', 'flags', 'QtQuick:QSGRenderNode.StateFlag'),
           ()),
      ),
      'prepare': (
          ('_ZN13QSGRenderNode7prepareEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'render': (
          ('_ZN13QSGRenderNode6renderEPKNS_11RenderStateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderNode.RenderState'),
           )),
      ),
      'releaseResources': (
          ('_ZN13QSGRenderNode16releaseResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'rect': (
          ('_ZNK13QSGRenderNode4rectEv',
           ('address', 'value', 'QtCore:QRectF'),
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

  def changedStates(self) -> StateFlags:
    """
    Calls Qt's 'StateFlags QSGRenderNode::changedStates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#changedStates

    Returns
    -------

    StateFlags
      The value standing for the combination Qt gave back.
    """
    #  StateFlags QSGRenderNode::changedStates() const
    ritual = 'ritual_ZNK13QSGRenderNode13changedStatesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderNode13changedStatesEv'
    return QSGRenderNode.StateFlags(self.uglySide.call(ritual))

  def flags(self) -> RenderingFlags:
    """
    Calls Qt's 'RenderingFlags QSGRenderNode::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#flags

    Returns
    -------

    RenderingFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderingFlags QSGRenderNode::flags() const
    ritual = 'ritual_ZNK13QSGRenderNode5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderNode5flagsEv'
    return QSGRenderNode.RenderingFlags(self.uglySide.call(ritual))

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGRenderNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGRenderNode::rect() const
    ritual = 'ritual_ZNK13QSGRenderNode4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderNode4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  def projectionMatrix(self) -> Optional[QMatrix4x4]:
    """
    Calls Qt's 'const QMatrix4x4 *QSGRenderNode::projectionMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendernode.html#projectionMatrix

    Returns
    -------

    Optional[QMatrix4x4]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMatrix4x4 *QSGRenderNode::projectionMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderNode16projectionMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteAt(address)

  @overload(int)
  def projectionMatrix(self, index: int) -> Optional[QMatrix4x4]:
    """
    Calls Qt's 'const QMatrix4x4 *QSGRenderNode::projectionMatrix(qsizetype
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendernode.html#projectionMatrix

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QMatrix4x4]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMatrix4x4 *QSGRenderNode::projectionMatrix(qsizetype index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderNode16projectionMatrixEx', index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteAt(address)

  def matrix(self) -> Optional[QMatrix4x4]:
    """
    Calls Qt's 'const QMatrix4x4 *QSGRenderNode::matrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#matrix

    Returns
    -------

    Optional[QMatrix4x4]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMatrix4x4 *QSGRenderNode::matrix() const
    address = self.uglySide.call('ritual_ZNK13QSGRenderNode6matrixEv')
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteAt(address)

  def clipList(self) -> Optional[QSGClipNode]:
    """
    Calls Qt's 'const QSGClipNode *QSGRenderNode::clipList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#clipList

    Returns
    -------

    Optional[QSGClipNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGClipNode *QSGRenderNode::clipList() const
    address = self.uglySide.call('ritual_ZNK13QSGRenderNode8clipListEv')
    from . import QSGClipNode
    return QSGClipNode._cuteAt(address)

  def inheritedOpacity(self) -> float:
    """
    Calls Qt's 'qreal QSGRenderNode::inheritedOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendernode.html#inheritedOpacity
    """
    #  qreal QSGRenderNode::inheritedOpacity() const
    return self.uglySide.call(
        'ritual_ZNK13QSGRenderNode16inheritedOpacityEv',
    )

  def renderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QSGRenderNode::renderTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#renderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QSGRenderNode::renderTarget() const
    address = self.uglySide.call('ritual_ZNK13QSGRenderNode12renderTargetEv')
    from ..QtGui import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def commandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer *QSGRenderNode::commandBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#commandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QSGRenderNode::commandBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderNode13commandBufferEv',
    )
    from ..QtGui import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

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
    Notes what was given, for Qt's 'QSGRenderNode::QSGRenderNode()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#QSGRenderNode
    """
    #  QSGRenderNode::QSGRenderNode()
    self._noteCreation(QSGRenderNode, lambda: Rituals.call(
        'ritual_ZN13QSGRenderNodeC1Ev',
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

  def prepare(self) -> None:
    """
    Calls Qt's 'void QSGRenderNode::prepare()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#prepare
    """
    #  void QSGRenderNode::prepare()
    ritual = 'ritual_ZN13QSGRenderNode7prepareEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSGRenderNode7prepareEv'
    self.uglySide.call(ritual)

  @overload(RenderState)
  @overload(NoneType)
  def render(self, state: Optional[RenderState]) -> None:
    """
    Calls Qt's 'void QSGRenderNode::render(const RenderState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendernode.html#render

    Parameters
    ----------

    state : Optional[RenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderNode::render(const RenderState *state)
    self.uglySide.call(
        'ritual_ZN13QSGRenderNode6renderEPKNS_11RenderStateE',
        self._addressOf(state),
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QSGRenderNode::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendernode.html#releaseResources
    """
    #  void QSGRenderNode::releaseResources()
    ritual = 'ritual_ZN13QSGRenderNode16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSGRenderNode16releaseResourcesEv'
    self.uglySide.call(ritual)
