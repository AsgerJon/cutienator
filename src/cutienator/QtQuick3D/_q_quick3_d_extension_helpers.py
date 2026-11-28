"""
QQuick3DExtensionHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/ssg/qquick3dextensionhelpers.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuick3DExtensionHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DExtensionHelpers: a plain Python object
  standing in front of one C++ QQuick3DExtensionHelpers.

  C++ hands a QQuick3DExtensionHelpers around as a copy, so every C++
  QQuick3DExtensionHelpers behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuick3DExtensionHelpers yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGNodeId QQuick3DExtensionHelpers::getNodeId(const QQuick3DObject
    &node)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGResourceId QQuick3DExtensionHelpers::getResourceId(const
    QQuick3DObject &resource)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGCameraId QQuick3DExtensionHelpers::getCameraId(const
    QQuick3DObject &camera)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGExtensionId QQuick3DExtensionHelpers::getExtensionId(const
    QQuick3DObject &extension)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGRenderGraphObject::Type
    QQuick3DExtensionHelpers::getNodeIdType(QSSGNodeId nodeId)': names the
    enum 'QSSGNodeId', whose class cannot be named here.
  - Qt's 'QQuick3DExtensionHelpers::~QQuick3DExtensionHelpers()': the
    destructor: Python removes its C++ QQuick3DExtensionHelpers by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQuick3DExtensionHelpers is created at the first use, not by
    'QQuick3DExtensionHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DExtensionHelpers back gives a copy the ritual
    made for Python, in a new cute QQuick3DExtensionHelpers.
  - Each name of Qt's QQuick3DExtensionHelpers that has no cute function yet,
    'getCameraId', 'getExtensionId', 'getNodeId', 'getNodeIdType',
    'getResourceId', 'isNull', holds a function that raises
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
  __qt_class__ = 'QQuick3DExtensionHelpers'

  #  Qt's '~QQuick3DExtensionHelpers()'. Naming it makes this a value class:
  #  Python owns every C++ QQuick3DExtensionHelpers behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuick3DExtensionHelpersD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DExtensionHelpers::QQuick3DExtensionHelpers()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dextensionhelpers.html
    """
    #  QQuick3DExtensionHelpers::QQuick3DExtensionHelpers()
    self._noteCreation(QQuick3DExtensionHelpers, lambda: Rituals.call(
        'ritual_ZN24QQuick3DExtensionHelpersC1Ev',
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

  @staticmethod
  def getCameraId(*__, **_) -> Never:
    """
    Qt's 'QSSGCameraId QQuick3DExtensionHelpers::getCameraId(const
    QQuick3DObject &camera)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.getCameraId' has no cute function yet. "
        "Qt's 'QSSGCameraId QQuick3DExtensionHelpers::getCameraId(const "
        "QQuick3DObject &camera)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def getExtensionId(*__, **_) -> Never:
    """
    Qt's 'QSSGExtensionId QQuick3DExtensionHelpers::getExtensionId(const
    QQuick3DObject &extension)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.getExtensionId' has no cute function "
        "yet. Qt's 'QSSGExtensionId "
        "QQuick3DExtensionHelpers::getExtensionId(const QQuick3DObject "
        "&extension)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getNodeId(*__, **_) -> Never:
    """
    Qt's 'QSSGNodeId QQuick3DExtensionHelpers::getNodeId(const QQuick3DObject
    &node)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.getNodeId' has no cute function yet. "
        "Qt's 'QSSGNodeId QQuick3DExtensionHelpers::getNodeId(const "
        "QQuick3DObject &node)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def getNodeIdType(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderGraphObject::Type
    QQuick3DExtensionHelpers::getNodeIdType(QSSGNodeId nodeId)': names the
    enum 'QSSGNodeId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.getNodeIdType' has no cute function yet. "
        "Qt's 'QSSGRenderGraphObject::Type "
        "QQuick3DExtensionHelpers::getNodeIdType(QSSGNodeId nodeId)': names "
        "the enum 'QSSGNodeId', whose class cannot be named here.")

  @staticmethod
  def getResourceId(*__, **_) -> Never:
    """
    Qt's 'QSSGResourceId QQuick3DExtensionHelpers::getResourceId(const
    QQuick3DObject &resource)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.getResourceId' has no cute function yet. "
        "Qt's 'QSSGResourceId QQuick3DExtensionHelpers::getResourceId(const "
        "QQuick3DObject &resource)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def isNull(*__, **_) -> Never:
    """
    Qt's 'QQuick3DExtensionHelpers::isNull': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuick3DExtensionHelpers.isNull' has no cute function yet. Qt's "
        "'QQuick3DExtensionHelpers::isNull': a template: a pattern and no "
        "single function.")
