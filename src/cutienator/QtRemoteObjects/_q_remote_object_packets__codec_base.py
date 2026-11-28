"""
QRemoteObjectPackets::CodecBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectPackets::CodecBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVariant
  from . import QRemoteObjectRootSource, QRemoteObjectSourceBase
  from . import QtROIoDeviceBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectRootSource = WAIT['QRemoteObjectRootSource']
  QRemoteObjectSourceBase = WAIT['QRemoteObjectSourceBase']
  QVariant = WAIT['QVariant']
  QtROIoDeviceBase = WAIT['QtROIoDeviceBase']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CodecBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRemoteObjectPackets::CodecBase: a plain Python
  object standing in front of one C++ QRemoteObjectPackets::CodecBase.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPackets::CodecBase that has a ritual
  and that Python can call so far, 14 names in all: 'serializeInitPacket',
  'serializeInitDynamicPacket', 'serializePropertyChangePacket',
  'serializeProperty', 'serializePingPacket', 'serializePongPacket',
  'serializeInvokePacket', 'serializeInvokeReplyPacket',
  'serializeHandshakePacket', 'serializeRemoveObjectPacket',
  'serializeAddObjectPacket', 'send', 'getPayload', 'reset'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CodecBase &QRemoteObjectPackets::CodecBase::operator=(const
    CodecBase &a0)': assignment: Python binds a name and has no operator for
    it.
  - Qt's 'CodecBase &QRemoteObjectPackets::CodecBase::operator=(CodecBase
    &&a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QRemoteObjectPackets::CodecBase::~CodecBase()': the destructor:
    Python never removes a C++ QRemoteObjectPackets::CodecBase.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeObjectListPacket(const
    ObjectInfoList &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeObjectListPacket(QDataStream
    &in, ObjectInfoList &a1)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializePropertyChangePacket(
    QDataStream &in, int &index, QVariant &value)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInvokePacket(QDataStream &in,
    int &call, int &index, QVariantList &args, int &serialId, int
    &propertyIndex)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeAddObjectPacket(QDataStream
    &a0, bool &isDynamic)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInitPacket(QDataStream &a0,
    QVariantList &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInvokeReplyPacket(QDataStream
    &in, int &ackedSerialId, QVariant &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QRemoteObjectPackets::CodecBase::send(const
    QSet<QtROIoDeviceBase *> &connections)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 3 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QRemoteObjectPackets::CodecBase is created at the first use, not
    by 'QRemoteObjectPackets::CodecBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectPackets::CodecBase.
  - Each name of Qt's QRemoteObjectPackets::CodecBase that has no cute
    function yet, '__init__', 'deserializeAddObjectPacket',
    'deserializeInitPacket', 'deserializeInvokePacket',
    'deserializeInvokeReplyPacket', 'deserializeObjectListPacket',
    'deserializePropertyChangePacket', 'serializeObjectListPacket', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPackets::CodecBase'

  #  A C++ QRemoteObjectPackets::CodecBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectPackets_CodecBase'

  #  The functions Qt calls itself that QRemoteObjectPackets::CodecBase is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'serializeObjectListPacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::serializeObjectListPacket(const'
          ' ObjectInfoList &)',
      ),
      'deserializeObjectListPacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializeObjectListPacket(QDa'
          'taStream &, ObjectInfoList &)',
      ),
      'deserializePropertyChangePacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializePropertyChangePacket'
          '(QDataStream &, int &, QVariant &)',
      ),
      'serializeInvokePacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::serializeInvokePacket(const '
          'QString &, int, int, const QVariantList &, int, int)',
      ),
      'deserializeInvokePacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializeInvokePacket(QDataSt'
          'ream &, int &, int &, QVariantList &, int &, int &)',
      ),
      'deserializeAddObjectPacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializeAddObjectPacket(QDat'
          'aStream &, bool &)',
      ),
      'deserializeInitPacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializeInitPacket(QDataStre'
          'am &, QVariantList &)',
      ),
      'deserializeInvokeReplyPacket': (
          'void '
          'QRemoteObjectPackets::CodecBase::deserializeInvokeReplyPacket(QD'
          'ataStream &, int &, QVariant &)',
      ),
  }

  #  The functions Qt calls itself that QRemoteObjectPackets::CodecBase is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'serializeInitPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase19serializeInitPacketEPK23QR'
           'emoteObjectRootSource',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectRootSource'),
           )),
      ),
      'serializeInitDynamicPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase26serializeInitDynamicPacket'
           'EPK23QRemoteObjectRootSource',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectRootSource'),
           )),
      ),
      'serializePropertyChangePacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase29serializePropertyChangePac'
           'ketEP23QRemoteObjectSourceBasei',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectSourceBase'),
               ('int', 'number', ''),
           )),
      ),
      'serializeProperty': (
          ('_ZN20QRemoteObjectPackets9CodecBase17serializePropertyEPK23QRem'
           'oteObjectSourceBasei',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectSourceBase'),
               ('int', 'number', ''),
           )),
      ),
      'serializePingPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase19serializePingPacketERK7QSt'
           'ring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'serializePongPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase19serializePongPacketERK7QSt'
           'ring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'serializeInvokeReplyPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase26serializeInvokeReplyPacket'
           'ERK7QStringiRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'serializeHandshakePacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase24serializeHandshakePacketEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'serializeRemoveObjectPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase27serializeRemoveObjectPacke'
           'tERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'serializeAddObjectPacket': (
          ('_ZN20QRemoteObjectPackets9CodecBase24serializeAddObjectPacketER'
           'K7QStringb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'getPayload': (
          ('_ZN20QRemoteObjectPackets9CodecBase10getPayloadEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'reset': (
          ('_ZN20QRemoteObjectPackets9CodecBase5resetEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QRemoteObjectPackets::CodecBase::CodecBase()': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'QRemoteObjectPackets::CodecBase::CodecBase(const CodecBase &a0)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    - Qt's 'QRemoteObjectPackets::CodecBase::CodecBase(CodecBase &&a0)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.__init__' has no cute function "
        "yet. Qt's 'QRemoteObjectPackets::CodecBase::CodecBase()': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open. Qt's "
        "'QRemoteObjectPackets::CodecBase::CodecBase(const CodecBase &a0)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open. Qt's "
        "'QRemoteObjectPackets::CodecBase::CodecBase(CodecBase &&a0)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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
    QRemoteObjectPackets::CodecBase::serializeInitPacket(const
    QRemoteObjectRootSource *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectRootSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::CodecBase::serializeInitPacket(const
    #      QRemoteObjectRootSource *a0)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase19serializeInitPacketEPK2'
        '3QRemoteObjectRootSource',
        self._addressOf(a0),
    )

  @overload(QRemoteObjectRootSource)
  @overload(NoneType)
  def serializeInitDynamicPacket(
      self,
      a0: Optional[QRemoteObjectRootSource],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeInitDynamicPacket(const
    QRemoteObjectRootSource *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectRootSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::CodecBase::serializeInitDynamicPacket(const
    #      QRemoteObjectRootSource *a0)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase26serializeInitDynamicPac'
        'ketEPK23QRemoteObjectRootSource',
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
    QRemoteObjectPackets::CodecBase::serializePropertyChangePacket(
    QRemoteObjectSourceBase *source, int signalIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signalIndex : int
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::CodecBase::serializePropertyChangePacket(
    #      QRemoteObjectSourceBase *source, int signalIndex)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase29serializePropertyChange'
        'PacketEP23QRemoteObjectSourceBasei',
        self._addressOf(source), signalIndex,
    )

  @overload(QRemoteObjectSourceBase, int)
  @overload(NoneType, int)
  def serializeProperty(
      self,
      source: Optional[QRemoteObjectSourceBase],
      internalIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::CodecBase::serializeProperty(const
    QRemoteObjectSourceBase *source, int internalIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    internalIndex : int
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::CodecBase::serializeProperty(const
    #      QRemoteObjectSourceBase *source, int internalIndex)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase17serializePropertyEPK23Q'
        'RemoteObjectSourceBasei',
        self._addressOf(source), internalIndex,
    )

  @overload(str)
  def serializePingPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializePingPacket(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectPackets::CodecBase::serializePingPacket(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase19serializePingPacketERK7'
        'QString',
        name,
    )

  @overload(str)
  def serializePongPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializePongPacket(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectPackets::CodecBase::serializePongPacket(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase19serializePongPacketERK7'
        'QString',
        name,
    )

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
    QRemoteObjectPackets::CodecBase::serializeInvokePacket(const QString
    &name, int call, int index, const QVariantList &args, int serialId, int
    propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

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
    #  void QRemoteObjectPackets::CodecBase::serializeInvokePacket(const
    #      QString &name, int call, int index, const QVariantList &args, int
    #      serialId, int propertyIndex)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase21serializeInvokePacketER'
        'K7QStringiiRK5QListI8QVariantEii',
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
    QRemoteObjectPackets::CodecBase::serializeInvokeReplyPacket(const QString
    &name, int ackedSerialId, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

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
    #  void QRemoteObjectPackets::CodecBase::serializeInvokeReplyPacket(const
    #      QString &name, int ackedSerialId, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase26serializeInvokeReplyPac'
        'ketERK7QStringiRK8QVariant',
        name, ackedSerialId, self._valueOf(value),
    )

  def serializeHandshakePacket(self) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeHandshakePacket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html
    """
    #  void QRemoteObjectPackets::CodecBase::serializeHandshakePacket()
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase24serializeHandshakePacke'
        'tEv',
    )

  @overload(str)
  def serializeRemoveObjectPacket(self, name: str) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeRemoveObjectPacket(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QRemoteObjectPackets::CodecBase::serializeRemoveObjectPacket(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase27serializeRemoveObjectPa'
        'cketERK7QString',
        name,
    )

  @overload(str, bool)
  def serializeAddObjectPacket(self, name: str, isDynamic: bool) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeAddObjectPacket(const QString
    &name, bool isDynamic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    isDynamic : bool
      Passed on as it is.
    """
    #  void QRemoteObjectPackets::CodecBase::serializeAddObjectPacket(const
    #      QString &name, bool isDynamic)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase24serializeAddObjectPacke'
        'tERK7QStringb',
        name, isDynamic,
    )

  @overload(QtROIoDeviceBase)
  @overload(NoneType)
  def send(self, connection: Optional[QtROIoDeviceBase]) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase
    *connection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html#send

    Parameters
    ----------

    connection : Optional[QtROIoDeviceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase
    #      *connection)
    self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase4sendEP16QtROIoDeviceBase',
        self._addressOf(connection),
    )

  def getPayload(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray
    &QRemoteObjectPackets::CodecBase::getPayload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html#getPayload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QRemoteObjectPackets::CodecBase::getPayload()
    address = self.uglySide.call(
        'ritual_ZN20QRemoteObjectPackets9CodecBase10getPayloadEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPackets::CodecBase::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-codecbase.html#reset
    """
    #  void QRemoteObjectPackets::CodecBase::reset()
    ritual = 'ritual_ZN20QRemoteObjectPackets9CodecBase5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QRemoteObjectPackets9CodecBase5resetEv'
    self.uglySide.call(ritual)

  @staticmethod
  def deserializeAddObjectPacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeAddObjectPacket(QDataStream
    &a0, bool &isDynamic)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializeAddObjectPacket' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializeAddObjectPacket(QDataSt"
        "ream &a0, bool &isDynamic)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def deserializeInitPacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInitPacket(QDataStream &a0,
    QVariantList &a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializeInitPacket' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializeInitPacket(QDataStream "
        "&a0, QVariantList &a1)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def deserializeInvokePacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInvokePacket(QDataStream &in,
    int &call, int &index, QVariantList &args, int &serialId, int
    &propertyIndex)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializeInvokePacket' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializeInvokePacket(QDataStrea"
        "m &in, int &call, int &index, QVariantList &args, int &serialId, "
        "int &propertyIndex)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def deserializeInvokeReplyPacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeInvokeReplyPacket(QDataStream
    &in, int &ackedSerialId, QVariant &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializeInvokeReplyPacket' has "
        "no cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializeInvokeReplyPacket(QData"
        "Stream &in, int &ackedSerialId, QVariant &value)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def deserializeObjectListPacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializeObjectListPacket(QDataStream
    &in, ObjectInfoList &a1)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializeObjectListPacket' has "
        "no cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializeObjectListPacket(QDataS"
        "tream &in, ObjectInfoList &a1)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def deserializePropertyChangePacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::deserializePropertyChangePacket(
    QDataStream &in, int &index, QVariant &value)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.deserializePropertyChangePacket' "
        "has no cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::deserializePropertyChangePacket(QD"
        "ataStream &in, int &index, QVariant &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def serializeObjectListPacket(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectPackets::CodecBase::serializeObjectListPacket(const
    ObjectInfoList &a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectPackets.CodecBase.serializeObjectListPacket' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectPackets::CodecBase::serializeObjectListPacket(const "
        "ObjectInfoList &a0)': takes a type Python has no way to hand over "
        "yet.")
