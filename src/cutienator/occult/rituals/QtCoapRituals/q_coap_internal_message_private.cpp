//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapinternalmessage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapinternalmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoapinternalmessage_p.h"
#include "qcoaprequest_p.h"
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 21, as _ZN27QCoapInternalMessagePrivateD1Ev
inline QCoapInternalMessagePrivate::~QCoapInternalMessagePrivate()
{
}
//  -----------------------------------------------------------------------

//  QCoapInternalMessagePrivate::QCoapInternalMessagePrivate()
extern "C" Q_DECL_EXPORT
QCoapInternalMessagePrivate *ritual_ZN27QCoapInternalMessagePrivateC1Ev() {
  return new QCoapInternalMessagePrivate();
}

//  QCoapInternalMessagePrivate::~QCoapInternalMessagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCoapInternalMessagePrivateD1Ev(
    QCoapInternalMessagePrivate *self) {
  delete self;
}
