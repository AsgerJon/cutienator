//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltype_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QQmlType::QQmlType()
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN8QQmlTypeC1Ev() {
  return new QQmlType();
}

//  QQmlType::QQmlType(const QQmlType &other)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN8QQmlTypeC1ERKS_(const QQmlType *other) {
  return new QQmlType(*other);
}

//  QQmlType::QQmlType(const QQmlTypePrivate *priv)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN8QQmlTypeC1EPK15QQmlTypePrivate(
    const QQmlTypePrivate *priv) {
  return new QQmlType(priv);
}

//  QQmlType::~QQmlType()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlTypeD1Ev(QQmlType *self) {
  delete self;
}

//  bool QQmlType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType7isValidEv(const QQmlType *self) {
  return self->isValid();
}

//  QByteArray QQmlType::typeName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QQmlType8typeNameEv(const QQmlType *self) {
  return new QByteArray(self->typeName());
}

//  QString QQmlType::qmlTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlType11qmlTypeNameEv(const QQmlType *self) {
  return new QString(self->qmlTypeName());
}

//  QString QQmlType::elementName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlType11elementNameEv(const QQmlType *self) {
  return new QString(self->elementName());
}

//  QHashedString QQmlType::module() const
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZNK8QQmlType6moduleEv(const QQmlType *self) {
  return new QHashedString(self->module());
}

//  QTypeRevision QQmlType::version() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK8QQmlType7versionEv(const QQmlType *self) {
  return new QTypeRevision(self->version());
}

//  bool QQmlType::availableInVersion(QTypeRevision version) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType18availableInVersionE13QTypeRevision(
    const QQmlType *self,
    const QTypeRevision *version) {
  return self->availableInVersion(*version);
}

//  bool QQmlType::availableInVersion(const QHashedStringRef &module,
//      QTypeRevision version) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType18availableInVersionERK16QHashedStringRef13QTypeRevision(
    const QQmlType *self,
    const QHashedStringRef *module,
    const QTypeRevision *version) {
  return self->availableInVersion(*module, *version);
}

//  bool QQmlType::canConstructValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType21canConstructValueTypeEv(const QQmlType *self) {
  return self->canConstructValueType();
}

//  bool QQmlType::canPopulateValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType20canPopulateValueTypeEv(const QQmlType *self) {
  return self->canPopulateValueType();
}

//  QObject *QQmlType::create() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QQmlType6createEv(const QQmlType *self) {
  return self->create();
}

//  QObject *QQmlType::createWithQQmlData() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QQmlType18createWithQQmlDataEv(const QQmlType *self) {
  return self->createWithQQmlData();
}

//  QQmlCustomParser *QQmlType::customParser() const
extern "C" Q_DECL_EXPORT
QQmlCustomParser *ritual_ZNK8QQmlType12customParserEv(const QQmlType *self) {
  return self->customParser();
}

//  bool QQmlType::isCreatable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType11isCreatableEv(const QQmlType *self) {
  return self->isCreatable();
}

//  const QMetaObject *QQmlType::extensionMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlType19extensionMetaObjectEv(
    const QQmlType *self) {
  return self->extensionMetaObject();
}

//  bool QQmlType::isExtendedType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType14isExtendedTypeEv(const QQmlType *self) {
  return self->isExtendedType();
}

//  QString QQmlType::noCreationReason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlType16noCreationReasonEv(const QQmlType *self) {
  return new QString(self->noCreationReason());
}

//  bool QQmlType::isSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType11isSingletonEv(const QQmlType *self) {
  return self->isSingleton();
}

//  bool QQmlType::isInterface() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType11isInterfaceEv(const QQmlType *self) {
  return self->isInterface();
}

//  bool QQmlType::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType11isCompositeEv(const QQmlType *self) {
  return self->isComposite();
}

//  bool QQmlType::isCompositeSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType20isCompositeSingletonEv(const QQmlType *self) {
  return self->isCompositeSingleton();
}

//  bool QQmlType::isQObjectSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType18isQObjectSingletonEv(const QQmlType *self) {
  return self->isQObjectSingleton();
}

//  bool QQmlType::isQJSValueSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType19isQJSValueSingletonEv(const QQmlType *self) {
  return self->isQJSValueSingleton();
}

//  bool QQmlType::isSequentialContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType21isSequentialContainerEv(const QQmlType *self) {
  return self->isSequentialContainer();
}

//  bool QQmlType::isValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType11isValueTypeEv(const QQmlType *self) {
  return self->isValueType();
}

//  QMetaType QQmlType::typeId() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK8QQmlType6typeIdEv(const QQmlType *self) {
  return new QMetaType(self->typeId());
}

//  QMetaType QQmlType::qListTypeId() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK8QQmlType11qListTypeIdEv(const QQmlType *self) {
  return new QMetaType(self->qListTypeId());
}

//  QMetaSequence QQmlType::listMetaSequence() const
extern "C" Q_DECL_EXPORT
QMetaSequence *ritual_ZNK8QQmlType16listMetaSequenceEv(
    const QQmlType *self) {
  return new QMetaSequence(self->listMetaSequence());
}

//  const QMetaObject *QQmlType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlType10metaObjectEv(const QQmlType *self) {
  return self->metaObject();
}

//  const QMetaObject *QQmlType::metaObjectForValueType() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlType22metaObjectForValueTypeEv(
    const QQmlType *self) {
  return self->metaObjectForValueType();
}

//  const QMetaObject *QQmlType::baseMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlType14baseMetaObjectEv(
    const QQmlType *self) {
  return self->baseMetaObject();
}

//  QTypeRevision QQmlType::metaObjectRevision() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK8QQmlType18metaObjectRevisionEv(
    const QQmlType *self) {
  return new QTypeRevision(self->metaObjectRevision());
}

//  bool QQmlType::containsRevisionedAttributes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType28containsRevisionedAttributesEv(
    const QQmlType *self) {
  return self->containsRevisionedAttributes();
}

//  const QMetaObject *QQmlType::attachedPropertiesType(QQmlTypeLoader
//      *typeLoader) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlType22attachedPropertiesTypeEP14QQmlTypeLoader(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader) {
  return self->attachedPropertiesType(typeLoader);
}

//  int QQmlType::parserStatusCast() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType16parserStatusCastEv(const QQmlType *self) {
  return self->parserStatusCast();
}

//  const char *QQmlType::interfaceIId() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK8QQmlType12interfaceIIdEv(const QQmlType *self) {
  return self->interfaceIId();
}

//  int QQmlType::propertyValueSourceCast() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType23propertyValueSourceCastEv(const QQmlType *self) {
  return self->propertyValueSourceCast();
}

//  int QQmlType::propertyValueInterceptorCast() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType28propertyValueInterceptorCastEv(
    const QQmlType *self) {
  return self->propertyValueInterceptorCast();
}

//  int QQmlType::finalizerCast() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType13finalizerCastEv(const QQmlType *self) {
  return self->finalizerCast();
}

//  int QQmlType::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType5indexEv(const QQmlType *self) {
  return self->index();
}

//  bool QQmlType::isInlineComponentType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlType21isInlineComponentTypeEv(const QQmlType *self) {
  return self->isInlineComponentType();
}

//  QUrl QQmlType::sourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QQmlType9sourceUrlEv(const QQmlType *self) {
  return new QUrl(self->sourceUrl());
}

//  int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
//      QHashedStringRef &a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType9enumValueEP14QQmlTypeLoaderRK16QHashedStringRefPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QHashedStringRef *a1,
    bool *ok) {
  return self->enumValue(typeLoader, *a1, ok);
}

//  int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
//      QHashedCStringRef &a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType9enumValueEP14QQmlTypeLoaderRK17QHashedCStringRefPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QHashedCStringRef *a1,
    bool *ok) {
  return self->enumValue(typeLoader, *a1, ok);
}

//  int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const QV4::String
//      *a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType9enumValueEP14QQmlTypeLoaderPKN3QV46StringEPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QV4::String *a1,
    bool *ok) {
  return self->enumValue(typeLoader, a1, ok);
}

//  int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const
//      QV4::String *a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType15scopedEnumIndexEP14QQmlTypeLoaderPKN3QV46StringEPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QV4::String *a1,
    bool *ok) {
  return self->scopedEnumIndex(typeLoader, a1, ok);
}

//  int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const QString
//      &a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType15scopedEnumIndexEP14QQmlTypeLoaderRK7QStringPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QString *a1,
    bool *ok) {
  return self->scopedEnumIndex(typeLoader, *a1, ok);
}

//  int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const
//      QV4::String *a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType17unscopedEnumIndexEP14QQmlTypeLoaderPKN3QV46StringEPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QV4::String *a1,
    bool *ok) {
  return self->unscopedEnumIndex(typeLoader, a1, ok);
}

//  int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const QString
//      &a1, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType17unscopedEnumIndexEP14QQmlTypeLoaderRK7QStringPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QString *a1,
    bool *ok) {
  return self->unscopedEnumIndex(typeLoader, *a1, ok);
}

//  int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int index,
//      const QV4::String *a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType15scopedEnumValueEP14QQmlTypeLoaderiPKN3QV46StringEPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    const QV4::String *a2,
    bool *ok) {
  return self->scopedEnumValue(typeLoader, index, a2, ok);
}

//  int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int index,
//      const QString &a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType15scopedEnumValueEP14QQmlTypeLoaderiRK7QStringPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    const QString *a2,
    bool *ok) {
  return self->scopedEnumValue(typeLoader, index, *a2, ok);
}

//  int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, const
//      QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType15scopedEnumValueEP14QQmlTypeLoaderRK16QHashedStringRefS4_Pb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QHashedStringRef *a1,
    const QHashedStringRef *a2,
    bool *ok) {
  return self->scopedEnumValue(typeLoader, *a1, *a2, ok);
}

//  int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int index,
//      const QV4::String *a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType17unscopedEnumValueEP14QQmlTypeLoaderiPKN3QV46StringEPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    const QV4::String *a2,
    bool *ok) {
  return self->unscopedEnumValue(typeLoader, index, a2, ok);
}

//  int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int index,
//      const QString &a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType17unscopedEnumValueEP14QQmlTypeLoaderiRK7QStringPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    const QString *a2,
    bool *ok) {
  return self->unscopedEnumValue(typeLoader, index, *a2, ok);
}

//  int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, const
//      QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QQmlType17unscopedEnumValueEP14QQmlTypeLoaderRK16QHashedStringRefS4_Pb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    const QHashedStringRef *a1,
    const QHashedStringRef *a2,
    bool *ok) {
  return self->unscopedEnumValue(typeLoader, *a1, *a2, ok);
}

//  QString QQmlType::scopedEnumKey(QQmlTypeLoader *typeLoader, int index,
//      int value, bool *ok) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlType13scopedEnumKeyEP14QQmlTypeLoaderiiPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QString(self->scopedEnumKey(typeLoader, index, value, ok));
}

//  QStringList QQmlType::scopedEnumKeys(QQmlTypeLoader *typeLoader, int
//      index, int value, bool *ok) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QQmlType14scopedEnumKeysEP14QQmlTypeLoaderiiPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QList<QString>(
      self->scopedEnumKeys(
          typeLoader,
          index,
          value,
          ok));
}

//  QString QQmlType::unscopedEnumKey(QQmlTypeLoader *typeLoader, int index,
//      int value, bool *ok) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlType15unscopedEnumKeyEP14QQmlTypeLoaderiiPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QString(self->unscopedEnumKey(typeLoader, index, value, ok));
}

//  QStringList QQmlType::unscopedEnumKeys(QQmlTypeLoader *typeLoader, int
//      index, int value, bool *ok) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QQmlType16unscopedEnumKeysEP14QQmlTypeLoaderiiPb(
    const QQmlType *self,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QList<QString>(
      self->unscopedEnumKeys(
          typeLoader,
          index,
          value,
          ok));
}

//  const QQmlTypePrivate *QQmlType::priv() const
extern "C" Q_DECL_EXPORT
const QQmlTypePrivate *ritual_ZNK8QQmlType4privEv(const QQmlType *self) {
  return self->priv();
}

//  void QQmlType::refHandle(const QQmlTypePrivate *priv)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlType9refHandleEPK15QQmlTypePrivate(
    const QQmlTypePrivate *priv) {
  QQmlType::refHandle(priv);
}

//  void QQmlType::derefHandle(const QQmlTypePrivate *priv)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlType11derefHandleEPK15QQmlTypePrivate(
    const QQmlTypePrivate *priv) {
  QQmlType::derefHandle(priv);
}

//  int QQmlType::refCount(const QQmlTypePrivate *priv)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QQmlType8refCountEPK15QQmlTypePrivate(
    const QQmlTypePrivate *priv) {
  return QQmlType::refCount(priv);
}

//  void QQmlType::createProxy(QObject *instance) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QQmlType11createProxyEP7QObject(
    const QQmlType *self,
    QObject *instance) {
  self->createProxy(instance);
}

//  bool operator==(const QQmlType &a, const QQmlType &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QQmlTypeS1_(const QQmlType *a, const QQmlType *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QQmlType &a, const QQmlType &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QQmlTypeS1_(const QQmlType *a, const QQmlType *b) {
  return operator!=(*a, *b);
}

//  QList<QQmlType>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlType> *ritual_list_make_QQmlType() {
  return new QList<QQmlType>();
}

//  void QList<QQmlType>::append(const QQmlType &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlType(
    QList<QQmlType> *self,
    const QQmlType *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlType>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlType(const QList<QQmlType> *self) {
  return self->size();
}

//  const QQmlType &QList<QQmlType>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_list_at_QQmlType(
    const QList<QQmlType> *self,
    long long index) {
  return new QQmlType(self->at(index));
}

//  QList<QQmlType>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlType(QList<QQmlType> *self) {
  delete self;
}
