//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponse.h>
#include <private/qhttpserverresponder_p.h>
#include <private/qhttpserverliterals_p.h>
#include <private/qhttpserverrequest_p.h>
#include <private/qhttpserverresponse_p.h>
#include <private/qhttpserverstream_p.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qloggingcategory.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 124, as _ZN27QHttpServerResponderPrivate6cancelEv
inline void QHttpServerResponderPrivate::cancel()
{
    canceled = true;
}
//  -----------------------------------------------------------------------

//  void QHttpServerResponderPrivate::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate6cancelEv(
    QHttpServerResponderPrivate *self) {
  self->cancel();
}
