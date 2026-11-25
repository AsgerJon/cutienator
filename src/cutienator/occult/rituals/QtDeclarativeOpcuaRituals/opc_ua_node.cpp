//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuanode_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object.
//  Not written: the constructor, 'tr' and every function that is not
//  virtual, which Qt's library offers not.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuanode_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *OpcUaNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9OpcUaNode10metaObjectEv(
    const OpcUaNode *self) {
  return self->metaObject();
}

//  OpcUaNode::~OpcUaNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN9OpcUaNodeD1Ev(OpcUaNode *self) {
  delete self;
}

//  void OpcUaNode::setupNode(const QString &absoluteNodePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN9OpcUaNode9setupNodeERK7QString(
    OpcUaNode *self,
    const QString *absoluteNodePath) {
  self->setupNode(*absoluteNodePath);
}

//  bool OpcUaNode::checkValidity()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9OpcUaNode13checkValidityEv(OpcUaNode *self) {
  return self->checkValidity();
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
