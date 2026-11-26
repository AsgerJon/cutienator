//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/qscxmlexecutablecontent.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/private/qscxmlinvokableservice_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlinvokableservice.cpp, line 124, as _ZN36QScxmlInvokableServiceFactoryPrivateC1ERKN23QScxmlExecutableContent10InvokeInfoERK5QListIiERKS4_INS0_13ParameterInfoEE
inline QScxmlInvokableServiceFactoryPrivate::QScxmlInvokableServiceFactoryPrivate(
        const QScxmlExecutableContent::InvokeInfo &invokeInfo,
        const QList<QScxmlExecutableContent::StringId> &namelist,
        const QList<QScxmlExecutableContent::ParameterInfo> &parameters)
    : invokeInfo(invokeInfo)
    , names(namelist)
    , parameters(parameters)
{}
//  -----------------------------------------------------------------------

//  QScxmlInvokableServiceFactoryPrivate::QScxmlInvokableServiceFactoryPrivat
//      e(const QScxmlExecutableContent::InvokeInfo &invokeInfo, const
//      QList<QScxmlExecutableContent::StringId> &names, const
//      QList<QScxmlExecutableContent::ParameterInfo> &parameters)
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactoryPrivate *ritual_ZN36QScxmlInvokableServiceFactoryPrivateC1ERKN23QScxmlExecutableContent10InvokeInfoERK5QListIiERKS4_INS0_13ParameterInfoEE(
    const QScxmlExecutableContent::InvokeInfo *invokeInfo,
    const QList<QScxmlExecutableContent::StringId> *names,
    const QList<QScxmlExecutableContent::ParameterInfo> *parameters) {
  return new QScxmlInvokableServiceFactoryPrivate(
      *invokeInfo,
      *names,
      *parameters);
}
