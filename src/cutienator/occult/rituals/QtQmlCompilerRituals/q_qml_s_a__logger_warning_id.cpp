//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmljsloggingutils.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQmlCompiler/qqmljsloggingutils.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QQmlSA::LoggerWarningId::LoggerWarningId(QAnyStringView name)
extern "C" Q_DECL_EXPORT
QQmlSA::LoggerWarningId *ritual_ZN6QQmlSA15LoggerWarningIdC1E14QAnyStringView(
    const QString *name) {
  return new QQmlSA::LoggerWarningId(QAnyStringView(*name));
}

//  QAnyStringView QQmlSA::LoggerWarningId::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA15LoggerWarningId4nameEv(
    const QQmlSA::LoggerWarningId *self) {
  return new QString(self->name().toString());
}

//  bool operator==(const LoggerWarningId &a, const LoggerWarningId &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_15LoggerWarningIdES2_(
    const QQmlSA::LoggerWarningId *a,
    const QQmlSA::LoggerWarningId *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const LoggerWarningId &a, const LoggerWarningId &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_15LoggerWarningIdES2_(
    const QQmlSA::LoggerWarningId *a,
    const QQmlSA::LoggerWarningId *b) {
  return operator!=(*a, *b);
}

//  QQmlSA::LoggerWarningId::~LoggerWarningId()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA15LoggerWarningIdD1Ev(QQmlSA::LoggerWarningId *self) {
  delete self;
}
