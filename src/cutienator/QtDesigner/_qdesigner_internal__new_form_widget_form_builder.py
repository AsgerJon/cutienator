"""
qdesigner_internal::NewFormWidgetFormBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formbuilder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::NewFormWidgetFormBuilder to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import DomCustomWidgets, QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomCustomWidgets = WAIT['DomCustomWidgets']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class NewFormWidgetFormBuilder(qdesigner_internal.QDesignerFormBuilder):
  """
  The cute side of Qt's qdesigner_internal::NewFormWidgetFormBuilder: a plain
  Python object standing in front of one C++
  qdesigner_internal::NewFormWidgetFormBuilder.

  It is built on the cute 'qdesigner_internal::QDesignerFormBuilder', as Qt's
  qdesigner_internal::NewFormWidgetFormBuilder is built on Qt's
  qdesigner_internal::QDesignerFormBuilder, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::NewFormWidgetFormBuilder that
  has a ritual and that Python can call so far, 1 name in all:
  'createCustomWidgets'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::NewFormWidgetFormBuilder is created at the
    first use, not by 'qdesigner_internal::NewFormWidgetFormBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::NewFormWidgetFormBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::NewFormWidgetFormBuilder'

  #  A C++ qdesigner_internal::NewFormWidgetFormBuilder Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_NewFormWidgetFormBuilder'

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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(
      QDesignerFormEditorInterface, WAIT['qdesigner_internal.DeviceProfile'],
  )
  @overload(NoneType, WAIT['qdesigner_internal.DeviceProfile'])
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      deviceProfile: Optional[qdesigner_internal.DeviceProfile] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::NewFormWidgetFormBuilder::NewFormWidgetFormBuilder(
    QDesignerFormEditorInterface *core, const DeviceProfile &deviceProfile)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidgetformbuilder.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deviceProfile : Optional[qdesigner_internal.DeviceProfile]
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own. May be
      left out, as in Qt: a new 'qdesigner_internal.DeviceProfile()' is then
      passed on.
    """
    #  qdesigner_internal::NewFormWidgetFormBuilder::
    #      NewFormWidgetFormBuilder(QDesignerFormEditorInterface *core, const
    #      DeviceProfile &deviceProfile)
    if deviceProfile is None:
      deviceProfile = qdesigner_internal.DeviceProfile()
    self._noteCreation(NewFormWidgetFormBuilder, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24NewFormWidgetFormBuilderC1EP28QDesi'
        'gnerFormEditorInterfaceRKNS_13DeviceProfileE',
        self._addressOf(core), self._valueOf(deviceProfile),
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

  @overload(DomCustomWidgets)
  @overload(NoneType)
  def createCustomWidgets(self, a0: Optional[DomCustomWidgets]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidgetFormBuilder::createCustomWidgets(
    DomCustomWidgets *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidgetformbuilder.html

    Parameters
    ----------

    a0 : Optional[DomCustomWidgets]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      qdesigner_internal::NewFormWidgetFormBuilder::createCustomWidgets(
    #      DomCustomWidgets *a0)
    ritual = (
        'ritual_ZN18qdesigner_internal24NewFormWidgetFormBuilder19createCus'
        'tomWidgetsEP16DomCustomWidgets')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24NewFormWidgetFormBuilder19cre'
          'ateCustomWidgetsEP16DomCustomWidgets')
    self.uglySide.call(ritual, self._addressOf(a0))
