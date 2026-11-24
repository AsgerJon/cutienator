//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuagenericstructhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuagenericstructhandler.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuagenericstructhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuastructuredefinition.h>
#include <QtOpcUa/qopcuaenumdefinition.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/private/qopcuainternaldatatypenode_p.h>
#include <QtOpcUa/private/qopcuagenericstructhandler_p.h>
#include <QtOpcUa/private/qopcuagenericstructhandler_p.h>
#include <QtOpcUa/qopcuaargument.h>
#include <QtOpcUa/qopcuaaxisinformation.h>
#include <QtOpcUa/qopcuabinarydataencoding.h>
#include <QtOpcUa/qopcuacomplexnumber.h>
#include <QtOpcUa/qopcuadatavalue.h>
#include <QtOpcUa/qopcuadiagnosticinfo.h>
#include <QtOpcUa/qopcuadoublecomplexnumber.h>
#include <QtOpcUa/qopcuaenumfield.h>
#include <QtOpcUa/qopcuaeuinformation.h>
#include <QtOpcUa/qopcuagenericstructhandler.h>
#include <QtOpcUa/qopcuagenericstructvalue.h>
#include <QtOpcUa/qopcuarange.h>
#include <QtOpcUa/qopcuastructurefield.h>
#include <QtOpcUa/qopcuaxvalue.h>
#include <QtOpcUa/private/qopcuainternaldatatypenode_p.h>
#include <QtCore/quuid.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 93, as _ZNK26QOpcUaInternalDataTypeNode8childrenEv
inline const std::vector<std::unique_ptr<QOpcUaInternalDataTypeNode> > &QOpcUaInternalDataTypeNode::children() const
{
    return m_children;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 30, as _ZN33QOpcUaGenericStructHandlerPrivateC1EP12QOpcUaClient
inline QOpcUaGenericStructHandlerPrivate::QOpcUaGenericStructHandlerPrivate(QOpcUaClient *client)
    : m_client(client)
{
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 110, as _ZNK33QOpcUaGenericStructHandlerPrivate38structureDefinitionForBinaryEncodingIdERK7QString
inline QOpcUaStructureDefinition QOpcUaGenericStructHandlerPrivate::structureDefinitionForBinaryEncodingId(const QString &id) const
{
    const auto entry = m_structuresByEncodingId.constFind(id);
    return entry != m_structuresByEncodingId.constEnd() ? entry.value().structureDefinition : QOpcUaStructureDefinition();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 116, as _ZNK33QOpcUaGenericStructHandlerPrivate28structureDefinitionForTypeIdERK7QString
inline QOpcUaStructureDefinition QOpcUaGenericStructHandlerPrivate::structureDefinitionForTypeId(const QString &id) const
{
    const auto entry = m_structuresByTypeId.constFind(id);
    return entry != m_structuresByTypeId.constEnd() ? entry.value().structureDefinition : QOpcUaStructureDefinition();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 122, as _ZNK33QOpcUaGenericStructHandlerPrivate23enumDefinitionForTypeIdERK7QString
inline QOpcUaEnumDefinition QOpcUaGenericStructHandlerPrivate::enumDefinitionForTypeId(const QString &id) const
{
    const auto entry = m_enumsByTypeId.constFind(id);
    return entry != m_enumsByTypeId.constEnd() ? entry.value().enumDefinition : QOpcUaEnumDefinition();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 128, as _ZNK33QOpcUaGenericStructHandlerPrivate27typeNameForBinaryEncodingIdERK7QString
inline QString QOpcUaGenericStructHandlerPrivate::typeNameForBinaryEncodingId(const QString &id) const
{
    const auto entry = m_typeNamesByEncodingId.constFind(id);
    return entry != m_typeNamesByEncodingId.constEnd() ? entry.value() : QString();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 134, as _ZNK33QOpcUaGenericStructHandlerPrivate17typeNameForTypeIdERK7QString
inline QString QOpcUaGenericStructHandlerPrivate::typeNameForTypeId(const QString &id) const
{
    const auto entry = m_typeNamesByTypeId.constFind(id);
    return entry != m_typeNamesByTypeId.constEnd() ? entry.value() : QString();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 140, as _ZNK33QOpcUaGenericStructHandlerPrivate21dataTypeKindForTypeIdERK7QString
inline QOpcUaGenericStructHandler::DataTypeKind QOpcUaGenericStructHandlerPrivate::dataTypeKindForTypeId(const QString &id) const
{
    const auto isStruct = m_structuresByTypeId.constFind(id);
    if (isStruct != m_structuresByTypeId.constEnd())
        return QOpcUaGenericStructHandler::DataTypeKind::Struct;

    const auto isEnum = m_enumsByTypeId.constFind(id);
    if (isEnum != m_enumsByTypeId.constEnd())
        return QOpcUaGenericStructHandler::DataTypeKind::Enum;

    return typeNameForTypeId(id).isEmpty() ?
               QOpcUaGenericStructHandler::DataTypeKind::Unknown : QOpcUaGenericStructHandler::DataTypeKind::Other;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 154, as _ZNK33QOpcUaGenericStructHandlerPrivate25typeIdForBinaryEncodingIdERK7QString
inline QString QOpcUaGenericStructHandlerPrivate::typeIdForBinaryEncodingId(const QString &id) const
{
    const auto entry = m_structuresByEncodingId.constFind(id);
    return entry != m_structuresByEncodingId.constEnd() ? entry->nodeId : QString();
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 160, as _ZNK33QOpcUaGenericStructHandlerPrivate16isAbstractTypeIdERK7QString
inline bool QOpcUaGenericStructHandlerPrivate::isAbstractTypeId(const QString &id) const
{
    return m_abstractTypeIds.contains(id);
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 754, as _ZN33QOpcUaGenericStructHandlerPrivate14handleFinishedEb
inline void QOpcUaGenericStructHandlerPrivate::handleFinished(bool success)
{
    if (m_hasError)
        return;

    m_finishedCount++;
    m_hasError = !success;

    Q_Q(QOpcUaGenericStructHandler);

    if (m_finishedCount == 1 || m_hasError) {
        m_initialized = !m_hasError;
        emit q->initializedChanged(m_initialized);
    }
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 831, as _ZNK33QOpcUaGenericStructHandlerPrivate11initializedEv
inline bool QOpcUaGenericStructHandlerPrivate::initialized() const
{
    return m_initialized;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 949, as _ZN33QOpcUaGenericStructHandlerPrivate34processSubtypeOfKnownTypeRecursiveEP26QOpcUaInternalDataTypeNodeRK7QString
inline void QOpcUaGenericStructHandlerPrivate::processSubtypeOfKnownTypeRecursive(QOpcUaInternalDataTypeNode *node, const QString &id)
{
    m_typeNamesByTypeId[node->nodeId()] = node->name();

    if (node->isAbstract())
        m_abstractTypeIds.insert(node->nodeId());

    if (node->nodeId() != id)
        m_knownSubtypes[node->nodeId()] = id;

    for (const auto &child : node->children())
        processSubtypeOfKnownTypeRecursive(child.get(), id);
}
//  -----------------------------------------------------------------------

//  QOpcUaGenericStructHandler *QOpcUaGenericStructHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandler *ritual_ZN33QOpcUaGenericStructHandlerPrivate6q_funcEv(
    QOpcUaGenericStructHandlerPrivate *self) {
  return self->q_func();
}

//  const QOpcUaGenericStructHandler
//      *QOpcUaGenericStructHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaGenericStructHandler *ritual_ZNK33QOpcUaGenericStructHandlerPrivate6q_funcEv(
    const QOpcUaGenericStructHandlerPrivate *self) {
  return self->q_func();
}

//  QOpcUaGenericStructHandlerPrivate::QOpcUaGenericStructHandlerPrivate(QOpc
//      UaClient *client)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandlerPrivate *ritual_ZN33QOpcUaGenericStructHandlerPrivateC1EP12QOpcUaClient(
    QOpcUaClient *client) {
  return new QOpcUaGenericStructHandlerPrivate(client);
}

//  QOpcUaStructureDefinition QOpcUaGenericStructHandlerPrivate::structureDef
//      initionForBinaryEncodingId(const QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZNK33QOpcUaGenericStructHandlerPrivate38structureDefinitionForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QOpcUaStructureDefinition(
      self->structureDefinitionForBinaryEncodingId(
          *id));
}

//  QOpcUaStructureDefinition
//      QOpcUaGenericStructHandlerPrivate::structureDefinitionForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZNK33QOpcUaGenericStructHandlerPrivate28structureDefinitionForTypeIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QOpcUaStructureDefinition(
      self->structureDefinitionForTypeId(
          *id));
}

//  QOpcUaEnumDefinition
//      QOpcUaGenericStructHandlerPrivate::enumDefinitionForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZNK33QOpcUaGenericStructHandlerPrivate23enumDefinitionForTypeIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QOpcUaEnumDefinition(self->enumDefinitionForTypeId(*id));
}

//  QString
//      QOpcUaGenericStructHandlerPrivate::typeNameForBinaryEncodingId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QOpcUaGenericStructHandlerPrivate27typeNameForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QString(self->typeNameForBinaryEncodingId(*id));
}

//  QString QOpcUaGenericStructHandlerPrivate::typeNameForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QOpcUaGenericStructHandlerPrivate17typeNameForTypeIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QString(self->typeNameForTypeId(*id));
}

//  QOpcUaGenericStructHandler::DataTypeKind
//      QOpcUaGenericStructHandlerPrivate::dataTypeKindForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandler::DataTypeKind ritual_ZNK33QOpcUaGenericStructHandlerPrivate21dataTypeKindForTypeIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return self->dataTypeKindForTypeId(*id);
}

//  QString
//      QOpcUaGenericStructHandlerPrivate::typeIdForBinaryEncodingId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QOpcUaGenericStructHandlerPrivate25typeIdForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return new QString(self->typeIdForBinaryEncodingId(*id));
}

//  bool QOpcUaGenericStructHandlerPrivate::isAbstractTypeId(const QString
//      &id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QOpcUaGenericStructHandlerPrivate16isAbstractTypeIdERK7QString(
    const QOpcUaGenericStructHandlerPrivate *self,
    const QString *id) {
  return self->isAbstractTypeId(*id);
}

//  void QOpcUaGenericStructHandlerPrivate::handleFinished(bool success)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate14handleFinishedEb(
    QOpcUaGenericStructHandlerPrivate *self,
    bool success) {
  self->handleFinished(success);
}

//  bool QOpcUaGenericStructHandlerPrivate::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QOpcUaGenericStructHandlerPrivate11initializedEv(
    const QOpcUaGenericStructHandlerPrivate *self) {
  return self->initialized();
}

//  void QOpcUaGenericStructHandlerPrivate::processSubtypeOfKnownTypeRecursiv
//      e(QOpcUaInternalDataTypeNode *node, const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate34processSubtypeOfKnownTypeRecursiveEP26QOpcUaInternalDataTypeNodeRK7QString(
    QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaInternalDataTypeNode *node,
    const QString *id) {
  self->processSubtypeOfKnownTypeRecursive(node, *id);
}
