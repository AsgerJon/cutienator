//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuaelementoperand_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'index' and 'setIndex',
//  which are not virtual and are defined outside the header; the
//  signal 'dataChanged'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuaelementoperand_p.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *OpcUaElementOperand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19OpcUaElementOperand10metaObjectEv(
    const OpcUaElementOperand *self) {
  return self->metaObject();
}

//  OpcUaElementOperand::~OpcUaElementOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN19OpcUaElementOperandD1Ev(OpcUaElementOperand *self) {
  delete self;
}

//  QVariant OpcUaElementOperand::toCppVariant(QOpcUaClient *client) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19OpcUaElementOperand12toCppVariantEP12QOpcUaClient(
    const OpcUaElementOperand *self,
    QOpcUaClient *client) {
  return new QVariant(self->toCppVariant(client));
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
