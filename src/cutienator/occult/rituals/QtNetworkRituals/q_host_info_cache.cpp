//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostinfo.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhostinfo.h"
#include "qhostinfo_p.h"
#include <qplatformdefs.h>
#include "QtCore/qapplicationstatic.h"
#include <qabstracteventdispatcher.h>
#include <qcoreapplication.h>
#include <qmetaobject.h>
#include <qscopeguard.h>
#include <qstringlist.h>
#include <qthread.h>
#include <qurl.h>
#include <private/qobject_p.h>
#include <algorithm>
#ifdef Q_OS_UNIX
#  include <unistd.h>
#  include <netdb.h>
#  include <netinet/in.h>
#elif defined Q_OS_WIN
#  include <ws2tcpip.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qhostinfo.cpp, line 1156, as _ZN14QHostInfoCacheC1Ev
#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
inline QHostInfoCache::QHostInfoCache() : max_age(60), enabled(true), cache(128)
{
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

//  from src/network/kernel/qhostinfo.cpp, line 1160, as _ZN14QHostInfoCache3getERK7QStringPb
#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
inline QHostInfo QHostInfoCache::get(const QString &name, bool *valid)
{
    QMutexLocker locker(&this->mutex);

    *valid = false;
    if (QHostInfoCacheElement *element = cache.object(name)) {
        if (element->age.elapsed() < max_age*1000)
            *valid = true;
        return element->info;

        // FIXME idea:
        // if too old but not expired, trigger a new lookup
        // to freshen our cache
    }

    return QHostInfo();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

//  from src/network/kernel/qhostinfo.cpp, line 1178, as _ZN14QHostInfoCache3putERK7QStringRK9QHostInfo
#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
inline void QHostInfoCache::put(const QString &name, const QHostInfo &info)
{
    // if the lookup failed, don't cache
    if (info.error() != QHostInfo::NoError)
        return;

    QHostInfoCacheElement* element = new QHostInfoCacheElement();
    element->info = info;
    element->age = QElapsedTimer();
    element->age.start();

    QMutexLocker locker(&this->mutex);
    cache.insert(name, element); // cache will take ownership
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

//  from src/network/kernel/qhostinfo.cpp, line 1193, as _ZN14QHostInfoCache5clearEv
#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
inline void QHostInfoCache::clear()
{
    QMutexLocker locker(&this->mutex);
    cache.clear();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  -----------------------------------------------------------------------

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  QHostInfoCache::QHostInfoCache()
extern "C" Q_DECL_EXPORT
QHostInfoCache *ritual_ZN14QHostInfoCacheC1Ev() {
  return new QHostInfoCache();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  QHostInfo QHostInfoCache::get(const QString &name, bool *valid)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN14QHostInfoCache3getERK7QStringPb(
    QHostInfoCache *self,
    const QString *name,
    bool *valid) {
  return new QHostInfo(self->get(*name, valid));
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  void QHostInfoCache::put(const QString &name, const QHostInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHostInfoCache3putERK7QStringRK9QHostInfo(
    QHostInfoCache *self,
    const QString *name,
    const QHostInfo *info) {
  self->put(*name, *info);
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  void QHostInfoCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHostInfoCache5clearEv(QHostInfoCache *self) {
  self->clear();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  bool QHostInfoCache::isEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QHostInfoCache9isEnabledEv(QHostInfoCache *self) {
  return self->isEnabled();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  void QHostInfoCache::setEnabled(bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHostInfoCache10setEnabledEb(QHostInfoCache *self, bool e) {
  self->setEnabled(e);
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
