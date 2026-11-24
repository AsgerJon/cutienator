//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QQsbCollection::Entry::Entry()
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN14QQsbCollection5EntryC1Ev() {
  return new QQsbCollection::Entry();
}

//  QQsbCollection::Entry::Entry(const QByteArray &key)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN14QQsbCollection5EntryC1ERK10QByteArray(
    const QByteArray *key) {
  return new QQsbCollection::Entry(*key);
}

//  QQsbCollection::Entry::Entry(const QByteArray &key, qint64 value)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN14QQsbCollection5EntryC1ERK10QByteArrayx(
    const QByteArray *key,
    qint64 value) {
  return new QQsbCollection::Entry(*key, value);
}

//  bool QQsbCollection::Entry::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQsbCollection5Entry7isValidEv(
    const QQsbCollection::Entry *self) {
  return self->isValid();
}

//  QQsbCollection::Entry::~Entry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollection5EntryD1Ev(QQsbCollection::Entry *self) {
  delete self;
}
