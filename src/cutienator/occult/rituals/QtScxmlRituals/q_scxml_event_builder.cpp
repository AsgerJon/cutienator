//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlevent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtScxml/qscxmlglobals.h>
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#if !defined(BUILD_QSCXMLC)
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qscxmlexecutablecontent_p.h"
#include "qscxmlevent_p.h"
#include "qscxmlstatemachine_p.h"
#include <qjsondocument.h>
#include <qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlevent.cpp, line 191, as _ZN18QScxmlEventBuilder11submitErrorERK7QStringS2_S2_
inline void QScxmlEventBuilder::submitError(const QString &type, const QString &msg, const QString &sendid)
{
    QScxmlStateMachinePrivate::get(stateMachine)->submitError(type, msg, sendid);
}
//  -----------------------------------------------------------------------

//  QScxmlEventBuilder::QScxmlEventBuilder()
extern "C" Q_DECL_EXPORT
QScxmlEventBuilder *ritual_ZN18QScxmlEventBuilderC1Ev() {
  return new QScxmlEventBuilder();
}

//  void QScxmlEventBuilder::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlEventBuilder4initEv(QScxmlEventBuilder *self) {
  self->init();
}

//  QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine *stateMachine,
//      const QString &eventName, const QScxmlExecutableContent::DoneData
//      *doneData)
extern "C" Q_DECL_EXPORT
QScxmlEventBuilder *ritual_ZN18QScxmlEventBuilderC1EP18QScxmlStateMachineRK7QStringPKN23QScxmlExecutableContent8DoneDataE(
    QScxmlStateMachine *stateMachine,
    const QString *eventName,
    const QScxmlExecutableContent::DoneData *doneData) {
  return new QScxmlEventBuilder(stateMachine, *eventName, doneData);
}

//  QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine *stateMachine,
//      const QScxmlExecutableContent::Send &send)
extern "C" Q_DECL_EXPORT
QScxmlEventBuilder *ritual_ZN18QScxmlEventBuilderC1EP18QScxmlStateMachineRKN23QScxmlExecutableContent4SendE(
    QScxmlStateMachine *stateMachine,
    const QScxmlExecutableContent::Send *send) {
  return new QScxmlEventBuilder(stateMachine, *send);
}

//  void QScxmlEventBuilder::submitError(const QString &type, const QString
//      &msg, const QString &sendid)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlEventBuilder11submitErrorERK7QStringS2_S2_(
    QScxmlEventBuilder *self,
    const QString *type,
    const QString *msg,
    const QString *sendid) {
  self->submitError(*type, *msg, *sendid);
}

//  QScxmlEventBuilder::~QScxmlEventBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlEventBuilderD1Ev(QScxmlEventBuilder *self) {
  delete self;
}

#endif  // !defined(BUILD_QSCXMLC)
