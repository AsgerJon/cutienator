"""
QQmlUnbindableToUnbindablePropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlUnbindableToUnbindablePropertyBinding to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlNotifierEndpoint, QQmlPropertyToUnbindablePropertyBinding

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlUnbindableToUnbindablePropertyBinding(QQmlNotifierEndpoint, QQmlPropertyToUnbindablePropertyBinding):
  """
  The cute side of Qt's QQmlUnbindableToUnbindablePropertyBinding: a plain
  Python object standing in front of one C++
  QQmlUnbindableToUnbindablePropertyBinding.

  It is built on the cute 'QQmlNotifierEndpoint', as Qt's
  QQmlUnbindableToUnbindablePropertyBinding is built on Qt's
  QQmlNotifierEndpoint, and has everything that class has. It is built on the
  cute 'QQmlPropertyToUnbindablePropertyBinding' as well, as Qt's
  QQmlUnbindableToUnbindablePropertyBinding is built on Qt's
  QQmlPropertyToUnbindablePropertyBinding too, and has everything that class
  has.

  C++ hands a QQmlUnbindableToUnbindablePropertyBinding around as a copy, so
  every C++ QQmlUnbindableToUnbindablePropertyBinding behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlUnbindableToUnbindablePropertyBinding that has a
  ritual and that Python can call so far, 1 name in all: 'captureProperty'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlUnbindableToUnbindablePropertyBinding::
    ~QQmlUnbindableToUnbindablePropertyBinding()': the destructor: Python
    removes its C++ QQmlUnbindableToUnbindablePropertyBinding by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'typeinfo for
  QQmlPropertyToUnbindablePropertyBinding', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlUnbindableToUnbindablePropertyBinding is created at the first
    use, not by 'QQmlUnbindableToUnbindablePropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlUnbindableToUnbindablePropertyBinding back gives
    a copy the ritual made for Python, in a new cute
    QQmlUnbindableToUnbindablePropertyBinding.
  - Each name of Qt's QQmlUnbindableToUnbindablePropertyBinding that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QQmlUnbindableToUnbindablePropertyBinding'

  #  Qt's QQmlUnbindableToUnbindablePropertyBinding is built on more than one
  #  class. The part of a C++ QQmlUnbindableToUnbindablePropertyBinding that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlPropertyToUnbindablePropertyBinding':
          'ritual_cast_QQmlUnbindableToUnbindablePropertyBinding_QQmlPropertyToUnbindablePropertyBinding',
  }

  #  A C++ QQmlUnbindableToUnbindablePropertyBinding Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlUnbindableToUnbindablePropertyBinding'

  #  Qt's '~QQmlUnbindableToUnbindablePropertyBinding()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QQmlUnbindableToUnbindablePropertyBinding behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN41QQmlUnbindableToUnbindablePropertyBindingD1Ev')

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
    Qt's 'QQmlUnbindableToUnbindablePropertyBinding::
    QQmlUnbindableToUnbindablePropertyBinding(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target)': leans on 'typeinfo
    for QQmlPropertyToUnbindablePropertyBinding', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlUnbindableToUnbindablePropertyBinding.__init__' has no cute "
        "function yet. Qt's "
        "'QQmlUnbindableToUnbindablePropertyBinding::QQmlUnbindableToUnbinda"
        "blePropertyBinding(QQmlEngine *engine, const QQmlProperty &source, "
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
    QQmlUnbindableToUnbindablePropertyBinding::captureProperty(const
    QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlunbindabletounbindablepropertybinding.html

    Parameters
    ----------

    sourceMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceProperty : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlUnbindableToUnbindablePropertyBinding::captureProperty(const
    #      QMetaObject *sourceMetaObject, const QMetaProperty
    #      &sourceProperty)
    self.uglySide.call(
        'ritual_ZN41QQmlUnbindableToUnbindablePropertyBinding15capturePrope'
        'rtyEPK11QMetaObjectRK13QMetaProperty',
        self._addressOf(sourceMetaObject, 'QMetaObject'),
        self._valueOf(sourceProperty),
    )
