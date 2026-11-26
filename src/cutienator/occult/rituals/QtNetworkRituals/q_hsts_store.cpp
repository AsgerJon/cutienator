//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhstsstore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(settings)
#if QT_CONFIG(settings)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhstsstore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhstsstore_p.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhstsstore.cpp, line 22, as local:qhstsstore.cpp:host_name_to_settings_key
static QString host_name_to_settings_key(const QString &hostName)
{
    const QByteArray hostNameAsHex(hostName.toUtf8().toHex());
    return QString::fromLatin1(hostNameAsHex);
}

//  from src/network/access/qhstsstore.cpp, line 28, as local:qhstsstore.cpp:settings_key_to_host_name
static QString settings_key_to_host_name(const QString &key)
{
    const QByteArray hostNameAsUtf8(QByteArray::fromHex(key.toLatin1()));
    return QString::fromUtf8(hostNameAsUtf8);
}

//  from src/network/access/qhstsstore.cpp, line 34, as _ZN10QHstsStoreC1ERK7QString
inline QHstsStore::QHstsStore(const QString &dirName)
    : store(absoluteFilePath(dirName), QSettings::IniFormat)
{
    // Disable fallbacks, we do not want to use anything but our own ini file.
    store.setFallbacksEnabled(false);
}

//  from src/network/access/qhstsstore.cpp, line 41, as _ZN10QHstsStoreD1Ev
inline QHstsStore::~QHstsStore()
{
    synchronize();
}

//  from src/network/access/qhstsstore.cpp, line 46, as _ZN10QHstsStore12readPoliciesEv
inline QList<QHstsPolicy> QHstsStore::readPolicies()
{
    // This function only attempts to read policies, making no decision about
    // expired policies. It's up to a user (QHstsCache) to mark these policies
    // for deletion and sync the store later. But we immediately remove keys/values
    // (if the store isWritable) for the policies that we fail to read.
    QList<QHstsPolicy> policies;

    beginHstsGroups();

    const QStringList keys = store.childKeys();
    for (const auto &key : keys) {
        QHstsPolicy restoredPolicy;
        if (deserializePolicy(key, restoredPolicy)) {
            restoredPolicy.setHost(settings_key_to_host_name(key));
            policies.push_back(std::move(restoredPolicy));
        } else if (isWritable()) {
            evictPolicy(key);
        }
    }

    endHstsGroups();

    return policies;
}

//  from src/network/access/qhstsstore.cpp, line 72, as _ZN10QHstsStore13addToObservedERK11QHstsPolicy
inline void QHstsStore::addToObserved(const QHstsPolicy &policy)
{
    observedPolicies.push_back(policy);
}

//  from src/network/access/qhstsstore.cpp, line 77, as _ZN10QHstsStore11synchronizeEv
inline void QHstsStore::synchronize()
{
    if (!isWritable())
        return;

    if (observedPolicies.size()) {
        beginHstsGroups();
        for (const QHstsPolicy &policy : std::as_const(observedPolicies)) {
            const QString key(host_name_to_settings_key(policy.host()));
            // If we fail to write a new, updated policy, we also remove the old one.
            if (policy.isExpired() || !serializePolicy(key, policy))
                evictPolicy(key);
        }
        observedPolicies.clear();
        endHstsGroups();
    }

    store.sync();
}

//  from src/network/access/qhstsstore.cpp, line 97, as _ZNK10QHstsStore10isWritableEv
inline bool QHstsStore::isWritable() const
{
    return store.isWritable();
}

//  from src/network/access/qhstsstore.cpp, line 102, as _ZN10QHstsStore16absoluteFilePathERK7QString
inline QString QHstsStore::absoluteFilePath(const QString &dirName)
{
    const QDir dir(dirName.isEmpty() ? QStandardPaths::writableLocation(QStandardPaths::CacheLocation)
                                     : dirName);
    return dir.absoluteFilePath("hstsstore"_L1);
}

//  from src/network/access/qhstsstore.cpp, line 109, as _ZN10QHstsStore15beginHstsGroupsEv
inline void QHstsStore::beginHstsGroups()
{
    store.beginGroup("StrictTransportSecurity"_L1);
    store.beginGroup("Policies"_L1);
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

//  from src/network/access/qhstsstore.cpp, line 121, as _ZN10QHstsStore17deserializePolicyERK7QStringR11QHstsPolicy
inline bool QHstsStore::deserializePolicy(const QString &key, QHstsPolicy &policy)
{
    Q_ASSERT(store.contains(key));

    const QVariant data(store.value(key));
    if (data.isNull() || !data.canConvert<QByteArray>())
        return false;

    const QByteArray serializedData(data.toByteArray());
    QDataStream streamer(serializedData);
    qint64 expiryInMS = 0;
    if (!(streamer >> expiryInMS))
        return false;
    bool includesSubDomains = false;
    if (!(streamer >> includesSubDomains))
        return false;

    policy.setExpiry(QDateTime::fromMSecsSinceEpoch(expiryInMS));
    policy.setIncludesSubDomains(includesSubDomains);

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

//  QHstsStore::QHstsStore(const QString &dirName)
extern "C" Q_DECL_EXPORT
QHstsStore *ritual_ZN10QHstsStoreC1ERK7QString(const QString *dirName) {
  return new QHstsStore(*dirName);
}

//  QHstsStore::~QHstsStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStoreD1Ev(QHstsStore *self) {
  delete self;
}

//  QList<QHstsPolicy> QHstsStore::readPolicies()
extern "C" Q_DECL_EXPORT
QList<QHstsPolicy> *ritual_ZN10QHstsStore12readPoliciesEv(QHstsStore *self) {
  return new QList<QHstsPolicy>(self->readPolicies());
}

//  void QHstsStore::addToObserved(const QHstsPolicy &policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore13addToObservedERK11QHstsPolicy(
    QHstsStore *self,
    const QHstsPolicy *policy) {
  self->addToObserved(*policy);
}

//  void QHstsStore::synchronize()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore11synchronizeEv(QHstsStore *self) {
  self->synchronize();
}

//  bool QHstsStore::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QHstsStore10isWritableEv(const QHstsStore *self) {
  return self->isWritable();
}

//  QString QHstsStore::absoluteFilePath(const QString &dirName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QHstsStore16absoluteFilePathERK7QString(
    const QString *dirName) {
  return new QString(QHstsStore::absoluteFilePath(*dirName));
}

//  void QHstsStore::beginHstsGroups()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsStore15beginHstsGroupsEv(QHstsStore *self) {
  self->beginHstsGroups();
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

//  bool QHstsStore::deserializePolicy(const QString &key, QHstsPolicy
//      &policy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QHstsStore17deserializePolicyERK7QStringR11QHstsPolicy(
    QHstsStore *self,
    const QString *key,
    QHstsPolicy *policy) {
  return self->deserializePolicy(*key, *policy);
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
#endif  // QT_CONFIG(settings)
