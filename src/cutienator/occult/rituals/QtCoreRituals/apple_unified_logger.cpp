//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  An 'os_log_t' is passed as an address.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN) && !defined(QT_BOOTSTRAPPED)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>
#include <QtCore/qstring.h>

//  bool AppleUnifiedLogger::messageHandler(QtMsgType msgType, const
//      QMessageLogContext &context, const QString &message)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18AppleUnifiedLogger14messageHandlerE9QtMsgTypeRK18QMessageLogContextRK7QString(
    QtMsgType msgType,
    const QMessageLogContext *context,
    const QString *message) {
  return AppleUnifiedLogger::messageHandler(msgType, *context, *message);
}

//  bool AppleUnifiedLogger::messageHandler(QtMsgType msgType, const
//      QMessageLogContext &context, const QString &message, const QString
//      &subsystem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18AppleUnifiedLogger14messageHandlerE9QtMsgTypeRK18QMessageLogContextRK7QStringS6_(
    QtMsgType msgType,
    const QMessageLogContext *context,
    const QString *message,
    const QString *subsystem) {
  return AppleUnifiedLogger::messageHandler(msgType, *context, *message, *subsystem);
}

//  bool AppleUnifiedLogger::preventsStderrLogging()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18AppleUnifiedLogger21preventsStderrLoggingEv() {
  return AppleUnifiedLogger::preventsStderrLogging();
}

//  os_log_type_t AppleUnifiedLogger::logTypeForMessageType(QtMsgType
//      msgType)
extern "C" Q_DECL_EXPORT
os_log_type_t ritual_ZN18AppleUnifiedLogger21logTypeForMessageTypeE9QtMsgType(
    QtMsgType msgType) {
  return AppleUnifiedLogger::logTypeForMessageType(msgType);
}

//  os_log_t AppleUnifiedLogger::cachedLog(const QString &subsystem, const
//      QString &category)
extern "C" Q_DECL_EXPORT
os_log_t ritual_ZN18AppleUnifiedLogger9cachedLogERK7QStringS2_(
    const QString *subsystem,
    const QString *category) {
  return AppleUnifiedLogger::cachedLog(*subsystem, *category);
}

//  AppleUnifiedLogger::~AppleUnifiedLogger()
extern "C" Q_DECL_EXPORT
void ritual_ZN18AppleUnifiedLoggerD1Ev(AppleUnifiedLogger *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN) && !defined(QT_BOOTSTRAPPED)
