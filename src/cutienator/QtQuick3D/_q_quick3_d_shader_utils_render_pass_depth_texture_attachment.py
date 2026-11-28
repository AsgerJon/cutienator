"""
QQuick3DShaderUtilsRenderPassDepthTextureAttachment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsRenderPassDepthTextureAttachment to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsRenderPassDepthTextureAttachment(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsRenderPassDepthTextureAttachment:
  a plain Python object standing in front of one C++
  QQuick3DShaderUtilsRenderPassDepthTextureAttachment.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsRenderPassDepthTextureAttachment is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsRenderPassDepthTextureAttachment
  that has a ritual and that Python can call so far, 3 names in all:
  'metaObject', 'tr', 'cloneCommand'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QQuick3DShaderUtilsRenderPassDepthTextureAttachment::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QQuick3DShaderUtilsRenderPassDepthTextureAttachment::
    ~QQuick3DShaderUtilsRenderPassDepthTextureAttachment()': the destructor:
    Python never removes a C++
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsRenderPassDepthTextureAttachment is created at
    the first use, not by
    'QQuick3DShaderUtilsRenderPassDepthTextureAttachment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment.
  - Qt tells when it has removed the C++
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassdepthtextureattachment.html

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
    #  QString QQuick3DShaderUtilsRenderPassDepthTextureAttachment::tr(const
    #      char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN51QQuick3DShaderUtilsRenderPassDepthTextureAttachment2trE'
        'PKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsRenderPassDepthTextureAttachment'

  #  A C++ QQuick3DShaderUtilsRenderPassDepthTextureAttachment Python makes
  #  is of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsRenderPassDepthTextureAttachment'

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
    *QQuick3DShaderUtilsRenderPassDepthTextureAttachment::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassdepthtextureattachment.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuick3DShaderUtilsRenderPassDepthTextureAttachment::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK51QQuick3DShaderUtilsRenderPassDepthTextureAttachment10m'
        'etaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's
    'QQuick3DShaderUtilsRenderPassDepthTextureAttachment::
    QQuick3DShaderUtilsRenderPassDepthTextureAttachment()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassdepthtextureattachment.html
    """
    #  QQuick3DShaderUtilsRenderPassDepthTextureAttachment::
    #      QQuick3DShaderUtilsRenderPassDepthTextureAttachment()
    self._noteCreation(
        QQuick3DShaderUtilsRenderPassDepthTextureAttachment, lambda: Rituals.call(
            'ritual_ZN51QQuick3DShaderUtilsRenderPassDepthTextureAttachment'
            'C1Ev',
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
    *QQuick3DShaderUtilsRenderPassDepthTextureAttachment::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassdepthtextureattachment.html

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsRenderPassDepthTextureAttachment::
    #      cloneCommand()
    ritual = (
        'ritual_ZN51QQuick3DShaderUtilsRenderPassDepthTextureAttachment12cl'
        'oneCommandEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN51QQuick3DShaderUtilsRenderPassDepthTextureAttachme'
          'nt12cloneCommandEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)
