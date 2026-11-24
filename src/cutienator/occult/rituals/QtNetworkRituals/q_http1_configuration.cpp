//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttp1configuration.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/qhttp1configuration.h>

//  QHttp1Configuration::QHttp1Configuration()
extern "C" Q_DECL_EXPORT
QHttp1Configuration *ritual_ZN19QHttp1ConfigurationC1Ev() {
  return new QHttp1Configuration();
}

//  QHttp1Configuration::QHttp1Configuration(const QHttp1Configuration
//      &other)
extern "C" Q_DECL_EXPORT
QHttp1Configuration *ritual_ZN19QHttp1ConfigurationC1ERKS_(
    const QHttp1Configuration *other) {
  return new QHttp1Configuration(*other);
}

//  QHttp1Configuration::~QHttp1Configuration()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp1ConfigurationD1Ev(QHttp1Configuration *self) {
  delete self;
}

//  void QHttp1Configuration::setNumberOfConnectionsPerHost(qsizetype amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp1Configuration29setNumberOfConnectionsPerHostEx(
    QHttp1Configuration *self,
    qsizetype amount) {
  self->setNumberOfConnectionsPerHost(amount);
}

//  qsizetype QHttp1Configuration::numberOfConnectionsPerHost() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QHttp1Configuration26numberOfConnectionsPerHostEv(
    const QHttp1Configuration *self) {
  return self->numberOfConnectionsPerHost();
}

//  bool QHttp1Configuration::equals(const QHttp1Configuration &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttp1Configuration6equalsERKS_(
    const QHttp1Configuration *self,
    const QHttp1Configuration *other) {
  return self->equals(*other);
}

//  bool operator==(const QHttp1Configuration &lhs, const QHttp1Configuration
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QHttp1ConfigurationS1_(
    const QHttp1Configuration *lhs,
    const QHttp1Configuration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHttp1Configuration &lhs, const QHttp1Configuration
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QHttp1ConfigurationS1_(
    const QHttp1Configuration *lhs,
    const QHttp1Configuration *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
