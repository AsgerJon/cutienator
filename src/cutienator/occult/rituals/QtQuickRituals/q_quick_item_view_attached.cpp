//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickItemViewAttached that Python can take functions over in. Every QQuickItemViewAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemViewAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemViewAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItemViewAttached : public QQuickItemViewAttached {
public:
  using QQuickItemViewAttached::QQuickItemViewAttached;
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
      CuteQQuickItemViewAttachedCall0 call = reinterpret_cast<CuteQQuickItemViewAttachedCall0>(taken[0]);
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
      CuteQQuickItemViewAttachedCall1 call = reinterpret_cast<CuteQQuickItemViewAttachedCall1>(taken[1]);
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
      CuteQQuickItemViewAttachedCall2 call = reinterpret_cast<CuteQQuickItemViewAttachedCall2>(taken[2]);
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
      CuteQQuickItemViewAttachedCall3 call = reinterpret_cast<CuteQQuickItemViewAttachedCall3>(taken[3]);
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
      CuteQQuickItemViewAttachedCall4 call = reinterpret_cast<CuteQQuickItemViewAttachedCall4>(taken[4]);
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
      CuteQQuickItemViewAttachedCall5 call = reinterpret_cast<CuteQQuickItemViewAttachedCall5>(taken[5]);
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
      CuteQQuickItemViewAttachedCall6 call = reinterpret_cast<CuteQQuickItemViewAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItemViewAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickItemViewAttached10metaObjectEv(
    const QQuickItemViewAttached *self) {
  return self->metaObject();
}

//  QString QQuickItemViewAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickItemViewAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemViewAttached::tr(s, c, n));
}

//  QQuickItemViewAttached::QQuickItemViewAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickItemViewAttached *ritual_ZN22QQuickItemViewAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickItemViewAttached(parent);
}

//  QQuickItemViewAttached::~QQuickItemViewAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttachedD1Ev(QQuickItemViewAttached *self) {
  delete self;
}

//  bool QQuickItemViewAttached::isCurrentItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickItemViewAttached13isCurrentItemEv(
    const QQuickItemViewAttached *self) {
  return self->isCurrentItem();
}

//  void QQuickItemViewAttached::setIsCurrentItem(bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached16setIsCurrentItemEb(
    QQuickItemViewAttached *self,
    bool c) {
  self->setIsCurrentItem(c);
}

//  bool QQuickItemViewAttached::delayRemove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickItemViewAttached11delayRemoveEv(
    const QQuickItemViewAttached *self) {
  return self->delayRemove();
}

//  void QQuickItemViewAttached::setDelayRemove(bool delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached14setDelayRemoveEb(
    QQuickItemViewAttached *self,
    bool delay) {
  self->setDelayRemove(delay);
}

//  QString QQuickItemViewAttached::section() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickItemViewAttached7sectionEv(
    const QQuickItemViewAttached *self) {
  return new QString(self->section());
}

//  void QQuickItemViewAttached::setSection(const QString &sect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached10setSectionERK7QString(
    QQuickItemViewAttached *self,
    const QString *sect) {
  self->setSection(*sect);
}

//  QString QQuickItemViewAttached::prevSection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickItemViewAttached11prevSectionEv(
    const QQuickItemViewAttached *self) {
  return new QString(self->prevSection());
}

//  void QQuickItemViewAttached::setPrevSection(const QString &sect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached14setPrevSectionERK7QString(
    QQuickItemViewAttached *self,
    const QString *sect) {
  self->setPrevSection(*sect);
}

//  QString QQuickItemViewAttached::nextSection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickItemViewAttached11nextSectionEv(
    const QQuickItemViewAttached *self) {
  return new QString(self->nextSection());
}

//  void QQuickItemViewAttached::setNextSection(const QString &sect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached14setNextSectionERK7QString(
    QQuickItemViewAttached *self,
    const QString *sect) {
  self->setNextSection(*sect);
}

//  void QQuickItemViewAttached::setSections(const QString &prev, const
//      QString &sect, const QString &next)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached11setSectionsERK7QStringS2_S2_(
    QQuickItemViewAttached *self,
    const QString *prev,
    const QString *sect,
    const QString *next) {
  self->setSections(*prev, *sect, *next);
}

//  void QQuickItemViewAttached::emitAdd()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached7emitAddEv(
    QQuickItemViewAttached *self) {
  self->emitAdd();
}

//  void QQuickItemViewAttached::emitRemove()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickItemViewAttached10emitRemoveEv(
    QQuickItemViewAttached *self) {
  self->emitRemove();
}

//  a Python function taken by a CuteQQuickItemViewAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemViewAttached(
    QQuickItemViewAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemViewAttached *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_itemview)
