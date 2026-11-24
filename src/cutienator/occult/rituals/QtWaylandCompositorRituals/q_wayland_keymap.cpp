//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandkeymap.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandkeymap.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandKeymap that Python can take functions over in. Every QWaylandKeymap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandKeymapCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandKeymapCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandKeymapCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandKeymapCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandKeymapCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandKeymapCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandKeymapCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandKeymap : public QWaylandKeymap {
public:
  using QWaylandKeymap::QWaylandKeymap;
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
      CuteQWaylandKeymapCall0 call = reinterpret_cast<CuteQWaylandKeymapCall0>(taken[0]);
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
      CuteQWaylandKeymapCall1 call = reinterpret_cast<CuteQWaylandKeymapCall1>(taken[1]);
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
      CuteQWaylandKeymapCall2 call = reinterpret_cast<CuteQWaylandKeymapCall2>(taken[2]);
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
      CuteQWaylandKeymapCall3 call = reinterpret_cast<CuteQWaylandKeymapCall3>(taken[3]);
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
      CuteQWaylandKeymapCall4 call = reinterpret_cast<CuteQWaylandKeymapCall4>(taken[4]);
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
      CuteQWaylandKeymapCall5 call = reinterpret_cast<CuteQWaylandKeymapCall5>(taken[5]);
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
      CuteQWaylandKeymapCall6 call = reinterpret_cast<CuteQWaylandKeymapCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandKeymap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWaylandKeymap10metaObjectEv(
    const QWaylandKeymap *self) {
  return self->metaObject();
}

//  QString QWaylandKeymap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWaylandKeymap2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandKeymap::tr(s, c, n));
}

//  QWaylandKeymapPrivate *QWaylandKeymap::d_func()
extern "C" Q_DECL_EXPORT
QWaylandKeymapPrivate *ritual_ZN14QWaylandKeymap6d_funcEv(
    QWaylandKeymap *self) {
  return self->d_func();
}

//  const QWaylandKeymapPrivate *QWaylandKeymap::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandKeymapPrivate *ritual_ZNK14QWaylandKeymap6d_funcEv(
    const QWaylandKeymap *self) {
  return self->d_func();
}

//  QWaylandKeymap::QWaylandKeymap(const QString &layout, const QString
//      &variant, const QString &options, const QString &model, const QString
//      &rules, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandKeymap *ritual_ZN14QWaylandKeymapC1ERK7QStringS2_S2_S2_S2_P7QObject(
    const QString *layout,
    const QString *variant,
    const QString *options,
    const QString *model,
    const QString *rules,
    QObject *parent) {
  return new CuteQWaylandKeymap(
      *layout,
      *variant,
      *options,
      *model,
      *rules,
      parent);
}

//  QString QWaylandKeymap::layout() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandKeymap6layoutEv(const QWaylandKeymap *self) {
  return new QString(self->layout());
}

//  void QWaylandKeymap::setLayout(const QString &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandKeymap9setLayoutERK7QString(
    QWaylandKeymap *self,
    const QString *layout) {
  self->setLayout(*layout);
}

//  QString QWaylandKeymap::variant() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandKeymap7variantEv(const QWaylandKeymap *self) {
  return new QString(self->variant());
}

//  void QWaylandKeymap::setVariant(const QString &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandKeymap10setVariantERK7QString(
    QWaylandKeymap *self,
    const QString *variant) {
  self->setVariant(*variant);
}

//  QString QWaylandKeymap::options() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandKeymap7optionsEv(const QWaylandKeymap *self) {
  return new QString(self->options());
}

//  void QWaylandKeymap::setOptions(const QString &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandKeymap10setOptionsERK7QString(
    QWaylandKeymap *self,
    const QString *options) {
  self->setOptions(*options);
}

//  QString QWaylandKeymap::rules() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandKeymap5rulesEv(const QWaylandKeymap *self) {
  return new QString(self->rules());
}

//  void QWaylandKeymap::setRules(const QString &rules)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandKeymap8setRulesERK7QString(
    QWaylandKeymap *self,
    const QString *rules) {
  self->setRules(*rules);
}

//  QString QWaylandKeymap::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandKeymap5modelEv(const QWaylandKeymap *self) {
  return new QString(self->model());
}

//  void QWaylandKeymap::setModel(const QString &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandKeymap8setModelERK7QString(
    QWaylandKeymap *self,
    const QString *model) {
  self->setModel(*model);
}

//  a Python function taken by a CuteQWaylandKeymap, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandKeymap(
    QWaylandKeymap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandKeymap *>(self)->take(key, call);
}
