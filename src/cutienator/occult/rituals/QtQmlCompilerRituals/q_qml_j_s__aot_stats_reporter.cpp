//  Written by dev_tooling.RitualGenerator from the records of QtQmlCompiler/
//  6.12.0/QtQmlCompiler/private/qqmljscompilerstatsreporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstatsreporter_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QQmlJS::AotStatsReporter::AotStatsReporter(const QQmlJS::AotStats &stats,
//      const QStringList &emptyModules, const QStringList
//      &onlyBytecodeModules)
extern "C" Q_DECL_EXPORT
QQmlJS::AotStatsReporter *ritual_ZN6QQmlJS16AotStatsReporterC1ERKNS_8AotStatsERK5QListI7QStringES8_(
    const QQmlJS::AotStats *stats,
    const QList<QString> *emptyModules,
    const QList<QString> *onlyBytecodeModules) {
  return new QQmlJS::AotStatsReporter(
      *stats,
      *emptyModules,
      *onlyBytecodeModules);
}

//  QString QQmlJS::AotStatsReporter::format() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS16AotStatsReporter6formatEv(
    const QQmlJS::AotStatsReporter *self) {
  return new QString(self->format());
}

//  void QQmlJS::AotStatsReporter::formatDetailedStats(QTextStream &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QQmlJS16AotStatsReporter19formatDetailedStatsER11QTextStream(
    const QQmlJS::AotStatsReporter *self,
    QTextStream *a0) {
  self->formatDetailedStats(*a0);
}

//  void QQmlJS::AotStatsReporter::formatSummary(QTextStream &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QQmlJS16AotStatsReporter13formatSummaryER11QTextStream(
    const QQmlJS::AotStatsReporter *self,
    QTextStream *a0) {
  self->formatSummary(*a0);
}

//  QString QQmlJS::AotStatsReporter::formatSuccessRate(int codegens, int
//      successes, int skips) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS16AotStatsReporter17formatSuccessRateEiii(
    const QQmlJS::AotStatsReporter *self,
    int codegens,
    int successes,
    int skips) {
  return new QString(self->formatSuccessRate(codegens, successes, skips));
}

//  QQmlJS::AotStatsReporter::~AotStatsReporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS16AotStatsReporterD1Ev(QQmlJS::AotStatsReporter *self) {
  delete self;
}
