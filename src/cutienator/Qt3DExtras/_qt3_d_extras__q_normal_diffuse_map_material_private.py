"""
Qt3DExtras::QNormalDiffuseMapMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qnormaldiffusemapmaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::QNormalDiffuseMapMaterialPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
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


class QNormalDiffuseMapMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QNormalDiffuseMapMaterialPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QNormalDiffuseMapMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QNormalDiffuseMapMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QNormalDiffuseMapMaterialPrivate that
  has a ritual and that Python can call so far, 8 names in all: 'init',
  'handleAmbientChanged', 'handleDiffuseChanged', 'handleNormalChanged',
  'handleSpecularChanged', 'handleShininessChanged',
  'handleTextureScaleChanged', 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QNormalDiffuseMapMaterial
    *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func() const': takes in
    Python what 'QNormalDiffuseMapMaterial
    *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QNormalDiffuseMapMaterialPrivate is created at the
    first use, not by 'Qt3DExtras::QNormalDiffuseMapMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QNormalDiffuseMapMaterialPrivate'

  #  A C++ Qt3DExtras::QNormalDiffuseMapMaterialPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QNormalDiffuseMapMaterialPrivate'

  #  The functions Qt calls itself that
  #  Qt3DExtras::QNormalDiffuseMapMaterialPrivate is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv',
           ('nothing', 'nothing', ''),
           ()),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    QNormalDiffuseMapMaterialPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html
    """
    #  Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      QNormalDiffuseMapMaterialPrivate()
    self._noteCreation(
        QNormalDiffuseMapMaterialPrivate, lambda: Rituals.call(
            'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init()
    ritual = 'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4init'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QVariant)
  def handleAmbientChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleAmbientChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      handleAmbientChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleAmb'
        'ientChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleDiffuseChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleDiffuseChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      handleDiffuseChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleDif'
        'fuseChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleNormalChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleNormalChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleNormalChanged(
    #      const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate19handleNor'
        'malChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleSpecularChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleSpecularChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      handleSpecularChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate21handleSpe'
        'cularChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleShininessChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleShininessChanged(
    const QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      handleShininessChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate22handleShi'
        'ninessChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleTextureScaleChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleTextureScaleChanged(
    const QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::
    #      handleTextureScaleChanged(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate25handleTex'
        'tureScaleChangedERK8QVariant',
        self._valueOf(var),
    )

  def q_func(self) -> Optional[Qt3DExtras.QNormalDiffuseMapMaterial]:
    """
    Calls Qt's 'QNormalDiffuseMapMaterial
    *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterialprivate.html

    Returns
    -------

    Optional[Qt3DExtras.QNormalDiffuseMapMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNormalDiffuseMapMaterial
    #      *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QNormalDiffuseMapMaterial._cuteAt(address)
