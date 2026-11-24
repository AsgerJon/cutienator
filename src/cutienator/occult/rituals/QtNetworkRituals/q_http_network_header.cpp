//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QHttpNetworkHeader that Python can take functions over in. Every QHttpNetworkHeader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef const QUrl * (*CuteQHttpNetworkHeaderCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkHeaderCall1)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkHeaderCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkHeaderCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpNetworkHeaderCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkHeaderCall5)(const void *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QHttpHeaders * (*CuteQHttpNetworkHeaderCall6)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QByteArray * (*CuteQHttpNetworkHeaderCall7)(const void *, const QByteArrayView *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkHeaderCall8)(const void *, const QByteArray *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
class CuteQHttpNetworkHeader : public QHttpNetworkHeader {
public:
  using QHttpNetworkHeader::QHttpNetworkHeader;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader3urlEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader6setUrlERK4QUrl")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12majorVersionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12minorVersionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader13contentLengthEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader16setContentLengthEx")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader6headerEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QByteArray")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
    return false;
  }

#if QT_CONFIG(http)
  //  QUrl QHttpNetworkHeader::url() const
  QUrl url() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall0 call = reinterpret_cast<CuteQHttpNetworkHeaderCall0>(taken[0]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkHeader::setUrl(const QUrl &url)
  void setUrl(const QUrl &url) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall1 call = reinterpret_cast<CuteQHttpNetworkHeaderCall1>(taken[1]);
      call(this, &url, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkHeader::majorVersion() const
  int majorVersion() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall2 call = reinterpret_cast<CuteQHttpNetworkHeaderCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkHeader::minorVersion() const
  int minorVersion() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall3 call = reinterpret_cast<CuteQHttpNetworkHeaderCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpNetworkHeader::contentLength() const
  qint64 contentLength() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall4 call = reinterpret_cast<CuteQHttpNetworkHeaderCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkHeader::setContentLength(qint64 length)
  void setContentLength(qint64 length) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall5 call = reinterpret_cast<CuteQHttpNetworkHeaderCall5>(taken[5]);
      call(this, length, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QHttpHeaders QHttpNetworkHeader::header() const
  QHttpHeaders header() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall6 call = reinterpret_cast<CuteQHttpNetworkHeaderCall6>(taken[6]);
      const QHttpHeaders * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QByteArray QHttpNetworkHeader::headerField(QByteArrayView name, const
  //      QByteArray &defaultValue) const
  QByteArray headerField(
      QByteArrayView name,
      const QByteArray &defaultValue) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall7 call = reinterpret_cast<CuteQHttpNetworkHeaderCall7>(taken[7]);
      const QByteArray * given = call(this, &name, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkHeader::setHeaderField(const QByteArray &name, const
  //      QByteArray &data)
  void setHeaderField(
      const QByteArray &name,
      const QByteArray &data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpNetworkHeaderCall8 call = reinterpret_cast<CuteQHttpNetworkHeaderCall8>(taken[8]);
      call(this, &name, &data, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(http)
};

//  QHttpNetworkHeader::~QHttpNetworkHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpNetworkHeaderD1Ev(QHttpNetworkHeader *self) {
  delete self;
}

//  QUrl QHttpNetworkHeader::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QHttpNetworkHeader3urlEv(const QHttpNetworkHeader *self) {
  return new QUrl(self->url());
}

//  void QHttpNetworkHeader::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpNetworkHeader6setUrlERK4QUrl(
    QHttpNetworkHeader *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  int QHttpNetworkHeader::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHttpNetworkHeader12majorVersionEv(
    const QHttpNetworkHeader *self) {
  return self->majorVersion();
}

//  int QHttpNetworkHeader::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHttpNetworkHeader12minorVersionEv(
    const QHttpNetworkHeader *self) {
  return self->minorVersion();
}

//  qint64 QHttpNetworkHeader::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QHttpNetworkHeader13contentLengthEv(
    const QHttpNetworkHeader *self) {
  return self->contentLength();
}

//  void QHttpNetworkHeader::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpNetworkHeader16setContentLengthEx(
    QHttpNetworkHeader *self,
    qint64 length) {
  self->setContentLength(length);
}

//  QHttpHeaders QHttpNetworkHeader::header() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK18QHttpNetworkHeader6headerEv(
    const QHttpNetworkHeader *self) {
  return new QHttpHeaders(self->header());
}

//  QByteArray QHttpNetworkHeader::headerField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkHeader *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->headerField(*name, *defaultValue));
}

//  void QHttpNetworkHeader::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkHeader *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->setHeaderField(*name, *data);
}

//  a Python function taken by a CuteQHttpNetworkHeader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpNetworkHeader(
    QHttpNetworkHeader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpNetworkHeader *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
