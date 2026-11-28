"""
Qt3DRender::QRenderSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendersettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderSettings(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QRenderSettings: a plain Python object
  standing in front of one C++ Qt3DRender::QRenderSettings.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QRenderSettings is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderSettings that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'renderCapabilities', 'pickingSettings', 'activeFrameGraph',
  'renderPolicy', 'setActiveFrameGraph', 'setRenderPolicy',
  'activeFrameGraphChanged', 'renderPolicyChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderSettings::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderSettings::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderSettings::~QRenderSettings()': the destructor:
    Python never removes a C++ Qt3DRender::QRenderSettings.
  - Qt's 'const QRenderSettingsPrivate *Qt3DRender::QRenderSettings::d_func()
    const': takes in Python what 'QRenderSettingsPrivate
    *Qt3DRender::QRenderSettings::d_func()' takes.
  - Qt's 'Qt3DRender::QRenderSettings::QRenderSettings(QRenderSettingsPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderSettings is created at the first use, not by
    'Qt3DRender::QRenderSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderSettings.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderSettings. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QRenderSettings, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RenderPolicy(CuteNum):
    """
    The enum 'Qt3DRender::QRenderSettings::RenderPolicy' of Qt, with the 2
    names Qt gives in it.
    """

    OnDemand = Kee[int](0)
    Always = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QRenderSettings::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#tr

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
    #  QString Qt3DRender::QRenderSettings::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender15QRenderSettings2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderSettings'

  #  A C++ Qt3DRender::QRenderSettings Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QRenderSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QRenderSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeFrameGraph(self) -> Optional[Qt3DRender.QFrameGraphNode]:
    """
    Calls Qt's 'QFrameGraphNode
    *Qt3DRender::QRenderSettings::activeFrameGraph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#activeFrameGraph

    Returns
    -------

    Optional[Qt3DRender.QFrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFrameGraphNode *Qt3DRender::QRenderSettings::activeFrameGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QRenderSettings16activeFrameGraphEv',
    )
    return Qt3DRender.QFrameGraphNode._cuteAt(address)

  def renderPolicy(self) -> RenderPolicy:
    """
    Calls Qt's 'RenderPolicy Qt3DRender::QRenderSettings::renderPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#renderPolicy

    Returns
    -------

    RenderPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderPolicy(number)'
      gives.
    """
    #  RenderPolicy Qt3DRender::QRenderSettings::renderPolicy() const
    return QRenderSettings.RenderPolicy(self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QRenderSettings12renderPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QFrameGraphNode'])
  @overload(NoneType)
  def setActiveFrameGraph(
      self,
      activeFrameGraph: Optional[Qt3DRender.QFrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettings::setActiveFrameGraph(QFrameGraphNode
    *activeFrameGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html

    Parameters
    ----------

    activeFrameGraph : Optional[Qt3DRender.QFrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderSettings::setActiveFrameGraph(QFrameGraphNode
    #      *activeFrameGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings19setActiveFrameGraphEPNS_15'
        'QFrameGraphNodeE',
        self._addressOf(activeFrameGraph),
    )

  @overload(RenderPolicy)
  def setRenderPolicy(self, renderPolicy: RenderPolicy) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettings::setRenderPolicy(RenderPolicy renderPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#setRenderPolicy

    Parameters
    ----------

    renderPolicy : RenderPolicy
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderSettings::setRenderPolicy(RenderPolicy
    #      renderPolicy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings15setRenderPolicyENS0_12Rend'
        'erPolicyE',
        renderPolicy.value,
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
    'Qt3DRender::QRenderSettings::QRenderSettings(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#QRenderSettings

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderSettings::QRenderSettings(Qt3DCore::QNode *parent)
    self._noteCreation(QRenderSettings, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender15QRenderSettingsC1EPN8Qt3DCore5QNodeE',
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

  def renderCapabilities(self) -> Optional[Qt3DRender.QRenderCapabilities]:
    """
    Calls Qt's 'QRenderCapabilities
    *Qt3DRender::QRenderSettings::renderCapabilities()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#renderCapabilities

    Returns
    -------

    Optional[Qt3DRender.QRenderCapabilities]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCapabilities *Qt3DRender::QRenderSettings::renderCapabilities()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings18renderCapabilitiesEv',
    )
    return Qt3DRender.QRenderCapabilities._cuteAt(address)

  def pickingSettings(self) -> Optional[Qt3DRender.QPickingSettings]:
    """
    Calls Qt's 'QPickingSettings
    *Qt3DRender::QRenderSettings::pickingSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#pickingSettings

    Returns
    -------

    Optional[Qt3DRender.QPickingSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPickingSettings *Qt3DRender::QRenderSettings::pickingSettings()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings15pickingSettingsEv',
    )
    return Qt3DRender.QPickingSettings._cuteAt(address)

  @overload(WAIT['Qt3DRender.QFrameGraphNode'])
  @overload(NoneType)
  def activeFrameGraphChanged(
      self,
      activeFrameGraph: Optional[Qt3DRender.QFrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettings::activeFrameGraphChanged(QFrameGraphNode
    *activeFrameGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html

    Parameters
    ----------

    activeFrameGraph : Optional[Qt3DRender.QFrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderSettings::activeFrameGraphChanged(
    #      QFrameGraphNode *activeFrameGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings23activeFrameGraphChangedEPN'
        'S_15QFrameGraphNodeE',
        self._addressOf(activeFrameGraph),
    )

  @overload(RenderPolicy)
  def renderPolicyChanged(self, renderPolicy: RenderPolicy) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettings::renderPolicyChanged(RenderPolicy
    renderPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html

    Parameters
    ----------

    renderPolicy : RenderPolicy
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderSettings::renderPolicyChanged(RenderPolicy
    #      renderPolicy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings19renderPolicyChangedENS0_12'
        'RenderPolicyE',
        renderPolicy.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QRenderSettingsPrivate]:
    """
    Calls Qt's 'QRenderSettingsPrivate
    *Qt3DRender::QRenderSettings::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettings.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderSettingsPrivate *Qt3DRender::QRenderSettings::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender15QRenderSettings6d_funcEv',
    )
    return Qt3DRender.QRenderSettingsPrivate._cuteAt(address)
