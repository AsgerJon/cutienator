//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Edited by hand on 2026-11-25, mended on
//  2026-11-26: added by hand, instances of templates of the class: 8. Kept
//  as it is when the generator runs again.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qdatetime.h>
#include <QtQml/qjsprimitivevalue.h>

//  QObject *QQmlPrivate::AOTCompiledContext::thisObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QQmlPrivate18AOTCompiledContext10thisObjectEv(
    const QQmlPrivate::AOTCompiledContext *self) {
  return self->thisObject();
}

//  QQmlEngine *QQmlPrivate::AOTCompiledContext::qmlEngine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK11QQmlPrivate18AOTCompiledContext9qmlEngineEv(
    const QQmlPrivate::AOTCompiledContext *self) {
  return self->qmlEngine();
}

//  QJSValue QQmlPrivate::AOTCompiledContext::jsMetaType(int index) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK11QQmlPrivate18AOTCompiledContext10jsMetaTypeEi(
    const QQmlPrivate::AOTCompiledContext *self,
    int index) {
  return new QJSValue(self->jsMetaType(index));
}

//  void QQmlPrivate::AOTCompiledContext::setInstructionPointer(int offset)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext21setInstructionPointerEi(
    const QQmlPrivate::AOTCompiledContext *self,
    int offset) {
  self->setInstructionPointer(offset);
}

//  void QQmlPrivate::AOTCompiledContext::setLocals(const
//      AOTTrackedLocalsStorage *locals) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext9setLocalsEPKNS_23AOTTrackedLocalsStorageE(
    const QQmlPrivate::AOTCompiledContext *self,
    const QQmlPrivate::AOTTrackedLocalsStorage *locals) {
  self->setLocals(locals);
}

//  void QQmlPrivate::AOTCompiledContext::setReturnValueUndefined() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setReturnValueUndefinedEv(
    const QQmlPrivate::AOTCompiledContext *self) {
  self->setReturnValueUndefined();
}

//  void QQmlPrivate::AOTCompiledContext::mark(QObject *object,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markEP7QObjectPN3QV49MarkStackE(
    QObject *object,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark(object, markStack);
}

//  void QQmlPrivate::AOTCompiledContext::mark(const QVariant &variant,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markERK8QVariantPN3QV49MarkStackE(
    const QVariant *variant,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark(*variant, markStack);
}

//  bool QQmlPrivate::AOTCompiledContext::captureLookup(uint index, QObject
//      *object) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext13captureLookupEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  return self->captureLookup(index, object);
}

//  bool
//      QQmlPrivate::AOTCompiledContext::captureQmlContextPropertyLookup(uint
//      index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext31captureQmlContextPropertyLookupEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index) {
  return self->captureQmlContextPropertyLookup(index);
}

//  void QQmlPrivate::AOTCompiledContext::captureTranslation() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18captureTranslationEv(
    const QQmlPrivate::AOTCompiledContext *self) {
  self->captureTranslation();
}

//  QString QQmlPrivate::AOTCompiledContext::translationContext() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlPrivate18AOTCompiledContext18translationContextEv(
    const QQmlPrivate::AOTCompiledContext *self) {
  return new QString(self->translationContext());
}

//  QMetaType QQmlPrivate::AOTCompiledContext::lookupResultMetaType(uint
//      index) const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK11QQmlPrivate18AOTCompiledContext20lookupResultMetaTypeEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index) {
  return new QMetaType(self->lookupResultMetaType(index));
}

//  void QQmlPrivate::AOTCompiledContext::storeNameSloppy(uint nameIndex,
//      void *value, QMetaType type) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext15storeNameSloppyEjPv9QMetaType(
    const QQmlPrivate::AOTCompiledContext *self,
    uint nameIndex,
    void *value,
    const QMetaType *type) {
  self->storeNameSloppy(nameIndex, value, *type);
}

//  QJSValue QQmlPrivate::AOTCompiledContext::javaScriptGlobalProperty(uint
//      nameIndex) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK11QQmlPrivate18AOTCompiledContext24javaScriptGlobalPropertyEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint nameIndex) {
  return new QJSValue(self->javaScriptGlobalProperty(nameIndex));
}

//  const QLoggingCategory
//      *QQmlPrivate::AOTCompiledContext::resolveLoggingCategory(QObject
//      *wrapper, bool *ok) const
extern "C" Q_DECL_EXPORT
const QLoggingCategory *ritual_ZNK11QQmlPrivate18AOTCompiledContext22resolveLoggingCategoryEP7QObjectPb(
    const QQmlPrivate::AOTCompiledContext *self,
    QObject *wrapper,
    bool *ok) {
  return self->resolveLoggingCategory(wrapper, ok);
}

//  void QQmlPrivate::AOTCompiledContext::writeToConsole(QtMsgType type,
//      const QString &message, const QLoggingCategory *loggingCategory)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext14writeToConsoleE9QtMsgTypeRK7QStringPK16QLoggingCategory(
    const QQmlPrivate::AOTCompiledContext *self,
    QtMsgType type,
    const QString *message,
    const QLoggingCategory *loggingCategory) {
  self->writeToConsole(type, *message, loggingCategory);
}

//  QVariant QQmlPrivate::AOTCompiledContext::constructValueType(QMetaType
//      resultMetaType, const QMetaObject *resultMetaObject, int ctorIndex,
//      void **args) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQmlPrivate18AOTCompiledContext18constructValueTypeE9QMetaTypePK11QMetaObjectiPPv(
    const QQmlPrivate::AOTCompiledContext *self,
    const QMetaType *resultMetaType,
    const QMetaObject *resultMetaObject,
    int ctorIndex,
    void **args) {
  return new QVariant(
      self->constructValueType(
          *resultMetaType,
          resultMetaObject,
          ctorIndex,
          args));
}

//  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(double
//      timestamp) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeEd(
    const QQmlPrivate::AOTCompiledContext *self,
    double timestamp) {
  return new QDateTime(self->constructDateTime(timestamp));
}

//  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(const
//      QString &string) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeERK7QString(
    const QQmlPrivate::AOTCompiledContext *self,
    const QString *string) {
  return new QDateTime(self->constructDateTime(*string));
}

//  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(const
//      QJSPrimitiveValue &arg) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeERK17QJSPrimitiveValue(
    const QQmlPrivate::AOTCompiledContext *self,
    const QJSPrimitiveValue *arg) {
  return new QDateTime(self->constructDateTime(*arg));
}

//  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(double year,
//      double month, double day, double hours, double minutes, double
//      seconds, double msecs) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeEddddddd(
    const QQmlPrivate::AOTCompiledContext *self,
    double year,
    double month,
    double day,
    double hours,
    double minutes,
    double seconds,
    double msecs) {
  return new QDateTime(
      self->constructDateTime(
          year,
          month,
          day,
          hours,
          minutes,
          seconds,
          msecs));
}

//  bool QQmlPrivate::AOTCompiledContext::callQmlContextPropertyLookup(uint
//      index, void **args, int argc) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext28callQmlContextPropertyLookupEjPPvi(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void **args,
    int argc) {
  return self->callQmlContextPropertyLookup(index, args, argc);
}

//  void
//      QQmlPrivate::AOTCompiledContext::initCallQmlContextPropertyLookup(uin
//      t index, int relativeMethodIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext32initCallQmlContextPropertyLookupEji(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    int relativeMethodIndex) {
  self->initCallQmlContextPropertyLookup(index, relativeMethodIndex);
}

//  bool QQmlPrivate::AOTCompiledContext::loadContextIdLookup(uint index,
//      void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext19loadContextIdLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->loadContextIdLookup(index, target);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadContextIdLookup(uint index)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23initLoadContextIdLookupEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index) {
  self->initLoadContextIdLookup(index);
}

//  bool QQmlPrivate::AOTCompiledContext::callObjectPropertyLookup(uint
//      index, QObject *object, void **args, int argc) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext24callObjectPropertyLookupEjP7QObjectPPvi(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    void **args,
    int argc) {
  return self->callObjectPropertyLookup(index, object, args, argc);
}

//  void QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookup(uint
//      index, QObject *object, int relativeMethodIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext28initCallObjectPropertyLookupEjP7QObjecti(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    int relativeMethodIndex) {
  self->initCallObjectPropertyLookup(index, object, relativeMethodIndex);
}

//  void QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookupAsVaria
//      nt(uint index, QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext37initCallObjectPropertyLookupAsVariantEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initCallObjectPropertyLookupAsVariant(index, object);
}

//  bool QQmlPrivate::AOTCompiledContext::loadGlobalLookup(uint index, void
//      *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext16loadGlobalLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->loadGlobalLookup(index, target);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadGlobalLookup(uint index,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext20initLoadGlobalLookupEj9QMetaType(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaType *type) {
  self->initLoadGlobalLookup(index, *type);
}

//  bool QQmlPrivate::AOTCompiledContext::loadScopeObjectPropertyLookup(uint
//      index, void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext29loadScopeObjectPropertyLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->loadScopeObjectPropertyLookup(index, target);
}

//  bool
//      QQmlPrivate::AOTCompiledContext::writeBackScopeObjectPropertyLookup(u
//      int index, void *source) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext34writeBackScopeObjectPropertyLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *source) {
  return self->writeBackScopeObjectPropertyLookup(index, source);
}

//  void
//      QQmlPrivate::AOTCompiledContext::initLoadScopeObjectPropertyLookup(ui
//      nt index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext33initLoadScopeObjectPropertyLookupEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index) {
  self->initLoadScopeObjectPropertyLookup(index);
}

//  bool QQmlPrivate::AOTCompiledContext::loadSingletonLookup(uint index,
//      void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext19loadSingletonLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->loadSingletonLookup(index, target);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadSingletonLookup(uint index,
//      uint importNamespace) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23initLoadSingletonLookupEjj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    uint importNamespace) {
  self->initLoadSingletonLookup(index, importNamespace);
}

//  bool QQmlPrivate::AOTCompiledContext::loadAttachedLookup(uint index,
//      QObject *object, void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext18loadAttachedLookupEjP7QObjectPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    void *target) {
  return self->loadAttachedLookup(index, object, target);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadAttachedLookup(uint index,
//      uint importNamespace, QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext22initLoadAttachedLookupEjjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    uint importNamespace,
    QObject *object) {
  self->initLoadAttachedLookup(index, importNamespace, object);
}

//  bool QQmlPrivate::AOTCompiledContext::loadTypeLookup(uint index, void
//      *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext14loadTypeLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->loadTypeLookup(index, target);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadTypeLookup(uint index, uint
//      importNamespace) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18initLoadTypeLookupEjj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    uint importNamespace) {
  self->initLoadTypeLookup(index, importNamespace);
}

//  bool QQmlPrivate::AOTCompiledContext::getObjectLookup(uint index, QObject
//      *object, void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext15getObjectLookupEjP7QObjectPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    void *target) {
  return self->getObjectLookup(index, object, target);
}

//  bool QQmlPrivate::AOTCompiledContext::writeBackObjectLookup(uint index,
//      QObject *object, void *source) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext21writeBackObjectLookupEjP7QObjectPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    void *source) {
  return self->writeBackObjectLookup(index, object, source);
}

//  void QQmlPrivate::AOTCompiledContext::initGetObjectLookup(uint index,
//      QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext19initGetObjectLookupEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initGetObjectLookup(index, object);
}

//  void QQmlPrivate::AOTCompiledContext::initGetObjectLookupAsVariant(uint
//      index, QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext28initGetObjectLookupAsVariantEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initGetObjectLookupAsVariant(index, object);
}

//  bool QQmlPrivate::AOTCompiledContext::getValueLookup(uint index, void
//      *value, void *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext14getValueLookupEjPvS1_(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *value,
    void *target) {
  return self->getValueLookup(index, value, target);
}

//  bool QQmlPrivate::AOTCompiledContext::writeBackValueLookup(uint index,
//      void *value, void *source) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext20writeBackValueLookupEjPvS1_(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *value,
    void *source) {
  return self->writeBackValueLookup(index, value, source);
}

//  void QQmlPrivate::AOTCompiledContext::initGetValueLookup(uint index,
//      const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18initGetValueLookupEjPK11QMetaObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject) {
  self->initGetValueLookup(index, metaObject);
}

//  bool QQmlPrivate::AOTCompiledContext::getEnumLookup(uint index, void
//      *target) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext13getEnumLookupEjPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target) {
  return self->getEnumLookup(index, target);
}

//  void QQmlPrivate::AOTCompiledContext::initGetEnumLookup(uint index, const
//      QMetaObject *metaObject, const char *enumerator, const char
//      *enumValue) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext17initGetEnumLookupEjPK11QMetaObjectPKcS5_(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject,
    const char *enumerator,
    const char *enumValue) {
  self->initGetEnumLookup(index, metaObject, enumerator, enumValue);
}

//  bool QQmlPrivate::AOTCompiledContext::setObjectLookup(uint index, QObject
//      *object, void *value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext15setObjectLookupEjP7QObjectPv(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    void *value) {
  return self->setObjectLookup(index, object, value);
}

//  void QQmlPrivate::AOTCompiledContext::initSetObjectLookup(uint index,
//      QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext19initSetObjectLookupEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initSetObjectLookup(index, object);
}

//  void QQmlPrivate::AOTCompiledContext::initSetObjectLookupAsVariant(uint
//      index, QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext28initSetObjectLookupAsVariantEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initSetObjectLookupAsVariant(index, object);
}

//  bool QQmlPrivate::AOTCompiledContext::setValueLookup(uint index, void
//      *target, void *value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext14setValueLookupEjPvS1_(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target,
    void *value) {
  return self->setValueLookup(index, target, value);
}

//  void QQmlPrivate::AOTCompiledContext::initSetValueLookup(uint index,
//      const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18initSetValueLookupEjPK11QMetaObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject) {
  self->initSetValueLookup(index, metaObject);
}

//  void QQmlPrivate::AOTCompiledContext::initSetValueLookupAsVariant(uint
//      index, const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext27initSetValueLookupAsVariantEjPK11QMetaObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject) {
  self->initSetValueLookupAsVariant(index, metaObject);
}

//  bool QQmlPrivate::AOTCompiledContext::callValueLookup(uint index, void
//      *target, void **args, int argc) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate18AOTCompiledContext15callValueLookupEjPvPS1_i(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    void *target,
    void **args,
    int argc) {
  return self->callValueLookup(index, target, args, argc);
}

//  void QQmlPrivate::AOTCompiledContext::initCallValueLookup(uint index,
//      const QMetaObject *metaObject, int relativeMethodIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext19initCallValueLookupEjPK11QMetaObjecti(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject,
    int relativeMethodIndex) {
  self->initCallValueLookup(index, metaObject, relativeMethodIndex);
}

//  void
//      QQmlPrivate::AOTCompiledContext::setObjectImplicitDestructible(QObjec
//      t *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext29setObjectImplicitDestructibleEP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    QObject *object) {
  self->setObjectImplicitDestructible(object);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(QObject
//      *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleEP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    QObject *object) {
  self->setImplicitDestructible(object);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(const
//      QVariant &variant) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleERK8QVariant(
    const QQmlPrivate::AOTCompiledContext *self,
    const QVariant *variant) {
  self->setImplicitDestructible(*variant);
}

//  QQmlPrivate::AOTCompiledContext::~AOTCompiledContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContextD1Ev(
    QQmlPrivate::AOTCompiledContext *self) {
  delete self;
}

//  static void QQmlPrivate::AOTCompiledContext::mark<int>(int,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markIiEEvT_PN3QV49MarkStackE(
    int value,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark<int>(value, markStack);
}

//  static void QQmlPrivate::AOTCompiledContext::mark<double>(double,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markIdEEvT_PN3QV49MarkStackE(
    double value,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark<double>(value, markStack);
}

//  static void QQmlPrivate::AOTCompiledContext::mark<bool>(bool,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markIbEEvT_PN3QV49MarkStackE(
    bool value,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark<bool>(value, markStack);
}

//  static void QQmlPrivate::AOTCompiledContext::mark<QString>(QString,
//      QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContext4markI7QStringEEvT_PN3QV49MarkStackE(
    const QString *value,
    QV4::MarkStack *markStack) {
  QQmlPrivate::AOTCompiledContext::mark<QString>(*value, markStack);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible<int>(const
//      int &value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleIiEEvRKT_(
    const QQmlPrivate::AOTCompiledContext *self,
    const int *value) {
  self->setImplicitDestructible<int>(*value);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible<double>(
//      const double &value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleIdEEvRKT_(
    const QQmlPrivate::AOTCompiledContext *self,
    const double *value) {
  self->setImplicitDestructible<double>(*value);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible<bool>(const
//      bool &value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleIbEEvRKT_(
    const QQmlPrivate::AOTCompiledContext *self,
    const bool *value) {
  self->setImplicitDestructible<bool>(*value);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible<QString>(
//      const QString &value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleI7QStringEEvRKT_(
    const QQmlPrivate::AOTCompiledContext *self,
    const QString *value) {
  self->setImplicitDestructible<QString>(*value);
}
