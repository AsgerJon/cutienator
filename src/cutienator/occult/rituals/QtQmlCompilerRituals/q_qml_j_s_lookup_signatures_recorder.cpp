//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslookupsignatures_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslookupsignatures_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <optional>

//  QQmlJSLookupSignaturesRecorder::QQmlJSLookupSignaturesRecorder(const
//      QString &currentFilePath, const QQmlJSTypeResolver *typeResolver)
extern "C" Q_DECL_EXPORT
QQmlJSLookupSignaturesRecorder *ritual_ZN30QQmlJSLookupSignaturesRecorderC1ERK7QStringPK18QQmlJSTypeResolver(
    const QString *currentFilePath,
    const QQmlJSTypeResolver *typeResolver) {
  return new QQmlJSLookupSignaturesRecorder(*currentFilePath, typeResolver);
}

//  QQmlPrivate::AOTLookupValidation::LookupSignatures
//      QQmlJSLookupSignaturesRecorder::signatures() const
extern "C" Q_DECL_EXPORT
QQmlPrivate::AOTLookupValidation::LookupSignatures *ritual_ZNK30QQmlJSLookupSignaturesRecorder10signaturesEv(
    const QQmlJSLookupSignaturesRecorder *self) {
  return new QQmlPrivate::AOTLookupValidation::LookupSignatures(
      self->signatures());
}

//  bool QQmlJSLookupSignaturesRecorder::recordPropertyLookup(const
//      QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QQmlJSLookupSignaturesRecorder20recordPropertyLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK18QQmlJSMetaProperty(
    QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaProperty *prop) {
  return self->recordPropertyLookup(*base, *prop);
}

//  bool QQmlJSLookupSignaturesRecorder::recordMethodLookup(const
//      QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QQmlJSLookupSignaturesRecorder18recordMethodLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK16QQmlJSMetaMethod(
    QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaMethod *method) {
  return self->recordMethodLookup(*base, *method);
}

//  bool QQmlJSLookupSignaturesRecorder::recordEnumKeyLookup(const
//      QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const
//      QString &keyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QQmlJSLookupSignaturesRecorder19recordEnumKeyLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK14QQmlJSMetaEnumRK7QString(
    QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaEnum *metaEnum,
    const QString *keyName) {
  return self->recordEnumKeyLookup(*base, *metaEnum, *keyName);
}

//  QString QQmlJSLookupSignaturesRecorder::rejectMessage()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQmlJSLookupSignaturesRecorder13rejectMessageEv(
    QQmlJSLookupSignaturesRecorder *self) {
  return new QString(self->rejectMessage());
}

//  bool QQmlJSLookupSignaturesRecorder::cantDesync(const
//      QQmlJSScope::ConstPtr &base) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQmlJSLookupSignaturesRecorder10cantDesyncERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *base) {
  return self->cantDesync(*base);
}

//  bool QQmlJSLookupSignaturesRecorder::safeBase(const QQmlJSScope::ConstPtr
//      &base) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQmlJSLookupSignaturesRecorder8safeBaseERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *base) {
  return self->safeBase(*base);
}

//  bool QQmlJSLookupSignaturesRecorder::isUnnamedCompositeType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQmlJSLookupSignaturesRecorder22isUnnamedCompositeTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isUnnamedCompositeType(*type);
}

//  std::optional<QQmlPrivate::AOTLookupValidation::Type>
//      QQmlJSLookupSignaturesRecorder::type(const QQmlJSScope::ConstPtr
//      &type)
extern "C" Q_DECL_EXPORT
std::optional<QQmlPrivate::AOTLookupValidation::Type> *ritual_ZN30QQmlJSLookupSignaturesRecorder4typeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSLookupSignaturesRecorder *self,
    const QQmlJSScope::ConstPtr *type) {
  return new std::optional<QQmlPrivate::AOTLookupValidation::Type>(
      self->type(
          *type));
}

//  QQmlJSLookupSignaturesRecorder::~QQmlJSLookupSignaturesRecorder()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQmlJSLookupSignaturesRecorderD1Ev(
    QQmlJSLookupSignaturesRecorder *self) {
  delete self;
}

//  a QQmlPrivate::AOTLookupValidation::LookupSignatures a ritual of
//      QQmlJSLookupSignaturesRecorder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSLookupSignaturesRecorder__QQmlPrivate_AOTLookupValidation_LookupSignatures(
    QQmlPrivate::AOTLookupValidation::LookupSignatures *self) {
  delete self;
}

//  a std::optional<QQmlPrivate::AOTLookupValidation::Type> a ritual of
//      QQmlJSLookupSignaturesRecorder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSLookupSignaturesRecorder__std_optional_QQmlPrivate_AOTLookupValidation_Type(
    std::optional<QQmlPrivate::AOTLookupValidation::Type> *self) {
  delete self;
}
