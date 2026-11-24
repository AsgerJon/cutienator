//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmljsloggingutils.h>
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlJSLogger::registerCategory(const QQmlJS::LoggerCategory
//      &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger16registerCategoryERKN6QQmlJS14LoggerCategoryE(
    QQmlJSLogger *self,
    const QQmlJS::LoggerCategory *category) {
  self->registerCategory(*category);
}

//  QQmlJSLogger::QQmlJSLogger()
extern "C" Q_DECL_EXPORT
QQmlJSLogger *ritual_ZN12QQmlJSLoggerC1Ev() {
  return new QQmlJSLogger();
}

//  QQmlJSLogger::~QQmlJSLogger()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLoggerD1Ev(QQmlJSLogger *self) {
  delete self;
}

//  bool QQmlJSLogger::hasWarnings() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger11hasWarningsEv(const QQmlJSLogger *self) {
  return self->hasWarnings();
}

//  bool QQmlJSLogger::hasErrors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger9hasErrorsEv(const QQmlJSLogger *self) {
  return self->hasErrors();
}

//  qsizetype QQmlJSLogger::numWarnings() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QQmlJSLogger11numWarningsEv(const QQmlJSLogger *self) {
  return self->numWarnings();
}

//  qsizetype QQmlJSLogger::numErrors() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QQmlJSLogger9numErrorsEv(const QQmlJSLogger *self) {
  return self->numErrors();
}

//  QQmlJS::WarningSeverity
//      QQmlJSLogger::categorySeverity(QQmlJS::LoggerWarningId id) const
extern "C" Q_DECL_EXPORT
QQmlJS::WarningSeverity ritual_ZNK12QQmlJSLogger16categorySeverityEN6QQmlSA15LoggerWarningIdE(
    const QQmlJSLogger *self,
    const QQmlSA::LoggerWarningId *id) {
  return self->categorySeverity(*id);
}

//  void QQmlJSLogger::setCategorySeverity(QQmlJS::LoggerWarningId id,
//      QQmlJS::WarningSeverity severity)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger19setCategorySeverityEN6QQmlSA15LoggerWarningIdENS0_15WarningSeverityE(
    QQmlJSLogger *self,
    const QQmlSA::LoggerWarningId *id,
    QQmlJS::WarningSeverity severity) {
  self->setCategorySeverity(*id, severity);
}

//  bool QQmlJSLogger::wasCategoryChanged(QQmlJS::LoggerWarningId id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger18wasCategoryChangedEN6QQmlSA15LoggerWarningIdE(
    const QQmlJSLogger *self,
    const QQmlSA::LoggerWarningId *id) {
  return self->wasCategoryChanged(*id);
}

//  QQmlJS::WarningSeverity QQmlJSLogger::compileErrorSeverity() const
extern "C" Q_DECL_EXPORT
QQmlJS::WarningSeverity ritual_ZNK12QQmlJSLogger20compileErrorSeverityEv(
    const QQmlJSLogger *self) {
  return self->compileErrorSeverity();
}

//  void QQmlJSLogger::setCompileErrorSeverity(QQmlJS::WarningSeverity
//      severity)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger23setCompileErrorSeverityEN6QQmlSA15WarningSeverityE(
    QQmlJSLogger *self,
    QQmlJS::WarningSeverity severity) {
  self->setCompileErrorSeverity(severity);
}

//  QString QQmlJSLogger::compileErrorPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger18compileErrorPrefixEv(
    const QQmlJSLogger *self) {
  return new QString(self->compileErrorPrefix());
}

//  void QQmlJSLogger::setCompileErrorPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger21setCompileErrorPrefixERK7QString(
    QQmlJSLogger *self,
    const QString *prefix) {
  self->setCompileErrorPrefix(*prefix);
}

//  QString QQmlJSLogger::compileSkipPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger17compileSkipPrefixEv(
    const QQmlJSLogger *self) {
  return new QString(self->compileSkipPrefix());
}

//  void QQmlJSLogger::setCompileSkipPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger20setCompileSkipPrefixERK7QString(
    QQmlJSLogger *self,
    const QString *prefix) {
  self->setCompileSkipPrefix(*prefix);
}

//  void QQmlJSLogger::logCompileError(const QString &message, const
//      QQmlJS::SourceLocation &srcLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger15logCompileErrorERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSLogger *self,
    const QString *message,
    const QQmlJS::SourceLocation *srcLocation) {
  self->logCompileError(*message, *srcLocation);
}

//  void QQmlJSLogger::logCompileSkip(const QString &message, const
//      QQmlJS::SourceLocation &srcLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger14logCompileSkipERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSLogger *self,
    const QString *message,
    const QQmlJS::SourceLocation *srcLocation) {
  self->logCompileSkip(*message, *srcLocation);
}

//  void QQmlJSLogger::setSilent(bool silent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger9setSilentEb(QQmlJSLogger *self, bool silent) {
  self->setSilent(silent);
}

//  bool QQmlJSLogger::isSilent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger8isSilentEv(const QQmlJSLogger *self) {
  return self->isSilent();
}

//  void QQmlJSLogger::setManualFlush(bool manualFlush)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger14setManualFlushEb(
    QQmlJSLogger *self,
    bool manualFlush) {
  self->setManualFlush(manualFlush);
}

//  bool QQmlJSLogger::hasManualFlush() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger14hasManualFlushEv(const QQmlJSLogger *self) {
  return self->hasManualFlush();
}

//  void QQmlJSLogger::manualFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger11manualFlushEv(QQmlJSLogger *self) {
  self->manualFlush();
}

//  void QQmlJSLogger::setIsDisabled(bool isDisabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger13setIsDisabledEb(
    QQmlJSLogger *self,
    bool isDisabled) {
  self->setIsDisabled(isDisabled);
}

//  bool QQmlJSLogger::isDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger10isDisabledEv(const QQmlJSLogger *self) {
  return self->isDisabled();
}

//  void QQmlJSLogger::setCode(const QString &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger7setCodeERK7QString(
    QQmlJSLogger *self,
    const QString *code) {
  self->setCode(*code);
}

//  QString QQmlJSLogger::code() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger4codeEv(const QQmlJSLogger *self) {
  return new QString(self->code());
}

//  void QQmlJSLogger::setFilePath(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger11setFilePathERK7QString(
    QQmlJSLogger *self,
    const QString *filePath) {
  self->setFilePath(*filePath);
}

//  QString QQmlJSLogger::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger8filePathEv(const QQmlJSLogger *self) {
  return new QString(self->filePath());
}

//  bool QQmlJSLogger::currentFunctionHasCompileError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger30currentFunctionHasCompileErrorEv(
    const QQmlJSLogger *self) {
  return self->currentFunctionHasCompileError();
}

//  bool QQmlJSLogger::currentFunctionWasSkipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger25currentFunctionWasSkippedEv(
    const QQmlJSLogger *self) {
  return self->currentFunctionWasSkipped();
}

//  bool QQmlJSLogger::currentFunctionHasErrorOrSkip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlJSLogger29currentFunctionHasErrorOrSkipEv(
    const QQmlJSLogger *self) {
  return self->currentFunctionHasErrorOrSkip();
}

//  QString QQmlJSLogger::currentFunctionCompileErrorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger34currentFunctionCompileErrorMessageEv(
    const QQmlJSLogger *self) {
  return new QString(self->currentFunctionCompileErrorMessage());
}

//  QString QQmlJSLogger::currentFunctionCompileSkipMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlJSLogger33currentFunctionCompileSkipMessageEv(
    const QQmlJSLogger *self) {
  return new QString(self->currentFunctionCompileSkipMessage());
}

//  void QQmlJSLogger::startTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger16startTransactionEv(QQmlJSLogger *self) {
  self->startTransaction();
}

//  void QQmlJSLogger::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger6commitEv(QQmlJSLogger *self) {
  self->commit();
}

//  void QQmlJSLogger::rollback()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger8rollbackEv(QQmlJSLogger *self) {
  self->rollback();
}

//  void QQmlJSLogger::finalizeFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger16finalizeFunctionEv(QQmlJSLogger *self) {
  self->finalizeFunction();
}

//  void QQmlJSLogger::printContext(const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger12printContextERKN6QQmlJS14SourceLocationE(
    QQmlJSLogger *self,
    const QQmlJS::SourceLocation *location) {
  self->printContext(*location);
}

//  void QQmlJSLogger::printFix(const QQmlJSFixSuggestion &fix)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger8printFixERK19QQmlJSFixSuggestion(
    QQmlJSLogger *self,
    const QQmlJSFixSuggestion *fix) {
  self->printFix(*fix);
}

//  void QQmlJSLogger::countMessage(const Message &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlJSLogger12countMessageERK7Message(
    QQmlJSLogger *self,
    const Message *message) {
  self->countMessage(*message);
}
