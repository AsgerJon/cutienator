"""
QQmlPropertyToBindablePropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyToBindablePropertyBinding to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QtPrivate
from . import QQmlPropertyBindingBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlEngine, QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyToBindablePropertyBinding(QQmlPropertyBindingBase):
  """
  The cute side of Qt's QQmlPropertyToBindablePropertyBinding: a plain Python
  object standing in front of one C++ QQmlPropertyToBindablePropertyBinding.

  It is built on the cute 'QQmlPropertyBindingBase', as Qt's
  QQmlPropertyToBindablePropertyBinding is built on Qt's
  QQmlPropertyBindingBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyToBindablePropertyBinding that has a
  ritual and that Python can call so far, 1 name in all: 'source'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlPropertyToBindablePropertyBinding is created at the first
    use, not by 'QQmlPropertyToBindablePropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyToBindablePropertyBinding.
  - Each name of Qt's QQmlPropertyToBindablePropertyBinding that has no cute
    function yet, 'update', holds a function that raises
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
  __qt_class__ = 'QQmlPropertyToBindablePropertyBinding'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlPropertyToBindablePropertyBinding::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytobindablepropertybinding.html#source

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlPropertyToBindablePropertyBinding::source() const
    address = self.uglySide.call(
        'ritual_ZNK37QQmlPropertyToBindablePropertyBinding6sourceEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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

  @overload(
      QQmlEngine, QQmlProperty, QQmlProperty,
      WAIT['QtPrivate.BindingFunctionVTable'],
  )
  @overload(QQmlEngine, QQmlProperty, QQmlProperty, NoneType)
  @overload(
      NoneType, QQmlProperty, QQmlProperty,
      WAIT['QtPrivate.BindingFunctionVTable'],
  )
  @overload(NoneType, QQmlProperty, QQmlProperty, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      source: QQmlProperty,
      target: QQmlProperty,
      vtable: Optional[QtPrivate.BindingFunctionVTable],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyToBindablePropertyBinding::
    QQmlPropertyToBindablePropertyBinding(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target, const
    QtPrivate::BindingFunctionVTable *vtable)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytobindablepropertybinding.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    target : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    vtable : Optional[QtPrivate.BindingFunctionVTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlPropertyToBindablePropertyBinding::
    #      QQmlPropertyToBindablePropertyBinding(QQmlEngine *engine, const
    #      QQmlProperty &source, const QQmlProperty &target, const
    #      QtPrivate::BindingFunctionVTable *vtable)
    self._noteCreation(
        QQmlPropertyToBindablePropertyBinding, lambda: Rituals.call(
            'ritual_ZN37QQmlPropertyToBindablePropertyBindingC1EP10QQmlEngi'
            'neRK12QQmlPropertyS4_PKN9QtPrivate21BindingFunctionVTableE',
            self._addressOf(engine), self._valueOf(source),
            self._valueOf(target), self._addressOf(vtable),
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
  def update(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyToBindablePropertyBinding::update': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlPropertyToBindablePropertyBinding.update' has no cute "
        "function yet. Qt's "
        "'QQmlPropertyToBindablePropertyBinding::update': a template: a "
        "pattern and no single function.")
