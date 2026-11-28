"""
QRemoteObjectPackets::DataStreamPacket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectPackets::DataStreamPacket to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QDataStream

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class DataStreamPacket(QDataStream):
  """
  The cute side of Qt's QRemoteObjectPackets::DataStreamPacket: a plain
  Python object standing in front of one C++
  QRemoteObjectPackets::DataStreamPacket.

  It is built on the cute 'QDataStream', as Qt's
  QRemoteObjectPackets::DataStreamPacket is built on Qt's QDataStream, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPackets::DataStreamPacket that has a
  ritual and that Python can call so far, 4 names in all: 'setId',
  'finishPacket', 'payload', 'reset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRemoteObjectPackets::DataStreamPacket is created at the first
    use, not by 'QRemoteObjectPackets::DataStreamPacket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectPackets::DataStreamPacket.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPackets::DataStreamPacket'

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

  @overload(int)
  def setId(self, id: int) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::DataStreamPacket::setId(quint16
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-datastreampacket.html#setId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::DataStreamPacket::setId(quint16 id)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16DataStreamPacket5setIdEt', id,
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

  @overload()
  @overload(int)
  def __init__(self, id: int = 6) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectPackets::DataStreamPacket::DataStreamPacket(quint16 id)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-datastreampacket.html

    Parameters
    ----------

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 6.
    """
    #  QRemoteObjectPackets::DataStreamPacket::DataStreamPacket(quint16 id)
    self._noteCreation(DataStreamPacket, lambda: Rituals.call(
        'ritual_ZN20QRemoteObjectPackets16DataStreamPacketC1Et', id,
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

  def finishPacket(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::DataStreamPacket::finishPacket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-datastreampacket.html
    """
    #  void QRemoteObjectPackets::DataStreamPacket::finishPacket()
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16DataStreamPacket12finishPacketEv',
    )

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray
    &QRemoteObjectPackets::DataStreamPacket::payload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-datastreampacket.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QRemoteObjectPackets::DataStreamPacket::payload()
    address = self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16DataStreamPacket7payloadEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::DataStreamPacket::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-datastreampacket.html#reset
    """
    #  void QRemoteObjectPackets::DataStreamPacket::reset()
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16DataStreamPacket5resetEv',
    )
