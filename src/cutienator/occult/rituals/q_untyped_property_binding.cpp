//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>
#include <QtCore/qmetatype.h>

//  QUntypedPropertyBinding::QUntypedPropertyBinding()
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN23QUntypedPropertyBindingC1Ev() {
  return new QUntypedPropertyBinding();
}

//  QUntypedPropertyBinding::QUntypedPropertyBinding(const
//      QUntypedPropertyBinding &other)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN23QUntypedPropertyBindingC1ERKS_(
    const QUntypedPropertyBinding *other) {
  return new QUntypedPropertyBinding(*other);
}

//  QUntypedPropertyBinding::~QUntypedPropertyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QUntypedPropertyBindingD1Ev(QUntypedPropertyBinding *self) {
  delete self;
}

//  bool QUntypedPropertyBinding::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QUntypedPropertyBinding6isNullEv(
    const QUntypedPropertyBinding *self) {
  return self->isNull();
}

//  QPropertyBindingError QUntypedPropertyBinding::error() const
extern "C" Q_DECL_EXPORT
QPropertyBindingError *ritual_ZNK23QUntypedPropertyBinding5errorEv(
    const QUntypedPropertyBinding *self) {
  return new QPropertyBindingError(self->error());
}

//  QMetaType QUntypedPropertyBinding::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK23QUntypedPropertyBinding13valueMetaTypeEv(
    const QUntypedPropertyBinding *self) {
  return new QMetaType(self->valueMetaType());
}
