"""
QQuickImageBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickimagebase_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickImageBasePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QQuickImageBase, QQuickImplicitSizeItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageBasePrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickImageBasePrivate: a plain Python object
  standing in front of one C++ QQuickImageBasePrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickImageBasePrivate is built on Qt's QQuickImplicitSizeItemPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageBasePrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'get',
  'updateDevicePixelRatio', 'setStatus', 'setProgress'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickImageBase *QQuickImageBasePrivate::q_func() const':
    takes in Python what 'QQuickImageBase *QQuickImageBasePrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickImageBasePrivate is created at the first use, not by
    'QQuickImageBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageBasePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickImageBase)
  @overload(NoneType)
  def get(
      image: Optional[QQuickImageBase],
  ) -> Optional[QQuickImageBasePrivate]:
    """
    Calls Qt's 'QQuickImageBasePrivate
    *QQuickImageBasePrivate::get(QQuickImageBase *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebaseprivate.html#get

    Parameters
    ----------

    image : Optional[QQuickImageBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickImageBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageBasePrivate *QQuickImageBasePrivate::get(QQuickImageBase
    #      *image)
    address = Rituals.call(
        'ritual_ZN22QQuickImageBasePrivate3getEP15QQuickImageBase',
        CuteMixin._addressOf(image),
    )
    return QQuickImageBasePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageBasePrivate'

  #  A C++ QQuickImageBasePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageBasePrivate'

  #  The functions Qt calls itself that QQuickImageBasePrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateDevicePixelRatio': (
          ('_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
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

  @overload(QQuickImageBase.Status)
  def setStatus(self, value: QQuickImageBase.Status) -> None:
    """
    Calls Qt's 'void
    QQuickImageBasePrivate::setStatus(QQuickImageBase::Status value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebaseprivate.html#setStatus

    Parameters
    ----------

    value : QQuickImageBase.Status
      Passed on as its number.
    """
    #  void QQuickImageBasePrivate::setStatus(QQuickImageBase::Status value)
    self.uglySide.call(
        'ritual_ZN22QQuickImageBasePrivate9setStatusEN15QQuickImageBase6Sta'
        'tusE',
        value.value,
    )

  @overload(float)
  def setProgress(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickImageBasePrivate::setProgress(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebaseprivate.html#setProgress

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickImageBasePrivate::setProgress(qreal value)
    self.uglySide.call(
        'ritual_ZN22QQuickImageBasePrivate11setProgressEd', value,
    )

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
    'QQuickImageBasePrivate::QQuickImageBasePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebaseprivate.html#QQuickImageBasePrivate
    """
    #  QQuickImageBasePrivate::QQuickImageBasePrivate()
    self._noteCreation(QQuickImageBasePrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickImageBasePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickImageBase]:
    """
    Calls Qt's 'QQuickImageBase *QQuickImageBasePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebaseprivate.html#q_func

    Returns
    -------

    Optional[QQuickImageBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageBase *QQuickImageBasePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickImageBasePrivate6q_funcEv',
    )
    return QQuickImageBase._cuteAt(address)

  @overload(float)
  def updateDevicePixelRatio(self, targetDevicePixelRatio: float) -> bool:
    """
    Calls Qt's 'bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
    targetDevicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebaseprivate.html#updateDevicePixelRatio

    Parameters
    ----------

    targetDevicePixelRatio : float
      Passed on as it is.
    """
    #  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
    #      targetDevicePixelRatio)
    ritual = 'ritual_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd')
    return self.uglySide.call(ritual, targetDevicePixelRatio)
