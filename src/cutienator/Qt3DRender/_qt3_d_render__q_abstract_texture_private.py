"""
Qt3DRender::QAbstractTexturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qabstracttexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QAbstractTexturePrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QAbstractTexturePrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QAbstractTexturePrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QAbstractTexturePrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::QAbstractTexturePrivate is built on Qt's
  Qt3DCore::QNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractTexturePrivate that has a
  ritual and that Python can call so far, 4 names in all: 'q_func',
  'setStatus', 'setHandle', 'setHandleType'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractTexture
    *Qt3DRender::QAbstractTexturePrivate::q_func() const': takes in Python
    what 'QAbstractTexture *Qt3DRender::QAbstractTexturePrivate::q_func()'
    takes.
  - Qt's 'QTextureGeneratorPtr
    Qt3DRender::QAbstractTexturePrivate::dataFunctor() const': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DRender::QAbstractTexturePrivate::setDataFunctor(const
    QTextureGeneratorPtr &generator)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractTexturePrivate is created at the first use,
    not by 'Qt3DRender::QAbstractTexturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractTexturePrivate.
  - Each name of Qt's Qt3DRender::QAbstractTexturePrivate that has no cute
    function yet, 'dataFunctor', 'setDataFunctor', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractTexturePrivate'

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

  @overload(Qt3DRender.QAbstractTexture.Status)
  def setStatus(self, status: Qt3DRender.QAbstractTexture.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexturePrivate::setStatus(QAbstractTexture::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureprivate.html#setStatus

    Parameters
    ----------

    status : Qt3DRender.QAbstractTexture.Status
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexturePrivate::setStatus(QAbstractTexture::
    #      Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAbstractTexturePrivate9setStatusENS_16QAbs'
        'tractTexture6StatusE',
        status.value,
    )

  @overload(QVariant)
  def setHandle(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexturePrivate::setHandle(const
    QVariant &handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureprivate.html#setHandle

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QAbstractTexturePrivate::setHandle(const QVariant
    #      &handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAbstractTexturePrivate9setHandleERK8QVaria'
        'nt',
        self._valueOf(handle),
    )

  @overload(Qt3DRender.QAbstractTexture.HandleType)
  def setHandleType(
      self,
      type: Qt3DRender.QAbstractTexture.HandleType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexturePrivate::setHandleType(QAbstractTexture::
    HandleType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureprivate.html

    Parameters
    ----------

    type : Qt3DRender.QAbstractTexture.HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexturePrivate::setHandleType(
    #      QAbstractTexture::HandleType type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAbstractTexturePrivate13setHandleTypeENS_1'
        '6QAbstractTexture10HandleTypeE',
        type.value,
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
    'Qt3DRender::QAbstractTexturePrivate::QAbstractTexturePrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureprivate.html
    """
    #  Qt3DRender::QAbstractTexturePrivate::QAbstractTexturePrivate()
    self._noteCreation(QAbstractTexturePrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender23QAbstractTexturePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'QAbstractTexture
    *Qt3DRender::QAbstractTexturePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTexture *Qt3DRender::QAbstractTexturePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAbstractTexturePrivate6q_funcEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  @staticmethod
  def dataFunctor(*__, **_) -> Never:
    """
    Qt's 'QTextureGeneratorPtr
    Qt3DRender::QAbstractTexturePrivate::dataFunctor() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTexturePrivate.dataFunctor' has no cute "
        "function yet. Qt's 'QTextureGeneratorPtr "
        "Qt3DRender::QAbstractTexturePrivate::dataFunctor() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setDataFunctor(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAbstractTexturePrivate::setDataFunctor(const
    QTextureGeneratorPtr &generator)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTexturePrivate.setDataFunctor' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::QAbstractTexturePrivate::setDataFunctor(const "
        "QTextureGeneratorPtr &generator)': takes a type Python has no way "
        "to hand over yet.")
