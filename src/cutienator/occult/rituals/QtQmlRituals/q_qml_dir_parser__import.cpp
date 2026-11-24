//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>

//  QQmlDirParser::Import::Import()
extern "C" Q_DECL_EXPORT
QQmlDirParser::Import *ritual_ZN13QQmlDirParser6ImportC1Ev() {
  return new QQmlDirParser::Import();
}

//  QQmlDirParser::Import::Import(QString module, QTypeRevision version,
//      Flags flags)
extern "C" Q_DECL_EXPORT
QQmlDirParser::Import *ritual_ZN13QQmlDirParser6ImportC1E7QString13QTypeRevision6QFlagsINS0_4FlagEE(
    const QString *module,
    const QTypeRevision *version,
    int flags) {
  return new QQmlDirParser::Import(
      *module,
      *version,
      QFlags<QQmlDirParser::Import::Flag>::fromInt(flags));
}

//  bool operator==(const Import &lhs, const Import &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN13QQmlDirParser6ImportES2_(
    const QQmlDirParser::Import *lhs,
    const QQmlDirParser::Import *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Import &lhs, const Import &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN13QQmlDirParser6ImportES2_(
    const QQmlDirParser::Import *lhs,
    const QQmlDirParser::Import *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QQmlDirParser::Import::~Import()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser6ImportD1Ev(QQmlDirParser::Import *self) {
  delete self;
}
