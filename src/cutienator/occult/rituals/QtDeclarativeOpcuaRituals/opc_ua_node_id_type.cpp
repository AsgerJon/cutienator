//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuanodeidtype_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; every other function of
//  the class, as none is virtual or defined in the header; the
//  signals.
//  Its destructor, which the class does not declare, is virtual, as
//  QObject's is, and is called through 'delete'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuanodeidtype_p.h>

//  const QMetaObject *OpcUaNodeIdType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15OpcUaNodeIdType10metaObjectEv(
    const OpcUaNodeIdType *self) {
  return self->metaObject();
}

//  OpcUaNodeIdType::~OpcUaNodeIdType()
extern "C" Q_DECL_EXPORT
void ritual_ZN15OpcUaNodeIdTypeD1Ev(OpcUaNodeIdType *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
