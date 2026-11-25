//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/
//  opcuaattributeoperand_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; every other function of
//  the class but 'toCppVariant', as none is virtual or defined in
//  the header ('browsePath' gives a 'QQmlListProperty', a template,
//  and the static functions take one); the signal
//  'dataChanged'.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/opcuaattributeoperand_p.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *OpcUaAttributeOperand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21OpcUaAttributeOperand10metaObjectEv(
    const OpcUaAttributeOperand *self) {
  return self->metaObject();
}

//  OpcUaAttributeOperand::~OpcUaAttributeOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN21OpcUaAttributeOperandD1Ev(OpcUaAttributeOperand *self) {
  delete self;
}

//  QVariant OpcUaAttributeOperand::toCppVariant(QOpcUaClient *client) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21OpcUaAttributeOperand12toCppVariantEP12QOpcUaClient(
    const OpcUaAttributeOperand *self,
    QOpcUaClient *client) {
  return new QVariant(self->toCppVariant(client));
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
