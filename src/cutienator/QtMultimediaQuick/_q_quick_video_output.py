"""
QQuickVideoOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickvideooutput_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVideoOutput to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtMultimedia import QVideoFrame, QVideoSink
  from ..QtQuick import QSGNode
  from . import QSGVideoNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSGVideoNode = WAIT['QSGVideoNode']
  QSize = WAIT['QSize']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickVideoOutput(QQuickItem):
  """
  The cute side of Qt's QQuickVideoOutput: a plain Python object standing in
  front of one C++ QQuickVideoOutput.

  It is built on the cute 'QQuickItem', as Qt's QQuickVideoOutput is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickVideoOutput that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'videoSink',
  'fillMode', 'setFillMode', 'orientation', 'setOrientation', 'mirrored',
  'setMirrored', 'sourceRect', 'contentRect', 'endOfStreamPolicy',
  'setEndOfStreamPolicy', 'clearOutput', 'sourceChanged', 'fillModeChanged',
  'orientationChanged', 'mirroredChanged', 'sourceRectChanged',
  'contentRectChanged', 'endOfStreamPolicyChanged', 'updatePaintNode',
  'itemChange', 'geometryChange', 'releaseResources', 'nativeSize',
  'updateGeometry', 'adjustedViewport', 'setFrame', 'initRhiForSink',
  'updateHdr', 'disconnectWindowConnections', '_q_newFrame',
  '_q_updateGeometry'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickVideoOutput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickVideoOutput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickVideoOutput::~QQuickVideoOutput()': the destructor: Python
    never removes a C++ QQuickVideoOutput.
  - Qt's 'void
    QQuickVideoOutput::setSignalBackoff(std::optional<std::chrono::
    nanoseconds> a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 44 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QQuickVideoOutput is created at the first use, not by
    'QQuickVideoOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickVideoOutput.
  - Qt tells when it has removed the C++ QQuickVideoOutput. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickVideoOutput that has no cute function yet,
    'makeGuardedCall', 'setSignalBackoff', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickVideoOutput, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class EndOfStreamPolicy(CuteNum):
    """
    The enum 'QQuickVideoOutput::EndOfStreamPolicy' of Qt, with the 2 names
    Qt gives in it.
    """

    ClearOutput = Kee[int](0)
    KeepLastFrame = Kee[int](1)

  class FillMode(CuteNum):
    """
    The enum 'QQuickVideoOutput::FillMode' of Qt, with the 3 names Qt gives
    in it.
    """

    Stretch = Kee[int](0)
    PreserveAspectFit = Kee[int](1)
    PreserveAspectCrop = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickVideoOutput::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickVideoOutput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickVideoOutput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVideoOutput'

  #  A C++ QQuickVideoOutput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickVideoOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickVideoOutput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickVideoOutput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QQuickVideoOutput::videoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QQuickVideoOutput::videoSink() const
    address = self.uglySide.call('ritual_ZNK17QQuickVideoOutput9videoSinkEv')
    from ..QtMultimedia import QVideoSink
    return QVideoSink._cuteAt(address)

  def fillMode(self) -> FillMode:
    """
    Calls Qt's 'FillMode QQuickVideoOutput::fillMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#fillMode

    Returns
    -------

    FillMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FillMode(number)' gives.
    """
    #  FillMode QQuickVideoOutput::fillMode() const
    return QQuickVideoOutput.FillMode(self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput8fillModeEv',
    ))

  def orientation(self) -> int:
    """
    Calls Qt's 'int QQuickVideoOutput::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#orientation
    """
    #  int QQuickVideoOutput::orientation() const
    return self.uglySide.call('ritual_ZNK17QQuickVideoOutput11orientationEv')

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickVideoOutput::mirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#mirrored
    """
    #  bool QQuickVideoOutput::mirrored() const
    return self.uglySide.call('ritual_ZNK17QQuickVideoOutput8mirroredEv')

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickVideoOutput::sourceRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickVideoOutput::sourceRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput10sourceRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def contentRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickVideoOutput::contentRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#contentRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickVideoOutput::contentRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput11contentRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def endOfStreamPolicy(self) -> EndOfStreamPolicy:
    """
    Calls Qt's 'EndOfStreamPolicy QQuickVideoOutput::endOfStreamPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#endOfStreamPolicy

    Returns
    -------

    EndOfStreamPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'EndOfStreamPolicy(number)' gives.
    """
    #  EndOfStreamPolicy QQuickVideoOutput::endOfStreamPolicy() const
    return QQuickVideoOutput.EndOfStreamPolicy(self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput17endOfStreamPolicyEv',
    ))

  def nativeSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickVideoOutput::nativeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#nativeSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickVideoOutput::nativeSize() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput10nativeSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def adjustedViewport(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickVideoOutput::adjustedViewport() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#adjustedViewport

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickVideoOutput::adjustedViewport() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVideoOutput16adjustedViewportEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FillMode)
  def setFillMode(self, mode: FillMode) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::setFillMode(FillMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#setFillMode

    Parameters
    ----------

    mode : FillMode
      Passed on as its number.
    """
    #  void QQuickVideoOutput::setFillMode(FillMode mode)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput11setFillModeENS_8FillModeE',
        mode.value,
    )

  @overload(int)
  def setOrientation(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::setOrientation(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#setOrientation

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickVideoOutput::setOrientation(int a0)
    self.uglySide.call('ritual_ZN17QQuickVideoOutput14setOrientationEi', a0)

  @overload(bool)
  def setMirrored(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::setMirrored(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#setMirrored

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickVideoOutput::setMirrored(bool a0)
    self.uglySide.call('ritual_ZN17QQuickVideoOutput11setMirroredEb', a0)

  @overload(EndOfStreamPolicy)
  def setEndOfStreamPolicy(self, policy: EndOfStreamPolicy) -> None:
    """
    Calls Qt's 'void
    QQuickVideoOutput::setEndOfStreamPolicy(EndOfStreamPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#setEndOfStreamPolicy

    Parameters
    ----------

    policy : EndOfStreamPolicy
      Passed on as its number.
    """
    #  void QQuickVideoOutput::setEndOfStreamPolicy(EndOfStreamPolicy policy)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput20setEndOfStreamPolicyENS_17EndOfStrea'
        'mPolicyE',
        policy.value,
    )

  @overload(QVideoFrame)
  def setFrame(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::setFrame(const QVideoFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#setFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QQuickVideoOutput::setFrame(const QVideoFrame &frame)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput8setFrameERK11QVideoFrame',
        self._valueOf(frame),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickVideoOutput::QQuickVideoOutput(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#QQuickVideoOutput

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickVideoOutput::QQuickVideoOutput(QQuickItem *parent)
    self._noteCreation(QQuickVideoOutput, lambda: Rituals.call(
        'ritual_ZN17QQuickVideoOutputC1EP10QQuickItem',
        self._addressOf(parent),
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

  def clearOutput(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::clearOutput()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#clearOutput
    """
    #  void QQuickVideoOutput::clearOutput()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput11clearOutputEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#sourceChanged
    """
    #  void QQuickVideoOutput::sourceChanged()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput13sourceChangedEv')

  @overload(FillMode)
  def fillModeChanged(self, a0: FillMode) -> None:
    """
    Calls Qt's 'void
    QQuickVideoOutput::fillModeChanged(QQuickVideoOutput::FillMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#fillModeChanged

    Parameters
    ----------

    a0 : FillMode
      Passed on as its number.
    """
    #  void QQuickVideoOutput::fillModeChanged(QQuickVideoOutput::FillMode
    #      a0)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput15fillModeChangedENS_8FillModeE',
        a0.value,
    )

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#orientationChanged
    """
    #  void QQuickVideoOutput::orientationChanged()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput18orientationChangedEv')

  def mirroredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::mirroredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#mirroredChanged
    """
    #  void QQuickVideoOutput::mirroredChanged()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput15mirroredChangedEv')

  def sourceRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::sourceRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#sourceRectChanged
    """
    #  void QQuickVideoOutput::sourceRectChanged()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput17sourceRectChangedEv')

  def contentRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::contentRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#contentRectChanged
    """
    #  void QQuickVideoOutput::contentRectChanged()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput18contentRectChangedEv')

  @overload(EndOfStreamPolicy)
  def endOfStreamPolicyChanged(self, a0: EndOfStreamPolicy) -> None:
    """
    Calls Qt's 'void
    QQuickVideoOutput::endOfStreamPolicyChanged(QQuickVideoOutput::
    EndOfStreamPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#endOfStreamPolicyChanged

    Parameters
    ----------

    a0 : EndOfStreamPolicy
      Passed on as its number.
    """
    #  void QQuickVideoOutput::endOfStreamPolicyChanged(QQuickVideoOutput::
    #      EndOfStreamPolicy a0)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput24endOfStreamPolicyChangedENS_17EndOfS'
        'treamPolicyE',
        a0.value,
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickVideoOutput::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickVideoOutput::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN17QQuickVideoOutput15updatePaintNodeEP7QSGNodePN10QQuickI'
        'tem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickVideoOutput15updatePaintNodeEP7QSGNodePN10Q'
          'QuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      changeData: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::itemChange(ItemChange change, const
    ItemChangeData &changeData)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    changeData : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickVideoOutput::itemChange(ItemChange change, const
    #      ItemChangeData &changeData)
    ritual = (
        'ritual_ZN17QQuickVideoOutput10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickVideoOutput10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(changeData))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickVideoOutput::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN17QQuickVideoOutput14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickVideoOutput14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#releaseResources
    """
    #  void QQuickVideoOutput::releaseResources()
    ritual = 'ritual_ZN17QQuickVideoOutput16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickVideoOutput16releaseResourcesEv'
    self.uglySide.call(ritual)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#updateGeometry
    """
    #  void QQuickVideoOutput::updateGeometry()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput14updateGeometryEv')

  def initRhiForSink(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::initRhiForSink()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#initRhiForSink
    """
    #  void QQuickVideoOutput::initRhiForSink()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput14initRhiForSinkEv')

  @overload(QSGVideoNode)
  @overload(NoneType)
  def updateHdr(self, videoNode: Optional[QSGVideoNode]) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::updateHdr(QSGVideoNode *videoNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#updateHdr

    Parameters
    ----------

    videoNode : Optional[QSGVideoNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickVideoOutput::updateHdr(QSGVideoNode *videoNode)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput9updateHdrEP12QSGVideoNode',
        self._addressOf(videoNode),
    )

  def disconnectWindowConnections(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::disconnectWindowConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#disconnectWindowConnections
    """
    #  void QQuickVideoOutput::disconnectWindowConnections()
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput27disconnectWindowConnectionsEv',
    )

  @overload(QSize)
  def _q_newFrame(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::_q_newFrame(QSize a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvideooutput.html#_q_newFrame

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickVideoOutput::_q_newFrame(QSize a0)
    self.uglySide.call(
        'ritual_ZN17QQuickVideoOutput11_q_newFrameE5QSize',
        self._valueOf(a0),
    )

  def _q_updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickVideoOutput::_q_updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvideooutput.html#_q_updateGeometry
    """
    #  void QQuickVideoOutput::_q_updateGeometry()
    self.uglySide.call('ritual_ZN17QQuickVideoOutput17_q_updateGeometryEv')

  @staticmethod
  def makeGuardedCall(*__, **_) -> Never:
    """
    Qt's 'QQuickVideoOutput::makeGuardedCall': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickVideoOutput.makeGuardedCall' has no cute function yet. Qt's "
        "'QQuickVideoOutput::makeGuardedCall': a template: a pattern and no "
        "single function.")

  @staticmethod
  def setSignalBackoff(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickVideoOutput::setSignalBackoff(std::optional<std::chrono::
    nanoseconds> a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickVideoOutput.setSignalBackoff' has no cute function yet. "
        "Qt's 'void "
        "QQuickVideoOutput::setSignalBackoff(std::optional<std::chrono::nano"
        "seconds> a0)': takes a type Python has no way to hand over yet.")
