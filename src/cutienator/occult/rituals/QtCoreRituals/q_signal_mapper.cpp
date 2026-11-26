//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsignalmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsignalmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSignalMapper that Python can take functions over in. Every QSignalMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSignalMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSignalMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSignalMapper : public QSignalMapper {
public:
  using QSignalMapper::QSignalMapper;
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
      CuteQSignalMapperCall0 call = reinterpret_cast<CuteQSignalMapperCall0>(taken[0]);
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
      CuteQSignalMapperCall1 call = reinterpret_cast<CuteQSignalMapperCall1>(taken[1]);
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
      CuteQSignalMapperCall2 call = reinterpret_cast<CuteQSignalMapperCall2>(taken[2]);
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
      CuteQSignalMapperCall3 call = reinterpret_cast<CuteQSignalMapperCall3>(taken[3]);
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
      CuteQSignalMapperCall4 call = reinterpret_cast<CuteQSignalMapperCall4>(taken[4]);
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
      CuteQSignalMapperCall5 call = reinterpret_cast<CuteQSignalMapperCall5>(taken[5]);
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
      CuteQSignalMapperCall6 call = reinterpret_cast<CuteQSignalMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSignalMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSignalMapper10metaObjectEv(
    const QSignalMapper *self) {
  return self->metaObject();
}

//  void *QSignalMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QSignalMapper11qt_metacastEPKc(
    QSignalMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSignalMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSignalMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QSignalMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSignalMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSignalMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSignalMapper::tr(s, c, n));
}

//  QSignalMapperPrivate *QSignalMapper::d_func()
extern "C" Q_DECL_EXPORT
QSignalMapperPrivate *ritual_ZN13QSignalMapper6d_funcEv(
    QSignalMapper *self) {
  return self->d_func();
}

//  const QSignalMapperPrivate *QSignalMapper::d_func() const
extern "C" Q_DECL_EXPORT
const QSignalMapperPrivate *ritual_ZNK13QSignalMapper6d_funcEv(
    const QSignalMapper *self) {
  return self->d_func();
}

//  QSignalMapper::QSignalMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QSignalMapper *ritual_ZN13QSignalMapperC1EP7QObject(QObject *parent) {
  return new CuteQSignalMapper(parent);
}

//  QSignalMapper::~QSignalMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapperD1Ev(QSignalMapper *self) {
  delete self;
}

//  void QSignalMapper::setMapping(QObject *sender, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjecti(
    QSignalMapper *self,
    QObject *sender,
    int id) {
  self->setMapping(sender, id);
}

//  void QSignalMapper::setMapping(QObject *sender, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjectRK7QString(
    QSignalMapper *self,
    QObject *sender,
    const QString *text) {
  self->setMapping(sender, *text);
}

//  void QSignalMapper::setMapping(QObject *sender, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjectS1_(
    QSignalMapper *self,
    QObject *sender,
    QObject *object) {
  self->setMapping(sender, object);
}

//  void QSignalMapper::removeMappings(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper14removeMappingsEP7QObject(
    QSignalMapper *self,
    QObject *sender) {
  self->removeMappings(sender);
}

//  QObject *QSignalMapper::mapping(int id) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingEi(
    const QSignalMapper *self,
    int id) {
  return self->mapping(id);
}

//  QObject *QSignalMapper::mapping(const QString &text) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingERK7QString(
    const QSignalMapper *self,
    const QString *text) {
  return self->mapping(*text);
}

//  QObject *QSignalMapper::mapping(QObject *object) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingEP7QObject(
    const QSignalMapper *self,
    QObject *object) {
  return self->mapping(object);
}

//  void QSignalMapper::mappedInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper9mappedIntEi(QSignalMapper *self, int a0) {
  self->mappedInt(a0);
}

//  void QSignalMapper::mappedString(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper12mappedStringERK7QString(
    QSignalMapper *self,
    const QString *a0) {
  self->mappedString(*a0);
}

//  void QSignalMapper::mappedObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper12mappedObjectEP7QObject(
    QSignalMapper *self,
    QObject *a0) {
  self->mappedObject(a0);
}

//  void QSignalMapper::map()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper3mapEv(QSignalMapper *self) {
  self->map();
}

//  void QSignalMapper::map(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper3mapEP7QObject(
    QSignalMapper *self,
    QObject *sender) {
  self->map(sender);
}

//  a Python function taken by a CuteQSignalMapper, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSignalMapper(
    QSignalMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSignalMapper *>(self)->take(key, call);
}
