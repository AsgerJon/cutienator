//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandclient.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandclient.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWaylandClient that Python can take functions over in. Every QWaylandClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandClientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandClientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandClientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandClientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandClientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandClientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandClient : public QWaylandClient {
public:
  using QWaylandClient::QWaylandClient;
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
      CuteQWaylandClientCall0 call = reinterpret_cast<CuteQWaylandClientCall0>(taken[0]);
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
      CuteQWaylandClientCall1 call = reinterpret_cast<CuteQWaylandClientCall1>(taken[1]);
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
      CuteQWaylandClientCall2 call = reinterpret_cast<CuteQWaylandClientCall2>(taken[2]);
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
      CuteQWaylandClientCall3 call = reinterpret_cast<CuteQWaylandClientCall3>(taken[3]);
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
      CuteQWaylandClientCall4 call = reinterpret_cast<CuteQWaylandClientCall4>(taken[4]);
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
      CuteQWaylandClientCall5 call = reinterpret_cast<CuteQWaylandClientCall5>(taken[5]);
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
      CuteQWaylandClientCall6 call = reinterpret_cast<CuteQWaylandClientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWaylandClient10metaObjectEv(
    const QWaylandClient *self) {
  return self->metaObject();
}

//  void *QWaylandClient::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QWaylandClient11qt_metacastEPKc(
    QWaylandClient *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandClient::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWaylandClient11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandClient *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWaylandClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandClient::tr(s, c, n));
}

//  QWaylandClientPrivate *QWaylandClient::d_func()
extern "C" Q_DECL_EXPORT
QWaylandClientPrivate *ritual_ZN14QWaylandClient6d_funcEv(
    QWaylandClient *self) {
  return self->d_func();
}

//  const QWaylandClientPrivate *QWaylandClient::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandClientPrivate *ritual_ZNK14QWaylandClient6d_funcEv(
    const QWaylandClient *self) {
  return self->d_func();
}

//  void QWaylandClient::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandClient24qt_qmlMarker_uncreatableEv(
    QWaylandClient *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandClient::~QWaylandClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandClientD1Ev(QWaylandClient *self) {
  delete self;
}

//  TextInputProtocols QWaylandClient::textInputProtocols() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QWaylandClient18textInputProtocolsEv(
    const QWaylandClient *self) {
  return static_cast<int>(self->textInputProtocols().toInt());
}

//  void QWaylandClient::setTextInputProtocols(TextInputProtocols p)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandClient21setTextInputProtocolsE6QFlagsINS_17TextInputProtocolEE(
    QWaylandClient *self,
    int p) {
  self->setTextInputProtocols(
      QFlags<QWaylandClient::TextInputProtocol>::fromInt(p));
}

//  QWaylandClient *QWaylandClient::fromWlClient(QWaylandCompositor
//      *compositor, wl_client *wlClient)
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_ZN14QWaylandClient12fromWlClientEP18QWaylandCompositorP9wl_client(
    QWaylandCompositor *compositor,
    wl_client *wlClient) {
  return QWaylandClient::fromWlClient(compositor, wlClient);
}

//  QWaylandCompositor *QWaylandClient::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK14QWaylandClient10compositorEv(
    const QWaylandClient *self) {
  return self->compositor();
}

//  wl_client *QWaylandClient::client() const
extern "C" Q_DECL_EXPORT
wl_client *ritual_ZNK14QWaylandClient6clientEv(const QWaylandClient *self) {
  return self->client();
}

//  qint64 QWaylandClient::userId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QWaylandClient6userIdEv(const QWaylandClient *self) {
  return self->userId();
}

//  qint64 QWaylandClient::groupId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QWaylandClient7groupIdEv(const QWaylandClient *self) {
  return self->groupId();
}

//  qint64 QWaylandClient::processId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QWaylandClient9processIdEv(const QWaylandClient *self) {
  return self->processId();
}

//  void QWaylandClient::kill(int signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandClient4killEi(QWaylandClient *self, int signal) {
  self->kill(signal);
}

//  void QWaylandClient::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandClient5closeEv(QWaylandClient *self) {
  self->close();
}

//  QWaylandClient::QWaylandClient(QWaylandCompositor *compositor, wl_client
//      *client)
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_ZN14QWaylandClientC1EP18QWaylandCompositorP9wl_client(
    QWaylandCompositor *compositor,
    wl_client *client) {
  return new CuteQWaylandClient(compositor, client);
}

//  a Python function taken by a CuteQWaylandClient, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandClient(
    QWaylandClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandClient *>(self)->take(key, call);
}

//  QList<QWaylandClient *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandClient *> *ritual_list_make_QWaylandClient_ptr() {
  return new QList<QWaylandClient *>();
}

//  void QList<QWaylandClient *>::append(const QWaylandClient * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandClient_ptr(
    QList<QWaylandClient *> *self,
    QWaylandClient *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandClient *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandClient_ptr(
    const QList<QWaylandClient *> *self) {
  return self->size();
}

//  const QWaylandClient * &QList<QWaylandClient *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_list_at_QWaylandClient_ptr(
    const QList<QWaylandClient *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandClient *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandClient_ptr(QList<QWaylandClient *> *self) {
  delete self;
}
