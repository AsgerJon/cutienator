//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlscriptstring.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qstring.h>

//  QQmlScriptString::QQmlScriptString()
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZN16QQmlScriptStringC1Ev() {
  return new QQmlScriptString();
}

//  QQmlScriptString::QQmlScriptString(const QQmlScriptString &a0)
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZN16QQmlScriptStringC1ERKS_(
    const QQmlScriptString *a0) {
  return new QQmlScriptString(*a0);
}

//  QQmlScriptString::~QQmlScriptString()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlScriptStringD1Ev(QQmlScriptString *self) {
  delete self;
}

//  bool QQmlScriptString::operator==(const QQmlScriptString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptStringeqERKS_(
    const QQmlScriptString *self,
    const QQmlScriptString *a0) {
  return self->operator==(*a0);
}

//  bool QQmlScriptString::operator!=(const QQmlScriptString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptStringneERKS_(
    const QQmlScriptString *self,
    const QQmlScriptString *a0) {
  return self->operator!=(*a0);
}

//  bool QQmlScriptString::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptString7isEmptyEv(const QQmlScriptString *self) {
  return self->isEmpty();
}

//  bool QQmlScriptString::isUndefinedLiteral() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptString18isUndefinedLiteralEv(
    const QQmlScriptString *self) {
  return self->isUndefinedLiteral();
}

//  bool QQmlScriptString::isNullLiteral() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptString13isNullLiteralEv(
    const QQmlScriptString *self) {
  return self->isNullLiteral();
}

//  QString QQmlScriptString::stringLiteral() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlScriptString13stringLiteralEv(
    const QQmlScriptString *self) {
  return new QString(self->stringLiteral());
}

//  qreal QQmlScriptString::numberLiteral(bool *ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQmlScriptString13numberLiteralEPb(
    const QQmlScriptString *self,
    bool *ok) {
  return self->numberLiteral(ok);
}

//  bool QQmlScriptString::booleanLiteral(bool *ok) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlScriptString14booleanLiteralEPb(
    const QQmlScriptString *self,
    bool *ok) {
  return self->booleanLiteral(ok);
}

//  QQmlScriptString::QQmlScriptString(const QString &script, QQmlContext
//      *context, QObject *scope)
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZN16QQmlScriptStringC1ERK7QStringP11QQmlContextP7QObject(
    const QString *script,
    QQmlContext *context,
    QObject *scope) {
  return new QQmlScriptString(*script, context, scope);
}
