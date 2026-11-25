//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuaendpointdiscovery_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Written as well: 'classBegin' and 'componentComplete', the
//  class's private overrides of QQmlParserStatus.
//  Not written: the constructor and 'tr'; every other function of
//  the class, slots included, as none is virtual or defined in the
//  header; the signals.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuaendpointdiscovery_p.h>

//  const QMetaObject *OpcUaEndpointDiscovery::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22OpcUaEndpointDiscovery10metaObjectEv(
    const OpcUaEndpointDiscovery *self) {
  return self->metaObject();
}

//  OpcUaEndpointDiscovery::~OpcUaEndpointDiscovery()
extern "C" Q_DECL_EXPORT
void ritual_ZN22OpcUaEndpointDiscoveryD1Ev(OpcUaEndpointDiscovery *self) {
  delete self;
}

//  void OpcUaEndpointDiscovery::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN22OpcUaEndpointDiscovery10classBeginEv(
    OpcUaEndpointDiscovery *self) {
  self->classBegin();
}

//  void OpcUaEndpointDiscovery::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22OpcUaEndpointDiscovery17componentCompleteEv(
    OpcUaEndpointDiscovery *self) {
  self->componentComplete();
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
