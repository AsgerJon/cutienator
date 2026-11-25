//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuanodeid_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; the signals.
//  Its destructor, which the class does not declare, is virtual, as
//  QObject's is, and is called through 'delete'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuanodeid_p.h>

//  const QMetaObject *OpcUaNodeId::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11OpcUaNodeId10metaObjectEv(
    const OpcUaNodeId *self) {
  return self->metaObject();
}

//  OpcUaNodeId::~OpcUaNodeId()
extern "C" Q_DECL_EXPORT
void ritual_ZN11OpcUaNodeIdD1Ev(OpcUaNodeId *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
