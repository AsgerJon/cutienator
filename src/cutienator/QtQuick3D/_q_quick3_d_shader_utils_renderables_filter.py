"""
QQuick3DShaderUtilsRenderablesFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsRenderablesFilter to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags
from ..occult import Rituals
from . import QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsRenderablesFilter(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsRenderablesFilter: a plain Python
  object standing in front of one C++ QQuick3DShaderUtilsRenderablesFilter.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsRenderablesFilter is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsRenderablesFilter that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'renderableTypes', 'setRenderableTypes', 'cloneCommand'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsRenderablesFilter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DShaderUtilsRenderablesFilter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsRenderablesFilter::
    ~QQuick3DShaderUtilsRenderablesFilter()': the destructor: Python never
    removes a C++ QQuick3DShaderUtilsRenderablesFilter.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsRenderablesFilter is created at the first use,
    not by 'QQuick3DShaderUtilsRenderablesFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsRenderablesFilter.
  - Qt tells when it has removed the C++
    QQuick3DShaderUtilsRenderablesFilter. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside QQuick3DShaderUtilsRenderablesFilter, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class RenderableType(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QQuick3DShaderUtilsRenderablesFilter::RenderableType' of
    Qt, with the 3 names Qt gives in it. Qt names the type of its
    combinations 'QQuick3DShaderUtilsRenderablesFilter::RenderableTypes'. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    NULL = 0x0
    Opaque = 0x1
    Transparent = 0x2

  RenderableTypes = RenderableType

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
    Calls Qt's 'QString QQuick3DShaderUtilsRenderablesFilter::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html#tr

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
    #  QString QQuick3DShaderUtilsRenderablesFilter::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderablesFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsRenderablesFilter'

  #  A C++ QQuick3DShaderUtilsRenderablesFilter Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsRenderablesFilter'

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
    *QQuick3DShaderUtilsRenderablesFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsRenderablesFilter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK36QQuick3DShaderUtilsRenderablesFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderableTypes(self) -> RenderableTypes:
    """
    Calls Qt's 'RenderableTypes
    QQuick3DShaderUtilsRenderablesFilter::renderableTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html

    Returns
    -------

    RenderableTypes
      The value standing for the combination Qt gave back.
    """
    #  RenderableTypes
    #      QQuick3DShaderUtilsRenderablesFilter::renderableTypes() const
    return QQuick3DShaderUtilsRenderablesFilter.RenderableTypes(
        self.uglySide.call(
            'ritual_ZNK36QQuick3DShaderUtilsRenderablesFilter15renderableTy'
            'pesEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RenderableTypes)
  def setRenderableTypes(self, types: RenderableTypes) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsRenderablesFilter::setRenderableTypes(RenderableTypes
    types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html

    Parameters
    ----------

    types : RenderableTypes
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsRenderablesFilter::setRenderableTypes(
    #      RenderableTypes types)
    self.uglySide.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderablesFilter18setRenderableType'
        'sE6QFlagsINS_14RenderableTypeEE',
        types.value,
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
    Notes what was given, for Qt's 'QQuick3DShaderUtilsRenderablesFilter::
    QQuick3DShaderUtilsRenderablesFilter()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html
    """
    #  QQuick3DShaderUtilsRenderablesFilter::
    #      QQuick3DShaderUtilsRenderablesFilter()
    self._noteCreation(
        QQuick3DShaderUtilsRenderablesFilter, lambda: Rituals.call(
            'ritual_ZN36QQuick3DShaderUtilsRenderablesFilterC1Ev',
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
    *QQuick3DShaderUtilsRenderablesFilter::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderablesfilter.html

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsRenderablesFilter::cloneCommand()
    ritual = (
        'ritual_ZN36QQuick3DShaderUtilsRenderablesFilter12cloneCommandEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QQuick3DShaderUtilsRenderablesFilter12cloneComman'
          'dEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)
