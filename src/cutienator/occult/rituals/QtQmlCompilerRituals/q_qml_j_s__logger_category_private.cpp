//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: the rituals of the two friend
//  functions 'operator==' and 'operator!=' of two
//  'LoggerCategoryPrivate' are taken out, with their rows: they call
//  'operatorEqualsImpl', which Qt declares but its library does not
//  offer (undefined reference). Kept as it is when the generator runs
//  again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmljsloggingutils.h>
#include <QtCore/qstring.h>

//  QQmlJS::LoggerCategoryPrivate::LoggerCategoryPrivate()
extern "C" Q_DECL_EXPORT
QQmlJS::LoggerCategoryPrivate *ritual_ZN6QQmlJS21LoggerCategoryPrivateC1Ev() {
  return new QQmlJS::LoggerCategoryPrivate();
}

//  LoggerWarningId QQmlJS::LoggerCategoryPrivate::id() const
extern "C" Q_DECL_EXPORT
QQmlSA::LoggerWarningId *ritual_ZNK6QQmlJS21LoggerCategoryPrivate2idEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return new QQmlSA::LoggerWarningId(self->id());
}

//  QString QQmlJS::LoggerCategoryPrivate::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS21LoggerCategoryPrivate4nameEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return new QString(self->name());
}

//  QString QQmlJS::LoggerCategoryPrivate::settingsName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS21LoggerCategoryPrivate12settingsNameEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return new QString(self->settingsName());
}

//  QString QQmlJS::LoggerCategoryPrivate::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS21LoggerCategoryPrivate11descriptionEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return new QString(self->description());
}

//  bool QQmlJS::LoggerCategoryPrivate::isEssential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS21LoggerCategoryPrivate11isEssentialEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return self->isEssential();
}

//  WarningSeverity QQmlJS::LoggerCategoryPrivate::severity() const
extern "C" Q_DECL_EXPORT
QQmlJS::WarningSeverity ritual_ZNK6QQmlJS21LoggerCategoryPrivate8severityEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return self->severity();
}

//  bool QQmlJS::LoggerCategoryPrivate::hasChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS21LoggerCategoryPrivate10hasChangedEv(
    const QQmlJS::LoggerCategoryPrivate *self) {
  return self->hasChanged();
}

//  bool QQmlJS::LoggerCategoryPrivate::operator==(const LoggerWarningId
//      warningId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS21LoggerCategoryPrivateeqEN6QQmlSA15LoggerWarningIdE(
    const QQmlJS::LoggerCategoryPrivate *self,
    const QQmlSA::LoggerWarningId *warningId) {
  return self->operator==(*warningId);
}

//  QQmlJS::LoggerCategoryPrivate::~LoggerCategoryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS21LoggerCategoryPrivateD1Ev(
    QQmlJS::LoggerCategoryPrivate *self) {
  delete self;
}
