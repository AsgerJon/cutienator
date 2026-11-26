//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QQsbInMemoryCollection::QQsbInMemoryCollection()
extern "C" Q_DECL_EXPORT
QQsbInMemoryCollection *ritual_ZN22QQsbInMemoryCollectionC1Ev() {
  return new QQsbInMemoryCollection();
}

//  EntryMap QQsbInMemoryCollection::availableEntries() const
extern "C" Q_DECL_EXPORT
QQsbCollection::EntryMap *ritual_ZNK22QQsbInMemoryCollection16availableEntriesEv(
    const QQsbInMemoryCollection *self) {
  return new QQsbCollection::EntryMap(self->availableEntries());
}

//  Entry QQsbInMemoryCollection::addEntry(const QByteArray &key, const
//      EntryDesc &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN22QQsbInMemoryCollection8addEntryERK10QByteArrayRKN14QQsbCollection9EntryDescE(
    QQsbInMemoryCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(self->addEntry(*key, *entryDesc));
}

//  bool QQsbInMemoryCollection::extractEntry(Entry entry, EntryDesc
//      &entryDesc)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQsbInMemoryCollection12extractEntryEN14QQsbCollection5EntryERNS0_9EntryDescE(
    QQsbInMemoryCollection *self,
    const QQsbCollection::Entry *entry,
    QQsbCollection::EntryDesc *entryDesc) {
  return self->extractEntry(*entry, *entryDesc);
}

//  void QQsbInMemoryCollection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQsbInMemoryCollection5clearEv(
    QQsbInMemoryCollection *self) {
  self->clear();
}

//  bool QQsbInMemoryCollection::load(const QString &filename)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQsbInMemoryCollection4loadERK7QString(
    QQsbInMemoryCollection *self,
    const QString *filename) {
  return self->load(*filename);
}

//  bool QQsbInMemoryCollection::save(const QString &filename)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQsbInMemoryCollection4saveERK7QString(
    QQsbInMemoryCollection *self,
    const QString *filename) {
  return self->save(*filename);
}

//  Entry QQsbInMemoryCollection::addEntry(const QByteArray &key, const
//      EntryDesc &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_own_ZN22QQsbInMemoryCollection8addEntryERK10QByteArrayRKN14QQsbCollection9EntryDescE(
    QQsbInMemoryCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(
      self->QQsbInMemoryCollection::addEntry(
          *key,
          *entryDesc));
}

//  a QQsbCollection::EntryMap a ritual of QQsbInMemoryCollection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQsbInMemoryCollection__QQsbCollection_EntryMap(
    QQsbCollection::EntryMap *self) {
  delete self;
}
