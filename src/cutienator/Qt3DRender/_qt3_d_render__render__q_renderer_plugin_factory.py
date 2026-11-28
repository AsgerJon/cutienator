"""
Qt3DRender::Render::QRendererPluginFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrendererpluginfactory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::QRendererPluginFactory to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QRendererPluginFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::QRendererPluginFactory: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::QRendererPluginFactory.

  C++ hands a Qt3DRender::Render::QRendererPluginFactory around as a copy, so
  every C++ Qt3DRender::Render::QRendererPluginFactory behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::QRendererPluginFactory that has
  a ritual and that Python can call so far, 2 names in all: 'keys', 'create'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::QRendererPluginFactory::~QRendererPluginFactory()':
    the destructor: Python removes its C++
    Qt3DRender::Render::QRendererPluginFactory by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::QRendererPluginFactory is created at the
    first use, not by 'Qt3DRender::Render::QRendererPluginFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::QRendererPluginFactory back gives
    a copy the ritual made for Python, in a new cute
    Qt3DRender::Render::QRendererPluginFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::Render::QRendererPluginFactory::keys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrendererpluginfactory.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::Render::QRendererPluginFactory::keys()
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render22QRendererPluginFactory4keysEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def create(name: str) -> Optional[Qt3DRender.Render.AbstractRenderer]:
    """
    Calls Qt's 'AbstractRenderer
    *Qt3DRender::Render::QRendererPluginFactory::create(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrendererpluginfactory.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DRender.Render.AbstractRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractRenderer
    #      *Qt3DRender::Render::QRendererPluginFactory::create(const QString
    #      &name)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render22QRendererPluginFactory6createERK7QSt'
        'ring',
        name,
    )
    return Qt3DRender.Render.AbstractRenderer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::QRendererPluginFactory'

  #  Qt's '~Qt3DRender::Render::QRendererPluginFactory()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DRender::Render::QRendererPluginFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render22QRendererPluginFactoryD1Ev')

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
