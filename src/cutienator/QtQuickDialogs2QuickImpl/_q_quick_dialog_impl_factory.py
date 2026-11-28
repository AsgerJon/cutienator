"""
QQuickDialogImplFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickdialogimplfactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogImplFactory to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuickDialogImplFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDialogImplFactory: a plain Python object
  standing in front of one C++ QQuickDialogImplFactory.

  C++ hands a QQuickDialogImplFactory around as a copy, so every C++
  QQuickDialogImplFactory behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuickDialogImplFactory yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::unique_ptr<QPlatformDialogHelper>
    QQuickDialogImplFactory::createPlatformDialogHelper(QQuickDialogType
    type, QObject *parent)': names the enum 'QQuickDialogType', whose class
    cannot be named here.
  - Qt's 'QQuickDialogImplFactory::~QQuickDialogImplFactory()': the
    destructor: Python removes its C++ QQuickDialogImplFactory by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQuickDialogImplFactory is created at the first use, not by
    'QQuickDialogImplFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDialogImplFactory back gives a copy the ritual
    made for Python, in a new cute QQuickDialogImplFactory.
  - Each name of Qt's QQuickDialogImplFactory that has no cute function yet,
    'createPlatformDialogHelper', holds a function that raises
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
  __qt_class__ = 'QQuickDialogImplFactory'

  #  Qt's '~QQuickDialogImplFactory()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickDialogImplFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQuickDialogImplFactoryD1Ev'

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
  def createPlatformDialogHelper(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QPlatformDialogHelper>
    QQuickDialogImplFactory::createPlatformDialogHelper(QQuickDialogType
    type, QObject *parent)': names the enum 'QQuickDialogType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QQuickDialogImplFactory.createPlatformDialogHelper' has no cute "
        "function yet. Qt's 'std::unique_ptr<QPlatformDialogHelper> "
        "QQuickDialogImplFactory::createPlatformDialogHelper(QQuickDialogTyp"
        "e type, QObject *parent)': names the enum 'QQuickDialogType', "
        "whose class cannot be named here.")
