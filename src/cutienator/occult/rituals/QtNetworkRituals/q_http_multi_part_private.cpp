//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhttpmultipart.h"
#include "qhttpmultipart_p.h"
#include "QtCore/qdatetime.h" // for initializing the random number generator with QTime
#include <QtCore/qdebug.h>
#include "QtCore/qmutex.h"
#include "QtCore/qrandom.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpmultipart.cpp, line 412, as _ZN21QHttpMultiPartPrivateD1Ev
inline QHttpMultiPartPrivate::~QHttpMultiPartPrivate()
{
    delete device;
}
//  -----------------------------------------------------------------------

//  QHttpMultiPartPrivate::~QHttpMultiPartPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttpMultiPartPrivateD1Ev(QHttpMultiPartPrivate *self) {
  delete self;
}

//  QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(QHttpMultiPart
//      *message)
extern "C" Q_DECL_EXPORT
QHttpMultiPartPrivate *ritual_ZN21QHttpMultiPartPrivate3getEP14QHttpMultiPart(
    QHttpMultiPart *message) {
  return QHttpMultiPartPrivate::get(message);
}

//  const QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(const
//      QHttpMultiPart *message)
extern "C" Q_DECL_EXPORT
const QHttpMultiPartPrivate *ritual_ZN21QHttpMultiPartPrivate3getEPK14QHttpMultiPart(
    const QHttpMultiPart *message) {
  return QHttpMultiPartPrivate::get(message);
}

#endif  // QT_CONFIG(http)
