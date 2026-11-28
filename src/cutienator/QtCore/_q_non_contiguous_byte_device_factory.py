"""
QNonContiguousByteDeviceFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNonContiguousByteDeviceFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIODevice, QNonContiguousByteDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QNonContiguousByteDevice = WAIT['QNonContiguousByteDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNonContiguousByteDeviceFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNonContiguousByteDeviceFactory: a plain Python
  object standing in front of one C++ QNonContiguousByteDeviceFactory.

  C++ hands a QNonContiguousByteDeviceFactory around as a copy, so every C++
  QNonContiguousByteDeviceFactory behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QNonContiguousByteDeviceFactory that has a ritual
  and that Python can call so far, 2 names in all: 'create', 'wrap'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
    QNonContiguousByteDeviceFactory::createShared(QIODevice *device)': gives
    a type Python has no way to take yet.
  - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
    QNonContiguousByteDeviceFactory::createShared(const QByteArray
    &byteArray)': gives a type Python has no way to take yet.
  - Qt's 'QNonContiguousByteDevice
    *QNonContiguousByteDeviceFactory::create(std::shared_ptr<QRingBuffer>
    ringBuffer)': takes a type Python has no way to hand over yet.
  - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
    QNonContiguousByteDeviceFactory::createShared(std::
    shared_ptr<QRingBuffer> ringBuffer)': takes a type Python has no way to
    hand over yet.
  - Qt's
    'QNonContiguousByteDeviceFactory::~QNonContiguousByteDeviceFactory()':
    the destructor: Python removes its C++ QNonContiguousByteDeviceFactory by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNonContiguousByteDeviceFactory is created at the first use, not
    by 'QNonContiguousByteDeviceFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNonContiguousByteDeviceFactory back gives a copy the
    ritual made for Python, in a new cute QNonContiguousByteDeviceFactory.
  - Each name of Qt's QNonContiguousByteDeviceFactory that has no cute
    function yet, 'createShared', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  def create(
      device: Optional[QIODevice],
  ) -> Optional[QNonContiguousByteDevice]:
    """
    Calls Qt's 'QNonContiguousByteDevice
    *QNonContiguousByteDeviceFactory::create(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicefactory.html#create

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNonContiguousByteDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNonContiguousByteDevice
    #      *QNonContiguousByteDeviceFactory::create(QIODevice *device)
    address = Rituals.call(
        'ritual_ZN31QNonContiguousByteDeviceFactory6createEP9QIODevice',
        CuteMixin._addressOf(device),
    )
    from . import QNonContiguousByteDevice
    return QNonContiguousByteDevice._cuteAt(address)

  @staticmethod
  @overload(QByteArray)
  def create(byteArray: QByteArray) -> Optional[QNonContiguousByteDevice]:
    """
    Calls Qt's 'QNonContiguousByteDevice
    *QNonContiguousByteDeviceFactory::create(const QByteArray &byteArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicefactory.html#create

    Parameters
    ----------

    byteArray : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNonContiguousByteDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNonContiguousByteDevice
    #      *QNonContiguousByteDeviceFactory::create(const QByteArray
    #      &byteArray)
    address = Rituals.call(
        'ritual_ZN31QNonContiguousByteDeviceFactory6createERK10QByteArray',
        CuteMixin._valueOf(byteArray),
    )
    from . import QNonContiguousByteDevice
    return QNonContiguousByteDevice._cuteAt(address)

  @staticmethod
  @overload(QNonContiguousByteDevice)
  @overload(NoneType)
  def wrap(
      byteDevice: Optional[QNonContiguousByteDevice],
  ) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice
    *QNonContiguousByteDeviceFactory::wrap(QNonContiguousByteDevice
    *byteDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicefactory.html#wrap

    Parameters
    ----------

    byteDevice : Optional[QNonContiguousByteDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice
    #      *QNonContiguousByteDeviceFactory::wrap(QNonContiguousByteDevice
    #      *byteDevice)
    address = Rituals.call(
        'ritual_ZN31QNonContiguousByteDeviceFactory4wrapEP24QNonContiguousB'
        'yteDevice',
        CuteMixin._addressOf(byteDevice),
    )
    from . import QIODevice
    return QIODevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNonContiguousByteDeviceFactory'

  #  Qt's '~QNonContiguousByteDeviceFactory()'. Naming it makes this a value
  #  class: Python owns every C++ QNonContiguousByteDeviceFactory behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QNonContiguousByteDeviceFactoryD1Ev'

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

  @staticmethod
  def createShared(*__, **_) -> Never:
    """
    - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
      QNonContiguousByteDeviceFactory::createShared(QIODevice *device)':
      gives a type Python has no way to take yet.
    - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
      QNonContiguousByteDeviceFactory::createShared(const QByteArray
      &byteArray)': gives a type Python has no way to take yet.
    - Qt's 'std::shared_ptr<QNonContiguousByteDevice>
      QNonContiguousByteDeviceFactory::createShared(std::
      shared_ptr<QRingBuffer> ringBuffer)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDeviceFactory.createShared' has no cute "
        "function yet. Qt's 'std::shared_ptr<QNonContiguousByteDevice> "
        "QNonContiguousByteDeviceFactory::createShared(QIODevice *device)': "
        "gives a type Python has no way to take yet. Qt's "
        "'std::shared_ptr<QNonContiguousByteDevice> "
        "QNonContiguousByteDeviceFactory::createShared(const QByteArray "
        "&byteArray)': gives a type Python has no way to take yet. Qt's "
        "'std::shared_ptr<QNonContiguousByteDevice> "
        "QNonContiguousByteDeviceFactory::createShared(std::shared_ptr<QRing"
        "Buffer> ringBuffer)': takes a type Python has no way to hand over "
        "yet.")
