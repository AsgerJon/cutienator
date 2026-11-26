//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlloggingcategory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlMeta/QtQmlMeta>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlloggingcategory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlLoggingCategory that Python can take functions over in. Every QQmlLoggingCategory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlLoggingCategoryCall0)(const void *, int *);
typedef void (*CuteQQmlLoggingCategoryCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlLoggingCategoryCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlLoggingCategoryCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLoggingCategoryCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLoggingCategoryCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLoggingCategoryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLoggingCategoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLoggingCategoryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlLoggingCategory : public QQmlLoggingCategory {
public:
  using QQmlLoggingCategory::QQmlLoggingCategory;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQmlLoggingCategory::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall0 call = reinterpret_cast<CuteQQmlLoggingCategoryCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlLoggingCategory::classBegin();
  }

  //  void QQmlLoggingCategory::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall1 call = reinterpret_cast<CuteQQmlLoggingCategoryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlLoggingCategory::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall2 call = reinterpret_cast<CuteQQmlLoggingCategoryCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall3 call = reinterpret_cast<CuteQQmlLoggingCategoryCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall4 call = reinterpret_cast<CuteQQmlLoggingCategoryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall5 call = reinterpret_cast<CuteQQmlLoggingCategoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall6 call = reinterpret_cast<CuteQQmlLoggingCategoryCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall7 call = reinterpret_cast<CuteQQmlLoggingCategoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlLoggingCategoryCall8 call = reinterpret_cast<CuteQQmlLoggingCategoryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlLoggingCategory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQmlLoggingCategory10metaObjectEv(
    const QQmlLoggingCategory *self) {
  return self->metaObject();
}

//  void *QQmlLoggingCategory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQmlLoggingCategory11qt_metacastEPKc(
    QQmlLoggingCategory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlLoggingCategory::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlLoggingCategory11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlLoggingCategory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlLoggingCategory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlLoggingCategory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlLoggingCategory::tr(s, c, n));
}

//  QQmlLoggingCategory::QQmlLoggingCategory(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlLoggingCategory *ritual_ZN19QQmlLoggingCategoryC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlLoggingCategory(parent);
}

//  QQmlLoggingCategory::~QQmlLoggingCategory()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategoryD1Ev(QQmlLoggingCategory *self) {
  delete self;
}

//  DefaultLogLevel QQmlLoggingCategory::defaultLogLevel() const
extern "C" Q_DECL_EXPORT
QQmlLoggingCategory::DefaultLogLevel ritual_ZNK19QQmlLoggingCategory15defaultLogLevelEv(
    const QQmlLoggingCategory *self) {
  return self->defaultLogLevel();
}

//  void QQmlLoggingCategory::setDefaultLogLevel(DefaultLogLevel
//      defaultLogLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategory18setDefaultLogLevelENS_15DefaultLogLevelE(
    QQmlLoggingCategory *self,
    QQmlLoggingCategory::DefaultLogLevel defaultLogLevel) {
  self->setDefaultLogLevel(defaultLogLevel);
}

//  QString QQmlLoggingCategory::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLoggingCategory4nameEv(
    const QQmlLoggingCategory *self) {
  return new QString(self->name());
}

//  void QQmlLoggingCategory::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategory7setNameERK7QString(
    QQmlLoggingCategory *self,
    const QString *name) {
  self->setName(*name);
}

//  void QQmlLoggingCategory::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategory10classBeginEv(
    QQmlLoggingCategory *self) {
  self->classBegin();
}

//  void QQmlLoggingCategory::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategory17componentCompleteEv(
    QQmlLoggingCategory *self) {
  self->componentComplete();
}

//  void QQmlLoggingCategory::forceCompletion()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLoggingCategory15forceCompletionEv(
    QQmlLoggingCategory *self) {
  self->forceCompletion();
}

//  QQmlLoggingCategory as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlLoggingCategory_QQmlParserStatus(
    QQmlLoggingCategory *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlLoggingCategory, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlLoggingCategory(
    QQmlLoggingCategory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlLoggingCategory *>(self)->take(key, call);
}

//  void QQmlLoggingCategory::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlLoggingCategory10classBeginEv(
    QQmlLoggingCategory *self) {
  self->QQmlLoggingCategory::classBegin();
}

//  void QQmlLoggingCategory::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlLoggingCategory17componentCompleteEv(
    QQmlLoggingCategory *self) {
  self->QQmlLoggingCategory::componentComplete();
}
