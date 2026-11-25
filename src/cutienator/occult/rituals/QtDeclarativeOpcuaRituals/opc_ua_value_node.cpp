//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuavaluenode_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object.
//  Not written: the constructor, 'tr' and every function that is not
//  virtual, which Qt's library offers not.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuavaluenode_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *OpcUaValueNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14OpcUaValueNode10metaObjectEv(
    const OpcUaValueNode *self) {
  return self->metaObject();
}

//  OpcUaValueNode::~OpcUaValueNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN14OpcUaValueNodeD1Ev(OpcUaValueNode *self) {
  delete self;
}

//  void OpcUaValueNode::setupNode(const QString &absolutePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14OpcUaValueNode9setupNodeERK7QString(
    OpcUaValueNode *self,
    const QString *absolutePath) {
  self->setupNode(*absolutePath);
}

//  bool OpcUaValueNode::checkValidity()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14OpcUaValueNode13checkValidityEv(OpcUaValueNode *self) {
  return self->checkValidity();
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
