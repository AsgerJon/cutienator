"""
QQuickParticleGroupData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleGroupData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickParticleData, QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleGroupData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickParticleGroupData: a plain Python object
  standing in front of one C++ QQuickParticleGroupData.

  C++ hands a QQuickParticleGroupData around as a copy, so every C++
  QQuickParticleGroupData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickParticleGroupData that has a ritual and that
  Python can call so far, 9 names in all: 'size', 'isActive', 'name',
  'setSize', 'recycle', 'initList', 'kill', 'newDatum', 'prepareRecycler'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickParticleGroupData::~QQuickParticleGroupData()': the
    destructor: Python removes its C++ QQuickParticleGroupData by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQuickParticleGroupData is created at the first use, not by
    'QQuickParticleGroupData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickParticleGroupData back gives a copy the ritual
    made for Python, in a new cute QQuickParticleGroupData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleGroupData'

  #  Qt's '~QQuickParticleGroupData()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickParticleGroupData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQuickParticleGroupDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QQuickParticleGroupData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroupdata.html#size
    """
    #  int QQuickParticleGroupData::size() const
    return self.uglySide.call('ritual_ZNK23QQuickParticleGroupData4sizeEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickParticleGroupData::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroupdata.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickParticleGroupData::name() const
    return self.uglySide.call('ritual_ZNK23QQuickParticleGroupData4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSize(self, newSize: int) -> None:
    """
    Calls Qt's 'void QQuickParticleGroupData::setSize(int newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#setSize

    Parameters
    ----------

    newSize : int
      Passed on as it is.
    """
    #  void QQuickParticleGroupData::setSize(int newSize)
    self.uglySide.call(
        'ritual_ZN23QQuickParticleGroupData7setSizeEi', newSize,
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

  @overload(str, QQuickParticleSystem)
  @overload(str, NoneType)
  def __init__(self, name: str, sys: Optional[QQuickParticleSystem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickParticleGroupData::QQuickParticleGroupData(const QString &name,
    QQuickParticleSystem *sys)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    sys : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickParticleGroupData::QQuickParticleGroupData(const QString &name,
    #      QQuickParticleSystem *sys)
    self._noteCreation(QQuickParticleGroupData, lambda: Rituals.call(
        'ritual_ZN23QQuickParticleGroupDataC1ERK7QStringP20QQuickParticleSy'
        'stem',
        name, self._addressOf(sys),
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

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleGroupData::isActive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#isActive
    """
    #  bool QQuickParticleGroupData::isActive()
    return self.uglySide.call(
        'ritual_ZN23QQuickParticleGroupData8isActiveEv',
    )

  def recycle(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleGroupData::recycle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#recycle
    """
    #  bool QQuickParticleGroupData::recycle()
    return self.uglySide.call('ritual_ZN23QQuickParticleGroupData7recycleEv')

  def initList(self) -> None:
    """
    Calls Qt's 'void QQuickParticleGroupData::initList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#initList
    """
    #  void QQuickParticleGroupData::initList()
    self.uglySide.call('ritual_ZN23QQuickParticleGroupData8initListEv')

  @overload(QQuickParticleData)
  @overload(NoneType)
  def kill(self, d: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleGroupData::kill(QQuickParticleData *d)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroupdata.html#kill

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleGroupData::kill(QQuickParticleData *d)
    self.uglySide.call(
        'ritual_ZN23QQuickParticleGroupData4killEP18QQuickParticleData',
        self._addressOf(d),
    )

  @overload(bool)
  def newDatum(self, respectsLimits: bool) -> Optional[QQuickParticleData]:
    """
    Calls Qt's 'QQuickParticleData *QQuickParticleGroupData::newDatum(bool
    respectsLimits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#newDatum

    Parameters
    ----------

    respectsLimits : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQuickParticleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleData *QQuickParticleGroupData::newDatum(bool
    #      respectsLimits)
    address = self.uglySide.call(
        'ritual_ZN23QQuickParticleGroupData8newDatumEb', respectsLimits,
    )
    from . import QQuickParticleData
    return QQuickParticleData._cuteAt(address)

  @overload(QQuickParticleData)
  @overload(NoneType)
  def prepareRecycler(self, d: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleGroupData::prepareRecycler(QQuickParticleData *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroupdata.html#prepareRecycler

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleGroupData::prepareRecycler(QQuickParticleData *d)
    self.uglySide.call(
        'ritual_ZN23QQuickParticleGroupData15prepareRecyclerEP18QQuickParti'
        'cleData',
        self._addressOf(d),
    )
