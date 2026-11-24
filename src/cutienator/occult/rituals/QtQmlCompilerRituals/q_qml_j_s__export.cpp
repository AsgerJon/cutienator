//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>

//  QQmlJS::Export::Export()
extern "C" Q_DECL_EXPORT
QQmlJS::Export *ritual_ZN6QQmlJS6ExportC1Ev() {
  return new QQmlJS::Export();
}

//  QString QQmlJS::Export::package() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS6Export7packageEv(const QQmlJS::Export *self) {
  return new QString(self->package());
}

//  QString QQmlJS::Export::type() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS6Export4typeEv(const QQmlJS::Export *self) {
  return new QString(self->type());
}

//  QTypeRevision QQmlJS::Export::version() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK6QQmlJS6Export7versionEv(
    const QQmlJS::Export *self) {
  return new QTypeRevision(self->version());
}

//  QTypeRevision QQmlJS::Export::revision() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK6QQmlJS6Export8revisionEv(
    const QQmlJS::Export *self) {
  return new QTypeRevision(self->revision());
}

//  QQmlJS::Export::~Export()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6ExportD1Ev(QQmlJS::Export *self) {
  delete self;
}
