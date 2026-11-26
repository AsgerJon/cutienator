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
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
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

//  from ../qtscxml/src/scxml/qscxmlinvokableservice.cpp, line 225, as _ZNK29QScxmlInvokableServicePrivate13calculateDataEP18QScxmlStateMachineRK5QListIN23QScxmlExecutableContent13ParameterInfoEERKS2_IiEPb
inline QVariantMap QScxmlInvokableServicePrivate::calculateData(
        QScxmlStateMachine *parent,
        const QList<QScxmlExecutableContent::ParameterInfo> &parameters,
        const QList<QScxmlExecutableContent::StringId> &names,
        bool *ok) const
{
    Q_ASSERT(ok);

    QVariantMap result;
    auto dataModel = parent->dataModel();
    auto tableData = parent->tableData();

    for (const QScxmlExecutableContent::ParameterInfo &param : parameters) {
        auto name = tableData->string(param.name);

        if (param.expr != QScxmlExecutableContent::NoEvaluator) {
            *ok = false;
            auto v = dataModel->evaluateToVariant(param.expr, ok);
            if (!*ok)
                return QVariantMap();
            result.insert(name, v);
        } else {
            QString loc;
            if (param.location != QScxmlExecutableContent::NoString) {
                loc = tableData->string(param.location);
            }

            if (loc.isEmpty()) {
                // TODO: error message?
                *ok = false;
                return QVariantMap();
            }

            auto v = dataModel->scxmlProperty(loc);
            result.insert(name, v);
        }
    }

    for (QScxmlExecutableContent::StringId locid : names) {
        QString loc;
        if (locid != QScxmlExecutableContent::NoString) {
            loc = tableData->string(locid);
        }
        if (loc.isEmpty()) {
            // TODO: error message?
            *ok = false;
            return QVariantMap();
        }
        if (dataModel->hasScxmlProperty(loc)) {
            auto v = dataModel->scxmlProperty(loc);
            result.insert(loc, v);
        } else {
            *ok = false;
            return QVariantMap();
        }
    }

    return result;
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

//  QVariantMap
//      QScxmlInvokableServicePrivate::calculateData(QScxmlStateMachine
//      *parent, const QList<QScxmlExecutableContent::ParameterInfo>
//      &parameters, const QList<QScxmlExecutableContent::StringId> &names,
//      bool *ok) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK29QScxmlInvokableServicePrivate13calculateDataEP18QScxmlStateMachineRK5QListIN23QScxmlExecutableContent13ParameterInfoEERKS2_IiEPb(
    const QScxmlInvokableServicePrivate *self,
    QScxmlStateMachine *parent,
    const QList<QScxmlExecutableContent::ParameterInfo> *parameters,
    const QList<QScxmlExecutableContent::StringId> *names,
    bool *ok) {
  return new QMap<QString, QVariant>(
      self->calculateData(
          parent,
          *parameters,
          *names,
          ok));
}
