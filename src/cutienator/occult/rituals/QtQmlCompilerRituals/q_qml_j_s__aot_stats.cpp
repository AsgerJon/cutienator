//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsondocument.h>
#include <optional>
#include <QtCore/QStringList>
#include <QtCore/QString>
#include <QtCore/QJsonDocument>

//  const QHash<QString, QHash<QString, QList<AotStatsEntry>>>
//      &QQmlJS::AotStats::entries() const
extern "C" Q_DECL_EXPORT
const QHash<QString, QHash<QString, QList<QQmlJS::AotStatsEntry>>> *ritual_ZNK6QQmlJS8AotStats7entriesEv(
    const QQmlJS::AotStats *self) {
  return &(self->entries());
}

//  void QQmlJS::AotStats::registerFile(const QString &moduleId, const
//      QString &filepath)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS8AotStats12registerFileERK7QStringS3_(
    QQmlJS::AotStats *self,
    const QString *moduleId,
    const QString *filepath) {
  self->registerFile(*moduleId, *filepath);
}

//  void QQmlJS::AotStats::addEntry(const QString &moduleId, const QString
//      &filepath, const AotStatsEntry &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS8AotStats8addEntryERK7QStringS3_RKNS_13AotStatsEntryE(
    QQmlJS::AotStats *self,
    const QString *moduleId,
    const QString *filepath,
    const QQmlJS::AotStatsEntry *entry) {
  self->addEntry(*moduleId, *filepath, *entry);
}

//  void QQmlJS::AotStats::insert(const AotStats &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS8AotStats6insertERKS0_(
    QQmlJS::AotStats *self,
    const QQmlJS::AotStats *other) {
  self->insert(*other);
}

//  std::optional<QStringList> QQmlJS::AotStats::readAllLines(const QString
//      &path)
extern "C" Q_DECL_EXPORT
std::optional<QStringList> *ritual_ZN6QQmlJS8AotStats12readAllLinesERK7QString(
    const QString *path) {
  return new std::optional<QStringList>(
      QQmlJS::AotStats::readAllLines(
          *path));
}

//  bool QQmlJS::AotStats::saveToDisk(const QString &filepath) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS8AotStats10saveToDiskERK7QString(
    const QQmlJS::AotStats *self,
    const QString *filepath) {
  return self->saveToDisk(*filepath);
}

//  std::optional<AotStats> QQmlJS::AotStats::parseAotstatsFile(const QString
//      &aotstatsPath)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJS::AotStats> *ritual_ZN6QQmlJS8AotStats17parseAotstatsFileERK7QString(
    const QString *aotstatsPath) {
  return new std::optional<QQmlJS::AotStats>(
      QQmlJS::AotStats::parseAotstatsFile(
          *aotstatsPath));
}

//  std::optional<AotStats> QQmlJS::AotStats::aggregateAotstatsList(const
//      QString &aotstatsListPath)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJS::AotStats> *ritual_ZN6QQmlJS8AotStats21aggregateAotstatsListERK7QString(
    const QString *aotstatsListPath) {
  return new std::optional<QQmlJS::AotStats>(
      QQmlJS::AotStats::aggregateAotstatsList(
          *aotstatsListPath));
}

//  std::optional<AotStats> QQmlJS::AotStats::fromJsonDocument(const
//      QJsonDocument &a0)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJS::AotStats> *ritual_ZN6QQmlJS8AotStats16fromJsonDocumentERK13QJsonDocument(
    const QJsonDocument *a0) {
  return new std::optional<QQmlJS::AotStats>(
      QQmlJS::AotStats::fromJsonDocument(
          *a0));
}

//  QJsonDocument QQmlJS::AotStats::toJsonDocument() const
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZNK6QQmlJS8AotStats14toJsonDocumentEv(
    const QQmlJS::AotStats *self) {
  return new QJsonDocument(self->toJsonDocument());
}

//  QQmlJS::AotStats::~AotStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS8AotStatsD1Ev(QQmlJS::AotStats *self) {
  delete self;
}

//  a std::optional<QStringList> a ritual of QQmlJS::AotStats gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJS_AotStats__std_optional_QStringList(
    std::optional<QStringList> *self) {
  delete self;
}

//  a std::optional<QQmlJS::AotStats> a ritual of QQmlJS::AotStats gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJS_AotStats__std_optional_QQmlJS_AotStats(
    std::optional<QQmlJS::AotStats> *self) {
  delete self;
}
