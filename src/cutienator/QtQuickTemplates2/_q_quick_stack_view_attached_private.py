"""
QQuickStackViewAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackViewAttachedPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick import QQuickItem
  from . import QQuickStackViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickStackViewAttached = WAIT['QQuickStackViewAttached']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackViewAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickStackViewAttachedPrivate: a plain Python object
  standing in front of one C++ QQuickStackViewAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickStackViewAttachedPrivate is built on Qt's QObjectPrivate, and has
  everything that class has. Qt's QQuickStackViewAttachedPrivate is built on
  Qt's QSafeQuickItemChangeListener<QQuickStackViewAttachedPrivate> as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickStackViewAttachedPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func', 'get',
  'itemParentChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickStackViewAttached
    *QQuickStackViewAttachedPrivate::q_func() const': takes in Python what
    'QQuickStackViewAttached *QQuickStackViewAttachedPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickStackViewAttachedPrivate is created at the first use, not
    by 'QQuickStackViewAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackViewAttachedPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickStackViewAttached)
  @overload(NoneType)
  def get(
      attached: Optional[QQuickStackViewAttached],
  ) -> Optional[QQuickStackViewAttachedPrivate]:
    """
    Calls Qt's 'QQuickStackViewAttachedPrivate
    *QQuickStackViewAttachedPrivate::get(QQuickStackViewAttached *attached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattachedprivate.html#get

    Parameters
    ----------

    attached : Optional[QQuickStackViewAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickStackViewAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewAttachedPrivate
    #      *QQuickStackViewAttachedPrivate::get(QQuickStackViewAttached
    #      *attached)
    address = Rituals.call(
        'ritual_ZN30QQuickStackViewAttachedPrivate3getEP23QQuickStackViewAt'
        'tached',
        CuteMixin._addressOf(attached),
    )
    return QQuickStackViewAttachedPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackViewAttachedPrivate'

  #  A C++ QQuickStackViewAttachedPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStackViewAttachedPrivate'

  #  The functions Qt calls itself that QQuickStackViewAttachedPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemParentChanged': (
          ('_ZN30QQuickStackViewAttachedPrivate17itemParentChangedEP10QQuic'
           'kItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  def q_func(self) -> Optional[QQuickStackViewAttached]:
    """
    Calls Qt's 'QQuickStackViewAttached
    *QQuickStackViewAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickStackViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewAttached *QQuickStackViewAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickStackViewAttachedPrivate6q_funcEv',
    )
    from . import QQuickStackViewAttached
    return QQuickStackViewAttached._cuteAt(address)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      item: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickStackViewAttachedPrivate::itemParentChanged(QQuickItem *item,
    QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattachedprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackViewAttachedPrivate::itemParentChanged(QQuickItem
    #      *item, QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN30QQuickStackViewAttachedPrivate17itemParentChangedEP10QQ'
        'uickItemS1_',
        self._addressOf(item), self._addressOf(parent),
    )
