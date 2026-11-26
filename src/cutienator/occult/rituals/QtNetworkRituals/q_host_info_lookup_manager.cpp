//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostinfo.h>
#include <QtNetwork/private/qhostinfo_p.h>
#include <qplatformdefs.h>
#include "QtCore/qapplicationstatic.h"
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/qurl.h>
#include <QtCore/private/qobject_p.h>
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

using namespace Qt::StringLiterals;

//  from src/network/kernel/qhostinfo.cpp, line 46, as local:qhostinfo.cpp:ToBeLookedUpEquals
namespace {
struct ToBeLookedUpEquals {
    typedef bool result_type;
    explicit ToBeLookedUpEquals(const QString &toBeLookedUp) noexcept : m_toBeLookedUp(toBeLookedUp) {}
    result_type operator()(QHostInfoRunnable* lookup) const noexcept
    {
        return m_toBeLookedUp == lookup->toBeLookedUp;
    }
private:
    QString m_toBeLookedUp;
};
}  // namespace

//  from src/network/kernel/qhostinfo.cpp, line 57, as local:qhostinfo.cpp:separate_if
namespace {
inline template <typename InputIt, typename OutputIt1, typename OutputIt2, typename UnaryPredicate>
std::pair<OutputIt1, OutputIt2> separate_if(InputIt first, InputIt last, OutputIt1 dest1, OutputIt2 dest2, UnaryPredicate p)
{
    while (first != last) {
        if (p(*first)) {
            *dest1 = *first;
            ++dest1;
        } else {
            *dest2 = *first;
            ++dest2;
        }
        ++first;
    }
    return std::make_pair(dest1, dest2);
}
}  // namespace

//  from src/network/kernel/qhostinfo.cpp, line 1156, as _ZN14QHostInfoCacheC1Ev
#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
inline QHostInfoCache::QHostInfoCache() : max_age(60), enabled(true), cache(128)
{
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

//  from src/network/kernel/qhostinfo.cpp, line 941, as _ZN22QHostInfoLookupManager23rescheduleWithMutexHeldEv
inline void QHostInfoLookupManager::rescheduleWithMutexHeld()
{
    if (wasDeleted)
        return;

    // goals of this function:
    //  - launch new lookups via the thread pool
    //  - make sure only one lookup per host/IP is in progress

    if (!finishedLookups.isEmpty()) {
        // remove ID from aborted if it is in there
        for (int i = 0; i < finishedLookups.size(); i++) {
           abortedLookups.removeAll(finishedLookups.at(i)->id);
        }

        finishedLookups.clear();
    }

#if QT_CONFIG(thread)
    auto isAlreadyRunning = [this](QHostInfoRunnable *lookup) {
        return std::any_of(currentLookups.cbegin(), currentLookups.cend(), ToBeLookedUpEquals(lookup->toBeLookedUp));
    };

    // Transfer any postponed lookups that aren't currently running to the scheduled list, keeping already-running lookups:
    postponedLookups.erase(separate_if(postponedLookups.begin(),
                                       postponedLookups.end(),
                                       postponedLookups.begin(),
                                       std::front_inserter(scheduledLookups), // prepend! we want to finish it ASAP
                                       isAlreadyRunning).first,
                           postponedLookups.end());

    // Unschedule and postpone any that are currently running:
    scheduledLookups.erase(separate_if(scheduledLookups.begin(),
                                       scheduledLookups.end(),
                                       std::back_inserter(postponedLookups),
                                       scheduledLookups.begin(),
                                       isAlreadyRunning).second,
                           scheduledLookups.end());

    const int availableThreads = std::max(threadPool.maxThreadCount(), 1) - currentLookups.size();
    if (availableThreads > 0) {
        int readyToStartCount = qMin(availableThreads, scheduledLookups.size());
        auto it = scheduledLookups.begin();
        while (readyToStartCount--) {
            // runnable now running in new thread, track this in currentLookups
            threadPool.start(*it);
            currentLookups.push_back(std::move(*it));
            ++it;
        }
        scheduledLookups.erase(scheduledLookups.begin(), it);
    }
#else
    if (!scheduledLookups.isEmpty())
        scheduledLookups.takeFirst()->run();
#endif
}

//  from src/network/kernel/qhostinfo.cpp, line 900, as _ZN22QHostInfoLookupManagerC1Ev
inline QHostInfoLookupManager::QHostInfoLookupManager() : wasDeleted(false)
{
#if QT_CONFIG(thread)
    QObject::connect(QCoreApplication::instance(), &QObject::destroyed,
                     &threadPool, [&](QObject *) { threadPool.waitForDone(); },
                     Qt::DirectConnection);
    threadPool.setMaxThreadCount(20); // do up to 20 DNS lookups in parallel
#endif
}

//  from src/network/kernel/qhostinfo.cpp, line 910, as _ZN22QHostInfoLookupManagerD1Ev
inline QHostInfoLookupManager::~QHostInfoLookupManager()
{
    QMutexLocker locker(&mutex);
    wasDeleted = true;
    locker.unlock();

    // don't qDeleteAll currentLookups, the QThreadPool has ownership
    clear();
}

//  from src/network/kernel/qhostinfo.cpp, line 920, as _ZN22QHostInfoLookupManager5clearEv
inline void QHostInfoLookupManager::clear()
{
    {
        QMutexLocker locker(&mutex);
        qDeleteAll(scheduledLookups);
        qDeleteAll(finishedLookups);
#if QT_CONFIG(thread)
        qDeleteAll(postponedLookups);
        postponedLookups.clear();
#endif
        scheduledLookups.clear();
        finishedLookups.clear();
    }

#if QT_CONFIG(thread)
    threadPool.waitForDone();
#endif
    cache.clear();
}

//  from src/network/kernel/qhostinfo.cpp, line 999, as _ZN22QHostInfoLookupManager14scheduleLookupEP17QHostInfoRunnable
inline void QHostInfoLookupManager::scheduleLookup(QHostInfoRunnable *r)
{
    QMutexLocker locker(&this->mutex);

    if (wasDeleted)
        return;

    scheduledLookups.enqueue(r);
    rescheduleWithMutexHeld();
}

//  from src/network/kernel/qhostinfo.cpp, line 1011, as _ZN22QHostInfoLookupManager11abortLookupEi
inline void QHostInfoLookupManager::abortLookup(int id)
{
    QMutexLocker locker(&this->mutex);

    if (wasDeleted)
        return;

    if (id == -1)
        return;

#if QT_CONFIG(thread)
    // is postponed? delete and return
    for (int i = 0; i < postponedLookups.size(); i++) {
        if (postponedLookups.at(i)->id == id) {
            delete postponedLookups.takeAt(i);
            return;
        }
    }
#endif

    // is scheduled? delete and return
    for (int i = 0; i < scheduledLookups.size(); i++) {
        if (scheduledLookups.at(i)->id == id) {
            delete scheduledLookups.takeAt(i);
            return;
        }
    }

    if (!abortedLookups.contains(id))
        abortedLookups.append(id);
}

//  from src/network/kernel/qhostinfo.cpp, line 1055, as _ZN22QHostInfoLookupManager14lookupFinishedEP17QHostInfoRunnable
inline void QHostInfoLookupManager::lookupFinished(QHostInfoRunnable *r)
{
    QMutexLocker locker(&this->mutex);

    if (wasDeleted)
        return;

#if QT_CONFIG(thread)
    currentLookups.removeOne(r);
#endif
    finishedLookups.append(r);
    rescheduleWithMutexHeld();
}

//  from src/network/kernel/qhostinfo.cpp, line 1044, as _ZN22QHostInfoLookupManager10wasAbortedEi
inline bool QHostInfoLookupManager::wasAborted(int id)
{
    QMutexLocker locker(&this->mutex);

    if (wasDeleted)
        return true;

    return abortedLookups.contains(id);
}
//  -----------------------------------------------------------------------

//  QHostInfoLookupManager::QHostInfoLookupManager()
extern "C" Q_DECL_EXPORT
QHostInfoLookupManager *ritual_ZN22QHostInfoLookupManagerC1Ev() {
  return new QHostInfoLookupManager();
}

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  QHostInfoLookupManager::~QHostInfoLookupManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHostInfoLookupManagerD1Ev(QHostInfoLookupManager *self) {
  delete self;
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

#if defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)
//  void QHostInfoLookupManager::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHostInfoLookupManager5clearEv(
    QHostInfoLookupManager *self) {
  self->clear();
}
#endif  // defined(QT_BUILD_INTERNAL) || QT_CONFIG(hostinfocache)

//  void QHostInfoLookupManager::scheduleLookup(QHostInfoRunnable *r)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHostInfoLookupManager14scheduleLookupEP17QHostInfoRunnable(
    QHostInfoLookupManager *self,
    QHostInfoRunnable *r) {
  self->scheduleLookup(r);
}

//  void QHostInfoLookupManager::abortLookup(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHostInfoLookupManager11abortLookupEi(
    QHostInfoLookupManager *self,
    int id) {
  self->abortLookup(id);
}

//  void QHostInfoLookupManager::lookupFinished(QHostInfoRunnable *r)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHostInfoLookupManager14lookupFinishedEP17QHostInfoRunnable(
    QHostInfoLookupManager *self,
    QHostInfoRunnable *r) {
  self->lookupFinished(r);
}

//  bool QHostInfoLookupManager::wasAborted(int id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHostInfoLookupManager10wasAbortedEi(
    QHostInfoLookupManager *self,
    int id) {
  return self->wasAborted(id);
}
