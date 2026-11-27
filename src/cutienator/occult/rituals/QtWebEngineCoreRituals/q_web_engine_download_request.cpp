//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginedownloadrequest.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebenginedownloadrequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineDownloadRequest that Python can take functions over in. Every QWebEngineDownloadRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineDownloadRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineDownloadRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineDownloadRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineDownloadRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineDownloadRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineDownloadRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineDownloadRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineDownloadRequest : public QWebEngineDownloadRequest {
public:
  using QWebEngineDownloadRequest::QWebEngineDownloadRequest;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall0 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall1 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall2 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall3 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall4 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall5 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebEngineDownloadRequestCall6 call = reinterpret_cast<CuteQWebEngineDownloadRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineDownloadRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QWebEngineDownloadRequest10metaObjectEv(
    const QWebEngineDownloadRequest *self) {
  return self->metaObject();
}

//  void *QWebEngineDownloadRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QWebEngineDownloadRequest11qt_metacastEPKc(
    QWebEngineDownloadRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineDownloadRequest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QWebEngineDownloadRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineDownloadRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineDownloadRequest::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QWebEngineDownloadRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineDownloadRequest::tr(s, c, n));
}

//  QWebEngineDownloadRequest::~QWebEngineDownloadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequestD1Ev(
    QWebEngineDownloadRequest *self) {
  delete self;
}

//  quint32 QWebEngineDownloadRequest::id() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QWebEngineDownloadRequest2idEv(
    const QWebEngineDownloadRequest *self) {
  return self->id();
}

//  DownloadState QWebEngineDownloadRequest::state() const
extern "C" Q_DECL_EXPORT
QWebEngineDownloadRequest::DownloadState ritual_ZNK25QWebEngineDownloadRequest5stateEv(
    const QWebEngineDownloadRequest *self) {
  return self->state();
}

//  qint64 QWebEngineDownloadRequest::totalBytes() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QWebEngineDownloadRequest10totalBytesEv(
    const QWebEngineDownloadRequest *self) {
  return self->totalBytes();
}

//  qint64 QWebEngineDownloadRequest::receivedBytes() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QWebEngineDownloadRequest13receivedBytesEv(
    const QWebEngineDownloadRequest *self) {
  return self->receivedBytes();
}

//  QUrl QWebEngineDownloadRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QWebEngineDownloadRequest3urlEv(
    const QWebEngineDownloadRequest *self) {
  return new QUrl(self->url());
}

//  QString QWebEngineDownloadRequest::mimeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWebEngineDownloadRequest8mimeTypeEv(
    const QWebEngineDownloadRequest *self) {
  return new QString(self->mimeType());
}

//  bool QWebEngineDownloadRequest::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QWebEngineDownloadRequest10isFinishedEv(
    const QWebEngineDownloadRequest *self) {
  return self->isFinished();
}

//  bool QWebEngineDownloadRequest::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QWebEngineDownloadRequest8isPausedEv(
    const QWebEngineDownloadRequest *self) {
  return self->isPaused();
}

//  SavePageFormat QWebEngineDownloadRequest::savePageFormat() const
extern "C" Q_DECL_EXPORT
QWebEngineDownloadRequest::SavePageFormat ritual_ZNK25QWebEngineDownloadRequest14savePageFormatEv(
    const QWebEngineDownloadRequest *self) {
  return self->savePageFormat();
}

//  void QWebEngineDownloadRequest::setSavePageFormat(SavePageFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest17setSavePageFormatENS_14SavePageFormatE(
    QWebEngineDownloadRequest *self,
    QWebEngineDownloadRequest::SavePageFormat format) {
  self->setSavePageFormat(format);
}

//  DownloadInterruptReason QWebEngineDownloadRequest::interruptReason()
//      const
extern "C" Q_DECL_EXPORT
QWebEngineDownloadRequest::DownloadInterruptReason ritual_ZNK25QWebEngineDownloadRequest15interruptReasonEv(
    const QWebEngineDownloadRequest *self) {
  return self->interruptReason();
}

//  QString QWebEngineDownloadRequest::interruptReasonString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWebEngineDownloadRequest21interruptReasonStringEv(
    const QWebEngineDownloadRequest *self) {
  return new QString(self->interruptReasonString());
}

//  bool QWebEngineDownloadRequest::isSavePageDownload() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QWebEngineDownloadRequest18isSavePageDownloadEv(
    const QWebEngineDownloadRequest *self) {
  return self->isSavePageDownload();
}

//  QString QWebEngineDownloadRequest::suggestedFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWebEngineDownloadRequest17suggestedFileNameEv(
    const QWebEngineDownloadRequest *self) {
  return new QString(self->suggestedFileName());
}

//  QString QWebEngineDownloadRequest::downloadDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWebEngineDownloadRequest17downloadDirectoryEv(
    const QWebEngineDownloadRequest *self) {
  return new QString(self->downloadDirectory());
}

//  void QWebEngineDownloadRequest::setDownloadDirectory(const QString
//      &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest20setDownloadDirectoryERK7QString(
    QWebEngineDownloadRequest *self,
    const QString *directory) {
  self->setDownloadDirectory(*directory);
}

//  QString QWebEngineDownloadRequest::downloadFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWebEngineDownloadRequest16downloadFileNameEv(
    const QWebEngineDownloadRequest *self) {
  return new QString(self->downloadFileName());
}

//  void QWebEngineDownloadRequest::setDownloadFileName(const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest19setDownloadFileNameERK7QString(
    QWebEngineDownloadRequest *self,
    const QString *fileName) {
  self->setDownloadFileName(*fileName);
}

//  QWebEnginePage *QWebEngineDownloadRequest::page() const
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZNK25QWebEngineDownloadRequest4pageEv(
    const QWebEngineDownloadRequest *self) {
  return self->page();
}

//  void QWebEngineDownloadRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest6acceptEv(
    QWebEngineDownloadRequest *self) {
  self->accept();
}

//  void QWebEngineDownloadRequest::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest6cancelEv(
    QWebEngineDownloadRequest *self) {
  self->cancel();
}

//  void QWebEngineDownloadRequest::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest5pauseEv(
    QWebEngineDownloadRequest *self) {
  self->pause();
}

//  void QWebEngineDownloadRequest::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest6resumeEv(
    QWebEngineDownloadRequest *self) {
  self->resume();
}

//  void QWebEngineDownloadRequest::stateChanged(QWebEngineDownloadRequest::D
//      ownloadState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest12stateChangedENS_13DownloadStateE(
    QWebEngineDownloadRequest *self,
    QWebEngineDownloadRequest::DownloadState state) {
  self->stateChanged(state);
}

//  void QWebEngineDownloadRequest::savePageFormatChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest21savePageFormatChangedEv(
    QWebEngineDownloadRequest *self) {
  self->savePageFormatChanged();
}

//  void QWebEngineDownloadRequest::receivedBytesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest20receivedBytesChangedEv(
    QWebEngineDownloadRequest *self) {
  self->receivedBytesChanged();
}

//  void QWebEngineDownloadRequest::totalBytesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest17totalBytesChangedEv(
    QWebEngineDownloadRequest *self) {
  self->totalBytesChanged();
}

//  void QWebEngineDownloadRequest::interruptReasonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest22interruptReasonChangedEv(
    QWebEngineDownloadRequest *self) {
  self->interruptReasonChanged();
}

//  void QWebEngineDownloadRequest::isFinishedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest17isFinishedChangedEv(
    QWebEngineDownloadRequest *self) {
  self->isFinishedChanged();
}

//  void QWebEngineDownloadRequest::isPausedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest15isPausedChangedEv(
    QWebEngineDownloadRequest *self) {
  self->isPausedChanged();
}

//  void QWebEngineDownloadRequest::downloadDirectoryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest24downloadDirectoryChangedEv(
    QWebEngineDownloadRequest *self) {
  self->downloadDirectoryChanged();
}

//  void QWebEngineDownloadRequest::downloadFileNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWebEngineDownloadRequest23downloadFileNameChangedEv(
    QWebEngineDownloadRequest *self) {
  self->downloadFileNameChanged();
}

//  QWebEngineDownloadRequestPrivate *QWebEngineDownloadRequest::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineDownloadRequestPrivate *ritual_ZN25QWebEngineDownloadRequest6d_funcEv(
    QWebEngineDownloadRequest *self) {
  return self->d_func();
}

//  const QWebEngineDownloadRequestPrivate
//      *QWebEngineDownloadRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineDownloadRequestPrivate *ritual_ZNK25QWebEngineDownloadRequest6d_funcEv(
    const QWebEngineDownloadRequest *self) {
  return self->d_func();
}

//  QWebEngineDownloadRequest::QWebEngineDownloadRequest(QWebEngineDownloadRe
//      questPrivate *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineDownloadRequest *ritual_ZN25QWebEngineDownloadRequestC1EP32QWebEngineDownloadRequestPrivateP7QObject(
    QWebEngineDownloadRequestPrivate *a0,
    QObject *parent) {
  return new CuteQWebEngineDownloadRequest(a0, parent);
}

//  a Python function taken by a CuteQWebEngineDownloadRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineDownloadRequest(
    QWebEngineDownloadRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineDownloadRequest *>(self)->take(key, call);
}
