//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapinternalmessage_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 21, as _ZN27QCoapInternalMessagePrivateD2Ev
inline QCoapInternalMessagePrivate::~QCoapInternalMessagePrivate()
{
}
//  -----------------------------------------------------------------------

//  QCoapInternalRequestPrivate::QCoapInternalRequestPrivate()
extern "C" Q_DECL_EXPORT
QCoapInternalRequestPrivate *ritual_ZN27QCoapInternalRequestPrivateC1Ev() {
  return new QCoapInternalRequestPrivate();
}

//  QCoapInternalRequest *QCoapInternalRequestPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapInternalRequest *ritual_ZN27QCoapInternalRequestPrivate6q_funcEv(
    QCoapInternalRequestPrivate *self) {
  return self->q_func();
}

//  const QCoapInternalRequest *QCoapInternalRequestPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapInternalRequest *ritual_ZNK27QCoapInternalRequestPrivate6q_funcEv(
    const QCoapInternalRequestPrivate *self) {
  return self->q_func();
}
