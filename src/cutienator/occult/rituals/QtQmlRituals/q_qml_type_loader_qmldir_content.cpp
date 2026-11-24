//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypeloaderqmldircontent_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/qqmlerror.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderqmldircontent.cpp, line 26, as _ZN27QQmlTypeLoaderQmldirContent10setContentERK7QStringS2_
inline void QQmlTypeLoaderQmldirContent::setContent(const QString &location, const QString &content)
{
    Q_ASSERT(!m_hasContent);
    m_hasContent = true;
    m_location = location;
    m_parser.parse(content);
    m_parser.disambiguateFileSelectors();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderqmldircontent.cpp, line 35, as _ZN27QQmlTypeLoaderQmldirContent8setErrorERK9QQmlError
inline void QQmlTypeLoaderQmldirContent::setError(const QQmlError &error)
{
    QQmlJS::DiagnosticMessage parseError;
    parseError.loc.startLine = error.line();
    parseError.loc.startColumn = error.column();
    parseError.message = error.description();
    m_parser.setError(parseError);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderqmldircontent.cpp, line 11, as _ZNK27QQmlTypeLoaderQmldirContent6errorsERK7QStringRK4QUrl
inline QList<QQmlError> QQmlTypeLoaderQmldirContent::errors(const QString &uri, const QUrl &url) const
{
    QList<QQmlError> errors;
    const auto parseErrors = m_parser.errors(uri);
    for (const auto &parseError : parseErrors) {
        QQmlError error;
        error.setUrl(url);
        error.setLine(qmlConvertSourceCoordinate<quint32, int>(parseError.loc.startLine));
        error.setColumn(qmlConvertSourceCoordinate<quint32, int>(parseError.loc.startColumn));
        error.setDescription(parseError.message);
        errors.append(error);
    }
    return errors;
}
//  -----------------------------------------------------------------------

//  void QQmlTypeLoaderQmldirContent::setContent(const QString &location,
//      const QString &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlTypeLoaderQmldirContent10setContentERK7QStringS2_(
    QQmlTypeLoaderQmldirContent *self,
    const QString *location,
    const QString *content) {
  self->setContent(*location, *content);
}

//  void QQmlTypeLoaderQmldirContent::setError(const QQmlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlTypeLoaderQmldirContent8setErrorERK9QQmlError(
    QQmlTypeLoaderQmldirContent *self,
    const QQmlError *a0) {
  self->setError(*a0);
}

//  QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent()
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderQmldirContent *ritual_ZN27QQmlTypeLoaderQmldirContentC1Ev() {
  return new QQmlTypeLoaderQmldirContent();
}

//  QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent(const
//      QQmlTypeLoaderQmldirContent &a0)
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderQmldirContent *ritual_ZN27QQmlTypeLoaderQmldirContentC1ERKS_(
    const QQmlTypeLoaderQmldirContent *a0) {
  return new QQmlTypeLoaderQmldirContent(*a0);
}

//  bool QQmlTypeLoaderQmldirContent::hasContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent10hasContentEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->hasContent();
}

//  bool QQmlTypeLoaderQmldirContent::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent8hasErrorEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->hasError();
}

//  QList<QQmlError> QQmlTypeLoaderQmldirContent::errors(const QString &uri,
//      const QUrl &url) const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK27QQmlTypeLoaderQmldirContent6errorsERK7QStringRK4QUrl(
    const QQmlTypeLoaderQmldirContent *self,
    const QString *uri,
    const QUrl *url) {
  return new QList<QQmlError>(self->errors(*uri, *url));
}

//  bool QQmlTypeLoaderQmldirContent::hasTypeNamespace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent16hasTypeNamespaceEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->hasTypeNamespace();
}

//  QString QQmlTypeLoaderQmldirContent::typeNamespace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlTypeLoaderQmldirContent13typeNamespaceEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return new QString(self->typeNamespace());
}

//  QString QQmlTypeLoaderQmldirContent::qmldirLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlTypeLoaderQmldirContent14qmldirLocationEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return new QString(self->qmldirLocation());
}

//  QString QQmlTypeLoaderQmldirContent::preferredPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlTypeLoaderQmldirContent13preferredPathEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return new QString(self->preferredPath());
}

//  QString QQmlTypeLoaderQmldirContent::linkTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlTypeLoaderQmldirContent10linkTargetEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return new QString(self->linkTarget());
}

//  bool QQmlTypeLoaderQmldirContent::hasRedirection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent14hasRedirectionEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->hasRedirection();
}

//  bool QQmlTypeLoaderQmldirContent::designerSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent17designerSupportedEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->designerSupported();
}

//  bool QQmlTypeLoaderQmldirContent::hasTypeInfo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlTypeLoaderQmldirContent11hasTypeInfoEv(
    const QQmlTypeLoaderQmldirContent *self) {
  return self->hasTypeInfo();
}

//  QQmlTypeLoaderQmldirContent::~QQmlTypeLoaderQmldirContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlTypeLoaderQmldirContentD1Ev(
    QQmlTypeLoaderQmldirContent *self) {
  delete self;
}
