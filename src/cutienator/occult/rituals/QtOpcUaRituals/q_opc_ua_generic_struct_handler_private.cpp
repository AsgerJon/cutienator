//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuagenericstructhandler_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 10. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuagenericstructhandler.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuagenericstructhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuagenericstructvalue.h>
#include <QtOpcUa/qopcuastructuredefinition.h>
#include <QtOpcUa/qopcuaenumdefinition.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtOpcUa/private/qopcuainternaldatatypenode_p.h>
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
#include <QtOpcUa/qopcuarange.h>
#include <QtOpcUa/qopcuastructurefield.h>
#include <QtOpcUa/qopcuaxvalue.h>
#include <QtCore/quuid.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 28, as _Z22lcGenericStructHandlerv
inline const QLoggingCategory &lcGenericStructHandler()
{
    static const QLoggingCategory category("qt.opcuagenericstructhandler");
    return category;
}

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 15, as _ZN26QOpcUaInternalDataTypeNode10initializeERK7QString
inline bool QOpcUaInternalDataTypeNode::initialize(const QString &nodeId)
{
    if (!m_client)
        return false;

    m_nodeId = nodeId;

    m_node.reset(m_client->node(nodeId));

    if (!m_node)
        return false;

    QObject::connect(m_node.get(), &QOpcUaNode::browseFinished, this,
                     [this](const QList<QOpcUaReferenceDescription> &results, QOpcUa::UaStatusCode result) {
                         Q_UNUSED(result);

                         for (const auto &entry : results) {
                             auto child = new QOpcUaInternalDataTypeNode(m_client);
                             const auto success = child->initialize(entry.targetNodeId().nodeId());

                             if (!success) {
                                 child->deleteLater();
                                 handleFinished(false);
                                 qCWarning(lcGenericStructHandler) << "Failed to init child" << entry.browseName().name();
                                 return;
                             }

                             m_children.push_back(std::unique_ptr<QOpcUaInternalDataTypeNode>(child));

                             QObject::connect(child, &QOpcUaInternalDataTypeNode::initializeFinished, this, &QOpcUaInternalDataTypeNode::handleFinished);
                         }

                         const auto success = m_node->readAttributes(QOpcUa::NodeAttribute::IsAbstract |
                                                                     QOpcUa::NodeAttribute::DataTypeDefinition |
                                                                     QOpcUa::NodeAttribute::BrowseName);

                         if (!success) {
                             qCWarning(lcGenericStructHandler) << "Failed to read attributes for" << m_node->nodeId();
                             handleFinished(false);
                         }
                     });

    QObject::connect(m_node.get(), &QOpcUaNode::attributeRead, this, [this]() {
        m_isAbstract = m_node->attribute(QOpcUa::NodeAttribute::IsAbstract).toBool();
        m_definition = m_node->attribute(QOpcUa::NodeAttribute::DataTypeDefinition);
        m_name = m_node->attribute(QOpcUa::NodeAttribute::BrowseName).value<QOpcUaQualifiedName>().name();
        handleFinished(true);
    });

    const auto success = m_node->browseChildren(QOpcUa::ReferenceTypeId::HasSubtype, QOpcUa::NodeClass::DataType);
    if (!success) {
        qCWarning(lcGenericStructHandler) << "Failed to start browse for" << m_node->nodeId();
        handleFinished(false);
    }

    return success;
}

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

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 86, as _ZN33QOpcUaGenericStructHandlerPrivate33createGenericStructValueForTypeIdERK7QString
inline QOpcUaGenericStructValue QOpcUaGenericStructHandlerPrivate::createGenericStructValueForTypeId(const QString &typeId)
{
    const auto entry = m_structuresByTypeId.constFind(typeId);

    if (entry != m_structuresByTypeId.constEnd()) {
        QOpcUaGenericStructValue value(entry.value().name, typeId, entry.value().structureDefinition);

        if (entry.value().structureDefinition.structureType() != QOpcUaStructureDefinition::StructureType::Union) {
            const auto tempFields = entry.value().structureDefinition.fields();
            for (const auto &field : tempFields) {
                if (field.isOptional())
                    continue;

                value.fieldsRef().insert(field.name(), QVariant());
            }
        }

        return value;
    }

    qCWarning(lcGenericStructHandler) << "Unable to create a pre-filled generic struct value for" << typeId;
    return {};
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

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 770, as _ZN33QOpcUaGenericStructHandlerPrivate28addCustomStructureDefinitionERK25QOpcUaStructureDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE
inline bool QOpcUaGenericStructHandlerPrivate::addCustomStructureDefinition(const QOpcUaStructureDefinition &definition,
                                                                     const QString &typeId, const QString &name, QOpcUa::IsAbstract isAbstract)
{
    if (typeId.isEmpty()) {
        qCWarning(lcGenericStructHandler) << "Failed to add custom structure definition, typeId must not be empty";
        return false;
    }

    if (name.isEmpty()) {
        qCWarning(lcGenericStructHandler) << "Failed to add custom structure definition, name must not be empty";
        return false;
    }

    if (definition.defaultEncodingId().isEmpty()) {
        qCWarning(lcGenericStructHandler) << "Failed to add custom structure definition, definition.defaultEncodingId() must not be empty";
        return false;
    }

    StructMapEntry entry;
    entry.isAbstract = isAbstract == QOpcUa::IsAbstract::Abstract;
    entry.name = name;
    entry.nodeId = typeId;
    entry.structureDefinition = definition;

    m_structuresByTypeId[typeId] = entry;
    m_structuresByEncodingId[definition.defaultEncodingId()] = entry;
    m_typeNamesByEncodingId[definition.defaultEncodingId()] = name;
    m_typeNamesByTypeId[typeId] = name;

    if (entry.isAbstract)
        m_abstractTypeIds.insert(typeId);

    return true;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 805, as _ZN33QOpcUaGenericStructHandlerPrivate23addCustomEnumDefinitionERK20QOpcUaEnumDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE
inline bool QOpcUaGenericStructHandlerPrivate::addCustomEnumDefinition(const QOpcUaEnumDefinition &definition,
                                                                const QString &typeId, const QString &name,
                                                                QOpcUa::IsAbstract isAbstract)
{
    if (typeId.isEmpty()) {
        qCWarning(lcGenericStructHandler) << "Failed to add custom enum definition, typeId must not be empty";
        return false;
    }

    if (name.isEmpty()) {
        qCWarning(lcGenericStructHandler) << "Failed to add custom enum definition, name must not be empty";
        return false;
    }

    EnumMapEntry entry;
    entry.isAbstract = isAbstract == QOpcUa::IsAbstract::Abstract;
    entry.name = name;
    entry.nodeId = typeId;
    entry.enumDefinition = definition;

    m_enumsByTypeId[typeId] = entry;
    m_typeNamesByTypeId[typeId] = name;

    return true;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 831, as _ZNK33QOpcUaGenericStructHandlerPrivate11initializedEv
inline bool QOpcUaGenericStructHandlerPrivate::initialized() const
{
    return m_initialized;
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 836, as _ZN33QOpcUaGenericStructHandlerPrivate24handleInitializeFinishedEb
inline void QOpcUaGenericStructHandlerPrivate::handleInitializeFinished(bool success)
{
    if (!success) {
        qCWarning(lcGenericStructHandler) << "Failed to read the data type tree";
        handleFinished(false);
        return;
    } else {
        processDataTypeRecursive(m_baseDataType.get());
        handleFinished(true);
    }
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 848, as _ZN33QOpcUaGenericStructHandlerPrivate24processDataTypeRecursiveEP26QOpcUaInternalDataTypeNode
inline void QOpcUaGenericStructHandlerPrivate::processDataTypeRecursive(QOpcUaInternalDataTypeNode *node)
{
    qCDebug(lcGenericStructHandler) << "Found DataType:" << node->name();

    m_typeNamesByTypeId[node->nodeId()] = node->name();
    if (node->isAbstract())
        m_abstractTypeIds.insert(node->nodeId());

    for (const auto &child : node->children()) {
        if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Structure))
            processStructRecursive(child.get());
        else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Enumeration))
            processEnumRecursive(child.get());
        else {
            if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Boolean))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Int32))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::UInt32))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Double))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Float))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::String))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::LocalizedText))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::DateTime))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::UInt16))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Int16))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::UInt64))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Int64))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Byte))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::SByte))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::ByteString))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::XmlElement))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::NodeId))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::Guid))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::QualifiedName))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else if (child->nodeId() == QOpcUa::namespace0Id(QOpcUa::NodeIds::Namespace0::StatusCode))
                processSubtypeOfKnownTypeRecursive(child.get(), child->nodeId());
            else
                processDataTypeRecursive(child.get());
        }
    }
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 908, as _ZN33QOpcUaGenericStructHandlerPrivate22processStructRecursiveEP26QOpcUaInternalDataTypeNode
inline void QOpcUaGenericStructHandlerPrivate::processStructRecursive(QOpcUaInternalDataTypeNode *node)
{
    qCDebug(lcGenericStructHandler) << "Found struct:" << node->name();

    m_typeNamesByTypeId.insert(node->nodeId(), node->name());

    if (node->isAbstract())
        m_abstractTypeIds.insert(node->nodeId());

    const auto structureDefinition = node->definition().value<QOpcUaStructureDefinition>();
    if (!structureDefinition.defaultEncodingId().isEmpty())
        m_typeNamesByEncodingId.insert(structureDefinition.defaultEncodingId(), node->name());

    const StructMapEntry entry{ node->name(), node->nodeId(), node->isAbstract(), structureDefinition };
    m_structuresByEncodingId.insert(structureDefinition.defaultEncodingId(), entry);
    m_structuresByTypeId.insert(node->nodeId(), entry);

    for (const auto &child : node->children())
        processStructRecursive(child.get());
}

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 929, as _ZN33QOpcUaGenericStructHandlerPrivate20processEnumRecursiveEP26QOpcUaInternalDataTypeNode
inline void QOpcUaGenericStructHandlerPrivate::processEnumRecursive(QOpcUaInternalDataTypeNode *node)
{
    qCDebug(lcGenericStructHandler) << "Found enum:" << node->name();

    m_typeNamesByTypeId[node->nodeId()] = node->name();

    if (node->isAbstract())
        m_abstractTypeIds.insert(node->nodeId());

    EnumMapEntry entry;
    entry.name = node->name();
    entry.enumDefinition = node->definition().value<QOpcUaEnumDefinition>();
    entry.nodeId = node->nodeId();
    entry.isAbstract = node->isAbstract();
    m_enumsByTypeId.insert(node->nodeId(), entry);

    for (const auto &child : node->children())
        processEnumRecursive(child.get());
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

//  QOpcUaGenericStructValue QOpcUaGenericStructHandlerPrivate::createGeneric
//      StructValueForTypeId(const QString &typeId)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN33QOpcUaGenericStructHandlerPrivate33createGenericStructValueForTypeIdERK7QString(
    QOpcUaGenericStructHandlerPrivate *self,
    const QString *typeId) {
  return new QOpcUaGenericStructValue(
      self->createGenericStructValueForTypeId(
          *typeId));
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

//  bool
//      QOpcUaGenericStructHandlerPrivate::addCustomStructureDefinition(const
//      QOpcUaStructureDefinition &definition, const QString &typeId, const
//      QString &name, QOpcUa::IsAbstract isAbstract)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate28addCustomStructureDefinitionERK25QOpcUaStructureDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE(
    QOpcUaGenericStructHandlerPrivate *self,
    const QOpcUaStructureDefinition *definition,
    const QString *typeId,
    const QString *name,
    QOpcUa::IsAbstract isAbstract) {
  return self->addCustomStructureDefinition(
      *definition,
      *typeId,
      *name,
      isAbstract);
}

//  bool QOpcUaGenericStructHandlerPrivate::addCustomEnumDefinition(const
//      QOpcUaEnumDefinition &definition, const QString &typeId, const
//      QString &name, QOpcUa::IsAbstract isAbstract)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate23addCustomEnumDefinitionERK20QOpcUaEnumDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE(
    QOpcUaGenericStructHandlerPrivate *self,
    const QOpcUaEnumDefinition *definition,
    const QString *typeId,
    const QString *name,
    QOpcUa::IsAbstract isAbstract) {
  return self->addCustomEnumDefinition(
      *definition,
      *typeId,
      *name,
      isAbstract);
}

//  bool QOpcUaGenericStructHandlerPrivate::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QOpcUaGenericStructHandlerPrivate11initializedEv(
    const QOpcUaGenericStructHandlerPrivate *self) {
  return self->initialized();
}

//  void QOpcUaGenericStructHandlerPrivate::handleInitializeFinished(bool
//      success)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate24handleInitializeFinishedEb(
    QOpcUaGenericStructHandlerPrivate *self,
    bool success) {
  self->handleInitializeFinished(success);
}

//  void QOpcUaGenericStructHandlerPrivate::processDataTypeRecursive(QOpcUaIn
//      ternalDataTypeNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate24processDataTypeRecursiveEP26QOpcUaInternalDataTypeNode(
    QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaInternalDataTypeNode *node) {
  self->processDataTypeRecursive(node);
}

//  void QOpcUaGenericStructHandlerPrivate::processStructRecursive(QOpcUaInte
//      rnalDataTypeNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate22processStructRecursiveEP26QOpcUaInternalDataTypeNode(
    QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaInternalDataTypeNode *node) {
  self->processStructRecursive(node);
}

//  void QOpcUaGenericStructHandlerPrivate::processEnumRecursive(QOpcUaIntern
//      alDataTypeNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOpcUaGenericStructHandlerPrivate20processEnumRecursiveEP26QOpcUaInternalDataTypeNode(
    QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaInternalDataTypeNode *node) {
  self->processEnumRecursive(node);
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

//  QVariant QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar<int>(
//          QOpcUaBinaryDataEncoding &decoder, qint32 valueRank,
//          bool &success) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QOpcUaGenericStructHandlerPrivate19decodeArrayOrScalarIiLN6QOpcUa5TypesE4294967295EEE8QVariantR24QOpcUaBinaryDataEncodingiRb(const QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *decoder, int valueRank, bool *success) {
  return new QVariant(self->decodeArrayOrScalar<int>(
      *decoder, valueRank, *success));
}

//  QVariant QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar<double>(
//          QOpcUaBinaryDataEncoding &decoder, qint32 valueRank,
//          bool &success) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QOpcUaGenericStructHandlerPrivate19decodeArrayOrScalarIdLN6QOpcUa5TypesE4294967295EEE8QVariantR24QOpcUaBinaryDataEncodingiRb(const QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *decoder, int valueRank, bool *success) {
  return new QVariant(self->decodeArrayOrScalar<double>(
      *decoder, valueRank, *success));
}

//  QVariant QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar<bool>(
//          QOpcUaBinaryDataEncoding &decoder, qint32 valueRank,
//          bool &success) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QOpcUaGenericStructHandlerPrivate19decodeArrayOrScalarIbLN6QOpcUa5TypesE4294967295EEE8QVariantR24QOpcUaBinaryDataEncodingiRb(const QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *decoder, int valueRank, bool *success) {
  return new QVariant(self->decodeArrayOrScalar<bool>(
      *decoder, valueRank, *success));
}

//  QVariant QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar<QString>(
//          QOpcUaBinaryDataEncoding &decoder, qint32 valueRank,
//          bool &success) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QOpcUaGenericStructHandlerPrivate19decodeArrayOrScalarI7QStringLN6QOpcUa5TypesE4294967295EEE8QVariantR24QOpcUaBinaryDataEncodingiRb(const QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *decoder, int valueRank, bool *success) {
  return new QVariant(self->decodeArrayOrScalar<QString>(
      *decoder, valueRank, *success));
}

//  QVariant QOpcUaGenericStructHandlerPrivate::decodeArrayOrScalar<QByteArray>(
//          QOpcUaBinaryDataEncoding &decoder, qint32 valueRank,
//          bool &success) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QOpcUaGenericStructHandlerPrivate19decodeArrayOrScalarI10QByteArrayLN6QOpcUa5TypesE4294967295EEE8QVariantR24QOpcUaBinaryDataEncodingiRb(const QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *decoder, int valueRank, bool *success) {
  return new QVariant(self->decodeArrayOrScalar<QByteArray>(
      *decoder, valueRank, *success));
}

//  bool QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar<int>(
//          QOpcUaBinaryDataEncoding &encoder, qint32 valueRank,
//          const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate19encodeArrayOrScalarIiLN6QOpcUa5TypesE4294967295EEEbR24QOpcUaBinaryDataEncodingiRK8QVariant(QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *encoder, int valueRank,
    const QVariant *value) {
  return self->encodeArrayOrScalar<int>(
      *encoder, valueRank, *value);
}

//  bool QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar<double>(
//          QOpcUaBinaryDataEncoding &encoder, qint32 valueRank,
//          const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate19encodeArrayOrScalarIdLN6QOpcUa5TypesE4294967295EEEbR24QOpcUaBinaryDataEncodingiRK8QVariant(QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *encoder, int valueRank,
    const QVariant *value) {
  return self->encodeArrayOrScalar<double>(
      *encoder, valueRank, *value);
}

//  bool QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar<bool>(
//          QOpcUaBinaryDataEncoding &encoder, qint32 valueRank,
//          const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate19encodeArrayOrScalarIbLN6QOpcUa5TypesE4294967295EEEbR24QOpcUaBinaryDataEncodingiRK8QVariant(QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *encoder, int valueRank,
    const QVariant *value) {
  return self->encodeArrayOrScalar<bool>(
      *encoder, valueRank, *value);
}

//  bool QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar<QString>(
//          QOpcUaBinaryDataEncoding &encoder, qint32 valueRank,
//          const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate19encodeArrayOrScalarI7QStringLN6QOpcUa5TypesE4294967295EEEbR24QOpcUaBinaryDataEncodingiRK8QVariant(QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *encoder, int valueRank,
    const QVariant *value) {
  return self->encodeArrayOrScalar<QString>(
      *encoder, valueRank, *value);
}

//  bool QOpcUaGenericStructHandlerPrivate::encodeArrayOrScalar<QByteArray>(
//          QOpcUaBinaryDataEncoding &encoder, qint32 valueRank,
//          const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QOpcUaGenericStructHandlerPrivate19encodeArrayOrScalarI10QByteArrayLN6QOpcUa5TypesE4294967295EEEbR24QOpcUaBinaryDataEncodingiRK8QVariant(QOpcUaGenericStructHandlerPrivate *self,
    QOpcUaBinaryDataEncoding *encoder, int valueRank,
    const QVariant *value) {
  return self->encodeArrayOrScalar<QByteArray>(
      *encoder, valueRank, *value);
}
