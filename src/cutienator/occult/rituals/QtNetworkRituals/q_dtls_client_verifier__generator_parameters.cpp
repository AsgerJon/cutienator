//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdtls.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dtls) && QT_CONFIG(ssl)
#if QT_CONFIG(dtls)
#include <QtNetwork/qdtls.h>
#include <QtCore/qbytearray.h>

//  QDtlsClientVerifier::GeneratorParameters::GeneratorParameters()
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier::GeneratorParameters *ritual_ZN19QDtlsClientVerifier19GeneratorParametersC1Ev() {
  return new QDtlsClientVerifier::GeneratorParameters();
}

//  QDtlsClientVerifier::GeneratorParameters::GeneratorParameters(QCryptograp
//      hicHash::Algorithm a, const QByteArray &s)
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier::GeneratorParameters *ritual_ZN19QDtlsClientVerifier19GeneratorParametersC1EN18QCryptographicHash9AlgorithmERK10QByteArray(
    QCryptographicHash::Algorithm a,
    const QByteArray *s) {
  return new QDtlsClientVerifier::GeneratorParameters(a, *s);
}

//  QDtlsClientVerifier::GeneratorParameters::~GeneratorParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDtlsClientVerifier19GeneratorParametersD1Ev(
    QDtlsClientVerifier::GeneratorParameters *self) {
  delete self;
}

#endif  // QT_CONFIG(dtls)
#endif  // QT_CONFIG(dtls) && QT_CONFIG(ssl)
