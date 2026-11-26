//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  AotStats *QQmlJS::QQmlJSAotCompilerStats::instance()
extern "C" Q_DECL_EXPORT
QQmlJS::AotStats *ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8instanceEv() {
  return QQmlJS::QQmlJSAotCompilerStats::instance();
}

//  bool QQmlJS::QQmlJSAotCompilerStats::recordAotStats()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS22QQmlJSAotCompilerStats14recordAotStatsEv() {
  return QQmlJS::QQmlJSAotCompilerStats::recordAotStats();
}

//  void QQmlJS::QQmlJSAotCompilerStats::setRecordAotStats(bool
//      recordAotStats)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS22QQmlJSAotCompilerStats17setRecordAotStatsEb(
    bool recordAotStats) {
  QQmlJS::QQmlJSAotCompilerStats::setRecordAotStats(recordAotStats);
}

//  QString QQmlJS::QQmlJSAotCompilerStats::moduleId()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8moduleIdEv() {
  return new QString(QQmlJS::QQmlJSAotCompilerStats::moduleId());
}

//  void QQmlJS::QQmlJSAotCompilerStats::setModuleId(const QString &moduleId)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS22QQmlJSAotCompilerStats11setModuleIdERK7QString(
    const QString *moduleId) {
  QQmlJS::QQmlJSAotCompilerStats::setModuleId(*moduleId);
}

//  void QQmlJS::QQmlJSAotCompilerStats::registerFile(const QString
//      &filepath)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS22QQmlJSAotCompilerStats12registerFileERK7QString(
    const QString *filepath) {
  QQmlJS::QQmlJSAotCompilerStats::registerFile(*filepath);
}

//  void QQmlJS::QQmlJSAotCompilerStats::addEntry(const QString &filepath,
//      const QQmlJS::AotStatsEntry &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8addEntryERK7QStringRKNS_13AotStatsEntryE(
    const QString *filepath,
    const QQmlJS::AotStatsEntry *entry) {
  QQmlJS::QQmlJSAotCompilerStats::addEntry(*filepath, *entry);
}

//  QQmlJS::QQmlJSAotCompilerStats::~QQmlJSAotCompilerStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS22QQmlJSAotCompilerStatsD1Ev(
    QQmlJS::QQmlJSAotCompilerStats *self) {
  delete self;
}
