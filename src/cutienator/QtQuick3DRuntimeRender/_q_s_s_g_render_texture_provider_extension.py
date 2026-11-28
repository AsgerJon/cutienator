"""
QSSGRenderTextureProviderExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSSGRenderExtension

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderTextureProviderExtension(QSSGRenderExtension):
  """
  The cute side of Qt's QSSGRenderTextureProviderExtension: a plain Python
  object standing in front of one C++ QSSGRenderTextureProviderExtension.

  It is built on the cute 'QSSGRenderExtension', as Qt's
  QSSGRenderTextureProviderExtension is built on Qt's QSSGRenderExtension,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderTextureProviderExtension that has a ritual
  and that Python can call so far, 2 names in all: 'mode', 'stage'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGRenderTextureProviderExtension::~QSSGRenderTextureProviderExtension(
    )': the destructor: Python never removes a C++
    QSSGRenderTextureProviderExtension.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QSSGRenderTextureProviderExtension is created at the first use,
    not by 'QSSGRenderTextureProviderExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderTextureProviderExtension.
  - Each name of Qt's QSSGRenderTextureProviderExtension that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QSSGRenderTextureProviderExtension'

  #  A C++ QSSGRenderTextureProviderExtension Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGRenderTextureProviderExtension'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mode(self) -> QSSGRenderExtension.RenderMode:
    """
    Calls Qt's 'RenderMode QSSGRenderTextureProviderExtension::mode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureproviderextension.html#mode

    Returns
    -------

    QSSGRenderExtension.RenderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderExtension.RenderMode(number)' gives.
    """
    #  RenderMode QSSGRenderTextureProviderExtension::mode() const
    return QSSGRenderExtension.RenderMode(self.uglySide.call(
        'ritual_ZNK34QSSGRenderTextureProviderExtension4modeEv',
    ))

  def stage(self) -> QSSGRenderExtension.RenderStage:
    """
    Calls Qt's 'RenderStage QSSGRenderTextureProviderExtension::stage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureproviderextension.html#stage

    Returns
    -------

    QSSGRenderExtension.RenderStage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderExtension.RenderStage(number)' gives.
    """
    #  RenderStage QSSGRenderTextureProviderExtension::stage() const
    return QSSGRenderExtension.RenderStage(self.uglySide.call(
        'ritual_ZNK34QSSGRenderTextureProviderExtension5stageEv',
    ))

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
    'QSSGRenderTextureProviderExtension::QSSGRenderTextureProviderExtension(
    )': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSSGRenderTextureProviderExtension.__init__' has no cute function "
        "yet. Qt's "
        "'QSSGRenderTextureProviderExtension::QSSGRenderTextureProviderExten"
        "sion()': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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
