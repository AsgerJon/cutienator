"""
QQuick3DRenderOutputProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3drenderoutputprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DRenderOutputProvider to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DObject, QQuick3DRenderPass
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DObject = WAIT['QQuick3DObject']
  QQuick3DRenderPass = WAIT['QQuick3DRenderPass']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRenderOutputProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DRenderOutputProvider: a plain Python object
  standing in front of one C++ QQuick3DRenderOutputProvider.

  What exists
  -----------

  Every function of Qt's QQuick3DRenderOutputProvider that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'textureSource', 'setTextureSource', 'renderPass', 'setRenderPass',
  'attachmentSelector', 'setAttachmentSelector', 'textureSourceChanged',
  'renderPassChanged', 'attachmentSelectorChanged', 'updateSpatialNode',
  'markAllDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRenderOutputProvider::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DRenderOutputProvider::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DRenderOutputProvider::markDirty(DirtyType type)':
    names the enum 'QQuick3DRenderOutputProvider::DirtyType', whose class
    cannot be named here.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRenderOutputProvider is created at the first use, not by
    'QQuick3DRenderOutputProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRenderOutputProvider.
  - Qt tells when it has removed the C++ QQuick3DRenderOutputProvider. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DRenderOutputProvider that has no cute function
    yet, 'markDirty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DRenderOutputProvider, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class AttachmentSelector(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRenderOutputProvider::AttachmentSelector' of Qt, with
    the 4 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Attachment0 = Kee[int](0)
    Attachment1 = Kee[int](1)
    Attachment2 = Kee[int](2)
    Attachment3 = Kee[int](3)

  class TextureSource(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRenderOutputProvider::TextureSource' of Qt, with the 7
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    NULL = Kee[int](0)
    UserPassTexture = Kee[int](1)
    AoTexture = Kee[int](2)
    DepthTexture = Kee[int](3)
    ScreenTexture = Kee[int](4)
    NormalTexture = Kee[int](5)
    MotionVectorTexture = Kee[int](6)

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
    Calls Qt's 'QString QQuick3DRenderOutputProvider::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#tr

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
    #  QString QQuick3DRenderOutputProvider::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuick3DRenderOutputProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRenderOutputProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRenderOutputProvider::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRenderOutputProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DRenderOutputProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureSource(self) -> TextureSource:
    """
    Calls Qt's 'TextureSource QQuick3DRenderOutputProvider::textureSource()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#textureSource

    Returns
    -------

    TextureSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureSource(number)'
      gives.
    """
    #  TextureSource QQuick3DRenderOutputProvider::textureSource() const
    return QQuick3DRenderOutputProvider.TextureSource(self.uglySide.call(
        'ritual_ZNK28QQuick3DRenderOutputProvider13textureSourceEv',
    ))

  def renderPass(self) -> Optional[QQuick3DRenderPass]:
    """
    Calls Qt's 'QQuick3DRenderPass
    *QQuick3DRenderOutputProvider::renderPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#renderPass

    Returns
    -------

    Optional[QQuick3DRenderPass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderPass *QQuick3DRenderOutputProvider::renderPass() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DRenderOutputProvider10renderPassEv',
    )
    from ..QtQuick3D import QQuick3DRenderPass
    return QQuick3DRenderPass._cuteAt(address)

  def attachmentSelector(self) -> AttachmentSelector:
    """
    Calls Qt's 'AttachmentSelector
    QQuick3DRenderOutputProvider::attachmentSelector() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html

    Returns
    -------

    AttachmentSelector
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AttachmentSelector(number)' gives.
    """
    #  AttachmentSelector QQuick3DRenderOutputProvider::attachmentSelector()
    #      const
    return QQuick3DRenderOutputProvider.AttachmentSelector(
        self.uglySide.call(
            'ritual_ZNK28QQuick3DRenderOutputProvider18attachmentSelectorEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TextureSource)
  def setTextureSource(self, newTextureSource: TextureSource) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderOutputProvider::setTextureSource(TextureSource
    newTextureSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#setTextureSource

    Parameters
    ----------

    newTextureSource : TextureSource
      Passed on as its number.
    """
    #  void QQuick3DRenderOutputProvider::setTextureSource(TextureSource
    #      newTextureSource)
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider16setTextureSourceENS_13Tex'
        'tureSourceE',
        newTextureSource.value,
    )

  @overload(QQuick3DRenderPass)
  @overload(NoneType)
  def setRenderPass(
      self,
      newRenderPass: Optional[QQuick3DRenderPass],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderOutputProvider::setRenderPass(QQuick3DRenderPass
    *newRenderPass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#setRenderPass

    Parameters
    ----------

    newRenderPass : Optional[QQuick3DRenderPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderOutputProvider::setRenderPass(QQuick3DRenderPass
    #      *newRenderPass)
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider13setRenderPassEP18QQuick3D'
        'RenderPass',
        self._addressOf(newRenderPass),
    )

  @overload(AttachmentSelector)
  def setAttachmentSelector(
      self,
      newAttachmentSelector: AttachmentSelector,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderOutputProvider::setAttachmentSelector(AttachmentSelector
    newAttachmentSelector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html

    Parameters
    ----------

    newAttachmentSelector : AttachmentSelector
      Passed on as its number.
    """
    #  void QQuick3DRenderOutputProvider::setAttachmentSelector(
    #      AttachmentSelector newAttachmentSelector)
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider21setAttachmentSelectorENS_'
        '18AttachmentSelectorE',
        newAttachmentSelector.value,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRenderOutputProvider::QQuick3DRenderOutputProvider(
    QQuick3DObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRenderOutputProvider::QQuick3DRenderOutputProvider(
    #      QQuick3DObject *parent)
    self._noteCreation(QQuick3DRenderOutputProvider, lambda: Rituals.call(
        'ritual_ZN28QQuick3DRenderOutputProviderC1EP14QQuick3DObject',
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

  def textureSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderOutputProvider::textureSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html
    """
    #  void QQuick3DRenderOutputProvider::textureSourceChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider20textureSourceChangedEv',
    )

  def renderPassChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderOutputProvider::renderPassChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html
    """
    #  void QQuick3DRenderOutputProvider::renderPassChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider17renderPassChangedEv',
    )

  def attachmentSelectorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderOutputProvider::attachmentSelectorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html
    """
    #  void QQuick3DRenderOutputProvider::attachmentSelectorChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DRenderOutputProvider25attachmentSelectorChanged'
        'Ev',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DRenderOutputProvider::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DRenderOutputProvider::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN28QQuick3DRenderOutputProvider17updateSpatialNodeEP21QSSG'
        'RenderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DRenderOutputProvider17updateSpatialNodeEP'
          '21QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderOutputProvider::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderoutputprovider.html#markAllDirty
    """
    #  void QQuick3DRenderOutputProvider::markAllDirty()
    ritual = 'ritual_ZN28QQuick3DRenderOutputProvider12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QQuick3DRenderOutputProvider12markAllDirtyEv'
    self.uglySide.call(ritual)

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderOutputProvider::markDirty(DirtyType type)':
    names the enum 'QQuick3DRenderOutputProvider::DirtyType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DRenderOutputProvider.markDirty' has no cute function yet. "
        "Qt's 'void QQuick3DRenderOutputProvider::markDirty(DirtyType "
        "type)': names the enum 'QQuick3DRenderOutputProvider::DirtyType', "
        "whose class cannot be named here.")
