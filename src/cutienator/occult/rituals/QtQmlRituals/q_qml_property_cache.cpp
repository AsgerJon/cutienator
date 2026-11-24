//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlenumvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QQmlPropertyCache::~QQmlPropertyCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCacheD1Ev(QQmlPropertyCache *self) {
  delete self;
}

//  void QQmlPropertyCache::update(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache6updateEPK11QMetaObject(
    QQmlPropertyCache *self,
    const QMetaObject *a0) {
  self->update(a0);
}

//  void QQmlPropertyCache::invalidate(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache10invalidateEPK11QMetaObject(
    QQmlPropertyCache *self,
    const QMetaObject *a0) {
  self->invalidate(a0);
}

//  const QMetaObject *QQmlPropertyCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache10metaObjectEv(
    const QQmlPropertyCache *self) {
  return self->metaObject();
}

//  const QMetaObject *QQmlPropertyCache::createMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache16createMetaObjectEv(
    const QQmlPropertyCache *self) {
  return self->createMetaObject();
}

//  const QMetaObject *QQmlPropertyCache::firstCppMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache18firstCppMetaObjectEv(
    const QQmlPropertyCache *self) {
  return self->firstCppMetaObject();
}

//  const QQmlPropertyData *QQmlPropertyCache::property(int a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache8propertyEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->property(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::maybeUnresolvedProperty(int
//      a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache23maybeUnresolvedPropertyEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->maybeUnresolvedProperty(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::method(int a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache6methodEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->method(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::signal(int index) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache6signalEi(
    const QQmlPropertyCache *self,
    int index) {
  return self->signal(index);
}

//  QQmlEnumData *QQmlPropertyCache::qmlEnum(int a0) const
extern "C" Q_DECL_EXPORT
QQmlEnumData *ritual_ZNK17QQmlPropertyCache7qmlEnumEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->qmlEnum(a0);
}

//  int QQmlPropertyCache::methodIndexToSignalIndex(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache24methodIndexToSignalIndexEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->methodIndexToSignalIndex(a0);
}

//  QString QQmlPropertyCache::defaultPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlPropertyCache19defaultPropertyNameEv(
    const QQmlPropertyCache *self) {
  return new QString(self->defaultPropertyName());
}

//  const QQmlPropertyData *QQmlPropertyCache::defaultProperty() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache15defaultPropertyEv(
    const QQmlPropertyCache *self) {
  return self->defaultProperty();
}

//  const QQmlPropertyCache::ConstPtr &QQmlPropertyCache::parent() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK17QQmlPropertyCache6parentEv(
    const QQmlPropertyCache *self) {
  return new QQmlPropertyCache::ConstPtr(self->parent());
}

//  void QQmlPropertyCache::setParent(QQmlPropertyCache::ConstPtr newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache9setParentENS_8ConstPtrE(
    QQmlPropertyCache *self,
    const QQmlPropertyCache::ConstPtr *newParent) {
  self->setParent(*newParent);
}

//  const QQmlPropertyData *QQmlPropertyCache::overrideData(const
//      QQmlPropertyData *a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache12overrideDataEPK16QQmlPropertyData(
    const QQmlPropertyCache *self,
    const QQmlPropertyData *a0) {
  return self->overrideData(a0);
}

//  bool QQmlPropertyCache::isAllowedInRevision(const QQmlPropertyData *a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyCache19isAllowedInRevisionEPK16QQmlPropertyData(
    const QQmlPropertyCache *self,
    const QQmlPropertyData *a0) {
  return self->isAllowedInRevision(a0);
}

//  int QQmlPropertyCache::originalClone(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache13originalCloneEi(
    const QQmlPropertyCache *self,
    int index) {
  return self->originalClone(index);
}

//  int QQmlPropertyCache::originalClone(const QObject *a0, int index)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlPropertyCache13originalCloneEPK7QObjecti(
    const QObject *a0,
    int index) {
  return QQmlPropertyCache::originalClone(a0, index);
}

//  QList<QByteArray> QQmlPropertyCache::signalParameterNames(int index)
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK17QQmlPropertyCache20signalParameterNamesEi(
    const QQmlPropertyCache *self,
    int index) {
  return new QList<QByteArray>(self->signalParameterNames(index));
}

//  QString QQmlPropertyCache::signalParameterStringForJS(const
//      QList<QByteArray> &parameterNameList, QString *errorString)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlPropertyCache26signalParameterStringForJSERK5QListI10QByteArrayEP7QString(
    const QList<QByteArray> *parameterNameList,
    QString *errorString) {
  return new QString(
      QQmlPropertyCache::signalParameterStringForJS(
          *parameterNameList,
          errorString));
}

//  const char *QQmlPropertyCache::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK17QQmlPropertyCache9classNameEv(
    const QQmlPropertyCache *self) {
  return self->className();
}

//  int QQmlPropertyCache::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache13propertyCountEv(
    const QQmlPropertyCache *self) {
  return self->propertyCount();
}

//  int QQmlPropertyCache::ownPropertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache16ownPropertyCountEv(
    const QQmlPropertyCache *self) {
  return self->ownPropertyCount();
}

//  int QQmlPropertyCache::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14propertyOffsetEv(
    const QQmlPropertyCache *self) {
  return self->propertyOffset();
}

//  int QQmlPropertyCache::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache11methodCountEv(
    const QQmlPropertyCache *self) {
  return self->methodCount();
}

//  int QQmlPropertyCache::ownMethodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14ownMethodCountEv(
    const QQmlPropertyCache *self) {
  return self->ownMethodCount();
}

//  int QQmlPropertyCache::methodOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12methodOffsetEv(
    const QQmlPropertyCache *self) {
  return self->methodOffset();
}

//  int QQmlPropertyCache::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache11signalCountEv(
    const QQmlPropertyCache *self) {
  return self->signalCount();
}

//  int QQmlPropertyCache::ownSignalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14ownSignalCountEv(
    const QQmlPropertyCache *self) {
  return self->ownSignalCount();
}

//  int QQmlPropertyCache::signalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12signalOffsetEv(
    const QQmlPropertyCache *self) {
  return self->signalOffset();
}

//  int QQmlPropertyCache::ownEnumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12ownEnumCountEv(
    const QQmlPropertyCache *self) {
  return self->ownEnumCount();
}

//  bool QQmlPropertyCache::determineMetaObjectSizes(const QMetaObject &mo,
//      int *fieldCount, int *stringCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlPropertyCache24determineMetaObjectSizesERK11QMetaObjectPiS3_(
    const QMetaObject *mo,
    int *fieldCount,
    int *stringCount) {
  return QQmlPropertyCache::determineMetaObjectSizes(
      *mo,
      fieldCount,
      stringCount);
}

//  QTypeRevision QQmlPropertyCache::allowedRevision(int index) const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK17QQmlPropertyCache15allowedRevisionEi(
    const QQmlPropertyCache *self,
    int index) {
  return new QTypeRevision(self->allowedRevision(index));
}

//  void QQmlPropertyCache::setAllowedRevision(int index, QTypeRevision
//      allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache18setAllowedRevisionEi13QTypeRevision(
    QQmlPropertyCache *self,
    int index,
    const QTypeRevision *allowed) {
  self->setAllowedRevision(index, *allowed);
}

//  bool QQmlPropertyCache::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyCache11isCompositeEv(
    const QQmlPropertyCache *self) {
  return self->isComposite();
}

//  void QQmlPropertyCache::append(const QMetaObject *a0, QTypeRevision
//      typeVersion, QQmlPropertyData::Flags propertyFlags,
//      QQmlPropertyData::Flags methodFlags, QQmlPropertyData::Flags
//      signalFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache6appendEPK11QMetaObject13QTypeRevisionN16QQmlPropertyData5FlagsES5_S5_(
    QQmlPropertyCache *self,
    const QMetaObject *a0,
    const QTypeRevision *typeVersion,
    const QQmlPropertyData::Flags *propertyFlags,
    const QQmlPropertyData::Flags *methodFlags,
    const QQmlPropertyData::Flags *signalFlags) {
  self->append(a0, *typeVersion, *propertyFlags, *methodFlags, *signalFlags);
}

//  void QQmlPropertyCache::appendSignal(const QString &a0,
//      QQmlPropertyData::Flags a1, int coreIndex, const QMetaType *types,
//      const QList<QByteArray> &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache12appendSignalERK7QStringN16QQmlPropertyData5FlagsEiPK9QMetaTypeRK5QListI10QByteArrayE(
    QQmlPropertyCache *self,
    const QString *a0,
    const QQmlPropertyData::Flags *a1,
    int coreIndex,
    const QMetaType *types,
    const QList<QByteArray> *names) {
  self->appendSignal(*a0, *a1, coreIndex, types, *names);
}

//  void QQmlPropertyCache::appendMethod(const QString &a0,
//      QQmlPropertyData::Flags flags, int coreIndex, QMetaType returnType,
//      const QList<QByteArray> &names, const QList<QMetaType>
//      &parameterTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache12appendMethodERK7QStringN16QQmlPropertyData5FlagsEi9QMetaTypeRK5QListI10QByteArrayERKS6_IS5_E(
    QQmlPropertyCache *self,
    const QString *a0,
    const QQmlPropertyData::Flags *flags,
    int coreIndex,
    const QMetaType *returnType,
    const QList<QByteArray> *names,
    const QList<QMetaType> *parameterTypes) {
  self->appendMethod(
      *a0,
      *flags,
      coreIndex,
      *returnType,
      *names,
      *parameterTypes);
}

//  void QQmlPropertyCache::appendEnum(const QString &a0, const
//      QList<QQmlEnumValue> &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache10appendEnumERK7QStringRK5QListI13QQmlEnumValueE(
    QQmlPropertyCache *self,
    const QString *a0,
    const QList<QQmlEnumValue> *a1) {
  self->appendEnum(*a0, *a1);
}

//  QQmlPropertyCacheMethodArguments
//      *QQmlPropertyCache::createArgumentsObject(int count, const
//      QList<QByteArray> &names)
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheMethodArguments *ritual_ZN17QQmlPropertyCache21createArgumentsObjectEiRK5QListI10QByteArrayE(
    QQmlPropertyCache *self,
    int count,
    const QList<QByteArray> *names) {
  return self->createArgumentsObject(count, *names);
}
