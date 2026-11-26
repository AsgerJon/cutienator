//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QMultiMap>
#include <QtNetwork/QSsl>
#include <QtCore/QString>

//  A QTlsPrivate::X509Certificate that Python can take functions over in. Every QTlsPrivate::X509Certificate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTlsPrivate_X509CertificateCall0)(const void *, int *);
typedef bool (*CuteQTlsPrivate_X509CertificateCall1)(const void *, int *);
typedef const QByteArray * (*CuteQTlsPrivate_X509CertificateCall2)(const void *, int *);
typedef const QByteArray * (*CuteQTlsPrivate_X509CertificateCall3)(const void *, int *);
typedef const QDateTime * (*CuteQTlsPrivate_X509CertificateCall4)(const void *, int *);
typedef const QDateTime * (*CuteQTlsPrivate_X509CertificateCall5)(const void *, int *);
typedef void * (*CuteQTlsPrivate_X509CertificateCall6)(const void *, int *);
typedef qsizetype (*CuteQTlsPrivate_X509CertificateCall7)(const void *, int *);
typedef QString * (*CuteQTlsPrivate_X509CertificateCall8)(const void *, qsizetype, int *);
typedef QString * (*CuteQTlsPrivate_X509CertificateCall9)(const void *, qsizetype, int *);
typedef const QVariant * (*CuteQTlsPrivate_X509CertificateCall10)(const void *, qsizetype, int *);
typedef bool (*CuteQTlsPrivate_X509CertificateCall11)(const void *, qsizetype, int *);
typedef bool (*CuteQTlsPrivate_X509CertificateCall12)(const void *, qsizetype, int *);
typedef const QByteArray * (*CuteQTlsPrivate_X509CertificateCall13)(const void *, int *);
typedef const QByteArray * (*CuteQTlsPrivate_X509CertificateCall14)(const void *, int *);
typedef QString * (*CuteQTlsPrivate_X509CertificateCall15)(const void *, int *);
typedef void * (*CuteQTlsPrivate_X509CertificateCall16)(const void *, int *);
typedef size_t (*CuteQTlsPrivate_X509CertificateCall17)(const void *, size_t, int *);
class CuteQTlsPrivate_X509Certificate : public QTlsPrivate::X509Certificate {
public:
  using QTlsPrivate::X509Certificate::X509Certificate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate6isNullEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate12isSelfSignedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate7versionEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate12serialNumberEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate13effectiveDateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate10expiryDateEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate9publicKeyEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate18numberOfExtensionsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate15oidForExtensionEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate16nameForExtensionEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate17valueForExtensionEx")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate19isExtensionCriticalEx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate20isExtensionSupportedEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate5toPemEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate5toDerEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate6toTextEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate6handleEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15X509Certificate4hashEm")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  bool QTlsPrivate::X509Certificate::isNull() const
  bool isNull() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall0 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QTlsPrivate::X509Certificate::isSelfSigned() const
  bool isSelfSigned() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall1 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::X509Certificate::version() const
  QByteArray version() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall2 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall2>(taken[2]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::X509Certificate::serialNumber() const
  QByteArray serialNumber() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall3 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall3>(taken[3]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QDateTime QTlsPrivate::X509Certificate::effectiveDate() const
  QDateTime effectiveDate() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall4 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall4>(taken[4]);
      const QDateTime * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QDateTime QTlsPrivate::X509Certificate::expiryDate() const
  QDateTime expiryDate() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall5 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall5>(taken[5]);
      const QDateTime * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  TlsKey *QTlsPrivate::X509Certificate::publicKey() const
  QTlsPrivate::TlsKey *publicKey() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall6 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::TlsKey *>(given);
    }
    return QTlsPrivate::X509Certificate::publicKey();
  }

  //  qsizetype QTlsPrivate::X509Certificate::numberOfExtensions() const
  qsizetype numberOfExtensions() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall7 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall7>(taken[7]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QTlsPrivate::X509Certificate::oidForExtension(qsizetype i)
  //      const
  QString oidForExtension(qsizetype i) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall8 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall8>(taken[8]);
      QString * given = call(this, i, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QTlsPrivate::X509Certificate::nameForExtension(qsizetype i)
  //      const
  QString nameForExtension(qsizetype i) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall9 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall9>(taken[9]);
      QString * given = call(this, i, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QVariant QTlsPrivate::X509Certificate::valueForExtension(qsizetype i)
  //      const
  QVariant valueForExtension(qsizetype i) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall10 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall10>(taken[10]);
      const QVariant * given = call(this, i, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QTlsPrivate::X509Certificate::isExtensionCritical(qsizetype i)
  //      const
  bool isExtensionCritical(qsizetype i) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall11 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall11>(taken[11]);
      bool given = call(this, i, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QTlsPrivate::X509Certificate::isExtensionSupported(qsizetype i)
  //      const
  bool isExtensionSupported(qsizetype i) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall12 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall12>(taken[12]);
      bool given = call(this, i, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::X509Certificate::toPem() const
  QByteArray toPem() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall13 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall13>(taken[13]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::X509Certificate::toDer() const
  QByteArray toDer() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall14 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall14>(taken[14]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QString QTlsPrivate::X509Certificate::toText() const
  QString toText() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall15 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall15>(taken[15]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  Qt::HANDLE QTlsPrivate::X509Certificate::handle() const
  Qt::HANDLE handle() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall16 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return {};
  }

  //  size_t QTlsPrivate::X509Certificate::hash(size_t seed) const
  size_t hash(size_t seed) const noexcept override {
    if (taken[17]) {
      int handled = 0;
      CuteQTlsPrivate_X509CertificateCall17 call = reinterpret_cast<CuteQTlsPrivate_X509CertificateCall17>(taken[17]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QTlsPrivate::X509Certificate::~X509Certificate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15X509CertificateD1Ev(
    QTlsPrivate::X509Certificate *self) {
  delete self;
}

//  bool QTlsPrivate::X509Certificate::isEqual(const X509Certificate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15X509Certificate7isEqualERKS0_(
    const QTlsPrivate::X509Certificate *self,
    const QTlsPrivate::X509Certificate *other) {
  return self->isEqual(*other);
}

//  bool QTlsPrivate::X509Certificate::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15X509Certificate6isNullEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->isNull();
}

//  bool QTlsPrivate::X509Certificate::isSelfSigned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15X509Certificate12isSelfSignedEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->isSelfSigned();
}

//  QByteArray QTlsPrivate::X509Certificate::version() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate15X509Certificate7versionEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QByteArray(self->version());
}

//  QByteArray QTlsPrivate::X509Certificate::serialNumber() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate15X509Certificate12serialNumberEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QByteArray(self->serialNumber());
}

//  QStringList
//      QTlsPrivate::X509Certificate::issuerInfo(QSslCertificate::SubjectInfo
//      subject) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTlsPrivate15X509Certificate10issuerInfoEN15QSslCertificate11SubjectInfoE(
    const QTlsPrivate::X509Certificate *self,
    QSslCertificate::SubjectInfo subject) {
  return new QList<QString>(self->issuerInfo(subject));
}

//  QStringList QTlsPrivate::X509Certificate::issuerInfo(const QByteArray
//      &attribute) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTlsPrivate15X509Certificate10issuerInfoERK10QByteArray(
    const QTlsPrivate::X509Certificate *self,
    const QByteArray *attribute) {
  return new QList<QString>(self->issuerInfo(*attribute));
}

//  QStringList
//      QTlsPrivate::X509Certificate::subjectInfo(QSslCertificate::SubjectInf
//      o subject) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTlsPrivate15X509Certificate11subjectInfoEN15QSslCertificate11SubjectInfoE(
    const QTlsPrivate::X509Certificate *self,
    QSslCertificate::SubjectInfo subject) {
  return new QList<QString>(self->subjectInfo(subject));
}

//  QStringList QTlsPrivate::X509Certificate::subjectInfo(const QByteArray
//      &attribute) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTlsPrivate15X509Certificate11subjectInfoERK10QByteArray(
    const QTlsPrivate::X509Certificate *self,
    const QByteArray *attribute) {
  return new QList<QString>(self->subjectInfo(*attribute));
}

//  QList<QByteArray> QTlsPrivate::X509Certificate::subjectInfoAttributes()
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QTlsPrivate15X509Certificate21subjectInfoAttributesEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QList<QByteArray>(self->subjectInfoAttributes());
}

//  QList<QByteArray> QTlsPrivate::X509Certificate::issuerInfoAttributes()
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QTlsPrivate15X509Certificate20issuerInfoAttributesEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QList<QByteArray>(self->issuerInfoAttributes());
}

//  QMultiMap<QSsl::AlternativeNameEntryType, QString>
//      QTlsPrivate::X509Certificate::subjectAlternativeNames() const
extern "C" Q_DECL_EXPORT
QMultiMap<QSsl::AlternativeNameEntryType, QString> *ritual_ZNK11QTlsPrivate15X509Certificate23subjectAlternativeNamesEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QMultiMap<QSsl::AlternativeNameEntryType, QString>(
      self->subjectAlternativeNames());
}

//  QDateTime QTlsPrivate::X509Certificate::effectiveDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QTlsPrivate15X509Certificate13effectiveDateEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QDateTime(self->effectiveDate());
}

//  QDateTime QTlsPrivate::X509Certificate::expiryDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QTlsPrivate15X509Certificate10expiryDateEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QDateTime(self->expiryDate());
}

//  TlsKey *QTlsPrivate::X509Certificate::publicKey() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey *ritual_ZNK11QTlsPrivate15X509Certificate9publicKeyEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->publicKey();
}

//  qsizetype QTlsPrivate::X509Certificate::numberOfExtensions() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QTlsPrivate15X509Certificate18numberOfExtensionsEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->numberOfExtensions();
}

//  QString QTlsPrivate::X509Certificate::oidForExtension(qsizetype i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsPrivate15X509Certificate15oidForExtensionEx(
    const QTlsPrivate::X509Certificate *self,
    qsizetype i) {
  return new QString(self->oidForExtension(i));
}

//  QString QTlsPrivate::X509Certificate::nameForExtension(qsizetype i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsPrivate15X509Certificate16nameForExtensionEx(
    const QTlsPrivate::X509Certificate *self,
    qsizetype i) {
  return new QString(self->nameForExtension(i));
}

//  QVariant QTlsPrivate::X509Certificate::valueForExtension(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTlsPrivate15X509Certificate17valueForExtensionEx(
    const QTlsPrivate::X509Certificate *self,
    qsizetype i) {
  return new QVariant(self->valueForExtension(i));
}

//  bool QTlsPrivate::X509Certificate::isExtensionCritical(qsizetype i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15X509Certificate19isExtensionCriticalEx(
    const QTlsPrivate::X509Certificate *self,
    qsizetype i) {
  return self->isExtensionCritical(i);
}

//  bool QTlsPrivate::X509Certificate::isExtensionSupported(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15X509Certificate20isExtensionSupportedEx(
    const QTlsPrivate::X509Certificate *self,
    qsizetype i) {
  return self->isExtensionSupported(i);
}

//  QByteArray QTlsPrivate::X509Certificate::toPem() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate15X509Certificate5toPemEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QByteArray(self->toPem());
}

//  QByteArray QTlsPrivate::X509Certificate::toDer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate15X509Certificate5toDerEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QByteArray(self->toDer());
}

//  QString QTlsPrivate::X509Certificate::toText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsPrivate15X509Certificate6toTextEv(
    const QTlsPrivate::X509Certificate *self) {
  return new QString(self->toText());
}

//  Qt::HANDLE QTlsPrivate::X509Certificate::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK11QTlsPrivate15X509Certificate6handleEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->handle();
}

//  size_t QTlsPrivate::X509Certificate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK11QTlsPrivate15X509Certificate4hashEm(
    const QTlsPrivate::X509Certificate *self,
    size_t seed) {
  return self->hash(seed);
}

//  a Python function taken by a CuteQTlsPrivate_X509Certificate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_X509Certificate(
    QTlsPrivate::X509Certificate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_X509Certificate *>(self)->take(key, call);
}

//  TlsKey *QTlsPrivate::X509Certificate::publicKey() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey *ritual_own_ZNK11QTlsPrivate15X509Certificate9publicKeyEv(
    const QTlsPrivate::X509Certificate *self) {
  return self->QTlsPrivate::X509Certificate::publicKey();
}

//  a QMultiMap<QSsl::AlternativeNameEntryType, QString> a ritual of
//      QTlsPrivate::X509Certificate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTlsPrivate_X509Certificate__QMultiMap_QSsl_AlternativeNameEntryType_QString(
    QMultiMap<QSsl::AlternativeNameEntryType, QString> *self) {
  delete self;
}
