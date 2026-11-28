"""
Qt3DRender::Quick::QScene2D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/qscene2d.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScene2D(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::Quick::QScene2D: a plain Python object
  standing in front of one C++ Qt3DRender::Quick::QScene2D.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::Quick::QScene2D is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Quick::QScene2D that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject', 'tr', 'output',
  'renderPolicy', 'item', 'isMouseEnabled', 'addEntity', 'removeEntity',
  'setOutput', 'setRenderPolicy', 'setItem', 'setMouseEnabled',
  'outputChanged', 'renderPolicyChanged', 'itemChanged',
  'mouseEnabledChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Quick::QScene2D::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::Quick::QScene2D::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<Qt3DCore::QEntity *> Qt3DRender::Quick::QScene2D::entities()
    const': gives a type Python has no way to take yet.
  - Qt's 'const QScene2DPrivate *Qt3DRender::Quick::QScene2D::d_func()
    const': takes in Python what 'QScene2DPrivate
    *Qt3DRender::Quick::QScene2D::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::Quick::QScene2D is created at the first use, not by
    'Qt3DRender::Quick::QScene2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Quick::QScene2D.
  - Qt tells when it has removed the C++ Qt3DRender::Quick::QScene2D. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::Quick::QScene2D that has no cute function
    yet, 'entities', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Quick::QScene2D, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RenderPolicy(CuteNum):
    """
    The enum 'Qt3DRender::Quick::QScene2D::RenderPolicy' of Qt, with the 2
    names Qt gives in it.
    """

    Continuous = Kee[int](0)
    SingleShot = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::Quick::QScene2D::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#tr

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
    #  QString Qt3DRender::Quick::QScene2D::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Quick::QScene2D'

  #  A C++ Qt3DRender::Quick::QScene2D Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Quick_QScene2D'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::Quick::QScene2D::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::Quick::QScene2D::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick8QScene2D10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def output(self) -> Optional[Qt3DRender.QRenderTargetOutput]:
    """
    Calls Qt's 'Qt3DRender::QRenderTargetOutput
    *Qt3DRender::Quick::QScene2D::output() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#output

    Returns
    -------

    Optional[Qt3DRender.QRenderTargetOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QRenderTargetOutput *Qt3DRender::Quick::QScene2D::output()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick8QScene2D6outputEv',
    )
    return Qt3DRender.QRenderTargetOutput._cuteAt(address)

  def renderPolicy(self) -> RenderPolicy:
    """
    Calls Qt's 'QScene2D::RenderPolicy
    Qt3DRender::Quick::QScene2D::renderPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#renderPolicy

    Returns
    -------

    RenderPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderPolicy(number)'
      gives.
    """
    #  QScene2D::RenderPolicy Qt3DRender::Quick::QScene2D::renderPolicy()
    #      const
    return QScene2D.RenderPolicy(self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick8QScene2D12renderPolicyEv',
    ))

  def item(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *Qt3DRender::Quick::QScene2D::item() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#item

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *Qt3DRender::Quick::QScene2D::item() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick8QScene2D4itemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def isMouseEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::QScene2D::isMouseEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#isMouseEnabled
    """
    #  bool Qt3DRender::Quick::QScene2D::isMouseEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick8QScene2D14isMouseEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QRenderTargetOutput'])
  @overload(NoneType)
  def setOutput(
      self,
      output: Optional[Qt3DRender.QRenderTargetOutput],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::QScene2D::setOutput(Qt3DRender::QRenderTargetOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#setOutput

    Parameters
    ----------

    output : Optional[Qt3DRender.QRenderTargetOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::setOutput(Qt3DRender::
    #      QRenderTargetOutput *output)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D9setOutputEPNS_19QRenderTarget'
        'OutputE',
        self._addressOf(output),
    )

  @overload(RenderPolicy)
  def setRenderPolicy(self, policy: RenderPolicy) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::QScene2D::setRenderPolicy(QScene2D::RenderPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#setRenderPolicy

    Parameters
    ----------

    policy : RenderPolicy
      Passed on as its number.
    """
    #  void Qt3DRender::Quick::QScene2D::setRenderPolicy(QScene2D::
    #      RenderPolicy policy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D15setRenderPolicyENS1_12Render'
        'PolicyE',
        policy.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::setItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#setItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::setItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D7setItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(bool)
  def setMouseEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::setMouseEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#setMouseEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Quick::QScene2D::setMouseEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D15setMouseEnabledEb', enabled,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Quick::QScene2D::QScene2D(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#QScene2D

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::Quick::QScene2D::QScene2D(Qt3DCore::QNode *parent)
    self._noteCreation(QScene2D, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2DC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def addEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::addEntity(Qt3DCore::QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#addEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::addEntity(Qt3DCore::QEntity *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D9addEntityEPN8Qt3DCore7QEntity'
        'E',
        self._addressOf(entity),
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def removeEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::QScene2D::removeEntity(Qt3DCore::QEntity *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#removeEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::removeEntity(Qt3DCore::QEntity
    #      *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D12removeEntityEPN8Qt3DCore7QEn'
        'tityE',
        self._addressOf(entity),
    )

  @overload(WAIT['Qt3DRender.QRenderTargetOutput'])
  @overload(NoneType)
  def outputChanged(
      self,
      output: Optional[Qt3DRender.QRenderTargetOutput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::outputChanged(Qt3DRender::
    QRenderTargetOutput *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#outputChanged

    Parameters
    ----------

    output : Optional[Qt3DRender.QRenderTargetOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::outputChanged(Qt3DRender::
    #      QRenderTargetOutput *output)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D13outputChangedEPNS_19QRenderT'
        'argetOutputE',
        self._addressOf(output),
    )

  @overload(RenderPolicy)
  def renderPolicyChanged(self, policy: RenderPolicy) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::QScene2D::renderPolicyChanged(QScene2D::RenderPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#renderPolicyChanged

    Parameters
    ----------

    policy : RenderPolicy
      Passed on as its number.
    """
    #  void Qt3DRender::Quick::QScene2D::renderPolicyChanged(QScene2D::
    #      RenderPolicy policy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D19renderPolicyChangedENS1_12Re'
        'nderPolicyE',
        policy.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::itemChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#itemChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::QScene2D::itemChanged(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D11itemChangedEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(bool)
  def mouseEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::QScene2D::mouseEnabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#mouseEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Quick::QScene2D::mouseEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D19mouseEnabledChangedEb',
        enabled,
    )

  def d_func(self) -> Optional[Qt3DRender.Quick.QScene2DPrivate]:
    """
    Calls Qt's 'QScene2DPrivate *Qt3DRender::Quick::QScene2D::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2d.html#d_func

    Returns
    -------

    Optional[Qt3DRender.Quick.QScene2DPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScene2DPrivate *Qt3DRender::Quick::QScene2D::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick8QScene2D6d_funcEv',
    )
    return Qt3DRender.Quick.QScene2DPrivate._cuteAt(address)

  @staticmethod
  def entities(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QEntity *> Qt3DRender::Quick::QScene2D::entities()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Quick.QScene2D.entities' has no cute function yet. "
        "Qt's 'QList<Qt3DCore::QEntity *> "
        "Qt3DRender::Quick::QScene2D::entities() const': gives a type "
        "Python has no way to take yet.")
