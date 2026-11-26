//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QQsbCollection that Python can take functions over in. Every QQsbCollection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QQsbCollection::Entry * (*CuteQQsbCollectionCall0)(const void *, const QByteArray *, const QQsbCollection::EntryDesc *, int *);
class CuteQQsbCollection : public QQsbCollection {
public:
  using QQsbCollection::QQsbCollection;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Entry QQsbCollection::addEntry(const QByteArray &key, const EntryDesc
  //      &entryDesc)
  QQsbCollection::Entry addEntry(
      const QByteArray &key,
      const QQsbCollection::EntryDesc &entryDesc) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQsbCollectionCall0 call = reinterpret_cast<CuteQQsbCollectionCall0>(taken[0]);
      const QQsbCollection::Entry * given = call(this, &key, &entryDesc, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QQsbCollection::~QQsbCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollectionD1Ev(QQsbCollection *self) {
  delete self;
}

//  EntryMap QQsbCollection::availableEntries() const
extern "C" Q_DECL_EXPORT
QQsbCollection::EntryMap *ritual_ZNK14QQsbCollection16availableEntriesEv(
    const QQsbCollection *self) {
  return new QQsbCollection::EntryMap(self->availableEntries());
}

//  Entry QQsbCollection::addEntry(const QByteArray &key, const EntryDesc
//      &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE(
    QQsbCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(self->addEntry(*key, *entryDesc));
}

//  bool QQsbCollection::extractEntry(Entry entry, EntryDesc &entryDesc)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQsbCollection12extractEntryENS_5EntryERNS_9EntryDescE(
    QQsbCollection *self,
    const QQsbCollection::Entry *entry,
    QQsbCollection::EntryDesc *entryDesc) {
  return self->extractEntry(*entry, *entryDesc);
}

//  bool QQsbCollection::readEndHeader(QDataStream &ds, qint64 *startPos,
//      quint8 *version)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQsbCollection13readEndHeaderER11QDataStreamPxPh(
    QQsbCollection *self,
    QDataStream *ds,
    qint64 *startPos,
    quint8 *version) {
  return self->readEndHeader(*ds, startPos, version);
}

//  void QQsbCollection::writeEndHeader(QDataStream &ds, qint64 startPos,
//      quint8 version, quint64 magic)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollection14writeEndHeaderER11QDataStreamxhy(
    QQsbCollection *self,
    QDataStream *ds,
    qint64 startPos,
    quint8 version,
    quint64 magic) {
  self->writeEndHeader(*ds, startPos, version, magic);
}

//  bool QQsbCollection::readEndHeader(QIODevice *device, EntryMap *entries,
//      quint8 *version)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQsbCollection13readEndHeaderEP9QIODeviceP4QSetINS_5EntryEEPh(
    QQsbCollection *self,
    QIODevice *device,
    QQsbCollection::EntryMap *entries,
    quint8 *version) {
  return self->readEndHeader(device, entries, version);
}

//  void QQsbCollection::writeEndHeader(QIODevice *device, const EntryMap
//      &entries)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollection14writeEndHeaderEP9QIODeviceRK4QSetINS_5EntryEE(
    QQsbCollection *self,
    QIODevice *device,
    const QQsbCollection::EntryMap *entries) {
  self->writeEndHeader(device, *entries);
}

//  a Python function taken by a CuteQQsbCollection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQsbCollection(
    QQsbCollection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQsbCollection *>(self)->take(key, call);
}

//  a QQsbCollection::EntryMap a ritual of QQsbCollection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQsbCollection__QQsbCollection_EntryMap(
    QQsbCollection::EntryMap *self) {
  delete self;
}
