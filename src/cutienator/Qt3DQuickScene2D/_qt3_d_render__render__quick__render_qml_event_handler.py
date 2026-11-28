"""
Qt3DRender::Render::Quick::RenderQmlEventHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::Quick::RenderQmlEventHandler to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderQmlEventHandler(QObject):
  """
  The cute side of Qt's Qt3DRender::Render::Quick::RenderQmlEventHandler: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::Quick::RenderQmlEventHandler.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::Render::Quick::RenderQmlEventHandler is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Quick::RenderQmlEventHandler
  that has a ritual and that Python can call so far, 2 names in all:
  'metaObject', 'event'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 not a gap; 1 leans on 'Qt3DRender; 1
  leans on 'vtable for Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Quick::RenderQmlEventHandler is created at
    the first use, not by
    'Qt3DRender::Render::Quick::RenderQmlEventHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::Quick::RenderQmlEventHandler.
  - Qt tells when it has removed the C++
    Qt3DRender::Render::Quick::RenderQmlEventHandler. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's Qt3DRender::Render::Quick::RenderQmlEventHandler that
    has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::Quick::RenderQmlEventHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::Render::Quick::RenderQmlEventHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-renderqmleventhandler.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::Render::Quick::RenderQmlEventHandler::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Quick21RenderQmlEventHandler10metaOb'
        'jectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DRender::Render::Quick::RenderQmlEventHandler::RenderQmlEventHandler(
    Scene2D *node)': leans on 'vtable for
    Qt3DRender::Render::Quick::RenderQmlEventHandler', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Quick.RenderQmlEventHandler.__init__' has no "
        "cute function yet. Qt's "
        "'Qt3DRender::Render::Quick::RenderQmlEventHandler::RenderQmlEventHa"
        "ndler(Scene2D *node)': leans on 'vtable for "
        "Qt3DRender::Render::Quick::RenderQmlEventHandler', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::Quick::RenderQmlEventHandler::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-renderqmleventhandler.html

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::Quick::RenderQmlEventHandler::event(QEvent
    #      *e)
    ritual = (
        'ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler5eventEP6'
        'QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler5ev'
          'entEP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(e))
