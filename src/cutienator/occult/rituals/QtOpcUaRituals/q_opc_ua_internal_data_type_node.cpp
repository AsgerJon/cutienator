//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuainternaldatatypenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuainternaldatatypenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qopcuainternaldatatypenode_p.h"
#include "qopcuagenericstructhandler_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 73, as _ZNK26QOpcUaInternalDataTypeNode10definitionEv
inline QVariant QOpcUaInternalDataTypeNode::definition() const
{
    return m_definition;
}

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 78, as _ZNK26QOpcUaInternalDataTypeNode10isAbstractEv
inline bool QOpcUaInternalDataTypeNode::isAbstract() const
{
    return m_isAbstract;
}

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 83, as _ZNK26QOpcUaInternalDataTypeNode4nameEv
inline QString QOpcUaInternalDataTypeNode::name() const
{
    return m_name;
}

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 88, as _ZNK26QOpcUaInternalDataTypeNode6nodeIdEv
inline QString QOpcUaInternalDataTypeNode::nodeId() const
{
    return m_nodeId;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QOpcUaInternalDataTypeNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QOpcUaInternalDataTypeNode10metaObjectEv(
    const QOpcUaInternalDataTypeNode *self) {
  return self->metaObject();
}

//  QVariant QOpcUaInternalDataTypeNode::definition() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QOpcUaInternalDataTypeNode10definitionEv(
    const QOpcUaInternalDataTypeNode *self) {
  return new QVariant(self->definition());
}

//  bool QOpcUaInternalDataTypeNode::isAbstract() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaInternalDataTypeNode10isAbstractEv(
    const QOpcUaInternalDataTypeNode *self) {
  return self->isAbstract();
}

//  QString QOpcUaInternalDataTypeNode::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaInternalDataTypeNode4nameEv(
    const QOpcUaInternalDataTypeNode *self) {
  return new QString(self->name());
}

//  QString QOpcUaInternalDataTypeNode::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaInternalDataTypeNode6nodeIdEv(
    const QOpcUaInternalDataTypeNode *self) {
  return new QString(self->nodeId());
}
