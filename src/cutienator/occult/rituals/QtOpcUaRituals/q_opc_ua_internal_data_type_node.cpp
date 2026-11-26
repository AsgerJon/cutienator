//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuainternaldatatypenode_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QOpcUaInternalDataTypeNode' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  4 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuainternaldatatypenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qloggingcategory.h>
#include <QtOpcUa/private/qopcuainternaldatatypenode_p.h>
#include <QtOpcUa/private/qopcuagenericstructhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtOpcUa__QOpcUaInternalDataTypeNode.cpp, line 1, as moc:QOpcUaInternalDataTypeNode
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t {};
} // unnamed namespace

template <> constexpr inline auto QOpcUaInternalDataTypeNode::qt_create_metaobjectdata<qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QOpcUaInternalDataTypeNode",
        "initializeFinished",
        "",
        "success"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'initializeFinished'
        QtMocHelpers::SignalData<void(bool)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 3 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QOpcUaInternalDataTypeNode, qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QOpcUaInternalDataTypeNode::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>.metaTypes,
    nullptr
} };

void QOpcUaInternalDataTypeNode::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QOpcUaInternalDataTypeNode *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->initializeFinished((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QOpcUaInternalDataTypeNode::*)(bool )>(_a, &QOpcUaInternalDataTypeNode::initializeFinished, 0))
            return;
    }
}

const QMetaObject *QOpcUaInternalDataTypeNode::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QOpcUaInternalDataTypeNode::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QOpcUaInternalDataTypeNodeE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QOpcUaInternalDataTypeNode::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QOpcUaInternalDataTypeNode::initializeFinished(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 28, as _Z22lcGenericStructHandlerv
inline const QLoggingCategory &lcGenericStructHandler()
{
    static const QLoggingCategory category("qt.opcuagenericstructhandler");
    return category;
}

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 10, as _ZN26QOpcUaInternalDataTypeNodeC1EP12QOpcUaClient
inline QOpcUaInternalDataTypeNode::QOpcUaInternalDataTypeNode(QOpcUaClient *client)
    : m_client(client)
{
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

//  from ../qtopcua/src/opcua/client/qopcuainternaldatatypenode.cpp, line 98, as _ZN26QOpcUaInternalDataTypeNode14handleFinishedEb
inline void QOpcUaInternalDataTypeNode::handleFinished(bool success)
{
    if (m_hasError)
        return;

    m_finishedCount++;
    m_hasError = !success;

    if (m_finishedCount == m_children.size() + 1 || m_hasError)
        emit initializeFinished(!m_hasError);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QOpcUaInternalDataTypeNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QOpcUaInternalDataTypeNode10metaObjectEv(
    const QOpcUaInternalDataTypeNode *self) {
  return self->metaObject();
}

//  void *QOpcUaInternalDataTypeNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QOpcUaInternalDataTypeNode11qt_metacastEPKc(
    QOpcUaInternalDataTypeNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaInternalDataTypeNode::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QOpcUaInternalDataTypeNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaInternalDataTypeNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaInternalDataTypeNode::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QOpcUaInternalDataTypeNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaInternalDataTypeNode::tr(s, c, n));
}

//  QOpcUaInternalDataTypeNode::QOpcUaInternalDataTypeNode(QOpcUaClient
//      *client)
extern "C" Q_DECL_EXPORT
QOpcUaInternalDataTypeNode *ritual_ZN26QOpcUaInternalDataTypeNodeC1EP12QOpcUaClient(
    QOpcUaClient *client) {
  return new QOpcUaInternalDataTypeNode(client);
}

//  bool QOpcUaInternalDataTypeNode::initialize(const QString &nodeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QOpcUaInternalDataTypeNode10initializeERK7QString(
    QOpcUaInternalDataTypeNode *self,
    const QString *nodeId) {
  return self->initialize(*nodeId);
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

//  const std::vector<std::unique_ptr<QOpcUaInternalDataTypeNode>>
//      &QOpcUaInternalDataTypeNode::children() const
extern "C" Q_DECL_EXPORT
const std::vector<std::unique_ptr<QOpcUaInternalDataTypeNode>> *ritual_ZNK26QOpcUaInternalDataTypeNode8childrenEv(
    const QOpcUaInternalDataTypeNode *self) {
  return &(self->children());
}

//  void QOpcUaInternalDataTypeNode::initializeFinished(bool success)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaInternalDataTypeNode18initializeFinishedEb(
    QOpcUaInternalDataTypeNode *self,
    bool success) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QOpcUaInternalDataTypeNode")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "initializeFinished(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "initializeFinished(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&success)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QOpcUaInternalDataTypeNode::handleFinished(bool success)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaInternalDataTypeNode14handleFinishedEb(
    QOpcUaInternalDataTypeNode *self,
    bool success) {
  self->handleFinished(success);
}
