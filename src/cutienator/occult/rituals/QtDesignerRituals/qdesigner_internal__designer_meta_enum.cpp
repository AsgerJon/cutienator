//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum(const QString
//      &name, const QString &scope, const QString &separator)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerMetaEnum *ritual_ZN18qdesigner_internal16DesignerMetaEnumC1ERK7QStringS3_S3_(
    const QString *name,
    const QString *scope,
    const QString *separator) {
  return new qdesigner_internal::DesignerMetaEnum(*name, *scope, *separator);
}

//  qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum()
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerMetaEnum *ritual_ZN18qdesigner_internal16DesignerMetaEnumC1Ev() {
  return new qdesigner_internal::DesignerMetaEnum();
}

//  QString qdesigner_internal::DesignerMetaEnum::messageToStringFailed(int
//      value) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal16DesignerMetaEnum21messageToStringFailedEi(
    const qdesigner_internal::DesignerMetaEnum *self,
    int value) {
  return new QString(self->messageToStringFailed(value));
}

//  QString qdesigner_internal::DesignerMetaEnum::messageParseFailed(const
//      QString &s) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal16DesignerMetaEnum18messageParseFailedERK7QString(
    const qdesigner_internal::DesignerMetaEnum *self,
    const QString *s) {
  return new QString(self->messageParseFailed(*s));
}

//  int qdesigner_internal::DesignerMetaEnum::parseEnum(const QString &s,
//      bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal16DesignerMetaEnum9parseEnumERK7QStringPb(
    const qdesigner_internal::DesignerMetaEnum *self,
    const QString *s,
    bool *ok) {
  return self->parseEnum(*s, ok);
}

//  qdesigner_internal::DesignerMetaEnum::~DesignerMetaEnum()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16DesignerMetaEnumD1Ev(
    qdesigner_internal::DesignerMetaEnum *self) {
  delete self;
}
