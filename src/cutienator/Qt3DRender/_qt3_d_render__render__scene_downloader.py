"""
Qt3DRender::Render::SceneDownloader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/scenemanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::SceneDownloader to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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


class SceneDownloader(Qt3DCore.QDownloadRequest):
  """
  The cute side of Qt's Qt3DRender::Render::SceneDownloader: a plain Python
  object standing in front of one C++ Qt3DRender::Render::SceneDownloader.

  It is built on the cute 'Qt3DCore::QDownloadRequest', as Qt's
  Qt3DRender::Render::SceneDownloader is built on Qt's
  Qt3DCore::QDownloadRequest, and has everything that class has.

  C++ hands a Qt3DRender::Render::SceneDownloader around as a copy, so every
  C++ Qt3DRender::Render::SceneDownloader behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::SceneDownloader that has a
  ritual and that Python can call so far, 1 name in all: 'onCompleted'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::SceneDownloader::~SceneDownloader()': the
    destructor: Python removes its C++ Qt3DRender::Render::SceneDownloader by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::SceneDownloader is created at the first use,
    not by 'Qt3DRender::Render::SceneDownloader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::SceneDownloader back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::SceneDownloader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::SceneDownloader'

  #  Qt's '~Qt3DRender::Render::SceneDownloader()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::SceneDownloader
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render15SceneDownloaderD1Ev'

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
      QUrl, WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DRender.Render.SceneManager'],
  )
  @overload(QUrl, WAIT['Qt3DCore.QNodeId'], NoneType)
  def __init__(
      self,
      source: QUrl,
      sceneComponent: Qt3DCore.QNodeId,
      manager: Optional[Qt3DRender.Render.SceneManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::SceneDownloader::SceneDownloader(const QUrl &source,
    Qt3DCore::QNodeId sceneComponent, SceneManager *manager)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenedownloader.html

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    sceneComponent : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    manager : Optional[Qt3DRender.Render.SceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::SceneDownloader::SceneDownloader(const QUrl
    #      &source, Qt3DCore::QNodeId sceneComponent, SceneManager *manager)
    self._noteCreation(SceneDownloader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render15SceneDownloaderC1ERK4QUrlN8Qt3DCore7'
        'QNodeIdEPNS0_12SceneManagerE',
        self._valueOf(source), self._valueOf(sceneComponent),
        self._addressOf(manager),
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
    Calls Qt's 'void Qt3DRender::Render::SceneDownloader::onCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenedownloader.html#onCompleted
    """
    #  void Qt3DRender::Render::SceneDownloader::onCompleted()
    ritual = 'ritual_ZN10Qt3DRender6Render15SceneDownloader11onCompletedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render15SceneDownloader11onCompletedEv')
    self.uglySide.call(ritual)
