"""
Qt3DRender::Render::QRenderPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrenderplugin_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::QRenderPlugin to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderPlugin(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::QRenderPlugin: a plain Python
  object standing in front of one C++ Qt3DRender::Render::QRenderPlugin.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::QRenderPlugin that has a ritual
  and that Python can call so far, 3 names in all: 'registerBackendTypes',
  'unregisterBackendTypes', 'unregisterBackendType'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DRender::Render::QRenderPlugin::registerBackendType(QRenderAspect
    *aspect, const QMetaObject &obj, const Qt3DCore::QBackendNodeMapperPtr
    &functor)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::QRenderPlugin is created at the first use,
    not by 'Qt3DRender::Render::QRenderPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::QRenderPlugin.
  - Each name of Qt's Qt3DRender::Render::QRenderPlugin that has no cute
    function yet, 'registerBackendType', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::QRenderPlugin'

  #  A C++ Qt3DRender::Render::QRenderPlugin Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_QRenderPlugin'

  #  The functions Qt calls itself that Qt3DRender::Render::QRenderPlugin is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'registerBackendTypes': (
          ('_ZN10Qt3DRender6Render13QRenderPlugin20registerBackendTypesEPNS'
           '_13QRenderAspectEPNS0_16AbstractRendererE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.QRenderAspect'),
               ('address', 'address',
                'Qt3DRender:Qt3DRender.Render.AbstractRenderer'),
           )),
      ),
      'unregisterBackendTypes': (
          ('_ZN10Qt3DRender6Render13QRenderPlugin22unregisterBackendTypesEP'
           'NS_13QRenderAspectE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.QRenderAspect'),
           )),
      ),
  }

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

  @overload(
      WAIT['Qt3DRender.QRenderAspect'],
      WAIT['Qt3DRender.Render.AbstractRenderer'],
  )
  @overload(WAIT['Qt3DRender.QRenderAspect'], NoneType)
  @overload(NoneType, WAIT['Qt3DRender.Render.AbstractRenderer'])
  @overload(NoneType, NoneType)
  def registerBackendTypes(
      self,
      aspect: Optional[Qt3DRender.QRenderAspect],
      renderer: Optional[Qt3DRender.Render.AbstractRenderer],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::QRenderPlugin::registerBackendTypes(QRenderAspect
    *aspect, AbstractRenderer *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderplugin.html

    Parameters
    ----------

    aspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderer : Optional[Qt3DRender.Render.AbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::QRenderPlugin::registerBackendTypes(
    #      QRenderAspect *aspect, AbstractRenderer *renderer)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13QRenderPlugin20registerBackendTypesE'
        'PNS_13QRenderAspectEPNS0_16AbstractRendererE',
        self._addressOf(aspect), self._addressOf(renderer),
    )

  @overload(WAIT['Qt3DRender.QRenderAspect'])
  @overload(NoneType)
  def unregisterBackendTypes(
      self,
      aspect: Optional[Qt3DRender.QRenderAspect],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::QRenderPlugin::unregisterBackendTypes(QRenderAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderplugin.html

    Parameters
    ----------

    aspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::QRenderPlugin::unregisterBackendTypes(
    #      QRenderAspect *aspect)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13QRenderPlugin22unregisterBackendType'
        'sEPNS_13QRenderAspectE',
        self._addressOf(aspect),
    )

  @overload(WAIT['Qt3DRender.QRenderAspect'], QMetaObject)
  @overload(NoneType, QMetaObject)
  def unregisterBackendType(
      self,
      aspect: Optional[Qt3DRender.QRenderAspect],
      obj: QMetaObject,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::QRenderPlugin::unregisterBackendType(QRenderAspect
    *aspect, const QMetaObject &obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderplugin.html

    Parameters
    ----------

    aspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : QMetaObject
      Passed on as a value: Qt reads the C++ QMetaObject, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::QRenderPlugin::unregisterBackendType(
    #      QRenderAspect *aspect, const QMetaObject &obj)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13QRenderPlugin21unregisterBackendType'
        'EPNS_13QRenderAspectERK11QMetaObject',
        self._addressOf(aspect), self._valueOf(obj, 'QMetaObject'),
    )

  @staticmethod
  def registerBackendType(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::QRenderPlugin::registerBackendType(QRenderAspect
    *aspect, const QMetaObject &obj, const Qt3DCore::QBackendNodeMapperPtr
    &functor)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.QRenderPlugin.registerBackendType' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::QRenderPlugin::registerBackendType(QRenderAspec"
        "t *aspect, const QMetaObject &obj, const "
        "Qt3DCore::QBackendNodeMapperPtr &functor)': takes a type Python "
        "has no way to hand over yet.")
