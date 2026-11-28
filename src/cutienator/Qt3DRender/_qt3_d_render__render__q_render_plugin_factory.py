"""
Qt3DRender::Render::QRenderPluginFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrenderpluginfactory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::QRenderPluginFactory to be private: it
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


class QRenderPluginFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::QRenderPluginFactory: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::QRenderPluginFactory.

  C++ hands a Qt3DRender::Render::QRenderPluginFactory around as a copy, so
  every C++ Qt3DRender::Render::QRenderPluginFactory behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::QRenderPluginFactory that has a
  ritual and that Python can call so far, 2 names in all: 'keys', 'create'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::QRenderPluginFactory::~QRenderPluginFactory()':
    the destructor: Python removes its C++
    Qt3DRender::Render::QRenderPluginFactory by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::QRenderPluginFactory is created at the first
    use, not by 'Qt3DRender::Render::QRenderPluginFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::QRenderPluginFactory back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::QRenderPluginFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::Render::QRenderPluginFactory::keys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactory.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::Render::QRenderPluginFactory::keys()
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render20QRenderPluginFactory4keysEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QStringList)
  def create(
      name: str,
      args: QStringList,
  ) -> Optional[Qt3DRender.Render.QRenderPlugin]:
    """
    Calls Qt's 'QRenderPlugin
    *Qt3DRender::Render::QRenderPluginFactory::create(const QString &name,
    const QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactory.html#create

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[Qt3DRender.Render.QRenderPlugin]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderPlugin *Qt3DRender::Render::QRenderPluginFactory::create(const
    #      QString &name, const QStringList &args)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render20QRenderPluginFactory6createERK7QStri'
        'ngRK5QListIS2_E',
        name, CuteMixin._valueOf(args),
    )
    return Qt3DRender.Render.QRenderPlugin._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::QRenderPluginFactory'

  #  Qt's '~Qt3DRender::Render::QRenderPluginFactory()'. Naming it makes this
  #  a value class: Python owns every C++
  #  Qt3DRender::Render::QRenderPluginFactory behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render20QRenderPluginFactoryD1Ev')

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
