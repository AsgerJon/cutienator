//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dtls)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qdtls.h>
#include <cstring>

//  A QTlsPrivate::DtlsBase that Python can take functions over in. Every QTlsPrivate::DtlsBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsBaseCall0)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsBaseCall1)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef QString * (*CuteQTlsPrivate_DtlsBaseCall2)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsBaseCall3)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsBaseCall4)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QSslConfiguration * (*CuteQTlsPrivate_DtlsBaseCall5)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsBaseCall6)(const void *, const QDtlsClientVerifier::GeneratorParameters *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QDtlsClientVerifier::GeneratorParameters * (*CuteQTlsPrivate_DtlsBaseCall7)(const void *, int *);
#endif  // QT_CONFIG(dtls)
class CuteQTlsPrivate_DtlsBase : public QTlsPrivate::DtlsBase {
public:
  using QTlsPrivate::DtlsBase::DtlsBase;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase12setDtlsErrorE10QDtlsErrorRK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase5errorEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase11errorStringEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfiguration")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase13configurationEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN19QDtlsClientVerifier19GeneratorParametersE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
    return false;
  }

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const
  //      QString &description)
  void setDtlsError(QDtlsError code, const QString &description) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall0 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall0>(taken[0]);
      call(this, static_cast<int>(code), &description, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QDtlsError QTlsPrivate::DtlsBase::error() const
  QDtlsError error() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall1 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDtlsError>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QString QTlsPrivate::DtlsBase::errorString() const
  QString errorString() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall2 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::clearDtlsError()
  void clearDtlsError() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall3 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setConfiguration(const QSslConfiguration
  //      &configuration)
  void setConfiguration(const QSslConfiguration &configuration) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall4 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall4>(taken[4]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QSslConfiguration QTlsPrivate::DtlsBase::configuration() const
  QSslConfiguration configuration() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall5 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall5>(taken[5]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsBase::setCookieGeneratorParameters(const
  //      GenParams &params)
  bool setCookieGeneratorParameters(
      const QTlsPrivate::DtlsBase::GenParams &params) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall6 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall6>(taken[6]);
      bool given = call(this, &params, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters() const
  QTlsPrivate::DtlsBase::GenParams cookieGeneratorParameters() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsBaseCall7 call = reinterpret_cast<CuteQTlsPrivate_DtlsBaseCall7>(taken[7]);
      const QDtlsClientVerifier::GeneratorParameters * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)
};

//  QTlsPrivate::DtlsBase::~DtlsBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate8DtlsBaseD1Ev(QTlsPrivate::DtlsBase *self) {
  delete self;
}

//  void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const QString
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate8DtlsBase12setDtlsErrorE10QDtlsErrorRK7QString(
    QTlsPrivate::DtlsBase *self,
    QDtlsError code,
    const QString *description) {
  self->setDtlsError(code, *description);
}

//  QDtlsError QTlsPrivate::DtlsBase::error() const
extern "C" Q_DECL_EXPORT
QDtlsError ritual_ZNK11QTlsPrivate8DtlsBase5errorEv(
    const QTlsPrivate::DtlsBase *self) {
  return self->error();
}

//  QString QTlsPrivate::DtlsBase::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsPrivate8DtlsBase11errorStringEv(
    const QTlsPrivate::DtlsBase *self) {
  return new QString(self->errorString());
}

//  void QTlsPrivate::DtlsBase::clearDtlsError()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv(
    QTlsPrivate::DtlsBase *self) {
  self->clearDtlsError();
}

//  void QTlsPrivate::DtlsBase::setConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfiguration(
    QTlsPrivate::DtlsBase *self,
    const QSslConfiguration *configuration) {
  self->setConfiguration(*configuration);
}

//  QSslConfiguration QTlsPrivate::DtlsBase::configuration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK11QTlsPrivate8DtlsBase13configurationEv(
    const QTlsPrivate::DtlsBase *self) {
  return new QSslConfiguration(self->configuration());
}

//  bool QTlsPrivate::DtlsBase::setCookieGeneratorParameters(const GenParams
//      &params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN19QDtlsClientVerifier19GeneratorParametersE(
    QTlsPrivate::DtlsBase *self,
    const QDtlsClientVerifier::GeneratorParameters *params) {
  return self->setCookieGeneratorParameters(*params);
}

//  GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters() const
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier::GeneratorParameters *ritual_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv(
    const QTlsPrivate::DtlsBase *self) {
  return new QDtlsClientVerifier::GeneratorParameters(
      self->cookieGeneratorParameters());
}

//  a Python function taken by a CuteQTlsPrivate_DtlsBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_DtlsBase(
    QTlsPrivate::DtlsBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_DtlsBase *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dtls)
