//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhsts_p.h>
#include <QtNetwork/qhttpheaders.h>
#include "QtCore/private/qipaddress_p.h"
#include "QtCore/qlist.h"
#if QT_CONFIG(settings)
#include <QtNetwork/private/qhstsstore_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhsts.cpp, line 191, as _ZN10QHstsCache5clearEv
inline void QHstsCache::clear()
{
    knownHosts.clear();
}

//  from src/network/access/qhsts.cpp, line 196, as _ZNK10QHstsCache8policiesEv
inline QList<QHstsPolicy> QHstsCache::policies() const
{
    QList<QHstsPolicy> values;
    values.reserve(int(knownHosts.size()));
    for (const auto &host : knownHosts)
        values << host.second;
    return values;
}
//  -----------------------------------------------------------------------

//  void QHstsCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsCache5clearEv(QHstsCache *self) {
  self->clear();
}

//  QList<QHstsPolicy> QHstsCache::policies() const
extern "C" Q_DECL_EXPORT
QList<QHstsPolicy> *ritual_ZNK10QHstsCache8policiesEv(
    const QHstsCache *self) {
  return new QList<QHstsPolicy>(self->policies());
}

//  QHstsCache::~QHstsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsCacheD1Ev(QHstsCache *self) {
  delete self;
}
