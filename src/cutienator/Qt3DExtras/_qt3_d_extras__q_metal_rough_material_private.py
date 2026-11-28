"""
Qt3DExtras::QMetalRoughMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qmetalroughmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QMetalRoughMaterialPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QStringList
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


class QMetalRoughMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QMetalRoughMaterialPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QMetalRoughMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QMetalRoughMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QMetalRoughMaterialPrivate that has a
  ritual and that Python can call so far, 5 names in all: 'init',
  'handleTextureScaleChanged', 'updateLayersOnTechnique',
  'updateVertexShaderBasedOnLayers', 'q_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMetalRoughMaterial
    *Qt3DExtras::QMetalRoughMaterialPrivate::q_func() const': takes in Python
    what 'QMetalRoughMaterial
    *Qt3DExtras::QMetalRoughMaterialPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QMetalRoughMaterialPrivate is created at the first
    use, not by 'Qt3DExtras::QMetalRoughMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QMetalRoughMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QMetalRoughMaterialPrivate'

  #  A C++ Qt3DExtras::QMetalRoughMaterialPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QMetalRoughMaterialPrivate'

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
    'Qt3DExtras::QMetalRoughMaterialPrivate::QMetalRoughMaterialPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html
    """
    #  Qt3DExtras::QMetalRoughMaterialPrivate::QMetalRoughMaterialPrivate()
    self._noteCreation(QMetalRoughMaterialPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html#init
    """
    #  void Qt3DExtras::QMetalRoughMaterialPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate4initEv',
    )

  @overload(QVariant)
  def handleTextureScaleChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterialPrivate::handleTextureScaleChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DExtras::QMetalRoughMaterialPrivate::handleTextureScaleChanged(
    #      const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate25handleTextureSc'
        'aleChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QStringList)
  def updateLayersOnTechnique(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterialPrivate::updateLayersOnTechnique(const
    QStringList &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DExtras::QMetalRoughMaterialPrivate::updateLayersOnTechnique(
    #      const QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate23updateLayersOnT'
        'echniqueERK5QListI7QStringE',
        self._valueOf(layers),
    )

  @overload(QStringList)
  def updateVertexShaderBasedOnLayers(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterialPrivate::updateVertexShaderBasedOnLayers(
    const QStringList &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DExtras::QMetalRoughMaterialPrivate::
    #      updateVertexShaderBasedOnLayers(const QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate31updateVertexSha'
        'derBasedOnLayersERK5QListI7QStringE',
        self._valueOf(layers),
    )

  def q_func(self) -> Optional[Qt3DExtras.QMetalRoughMaterial]:
    """
    Calls Qt's 'QMetalRoughMaterial
    *Qt3DExtras::QMetalRoughMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterialprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QMetalRoughMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetalRoughMaterial *Qt3DExtras::QMetalRoughMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QMetalRoughMaterial._cuteAt(address)
