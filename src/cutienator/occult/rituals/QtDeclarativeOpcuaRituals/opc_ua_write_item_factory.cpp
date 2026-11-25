//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuawriteitem_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object.
//  Not written: the constructor, 'tr' and 'create', which Qt's
//  library offers not.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuawriteitem_p.h>

//  const QMetaObject *OpcUaWriteItemFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21OpcUaWriteItemFactory10metaObjectEv(
    const OpcUaWriteItemFactory *self) {
  return self->metaObject();
}

//  OpcUaWriteItemFactory::~OpcUaWriteItemFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN21OpcUaWriteItemFactoryD1Ev(OpcUaWriteItemFactory *self) {
  delete self;
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
