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

//  QOpcUaConnectionSettings &QOpcUaConnectionSettings::operator=(const
//      QOpcUaConnectionSettings &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZN24QOpcUaConnectionSettingsaSERKS_(
    QOpcUaConnectionSettings *self,
    const QOpcUaConnectionSettings *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaConnectionSettings::QOpcUaConnectionSettings(QOpcUaConnectionSettin
//      gs &&other)
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZN24QOpcUaConnectionSettingsC1EOS_(
    QOpcUaConnectionSettings *other) {
  return new QOpcUaConnectionSettings(std::move(*other));
}

//  QOpcUaConnectionSettings
//      &QOpcUaConnectionSettings::operator=(QOpcUaConnectionSettings
//      &&other)
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZN24QOpcUaConnectionSettingsaSEOS_(
    QOpcUaConnectionSettings *self,
    QOpcUaConnectionSettings *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpcUaConnectionSettings::~QOpcUaConnectionSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettingsD1Ev(
    QOpcUaConnectionSettings *self) {
  delete self;
}

//  void QOpcUaConnectionSettings::swap(QOpcUaConnectionSettings &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings4swapERS_(
    QOpcUaConnectionSettings *self,
    QOpcUaConnectionSettings *other) {
  self->swap(*other);
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

//  std::chrono::milliseconds
//      QOpcUaConnectionSettings::secureChannelLifeTime() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK24QOpcUaConnectionSettings21secureChannelLifeTimeEv(
    const QOpcUaConnectionSettings *self) {
  return static_cast<long long>(self->secureChannelLifeTime().count());
}

//  void QOpcUaConnectionSettings::setSecureChannelLifeTime(std::chrono::mill
//      iseconds lifeTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings24setSecureChannelLifeTimeENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QOpcUaConnectionSettings *self,
    long long lifeTime) {
  self->setSecureChannelLifeTime(std::chrono::milliseconds(lifeTime));
}

//  std::chrono::milliseconds QOpcUaConnectionSettings::sessionTimeout()
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK24QOpcUaConnectionSettings14sessionTimeoutEv(
    const QOpcUaConnectionSettings *self) {
  return static_cast<long long>(self->sessionTimeout().count());
}

//  void
//      QOpcUaConnectionSettings::setSessionTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings17setSessionTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QOpcUaConnectionSettings *self,
    long long timeout) {
  self->setSessionTimeout(std::chrono::milliseconds(timeout));
}

//  std::chrono::milliseconds QOpcUaConnectionSettings::requestTimeout()
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK24QOpcUaConnectionSettings14requestTimeoutEv(
    const QOpcUaConnectionSettings *self) {
  return static_cast<long long>(self->requestTimeout().count());
}

//  void
//      QOpcUaConnectionSettings::setRequestTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings17setRequestTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QOpcUaConnectionSettings *self,
    long long timeout) {
  self->setRequestTimeout(std::chrono::milliseconds(timeout));
}

//  std::chrono::milliseconds QOpcUaConnectionSettings::connectTimeout()
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK24QOpcUaConnectionSettings14connectTimeoutEv(
    const QOpcUaConnectionSettings *self) {
  return static_cast<long long>(self->connectTimeout().count());
}

//  void
//      QOpcUaConnectionSettings::setConnectTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaConnectionSettings17setConnectTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QOpcUaConnectionSettings *self,
    long long timeout) {
  self->setConnectTimeout(std::chrono::milliseconds(timeout));
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
