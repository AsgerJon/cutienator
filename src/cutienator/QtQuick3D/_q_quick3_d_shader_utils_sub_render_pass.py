"""
QQuick3DShaderUtilsSubRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsSubRenderPass to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DObject, QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand, QSSGRenderGraphObject
  from . import QQuick3DRenderPass, QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DRenderPass = WAIT['QQuick3DRenderPass']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsSubRenderPass(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsSubRenderPass: a plain Python
  object standing in front of one C++ QQuick3DShaderUtilsSubRenderPass.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsSubRenderPass is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsSubRenderPass that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'renderPass', 'setRenderPass', 'cloneCommand', 'renderPassChanged',
  'updateSpatialNode', 'itemChange', 'updateSceneManager'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsSubRenderPass::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuick3DShaderUtilsSubRenderPass::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuick3DShaderUtilsSubRenderPass::~QQuick3DShaderUtilsSubRenderPass()':
    the destructor: Python never removes a C++
    QQuick3DShaderUtilsSubRenderPass.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsSubRenderPass is created at the first use, not
    by 'QQuick3DShaderUtilsSubRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsSubRenderPass.
  - Qt tells when it has removed the C++ QQuick3DShaderUtilsSubRenderPass.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuick3DShaderUtilsSubRenderPass::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html#tr

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
    #  QString QQuick3DShaderUtilsSubRenderPass::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsSubRenderPass'

  #  A C++ QQuick3DShaderUtilsSubRenderPass Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsSubRenderPass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DShaderUtilsSubRenderPass::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsSubRenderPass::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DShaderUtilsSubRenderPass10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderPass(self) -> Optional[QQuick3DRenderPass]:
    """
    Calls Qt's 'QQuick3DRenderPass
    *QQuick3DShaderUtilsSubRenderPass::renderPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html#renderPass

    Returns
    -------

    Optional[QQuick3DRenderPass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderPass *QQuick3DShaderUtilsSubRenderPass::renderPass()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DShaderUtilsSubRenderPass10renderPassEv',
    )
    from . import QQuick3DRenderPass
    return QQuick3DRenderPass._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DRenderPass)
  @overload(NoneType)
  def setRenderPass(
      self,
      newRenderPass: Optional[QQuick3DRenderPass],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsSubRenderPass::setRenderPass(QQuick3DRenderPass
    *newRenderPass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html

    Parameters
    ----------

    newRenderPass : Optional[QQuick3DRenderPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DShaderUtilsSubRenderPass::setRenderPass(QQuick3DRenderPass
    #      *newRenderPass)
    self.uglySide.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass13setRenderPassEP18QQui'
        'ck3DRenderPass',
        self._addressOf(newRenderPass),
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
    'QQuick3DShaderUtilsSubRenderPass::QQuick3DShaderUtilsSubRenderPass()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html
    """
    #  QQuick3DShaderUtilsSubRenderPass::QQuick3DShaderUtilsSubRenderPass()
    self._noteCreation(
        QQuick3DShaderUtilsSubRenderPass, lambda: Rituals.call(
            'ritual_ZN32QQuick3DShaderUtilsSubRenderPassC1Ev',
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

  def cloneCommand(self) -> Optional[QSSGCommand]:
    """
    Calls Qt's 'QSSGCommand
    *QQuick3DShaderUtilsSubRenderPass::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html#cloneCommand

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsSubRenderPass::cloneCommand()
    ritual = 'ritual_ZN32QQuick3DShaderUtilsSubRenderPass12cloneCommandEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuick3DShaderUtilsSubRenderPass12cloneCommandEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)

  def renderPassChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsSubRenderPass::renderPassChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html
    """
    #  void QQuick3DShaderUtilsSubRenderPass::renderPassChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass17renderPassChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DShaderUtilsSubRenderPass::updateSpatialNode(
    QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html

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
    #      *QQuick3DShaderUtilsSubRenderPass::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    address = self.uglySide.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass17updateSpatialNodeEP21'
        'QSSGRenderGraphObject',
        self._addressOf(node),
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      change: QQuick3DObject.ItemChange,
      value: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsSubRenderPass::itemChange(ItemChange
    change, const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html#itemChange

    Parameters
    ----------

    change : QQuick3DObject.ItemChange
      Passed on as its number.

    value : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsSubRenderPass::itemChange(ItemChange change,
    #      const ItemChangeData &value)
    self.uglySide.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass10itemChangeEN14QQuick3'
        'DObject10ItemChangeERKNS0_14ItemChangeDataE',
        change.value, self._valueOf(value),
    )

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsSubRenderPass::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilssubrenderpass.html

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DShaderUtilsSubRenderPass::updateSceneManager(
    #      QQuick3DSceneManager *sceneManager)
    self.uglySide.call(
        'ritual_ZN32QQuick3DShaderUtilsSubRenderPass18updateSceneManagerEP2'
        '0QQuick3DSceneManager',
        self._addressOf(sceneManager),
    )
