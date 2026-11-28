"""
QRemoteObjectPackets::QDataStreamCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectPackets::QDataStreamCodec to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QRemoteObjectPackets

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVariant
  from . import QRemoteObjectRootSource, QRemoteObjectSourceBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectRootSource = WAIT['QRemoteObjectRootSource']
  QRemoteObjectSourceBase = WAIT['QRemoteObjectSourceBase']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDataStreamCodec(QRemoteObjectPackets.CodecBase):
  """
  The cute side of Qt's QRemoteObjectPackets::QDataStreamCodec: a plain
  Python object standing in front of one C++
  QRemoteObjectPackets::QDataStreamCodec.

  It is built on the cute 'QRemoteObjectPackets::CodecBase', as Qt's
  QRemoteObjectPackets::QDataStreamCodec is built on Qt's
  QRemoteObjectPackets::CodecBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPackets::QDataStreamCodec that has a
  ritual and that Python can call so far, 14 names in all:
  'serializeInitPacket', 'serializeInitDynamicPacket',
  'serializePropertyChangePacket', 'serializeProperty',
  'serializePingPacket', 'serializePongPacket', 'serializeInvokePacket',
  'serializeInvokeReplyPacket', 'serializeHandshakePacket',
  'serializeRemoveObjectPacket', 'serializeAddObjectPacket', 'getPayload',
  'reset', 'serializeProperties'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeObjectListPacket(const
    ObjectInfoList &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializeObjectListPacket(
    QDataStream &in, ObjectInfoList &a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializePropertyChangePacket(
    QDataStream &in, int &index, QVariant &value)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializeInvokePacket(
    QDataStream &in, int &call, int &index, QVariantList &args, int
    &serialId, int &propertyIndex)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializeAddObjectPacket(
    QDataStream &a0, bool &isDynamic)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializeInitPacket(QDataStream
    &a0, QVariantList &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::deserializeInvokeReplyPacket(
    QDataStream &in, int &ackedSerialId, QVariant &value)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray
  const&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken.

  What to expect
  --------------

  - The C++ QRemoteObjectPackets::QDataStreamCodec is created at the first
    use, not by 'QRemoteObjectPackets::QDataStreamCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectPackets::QDataStreamCodec.
  - Each name of Qt's QRemoteObjectPackets::QDataStreamCodec that has no cute
    function yet, 'serializeDefinition', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPackets::QDataStreamCodec'

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

  @overload(QRemoteObjectRootSource)
  @overload(NoneType)
  def serializeInitPacket(
      self,
      a0: Optional[QRemoteObjectRootSource],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeInitPacket(const
    QRemoteObjectRootSource *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectRootSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializeInitPacket(const
    #      QRemoteObjectRootSource *a0)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializeInitPa'
        'cketEPK23QRemoteObjectRootSource')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serialize'
          'InitPacketEPK23QRemoteObjectRootSource')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QRemoteObjectRootSource)
  @overload(NoneType)
  def serializeInitDynamicPacket(
      self,
      a0: Optional[QRemoteObjectRootSource],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeInitDynamicPacket(const
    QRemoteObjectRootSource *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectRootSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::
    #      serializeInitDynamicPacket(const QRemoteObjectRootSource *a0)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInitDy'
        'namicPacketEPK23QRemoteObjectRootSource',
        self._addressOf(a0),
    )

  @overload(QRemoteObjectSourceBase, int)
  @overload(NoneType, int)
  def serializePropertyChangePacket(
      self,
      source: Optional[QRemoteObjectSourceBase],
      signalIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializePropertyChangePacket(
    QRemoteObjectSourceBase *source, int signalIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signalIndex : int
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::
    #      serializePropertyChangePacket(QRemoteObjectSourceBase *source, int
    #      signalIndex)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec29serializeProper'
        'tyChangePacketEP23QRemoteObjectSourceBasei')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec29serialize'
          'PropertyChangePacketEP23QRemoteObjectSourceBasei')
    self.uglySide.call(ritual, self._addressOf(source), signalIndex)

  @overload(QRemoteObjectSourceBase, int)
  @overload(NoneType, int)
  def serializeProperty(
      self,
      source: Optional[QRemoteObjectSourceBase],
      internalIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeProperty(const
    QRemoteObjectSourceBase *source, int internalIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    internalIndex : int
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializeProperty(const
    #      QRemoteObjectSourceBase *source, int internalIndex)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec17serializeProper'
        'tyEPK23QRemoteObjectSourceBasei',
        self._addressOf(source), internalIndex,
    )

  @overload(str)
  def serializePingPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializePingPacket(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializePingPacket(const
    #      QString &name)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePingPa'
        'cketERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serialize'
          'PingPacketERK7QString')
    self.uglySide.call(ritual, name)

  @overload(str)
  def serializePongPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializePongPacket(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializePongPacket(const
    #      QString &name)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePongPa'
        'cketERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serialize'
          'PongPacketERK7QString')
    self.uglySide.call(ritual, name)

  @overload(str, int, int, QList[QVariant])
  @overload(str, int, int, QList[QVariant], int)
  @overload(str, int, int, QList[QVariant], int, int)
  def serializeInvokePacket(
      self,
      name: str,
      call: int,
      index: int,
      args: QList[QVariant],
      serialId: int = -1,
      propertyIndex: int = -1,
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeInvokePacket(const
    QString &name, int call, int index, const QVariantList &args, int
    serialId, int propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    call : int
      Passed on as it is.

    index : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serialId : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    propertyIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializeInvokePacket(
    #      const QString &name, int call, int index, const QVariantList
    #      &args, int serialId, int propertyIndex)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec21serializeInvoke'
        'PacketERK7QStringiiRK5QListI8QVariantEii',
        name, call, index, self._valueOf(args), serialId, propertyIndex,
    )

  @overload(str, int, QVariant)
  def serializeInvokeReplyPacket(
      self,
      name: str,
      ackedSerialId: int,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeInvokeReplyPacket(const
    QString &name, int ackedSerialId, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    ackedSerialId : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::
    #      serializeInvokeReplyPacket(const QString &name, int ackedSerialId,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInvoke'
        'ReplyPacketERK7QStringiRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec26serialize'
          'InvokeReplyPacketERK7QStringiRK8QVariant')
    self.uglySide.call(ritual, name, ackedSerialId, self._valueOf(value))

  def serializeHandshakePacket(self) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeHandshakePacket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html
    """
    #  void
    #      QRemoteObjectPackets::QDataStreamCodec::serializeHandshakePacket()
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeHandsh'
        'akePacketEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec24serialize'
          'HandshakePacketEv')
    self.uglySide.call(ritual)

  @overload(str)
  def serializeRemoveObjectPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeRemoveObjectPacket(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::
    #      serializeRemoveObjectPacket(const QString &name)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec27serializeRemove'
        'ObjectPacketERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec27serialize'
          'RemoveObjectPacketERK7QString')
    self.uglySide.call(ritual, name)

  @overload(str, bool)
  def serializeAddObjectPacket(self, name: str, isDynamic: bool) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeAddObjectPacket(const
    QString &name, bool isDynamic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    isDynamic : bool
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializeAddObjectPacket(
    #      const QString &name, bool isDynamic)
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeAddObj'
        'ectPacketERK7QStringb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec24serialize'
          'AddObjectPacketERK7QStringb')
    self.uglySide.call(ritual, name, isDynamic)

  def getPayload(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray
    &QRemoteObjectPackets::QDataStreamCodec::getPayload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QRemoteObjectPackets::QDataStreamCodec::getPayload()
    ritual = (
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloadEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloa'
          'dEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::QDataStreamCodec::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html#reset
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::reset()
    ritual = 'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv')
    self.uglySide.call(ritual)

  @overload(QRemoteObjectSourceBase)
  @overload(NoneType)
  def serializeProperties(
      self,
      source: Optional[QRemoteObjectSourceBase],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeProperties(const
    QRemoteObjectSourceBase *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qdatastreamcodec.html

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::QDataStreamCodec::serializeProperties(const
    #      QRemoteObjectSourceBase *source)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializeProper'
        'tiesEPK23QRemoteObjectSourceBase',
        self._addressOf(source),
    )

  @staticmethod
  def serializeDefinition(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::QDataStreamCodec::serializeDefinition(QDataStream
    &a0, const QRemoteObjectSourceBase *a1)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'isSequentialGadgetType'.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.QDataStreamCodec.serializeDefinition' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectPackets::QDataStreamCodec::serializeDefinition(QDataSt"
        "ream &a0, const QRemoteObjectSourceBase *a1)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'isSequentialGadgetType'.")
