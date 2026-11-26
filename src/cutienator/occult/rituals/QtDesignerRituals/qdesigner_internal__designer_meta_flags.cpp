//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags(const QString
//      &enumName, const QString &scope, const QString &separator)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerMetaFlags *ritual_ZN18qdesigner_internal17DesignerMetaFlagsC1ERK7QStringS3_S3_(
    const QString *enumName,
    const QString *scope,
    const QString *separator) {
  return new qdesigner_internal::DesignerMetaFlags(
      *enumName,
      *scope,
      *separator);
}

//  qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags()
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerMetaFlags *ritual_ZN18qdesigner_internal17DesignerMetaFlagsC1Ev() {
  return new qdesigner_internal::DesignerMetaFlags();
}

//  QStringList qdesigner_internal::DesignerMetaFlags::flags(int value) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal17DesignerMetaFlags5flagsEi(
    const qdesigner_internal::DesignerMetaFlags *self,
    int value) {
  return new QList<QString>(self->flags(value));
}

//  QString qdesigner_internal::DesignerMetaFlags::messageParseFailed(const
//      QString &s) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal17DesignerMetaFlags18messageParseFailedERK7QString(
    const qdesigner_internal::DesignerMetaFlags *self,
    const QString *s) {
  return new QString(self->messageParseFailed(*s));
}

//  int qdesigner_internal::DesignerMetaFlags::parseFlags(const QString &s,
//      bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal17DesignerMetaFlags10parseFlagsERK7QStringPb(
    const qdesigner_internal::DesignerMetaFlags *self,
    const QString *s,
    bool *ok) {
  return self->parseFlags(*s, ok);
}

//  qdesigner_internal::DesignerMetaFlags::~DesignerMetaFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17DesignerMetaFlagsD1Ev(
    qdesigner_internal::DesignerMetaFlags *self) {
  delete self;
}
