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

//  from ../qtopcua/src/opcua/client/qopcuagenericstructhandlerprivate.cpp, line 28, as _Z22lcGenericStructHandlerv
inline const QLoggingCategory &lcGenericStructHandler()
{
    static const QLoggingCategory category("qt.opcuagenericstructhandler");
    return category;
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
