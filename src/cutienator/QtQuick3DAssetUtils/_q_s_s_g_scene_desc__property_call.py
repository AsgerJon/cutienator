"""
QSSGSceneDesc::PropertyCall binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGSceneDesc::PropertyCall to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class PropertyCall(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGSceneDesc::PropertyCall: a plain Python object
  standing in front of one C++ QSSGSceneDesc::PropertyCall.

  What exists
  -----------

  No function of Qt's QSSGSceneDesc::PropertyCall yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGSceneDesc::PropertyCall::~PropertyCall()': the destructor:
    Python never removes a C++ QSSGSceneDesc::PropertyCall.
  - Qt's 'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const
    char *a1, const void *a2)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const
    char *a1, const QVariant &a2)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QSSGSceneDesc::PropertyCall::get(const QQuick3DObject &a0,
    const void **a1) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGSceneDesc::PropertyCall is created at the first use, not by
    'QSSGSceneDesc::PropertyCall(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGSceneDesc::PropertyCall.
  - Each name of Qt's QSSGSceneDesc::PropertyCall that has no cute function
    yet, 'get', 'set', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGSceneDesc::PropertyCall'

  #  The functions Qt calls itself that QSSGSceneDesc::PropertyCall is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'set': (
          'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &, const '
          'char *, const void *)',
          'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &, const '
          'char *, const QVariant &)',
      ),
      'get': (
          'bool QSSGSceneDesc::PropertyCall::get(const QQuick3DObject &, '
          'const void **) const',
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
  def get(*__, **_) -> Never:
    """
    Qt's 'bool QSSGSceneDesc::PropertyCall::get(const QQuick3DObject &a0,
    const void **a1) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGSceneDesc.PropertyCall.get' has no cute function yet. Qt's "
        "'bool QSSGSceneDesc::PropertyCall::get(const QQuick3DObject &a0, "
        "const void **a1) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    - Qt's 'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const
      char *a1, const void *a2)': takes a type Python has no way to hand over
      yet.
    - Qt's 'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const
      char *a1, const QVariant &a2)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGSceneDesc.PropertyCall.set' has no cute function yet. Qt's "
        "'bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const "
        "char *a1, const void *a2)': takes a type Python has no way to hand "
        "over yet. Qt's 'bool "
        "QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const char "
        "*a1, const QVariant &a2)': takes a type Python has no way to hand "
        "over yet.")
