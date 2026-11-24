//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboardtrace.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardtrace.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QVirtualKeyboardTrace may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVirtualKeyboardTrace : QVirtualKeyboardTrace {
  using QVirtualKeyboardTrace::timerEvent;
};

//  A QVirtualKeyboardTrace that Python can take functions over in. Every QVirtualKeyboardTrace
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardTraceCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardTraceCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardTraceCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardTraceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardTraceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardTraceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardTraceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardTrace : public QVirtualKeyboardTrace {
public:
  using QVirtualKeyboardTrace::QVirtualKeyboardTrace;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  void QVirtualKeyboardTrace::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQVirtualKeyboardTraceCall0 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QVirtualKeyboardTrace::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVirtualKeyboardTraceCall1 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVirtualKeyboardTraceCall2 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVirtualKeyboardTraceCall3 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall3>(taken[3]);
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
      CuteQVirtualKeyboardTraceCall4 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall4>(taken[4]);
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
      CuteQVirtualKeyboardTraceCall5 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall5>(taken[5]);
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
      CuteQVirtualKeyboardTraceCall6 call = reinterpret_cast<CuteQVirtualKeyboardTraceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardTrace::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QVirtualKeyboardTrace10metaObjectEv(
    const QVirtualKeyboardTrace *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardTrace::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QVirtualKeyboardTrace2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardTrace::tr(s, c, n));
}

//  void QVirtualKeyboardTrace::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace24qt_qmlMarker_uncreatableEv(
    QVirtualKeyboardTrace *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QVirtualKeyboardTrace::QVirtualKeyboardTrace(QObject *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardTrace *ritual_ZN21QVirtualKeyboardTraceC1EP7QObject(
    QObject *parent) {
  return new CuteQVirtualKeyboardTrace(parent);
}

//  QVirtualKeyboardTrace::~QVirtualKeyboardTrace()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTraceD1Ev(QVirtualKeyboardTrace *self) {
  delete self;
}

//  int QVirtualKeyboardTrace::traceId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QVirtualKeyboardTrace7traceIdEv(
    const QVirtualKeyboardTrace *self) {
  return self->traceId();
}

//  void QVirtualKeyboardTrace::setTraceId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace10setTraceIdEi(
    QVirtualKeyboardTrace *self,
    int id) {
  self->setTraceId(id);
}

//  QStringList QVirtualKeyboardTrace::channels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QVirtualKeyboardTrace8channelsEv(
    const QVirtualKeyboardTrace *self) {
  return new QList<QString>(self->channels());
}

//  void QVirtualKeyboardTrace::setChannels(const QStringList &channels)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace11setChannelsERK5QListI7QStringE(
    QVirtualKeyboardTrace *self,
    const QList<QString> *channels) {
  self->setChannels(*channels);
}

//  int QVirtualKeyboardTrace::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QVirtualKeyboardTrace6lengthEv(
    const QVirtualKeyboardTrace *self) {
  return self->length();
}

//  QVariantList QVirtualKeyboardTrace::points(int pos, int count) const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK21QVirtualKeyboardTrace6pointsEii(
    const QVirtualKeyboardTrace *self,
    int pos,
    int count) {
  return new QList<QVariant>(self->points(pos, count));
}

//  int QVirtualKeyboardTrace::addPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QVirtualKeyboardTrace8addPointERK7QPointF(
    QVirtualKeyboardTrace *self,
    const QPointF *point) {
  return self->addPoint(*point);
}

//  void QVirtualKeyboardTrace::setChannelData(const QString &channel, int
//      index, const QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace14setChannelDataERK7QStringiRK8QVariant(
    QVirtualKeyboardTrace *self,
    const QString *channel,
    int index,
    const QVariant *data) {
  self->setChannelData(*channel, index, *data);
}

//  QVariantList QVirtualKeyboardTrace::channelData(const QString &channel,
//      int pos, int count) const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK21QVirtualKeyboardTrace11channelDataERK7QStringii(
    const QVirtualKeyboardTrace *self,
    const QString *channel,
    int pos,
    int count) {
  return new QList<QVariant>(self->channelData(*channel, pos, count));
}

//  bool QVirtualKeyboardTrace::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QVirtualKeyboardTrace7isFinalEv(
    const QVirtualKeyboardTrace *self) {
  return self->isFinal();
}

//  void QVirtualKeyboardTrace::setFinal(bool final)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace8setFinalEb(
    QVirtualKeyboardTrace *self,
    bool final) {
  self->setFinal(final);
}

//  bool QVirtualKeyboardTrace::isCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QVirtualKeyboardTrace10isCanceledEv(
    const QVirtualKeyboardTrace *self) {
  return self->isCanceled();
}

//  void QVirtualKeyboardTrace::setCanceled(bool canceled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace11setCanceledEb(
    QVirtualKeyboardTrace *self,
    bool canceled) {
  self->setCanceled(canceled);
}

//  qreal QVirtualKeyboardTrace::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QVirtualKeyboardTrace7opacityEv(
    const QVirtualKeyboardTrace *self) {
  return self->opacity();
}

//  void QVirtualKeyboardTrace::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace10setOpacityEd(
    QVirtualKeyboardTrace *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QVirtualKeyboardTrace::startHideTimer(int delayMs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace14startHideTimerEi(
    QVirtualKeyboardTrace *self,
    int delayMs) {
  self->startHideTimer(delayMs);
}

//  void QVirtualKeyboardTrace::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVirtualKeyboardTrace10timerEventEP11QTimerEvent(
    QVirtualKeyboardTrace *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  a Python function taken by a CuteQVirtualKeyboardTrace, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardTrace(
    QVirtualKeyboardTrace *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardTrace *>(self)->take(key, call);
}

//  void QVirtualKeyboardTrace::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVirtualKeyboardTrace10timerEventEP11QTimerEvent(
    QVirtualKeyboardTrace *self,
    QTimerEvent *event) {
  static_cast<OwnQVirtualKeyboardTrace *>(self)->OwnQVirtualKeyboardTrace::timerEvent(
      event);
}

//  QList<QVirtualKeyboardTrace *>::QList()
extern "C" Q_DECL_EXPORT
QList<QVirtualKeyboardTrace *> *ritual_list_make_QVirtualKeyboardTrace_ptr() {
  return new QList<QVirtualKeyboardTrace *>();
}

//  void QList<QVirtualKeyboardTrace *>::append(const QVirtualKeyboardTrace *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QVirtualKeyboardTrace_ptr(
    QList<QVirtualKeyboardTrace *> *self,
    QVirtualKeyboardTrace *element) {
  self->append(element);
}

//  qsizetype QList<QVirtualKeyboardTrace *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QVirtualKeyboardTrace_ptr(
    const QList<QVirtualKeyboardTrace *> *self) {
  return self->size();
}

//  const QVirtualKeyboardTrace * &QList<QVirtualKeyboardTrace
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardTrace *ritual_list_at_QVirtualKeyboardTrace_ptr(
    const QList<QVirtualKeyboardTrace *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QVirtualKeyboardTrace *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QVirtualKeyboardTrace_ptr(
    QList<QVirtualKeyboardTrace *> *self) {
  delete self;
}
