//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qproperty.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QMetaProperty::QMetaProperty()
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZN13QMetaPropertyC1Ev() {
  return new QMetaProperty();
}

//  const char *QMetaProperty::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QMetaProperty4nameEv(const QMetaProperty *self) {
  return self->name();
}

//  const char *QMetaProperty::typeName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QMetaProperty8typeNameEv(const QMetaProperty *self) {
  return self->typeName();
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QVariant::Type QMetaProperty::type() const
extern "C" Q_DECL_EXPORT
QVariant::Type ritual_ZNK13QMetaProperty4typeEv(const QMetaProperty *self) {
  return self->type();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  int QMetaProperty::userType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty8userTypeEv(const QMetaProperty *self) {
  return self->userType();
}

//  int QMetaProperty::typeId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty6typeIdEv(const QMetaProperty *self) {
  return self->typeId();
}

//  QMetaType QMetaProperty::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK13QMetaProperty8metaTypeEv(const QMetaProperty *self) {
  return new QMetaType(self->metaType());
}

//  int QMetaProperty::propertyIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty13propertyIndexEv(const QMetaProperty *self) {
  return self->propertyIndex();
}

//  int QMetaProperty::relativePropertyIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty21relativePropertyIndexEv(
    const QMetaProperty *self) {
  return self->relativePropertyIndex();
}

//  bool QMetaProperty::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isReadableEv(const QMetaProperty *self) {
  return self->isReadable();
}

//  bool QMetaProperty::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isWritableEv(const QMetaProperty *self) {
  return self->isWritable();
}

//  bool QMetaProperty::isResettable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty12isResettableEv(const QMetaProperty *self) {
  return self->isResettable();
}

//  bool QMetaProperty::isDesignable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty12isDesignableEv(const QMetaProperty *self) {
  return self->isDesignable();
}

//  bool QMetaProperty::isScriptable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty12isScriptableEv(const QMetaProperty *self) {
  return self->isScriptable();
}

//  bool QMetaProperty::isStored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty8isStoredEv(const QMetaProperty *self) {
  return self->isStored();
}

//  bool QMetaProperty::isUser() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty6isUserEv(const QMetaProperty *self) {
  return self->isUser();
}

//  bool QMetaProperty::isConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isConstantEv(const QMetaProperty *self) {
  return self->isConstant();
}

//  bool QMetaProperty::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty7isFinalEv(const QMetaProperty *self) {
  return self->isFinal();
}

//  bool QMetaProperty::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty9isVirtualEv(const QMetaProperty *self) {
  return self->isVirtual();
}

//  bool QMetaProperty::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isOverrideEv(const QMetaProperty *self) {
  return self->isOverride();
}

//  bool QMetaProperty::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isRequiredEv(const QMetaProperty *self) {
  return self->isRequired();
}

//  bool QMetaProperty::isBindable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isBindableEv(const QMetaProperty *self) {
  return self->isBindable();
}

//  bool QMetaProperty::isFlagType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isFlagTypeEv(const QMetaProperty *self) {
  return self->isFlagType();
}

//  bool QMetaProperty::isEnumType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty10isEnumTypeEv(const QMetaProperty *self) {
  return self->isEnumType();
}

//  QMetaEnum QMetaProperty::enumerator() const
extern "C" Q_DECL_EXPORT
QMetaEnum *ritual_ZNK13QMetaProperty10enumeratorEv(
    const QMetaProperty *self) {
  return new QMetaEnum(self->enumerator());
}

//  bool QMetaProperty::hasNotifySignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty15hasNotifySignalEv(
    const QMetaProperty *self) {
  return self->hasNotifySignal();
}

//  QMetaMethod QMetaProperty::notifySignal() const
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZNK13QMetaProperty12notifySignalEv(
    const QMetaProperty *self) {
  return new QMetaMethod(self->notifySignal());
}

//  int QMetaProperty::notifySignalIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty17notifySignalIndexEv(
    const QMetaProperty *self) {
  return self->notifySignalIndex();
}

//  int QMetaProperty::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty8revisionEv(const QMetaProperty *self) {
  return self->revision();
}

//  QVariant QMetaProperty::read(const QObject *obj) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QMetaProperty4readEPK7QObject(
    const QMetaProperty *self,
    const QObject *obj) {
  return new QVariant(self->read(obj));
}

//  bool QMetaProperty::write(QObject *obj, const QVariant &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty5writeEP7QObjectRK8QVariant(
    const QMetaProperty *self,
    QObject *obj,
    const QVariant *value) {
  return self->write(obj, *value);
}

//  bool QMetaProperty::reset(QObject *obj) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty5resetEP7QObject(
    const QMetaProperty *self,
    QObject *obj) {
  return self->reset(obj);
}

//  QUntypedBindable QMetaProperty::bindable(QObject *object) const
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZNK13QMetaProperty8bindableEP7QObject(
    const QMetaProperty *self,
    QObject *object) {
  return new QUntypedBindable(self->bindable(object));
}

//  bool QMetaProperty::hasStdCppSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty12hasStdCppSetEv(const QMetaProperty *self) {
  return self->hasStdCppSet();
}

//  bool QMetaProperty::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty7isAliasEv(const QMetaProperty *self) {
  return self->isAlias();
}

//  bool QMetaProperty::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaProperty7isValidEv(const QMetaProperty *self) {
  return self->isValid();
}

//  const QMetaObject *QMetaProperty::enclosingMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QMetaProperty19enclosingMetaObjectEv(
    const QMetaProperty *self) {
  return self->enclosingMetaObject();
}

#if QT_DEPRECATED_SINCE(6, 4)
//  int QMetaProperty::registerPropertyType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMetaProperty20registerPropertyTypeEv(
    const QMetaProperty *self) {
  return self->registerPropertyType();
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  QMetaProperty::QMetaProperty(const QMetaObject *mobj, int index)
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZN13QMetaPropertyC1EPK11QMetaObjecti(
    const QMetaObject *mobj,
    int index) {
  return new QMetaProperty(mobj, index);
}

//  QMetaProperty::~QMetaProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMetaPropertyD1Ev(QMetaProperty *self) {
  delete self;
}

//  QHash<int, QMetaProperty>: QHash<int, QMetaProperty>()
extern "C" Q_DECL_EXPORT
QHash<int, QMetaProperty> *ritual_map_make_QHash_int_QMetaProperty() {
  return new QHash<int, QMetaProperty>();
}

//  QHash<int, QMetaProperty>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_int_QMetaProperty(
    QHash<int, QMetaProperty> *self,
    int key,
    const QMetaProperty *value) {
  self->insert(key, *value);
}

//  QHash<int, QMetaProperty>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_int_QMetaProperty(
    const QHash<int, QMetaProperty> *self) {
  return self->size();
}

//  QHash<int, QMetaProperty>: the key at a place
extern "C" Q_DECL_EXPORT
int ritual_map_key_QHash_int_QMetaProperty(
    const QHash<int, QMetaProperty> *self,
    long long index) {
  return *std::next(self->keyBegin(), index);
}

//  QHash<int, QMetaProperty>: the value at a place
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_map_value_QHash_int_QMetaProperty(
    const QHash<int, QMetaProperty> *self,
    long long index) {
  return new QMetaProperty(*std::next(self->constBegin(), index));
}

//  QHash<int, QMetaProperty>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_int_QMetaProperty(
    const QHash<int, QMetaProperty> *self,
    int key) {
  return self->contains(key);
}

//  QHash<int, QMetaProperty>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_map_get_QHash_int_QMetaProperty(
    const QHash<int, QMetaProperty> *self,
    int key) {
  return new QMetaProperty(self->value(key));
}

//  QHash<int, QMetaProperty>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_int_QMetaProperty(
    QHash<int, QMetaProperty> *self) {
  delete self;
}
