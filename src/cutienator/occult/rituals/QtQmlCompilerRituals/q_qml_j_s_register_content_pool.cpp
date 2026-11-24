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

//  QQmlJSRegisterContent
//      QQmlJSRegisterContentPool::clone(QQmlJSRegisterContent from)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN25QQmlJSRegisterContentPool5cloneE21QQmlJSRegisterContent(
    QQmlJSRegisterContentPool *self,
    const QQmlJSRegisterContent *from) {
  return new QQmlJSRegisterContent(self->clone(*from));
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
