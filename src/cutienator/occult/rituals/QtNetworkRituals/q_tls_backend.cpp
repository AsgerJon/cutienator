//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslkey.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtNetwork/QSsl>
#include <QtCore/QString>

//  A QTlsBackend that Python can take functions over in. Every QTlsBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTlsBackendCall0)(const void *, int *);
typedef long (*CuteQTlsBackendCall1)(const void *, int *);
typedef QString * (*CuteQTlsBackendCall2)(const void *, int *);
typedef long (*CuteQTlsBackendCall3)(const void *, int *);
typedef QString * (*CuteQTlsBackendCall4)(const void *, int *);
typedef void (*CuteQTlsBackendCall5)(const void *, int *);
typedef QString * (*CuteQTlsBackendCall6)(const void *, int *);
typedef void * (*CuteQTlsBackendCall7)(const void *, int *);
typedef void * (*CuteQTlsBackendCall8)(const void *, int *);
typedef void * (*CuteQTlsBackendCall9)(const void *, int *);
typedef void * (*CuteQTlsBackendCall10)(const void *, class QDtls *, int, int *);
typedef void * (*CuteQTlsBackendCall11)(const void *, int *);
typedef int (*CuteQTlsBackendCall12)(const void *, const QString *, int *);
typedef int (*CuteQTlsBackendCall13)(const void *, const QString *, int *);
typedef QString * (*CuteQTlsBackendCall14)(const void *, int, int *);
typedef QString * (*CuteQTlsBackendCall15)(const void *, int, int *);
typedef bool (*CuteQTlsBackendCall16)(const void *, int, int *);
typedef int (*CuteQTlsBackendCall17)(const void *, const QByteArray *, QByteArray *, int *);
typedef int (*CuteQTlsBackendCall18)(const void *, const QByteArray *, QByteArray *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsBackendCall19)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTlsBackendCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTlsBackendCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsBackendCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsBackendCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsBackendCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsBackendCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsBackendCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTlsBackend : public QTlsBackend {
public:
  using QTlsBackend::QTlsBackend;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QTlsBackend7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend23tlsLibraryVersionNumberEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend23tlsLibraryVersionStringEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend17ensureInitializedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend11backendNameEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend9createKeyEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend17createCertificateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend20createTlsCryptographEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend21createDtlsCryptographEP5QDtlsi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend24createDtlsCookieVerifierEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend20curveIdFromShortNameERK7QString")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend19curveIdFromLongNameERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend14shortNameForIdEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend13longNameForIdEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend15isTlsNamedCurveEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayPS0_")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayPS0_")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsBackend26forceAutotestSecurityLevelEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QTlsBackend::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsBackendCall0 call = reinterpret_cast<CuteQTlsBackendCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTlsBackend::isValid();
  }

  //  long QTlsBackend::tlsLibraryVersionNumber() const
  long tlsLibraryVersionNumber() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsBackendCall1 call = reinterpret_cast<CuteQTlsBackendCall1>(taken[1]);
      long given = call(this, &handled);
      if (handled) return given;
    }
    return QTlsBackend::tlsLibraryVersionNumber();
  }

  //  QString QTlsBackend::tlsLibraryVersionString() const
  QString tlsLibraryVersionString() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsBackendCall2 call = reinterpret_cast<CuteQTlsBackendCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTlsBackend::tlsLibraryVersionString();
  }

  //  long QTlsBackend::tlsLibraryBuildVersionNumber() const
  long tlsLibraryBuildVersionNumber() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsBackendCall3 call = reinterpret_cast<CuteQTlsBackendCall3>(taken[3]);
      long given = call(this, &handled);
      if (handled) return given;
    }
    return QTlsBackend::tlsLibraryBuildVersionNumber();
  }

  //  QString QTlsBackend::tlsLibraryBuildVersionString() const
  QString tlsLibraryBuildVersionString() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsBackendCall4 call = reinterpret_cast<CuteQTlsBackendCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTlsBackend::tlsLibraryBuildVersionString();
  }

  //  void QTlsBackend::ensureInitialized() const
  void ensureInitialized() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsBackendCall5 call = reinterpret_cast<CuteQTlsBackendCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTlsBackend::ensureInitialized();
  }

  //  QString QTlsBackend::backendName() const
  QString backendName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsBackendCall6 call = reinterpret_cast<CuteQTlsBackendCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QTlsPrivate::TlsKey *QTlsBackend::createKey() const
  QTlsPrivate::TlsKey *createKey() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsBackendCall7 call = reinterpret_cast<CuteQTlsBackendCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::TlsKey *>(given);
    }
    return QTlsBackend::createKey();
  }

  //  QTlsPrivate::X509Certificate *QTlsBackend::createCertificate() const
  QTlsPrivate::X509Certificate *createCertificate() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTlsBackendCall8 call = reinterpret_cast<CuteQTlsBackendCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::X509Certificate *>(given);
    }
    return QTlsBackend::createCertificate();
  }

  //  QTlsPrivate::TlsCryptograph *QTlsBackend::createTlsCryptograph()
  //      const
  QTlsPrivate::TlsCryptograph *createTlsCryptograph() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsBackendCall9 call = reinterpret_cast<CuteQTlsBackendCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::TlsCryptograph *>(given);
    }
    return QTlsBackend::createTlsCryptograph();
  }

  //  QTlsPrivate::DtlsCryptograph
  //      *QTlsBackend::createDtlsCryptograph(class QDtls *qObject, int
  //      mode) const
  QTlsPrivate::DtlsCryptograph *createDtlsCryptograph(
      class QDtls *qObject,
      int mode) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTlsBackendCall10 call = reinterpret_cast<CuteQTlsBackendCall10>(taken[10]);
      void * given = call(this, qObject, mode, &handled);
      if (handled) return static_cast<QTlsPrivate::DtlsCryptograph *>(given);
    }
    return QTlsBackend::createDtlsCryptograph(qObject, mode);
  }

  //  QTlsPrivate::DtlsCookieVerifier
  //      *QTlsBackend::createDtlsCookieVerifier() const
  QTlsPrivate::DtlsCookieVerifier *createDtlsCookieVerifier() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTlsBackendCall11 call = reinterpret_cast<CuteQTlsBackendCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::DtlsCookieVerifier *>(given);
    }
    return QTlsBackend::createDtlsCookieVerifier();
  }

  //  int QTlsBackend::curveIdFromShortName(const QString &name) const
  int curveIdFromShortName(const QString &name) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTlsBackendCall12 call = reinterpret_cast<CuteQTlsBackendCall12>(taken[12]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QTlsBackend::curveIdFromShortName(name);
  }

  //  int QTlsBackend::curveIdFromLongName(const QString &name) const
  int curveIdFromLongName(const QString &name) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTlsBackendCall13 call = reinterpret_cast<CuteQTlsBackendCall13>(taken[13]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QTlsBackend::curveIdFromLongName(name);
  }

  //  QString QTlsBackend::shortNameForId(int cid) const
  QString shortNameForId(int cid) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTlsBackendCall14 call = reinterpret_cast<CuteQTlsBackendCall14>(taken[14]);
      QString * given = call(this, cid, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTlsBackend::shortNameForId(cid);
  }

  //  QString QTlsBackend::longNameForId(int cid) const
  QString longNameForId(int cid) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTlsBackendCall15 call = reinterpret_cast<CuteQTlsBackendCall15>(taken[15]);
      QString * given = call(this, cid, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTlsBackend::longNameForId(cid);
  }

  //  bool QTlsBackend::isTlsNamedCurve(int cid) const
  bool isTlsNamedCurve(int cid) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTlsBackendCall16 call = reinterpret_cast<CuteQTlsBackendCall16>(taken[16]);
      bool given = call(this, cid, &handled);
      if (handled) return given;
    }
    return QTlsBackend::isTlsNamedCurve(cid);
  }

  //  int QTlsBackend::dhParametersFromDer(const QByteArray &derData,
  //      QByteArray *data) const
  int dhParametersFromDer(
      const QByteArray &derData,
      QByteArray *data) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTlsBackendCall17 call = reinterpret_cast<CuteQTlsBackendCall17>(taken[17]);
      int given = call(this, &derData, data, &handled);
      if (handled) return given;
    }
    return QTlsBackend::dhParametersFromDer(derData, data);
  }

  //  int QTlsBackend::dhParametersFromPem(const QByteArray &pemData,
  //      QByteArray *data) const
  int dhParametersFromPem(
      const QByteArray &pemData,
      QByteArray *data) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTlsBackendCall18 call = reinterpret_cast<CuteQTlsBackendCall18>(taken[18]);
      int given = call(this, &pemData, data, &handled);
      if (handled) return given;
    }
    return QTlsBackend::dhParametersFromPem(pemData, data);
  }

#if QT_CONFIG(ssl)
  //  void QTlsBackend::forceAutotestSecurityLevel()
  void forceAutotestSecurityLevel() override {
    if (taken[19]) {
      int handled = 0;
      CuteQTlsBackendCall19 call = reinterpret_cast<CuteQTlsBackendCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QTlsBackend::forceAutotestSecurityLevel();
  }
#endif  // QT_CONFIG(ssl)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTlsBackendCall20 call = reinterpret_cast<CuteQTlsBackendCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTlsBackendCall21 call = reinterpret_cast<CuteQTlsBackendCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTlsBackendCall22 call = reinterpret_cast<CuteQTlsBackendCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTlsBackendCall23 call = reinterpret_cast<CuteQTlsBackendCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTlsBackendCall24 call = reinterpret_cast<CuteQTlsBackendCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTlsBackendCall25 call = reinterpret_cast<CuteQTlsBackendCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTlsBackendCall26 call = reinterpret_cast<CuteQTlsBackendCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTlsBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTlsBackend10metaObjectEv(
    const QTlsBackend *self) {
  return self->metaObject();
}

//  void *QTlsBackend::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QTlsBackend11qt_metacastEPKc(
    QTlsBackend *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTlsBackend::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTlsBackend11qt_metacallEN11QMetaObject4CallEiPPv(
    QTlsBackend *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTlsBackend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTlsBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTlsBackend::tr(s, c, n));
}

//  QTlsBackend::~QTlsBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackendD1Ev(QTlsBackend *self) {
  delete self;
}

//  bool QTlsBackend::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsBackend7isValidEv(const QTlsBackend *self) {
  return self->isValid();
}

//  long QTlsBackend::tlsLibraryVersionNumber() const
extern "C" Q_DECL_EXPORT
long ritual_ZNK11QTlsBackend23tlsLibraryVersionNumberEv(
    const QTlsBackend *self) {
  return self->tlsLibraryVersionNumber();
}

//  QString QTlsBackend::tlsLibraryVersionString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsBackend23tlsLibraryVersionStringEv(
    const QTlsBackend *self) {
  return new QString(self->tlsLibraryVersionString());
}

//  long QTlsBackend::tlsLibraryBuildVersionNumber() const
extern "C" Q_DECL_EXPORT
long ritual_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv(
    const QTlsBackend *self) {
  return self->tlsLibraryBuildVersionNumber();
}

//  QString QTlsBackend::tlsLibraryBuildVersionString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv(
    const QTlsBackend *self) {
  return new QString(self->tlsLibraryBuildVersionString());
}

//  void QTlsBackend::ensureInitialized() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTlsBackend17ensureInitializedEv(const QTlsBackend *self) {
  self->ensureInitialized();
}

//  QString QTlsBackend::backendName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsBackend11backendNameEv(const QTlsBackend *self) {
  return new QString(self->backendName());
}

//  QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols() const
extern "C" Q_DECL_EXPORT
QList<QSsl::SslProtocol> *ritual_ZNK11QTlsBackend18supportedProtocolsEv(
    const QTlsBackend *self) {
  return new QList<QSsl::SslProtocol>(self->supportedProtocols());
}

//  QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures() const
extern "C" Q_DECL_EXPORT
QList<QSsl::SupportedFeature> *ritual_ZNK11QTlsBackend17supportedFeaturesEv(
    const QTlsBackend *self) {
  return new QList<QSsl::SupportedFeature>(self->supportedFeatures());
}

//  QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses() const
extern "C" Q_DECL_EXPORT
QList<QSsl::ImplementedClass> *ritual_ZNK11QTlsBackend18implementedClassesEv(
    const QTlsBackend *self) {
  return new QList<QSsl::ImplementedClass>(self->implementedClasses());
}

//  QTlsPrivate::TlsKey *QTlsBackend::createKey() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey *ritual_ZNK11QTlsBackend9createKeyEv(
    const QTlsBackend *self) {
  return self->createKey();
}

//  QTlsPrivate::X509Certificate *QTlsBackend::createCertificate() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::X509Certificate *ritual_ZNK11QTlsBackend17createCertificateEv(
    const QTlsBackend *self) {
  return self->createCertificate();
}

//  QList<QSslCertificate> QTlsBackend::systemCaCertificates() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK11QTlsBackend20systemCaCertificatesEv(
    const QTlsBackend *self) {
  return new QList<QSslCertificate>(self->systemCaCertificates());
}

//  QTlsPrivate::TlsCryptograph *QTlsBackend::createTlsCryptograph() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsCryptograph *ritual_ZNK11QTlsBackend20createTlsCryptographEv(
    const QTlsBackend *self) {
  return self->createTlsCryptograph();
}

//  QTlsPrivate::DtlsCryptograph *QTlsBackend::createDtlsCryptograph(class
//      QDtls *qObject, int mode) const
extern "C" Q_DECL_EXPORT
QTlsPrivate::DtlsCryptograph *ritual_ZNK11QTlsBackend21createDtlsCryptographEP5QDtlsi(
    const QTlsBackend *self,
    class QDtls *qObject,
    int mode) {
  return self->createDtlsCryptograph(qObject, mode);
}

//  QTlsPrivate::DtlsCookieVerifier *QTlsBackend::createDtlsCookieVerifier()
//      const
extern "C" Q_DECL_EXPORT
QTlsPrivate::DtlsCookieVerifier *ritual_ZNK11QTlsBackend24createDtlsCookieVerifierEv(
    const QTlsBackend *self) {
  return self->createDtlsCookieVerifier();
}

//  QTlsPrivate::X509ChainVerifyPtr QTlsBackend::X509Verifier() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QTlsBackend12X509VerifierEv(const QTlsBackend *self) {
  return reinterpret_cast<void *>(self->X509Verifier());
}

//  QTlsPrivate::X509PemReaderPtr QTlsBackend::X509PemReader() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QTlsBackend13X509PemReaderEv(const QTlsBackend *self) {
  return reinterpret_cast<void *>(self->X509PemReader());
}

//  QTlsPrivate::X509DerReaderPtr QTlsBackend::X509DerReader() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QTlsBackend13X509DerReaderEv(const QTlsBackend *self) {
  return reinterpret_cast<void *>(self->X509DerReader());
}

//  QTlsPrivate::X509Pkcs12ReaderPtr QTlsBackend::X509Pkcs12Reader() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QTlsBackend16X509Pkcs12ReaderEv(const QTlsBackend *self) {
  return reinterpret_cast<void *>(self->X509Pkcs12Reader());
}

//  QList<int> QTlsBackend::ellipticCurvesIds() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK11QTlsBackend17ellipticCurvesIdsEv(
    const QTlsBackend *self) {
  return new QList<int>(self->ellipticCurvesIds());
}

//  int QTlsBackend::curveIdFromShortName(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTlsBackend20curveIdFromShortNameERK7QString(
    const QTlsBackend *self,
    const QString *name) {
  return self->curveIdFromShortName(*name);
}

//  int QTlsBackend::curveIdFromLongName(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTlsBackend19curveIdFromLongNameERK7QString(
    const QTlsBackend *self,
    const QString *name) {
  return self->curveIdFromLongName(*name);
}

//  QString QTlsBackend::shortNameForId(int cid) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsBackend14shortNameForIdEi(
    const QTlsBackend *self,
    int cid) {
  return new QString(self->shortNameForId(cid));
}

//  QString QTlsBackend::longNameForId(int cid) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsBackend13longNameForIdEi(
    const QTlsBackend *self,
    int cid) {
  return new QString(self->longNameForId(cid));
}

//  bool QTlsBackend::isTlsNamedCurve(int cid) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsBackend15isTlsNamedCurveEi(
    const QTlsBackend *self,
    int cid) {
  return self->isTlsNamedCurve(cid);
}

//  int QTlsBackend::dhParametersFromDer(const QByteArray &derData,
//      QByteArray *data) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayPS0_(
    const QTlsBackend *self,
    const QByteArray *derData,
    QByteArray *data) {
  return self->dhParametersFromDer(*derData, data);
}

//  int QTlsBackend::dhParametersFromPem(const QByteArray &pemData,
//      QByteArray *data) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayPS0_(
    const QTlsBackend *self,
    const QByteArray *pemData,
    QByteArray *data) {
  return self->dhParametersFromPem(*pemData, data);
}

//  QList<QString> QTlsBackend::availableBackendNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QTlsBackend21availableBackendNamesEv() {
  return new QList<QString>(QTlsBackend::availableBackendNames());
}

//  QString QTlsBackend::defaultBackendName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTlsBackend18defaultBackendNameEv() {
  return new QString(QTlsBackend::defaultBackendName());
}

//  QTlsBackend *QTlsBackend::findBackend(const QString &backendName)
extern "C" Q_DECL_EXPORT
QTlsBackend *ritual_ZN11QTlsBackend11findBackendERK7QString(
    const QString *backendName) {
  return QTlsBackend::findBackend(*backendName);
}

//  QTlsBackend *QTlsBackend::activeOrAnyBackend()
extern "C" Q_DECL_EXPORT
QTlsBackend *ritual_ZN11QTlsBackend18activeOrAnyBackendEv() {
  return QTlsBackend::activeOrAnyBackend();
}

//  QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols(const QString
//      &backendName)
extern "C" Q_DECL_EXPORT
QList<QSsl::SslProtocol> *ritual_ZN11QTlsBackend18supportedProtocolsERK7QString(
    const QString *backendName) {
  return new QList<QSsl::SslProtocol>(
      QTlsBackend::supportedProtocols(
          *backendName));
}

//  QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures(const
//      QString &backendName)
extern "C" Q_DECL_EXPORT
QList<QSsl::SupportedFeature> *ritual_ZN11QTlsBackend17supportedFeaturesERK7QString(
    const QString *backendName) {
  return new QList<QSsl::SupportedFeature>(
      QTlsBackend::supportedFeatures(
          *backendName));
}

//  QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses(const
//      QString &backendName)
extern "C" Q_DECL_EXPORT
QList<QSsl::ImplementedClass> *ritual_ZN11QTlsBackend18implementedClassesERK7QString(
    const QString *backendName) {
  return new QList<QSsl::ImplementedClass>(
      QTlsBackend::implementedClasses(
          *backendName));
}

//  void QTlsBackend::resetBackend(QSslKey &key, QTlsPrivate::TlsKey
//      *keyBackend)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend12resetBackendER7QSslKeyPN11QTlsPrivate6TlsKeyE(
    QSslKey *key,
    QTlsPrivate::TlsKey *keyBackend) {
  QTlsBackend::resetBackend(*key, keyBackend);
}

//  void QTlsBackend::setupClientPskAuth(QSslPreSharedKeyAuthenticator *auth,
//      const char *hint, int hintLength, unsigned int maxIdentityLen,
//      unsigned int maxPskLen)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend18setupClientPskAuthEP29QSslPreSharedKeyAuthenticatorPKcijj(
    QSslPreSharedKeyAuthenticator *auth,
    const char *hint,
    int hintLength,
    unsigned int maxIdentityLen,
    unsigned int maxPskLen) {
  QTlsBackend::setupClientPskAuth(
      auth,
      hint,
      hintLength,
      maxIdentityLen,
      maxPskLen);
}

//  void QTlsBackend::setupServerPskAuth(QSslPreSharedKeyAuthenticator *auth,
//      const char *identity, const QByteArray &identityHint, unsigned int
//      maxPskLen)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend18setupServerPskAuthEP29QSslPreSharedKeyAuthenticatorPKcRK10QByteArrayj(
    QSslPreSharedKeyAuthenticator *auth,
    const char *identity,
    const QByteArray *identityHint,
    unsigned int maxPskLen) {
  QTlsBackend::setupServerPskAuth(auth, identity, *identityHint, maxPskLen);
}

#if QT_CONFIG(ssl)
//  QSslCipher QTlsBackend::createCiphersuite(const QString &description, int
//      bits, int supportedBits)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringii(
    const QString *description,
    int bits,
    int supportedBits) {
  return new QSslCipher(
      QTlsBackend::createCiphersuite(
          *description,
          bits,
          supportedBits));
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QSslCipher QTlsBackend::createCiphersuite(const QString &suiteName,
//      QSsl::SslProtocol protocol, const QString &protocolString)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringN4QSsl11SslProtocolES2_(
    const QString *suiteName,
    QSsl::SslProtocol protocol,
    const QString *protocolString) {
  return new QSslCipher(
      QTlsBackend::createCiphersuite(
          *suiteName,
          protocol,
          *protocolString));
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QSslCipher QTlsBackend::createCiphersuite(const QString &name, const
//      QString &keyExchangeMethod, const QString &encryptionMethod, const
//      QString &authenticationMethod, int bits, QSsl::SslProtocol protocol,
//      const QString &protocolString)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringS2_S2_S2_iN4QSsl11SslProtocolES2_(
    const QString *name,
    const QString *keyExchangeMethod,
    const QString *encryptionMethod,
    const QString *authenticationMethod,
    int bits,
    QSsl::SslProtocol protocol,
    const QString *protocolString) {
  return new QSslCipher(
      QTlsBackend::createCiphersuite(
          *name,
          *keyExchangeMethod,
          *encryptionMethod,
          *authenticationMethod,
          bits,
          protocol,
          *protocolString));
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QList<QSslCipher> QTlsBackend::defaultCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN11QTlsBackend14defaultCiphersEv() {
  return new QList<QSslCipher>(QTlsBackend::defaultCiphers());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QList<QSslCipher> QTlsBackend::defaultDtlsCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN11QTlsBackend18defaultDtlsCiphersEv() {
  return new QList<QSslCipher>(QTlsBackend::defaultDtlsCiphers());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setDefaultCiphers(const QList<QSslCipher> &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend17setDefaultCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QTlsBackend::setDefaultCiphers(*ciphers);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setDefaultDtlsCiphers(const QList<QSslCipher> &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend21setDefaultDtlsCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QTlsBackend::setDefaultDtlsCiphers(*ciphers);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setDefaultSupportedCiphers(const QList<QSslCipher>
//      &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend26setDefaultSupportedCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QTlsBackend::setDefaultSupportedCiphers(*ciphers);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::resetDefaultEllipticCurves()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend26resetDefaultEllipticCurvesEv() {
  QTlsBackend::resetDefaultEllipticCurves();
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setDefaultCaCertificates(const QList<QSslCertificate>
//      &certs)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend24setDefaultCaCertificatesERK5QListI15QSslCertificateE(
    const QList<QSslCertificate> *certs) {
  QTlsBackend::setDefaultCaCertificates(*certs);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  bool QTlsBackend::rootLoadingOnDemandAllowed(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsBackend26rootLoadingOnDemandAllowedERK17QSslConfiguration(
    const QSslConfiguration *configuration) {
  return QTlsBackend::rootLoadingOnDemandAllowed(*configuration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::storePeerCertificate(QSslConfiguration &configuration,
//      const QSslCertificate &peerCert)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend20storePeerCertificateER17QSslConfigurationRK15QSslCertificate(
    QSslConfiguration *configuration,
    const QSslCertificate *peerCert) {
  QTlsBackend::storePeerCertificate(*configuration, *peerCert);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::storePeerCertificateChain(QSslConfiguration
//      &configuration, const QList<QSslCertificate> &peerCertificateChain)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend25storePeerCertificateChainER17QSslConfigurationRK5QListI15QSslCertificateE(
    QSslConfiguration *configuration,
    const QList<QSslCertificate> *peerCertificateChain) {
  QTlsBackend::storePeerCertificateChain(
      *configuration,
      *peerCertificateChain);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::clearPeerCertificates(QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend21clearPeerCertificatesER17QSslConfiguration(
    QSslConfiguration *configuration) {
  QTlsBackend::clearPeerCertificates(*configuration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::clearPeerCertificates(QSslSocketPrivate *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend21clearPeerCertificatesEP17QSslSocketPrivate(
    QSslSocketPrivate *d) {
  QTlsBackend::clearPeerCertificates(d);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setPeerSessionShared(QSslSocketPrivate *d, bool shared)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend20setPeerSessionSharedEP17QSslSocketPrivateb(
    QSslSocketPrivate *d,
    bool shared) {
  QTlsBackend::setPeerSessionShared(d, shared);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setSessionAsn1(QSslSocketPrivate *d, const QByteArray
//      &asn1)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend14setSessionAsn1EP17QSslSocketPrivateRK10QByteArray(
    QSslSocketPrivate *d,
    const QByteArray *asn1) {
  QTlsBackend::setSessionAsn1(d, *asn1);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setSessionLifetimeHint(QSslSocketPrivate *d, int hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend22setSessionLifetimeHintEP17QSslSocketPrivatei(
    QSslSocketPrivate *d,
    int hint) {
  QTlsBackend::setSessionLifetimeHint(d, hint);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setAlpnStatus(QSslSocketPrivate *d,
//      AlpnNegotiationStatus st)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend13setAlpnStatusEP17QSslSocketPrivateN17QSslConfiguration29NextProtocolNegotiationStatusE(
    QSslSocketPrivate *d,
    QTlsBackend::AlpnNegotiationStatus st) {
  QTlsBackend::setAlpnStatus(d, st);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setNegotiatedProtocol(QSslSocketPrivate *d, const
//      QByteArray &protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend21setNegotiatedProtocolEP17QSslSocketPrivateRK10QByteArray(
    QSslSocketPrivate *d,
    const QByteArray *protocol) {
  QTlsBackend::setNegotiatedProtocol(d, *protocol);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::storePeerCertificate(QSslSocketPrivate *d, const
//      QSslCertificate &peerCert)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend20storePeerCertificateEP17QSslSocketPrivateRK15QSslCertificate(
    QSslSocketPrivate *d,
    const QSslCertificate *peerCert) {
  QTlsBackend::storePeerCertificate(d, *peerCert);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::storePeerCertificateChain(QSslSocketPrivate *d, const
//      QList<QSslCertificate> &peerChain)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend25storePeerCertificateChainEP17QSslSocketPrivateRK5QListI15QSslCertificateE(
    QSslSocketPrivate *d,
    const QList<QSslCertificate> *peerChain) {
  QTlsBackend::storePeerCertificateChain(d, *peerChain);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::addTrustedRoot(QSslSocketPrivate *d, const
//      QSslCertificate &rootCert)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend14addTrustedRootEP17QSslSocketPrivateRK15QSslCertificate(
    QSslSocketPrivate *d,
    const QSslCertificate *rootCert) {
  QTlsBackend::addTrustedRoot(d, *rootCert);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::setEphemeralKey(QSslSocketPrivate *d, const QSslKey
//      &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend15setEphemeralKeyEP17QSslSocketPrivateRK7QSslKey(
    QSslSocketPrivate *d,
    const QSslKey *key) {
  QTlsBackend::setEphemeralKey(d, *key);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QTlsBackend::forceAutotestSecurityLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsBackend26forceAutotestSecurityLevelEv(
    QTlsBackend *self) {
  self->forceAutotestSecurityLevel();
}
#endif  // QT_CONFIG(ssl)

//  a Python function taken by a CuteQTlsBackend, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsBackend(
    QTlsBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsBackend *>(self)->take(key, call);
}

//  bool QTlsBackend::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTlsBackend7isValidEv(const QTlsBackend *self) {
  return self->QTlsBackend::isValid();
}

//  long QTlsBackend::tlsLibraryVersionNumber() const
extern "C" Q_DECL_EXPORT
long ritual_own_ZNK11QTlsBackend23tlsLibraryVersionNumberEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::tlsLibraryVersionNumber();
}

//  QString QTlsBackend::tlsLibraryVersionString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QTlsBackend23tlsLibraryVersionStringEv(
    const QTlsBackend *self) {
  return new QString(self->QTlsBackend::tlsLibraryVersionString());
}

//  long QTlsBackend::tlsLibraryBuildVersionNumber() const
extern "C" Q_DECL_EXPORT
long ritual_own_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::tlsLibraryBuildVersionNumber();
}

//  QString QTlsBackend::tlsLibraryBuildVersionString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv(
    const QTlsBackend *self) {
  return new QString(self->QTlsBackend::tlsLibraryBuildVersionString());
}

//  void QTlsBackend::ensureInitialized() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QTlsBackend17ensureInitializedEv(
    const QTlsBackend *self) {
  self->QTlsBackend::ensureInitialized();
}

//  QTlsPrivate::TlsKey *QTlsBackend::createKey() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey *ritual_own_ZNK11QTlsBackend9createKeyEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::createKey();
}

//  QTlsPrivate::X509Certificate *QTlsBackend::createCertificate() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::X509Certificate *ritual_own_ZNK11QTlsBackend17createCertificateEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::createCertificate();
}

//  QTlsPrivate::TlsCryptograph *QTlsBackend::createTlsCryptograph() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsCryptograph *ritual_own_ZNK11QTlsBackend20createTlsCryptographEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::createTlsCryptograph();
}

//  QTlsPrivate::DtlsCryptograph *QTlsBackend::createDtlsCryptograph(class
//      QDtls *qObject, int mode) const
extern "C" Q_DECL_EXPORT
QTlsPrivate::DtlsCryptograph *ritual_own_ZNK11QTlsBackend21createDtlsCryptographEP5QDtlsi(
    const QTlsBackend *self,
    class QDtls *qObject,
    int mode) {
  return self->QTlsBackend::createDtlsCryptograph(qObject, mode);
}

//  QTlsPrivate::DtlsCookieVerifier *QTlsBackend::createDtlsCookieVerifier()
//      const
extern "C" Q_DECL_EXPORT
QTlsPrivate::DtlsCookieVerifier *ritual_own_ZNK11QTlsBackend24createDtlsCookieVerifierEv(
    const QTlsBackend *self) {
  return self->QTlsBackend::createDtlsCookieVerifier();
}

//  int QTlsBackend::curveIdFromShortName(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTlsBackend20curveIdFromShortNameERK7QString(
    const QTlsBackend *self,
    const QString *name) {
  return self->QTlsBackend::curveIdFromShortName(*name);
}

//  int QTlsBackend::curveIdFromLongName(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTlsBackend19curveIdFromLongNameERK7QString(
    const QTlsBackend *self,
    const QString *name) {
  return self->QTlsBackend::curveIdFromLongName(*name);
}

//  QString QTlsBackend::shortNameForId(int cid) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QTlsBackend14shortNameForIdEi(
    const QTlsBackend *self,
    int cid) {
  return new QString(self->QTlsBackend::shortNameForId(cid));
}

//  QString QTlsBackend::longNameForId(int cid) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QTlsBackend13longNameForIdEi(
    const QTlsBackend *self,
    int cid) {
  return new QString(self->QTlsBackend::longNameForId(cid));
}

//  bool QTlsBackend::isTlsNamedCurve(int cid) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTlsBackend15isTlsNamedCurveEi(
    const QTlsBackend *self,
    int cid) {
  return self->QTlsBackend::isTlsNamedCurve(cid);
}

//  int QTlsBackend::dhParametersFromDer(const QByteArray &derData,
//      QByteArray *data) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayPS0_(
    const QTlsBackend *self,
    const QByteArray *derData,
    QByteArray *data) {
  return self->QTlsBackend::dhParametersFromDer(*derData, data);
}

//  int QTlsBackend::dhParametersFromPem(const QByteArray &pemData,
//      QByteArray *data) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayPS0_(
    const QTlsBackend *self,
    const QByteArray *pemData,
    QByteArray *data) {
  return self->QTlsBackend::dhParametersFromPem(*pemData, data);
}

#if QT_CONFIG(ssl)
//  void QTlsBackend::forceAutotestSecurityLevel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTlsBackend26forceAutotestSecurityLevelEv(
    QTlsBackend *self) {
  self->QTlsBackend::forceAutotestSecurityLevel();
}
#endif  // QT_CONFIG(ssl)

//  a QList<QSsl::SslProtocol> a ritual of QTlsBackend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTlsBackend__QList_QSsl_SslProtocol(
    QList<QSsl::SslProtocol> *self) {
  delete self;
}

//  a QList<QSsl::SupportedFeature> a ritual of QTlsBackend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTlsBackend__QList_QSsl_SupportedFeature(
    QList<QSsl::SupportedFeature> *self) {
  delete self;
}

//  a QList<QSsl::ImplementedClass> a ritual of QTlsBackend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTlsBackend__QList_QSsl_ImplementedClass(
    QList<QSsl::ImplementedClass> *self) {
  delete self;
}

//  a QList<int> a ritual of QTlsBackend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTlsBackend__QList_int(QList<int> *self) {
  delete self;
}
