//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkinformation.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkinformation.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QNetworkInformation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QNetworkInformation10metaObjectEv(
    const QNetworkInformation *self) {
  return self->metaObject();
}

//  QString QNetworkInformation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QNetworkInformation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkInformation::tr(s, c, n));
}

//  Reachability QNetworkInformation::reachability() const
extern "C" Q_DECL_EXPORT
QNetworkInformation::Reachability ritual_ZNK19QNetworkInformation12reachabilityEv(
    const QNetworkInformation *self) {
  return self->reachability();
}

//  bool QNetworkInformation::isBehindCaptivePortal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNetworkInformation21isBehindCaptivePortalEv(
    const QNetworkInformation *self) {
  return self->isBehindCaptivePortal();
}

//  TransportMedium QNetworkInformation::transportMedium() const
extern "C" Q_DECL_EXPORT
QNetworkInformation::TransportMedium ritual_ZNK19QNetworkInformation15transportMediumEv(
    const QNetworkInformation *self) {
  return self->transportMedium();
}

//  bool QNetworkInformation::isMetered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNetworkInformation9isMeteredEv(
    const QNetworkInformation *self) {
  return self->isMetered();
}

//  QString QNetworkInformation::backendName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QNetworkInformation11backendNameEv(
    const QNetworkInformation *self) {
  return new QString(self->backendName());
}

//  bool QNetworkInformation::supports(Features features) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNetworkInformation8supportsE6QFlagsINS_7FeatureEE(
    const QNetworkInformation *self,
    int features) {
  return self->supports(
      QFlags<QNetworkInformation::Feature>::fromInt(features));
}

//  Features QNetworkInformation::supportedFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QNetworkInformation17supportedFeaturesEv(
    const QNetworkInformation *self) {
  return static_cast<int>(self->supportedFeatures().toInt());
}

//  bool QNetworkInformation::loadDefaultBackend()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNetworkInformation18loadDefaultBackendEv() {
  return QNetworkInformation::loadDefaultBackend();
}

//  bool QNetworkInformation::loadBackendByName(QStringView backend)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNetworkInformation17loadBackendByNameE11QStringView(
    const QString *backend) {
  return QNetworkInformation::loadBackendByName(QStringView(*backend));
}

//  bool QNetworkInformation::loadBackendByFeatures(Features features)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNetworkInformation21loadBackendByFeaturesE6QFlagsINS_7FeatureEE(
    int features) {
  return QNetworkInformation::loadBackendByFeatures(
      QFlags<QNetworkInformation::Feature>::fromInt(features));
}

#if QT_DEPRECATED_SINCE(6,4)
//  bool QNetworkInformation::load(QStringView backend)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNetworkInformation4loadE11QStringView(
    const QString *backend) {
  return QNetworkInformation::load(QStringView(*backend));
}
#endif  // QT_DEPRECATED_SINCE(6,4)

#if QT_DEPRECATED_SINCE(6,4)
//  bool QNetworkInformation::load(Features features)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNetworkInformation4loadE6QFlagsINS_7FeatureEE(
    int features) {
  return QNetworkInformation::load(
      QFlags<QNetworkInformation::Feature>::fromInt(features));
}
#endif  // QT_DEPRECATED_SINCE(6,4)

//  QStringList QNetworkInformation::availableBackends()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QNetworkInformation17availableBackendsEv() {
  return new QList<QString>(QNetworkInformation::availableBackends());
}

//  QNetworkInformation *QNetworkInformation::instance()
extern "C" Q_DECL_EXPORT
QNetworkInformation *ritual_ZN19QNetworkInformation8instanceEv() {
  return QNetworkInformation::instance();
}

//  QNetworkInformation::QNetworkInformation(QNetworkInformationBackend
//      *backend)
extern "C" Q_DECL_EXPORT
QNetworkInformation *ritual_ZN19QNetworkInformationC1EP26QNetworkInformationBackend(
    QNetworkInformationBackend *backend) {
  return new QNetworkInformation(backend);
}

//  QNetworkInformation::~QNetworkInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNetworkInformationD1Ev(QNetworkInformation *self) {
  delete self;
}
