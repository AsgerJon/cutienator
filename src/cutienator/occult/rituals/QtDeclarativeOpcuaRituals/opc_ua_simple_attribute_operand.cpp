//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuasimpleattributeoperand_p.h, Qt 6.12.0, from Qt's source. Kept as it
//  is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object.
//  Not written: the constructor, 'tr' and every function that is not
//  virtual, which Qt's library offers not.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuasimpleattributeoperand_p.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuaclient.h>

//  const QMetaObject *OpcUaSimpleAttributeOperand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27OpcUaSimpleAttributeOperand10metaObjectEv(
    const OpcUaSimpleAttributeOperand *self) {
  return self->metaObject();
}

//  OpcUaSimpleAttributeOperand::~OpcUaSimpleAttributeOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN27OpcUaSimpleAttributeOperandD1Ev(
    OpcUaSimpleAttributeOperand *self) {
  delete self;
}

//  QVariant OpcUaSimpleAttributeOperand::toCppVariant(QOpcUaClient *client)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27OpcUaSimpleAttributeOperand12toCppVariantEP12QOpcUaClient(
    const OpcUaSimpleAttributeOperand *self,
    QOpcUaClient *client) {
  return new QVariant(self->toCppVariant(client));
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
