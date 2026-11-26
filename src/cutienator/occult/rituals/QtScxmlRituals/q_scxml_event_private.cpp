//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlevent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtScxml/private/qscxmlevent_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlevent.cpp, line 549, as _ZN18QScxmlEventPrivate11debugStringEP11QScxmlEvent
inline QByteArray QScxmlEventPrivate::debugString(QScxmlEvent *event)
{
    if (event == nullptr) {
        return "<null>";
    }

    QJsonObject o;
    if (!event->name().isNull())
        o[QStringLiteral("name")] = event->name();
    if (!event->scxmlType().isNull())
        o[QStringLiteral("type")] = event->scxmlType();
    if (!event->sendId().isNull())
        o[QStringLiteral("sendid")] = event->sendId();
    if (!event->origin().isNull())
        o[QStringLiteral("origin")] = event->origin();
    if (!event->originType().isNull())
        o[QStringLiteral("origintype")] = event->originType();
    if (!event->invokeId().isNull())
        o[QStringLiteral("invokeid")] = event->invokeId();
    if (!event->data().isNull())
        o[QStringLiteral("data")] = QJsonValue::fromVariant(event->data());

    return QJsonDocument(o).toJson(QJsonDocument::Compact);
}
//  -----------------------------------------------------------------------

//  QScxmlEventPrivate::QScxmlEventPrivate()
extern "C" Q_DECL_EXPORT
QScxmlEventPrivate *ritual_ZN18QScxmlEventPrivateC1Ev() {
  return new QScxmlEventPrivate();
}

//  QByteArray QScxmlEventPrivate::debugString(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QScxmlEventPrivate11debugStringEP11QScxmlEvent(
    QScxmlEvent *event) {
  return new QByteArray(QScxmlEventPrivate::debugString(event));
}

//  QScxmlEventPrivate::~QScxmlEventPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlEventPrivateD1Ev(QScxmlEventPrivate *self) {
  delete self;
}
