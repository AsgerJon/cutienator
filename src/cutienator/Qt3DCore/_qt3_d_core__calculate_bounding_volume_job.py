"""
Qt3DCore::CalculateBoundingVolumeJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::CalculateBoundingVolumeJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CalculateBoundingVolumeJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DCore::CalculateBoundingVolumeJob: a plain Python
  object standing in front of one C++ Qt3DCore::CalculateBoundingVolumeJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DCore::CalculateBoundingVolumeJob is built on Qt's Qt3DCore::QAspectJob,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::CalculateBoundingVolumeJob that has a
  ritual and that Python can call so far, 4 names in all: 'setRoot',
  'isRequired', 'run', 'postFrame'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::addWatcher(
    QWeakPointer<BoundingVolumeJobProcessor> watcher)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::removeWatcher(
    QWeakPointer<BoundingVolumeJobProcessor> watcher)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::CalculateBoundingVolumeJob is created at the first use,
    not by 'Qt3DCore::CalculateBoundingVolumeJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::CalculateBoundingVolumeJob.
  - Each name of Qt's Qt3DCore::CalculateBoundingVolumeJob that has no cute
    function yet, 'addWatcher', 'removeWatcher', holds a function that raises
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
  __qt_class__ = 'Qt3DCore::CalculateBoundingVolumeJob'

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

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setRoot(self, root: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::setRoot(QEntity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-calculateboundingvolumejob.html#setRoot

    Parameters
    ----------

    root : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::CalculateBoundingVolumeJob::setRoot(QEntity *root)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob7setRootEPNS_7QEntit'
        'yE',
        self._addressOf(root),
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

  @overload(WAIT['Qt3DCore.QCoreAspect'])
  @overload(NoneType)
  def __init__(self, aspect: Optional[Qt3DCore.QCoreAspect]) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::CalculateBoundingVolumeJob::CalculateBoundingVolumeJob(
    QCoreAspect *aspect)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-calculateboundingvolumejob.html

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QCoreAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DCore::CalculateBoundingVolumeJob::CalculateBoundingVolumeJob(
    #      QCoreAspect *aspect)
    self._noteCreation(CalculateBoundingVolumeJob, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore26CalculateBoundingVolumeJobC1EPNS_11QCoreAspect'
        'E',
        self._addressOf(aspect),
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

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::CalculateBoundingVolumeJob::isRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-calculateboundingvolumejob.html
    """
    #  bool Qt3DCore::CalculateBoundingVolumeJob::isRequired()
    ritual = 'ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob10isRequiredEv')
    return self.uglySide.call(ritual)

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-calculateboundingvolumejob.html#run
    """
    #  void Qt3DCore::CalculateBoundingVolumeJob::run()
    ritual = 'ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob3runEv'
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def postFrame(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::CalculateBoundingVolumeJob::postFrame(QAspectEngine
    *aspectEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-calculateboundingvolumejob.html#postFrame

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::CalculateBoundingVolumeJob::postFrame(QAspectEngine
    #      *aspectEngine)
    ritual = (
        'ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob9postFrameEPNS_13QAs'
        'pectEngineE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob9postFrameEPNS'
          '_13QAspectEngineE')
    self.uglySide.call(ritual, self._addressOf(aspectEngine))

  @staticmethod
  def addWatcher(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::addWatcher(
    QWeakPointer<BoundingVolumeJobProcessor> watcher)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.CalculateBoundingVolumeJob.addWatcher' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::CalculateBoundingVolumeJob::addWatcher(QWeakPointer<Bound"
        "ingVolumeJobProcessor> watcher)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def removeWatcher(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::CalculateBoundingVolumeJob::removeWatcher(
    QWeakPointer<BoundingVolumeJobProcessor> watcher)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.CalculateBoundingVolumeJob.removeWatcher' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::CalculateBoundingVolumeJob::removeWatcher(QWeakPointer<Bo"
        "undingVolumeJobProcessor> watcher)': takes a type Python has no "
        "way to hand over yet.")
