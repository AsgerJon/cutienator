//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhstsstore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(settings)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhstsstore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhstsstore_p.h"
#include "qhstspolicy.h"
#include "qstandardpaths.h"
#include "qdatastream.h"
#include "qbytearray.h"
#include "qdatetime.h"
#include "qvariant.h"
#include "qstring.h"
#include "qdir.h"
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhstsstore.cpp, line 72, as _ZN10QHstsStore13addToObservedERK11QHstsPolicy
inline void QHstsStore::addToObserved(const QHstsPolicy &policy)
{
    observedPolicies.push_back(policy);
}

//  from src/network/access/qhstsstore.cpp, line 97, as _ZNK10QHstsStore10isWritableEv
inline bool QHstsStore::isWritable() const
{
    return store.isWritable();
}

//  from src/network/access/qhstsstore.cpp, line 144, as _ZN10QHstsStore15serializePolicyERK7QStringRK11QHstsPolicy
inline bool QHstsStore::serializePolicy(const QString &key, const QHstsPolicy &policy)
{
    Q_ASSERT(store.isWritable());

    QByteArray serializedData;
    QDataStream streamer(&serializedData, QIODevice::WriteOnly);
    streamer << policy.expiry().toMSecsSinceEpoch();
    streamer << policy.includesSubDomains();

    if (streamer.status() != QDataStream::Ok)
        return false;

    store.setValue(key, serializedData);
    return true;
}

//  from src/network/access/qhstsstore.cpp, line 160, as _ZN10QHstsStore11evictPolicyERK7QString
inline void QHstsStore::evictPolicy(const QString &key)
{
    Q_ASSERT(store.isWritable());
    if (store.contains(key))
        store.remove(key);
}

//  from src/network/access/qhstsstore.cpp, line 115, as _ZN10QHstsStore13endHstsGroupsEv
inline void QHstsStore::endHstsGroups()
{
    store.endGroup();
    store.endGroup();
}
//  -----------------------------------------------------------------------

//  void QHstsStore::addToObserved(const QHstsPolicy &policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore13addToObservedERK11QHstsPolicy(
    QHstsStore *self,
    const QHstsPolicy *policy) {
  self->addToObserved(*policy);
}

//  bool QHstsStore::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QHstsStore10isWritableEv(const QHstsStore *self) {
  return self->isWritable();
}

//  bool QHstsStore::serializePolicy(const QString &key, const QHstsPolicy
//      &policy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QHstsStore15serializePolicyERK7QStringRK11QHstsPolicy(
    QHstsStore *self,
    const QString *key,
    const QHstsPolicy *policy) {
  return self->serializePolicy(*key, *policy);
}

//  void QHstsStore::evictPolicy(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore11evictPolicyERK7QString(
    QHstsStore *self,
    const QString *key) {
  self->evictPolicy(*key);
}

//  void QHstsStore::endHstsGroups()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore13endHstsGroupsEv(QHstsStore *self) {
  self->endHstsGroups();
}

#endif  // QT_CONFIG(settings)
