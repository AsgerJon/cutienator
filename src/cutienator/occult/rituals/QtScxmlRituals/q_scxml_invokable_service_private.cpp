//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/qscxmlexecutablecontent.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qscxmlglobals_p.h"
#include "qscxmlinvokableservice_p.h"
#include "qscxmlstatemachine_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlinvokableservice.cpp, line 117, as _ZN29QScxmlInvokableServicePrivateC1EP18QScxmlStateMachine
inline QScxmlInvokableServicePrivate::QScxmlInvokableServicePrivate(QScxmlStateMachine *parentStateMachine)
    : parentStateMachine(parentStateMachine)
{
    static int metaType = qRegisterMetaType<QScxmlInvokableService *>();
    Q_UNUSED(metaType);
}

//  from ../qtscxml/src/scxml/qscxmlinvokableservice.cpp, line 199, as _ZNK29QScxmlInvokableServicePrivate11calculateIdEP18QScxmlStateMachineRKN23QScxmlExecutableContent10InvokeInfoEPb
inline QString QScxmlInvokableServicePrivate::calculateId(
        QScxmlStateMachine *parent, const QScxmlExecutableContent::InvokeInfo &invokeInfo,
        bool *ok) const
{
    Q_ASSERT(ok);
    *ok = true;
    auto stateMachine = parent->tableData();

    if (invokeInfo.id != QScxmlExecutableContent::NoString) {
        return stateMachine->string(invokeInfo.id);
    }

    const QString newId = QScxmlStateMachinePrivate::generateSessionId(
                stateMachine->string(invokeInfo.prefix));

    if (invokeInfo.location != QScxmlExecutableContent::NoString) {
        auto idloc = stateMachine->string(invokeInfo.location);
        auto ctxt = stateMachine->string(invokeInfo.context);
        *ok = parent->dataModel()->setScxmlProperty(idloc, newId, ctxt);
        if (!*ok)
            return QString();
    }

    return newId;
}
//  -----------------------------------------------------------------------

//  QScxmlInvokableServicePrivate::QScxmlInvokableServicePrivate(QScxmlStateM
//      achine *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableServicePrivate *ritual_ZN29QScxmlInvokableServicePrivateC1EP18QScxmlStateMachine(
    QScxmlStateMachine *parentStateMachine) {
  return new QScxmlInvokableServicePrivate(parentStateMachine);
}

//  QString QScxmlInvokableServicePrivate::calculateId(QScxmlStateMachine
//      *parent, const QScxmlExecutableContent::InvokeInfo &invokeInfo, bool
//      *ok) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QScxmlInvokableServicePrivate11calculateIdEP18QScxmlStateMachineRKN23QScxmlExecutableContent10InvokeInfoEPb(
    const QScxmlInvokableServicePrivate *self,
    QScxmlStateMachine *parent,
    const QScxmlExecutableContent::InvokeInfo *invokeInfo,
    bool *ok) {
  return new QString(self->calculateId(parent, *invokeInfo, ok));
}
