"""
QQuickAttachedPropertyPropagatorTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagatortarget_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAttachedPropertyPropagatorTarget to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAttachedPropertyPropagatorTarget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAttachedPropertyPropagatorTarget: a plain
  Python object standing in front of one C++
  QQuickAttachedPropertyPropagatorTarget.

  What exists
  -----------

  Every function of Qt's QQuickAttachedPropertyPropagatorTarget that has a
  ritual and that Python can call so far, 2 names in all: 'attacheeItem',
  'attachedParent'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickAttachedPropertyPropagatorTarget::
    ~QQuickAttachedPropertyPropagatorTarget()': the destructor: Python never
    removes a C++ QQuickAttachedPropertyPropagatorTarget.

  What to expect
  --------------

  - The C++ QQuickAttachedPropertyPropagatorTarget is created at the first
    use, not by 'QQuickAttachedPropertyPropagatorTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAttachedPropertyPropagatorTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAttachedPropertyPropagatorTarget'

  #  A C++ QQuickAttachedPropertyPropagatorTarget Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAttachedPropertyPropagatorTarget'

  #  The functions Qt calls itself that
  #  QQuickAttachedPropertyPropagatorTarget is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'attacheeItem': (
          ('_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv',
           ('address', 'address', 'QtQuick:QQuickItem'),
           ()),
      ),
      'attachedParent': (
          ('_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK'
           '11QMetaObject',
           ('address', 'address',
            'QtQuick:QtPrivate.QQuickAttachedPropertyPropagator'),
           (
               ('address', 'address', 'QtCore:QMetaObject'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def attacheeItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickAttachedPropertyPropagatorTarget::attacheeItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagatortarget.html

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAttachedPropertyPropagatorTarget::attacheeItem()
    #      const
    address = self._callAs(
        'QQuickAttachedPropertyPropagatorTarget',
        'ritual_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def attachedParent(
      self,
      attachedType: Optional[QMetaObject],
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QtPrivate::QQuickAttachedPropertyPropagator
    *QQuickAttachedPropertyPropagatorTarget::attachedParent(const QMetaObject
    *attachedType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagatortarget.html

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtPrivate::QQuickAttachedPropertyPropagator
    #      *QQuickAttachedPropertyPropagatorTarget::attachedParent(const
    #      QMetaObject *attachedType) const
    address = self._callAs(
        'QQuickAttachedPropertyPropagatorTarget',
        'ritual_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParent'
        'EPK11QMetaObject',
        self._addressOf(attachedType, 'QMetaObject'),
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)

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
