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

//  QRemoteObjectPackets::CodecBase::~CodecBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets9CodecBaseD1Ev(
    QRemoteObjectPackets::CodecBase *self) {
  delete self;
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
