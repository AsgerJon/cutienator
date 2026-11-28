"""
Qt3DRender::Render::PickBoundingVolumeJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PickBoundingVolumeJob to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtGui import QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PickBoundingVolumeJob(Qt3DRender.Render.AbstractPickingJob):
  """
  The cute side of Qt's Qt3DRender::Render::PickBoundingVolumeJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::PickBoundingVolumeJob.

  It is built on the cute 'Qt3DRender::Render::AbstractPickingJob', as Qt's
  Qt3DRender::Render::PickBoundingVolumeJob is built on Qt's
  Qt3DRender::Render::AbstractPickingJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::PickBoundingVolumeJob that has a
  ritual and that Python can call so far, 7 names in all: 'setRoot',
  'processMouseEvent', 'markPickersDirty', 'pickersDirty', 'runHelper',
  'processPickEvent', 'clearPreviouslyHoveredPickers'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HObjectPicker
    Qt3DRender::Render::PickBoundingVolumeJob::currentPicker() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<HObjectPicker>
    Qt3DRender::Render::PickBoundingVolumeJob::hoveredPickers() const': gives
    a type Python has no way to take yet.
  - Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::dispatchPickEvents(const
    QMouseEvent *event, const PickingUtils::HitList &sphereHits,
    QPickEvent::Buttons eventButton, int eventButtons, int eventModifiers,
    bool allHitsRequested, Qt3DCore::QNodeId viewportNodeId)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickBoundingVolumeJob is created at the first
    use, not by 'Qt3DRender::Render::PickBoundingVolumeJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::PickBoundingVolumeJob.
  - Each name of Qt's Qt3DRender::Render::PickBoundingVolumeJob that has no
    cute function yet, 'currentPicker', 'dispatchPickEvents',
    'hoveredPickers', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PickBoundingVolumeJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pickersDirty(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PickBoundingVolumeJob::pickersDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html
    """
    #  bool Qt3DRender::Render::PickBoundingVolumeJob::pickersDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21PickBoundingVolumeJob12pickersDirty'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::setRoot(Entity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::PickBoundingVolumeJob::setRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob7setRootEPNS0_6'
        'EntityE',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::PickBoundingVolumeJob::PickBoundingVolumeJob()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html
    """
    #  Qt3DRender::Render::PickBoundingVolumeJob::PickBoundingVolumeJob()
    self._noteCreation(PickBoundingVolumeJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJobC1Ev',
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

  @overload(QObject, QMouseEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def processMouseEvent(
      self,
      object: Optional[QObject],
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PickBoundingVolumeJob::processMouseEvent(QObject
    *object, QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::PickBoundingVolumeJob::processMouseEvent(
    #      QObject *object, QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob17processMouseE'
        'ventEP7QObjectP11QMouseEvent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  def markPickersDirty(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::markPickersDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html
    """
    #  void Qt3DRender::Render::PickBoundingVolumeJob::markPickersDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob16markPickersDi'
        'rtyEv',
    )

  def runHelper(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::PickBoundingVolumeJob::runHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html
    """
    #  bool Qt3DRender::Render::PickBoundingVolumeJob::runHelper()
    ritual = (
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob9runHelperEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render21PickBoundingVolumeJob9runHelpe'
          'rEv')
    return self.uglySide.call(ritual)

  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.PickConfiguration'], QObject,
      QMouseEvent,
  )
  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.PickConfiguration'], QObject,
      NoneType,
  )
  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.PickConfiguration'], NoneType,
      QMouseEvent,
  )
  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.PickConfiguration'], NoneType,
      NoneType,
  )
  def processPickEvent(
      self,
      pickConfiguration: Qt3DRender.Render.PickingUtils.PickConfiguration,
      object: Optional[QObject],
      event: Optional[QMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::processPickEvent(const
    PickingUtils::PickConfiguration &pickConfiguration, QObject *object,
    const QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html

    Parameters
    ----------

    pickConfiguration : Qt3DRender.Render.PickingUtils.PickConfiguration
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::PickingUtils::PickConfiguration, which stays
      Python's own.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::PickBoundingVolumeJob::processPickEvent(const
    #      PickingUtils::PickConfiguration &pickConfiguration, QObject
    #      *object, const QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob16processPickEv'
        'entERKNS0_12PickingUtils17PickConfigurationEP7QObjectPK11QMouseEve'
        'nt',
        self._valueOf(pickConfiguration), self._addressOf(object, 'QObject'),
        self._addressOf(event),
    )

  def clearPreviouslyHoveredPickers(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::clearPreviouslyHoveredPickers(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickboundingvolumejob.html
    """
    #  void Qt3DRender::Render::PickBoundingVolumeJob::
    #      clearPreviouslyHoveredPickers()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob29clearPrevious'
        'lyHoveredPickersEv',
    )

  @staticmethod
  def currentPicker(*__, **_) -> Never:
    """
    Qt's 'HObjectPicker
    Qt3DRender::Render::PickBoundingVolumeJob::currentPicker() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickBoundingVolumeJob.currentPicker' has no "
        "cute function yet. Qt's 'HObjectPicker "
        "Qt3DRender::Render::PickBoundingVolumeJob::currentPicker() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def dispatchPickEvents(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::PickBoundingVolumeJob::dispatchPickEvents(const
    QMouseEvent *event, const PickingUtils::HitList &sphereHits,
    QPickEvent::Buttons eventButton, int eventButtons, int eventModifiers,
    bool allHitsRequested, Qt3DCore::QNodeId viewportNodeId)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickBoundingVolumeJob.dispatchPickEvents' has "
        "no cute function yet. Qt's 'void "
        "Qt3DRender::Render::PickBoundingVolumeJob::dispatchPickEvents(const"
        " QMouseEvent *event, const PickingUtils::HitList &sphereHits, "
        "QPickEvent::Buttons eventButton, int eventButtons, int "
        "eventModifiers, bool allHitsRequested, Qt3DCore::QNodeId "
        "viewportNodeId)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def hoveredPickers(*__, **_) -> Never:
    """
    Qt's 'QList<HObjectPicker>
    Qt3DRender::Render::PickBoundingVolumeJob::hoveredPickers() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickBoundingVolumeJob.hoveredPickers' has no "
        "cute function yet. Qt's 'QList<HObjectPicker> "
        "Qt3DRender::Render::PickBoundingVolumeJob::hoveredPickers() "
        "const': gives a type Python has no way to take yet.")
