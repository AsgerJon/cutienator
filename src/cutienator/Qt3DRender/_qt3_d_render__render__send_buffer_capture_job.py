"""
Qt3DRender::Render::SendBufferCaptureJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/sendbuffercapturejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::SendBufferCaptureJob to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SendBufferCaptureJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::SendBufferCaptureJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::SendBufferCaptureJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::SendBufferCaptureJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::SendBufferCaptureJob that has a
  ritual and that Python can call so far, 3 names in all: 'setManagers',
  'hasRequests', 'run'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::SendBufferCaptureJob::~SendBufferCaptureJob()':
    the destructor: Python never removes a C++
    Qt3DRender::Render::SendBufferCaptureJob.
  - Qt's 'void
    Qt3DRender::Render::SendBufferCaptureJob::addRequest(QPair<Qt3DCore::
    QNodeId, QByteArray> request)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::SendBufferCaptureJob is created at the first
    use, not by 'Qt3DRender::Render::SendBufferCaptureJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::SendBufferCaptureJob.
  - Each name of Qt's Qt3DRender::Render::SendBufferCaptureJob that has no
    cute function yet, 'addRequest', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::SendBufferCaptureJob'

  #  A C++ Qt3DRender::Render::SendBufferCaptureJob Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_SendBufferCaptureJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasRequests(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::SendBufferCaptureJob::hasRequests()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sendbuffercapturejob.html
    """
    #  bool Qt3DRender::Render::SendBufferCaptureJob::hasRequests() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render20SendBufferCaptureJob11hasRequestsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      nodeManagers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::SendBufferCaptureJob::setManagers(NodeManagers
    *nodeManagers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sendbuffercapturejob.html

    Parameters
    ----------

    nodeManagers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::Render::SendBufferCaptureJob::setManagers(NodeManagers
    #      *nodeManagers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20SendBufferCaptureJob11setManagersEPN'
        'S0_12NodeManagersE',
        self._addressOf(nodeManagers),
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
    'Qt3DRender::Render::SendBufferCaptureJob::SendBufferCaptureJob()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sendbuffercapturejob.html
    """
    #  Qt3DRender::Render::SendBufferCaptureJob::SendBufferCaptureJob()
    self._noteCreation(SendBufferCaptureJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render20SendBufferCaptureJobC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::SendBufferCaptureJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sendbuffercapturejob.html#run
    """
    #  void Qt3DRender::Render::SendBufferCaptureJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20SendBufferCaptureJob3runEv',
    )

  @staticmethod
  def addRequest(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::SendBufferCaptureJob::addRequest(QPair<Qt3DCore::
    QNodeId, QByteArray> request)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.SendBufferCaptureJob.addRequest' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::SendBufferCaptureJob::addRequest(QPair<Qt3DCore"
        "::QNodeId, QByteArray> request)': takes a type Python has no way "
        "to hand over yet.")
