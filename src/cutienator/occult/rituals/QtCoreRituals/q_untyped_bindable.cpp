//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtCore/qproperty.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>

//  QUntypedBindable::QUntypedBindable(QUntypedPropertyData *d, const
//      QtPrivate::QBindableInterface *i)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC1EP20QUntypedPropertyDataPKN9QtPrivate18QBindableInterfaceE(
    QUntypedPropertyData *d,
    const QtPrivate::QBindableInterface *i) {
  return new QUntypedBindable(d, i);
}

//  QUntypedBindable::QUntypedBindable(QObject *obj, const QMetaProperty
//      &property, const QtPrivate::QBindableInterface *i)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC1EP7QObjectRK13QMetaPropertyPKN9QtPrivate18QBindableInterfaceE(
    QObject *obj,
    const QMetaProperty *property,
    const QtPrivate::QBindableInterface *i) {
  return new QUntypedBindable(obj, *property, i);
}

//  QUntypedBindable::QUntypedBindable(QObject *obj, const char *property,
//      const QtPrivate::QBindableInterface *i)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC1EP7QObjectPKcPKN9QtPrivate18QBindableInterfaceE(
    QObject *obj,
    const char *property,
    const QtPrivate::QBindableInterface *i) {
  return new QUntypedBindable(obj, property, i);
}

//  QUntypedBindable::QUntypedBindable()
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC1Ev() {
  return new QUntypedBindable();
}

//  bool QUntypedBindable::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QUntypedBindable7isValidEv(const QUntypedBindable *self) {
  return self->isValid();
}

//  bool QUntypedBindable::isBindable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QUntypedBindable10isBindableEv(
    const QUntypedBindable *self) {
  return self->isBindable();
}

//  bool QUntypedBindable::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QUntypedBindable10isReadOnlyEv(
    const QUntypedBindable *self) {
  return self->isReadOnly();
}

//  QUntypedPropertyBinding QUntypedBindable::makeBinding(const
//      QPropertyBindingSourceLocation &location) const
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZNK16QUntypedBindable11makeBindingERK30QPropertyBindingSourceLocation(
    const QUntypedBindable *self,
    const QPropertyBindingSourceLocation *location) {
  return new QUntypedPropertyBinding(self->makeBinding(*location));
}

//  QUntypedPropertyBinding QUntypedBindable::takeBinding()
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN16QUntypedBindable11takeBindingEv(
    QUntypedBindable *self) {
  return new QUntypedPropertyBinding(self->takeBinding());
}

//  void QUntypedBindable::observe(QPropertyObserver *observer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QUntypedBindable7observeEP17QPropertyObserver(
    const QUntypedBindable *self,
    QPropertyObserver *observer) {
  self->observe(observer);
}

//  QUntypedPropertyBinding QUntypedBindable::binding() const
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZNK16QUntypedBindable7bindingEv(
    const QUntypedBindable *self) {
  return new QUntypedPropertyBinding(self->binding());
}

//  bool QUntypedBindable::setBinding(const QUntypedPropertyBinding &binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QUntypedBindable10setBindingERK23QUntypedPropertyBinding(
    QUntypedBindable *self,
    const QUntypedPropertyBinding *binding) {
  return self->setBinding(*binding);
}

//  bool QUntypedBindable::hasBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QUntypedBindable10hasBindingEv(
    const QUntypedBindable *self) {
  return self->hasBinding();
}

//  QMetaType QUntypedBindable::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK16QUntypedBindable8metaTypeEv(
    const QUntypedBindable *self) {
  return new QMetaType(self->metaType());
}

//  QUntypedBindable::~QUntypedBindable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QUntypedBindableD1Ev(QUntypedBindable *self) {
  delete self;
}

//  QUntypedBindable::QUntypedBindable<QProperty<int>>(QProperty<int> *p)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC2I9QPropertyIiEEEPT_(
    QProperty<int> *p) {
  return new QUntypedBindable(p);
}

//  QUntypedBindable::QUntypedBindable<QProperty<double>>(
//      QProperty<double> *p)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC2I9QPropertyIdEEEPT_(
    QProperty<double> *p) {
  return new QUntypedBindable(p);
}

//  QUntypedBindable::QUntypedBindable<QProperty<bool>>(
//      QProperty<bool> *p)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC2I9QPropertyIbEEEPT_(
    QProperty<bool> *p) {
  return new QUntypedBindable(p);
}

//  QUntypedBindable::QUntypedBindable<QProperty<QString>>(
//      QProperty<QString> *p)
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZN16QUntypedBindableC2I9QPropertyI7QStringEEEPT_(
    QProperty<QString> *p) {
  return new QUntypedBindable(p);
}
