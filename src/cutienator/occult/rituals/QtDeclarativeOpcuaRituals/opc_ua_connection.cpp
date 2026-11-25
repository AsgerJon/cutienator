//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuaconnection_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; every other function of
//  the class, slots included, as none is virtual or defined in the
//  header (and 'availableBackends', 'namespaces' and
//  'supportedSecurityPolicies' give a QStringList, a QList); the
//  signals.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuaconnection_p.h>

//  const QMetaObject *OpcUaConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15OpcUaConnection10metaObjectEv(
    const OpcUaConnection *self) {
  return self->metaObject();
}

//  OpcUaConnection::~OpcUaConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15OpcUaConnectionD1Ev(OpcUaConnection *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
