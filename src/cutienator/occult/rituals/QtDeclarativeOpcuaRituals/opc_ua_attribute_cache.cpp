//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuaattributecache_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'attribute',
//  'attributeValue' and the slots 'setAttributeValue' and
//  'invalidate', which are not virtual and are defined outside the
//  header.
//  Its destructor, which the class does not declare, is virtual, as
//  QObject's is, and is called through 'delete'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuaattributecache_p.h>

//  const QMetaObject *OpcUaAttributeCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19OpcUaAttributeCache10metaObjectEv(
    const OpcUaAttributeCache *self) {
  return self->metaObject();
}

//  OpcUaAttributeCache::~OpcUaAttributeCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN19OpcUaAttributeCacheD1Ev(OpcUaAttributeCache *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
