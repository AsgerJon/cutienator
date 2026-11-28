"""
Qt3DExtras::QGoochMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qgoochmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QGoochMaterialPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class QGoochMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QGoochMaterialPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QGoochMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QGoochMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QGoochMaterialPrivate that has a ritual
  and that Python can call so far, 9 names in all: 'init',
  'handleDiffuseChanged', 'handleSpecularChanged', 'handleCoolChanged',
  'handleWarmChanged', 'handleAlphaChanged', 'handleBetaChanged',
  'handleShininessChanged', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGoochMaterial *Qt3DExtras::QGoochMaterialPrivate::q_func()
    const': takes in Python what 'QGoochMaterial
    *Qt3DExtras::QGoochMaterialPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QGoochMaterialPrivate is created at the first use,
    not by 'Qt3DExtras::QGoochMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QGoochMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QGoochMaterialPrivate'

  #  A C++ Qt3DExtras::QGoochMaterialPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QGoochMaterialPrivate'

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
    'Qt3DExtras::QGoochMaterialPrivate::QGoochMaterialPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html
    """
    #  Qt3DExtras::QGoochMaterialPrivate::QGoochMaterialPrivate()
    self._noteCreation(QGoochMaterialPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QGoochMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html#init
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::init()
    self.uglySide.call('ritual_ZN10Qt3DExtras21QGoochMaterialPrivate4initEv')

  @overload(QVariant)
  def handleDiffuseChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleDiffuseChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleDiffuseChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate20handleDiffuseChanged'
        'ERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleSpecularChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleSpecularChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleSpecularChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate21handleSpecularChange'
        'dERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleCoolChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleCoolChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleCoolChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleCoolChangedERK'
        '8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleWarmChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleWarmChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleWarmChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleWarmChangedERK'
        '8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleAlphaChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleAlphaChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleAlphaChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate18handleAlphaChangedER'
        'K8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleBetaChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleBetaChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleBetaChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleBetaChangedERK'
        '8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleShininessChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QGoochMaterialPrivate::handleShininessChanged(const QVariant
    &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterialPrivate::handleShininessChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate22handleShininessChang'
        'edERK8QVariant',
        self._valueOf(var),
    )

  def q_func(self) -> Optional[Qt3DExtras.QGoochMaterial]:
    """
    Calls Qt's 'QGoochMaterial *Qt3DExtras::QGoochMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterialprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QGoochMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGoochMaterial *Qt3DExtras::QGoochMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QGoochMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QGoochMaterial._cuteAt(address)
