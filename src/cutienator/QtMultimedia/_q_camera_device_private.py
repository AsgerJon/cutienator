"""
QCameraDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCameraDevicePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCameraDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCameraDevice = WAIT['QCameraDevice']


class QCameraDevicePrivate(QSharedData):
  """
  The cute side of Qt's QCameraDevicePrivate: a plain Python object standing
  in front of one C++ QCameraDevicePrivate.

  It is built on the cute 'QSharedData', as Qt's QCameraDevicePrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QCameraDevicePrivate around as a copy, so every C++
  QCameraDevicePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCameraDevicePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'handle', '__eq__', 'create'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCameraDevicePrivate *QCameraDevicePrivate::handle(QCameraDevice
    &device)': takes a type Python has no way to hand over yet.
  - Qt's 'QCameraDevicePrivate::~QCameraDevicePrivate()': the destructor:
    Python removes its C++ QCameraDevicePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCameraDevicePrivate is created at the first use, not by
    'QCameraDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCameraDevicePrivate back gives a copy the ritual
    made for Python, in a new cute QCameraDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCameraDevice)
  def handle(device: QCameraDevice) -> Optional[QCameraDevicePrivate]:
    """
    Calls Qt's 'const QCameraDevicePrivate
    *QCameraDevicePrivate::handle(const QCameraDevice &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradeviceprivate.html#handle

    Parameters
    ----------

    device : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.

    Returns
    -------

    Optional[QCameraDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCameraDevicePrivate *QCameraDevicePrivate::handle(const
    #      QCameraDevice &device)
    address = Rituals.call(
        'ritual_ZN20QCameraDevicePrivate6handleERK13QCameraDevice',
        CuteMixin._valueOf(device),
    )
    return QCameraDevicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCameraDevicePrivate'

  #  Qt's '~QCameraDevicePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCameraDevicePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCameraDevicePrivateD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QCameraDevicePrivate) -> bool:
    """
    Calls Qt's 'bool QCameraDevicePrivate::operator==(const
    QCameraDevicePrivate &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcameradeviceprivate.html#operator==

    Parameters
    ----------

    other : QCameraDevicePrivate
      Passed on as a value: Qt reads the C++ QCameraDevicePrivate, which
      stays Python's own.
    """
    #  bool QCameraDevicePrivate::operator==(const QCameraDevicePrivate
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK20QCameraDevicePrivateeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def create(self) -> QCameraDevice:
    """
    Calls Qt's 'QCameraDevice QCameraDevicePrivate::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradeviceprivate.html#create

    Returns
    -------

    QCameraDevice
      A new cute QCameraDevice around the copy Qt gave back. Python owns it.
    """
    #  QCameraDevice QCameraDevicePrivate::create()
    address = self.uglySide.call('ritual_ZN20QCameraDevicePrivate6createEv')
    from . import QCameraDevice
    return QCameraDevice._cuteOwning(address)
