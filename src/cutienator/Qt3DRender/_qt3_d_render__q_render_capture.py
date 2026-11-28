"""
Qt3DRender::QRenderCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderCapture(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QRenderCapture: a plain Python object
  standing in front of one C++ Qt3DRender::QRenderCapture.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QRenderCapture is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderCapture that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'requestCapture', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderCapture::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderCapture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QRenderCapturePrivate *Qt3DRender::QRenderCapture::d_func()
    const': takes in Python what 'QRenderCapturePrivate
    *Qt3DRender::QRenderCapture::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderCapture is created at the first use, not by
    'Qt3DRender::QRenderCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderCapture.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderCapture. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QRenderCapture::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#tr

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
    #  QString Qt3DRender::QRenderCapture::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QRenderCapture2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QRenderCapture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderCapture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QRenderCapture10metaObjectEv',
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderCapture::QRenderCapture(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#QRenderCapture

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderCapture::QRenderCapture(Qt3DCore::QNode *parent)
    self._noteCreation(QRenderCapture, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QRenderCaptureC1EPN8Qt3DCore5QNodeE',
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

  @overload(int)
  def requestCapture(
      self,
      captureId: int,
  ) -> Optional[Qt3DRender.QRenderCaptureReply]:
    """
    Calls Qt's 'Qt3DRender::QRenderCaptureReply
    *Qt3DRender::QRenderCapture::requestCapture(int captureId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#requestCapture

    Parameters
    ----------

    captureId : int
      Passed on as it is.

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QRenderCaptureReply
    #      *Qt3DRender::QRenderCapture::requestCapture(int captureId)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureEi', captureId,
    )
    return Qt3DRender.QRenderCaptureReply._cuteAt(address)

  @overload()
  def requestCapture(self) -> Optional[Qt3DRender.QRenderCaptureReply]:
    """
    Calls Qt's 'Qt3DRender::QRenderCaptureReply
    *Qt3DRender::QRenderCapture::requestCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#requestCapture

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QRenderCaptureReply
    #      *Qt3DRender::QRenderCapture::requestCapture()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureEv',
    )
    return Qt3DRender.QRenderCaptureReply._cuteAt(address)

  @overload(QRect)
  def requestCapture(
      self,
      rect: QRect,
  ) -> Optional[Qt3DRender.QRenderCaptureReply]:
    """
    Calls Qt's 'Qt3DRender::QRenderCaptureReply
    *Qt3DRender::QRenderCapture::requestCapture(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#requestCapture

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QRenderCaptureReply
    #      *Qt3DRender::QRenderCapture::requestCapture(const QRect &rect)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureERK5QRect',
        self._valueOf(rect),
    )
    return Qt3DRender.QRenderCaptureReply._cuteAt(address)

  def d_func(self) -> Optional[Qt3DRender.QRenderCapturePrivate]:
    """
    Calls Qt's 'QRenderCapturePrivate *Qt3DRender::QRenderCapture::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapture.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderCapturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCapturePrivate *Qt3DRender::QRenderCapture::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QRenderCapture6d_funcEv',
    )
    return Qt3DRender.QRenderCapturePrivate._cuteAt(address)
