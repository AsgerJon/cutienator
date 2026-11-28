"""
Qt3DExtras::QTextureMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtexturematerial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QTextureMaterialPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QTextureMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QTextureMaterialPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QTextureMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QTextureMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTextureMaterialPrivate that has a
  ritual and that Python can call so far, 4 names in all: 'init',
  'handleTextureChanged', 'handleTextureTransformChanged', 'q_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextureMaterial
    *Qt3DExtras::QTextureMaterialPrivate::q_func() const': takes in Python
    what 'QTextureMaterial *Qt3DExtras::QTextureMaterialPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTextureMaterialPrivate is created at the first use,
    not by 'Qt3DExtras::QTextureMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTextureMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QTextureMaterialPrivate'

  #  A C++ Qt3DExtras::QTextureMaterialPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QTextureMaterialPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QTextureMaterialPrivate::QTextureMaterialPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerialprivate.html
    """
    #  Qt3DExtras::QTextureMaterialPrivate::QTextureMaterialPrivate()
    self._noteCreation(QTextureMaterialPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras23QTextureMaterialPrivateC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTextureMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerialprivate.html#init
    """
    #  void Qt3DExtras::QTextureMaterialPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QTextureMaterialPrivate4initEv',
    )

  @overload(QVariant)
  def handleTextureChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterialPrivate::handleTextureChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QTextureMaterialPrivate::handleTextureChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QTextureMaterialPrivate20handleTextureChang'
        'edERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleTextureTransformChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterialPrivate::handleTextureTransformChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QTextureMaterialPrivate::
    #      handleTextureTransformChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QTextureMaterialPrivate29handleTextureTrans'
        'formChangedERK8QVariant',
        self._valueOf(var),
    )

  def q_func(self) -> Optional[Qt3DExtras.QTextureMaterial]:
    """
    Calls Qt's 'QTextureMaterial
    *Qt3DExtras::QTextureMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerialprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QTextureMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureMaterial *Qt3DExtras::QTextureMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QTextureMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QTextureMaterial._cuteAt(address)
