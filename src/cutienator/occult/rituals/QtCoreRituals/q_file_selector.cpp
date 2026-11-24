//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfileselector.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfileselector.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFileSelector that Python can take functions over in. Every QFileSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSelectorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSelectorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSelectorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSelectorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSelectorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSelectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSelectorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileSelector : public QFileSelector {
public:
  using QFileSelector::QFileSelector;
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
      CuteQFileSelectorCall0 call = reinterpret_cast<CuteQFileSelectorCall0>(taken[0]);
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
      CuteQFileSelectorCall1 call = reinterpret_cast<CuteQFileSelectorCall1>(taken[1]);
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
      CuteQFileSelectorCall2 call = reinterpret_cast<CuteQFileSelectorCall2>(taken[2]);
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
      CuteQFileSelectorCall3 call = reinterpret_cast<CuteQFileSelectorCall3>(taken[3]);
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
      CuteQFileSelectorCall4 call = reinterpret_cast<CuteQFileSelectorCall4>(taken[4]);
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
      CuteQFileSelectorCall5 call = reinterpret_cast<CuteQFileSelectorCall5>(taken[5]);
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
      CuteQFileSelectorCall6 call = reinterpret_cast<CuteQFileSelectorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QFileSelector10metaObjectEv(
    const QFileSelector *self) {
  return self->metaObject();
}

//  QString QFileSelector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFileSelector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSelector::tr(s, c, n));
}

//  QFileSelector::QFileSelector(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSelector *ritual_ZN13QFileSelectorC1EP7QObject(QObject *parent) {
  return new CuteQFileSelector(parent);
}

//  QFileSelector::~QFileSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFileSelectorD1Ev(QFileSelector *self) {
  delete self;
}

//  QString QFileSelector::select(const QString &filePath) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFileSelector6selectERK7QString(
    const QFileSelector *self,
    const QString *filePath) {
  return new QString(self->select(*filePath));
}

//  QUrl QFileSelector::select(const QUrl &filePath) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QFileSelector6selectERK4QUrl(
    const QFileSelector *self,
    const QUrl *filePath) {
  return new QUrl(self->select(*filePath));
}

//  QStringList QFileSelector::extraSelectors() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QFileSelector14extraSelectorsEv(
    const QFileSelector *self) {
  return new QList<QString>(self->extraSelectors());
}

//  void QFileSelector::setExtraSelectors(const QStringList &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFileSelector17setExtraSelectorsERK5QListI7QStringE(
    QFileSelector *self,
    const QList<QString> *list) {
  self->setExtraSelectors(*list);
}

//  QStringList QFileSelector::allSelectors() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QFileSelector12allSelectorsEv(
    const QFileSelector *self) {
  return new QList<QString>(self->allSelectors());
}

//  QFileSelectorPrivate *QFileSelector::d_func()
extern "C" Q_DECL_EXPORT
QFileSelectorPrivate *ritual_ZN13QFileSelector6d_funcEv(
    QFileSelector *self) {
  return self->d_func();
}

//  const QFileSelectorPrivate *QFileSelector::d_func() const
extern "C" Q_DECL_EXPORT
const QFileSelectorPrivate *ritual_ZNK13QFileSelector6d_funcEv(
    const QFileSelector *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQFileSelector, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSelector(
    QFileSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSelector *>(self)->take(key, call);
}
