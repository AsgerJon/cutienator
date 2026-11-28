"""
QQuickIconImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIconImagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtQuick import QQuickImagePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickIconImage


class QQuickIconImagePrivate(QQuickImagePrivate):
  """
  The cute side of Qt's QQuickIconImagePrivate: a plain Python object
  standing in front of one C++ QQuickIconImagePrivate.

  It is built on the cute 'QQuickImagePrivate', as Qt's
  QQuickIconImagePrivate is built on Qt's QQuickImagePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickIconImagePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'updateFillMode',
  'updateDevicePixelRatio'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickIconImage *QQuickIconImagePrivate::q_func() const':
    takes in Python what 'QQuickIconImage *QQuickIconImagePrivate::q_func()'
    takes.
  - Qt's 'QQuickIconImagePrivate::~QQuickIconImagePrivate()': the destructor:
    Python never removes a C++ QQuickIconImagePrivate.

  What to expect
  --------------

  - The C++ QQuickIconImagePrivate is created at the first use, not by
    'QQuickIconImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIconImagePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIconImagePrivate'

  #  A C++ QQuickIconImagePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickIconImagePrivate'

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

  def q_func(self) -> Optional[QQuickIconImage]:
    """
    Calls Qt's 'QQuickIconImage *QQuickIconImagePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimageprivate.html#q_func

    Returns
    -------

    Optional[QQuickIconImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIconImage *QQuickIconImagePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickIconImagePrivate6q_funcEv',
    )
    from . import QQuickIconImage
    return QQuickIconImage._cuteAt(address)

  def updateFillMode(self) -> None:
    """
    Calls Qt's 'void QQuickIconImagePrivate::updateFillMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimageprivate.html#updateFillMode
    """
    #  void QQuickIconImagePrivate::updateFillMode()
    self.uglySide.call('ritual_ZN22QQuickIconImagePrivate14updateFillModeEv')

  @overload(float)
  def updateDevicePixelRatio(self, targetDevicePixelRatio: float) -> bool:
    """
    Calls Qt's 'bool QQuickIconImagePrivate::updateDevicePixelRatio(qreal
    targetDevicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimageprivate.html#updateDevicePixelRatio

    Parameters
    ----------

    targetDevicePixelRatio : float
      Passed on as it is.
    """
    #  bool QQuickIconImagePrivate::updateDevicePixelRatio(qreal
    #      targetDevicePixelRatio)
    ritual = 'ritual_ZN22QQuickIconImagePrivate22updateDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickIconImagePrivate22updateDevicePixelRatioEd')
    return self.uglySide.call(ritual, targetDevicePixelRatio)
