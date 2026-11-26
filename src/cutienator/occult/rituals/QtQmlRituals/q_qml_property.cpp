//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>

//  QQmlProperty::QQmlProperty()
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1Ev() {
  return new QQmlProperty();
}

//  QQmlProperty::~QQmlProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlPropertyD1Ev(QQmlProperty *self) {
  delete self;
}

//  QQmlProperty::QQmlProperty(QObject *a0)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObject(QObject *a0) {
  return new QQmlProperty(a0);
}

//  QQmlProperty::QQmlProperty(QObject *a0, QQmlContext *a1)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObjectP11QQmlContext(
    QObject *a0,
    QQmlContext *a1) {
  return new QQmlProperty(a0, a1);
}

//  QQmlProperty::QQmlProperty(QObject *a0, QQmlEngine *a1)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObjectP10QQmlEngine(
    QObject *a0,
    QQmlEngine *a1) {
  return new QQmlProperty(a0, a1);
}

//  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObjectRK7QString(
    QObject *a0,
    const QString *a1) {
  return new QQmlProperty(a0, *a1);
}

//  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1, QQmlContext
//      *a2)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObjectRK7QStringP11QQmlContext(
    QObject *a0,
    const QString *a1,
    QQmlContext *a2) {
  return new QQmlProperty(a0, *a1, a2);
}

//  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1, QQmlEngine
//      *a2)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EP7QObjectRK7QStringP10QQmlEngine(
    QObject *a0,
    const QString *a1,
    QQmlEngine *a2) {
  return new QQmlProperty(a0, *a1, a2);
}

//  QQmlProperty::QQmlProperty(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1ERKS_(const QQmlProperty *a0) {
  return new QQmlProperty(*a0);
}

//  QQmlProperty &QQmlProperty::operator=(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyaSERKS_(
    QQmlProperty *self,
    const QQmlProperty *a0) {
  return &(self->operator=(*a0));
}

//  QQmlProperty::QQmlProperty(QQmlProperty &&other)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyC1EOS_(QQmlProperty *other) {
  return new QQmlProperty(std::move(*other));
}

//  QQmlProperty &QQmlProperty::operator=(QQmlProperty &&other)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN12QQmlPropertyaSEOS_(
    QQmlProperty *self,
    QQmlProperty *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QQmlProperty::swap(QQmlProperty &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProperty4swapERS_(
    QQmlProperty *self,
    QQmlProperty *other) {
  self->swap(*other);
}

//  bool QQmlProperty::operator==(const QQmlProperty &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlPropertyeqERKS_(
    const QQmlProperty *self,
    const QQmlProperty *a0) {
  return self->operator==(*a0);
}

//  Type QQmlProperty::type() const
extern "C" Q_DECL_EXPORT
QQmlProperty::Type ritual_ZNK12QQmlProperty4typeEv(
    const QQmlProperty *self) {
  return self->type();
}

//  bool QQmlProperty::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty7isValidEv(const QQmlProperty *self) {
  return self->isValid();
}

//  bool QQmlProperty::isProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty10isPropertyEv(const QQmlProperty *self) {
  return self->isProperty();
}

//  bool QQmlProperty::isSignalProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty16isSignalPropertyEv(const QQmlProperty *self) {
  return self->isSignalProperty();
}

//  int QQmlProperty::propertyType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQmlProperty12propertyTypeEv(const QQmlProperty *self) {
  return self->propertyType();
}

//  QMetaType QQmlProperty::propertyMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK12QQmlProperty16propertyMetaTypeEv(
    const QQmlProperty *self) {
  return new QMetaType(self->propertyMetaType());
}

//  PropertyTypeCategory QQmlProperty::propertyTypeCategory() const
extern "C" Q_DECL_EXPORT
QQmlProperty::PropertyTypeCategory ritual_ZNK12QQmlProperty20propertyTypeCategoryEv(
    const QQmlProperty *self) {
  return self->propertyTypeCategory();
}

//  const char *QQmlProperty::propertyTypeName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK12QQmlProperty16propertyTypeNameEv(
    const QQmlProperty *self) {
  return self->propertyTypeName();
}

//  QString QQmlProperty::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlProperty4nameEv(const QQmlProperty *self) {
  return new QString(self->name());
}

//  QVariant QQmlProperty::read() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QQmlProperty4readEv(const QQmlProperty *self) {
  return new QVariant(self->read());
}

//  QVariant QQmlProperty::read(const QObject *a0, const QString &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QQmlProperty4readEPK7QObjectRK7QString(
    const QObject *a0,
    const QString *a1) {
  return new QVariant(QQmlProperty::read(a0, *a1));
}

//  QVariant QQmlProperty::read(const QObject *a0, const QString &a1,
//      QQmlContext *a2)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QQmlProperty4readEPK7QObjectRK7QStringP11QQmlContext(
    const QObject *a0,
    const QString *a1,
    QQmlContext *a2) {
  return new QVariant(QQmlProperty::read(a0, *a1, a2));
}

//  QVariant QQmlProperty::read(const QObject *a0, const QString &a1,
//      QQmlEngine *a2)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QQmlProperty4readEPK7QObjectRK7QStringP10QQmlEngine(
    const QObject *a0,
    const QString *a1,
    QQmlEngine *a2) {
  return new QVariant(QQmlProperty::read(a0, *a1, a2));
}

//  bool QQmlProperty::write(const QVariant &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty5writeERK8QVariant(
    const QQmlProperty *self,
    const QVariant *a0) {
  return self->write(*a0);
}

//  bool QQmlProperty::write(QObject *a0, const QString &a1, const QVariant
//      &a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariant(
    QObject *a0,
    const QString *a1,
    const QVariant *a2) {
  return QQmlProperty::write(a0, *a1, *a2);
}

//  bool QQmlProperty::write(QObject *a0, const QString &a1, const QVariant
//      &a2, QQmlContext *a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariantP11QQmlContext(
    QObject *a0,
    const QString *a1,
    const QVariant *a2,
    QQmlContext *a3) {
  return QQmlProperty::write(a0, *a1, *a2, a3);
}

//  bool QQmlProperty::write(QObject *a0, const QString &a1, const QVariant
//      &a2, QQmlEngine *a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariantP10QQmlEngine(
    QObject *a0,
    const QString *a1,
    const QVariant *a2,
    QQmlEngine *a3) {
  return QQmlProperty::write(a0, *a1, *a2, a3);
}

//  bool QQmlProperty::reset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty5resetEv(const QQmlProperty *self) {
  return self->reset();
}

//  bool QQmlProperty::hasNotifySignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty15hasNotifySignalEv(const QQmlProperty *self) {
  return self->hasNotifySignal();
}

//  bool QQmlProperty::needsNotifySignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty17needsNotifySignalEv(
    const QQmlProperty *self) {
  return self->needsNotifySignal();
}

//  bool QQmlProperty::connectNotifySignal(QObject *dest, const char *slot)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty19connectNotifySignalEP7QObjectPKc(
    const QQmlProperty *self,
    QObject *dest,
    const char *slot) {
  return self->connectNotifySignal(dest, slot);
}

//  bool QQmlProperty::connectNotifySignal(QObject *dest, int method) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty19connectNotifySignalEP7QObjecti(
    const QQmlProperty *self,
    QObject *dest,
    int method) {
  return self->connectNotifySignal(dest, method);
}

//  bool QQmlProperty::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty10isWritableEv(const QQmlProperty *self) {
  return self->isWritable();
}

//  bool QQmlProperty::isBindable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty10isBindableEv(const QQmlProperty *self) {
  return self->isBindable();
}

//  bool QQmlProperty::isDesignable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty12isDesignableEv(const QQmlProperty *self) {
  return self->isDesignable();
}

//  bool QQmlProperty::isResettable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProperty12isResettableEv(const QQmlProperty *self) {
  return self->isResettable();
}

//  QObject *QQmlProperty::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QQmlProperty6objectEv(const QQmlProperty *self) {
  return self->object();
}

//  int QQmlProperty::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQmlProperty5indexEv(const QQmlProperty *self) {
  return self->index();
}

//  QMetaProperty QQmlProperty::property() const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK12QQmlProperty8propertyEv(
    const QQmlProperty *self) {
  return new QMetaProperty(self->property());
}

//  QMetaMethod QQmlProperty::method() const
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZNK12QQmlProperty6methodEv(const QQmlProperty *self) {
  return new QMetaMethod(self->method());
}

//  QList<QQmlProperty>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlProperty> *ritual_list_make_QQmlProperty() {
  return new QList<QQmlProperty>();
}

//  void QList<QQmlProperty>::append(const QQmlProperty &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlProperty(
    QList<QQmlProperty> *self,
    const QQmlProperty *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlProperty>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlProperty(const QList<QQmlProperty> *self) {
  return self->size();
}

//  const QQmlProperty &QList<QQmlProperty>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_list_at_QQmlProperty(
    const QList<QQmlProperty> *self,
    long long index) {
  return new QQmlProperty(self->at(index));
}

//  QList<QQmlProperty>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlProperty(QList<QQmlProperty> *self) {
  delete self;
}
