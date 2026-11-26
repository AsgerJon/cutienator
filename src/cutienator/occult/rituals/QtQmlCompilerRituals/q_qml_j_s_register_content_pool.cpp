//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QQmlJSRegisterContentPool::QQmlJSRegisterContentPool()
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContentPool *ritual_ZN25QQmlJSRegisterContentPoolC1Ev() {
  return new QQmlJSRegisterContentPool();
}

//  QQmlJSRegisterContentPool::~QQmlJSRegisterContentPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPoolD1Ev(
    QQmlJSRegisterContentPool *self) {
  delete self;
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createType(const
//      QQmlJSScope::ConstPtr &type, int resultLookupIndex, ContentVariant
//      variant, QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool10createTypeERK22QDeferredSharedPointerIK11QQmlJSScopeEiN21QQmlJSRegisterContent14ContentVariantES6_(
    QQmlJSRegisterContentPool *self,
    const QQmlJSScope::ConstPtr *type,
    int resultLookupIndex,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createType(
          *type,
          resultLookupIndex,
          variant,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createProperty(const
//      QQmlJSMetaProperty &property, int baseLookupIndex, int
//      resultLookupIndex, ContentVariant variant, QQmlJSRegisterContent
//      scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool14createPropertyERK18QQmlJSMetaPropertyiiN21QQmlJSRegisterContent14ContentVariantES3_(
    QQmlJSRegisterContentPool *self,
    const QQmlJSMetaProperty *property,
    int baseLookupIndex,
    int resultLookupIndex,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createProperty(
          *property,
          baseLookupIndex,
          resultLookupIndex,
          variant,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createEnumeration(const
//      QQmlJSMetaEnum &enumeration, const QString &enumMember,
//      ContentVariant variant, QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool17createEnumerationERK14QQmlJSMetaEnumRK7QStringN21QQmlJSRegisterContent14ContentVariantES6_(
    QQmlJSRegisterContentPool *self,
    const QQmlJSMetaEnum *enumeration,
    const QString *enumMember,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createEnumeration(
          *enumeration,
          *enumMember,
          variant,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createMethod(const
//      QList<QQmlJSMetaMethod> &methods, const QQmlJSScope::ConstPtr
//      &methodType, ContentVariant variant, QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool12createMethodERK5QListI16QQmlJSMetaMethodERK22QDeferredSharedPointerIK11QQmlJSScopeEN21QQmlJSRegisterContent14ContentVariantESB_(
    QQmlJSRegisterContentPool *self,
    const QList<QQmlJSMetaMethod> *methods,
    const QQmlJSScope::ConstPtr *methodType,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createMethod(
          *methods,
          *methodType,
          variant,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createMethodCall(const
//      QQmlJSMetaMethod &method, const QQmlJSScope::ConstPtr &returnType,
//      QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool16createMethodCallERK16QQmlJSMetaMethodRK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContent(
    QQmlJSRegisterContentPool *self,
    const QQmlJSMetaMethod *method,
    const QQmlJSScope::ConstPtr *returnType,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createMethodCall(
          *method,
          *returnType,
          *scope));
}

//  QQmlJSRegisterContent
//      QQmlJSRegisterContentPool::createImportNamespace(uint
//      importNamespaceStringId, const QQmlJSScope::ConstPtr
//      &importNamespaceType, ContentVariant variant, QQmlJSRegisterContent
//      scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool21createImportNamespaceEjRK22QDeferredSharedPointerIK11QQmlJSScopeEN21QQmlJSRegisterContent14ContentVariantES6_(
    QQmlJSRegisterContentPool *self,
    uint importNamespaceStringId,
    const QQmlJSScope::ConstPtr *importNamespaceType,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createImportNamespace(
          importNamespaceStringId,
          *importNamespaceType,
          variant,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSRegisterContentPool::createConversion(const
//      QList<QQmlJSRegisterContent> &origins, const QQmlJSScope::ConstPtr
//      &conversion, QQmlJSRegisterContent conversionScope, ContentVariant
//      variant, QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool16createConversionERK5QListI21QQmlJSRegisterContentERK22QDeferredSharedPointerIK11QQmlJSScopeES1_NS1_14ContentVariantES1_(
    QQmlJSRegisterContentPool *self,
    const QList<QQmlJSRegisterContent> *origins,
    const QQmlJSScope::ConstPtr *conversion,
    const QQmlJSRegisterContent *conversionScope,
    QQmlJSRegisterContentPool::ContentVariant variant,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->createConversion(
          *origins,
          *conversion,
          *conversionScope,
          variant,
          *scope));
}

//  QQmlJSRegisterContent
//      QQmlJSRegisterContentPool::storedIn(QQmlJSRegisterContent content,
//      const QQmlJSScope::ConstPtr &newStoredType)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool8storedInE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *content,
    const QQmlJSScope::ConstPtr *newStoredType) {
  return new QQmlJSRegisterContent(self->storedIn(*content, *newStoredType));
}

//  QQmlJSRegisterContent
//      QQmlJSRegisterContentPool::castTo(QQmlJSRegisterContent content,
//      const QQmlJSScope::ConstPtr &newContainedType)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool6castToE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *content,
    const QQmlJSScope::ConstPtr *newContainedType) {
  return new QQmlJSRegisterContent(
      self->castTo(
          *content,
          *newContainedType));
}

//  QQmlJSRegisterContent
//      QQmlJSRegisterContentPool::clone(QQmlJSRegisterContent from)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool5cloneE21QQmlJSRegisterContent(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *from) {
  return new QQmlJSRegisterContent(self->clone(*from));
}

//  void QQmlJSRegisterContentPool::storeType(QQmlJSRegisterContent content,
//      const QQmlJSScope::ConstPtr &stored)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPool9storeTypeE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *content,
    const QQmlJSScope::ConstPtr *stored) {
  self->storeType(*content, *stored);
}

//  void QQmlJSRegisterContentPool::adjustType(QQmlJSRegisterContent content,
//      const QQmlJSScope::ConstPtr &adjusted)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPool10adjustTypeE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *content,
    const QQmlJSScope::ConstPtr *adjusted) {
  self->adjustType(*content, *adjusted);
}

//  void QQmlJSRegisterContentPool::generalizeType(QQmlJSRegisterContent
//      content, const QQmlJSScope::ConstPtr &generalized)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPool14generalizeTypeE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *content,
    const QQmlJSScope::ConstPtr *generalized) {
  self->generalizeType(*content, *generalized);
}

//  void QQmlJSRegisterContentPool::setAllocationMode(AllocationMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPool17setAllocationModeENS_14AllocationModeE(
    QQmlJSRegisterContentPool *self,
    QQmlJSRegisterContentPool::AllocationMode mode) {
  self->setAllocationMode(mode);
}

//  void QQmlJSRegisterContentPool::clearTemporaries()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSRegisterContentPool16clearTemporariesEv(
    QQmlJSRegisterContentPool *self) {
  self->clearTemporaries();
}

//  QQmlJSRegisterContentPrivate *QQmlJSRegisterContentPool::clone(const
//      QQmlJSRegisterContentPrivate *from)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContentPrivate *ritual_ZN25QQmlJSRegisterContentPool5cloneEPK28QQmlJSRegisterContentPrivate(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContentPrivate *from) {
  return self->clone(from);
}

//  QQmlJSRegisterContentPrivate *QQmlJSRegisterContentPool::create()
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContentPrivate *ritual_ZN25QQmlJSRegisterContentPool6createEv(
    QQmlJSRegisterContentPool *self) {
  return self->create();
}

//  QQmlJSRegisterContentPrivate
//      *QQmlJSRegisterContentPool::create(QQmlJSRegisterContent scope,
//      ContentVariant variant)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContentPrivate *ritual_ZN25QQmlJSRegisterContentPool6createE21QQmlJSRegisterContentNS0_14ContentVariantE(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *scope,
    QQmlJSRegisterContentPool::ContentVariant variant) {
  return self->create(*scope, variant);
}
