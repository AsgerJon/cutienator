//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QTlsPrivate::TlsKey that Python can take functions over in. Every QTlsPrivate::TlsKey
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTlsPrivate_TlsKeyCall0)(const void *, int, int, const QByteArray *, const QByteArray *, bool, int *);
typedef void (*CuteQTlsPrivate_TlsKeyCall1)(const void *, int, int, const QByteArray *, const QByteArray *, bool, int *);
typedef const QByteArray * (*CuteQTlsPrivate_TlsKeyCall2)(const void *, const QByteArray *, int *);
typedef bool (*CuteQTlsPrivate_TlsKeyCall3)(const void *, int *);
typedef int (*CuteQTlsPrivate_TlsKeyCall4)(const void *, int *);
typedef int (*CuteQTlsPrivate_TlsKeyCall5)(const void *, int *);
typedef int (*CuteQTlsPrivate_TlsKeyCall6)(const void *, int *);
typedef void (*CuteQTlsPrivate_TlsKeyCall7)(const void *, bool, int *);
typedef bool (*CuteQTlsPrivate_TlsKeyCall8)(const void *, int *);
typedef const QByteArray * (*CuteQTlsPrivate_TlsKeyCall9)(const void *, int, const QByteArray *, const QByteArray *, const QByteArray *, int *);
typedef const QByteArray * (*CuteQTlsPrivate_TlsKeyCall10)(const void *, int, const QByteArray *, const QByteArray *, const QByteArray *, int *);
class CuteQTlsPrivate_TlsKey : public QTlsPrivate::TlsKey {
public:
  using QTlsPrivate::TlsKey::TlsKey;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QTlsPrivate6TlsKey9decodeDerEN4QSsl7KeyTypeENS1_12KeyAlgorithmERK10QByteArrayS6_b")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QTlsPrivate6TlsKey9decodePemEN4QSsl7KeyTypeENS1_12KeyAlgorithmERK10QByteArrayS6_b")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey5toPemERK10QByteArray")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey6isNullEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey4typeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey9algorithmEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey6lengthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QTlsPrivate6TlsKey5clearEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey7isPkcs8Ev")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey7decryptENS_6CipherERK10QByteArrayS4_S4_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QTlsPrivate6TlsKey7encryptENS_6CipherERK10QByteArrayS4_S4_")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QTlsPrivate::TlsKey::decodeDer(KeyType type, KeyAlgorithm
  //      algorithm, const QByteArray &der, const QByteArray &passPhrase,
  //      bool deepClear)
  void decodeDer(
      QTlsPrivate::TlsKey::KeyType type,
      QTlsPrivate::TlsKey::KeyAlgorithm algorithm,
      const QByteArray &der,
      const QByteArray &passPhrase,
      bool deepClear) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall0 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall0>(taken[0]);
      call(this, static_cast<int>(type), static_cast<int>(algorithm), &der, &passPhrase, deepClear, &handled);
      if (handled) return;
    }
  }

  //  void QTlsPrivate::TlsKey::decodePem(KeyType type, KeyAlgorithm
  //      algorithm, const QByteArray &pem, const QByteArray &passPhrase,
  //      bool deepClear)
  void decodePem(
      QTlsPrivate::TlsKey::KeyType type,
      QTlsPrivate::TlsKey::KeyAlgorithm algorithm,
      const QByteArray &pem,
      const QByteArray &passPhrase,
      bool deepClear) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall1 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall1>(taken[1]);
      call(this, static_cast<int>(type), static_cast<int>(algorithm), &pem, &passPhrase, deepClear, &handled);
      if (handled) return;
    }
  }

  //  QByteArray QTlsPrivate::TlsKey::toPem(const QByteArray &passPhrase)
  //      const
  QByteArray toPem(const QByteArray &passPhrase) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall2 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall2>(taken[2]);
      const QByteArray * given = call(this, &passPhrase, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QTlsPrivate::TlsKey::isNull() const
  bool isNull() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall3 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  KeyType QTlsPrivate::TlsKey::type() const
  QTlsPrivate::TlsKey::KeyType type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall4 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::TlsKey::KeyType>(given);
    }
    return {};
  }

  //  KeyAlgorithm QTlsPrivate::TlsKey::algorithm() const
  QTlsPrivate::TlsKey::KeyAlgorithm algorithm() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall5 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QTlsPrivate::TlsKey::KeyAlgorithm>(given);
    }
    return {};
  }

  //  int QTlsPrivate::TlsKey::length() const
  int length() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall6 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QTlsPrivate::TlsKey::clear(bool deepClear)
  void clear(bool deepClear) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall7 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall7>(taken[7]);
      call(this, deepClear, &handled);
      if (handled) return;
    }
  }

  //  bool QTlsPrivate::TlsKey::isPkcs8() const
  bool isPkcs8() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall8 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::TlsKey::decrypt(Cipher cipher, const
  //      QByteArray &data, const QByteArray &passPhrase, const QByteArray
  //      &iv) const
  QByteArray decrypt(
      QTlsPrivate::Cipher cipher,
      const QByteArray &data,
      const QByteArray &passPhrase,
      const QByteArray &iv) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall9 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall9>(taken[9]);
      const QByteArray * given = call(this, static_cast<int>(cipher), &data, &passPhrase, &iv, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QByteArray QTlsPrivate::TlsKey::encrypt(Cipher cipher, const
  //      QByteArray &data, const QByteArray &key, const QByteArray &iv)
  //      const
  QByteArray encrypt(
      QTlsPrivate::Cipher cipher,
      const QByteArray &data,
      const QByteArray &key,
      const QByteArray &iv) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTlsPrivate_TlsKeyCall10 call = reinterpret_cast<CuteQTlsPrivate_TlsKeyCall10>(taken[10]);
      const QByteArray * given = call(this, static_cast<int>(cipher), &data, &key, &iv, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QTlsPrivate::TlsKey::~TlsKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate6TlsKeyD1Ev(QTlsPrivate::TlsKey *self) {
  delete self;
}

//  void QTlsPrivate::TlsKey::decodeDer(KeyType type, KeyAlgorithm algorithm,
//      const QByteArray &der, const QByteArray &passPhrase, bool deepClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate6TlsKey9decodeDerEN4QSsl7KeyTypeENS1_12KeyAlgorithmERK10QByteArrayS6_b(
    QTlsPrivate::TlsKey *self,
    QTlsPrivate::TlsKey::KeyType type,
    QTlsPrivate::TlsKey::KeyAlgorithm algorithm,
    const QByteArray *der,
    const QByteArray *passPhrase,
    bool deepClear) {
  self->decodeDer(type, algorithm, *der, *passPhrase, deepClear);
}

//  void QTlsPrivate::TlsKey::decodePem(KeyType type, KeyAlgorithm algorithm,
//      const QByteArray &pem, const QByteArray &passPhrase, bool deepClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate6TlsKey9decodePemEN4QSsl7KeyTypeENS1_12KeyAlgorithmERK10QByteArrayS6_b(
    QTlsPrivate::TlsKey *self,
    QTlsPrivate::TlsKey::KeyType type,
    QTlsPrivate::TlsKey::KeyAlgorithm algorithm,
    const QByteArray *pem,
    const QByteArray *passPhrase,
    bool deepClear) {
  self->decodePem(type, algorithm, *pem, *passPhrase, deepClear);
}

//  QByteArray QTlsPrivate::TlsKey::toPem(const QByteArray &passPhrase) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate6TlsKey5toPemERK10QByteArray(
    const QTlsPrivate::TlsKey *self,
    const QByteArray *passPhrase) {
  return new QByteArray(self->toPem(*passPhrase));
}

//  bool QTlsPrivate::TlsKey::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate6TlsKey6isNullEv(
    const QTlsPrivate::TlsKey *self) {
  return self->isNull();
}

//  KeyType QTlsPrivate::TlsKey::type() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey::KeyType ritual_ZNK11QTlsPrivate6TlsKey4typeEv(
    const QTlsPrivate::TlsKey *self) {
  return self->type();
}

//  KeyAlgorithm QTlsPrivate::TlsKey::algorithm() const
extern "C" Q_DECL_EXPORT
QTlsPrivate::TlsKey::KeyAlgorithm ritual_ZNK11QTlsPrivate6TlsKey9algorithmEv(
    const QTlsPrivate::TlsKey *self) {
  return self->algorithm();
}

//  int QTlsPrivate::TlsKey::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTlsPrivate6TlsKey6lengthEv(
    const QTlsPrivate::TlsKey *self) {
  return self->length();
}

//  void QTlsPrivate::TlsKey::clear(bool deepClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate6TlsKey5clearEb(
    QTlsPrivate::TlsKey *self,
    bool deepClear) {
  self->clear(deepClear);
}

//  bool QTlsPrivate::TlsKey::isPkcs8() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate6TlsKey7isPkcs8Ev(
    const QTlsPrivate::TlsKey *self) {
  return self->isPkcs8();
}

//  QByteArray QTlsPrivate::TlsKey::decrypt(Cipher cipher, const QByteArray
//      &data, const QByteArray &passPhrase, const QByteArray &iv) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate6TlsKey7decryptENS_6CipherERK10QByteArrayS4_S4_(
    const QTlsPrivate::TlsKey *self,
    QTlsPrivate::Cipher cipher,
    const QByteArray *data,
    const QByteArray *passPhrase,
    const QByteArray *iv) {
  return new QByteArray(self->decrypt(cipher, *data, *passPhrase, *iv));
}

//  QByteArray QTlsPrivate::TlsKey::encrypt(Cipher cipher, const QByteArray
//      &data, const QByteArray &key, const QByteArray &iv) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate6TlsKey7encryptENS_6CipherERK10QByteArrayS4_S4_(
    const QTlsPrivate::TlsKey *self,
    QTlsPrivate::Cipher cipher,
    const QByteArray *data,
    const QByteArray *key,
    const QByteArray *iv) {
  return new QByteArray(self->encrypt(cipher, *data, *key, *iv));
}

//  a Python function taken by a CuteQTlsPrivate_TlsKey, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_TlsKey(
    QTlsPrivate::TlsKey *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_TlsKey *>(self)->take(key, call);
}
