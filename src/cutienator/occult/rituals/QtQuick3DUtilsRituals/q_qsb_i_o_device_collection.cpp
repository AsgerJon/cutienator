//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QQsbIODeviceCollection that Python can take functions over in. Every QQsbIODeviceCollection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QQsbCollection::Entry * (*CuteQQsbIODeviceCollectionCall0)(const void *, const QByteArray *, const QQsbCollection::EntryDesc *, int *);
class CuteQQsbIODeviceCollection : public QQsbIODeviceCollection {
public:
  using QQsbIODeviceCollection::QQsbIODeviceCollection;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Entry QQsbIODeviceCollection::addEntry(const QByteArray &key, const
  //      EntryDesc &entryDesc)
  QQsbCollection::Entry addEntry(
      const QByteArray &key,
      const QQsbCollection::EntryDesc &entryDesc) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQsbIODeviceCollectionCall0 call = reinterpret_cast<CuteQQsbIODeviceCollectionCall0>(taken[0]);
      const QQsbCollection::Entry * given = call(this, &key, &entryDesc, &handled);
      if (handled && given) return *given;
    }
    return QQsbIODeviceCollection::addEntry(key, entryDesc);
  }
};

//  QQsbIODeviceCollection::QQsbIODeviceCollection(const QString &filePath)
extern "C" Q_DECL_EXPORT
QQsbIODeviceCollection *ritual_ZN22QQsbIODeviceCollectionC1ERK7QString(
    const QString *filePath) {
  return new CuteQQsbIODeviceCollection(*filePath);
}

//  QQsbIODeviceCollection::~QQsbIODeviceCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQsbIODeviceCollectionD1Ev(QQsbIODeviceCollection *self) {
  delete self;
}

//  bool QQsbIODeviceCollection::map(MapMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQsbIODeviceCollection3mapENS_7MapModeE(
    QQsbIODeviceCollection *self,
    QQsbIODeviceCollection::MapMode mode) {
  return self->map(mode);
}

//  void QQsbIODeviceCollection::unmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQsbIODeviceCollection5unmapEv(
    QQsbIODeviceCollection *self) {
  self->unmap();
}

//  Entry QQsbIODeviceCollection::addEntry(const QByteArray &key, const
//      EntryDesc &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN22QQsbIODeviceCollection8addEntryERK10QByteArrayRKN14QQsbCollection9EntryDescE(
    QQsbIODeviceCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(self->addEntry(*key, *entryDesc));
}

//  void QQsbIODeviceCollection::dumpInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQsbIODeviceCollection8dumpInfoEv(
    QQsbIODeviceCollection *self) {
  self->dumpInfo();
}

//  void QQsbIODeviceCollection::dumpInfo(const QString &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQsbIODeviceCollection8dumpInfoERK7QString(
    const QString *device) {
  QQsbIODeviceCollection::dumpInfo(*device);
}

//  a Python function taken by a CuteQQsbIODeviceCollection, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQsbIODeviceCollection(
    QQsbIODeviceCollection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQsbIODeviceCollection *>(self)->take(key, call);
}

//  Entry QQsbIODeviceCollection::addEntry(const QByteArray &key, const
//      EntryDesc &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_own_ZN22QQsbIODeviceCollection8addEntryERK10QByteArrayRKN14QQsbCollection9EntryDescE(
    QQsbIODeviceCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(
      self->QQsbIODeviceCollection::addEntry(
          *key,
          *entryDesc));
}
