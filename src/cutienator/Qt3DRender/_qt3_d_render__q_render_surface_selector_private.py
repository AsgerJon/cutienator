"""
Qt3DRender::QRenderSurfaceSelectorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrendersurfaceselector_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QRenderSurfaceSelectorPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderSurfaceSelectorPrivate(Qt3DRender.QFrameGraphNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderSurfaceSelectorPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::QRenderSurfaceSelectorPrivate.

  It is built on the cute 'Qt3DRender::QFrameGraphNodePrivate', as Qt's
  Qt3DRender::QRenderSurfaceSelectorPrivate is built on Qt's
  Qt3DRender::QFrameGraphNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderSurfaceSelectorPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'find',
  'setExternalRenderTargetSize', 'externalRenderTargetSize'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QRenderSurfaceSelectorPrivate::
    ~QRenderSurfaceSelectorPrivate()': the destructor: Python never removes a
    C++ Qt3DRender::QRenderSurfaceSelectorPrivate.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderSurfaceSelectorPrivate is created at the first
    use, not by 'Qt3DRender::QRenderSurfaceSelectorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderSurfaceSelectorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def find(
      rootObject: Optional[QObject],
  ) -> Optional[Qt3DRender.QRenderSurfaceSelector]:
    """
    Calls Qt's 'QRenderSurfaceSelector
    *Qt3DRender::QRenderSurfaceSelectorPrivate::find(QObject *rootObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselectorprivate.html#find

    Parameters
    ----------

    rootObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Qt3DRender.QRenderSurfaceSelector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderSurfaceSelector
    #      *Qt3DRender::QRenderSurfaceSelectorPrivate::find(QObject
    #      *rootObject)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivate4findEP7QObjec'
        't',
        CuteMixin._addressOf(rootObject, 'QObject'),
    )
    return Qt3DRender.QRenderSurfaceSelector._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderSurfaceSelectorPrivate'

  #  A C++ Qt3DRender::QRenderSurfaceSelectorPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderSurfaceSelectorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def externalRenderTargetSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    Qt3DRender::QRenderSurfaceSelectorPrivate::externalRenderTargetSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselectorprivate.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DRender::QRenderSurfaceSelectorPrivate::
    #      externalRenderTargetSize() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender29QRenderSurfaceSelectorPrivate24externalRen'
        'derTargetSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setExternalRenderTargetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelectorPrivate::setExternalRenderTargetSize(
    const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselectorprivate.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::QRenderSurfaceSelectorPrivate::
    #      setExternalRenderTargetSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivate27setExternalR'
        'enderTargetSizeERK5QSize',
        self._valueOf(size),
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
    'Qt3DRender::QRenderSurfaceSelectorPrivate::
    QRenderSurfaceSelectorPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselectorprivate.html
    """
    #  Qt3DRender::QRenderSurfaceSelectorPrivate::
    #      QRenderSurfaceSelectorPrivate()
    self._noteCreation(QRenderSurfaceSelectorPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivateC1Ev',
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
