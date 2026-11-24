//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaconnectionsettings.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuaconnectionsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpcUaConnectionSettings::QOpcUaConnectionSettings()
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZN24QOpcUaConnectionSettingsC1Ev() {
  return new QOpcUaConnectionSettings();
}

//  QOpcUaConnectionSettings::QOpcUaConnectionSettings(const
//      QOpcUaConnectionSettings &other)
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZN24QOpcUaConnectionSettingsC1ERKS_(
    const QOpcUaConnectionSettings *other) {
  return new QOpcUaConnectionSettings(*other);
}

//  QOpcUaConnectionSettings::~QOpcUaConnectionSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettingsD1Ev(
    QOpcUaConnectionSettings *self) {
  delete self;
}

//  QStringList QOpcUaConnectionSettings::sessionLocaleIds() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK24QOpcUaConnectionSettings16sessionLocaleIdsEv(
    const QOpcUaConnectionSettings *self) {
  return new QList<QString>(self->sessionLocaleIds());
}

//  void QOpcUaConnectionSettings::setSessionLocaleIds(const QStringList
//      &localeIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings19setSessionLocaleIdsERK5QListI7QStringE(
    QOpcUaConnectionSettings *self,
    const QList<QString> *localeIds) {
  self->setSessionLocaleIds(*localeIds);
}

//  bool operator==(const QOpcUaConnectionSettings &lhs, const
//      QOpcUaConnectionSettings &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QOpcUaConnectionSettingsS1_(
    const QOpcUaConnectionSettings *lhs,
    const QOpcUaConnectionSettings *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaConnectionSettings &lhs, const
//      QOpcUaConnectionSettings &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QOpcUaConnectionSettingsS1_(
    const QOpcUaConnectionSettings *lhs,
    const QOpcUaConnectionSettings *rhs) {
  return operator!=(*lhs, *rhs);
}
