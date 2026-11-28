"""
Qt3DRender::MeshDownloadRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::MeshDownloadRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MeshDownloadRequest(Qt3DCore.QDownloadRequest):
  """
  The cute side of Qt's Qt3DRender::MeshDownloadRequest: a plain Python
  object standing in front of one C++ Qt3DRender::MeshDownloadRequest.

  It is built on the cute 'Qt3DCore::QDownloadRequest', as Qt's
  Qt3DRender::MeshDownloadRequest is built on Qt's
  Qt3DCore::QDownloadRequest, and has everything that class has.

  C++ hands a Qt3DRender::MeshDownloadRequest around as a copy, so every C++
  Qt3DRender::MeshDownloadRequest behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::MeshDownloadRequest that has a ritual
  and that Python can call so far, 1 name in all: 'onCompleted'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::MeshDownloadRequest::~MeshDownloadRequest()': the
    destructor: Python removes its C++ Qt3DRender::MeshDownloadRequest by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::MeshDownloadRequest is created at the first use, not
    by 'Qt3DRender::MeshDownloadRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::MeshDownloadRequest back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::MeshDownloadRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::MeshDownloadRequest'

  #  Qt's '~Qt3DRender::MeshDownloadRequest()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::MeshDownloadRequest behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender19MeshDownloadRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(
      WAIT['Qt3DCore.QNodeId'], QUrl, WAIT['Qt3DRender.Render.NodeManagers'],
  )
  @overload(WAIT['Qt3DCore.QNodeId'], QUrl, NoneType)
  def __init__(
      self,
      mesh: Qt3DCore.QNodeId,
      source: QUrl,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::MeshDownloadRequest::MeshDownloadRequest(Qt3DCore::QNodeId
    mesh, QUrl source, Render::NodeManagers *managers)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshdownloadrequest.html

    Parameters
    ----------

    mesh : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::MeshDownloadRequest::MeshDownloadRequest(Qt3DCore::QNodeId
    #      mesh, QUrl source, Render::NodeManagers *managers)
    self._noteCreation(MeshDownloadRequest, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19MeshDownloadRequestC1EN8Qt3DCore7QNodeIdE4Q'
        'UrlPNS_6Render12NodeManagersE',
        self._valueOf(mesh), self._valueOf(source),
        self._addressOf(managers),
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

  def onCompleted(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::MeshDownloadRequest::onCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshdownloadrequest.html#onCompleted
    """
    #  void Qt3DRender::MeshDownloadRequest::onCompleted()
    ritual = 'ritual_ZN10Qt3DRender19MeshDownloadRequest11onCompletedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender19MeshDownloadRequest11onCompletedEv')
    self.uglySide.call(ritual)
