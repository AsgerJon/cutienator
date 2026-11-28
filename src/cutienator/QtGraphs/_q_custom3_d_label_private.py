"""
QCustom3DLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qcustom3dlabel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCustom3DLabelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCustom3DItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QFont, QQuaternion, QVector3D
  from . import QCustom3DLabel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class QCustom3DLabelPrivate(QCustom3DItemPrivate):
  """
  The cute side of Qt's QCustom3DLabelPrivate: a plain Python object standing
  in front of one C++ QCustom3DLabelPrivate.

  It is built on the cute 'QCustom3DItemPrivate', as Qt's
  QCustom3DLabelPrivate is built on Qt's QCustom3DItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DLabelPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'resetDirtyBits'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCustom3DLabel *QCustom3DLabelPrivate::q_func() const': takes
    in Python what 'QCustom3DLabel *QCustom3DLabelPrivate::q_func()' takes.
  - Qt's 'QCustom3DLabelPrivate::~QCustom3DLabelPrivate()': the destructor:
    Python never removes a C++ QCustom3DLabelPrivate.

  What to expect
  --------------

  - The C++ QCustom3DLabelPrivate is created at the first use, not by
    'QCustom3DLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DLabelPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DLabelPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

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
    'QCustom3DLabelPrivate::QCustom3DLabelPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#QCustom3DLabelPrivate
    """
    #  QCustom3DLabelPrivate::QCustom3DLabelPrivate()
    self._noteCreation(QCustom3DLabelPrivate, lambda: Rituals.call(
        'ritual_ZN21QCustom3DLabelPrivateC1Ev',
    ))

  @overload(str, QFont, QVector3D, QVector3D, QQuaternion)
  def __init__(
      self,
      text: str,
      font: QFont,
      position: QVector3D,
      scaling: QVector3D,
      rotation: QQuaternion,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCustom3DLabelPrivate::QCustom3DLabelPrivate(const QString &text, const
    QFont &font, QVector3D position, QVector3D scaling, const QQuaternion
    &rotation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#QCustom3DLabelPrivate

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  QCustom3DLabelPrivate::QCustom3DLabelPrivate(const QString &text,
    #      const QFont &font, QVector3D position, QVector3D scaling, const
    #      QQuaternion &rotation)
    self._noteCreation(QCustom3DLabelPrivate, lambda: Rituals.call(
        'ritual_ZN21QCustom3DLabelPrivateC1ERK7QStringRK5QFont9QVector3DS6_'
        'RK11QQuaternion',
        text, self._valueOf(font), self._valueOf(position),
        self._valueOf(scaling), self._valueOf(rotation),
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

  def q_func(self) -> Optional[QCustom3DLabel]:
    """
    Calls Qt's 'QCustom3DLabel *QCustom3DLabelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#q_func

    Returns
    -------

    Optional[QCustom3DLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DLabel *QCustom3DLabelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QCustom3DLabelPrivate6q_funcEv')
    from . import QCustom3DLabel
    return QCustom3DLabel._cuteAt(address)

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QCustom3DLabelPrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#resetDirtyBits
    """
    #  void QCustom3DLabelPrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN21QCustom3DLabelPrivate14resetDirtyBitsEv')
