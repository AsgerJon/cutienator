//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrouter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrouter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverrouter_p.h>
#include <QtHttpServer/qhttpserverrouter.h>
#include <QtHttpServer/qhttpserverrouterrule.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserver.h>
#include <QtHttpServer/private/qhttpserverrouterrule_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetatype.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qthttpserver/src/httpserver/qhttpserverrouter.cpp, line 26, as local:qhttpserverrouter.cpp:defaultConverters
static const QHash<QMetaType, QString> defaultConverters = {
    { QMetaType::fromType<int>(), u"[+-]?\\d+"_s },
    { QMetaType::fromType<long>(), u"[+-]?\\d+"_s },
    { QMetaType::fromType<long long>(), u"[+-]?\\d+"_s },
    { QMetaType::fromType<short>(), u"[+-]?\\d+"_s },

    { QMetaType::fromType<unsigned int>(), u"[+]?\\d+"_s },
    { QMetaType::fromType<unsigned long>(), u"[+]?\\d+"_s },
    { QMetaType::fromType<unsigned long long>(), u"[+]?\\d+"_s },
    { QMetaType::fromType<unsigned short>(), u"[+]?\\d+"_s },

    { QMetaType::fromType<double>(), u"[+-]?(?:[0-9]+(?:[.][0-9]*)?|[.][0-9]+)"_s },
    { QMetaType::fromType<float>(), u"[+-]?(?:[0-9]+(?:[.][0-9]*)?|[.][0-9]+)"_s },

    { QMetaType::fromType<QString>(), u"[^/]+"_s },
    { QMetaType::fromType<QByteArray>(), u"[^/]+"_s },

    { QMetaType::fromType<QUrl>(), u".*"_s },

    { QMetaType::fromType<void>(), u""_s },
};

//  from ../qthttpserver/src/httpserver/qhttpserverrouter.cpp, line 146, as _ZN24QHttpServerRouterPrivateC1EP19QAbstractHttpServer
inline QHttpServerRouterPrivate::QHttpServerRouterPrivate(QAbstractHttpServer *server)
    : converters(defaultConverters), server(server)
{}
//  -----------------------------------------------------------------------

//  QHttpServerRouterPrivate::QHttpServerRouterPrivate(QAbstractHttpServer
//      *server)
extern "C" Q_DECL_EXPORT
QHttpServerRouterPrivate *ritual_ZN24QHttpServerRouterPrivateC1EP19QAbstractHttpServer(
    QAbstractHttpServer *server) {
  return new QHttpServerRouterPrivate(server);
}

//  QHttpServerRouterPrivate::~QHttpServerRouterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerRouterPrivateD1Ev(
    QHttpServerRouterPrivate *self) {
  delete self;
}
