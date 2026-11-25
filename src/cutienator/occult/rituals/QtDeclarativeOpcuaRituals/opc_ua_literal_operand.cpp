//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcualiteraloperand_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'value', 'setValue',
//  'type' and 'setType', which are not virtual and are defined
//  outside the header; the signal 'dataChanged'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcualiteraloperand_p.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *OpcUaLiteralOperand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19OpcUaLiteralOperand10metaObjectEv(
    const OpcUaLiteralOperand *self) {
  return self->metaObject();
}

//  OpcUaLiteralOperand::~OpcUaLiteralOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN19OpcUaLiteralOperandD1Ev(OpcUaLiteralOperand *self) {
  delete self;
}

//  QVariant OpcUaLiteralOperand::toCppVariant(QOpcUaClient *client) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19OpcUaLiteralOperand12toCppVariantEP12QOpcUaClient(
    const OpcUaLiteralOperand *self,
    QOpcUaClient *client) {
  return new QVariant(self->toCppVariant(client));
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
