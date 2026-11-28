"""
Qt3DRender::Render::RenderBackendResourceAccessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/resourceaccessor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::RenderBackendResourceAccessor to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class RenderBackendResourceAccessor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::RenderBackendResourceAccessor: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::RenderBackendResourceAccessor.

  What exists
  -----------

  No function of Qt's Qt3DRender::Render::RenderBackendResourceAccessor yet.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::RenderBackendResourceAccessor::
    ~RenderBackendResourceAccessor()': the destructor: Python never removes a
    C++ Qt3DRender::Render::RenderBackendResourceAccessor.
  - Qt's 'bool
    Qt3DRender::Render::RenderBackendResourceAccessor::accessResource(
    ResourceType type, Qt3DCore::QNodeId nodeId, void **handle, QMutex
    **lock)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderBackendResourceAccessor is created at
    the first use, not by
    'Qt3DRender::Render::RenderBackendResourceAccessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::RenderBackendResourceAccessor.
  - Each name of Qt's Qt3DRender::Render::RenderBackendResourceAccessor that
    has no cute function yet, 'accessResource', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside
  #  Qt3DRender::Render::RenderBackendResourceAccessor, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ResourceType(CuteNum):
    """
    The enum
    'Qt3DRender::Render::RenderBackendResourceAccessor::ResourceType' of Qt,
    with the 4 names Qt gives in it.
    """

    OGLTextureWrite = Kee[int](0)
    OGLTextureRead = Kee[int](1)
    OutputAttachment = Kee[int](2)
    EntityHandle = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderBackendResourceAccessor'

  #  The functions Qt calls itself that
  #  Qt3DRender::Render::RenderBackendResourceAccessor is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'accessResource': (
          'bool '
          'Qt3DRender::Render::RenderBackendResourceAccessor::accessResourc'
          'e(ResourceType, Qt3DCore::QNodeId, void **, QMutex **)',
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

  @staticmethod
  def accessResource(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::RenderBackendResourceAccessor::accessResource(
    ResourceType type, Qt3DCore::QNodeId nodeId, void **handle, QMutex
    **lock)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderBackendResourceAccessor.accessResource' "
        "has no cute function yet. Qt's 'bool "
        "Qt3DRender::Render::RenderBackendResourceAccessor::accessResource(R"
        "esourceType type, Qt3DCore::QNodeId nodeId, void **handle, QMutex "
        "**lock)': takes a type Python has no way to hand over yet.")
