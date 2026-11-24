//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qrestaccessmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qrestaccessmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/private/qrestaccessmanager_p.h>
#include <QtNetwork/qrestreply.h>
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qthread.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qrestaccessmanager.cpp, line 581, as _ZN25QRestAccessManagerPrivateD1Ev
inline QRestAccessManagerPrivate::~QRestAccessManagerPrivate()
{
    if (!activeRequests.isEmpty()) {
        qCWarning(lcQrest, "Access manager destroyed while %lld requests were still in progress",
                  qlonglong(activeRequests.size()));
    }
}
//  -----------------------------------------------------------------------

//  QRestAccessManagerPrivate::~QRestAccessManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRestAccessManagerPrivateD1Ev(
    QRestAccessManagerPrivate *self) {
  delete self;
}

//  QRestAccessManager *QRestAccessManagerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRestAccessManager *ritual_ZN25QRestAccessManagerPrivate6q_funcEv(
    QRestAccessManagerPrivate *self) {
  return self->q_func();
}

//  const QRestAccessManager *QRestAccessManagerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRestAccessManager *ritual_ZNK25QRestAccessManagerPrivate6q_funcEv(
    const QRestAccessManagerPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(http)
