"""
Qt3DCore::QBufferPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qbuffer_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::QBufferPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBufferPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DCore::QBufferPrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QBufferPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DCore::QBufferPrivate is built on Qt's Qt3DCore::QNodePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBufferPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'get', 'update',
  'setData'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBuffer *Qt3DCore::QBufferPrivate::q_func() const': takes in
    Python what 'QBuffer *Qt3DCore::QBufferPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QBufferPrivate is created at the first use, not by
    'Qt3DCore::QBufferPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBufferPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QBuffer'])
  @overload(NoneType)
  def get(q: Optional[Qt3DCore.QBuffer]) -> Optional[QBufferPrivate]:
    """
    Calls Qt's 'QBufferPrivate *Qt3DCore::QBufferPrivate::get(QBuffer *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbufferprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBufferPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBufferPrivate *Qt3DCore::QBufferPrivate::get(QBuffer *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore14QBufferPrivate3getEPNS_7QBufferE',
        CuteMixin._addressOf(q),
    )
    return QBufferPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBufferPrivate'

  #  A C++ Qt3DCore::QBufferPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBufferPrivate'

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

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBufferPrivate::setData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbufferprivate.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::QBufferPrivate::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QBufferPrivate7setDataERK10QByteArray',
        self._valueOf(data),
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
    'Qt3DCore::QBufferPrivate::QBufferPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbufferprivate.html#QBufferPrivate
    """
    #  Qt3DCore::QBufferPrivate::QBufferPrivate()
    self._noteCreation(QBufferPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QBufferPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QBuffer]:
    """
    Calls Qt's 'QBuffer *Qt3DCore::QBufferPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbufferprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBuffer *Qt3DCore::QBufferPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore14QBufferPrivate6q_funcEv',
    )
    return Qt3DCore.QBuffer._cuteAt(address)

  def update(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBufferPrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbufferprivate.html#update
    """
    #  void Qt3DCore::QBufferPrivate::update()
    ritual = 'ritual_ZN8Qt3DCore14QBufferPrivate6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore14QBufferPrivate6updateEv'
    self.uglySide.call(ritual)
