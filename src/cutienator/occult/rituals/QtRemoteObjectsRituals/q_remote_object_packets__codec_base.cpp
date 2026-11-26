//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearrayview.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <cstring>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 1110, as _ZN20QRemoteObjectPackets9CodecBase4sendERK4QSetIP16QtROIoDeviceBaseE
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void CodecBase::send(const QSet<QtROIoDeviceBase *> &connections)
{
    const auto bytearray = getPayload();
    for (auto conn : connections)
        conn->write(bytearray);
    reset();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 1126, as _ZN20QRemoteObjectPackets9CodecBase4sendEP16QtROIoDeviceBase
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void CodecBase::send(QtROIoDeviceBase *connection)
{
    const auto bytearray = getPayload();
    connection->write(bytearray);
    reset();
}
}  // namespace QRemoteObjectPackets
//  -----------------------------------------------------------------------

//  Only a class built on QRemoteObjectPackets::CodecBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectPackets_CodecBase : QRemoteObjectPackets::CodecBase {
  using QRemoteObjectPackets::CodecBase::reset;
};

//  A QRemoteObjectPackets::CodecBase that Python can take functions over in. Every QRemoteObjectPackets::CodecBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall0)(const void *, const QRemoteObjectRootSource *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall1)(const void *, const QRemoteObjectRootSource *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall2)(const void *, QRemoteObjectSourceBase *, int, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall3)(const void *, const QRemoteObjectSourceBase *, int, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall4)(const void *, const QString *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall5)(const void *, const QString *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall6)(const void *, const QString *, int, const QVariant *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall7)(const void *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall8)(const void *, const QString *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall9)(const void *, const QString *, bool, int *);
typedef const QByteArray * (*CuteQRemoteObjectPackets_CodecBaseCall10)(const void *, int *);
typedef void (*CuteQRemoteObjectPackets_CodecBaseCall11)(const void *, int *);
class CuteQRemoteObjectPackets_CodecBase : public QRemoteObjectPackets::CodecBase {
public:
  using QRemoteObjectPackets::CodecBase::CodecBase;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase19serializeInitPacketEPK23QRemoteObjectRootSource")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase26serializeInitDynamicPacketEPK23QRemoteObjectRootSource")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase29serializePropertyChangePacketEP23QRemoteObjectSourceBasei")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase17serializePropertyEPK23QRemoteObjectSourceBasei")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase19serializePingPacketERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase19serializePongPacketERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase26serializeInvokeReplyPacketERK7QStringiRK8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase24serializeHandshakePacketEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase27serializeRemoveObjectPacketERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase24serializeAddObjectPacketERK7QStringb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase10getPayloadEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectPackets9CodecBase5resetEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  void QRemoteObjectPackets::CodecBase::serializeInitPacket(const
  //      QRemoteObjectRootSource *a0)
  void serializeInitPacket(const QRemoteObjectRootSource *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall0 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QRemoteObjectPackets::CodecBase::serializeInitDynamicPacket(const
  //      QRemoteObjectRootSource *a0)
  void serializeInitDynamicPacket(
      const QRemoteObjectRootSource *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall1 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializePropertyChangePacket(Q
  //      RemoteObjectSourceBase *source, int signalIndex)
  void serializePropertyChangePacket(
      QRemoteObjectSourceBase *source,
      int signalIndex) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall2 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall2>(taken[2]);
      call(this, source, signalIndex, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializeProperty(const
  //      QRemoteObjectSourceBase *source, int internalIndex)
  void serializeProperty(
      const QRemoteObjectSourceBase *source,
      int internalIndex) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall3 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall3>(taken[3]);
      call(this, source, internalIndex, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializePingPacket(const
  //      QString &name)
  void serializePingPacket(const QString &name) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall4 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall4>(taken[4]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializePongPacket(const
  //      QString &name)
  void serializePongPacket(const QString &name) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall5 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall5>(taken[5]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QRemoteObjectPackets::CodecBase::serializeInvokeReplyPacket(const
  //      QString &name, int ackedSerialId, const QVariant &value)
  void serializeInvokeReplyPacket(
      const QString &name,
      int ackedSerialId,
      const QVariant &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall6 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall6>(taken[6]);
      call(this, &name, ackedSerialId, &value, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializeHandshakePacket()
  void serializeHandshakePacket() override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall7 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QRemoteObjectPackets::CodecBase::serializeRemoveObjectPacket(cons
  //      t QString &name)
  void serializeRemoveObjectPacket(const QString &name) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall8 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall8>(taken[8]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  void QRemoteObjectPackets::CodecBase::serializeAddObjectPacket(const
  //      QString &name, bool isDynamic)
  void serializeAddObjectPacket(
      const QString &name,
      bool isDynamic) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall9 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall9>(taken[9]);
      call(this, &name, isDynamic, &handled);
      if (handled) return;
    }
  }

  //  const QByteArray &QRemoteObjectPackets::CodecBase::getPayload()
  const QByteArray &getPayload() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall10 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall10>(taken[10]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QRemoteObjectPackets::CodecBase::reset()
  void reset() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRemoteObjectPackets_CodecBaseCall11 call = reinterpret_cast<CuteQRemoteObjectPackets_CodecBaseCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QRemoteObjectPackets::CodecBase::reset();
  }
};

//  CodecBase &QRemoteObjectPackets::CodecBase::operator=(const CodecBase
//      &a0)
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::CodecBase *ritual_ZN20QRemoteObjectPackets9CodecBaseaSERKS0_(
    QRemoteObjectPackets::CodecBase *self,
    const QRemoteObjectPackets::CodecBase *a0) {
  return &(self->operator=(*a0));
}

//  CodecBase &QRemoteObjectPackets::CodecBase::operator=(CodecBase &&a0)
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::CodecBase *ritual_ZN20QRemoteObjectPackets9CodecBaseaSEOS0_(
    QRemoteObjectPackets::CodecBase *self,
    QRemoteObjectPackets::CodecBase *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QRemoteObjectPackets::CodecBase::~CodecBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBaseD1Ev(
    QRemoteObjectPackets::CodecBase *self) {
  delete self;
}

//  void QRemoteObjectPackets::CodecBase::serializeObjectListPacket(const
//      ObjectInfoList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase25serializeObjectListPacketERK5QListINS_10ObjectInfoEE(
    QRemoteObjectPackets::CodecBase *self,
    const QRemoteObjectPackets::ObjectInfoList *a0) {
  self->serializeObjectListPacket(*a0);
}

//  void
//      QRemoteObjectPackets::CodecBase::deserializeObjectListPacket(QDataStr
//      eam &in, ObjectInfoList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase27deserializeObjectListPacketER11QDataStreamR5QListINS_10ObjectInfoEE(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *in,
    QRemoteObjectPackets::ObjectInfoList *a1) {
  self->deserializeObjectListPacket(*in, *a1);
}

//  void QRemoteObjectPackets::CodecBase::serializeInitPacket(const
//      QRemoteObjectRootSource *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase19serializeInitPacketEPK23QRemoteObjectRootSource(
    QRemoteObjectPackets::CodecBase *self,
    const QRemoteObjectRootSource *a0) {
  self->serializeInitPacket(a0);
}

//  void QRemoteObjectPackets::CodecBase::serializeInitDynamicPacket(const
//      QRemoteObjectRootSource *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase26serializeInitDynamicPacketEPK23QRemoteObjectRootSource(
    QRemoteObjectPackets::CodecBase *self,
    const QRemoteObjectRootSource *a0) {
  self->serializeInitDynamicPacket(a0);
}

//  void QRemoteObjectPackets::CodecBase::serializePropertyChangePacket(QRemo
//      teObjectSourceBase *source, int signalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase29serializePropertyChangePacketEP23QRemoteObjectSourceBasei(
    QRemoteObjectPackets::CodecBase *self,
    QRemoteObjectSourceBase *source,
    int signalIndex) {
  self->serializePropertyChangePacket(source, signalIndex);
}

//  void QRemoteObjectPackets::CodecBase::deserializePropertyChangePacket(QDa
//      taStream &in, int &index, QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase31deserializePropertyChangePacketER11QDataStreamRiR8QVariant(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *in,
    int *index,
    QVariant *value) {
  self->deserializePropertyChangePacket(*in, *index, *value);
}

//  void QRemoteObjectPackets::CodecBase::serializeProperty(const
//      QRemoteObjectSourceBase *source, int internalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase17serializePropertyEPK23QRemoteObjectSourceBasei(
    QRemoteObjectPackets::CodecBase *self,
    const QRemoteObjectSourceBase *source,
    int internalIndex) {
  self->serializeProperty(source, internalIndex);
}

//  void QRemoteObjectPackets::CodecBase::serializePingPacket(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase19serializePingPacketERK7QString(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name) {
  self->serializePingPacket(*name);
}

//  void QRemoteObjectPackets::CodecBase::serializePongPacket(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase19serializePongPacketERK7QString(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name) {
  self->serializePongPacket(*name);
}

//  void QRemoteObjectPackets::CodecBase::serializeInvokePacket(const QString
//      &name, int call, int index, const QVariantList &args, int serialId,
//      int propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase21serializeInvokePacketERK7QStringiiRK5QListI8QVariantEii(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name,
    int call,
    int index,
    const QList<QVariant> *args,
    int serialId,
    int propertyIndex) {
  self->serializeInvokePacket(
      *name,
      call,
      index,
      *args,
      serialId,
      propertyIndex);
}

//  void QRemoteObjectPackets::CodecBase::deserializeInvokePacket(QDataStream
//      &in, int &call, int &index, QVariantList &args, int &serialId, int
//      &propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase23deserializeInvokePacketER11QDataStreamRiS3_R5QListI8QVariantES3_S3_(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *in,
    int *call,
    int *index,
    QVariantList *args,
    int *serialId,
    int *propertyIndex) {
  self->deserializeInvokePacket(
      *in,
      *call,
      *index,
      *args,
      *serialId,
      *propertyIndex);
}

//  void QRemoteObjectPackets::CodecBase::serializeInvokeReplyPacket(const
//      QString &name, int ackedSerialId, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase26serializeInvokeReplyPacketERK7QStringiRK8QVariant(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name,
    int ackedSerialId,
    const QVariant *value) {
  self->serializeInvokeReplyPacket(*name, ackedSerialId, *value);
}

//  void QRemoteObjectPackets::CodecBase::serializeHandshakePacket()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase24serializeHandshakePacketEv(
    QRemoteObjectPackets::CodecBase *self) {
  self->serializeHandshakePacket();
}

//  void QRemoteObjectPackets::CodecBase::serializeRemoveObjectPacket(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase27serializeRemoveObjectPacketERK7QString(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name) {
  self->serializeRemoveObjectPacket(*name);
}

//  void QRemoteObjectPackets::CodecBase::serializeAddObjectPacket(const
//      QString &name, bool isDynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase24serializeAddObjectPacketERK7QStringb(
    QRemoteObjectPackets::CodecBase *self,
    const QString *name,
    bool isDynamic) {
  self->serializeAddObjectPacket(*name, isDynamic);
}

//  void
//      QRemoteObjectPackets::CodecBase::deserializeAddObjectPacket(QDataStre
//      am &a0, bool &isDynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase26deserializeAddObjectPacketER11QDataStreamRb(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *a0,
    bool *isDynamic) {
  self->deserializeAddObjectPacket(*a0, *isDynamic);
}

//  void QRemoteObjectPackets::CodecBase::deserializeInitPacket(QDataStream
//      &a0, QVariantList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase21deserializeInitPacketER11QDataStreamR5QListI8QVariantE(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *a0,
    QVariantList *a1) {
  self->deserializeInitPacket(*a0, *a1);
}

//  void
//      QRemoteObjectPackets::CodecBase::deserializeInvokeReplyPacket(QDataSt
//      ream &in, int &ackedSerialId, QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase28deserializeInvokeReplyPacketER11QDataStreamRiR8QVariant(
    QRemoteObjectPackets::CodecBase *self,
    QDataStream *in,
    int *ackedSerialId,
    QVariant *value) {
  self->deserializeInvokeReplyPacket(*in, *ackedSerialId, *value);
}

//  void QRemoteObjectPackets::CodecBase::send(const QSet<QtROIoDeviceBase *>
//      &connections)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase4sendERK4QSetIP16QtROIoDeviceBaseE(
    QRemoteObjectPackets::CodecBase *self,
    const QSet<QtROIoDeviceBase *> *connections) {
  self->send(*connections);
}

//  void QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase *connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase4sendEP16QtROIoDeviceBase(
    QRemoteObjectPackets::CodecBase *self,
    QtROIoDeviceBase *connection) {
  self->send(connection);
}

//  const QByteArray &QRemoteObjectPackets::CodecBase::getPayload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QRemoteObjectPackets9CodecBase10getPayloadEv(
    QRemoteObjectPackets::CodecBase *self) {
  return new QByteArray(self->getPayload());
}

//  void QRemoteObjectPackets::CodecBase::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBase5resetEv(
    QRemoteObjectPackets::CodecBase *self) {
  self->reset();
}

//  a Python function taken by a CuteQRemoteObjectPackets_CodecBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectPackets_CodecBase(
    QRemoteObjectPackets::CodecBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectPackets_CodecBase *>(self)->take(key, call);
}

//  void QRemoteObjectPackets::CodecBase::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets9CodecBase5resetEv(
    QRemoteObjectPackets::CodecBase *self) {
  static_cast<OwnQRemoteObjectPackets_CodecBase *>(self)->OwnQRemoteObjectPackets_CodecBase::reset();
}
