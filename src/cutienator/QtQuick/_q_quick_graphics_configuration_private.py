"""
QQuickGraphicsConfigurationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickgraphicsconfiguration_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphicsConfigurationPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickGraphicsConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphicsConfigurationPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphicsConfigurationPrivate: a plain Python
  object standing in front of one C++ QQuickGraphicsConfigurationPrivate.

  C++ hands a QQuickGraphicsConfigurationPrivate around as a copy, so every
  C++ QQuickGraphicsConfigurationPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQuickGraphicsConfigurationPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'get'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickGraphicsConfigurationPrivate
    *QQuickGraphicsConfigurationPrivate::get(const
    QQuickGraphicsConfiguration *p)': takes in Python what
    'QQuickGraphicsConfigurationPrivate
    *QQuickGraphicsConfigurationPrivate::get(QQuickGraphicsConfiguration *p)'
    takes.
  - Qt's
    'QQuickGraphicsConfigurationPrivate::~QQuickGraphicsConfigurationPrivate(
    )': the destructor: Python removes its C++
    QQuickGraphicsConfigurationPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickGraphicsConfigurationPrivate is created at the first use,
    not by 'QQuickGraphicsConfigurationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGraphicsConfigurationPrivate back gives a copy
    the ritual made for Python, in a new cute
    QQuickGraphicsConfigurationPrivate.
  """

  #  The enums Qt writes inside QQuickGraphicsConfigurationPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QQuickGraphicsConfigurationPrivate::Flag' of Qt, with the
    6 names Qt gives in it. Qt names the type of its combinations
    'QQuickGraphicsConfigurationPrivate::Flags'.
    """

    UseDepthBufferFor2D = 0x1
    EnableDebugLayer = 0x2
    EnableDebugMarkers = 0x4
    PreferSoftwareDevice = 0x8
    AutoPipelineCache = 0x10
    EnableTimestamps = 0x20

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickGraphicsConfiguration)
  @overload(NoneType)
  def get(
      p: Optional[QQuickGraphicsConfiguration],
  ) -> Optional[QQuickGraphicsConfigurationPrivate]:
    """
    Calls Qt's 'QQuickGraphicsConfigurationPrivate
    *QQuickGraphicsConfigurationPrivate::get(QQuickGraphicsConfiguration
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfigurationprivate.html#get

    Parameters
    ----------

    p : Optional[QQuickGraphicsConfiguration]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickGraphicsConfigurationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphicsConfigurationPrivate
    #      *QQuickGraphicsConfigurationPrivate::get(
    #      QQuickGraphicsConfiguration *p)
    address = Rituals.call(
        'ritual_ZN34QQuickGraphicsConfigurationPrivate3getEP27QQuickGraphic'
        'sConfiguration',
        CuteMixin._addressOf(p),
    )
    return QQuickGraphicsConfigurationPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphicsConfigurationPrivate'

  #  Qt's '~QQuickGraphicsConfigurationPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QQuickGraphicsConfigurationPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN34QQuickGraphicsConfigurationPrivateD1Ev'

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
    'QQuickGraphicsConfigurationPrivate::QQuickGraphicsConfigurationPrivate(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfigurationprivate.html
    """
    #  QQuickGraphicsConfigurationPrivate::
    #      QQuickGraphicsConfigurationPrivate()
    self._noteCreation(
        QQuickGraphicsConfigurationPrivate, lambda: Rituals.call(
            'ritual_ZN34QQuickGraphicsConfigurationPrivateC1Ev',
        ))

  @overload(THIS)
  def __init__(self, other: QQuickGraphicsConfigurationPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphicsConfigurationPrivate::QQuickGraphicsConfigurationPrivate(
    const QQuickGraphicsConfigurationPrivate &other)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfigurationprivate.html

    Parameters
    ----------

    other : QQuickGraphicsConfigurationPrivate
      Passed on as a value: Qt reads the C++
      QQuickGraphicsConfigurationPrivate, which stays Python's own.
    """
    #  QQuickGraphicsConfigurationPrivate::
    #      QQuickGraphicsConfigurationPrivate(const
    #      QQuickGraphicsConfigurationPrivate &other)
    self._noteCreation(
        QQuickGraphicsConfigurationPrivate, lambda: Rituals.call(
            'ritual_ZN34QQuickGraphicsConfigurationPrivateC1ERKS_',
            self._valueOf(other),
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
