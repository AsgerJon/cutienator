//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuamethodnode_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Written as well: 'setupNode' and 'checkValidity', the class's
//  private overrides of virtual functions of OpcUaNode.
//  Not written: the constructor and 'tr'; every other function of
//  the class, slots included, as none is virtual or defined in the
//  header ('inputArguments' gives a 'QQmlListProperty', a
//  template, 'outputArguments' a QVariantList, a QList, and the
//  static functions take a QQmlListProperty); the signals.
//  Its destructor, which the class does not declare, is virtual, as
//  QObject's is, and is called through 'delete'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuamethodnode_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *OpcUaMethodNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15OpcUaMethodNode10metaObjectEv(
    const OpcUaMethodNode *self) {
  return self->metaObject();
}

//  OpcUaMethodNode::~OpcUaMethodNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15OpcUaMethodNodeD1Ev(OpcUaMethodNode *self) {
  delete self;
}

//  void OpcUaMethodNode::setupNode(const QString &absolutePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN15OpcUaMethodNode9setupNodeERK7QString(
    OpcUaMethodNode *self,
    const QString *absolutePath) {
  self->setupNode(*absolutePath);
}

//  bool OpcUaMethodNode::checkValidity()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15OpcUaMethodNode13checkValidityEv(OpcUaMethodNode *self) {
  return self->checkValidity();
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
