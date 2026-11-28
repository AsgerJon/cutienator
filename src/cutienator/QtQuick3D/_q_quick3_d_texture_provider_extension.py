"""
QQuick3DTextureProviderExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/qquick3dtextureproviderextension.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject, QQuick3DRenderExtension

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DTextureProviderExtensionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DTextureProviderExtension(QQuick3DRenderExtension):
  """
  The cute side of Qt's QQuick3DTextureProviderExtension: a plain Python
  object standing in front of one C++ QQuick3DTextureProviderExtension.

  It is built on the cute 'QQuick3DRenderExtension', as Qt's
  QQuick3DTextureProviderExtension is built on Qt's QQuick3DRenderExtension,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DTextureProviderExtension that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'd_func', 'samplerHint', 'setSamplerHint', 'samplerHintChanged',
  'surfaceChanged', 'event', 'updateSpatialNode'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DTextureProviderExtension::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuick3DTextureProviderExtension::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DTextureProviderExtensionPrivate
    *QQuick3DTextureProviderExtension::d_func() const': takes in Python what
    'QQuick3DTextureProviderExtensionPrivate
    *QQuick3DTextureProviderExtension::d_func()' takes.
  - Qt's 'void QQuick3DTextureProviderExtension::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's
    'QQuick3DTextureProviderExtension::~QQuick3DTextureProviderExtension()':
    the destructor: Python never removes a C++
    QQuick3DTextureProviderExtension.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DTextureProviderExtension is created at the first use, not
    by 'QQuick3DTextureProviderExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DTextureProviderExtension.
  - Qt tells when it has removed the C++ QQuick3DTextureProviderExtension.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DTextureProviderExtension, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class SamplerHint(CuteNum, scoped=True):
    """
    The enum 'QQuick3DTextureProviderExtension::SamplerHint' of Qt, with the
    6 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Sampler2D = Kee[int](0)
    Sampler2DArray = Kee[int](1)
    Sampler3D = Kee[int](2)
    SamplerCube = Kee[int](3)
    SamplerCubeArray = Kee[int](4)
    SamplerBuffer = Kee[int](5)

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
    Calls Qt's 'QString QQuick3DTextureProviderExtension::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html#tr

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
    #  QString QQuick3DTextureProviderExtension::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuick3DTextureProviderExtension2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DTextureProviderExtension'

  #  A C++ QQuick3DTextureProviderExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DTextureProviderExtension'

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
    *QQuick3DTextureProviderExtension::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DTextureProviderExtension::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DTextureProviderExtension10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def samplerHint(self) -> SamplerHint:
    """
    Calls Qt's 'SamplerHint QQuick3DTextureProviderExtension::samplerHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html#samplerHint

    Returns
    -------

    SamplerHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SamplerHint(number)'
      gives.
    """
    #  SamplerHint QQuick3DTextureProviderExtension::samplerHint() const
    return QQuick3DTextureProviderExtension.SamplerHint(self.uglySide.call(
        'ritual_ZNK32QQuick3DTextureProviderExtension11samplerHintEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SamplerHint)
  def setSamplerHint(self, newSamplerHint: SamplerHint) -> None:
    """
    Calls Qt's 'void
    QQuick3DTextureProviderExtension::setSamplerHint(SamplerHint
    newSamplerHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html

    Parameters
    ----------

    newSamplerHint : SamplerHint
      Passed on as its number.
    """
    #  void QQuick3DTextureProviderExtension::setSamplerHint(SamplerHint
    #      newSamplerHint)
    self.uglySide.call(
        'ritual_ZN32QQuick3DTextureProviderExtension14setSamplerHintENS_11S'
        'amplerHintE',
        newSamplerHint.value,
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
    'QQuick3DTextureProviderExtension::QQuick3DTextureProviderExtension(
    QQuick3DObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DTextureProviderExtension::
    #      QQuick3DTextureProviderExtension(QQuick3DObject *parent)
    self._noteCreation(
        QQuick3DTextureProviderExtension, lambda: Rituals.call(
            'ritual_ZN32QQuick3DTextureProviderExtensionC1EP14QQuick3DObjec'
            't',
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

  def d_func(self) -> Optional[QQuick3DTextureProviderExtensionPrivate]:
    """
    Calls Qt's 'QQuick3DTextureProviderExtensionPrivate
    *QQuick3DTextureProviderExtension::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html#d_func

    Returns
    -------

    Optional[QQuick3DTextureProviderExtensionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTextureProviderExtensionPrivate
    #      *QQuick3DTextureProviderExtension::d_func()
    address = self.uglySide.call(
        'ritual_ZN32QQuick3DTextureProviderExtension6d_funcEv',
    )
    from . import QQuick3DTextureProviderExtensionPrivate
    return QQuick3DTextureProviderExtensionPrivate._cuteAt(address)

  def samplerHintChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureProviderExtension::samplerHintChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html
    """
    #  void QQuick3DTextureProviderExtension::samplerHintChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DTextureProviderExtension18samplerHintChangedEv',
    )

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureProviderExtension::surfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html
    """
    #  void QQuick3DTextureProviderExtension::surfaceChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DTextureProviderExtension14surfaceChangedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuick3DTextureProviderExtension::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DTextureProviderExtension::event(QEvent *event)
    ritual = 'ritual_ZN32QQuick3DTextureProviderExtension5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuick3DTextureProviderExtension5eventEP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DTextureProviderExtension::updateSpatialNode(
    QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtextureproviderextension.html

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
    #      *QQuick3DTextureProviderExtension::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN32QQuick3DTextureProviderExtension17updateSpatialNodeEP21'
        'QSSGRenderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuick3DTextureProviderExtension17updateSpatialNo'
          'deEP21QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
