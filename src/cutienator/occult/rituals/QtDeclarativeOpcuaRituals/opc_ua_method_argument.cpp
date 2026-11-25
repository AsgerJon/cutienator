//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuamethodargument_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'value', 'type' and the
//  slots 'setValue' and 'setType', which are not virtual and are
//  defined outside the header.
//  Its destructor, which the class does not declare, is virtual, as
//  QObject's is, and is called through 'delete'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuamethodargument_p.h>

//  const QMetaObject *OpcUaMethodArgument::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19OpcUaMethodArgument10metaObjectEv(
    const OpcUaMethodArgument *self) {
  return self->metaObject();
}

//  OpcUaMethodArgument::~OpcUaMethodArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN19OpcUaMethodArgumentD1Ev(OpcUaMethodArgument *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
