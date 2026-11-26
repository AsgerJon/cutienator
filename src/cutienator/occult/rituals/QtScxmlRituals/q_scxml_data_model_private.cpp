//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmldatamodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/qscxmldatamodel.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmldatamodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtScxml/qscxmlnulldatamodel.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtScxml/private/qscxmldatamodelplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmldatamodel.cpp, line 149, as _ZN22QScxmlDataModelPrivate20instantiateDataModelEN13DocumentModel5Scxml13DataModelTypeE
inline QScxmlDataModel *QScxmlDataModelPrivate::instantiateDataModel(DocumentModel::Scxml::DataModelType type)
{
    QScxmlDataModel *dataModel = nullptr;
    switch (type) {
    case DocumentModel::Scxml::NullDataModel:
        dataModel = new QScxmlNullDataModel;
        break;
    case DocumentModel::Scxml::JSDataModel:
        dataModel = QScxmlDataModel::createScxmlDataModel(QStringLiteral("ecmascriptdatamodel"));
        break;
    case DocumentModel::Scxml::CppDataModel:
        break;
    default:
        Q_UNREACHABLE();
    }
    return dataModel;
}
//  -----------------------------------------------------------------------

//  QScxmlDataModel *QScxmlDataModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZN22QScxmlDataModelPrivate6q_funcEv(
    QScxmlDataModelPrivate *self) {
  return self->q_func();
}

//  const QScxmlDataModel *QScxmlDataModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScxmlDataModel *ritual_ZNK22QScxmlDataModelPrivate6q_funcEv(
    const QScxmlDataModelPrivate *self) {
  return self->q_func();
}

//  QScxmlDataModelPrivate::QScxmlDataModelPrivate()
extern "C" Q_DECL_EXPORT
QScxmlDataModelPrivate *ritual_ZN22QScxmlDataModelPrivateC1Ev() {
  return new QScxmlDataModelPrivate();
}

//  QScxmlDataModel *QScxmlDataModelPrivate::instantiateDataModel(DocumentMod
//      el::Scxml::DataModelType type)
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZN22QScxmlDataModelPrivate20instantiateDataModelEN13DocumentModel5Scxml13DataModelTypeE(
    DocumentModel::Scxml::DataModelType type) {
  return QScxmlDataModelPrivate::instantiateDataModel(type);
}

//  void QScxmlDataModelPrivate::setStateMachine(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlDataModelPrivate15setStateMachineEP18QScxmlStateMachine(
    QScxmlDataModelPrivate *self,
    QScxmlStateMachine *stateMachine) {
  self->setStateMachine(stateMachine);
}

//  void QScxmlDataModelPrivate::emitStateMachineChanged(QScxmlStateMachine
//      *newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlDataModelPrivate23emitStateMachineChangedEP18QScxmlStateMachine(
    QScxmlDataModelPrivate *self,
    QScxmlStateMachine *newValue) {
  self->emitStateMachineChanged(newValue);
}

//  size_t QScxmlDataModelPrivate::_qt_property_m_stateMachine_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN22QScxmlDataModelPrivate34_qt_property_m_stateMachine_offsetEv() {
  return QScxmlDataModelPrivate::_qt_property_m_stateMachine_offset();
}
