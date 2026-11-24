//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectpendingcall_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qremoteobjectpendingcall.h"
#include "qremoteobjectpendingcall_p.h"
#include "qremoteobjectreplica_p.h"
#include <QtCore/qcoreapplication.h>
#include <private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpendingcall.cpp, line 18, as _ZN28QRemoteObjectPendingCallDataC1EiP34QRemoteObjectReplicaImplementation
inline QRemoteObjectPendingCallData::QRemoteObjectPendingCallData(int serialId, QRemoteObjectReplicaImplementation *replica)
    : replica(replica)
    , serialId(serialId)
    , error(QRemoteObjectPendingCall::InvalidMessage)
    , watcherHelper(nullptr)
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpendingcall.cpp, line 26, as _ZN28QRemoteObjectPendingCallDataD1Ev
inline QRemoteObjectPendingCallData::~QRemoteObjectPendingCallData()
{
}
//  -----------------------------------------------------------------------

//  QRemoteObjectPendingCallData::QRemoteObjectPendingCallData(int serialId,
//      QRemoteObjectReplicaImplementation *replica)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCallData *ritual_ZN28QRemoteObjectPendingCallDataC1EiP34QRemoteObjectReplicaImplementation(
    int serialId,
    QRemoteObjectReplicaImplementation *replica) {
  return new QRemoteObjectPendingCallData(serialId, replica);
}

//  QRemoteObjectPendingCallData::~QRemoteObjectPendingCallData()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QRemoteObjectPendingCallDataD1Ev(
    QRemoteObjectPendingCallData *self) {
  delete self;
}
