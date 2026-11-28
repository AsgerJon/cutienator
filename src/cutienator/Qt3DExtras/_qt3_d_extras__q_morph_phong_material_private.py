"""
Qt3DExtras::QMorphPhongMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qmorphphongmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QMorphPhongMaterialPrivate to be private: it declares
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


class QMorphPhongMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QMorphPhongMaterialPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QMorphPhongMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QMorphPhongMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QMorphPhongMaterialPrivate that has a
  ritual and that Python can call so far, 7 names in all: 'init',
  'handleAmbientChanged', 'handleDiffuseChanged', 'handleSpecularChanged',
  'handleShininessChanged', 'handleInterpolatorChanged', 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMorphPhongMaterial
    *Qt3DExtras::QMorphPhongMaterialPrivate::q_func() const': takes in Python
    what 'QMorphPhongMaterial
    *Qt3DExtras::QMorphPhongMaterialPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QMorphPhongMaterialPrivate is created at the first
    use, not by 'Qt3DExtras::QMorphPhongMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QMorphPhongMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QMorphPhongMaterialPrivate'

  #  A C++ Qt3DExtras::QMorphPhongMaterialPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QMorphPhongMaterialPrivate'

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
    'Qt3DExtras::QMorphPhongMaterialPrivate::QMorphPhongMaterialPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html
    """
    #  Qt3DExtras::QMorphPhongMaterialPrivate::QMorphPhongMaterialPrivate()
    self._noteCreation(QMorphPhongMaterialPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html#init
    """
    #  void Qt3DExtras::QMorphPhongMaterialPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate4initEv',
    )

  @overload(QVariant)
  def handleAmbientChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterialPrivate::handleAmbientChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DExtras::QMorphPhongMaterialPrivate::handleAmbientChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleAmbientCh'
        'angedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleDiffuseChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterialPrivate::handleDiffuseChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DExtras::QMorphPhongMaterialPrivate::handleDiffuseChanged(const
    #      QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleDiffuseCh'
        'angedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleSpecularChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterialPrivate::handleSpecularChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterialPrivate::handleSpecularChanged(
    #      const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate21handleSpecularC'
        'hangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleShininessChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterialPrivate::handleShininessChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterialPrivate::handleShininessChanged(
    #      const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate22handleShininess'
        'ChangedERK8QVariant',
        self._valueOf(var),
    )

  @overload(QVariant)
  def handleInterpolatorChanged(self, var: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterialPrivate::handleInterpolatorChanged(const
    QVariant &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DExtras::QMorphPhongMaterialPrivate::handleInterpolatorChanged(
    #      const QVariant &var)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate25handleInterpola'
        'torChangedERK8QVariant',
        self._valueOf(var),
    )

  def q_func(self) -> Optional[Qt3DExtras.QMorphPhongMaterial]:
    """
    Calls Qt's 'QMorphPhongMaterial
    *Qt3DExtras::QMorphPhongMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterialprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QMorphPhongMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphPhongMaterial *Qt3DExtras::QMorphPhongMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QMorphPhongMaterial._cuteAt(address)
