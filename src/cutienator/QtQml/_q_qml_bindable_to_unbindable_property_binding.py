"""
QQmlBindableToUnbindablePropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlBindableToUnbindablePropertyBinding to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QPropertyObserver
from . import QQmlPropertyToUnbindablePropertyBinding

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBindableToUnbindablePropertyBinding(QPropertyObserver, QQmlPropertyToUnbindablePropertyBinding):
  """
  The cute side of Qt's QQmlBindableToUnbindablePropertyBinding: a plain
  Python object standing in front of one C++
  QQmlBindableToUnbindablePropertyBinding.

  It is built on the cute 'QPropertyObserver', as Qt's
  QQmlBindableToUnbindablePropertyBinding is built on Qt's QPropertyObserver,
  and has everything that class has. It is built on the cute
  'QQmlPropertyToUnbindablePropertyBinding' as well, as Qt's
  QQmlBindableToUnbindablePropertyBinding is built on Qt's
  QQmlPropertyToUnbindablePropertyBinding too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQmlBindableToUnbindablePropertyBinding that has a
  ritual and that Python can call so far, 2 names in all: 'update',
  'captureProperty'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'typeinfo for
  QQmlPropertyToUnbindablePropertyBinding', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlBindableToUnbindablePropertyBinding is created at the first
    use, not by 'QQmlBindableToUnbindablePropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBindableToUnbindablePropertyBinding.
  - Each name of Qt's QQmlBindableToUnbindablePropertyBinding that has no
    cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPropertyObserver, QUntypedPropertyData)
  @overload(QPropertyObserver, NoneType)
  @overload(NoneType, QUntypedPropertyData)
  @overload(NoneType, NoneType)
  def update(
      observer: Optional[QPropertyObserver],
      a1: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlBindableToUnbindablePropertyBinding::update(QPropertyObserver
    *observer, QUntypedPropertyData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindabletounbindablepropertybinding.html

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlBindableToUnbindablePropertyBinding::update(QPropertyObserver
    #      *observer, QUntypedPropertyData *a1)
    Rituals.call(
        'ritual_ZN39QQmlBindableToUnbindablePropertyBinding6updateEP17QProp'
        'ertyObserverP20QUntypedPropertyData',
        CuteMixin._addressOf(observer), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBindableToUnbindablePropertyBinding'

  #  Qt's QQmlBindableToUnbindablePropertyBinding is built on more than one
  #  class. The part of a C++ QQmlBindableToUnbindablePropertyBinding that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlPropertyToUnbindablePropertyBinding':
          'ritual_cast_QQmlBindableToUnbindablePropertyBinding_QQmlPropertyToUnbindablePropertyBinding',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlBindableToUnbindablePropertyBinding::
    QQmlBindableToUnbindablePropertyBinding(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target)': leans on 'typeinfo
    for QQmlPropertyToUnbindablePropertyBinding', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlBindableToUnbindablePropertyBinding.__init__' has no cute "
        "function yet. Qt's "
        "'QQmlBindableToUnbindablePropertyBinding::QQmlBindableToUnbindableP"
        "ropertyBinding(QQmlEngine *engine, const QQmlProperty &source, "
        "const QQmlProperty &target)': leans on 'typeinfo for "
        "QQmlPropertyToUnbindablePropertyBinding', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QMetaObject, QMetaProperty)
  @overload(NoneType, QMetaProperty)
  def captureProperty(
      self,
      sourceMetaObject: Optional[QMetaObject],
      sourceProperty: QMetaProperty,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlBindableToUnbindablePropertyBinding::captureProperty(const
    QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindabletounbindablepropertybinding.html

    Parameters
    ----------

    sourceMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceProperty : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlBindableToUnbindablePropertyBinding::captureProperty(const
    #      QMetaObject *sourceMetaObject, const QMetaProperty
    #      &sourceProperty)
    self.uglySide.call(
        'ritual_ZN39QQmlBindableToUnbindablePropertyBinding15capturePropert'
        'yEPK11QMetaObjectRK13QMetaProperty',
        self._addressOf(sourceMetaObject, 'QMetaObject'),
        self._valueOf(sourceProperty),
    )
