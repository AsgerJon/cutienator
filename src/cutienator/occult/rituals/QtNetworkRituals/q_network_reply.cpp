//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkreply.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QNetworkReply may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkReply : QNetworkReply {
  using QNetworkReply::setSslConfigurationImplementation;
};

//  A QNetworkReply that Python can take functions over in. Every QNetworkReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkReplyCall0)(const void *, int *);
typedef bool (*CuteQNetworkReplyCall1)(const void *, int *);
typedef void (*CuteQNetworkReplyCall2)(const void *, qint64, int *);
typedef void (*CuteQNetworkReplyCall3)(const void *, int *);
typedef void (*CuteQNetworkReplyCall4)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkReplyCall5)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
typedef bool (*CuteQNetworkReplyCall6)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyCall7)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyCall8)(const void *, int *);
typedef bool (*CuteQNetworkReplyCall9)(const void *, qint64, int *);
typedef bool (*CuteQNetworkReplyCall10)(const void *, int *);
typedef bool (*CuteQNetworkReplyCall11)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyCall12)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyCall13)(const void *, int *);
typedef bool (*CuteQNetworkReplyCall14)(const void *, int *);
typedef bool (*CuteQNetworkReplyCall15)(const void *, int, int *);
typedef bool (*CuteQNetworkReplyCall16)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyCall17)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyCall18)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkReply : public QNetworkReply {
public:
  using QNetworkReply::QNetworkReply;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply17setReadBufferSizeEx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply5abortEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply15ignoreSslErrorsEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[19] = call;
      return true;
    }
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

  //  void QNetworkReply::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyCall0 call = reinterpret_cast<CuteQNetworkReplyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReply::close();
  }

  //  bool QNetworkReply::isSequential() const
  bool isSequential() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyCall1 call = reinterpret_cast<CuteQNetworkReplyCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReply::isSequential();
  }

  //  void QNetworkReply::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyCall2 call = reinterpret_cast<CuteQNetworkReplyCall2>(taken[2]);
      call(this, size, &handled);
      if (handled) return;
    }
    QNetworkReply::setReadBufferSize(size);
  }

  //  void QNetworkReply::abort()
  void abort() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkReplyCall3 call = reinterpret_cast<CuteQNetworkReplyCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QNetworkReply::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkReplyCall4 call = reinterpret_cast<CuteQNetworkReplyCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReply::ignoreSslErrors();
  }

#if QT_CONFIG(ssl)
  //  void QNetworkReply::setSslConfigurationImplementation(const
  //      QSslConfiguration &a0)
  void setSslConfigurationImplementation(
      const QSslConfiguration &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkReplyCall5 call = reinterpret_cast<CuteQNetworkReplyCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QNetworkReply::setSslConfigurationImplementation(a0);
  }
#endif  // QT_CONFIG(ssl)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkReplyCall6 call = reinterpret_cast<CuteQNetworkReplyCall6>(taken[6]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkReplyCall7 call = reinterpret_cast<CuteQNetworkReplyCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkReplyCall8 call = reinterpret_cast<CuteQNetworkReplyCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkReplyCall9 call = reinterpret_cast<CuteQNetworkReplyCall9>(taken[9]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkReplyCall10 call = reinterpret_cast<CuteQNetworkReplyCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkReplyCall11 call = reinterpret_cast<CuteQNetworkReplyCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkReplyCall12 call = reinterpret_cast<CuteQNetworkReplyCall12>(taken[12]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkReplyCall13 call = reinterpret_cast<CuteQNetworkReplyCall13>(taken[13]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkReplyCall14 call = reinterpret_cast<CuteQNetworkReplyCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkReplyCall15 call = reinterpret_cast<CuteQNetworkReplyCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkReplyCall16 call = reinterpret_cast<CuteQNetworkReplyCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkReplyCall17 call = reinterpret_cast<CuteQNetworkReplyCall17>(taken[17]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkReplyCall18 call = reinterpret_cast<CuteQNetworkReplyCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkReplyCall19 call = reinterpret_cast<CuteQNetworkReplyCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQNetworkReplyCall20 call = reinterpret_cast<CuteQNetworkReplyCall20>(taken[20]);
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
      CuteQNetworkReplyCall21 call = reinterpret_cast<CuteQNetworkReplyCall21>(taken[21]);
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
      CuteQNetworkReplyCall22 call = reinterpret_cast<CuteQNetworkReplyCall22>(taken[22]);
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
      CuteQNetworkReplyCall23 call = reinterpret_cast<CuteQNetworkReplyCall23>(taken[23]);
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
      CuteQNetworkReplyCall24 call = reinterpret_cast<CuteQNetworkReplyCall24>(taken[24]);
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
      CuteQNetworkReplyCall25 call = reinterpret_cast<CuteQNetworkReplyCall25>(taken[25]);
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
      CuteQNetworkReplyCall26 call = reinterpret_cast<CuteQNetworkReplyCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QNetworkReply10metaObjectEv(
    const QNetworkReply *self) {
  return self->metaObject();
}

//  void *QNetworkReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QNetworkReply11qt_metacastEPKc(
    QNetworkReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkReply::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QNetworkReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNetworkReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QNetworkReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkReply::tr(s, c, n));
}

//  QNetworkReply::~QNetworkReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReplyD1Ev(QNetworkReply *self) {
  delete self;
}

//  void QNetworkReply::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply5closeEv(QNetworkReply *self) {
  self->close();
}

//  bool QNetworkReply::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkReply12isSequentialEv(const QNetworkReply *self) {
  return self->isSequential();
}

//  qint64 QNetworkReply::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QNetworkReply14readBufferSizeEv(
    const QNetworkReply *self) {
  return self->readBufferSize();
}

//  void QNetworkReply::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply17setReadBufferSizeEx(
    QNetworkReply *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  QNetworkAccessManager *QNetworkReply::manager() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZNK13QNetworkReply7managerEv(
    const QNetworkReply *self) {
  return self->manager();
}

//  QNetworkAccessManager::Operation QNetworkReply::operation() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager::Operation ritual_ZNK13QNetworkReply9operationEv(
    const QNetworkReply *self) {
  return self->operation();
}

//  QNetworkRequest QNetworkReply::request() const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK13QNetworkReply7requestEv(
    const QNetworkReply *self) {
  return new QNetworkRequest(self->request());
}

//  NetworkError QNetworkReply::error() const
extern "C" Q_DECL_EXPORT
QNetworkReply::NetworkError ritual_ZNK13QNetworkReply5errorEv(
    const QNetworkReply *self) {
  return self->error();
}

//  bool QNetworkReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkReply10isFinishedEv(const QNetworkReply *self) {
  return self->isFinished();
}

//  bool QNetworkReply::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkReply9isRunningEv(const QNetworkReply *self) {
  return self->isRunning();
}

//  QUrl QNetworkReply::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QNetworkReply3urlEv(const QNetworkReply *self) {
  return new QUrl(self->url());
}

//  QVariant QNetworkReply::header(QNetworkRequest::KnownHeaders header)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QNetworkReply6headerEN15QNetworkRequest12KnownHeadersE(
    const QNetworkReply *self,
    QNetworkRequest::KnownHeaders header) {
  return new QVariant(self->header(header));
}

//  bool QNetworkReply::hasRawHeader(QAnyStringView headerName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkReply12hasRawHeaderE14QAnyStringView(
    const QNetworkReply *self,
    const QString *headerName) {
  return self->hasRawHeader(QAnyStringView(*headerName));
}

//  QList<QByteArray> QNetworkReply::rawHeaderList() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QNetworkReply13rawHeaderListEv(
    const QNetworkReply *self) {
  return new QList<QByteArray>(self->rawHeaderList());
}

//  QByteArray QNetworkReply::rawHeader(QAnyStringView headerName) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QNetworkReply9rawHeaderE14QAnyStringView(
    const QNetworkReply *self,
    const QString *headerName) {
  return new QByteArray(self->rawHeader(QAnyStringView(*headerName)));
}

//  const QList<RawHeaderPair> &QNetworkReply::rawHeaderPairs() const
extern "C" Q_DECL_EXPORT
const QList<QNetworkReply::RawHeaderPair> *ritual_ZNK13QNetworkReply14rawHeaderPairsEv(
    const QNetworkReply *self) {
  return &(self->rawHeaderPairs());
}

//  QHttpHeaders QNetworkReply::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK13QNetworkReply7headersEv(
    const QNetworkReply *self) {
  return new QHttpHeaders(self->headers());
}

//  QVariant QNetworkReply::attribute(QNetworkRequest::Attribute code) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QNetworkReply9attributeEN15QNetworkRequest9AttributeE(
    const QNetworkReply *self,
    QNetworkRequest::Attribute code) {
  return new QVariant(self->attribute(code));
}

#if QT_CONFIG(ssl)
//  QSslConfiguration QNetworkReply::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK13QNetworkReply16sslConfigurationEv(
    const QNetworkReply *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply19setSslConfigurationERK17QSslConfiguration(
    QNetworkReply *self,
    const QSslConfiguration *configuration) {
  self->setSslConfiguration(*configuration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::ignoreSslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply15ignoreSslErrorsERK5QListI9QSslErrorE(
    QNetworkReply *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}
#endif  // QT_CONFIG(ssl)

//  void QNetworkReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply5abortEv(QNetworkReply *self) {
  self->abort();
}

//  void QNetworkReply::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply15ignoreSslErrorsEv(QNetworkReply *self) {
  self->ignoreSslErrors();
}

//  void QNetworkReply::socketStartedConnecting()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply23socketStartedConnectingEv(
    QNetworkReply *self) {
  self->socketStartedConnecting();
}

//  void QNetworkReply::requestSent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply11requestSentEv(QNetworkReply *self) {
  self->requestSent();
}

//  void QNetworkReply::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply15metaDataChangedEv(QNetworkReply *self) {
  self->metaDataChanged();
}

//  void QNetworkReply::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply8finishedEv(QNetworkReply *self) {
  self->finished();
}

//  void QNetworkReply::errorOccurred(QNetworkReply::NetworkError a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply13errorOccurredENS_12NetworkErrorE(
    QNetworkReply *self,
    QNetworkReply::NetworkError a0) {
  self->errorOccurred(a0);
}

#if QT_CONFIG(ssl)
//  void QNetworkReply::encrypted()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply9encryptedEv(QNetworkReply *self) {
  self->encrypted();
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::sslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply9sslErrorsERK5QListI9QSslErrorE(
    QNetworkReply *self,
    const QList<QSslError> *errors) {
  self->sslErrors(*errors);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::preSharedKeyAuthenticationRequired(QSslPreSharedKeyAu
//      thenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply34preSharedKeyAuthenticationRequiredEP29QSslPreSharedKeyAuthenticator(
    QNetworkReply *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->preSharedKeyAuthenticationRequired(authenticator);
}
#endif  // QT_CONFIG(ssl)

//  void QNetworkReply::redirected(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply10redirectedERK4QUrl(
    QNetworkReply *self,
    const QUrl *url) {
  self->redirected(*url);
}

//  void QNetworkReply::redirectAllowed()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply15redirectAllowedEv(QNetworkReply *self) {
  self->redirectAllowed();
}

//  void QNetworkReply::uploadProgress(qint64 bytesSent, qint64 bytesTotal)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply14uploadProgressExx(
    QNetworkReply *self,
    qint64 bytesSent,
    qint64 bytesTotal) {
  self->uploadProgress(bytesSent, bytesTotal);
}

//  void QNetworkReply::downloadProgress(qint64 bytesReceived, qint64
//      bytesTotal)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply16downloadProgressExx(
    QNetworkReply *self,
    qint64 bytesReceived,
    qint64 bytesTotal) {
  self->downloadProgress(bytesReceived, bytesTotal);
}

//  QNetworkReply::QNetworkReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN13QNetworkReplyC1EP7QObject(QObject *parent) {
  return new CuteQNetworkReply(parent);
}

//  QNetworkReply::QNetworkReply(QNetworkReplyPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN13QNetworkReplyC1ER20QNetworkReplyPrivateP7QObject(
    QNetworkReplyPrivate *dd,
    QObject *parent) {
  return new CuteQNetworkReply(*dd, parent);
}

//  qint64 QNetworkReply::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13QNetworkReply9writeDataEPKcx(
    QNetworkReply *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  void QNetworkReply::setOperation(QNetworkAccessManager::Operation
//      operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply12setOperationEN21QNetworkAccessManager9OperationE(
    QNetworkReply *self,
    QNetworkAccessManager::Operation operation) {
  self->setOperation(operation);
}

//  void QNetworkReply::setRequest(const QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply10setRequestERK15QNetworkRequest(
    QNetworkReply *self,
    const QNetworkRequest *request) {
  self->setRequest(*request);
}

//  void QNetworkReply::setError(NetworkError errorCode, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply8setErrorENS_12NetworkErrorERK7QString(
    QNetworkReply *self,
    QNetworkReply::NetworkError errorCode,
    const QString *errorString) {
  self->setError(errorCode, *errorString);
}

//  void QNetworkReply::setFinished(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply11setFinishedEb(QNetworkReply *self, bool a0) {
  self->setFinished(a0);
}

//  void QNetworkReply::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply6setUrlERK4QUrl(
    QNetworkReply *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  void QNetworkReply::setHeader(QNetworkRequest::KnownHeaders header, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply9setHeaderEN15QNetworkRequest12KnownHeadersERK8QVariant(
    QNetworkReply *self,
    QNetworkRequest::KnownHeaders header,
    const QVariant *value) {
  self->setHeader(header, *value);
}

//  void QNetworkReply::setRawHeader(const QByteArray &headerName, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply12setRawHeaderERK10QByteArrayS2_(
    QNetworkReply *self,
    const QByteArray *headerName,
    const QByteArray *value) {
  self->setRawHeader(*headerName, *value);
}

//  void QNetworkReply::setHeaders(const QHttpHeaders &newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply10setHeadersERK12QHttpHeaders(
    QNetworkReply *self,
    const QHttpHeaders *newHeaders) {
  self->setHeaders(*newHeaders);
}

//  void QNetworkReply::setHeaders(QHttpHeaders &&newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply10setHeadersEO12QHttpHeaders(
    QNetworkReply *self,
    QHttpHeaders *newHeaders) {
  self->setHeaders(std::move(*newHeaders));
}

//  void QNetworkReply::setWellKnownHeader(QHttpHeaders::WellKnownHeader
//      name, QByteArrayView value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply18setWellKnownHeaderEN12QHttpHeaders15WellKnownHeaderE14QByteArrayView(
    QNetworkReply *self,
    QHttpHeaders::WellKnownHeader name,
    const QByteArrayView *value) {
  self->setWellKnownHeader(name, *value);
}

//  void QNetworkReply::setAttribute(QNetworkRequest::Attribute code, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply12setAttributeEN15QNetworkRequest9AttributeERK8QVariant(
    QNetworkReply *self,
    QNetworkRequest::Attribute code,
    const QVariant *value) {
  self->setAttribute(code, *value);
}

#if QT_CONFIG(ssl)
//  void QNetworkReply::sslConfigurationImplementation(QSslConfiguration &a0)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QNetworkReply30sslConfigurationImplementationER17QSslConfiguration(
    const QNetworkReply *self,
    QSslConfiguration *a0) {
  self->sslConfigurationImplementation(*a0);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::setSslConfigurationImplementation(const
//      QSslConfiguration &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReply *self,
    const QSslConfiguration *a0) {
  self->setSslConfigurationImplementation(*a0);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkReply::ignoreSslErrorsImplementation(const QList<QSslError>
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkReply29ignoreSslErrorsImplementationERK5QListI9QSslErrorE(
    QNetworkReply *self,
    const QList<QSslError> *a0) {
  self->ignoreSslErrorsImplementation(*a0);
}
#endif  // QT_CONFIG(ssl)

//  QNetworkReplyPrivate *QNetworkReply::d_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyPrivate *ritual_ZN13QNetworkReply6d_funcEv(
    QNetworkReply *self) {
  return self->d_func();
}

//  const QNetworkReplyPrivate *QNetworkReply::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyPrivate *ritual_ZNK13QNetworkReply6d_funcEv(
    const QNetworkReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReply(
    QNetworkReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReply *>(self)->take(key, call);
}

//  void QNetworkReply::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QNetworkReply5closeEv(QNetworkReply *self) {
  self->QNetworkReply::close();
}

//  bool QNetworkReply::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QNetworkReply12isSequentialEv(
    const QNetworkReply *self) {
  return self->QNetworkReply::isSequential();
}

//  void QNetworkReply::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QNetworkReply17setReadBufferSizeEx(
    QNetworkReply *self,
    qint64 size) {
  self->QNetworkReply::setReadBufferSize(size);
}

//  void QNetworkReply::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QNetworkReply15ignoreSslErrorsEv(QNetworkReply *self) {
  self->QNetworkReply::ignoreSslErrors();
}

#if QT_CONFIG(ssl)
//  void QNetworkReply::setSslConfigurationImplementation(const
//      QSslConfiguration &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReply *self,
    const QSslConfiguration *a0) {
  static_cast<OwnQNetworkReply *>(self)->OwnQNetworkReply::setSslConfigurationImplementation(
      *a0);
}
#endif  // QT_CONFIG(ssl)
