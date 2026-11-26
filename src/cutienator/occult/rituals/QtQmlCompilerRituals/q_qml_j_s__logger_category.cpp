//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmljsloggingutils.h>

//  LoggerCategoryPrivate *QQmlJS::LoggerCategory::d_func()
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategoryPrivate *ritual_ZN6QQmlJS14LoggerCategory6d_funcEv(
    QQmlJS::LoggerCategory *self) {
  return self->d_func();
}

//  const LoggerCategoryPrivate *QQmlJS::LoggerCategory::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlJS::LoggerCategoryPrivate *ritual_ZNK6QQmlJS14LoggerCategory6d_funcEv(
    const QQmlJS::LoggerCategory *self) {
  return self->d_func();
}

//  QQmlJS::LoggerCategory::LoggerCategory()
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryC1Ev() {
  return new QQmlJS::LoggerCategory();
}

//  QQmlJS::LoggerCategory::LoggerCategory(const QString &name, const QString
//      &settingsName, const QString &description, WarningSeverity severity,
//      Essentiality essentiality)
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryC1ERK7QStringS3_S3_N6QQmlSA15WarningSeverityENS0_12EssentialityE(
    const QString *name,
    const QString *settingsName,
    const QString *description,
    QQmlJS::WarningSeverity severity,
    QQmlJS::LoggerCategory::Essentiality essentiality) {
  return new QQmlJS::LoggerCategory(
      *name,
      *settingsName,
      *description,
      severity,
      essentiality);
}

//  QQmlJS::LoggerCategory::LoggerCategory(const LoggerCategory &a0)
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryC1ERKS0_(
    const QQmlJS::LoggerCategory *a0) {
  return new QQmlJS::LoggerCategory(*a0);
}

//  QQmlJS::LoggerCategory::LoggerCategory(LoggerCategory &&a0)
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryC1EOS0_(
    QQmlJS::LoggerCategory *a0) {
  return new QQmlJS::LoggerCategory(std::move(*a0));
}

//  LoggerCategory &QQmlJS::LoggerCategory::operator=(const LoggerCategory
//      &a0)
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryaSERKS0_(
    QQmlJS::LoggerCategory *self,
    const QQmlJS::LoggerCategory *a0) {
  return &(self->operator=(*a0));
}

//  LoggerCategory &QQmlJS::LoggerCategory::operator=(LoggerCategory &&a0)
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategory *ritual_ZN6QQmlJS14LoggerCategoryaSEOS0_(
    QQmlJS::LoggerCategory *self,
    QQmlJS::LoggerCategory *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlJS::LoggerCategory::~LoggerCategory()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS14LoggerCategoryD1Ev(QQmlJS::LoggerCategory *self) {
  delete self;
}

//  QString QQmlJS::LoggerCategory::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS14LoggerCategory4nameEv(
    const QQmlJS::LoggerCategory *self) {
  return new QString(self->name());
}

//  QString QQmlJS::LoggerCategory::settingsName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS14LoggerCategory12settingsNameEv(
    const QQmlJS::LoggerCategory *self) {
  return new QString(self->settingsName());
}

//  QString QQmlJS::LoggerCategory::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS14LoggerCategory11descriptionEv(
    const QQmlJS::LoggerCategory *self) {
  return new QString(self->description());
}

//  WarningSeverity QQmlJS::LoggerCategory::severity() const
extern "C" Q_DECL_EXPORT
QQmlJS::WarningSeverity ritual_ZNK6QQmlJS14LoggerCategory8severityEv(
    const QQmlJS::LoggerCategory *self) {
  return self->severity();
}

//  bool QQmlJS::LoggerCategory::isEssential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS14LoggerCategory11isEssentialEv(
    const QQmlJS::LoggerCategory *self) {
  return self->isEssential();
}

//  LoggerWarningId QQmlJS::LoggerCategory::id() const
extern "C" Q_DECL_EXPORT
QQmlSA::LoggerWarningId *ritual_ZNK6QQmlJS14LoggerCategory2idEv(
    const QQmlJS::LoggerCategory *self) {
  return new QQmlSA::LoggerWarningId(self->id());
}

//  void QQmlJS::LoggerCategory::setSeverity(WarningSeverity a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS14LoggerCategory11setSeverityEN6QQmlSA15WarningSeverityE(
    QQmlJS::LoggerCategory *self,
    QQmlJS::WarningSeverity a0) {
  self->setSeverity(a0);
}
