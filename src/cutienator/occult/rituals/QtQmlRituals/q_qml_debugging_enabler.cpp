//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmldebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#if QT_CONFIG(qml_debug)
#include <QtQml/QtQml>
#include <QtQml/qqmldebug.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  void QQmlDebuggingEnabler::enableDebugging(bool printWarning)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebuggingEnabler15enableDebuggingEb(bool printWarning) {
  QQmlDebuggingEnabler::enableDebugging(printWarning);
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QQmlDebuggingEnabler::QQmlDebuggingEnabler(bool printWarning)
extern "C" Q_DECL_EXPORT
QQmlDebuggingEnabler *ritual_ZN20QQmlDebuggingEnablerC1Eb(
    bool printWarning) {
  return new QQmlDebuggingEnabler(printWarning);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  QStringList QQmlDebuggingEnabler::debuggerServices()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QQmlDebuggingEnabler16debuggerServicesEv() {
  return new QList<QString>(QQmlDebuggingEnabler::debuggerServices());
}

//  QStringList QQmlDebuggingEnabler::inspectorServices()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QQmlDebuggingEnabler17inspectorServicesEv() {
  return new QList<QString>(QQmlDebuggingEnabler::inspectorServices());
}

//  QStringList QQmlDebuggingEnabler::profilerServices()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QQmlDebuggingEnabler16profilerServicesEv() {
  return new QList<QString>(QQmlDebuggingEnabler::profilerServices());
}

//  QStringList QQmlDebuggingEnabler::nativeDebuggerServices()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QQmlDebuggingEnabler22nativeDebuggerServicesEv() {
  return new QList<QString>(QQmlDebuggingEnabler::nativeDebuggerServices());
}

//  void QQmlDebuggingEnabler::setServices(const QStringList &services)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebuggingEnabler11setServicesERK5QListI7QStringE(
    const QList<QString> *services) {
  QQmlDebuggingEnabler::setServices(*services);
}

//  bool QQmlDebuggingEnabler::startTcpDebugServer(int port, StartMode mode,
//      const QString &hostName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebuggingEnabler19startTcpDebugServerEiNS_9StartModeERK7QString(
    int port,
    QQmlDebuggingEnabler::StartMode mode,
    const QString *hostName) {
  return QQmlDebuggingEnabler::startTcpDebugServer(port, mode, *hostName);
}

//  bool QQmlDebuggingEnabler::connectToLocalDebugger(const QString
//      &socketFileName, StartMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebuggingEnabler22connectToLocalDebuggerERK7QStringNS_9StartModeE(
    const QString *socketFileName,
    QQmlDebuggingEnabler::StartMode mode) {
  return QQmlDebuggingEnabler::connectToLocalDebugger(*socketFileName, mode);
}

//  bool QQmlDebuggingEnabler::startDebugConnector(const QString &pluginName,
//      const QVariantHash &configuration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebuggingEnabler19startDebugConnectorERK7QStringRK5QHashIS0_8QVariantE(
    const QString *pluginName,
    const QHash<QString, QVariant> *configuration) {
  return QQmlDebuggingEnabler::startDebugConnector(
      *pluginName,
      *configuration);
}

//  QQmlDebuggingEnabler::~QQmlDebuggingEnabler()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebuggingEnablerD1Ev(QQmlDebuggingEnabler *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
