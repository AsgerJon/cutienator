//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::PreviewManager that Python can take functions over in. Every qdesigner_internal::PreviewManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_PreviewManagerCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*Cuteqdesigner_internal_PreviewManagerCall1)(const void *, const QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_PreviewManagerCall2)(const void *, const QDesignerFormWindowInterface *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_PreviewManagerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PreviewManagerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PreviewManagerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PreviewManagerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PreviewManagerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PreviewManagerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_PreviewManager : public qdesigner_internal::PreviewManager {
public:
  using qdesigner_internal::PreviewManager::PreviewManager;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14PreviewManager18previewWindowFlagsEPK7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14PreviewManager25createDeviceSkinContainerEPK28QDesignerFormWindowInterface")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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

#if !defined(QT_NO_QOBJECT)
  //  bool qdesigner_internal::PreviewManager::eventFilter(QObject
  //      *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_PreviewManagerCall0 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall0>(taken[0]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::PreviewManager::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  Qt::WindowFlags
  //      qdesigner_internal::PreviewManager::previewWindowFlags(const
  //      QWidget *widget) const
  Qt::WindowFlags previewWindowFlags(const QWidget *widget) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_PreviewManagerCall1 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall1>(taken[1]);
      int given = call(this, widget, &handled);
      if (handled) return QFlags<Qt::WindowType>::fromInt(given);
    }
    return qdesigner_internal::PreviewManager::previewWindowFlags(widget);
  }

  //  QWidget
  //      *qdesigner_internal::PreviewManager::createDeviceSkinContainer(co
  //      nst QDesignerFormWindowInterface *a0) const
  QWidget *createDeviceSkinContainer(
      const QDesignerFormWindowInterface *a0) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_PreviewManagerCall2 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall2>(taken[2]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::PreviewManager::createDeviceSkinContainer(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_PreviewManagerCall3 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_PreviewManagerCall4 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall4>(taken[4]);
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
      Cuteqdesigner_internal_PreviewManagerCall5 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall5>(taken[5]);
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
      Cuteqdesigner_internal_PreviewManagerCall6 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall6>(taken[6]);
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
      Cuteqdesigner_internal_PreviewManagerCall7 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall7>(taken[7]);
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
      Cuteqdesigner_internal_PreviewManagerCall8 call = reinterpret_cast<Cuteqdesigner_internal_PreviewManagerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::PreviewManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14PreviewManager10metaObjectEv(
    const qdesigner_internal::PreviewManager *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::PreviewManager::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14PreviewManager2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::PreviewManager::tr(s, c, n));
}

//  Qt::WindowFlags
//      qdesigner_internal::PreviewManager::previewWindowFlags(const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14PreviewManager18previewWindowFlagsEPK7QWidget(
    const qdesigner_internal::PreviewManager *self,
    const QWidget *widget) {
  return static_cast<int>(self->previewWindowFlags(widget).toInt());
}

//  QWidget
//      *qdesigner_internal::PreviewManager::createDeviceSkinContainer(const
//      QDesignerFormWindowInterface *a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal14PreviewManager25createDeviceSkinContainerEPK28QDesignerFormWindowInterface(
    const qdesigner_internal::PreviewManager *self,
    const QDesignerFormWindowInterface *a0) {
  return self->createDeviceSkinContainer(a0);
}

//  a Python function taken by a Cuteqdesigner_internal_PreviewManager, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_PreviewManager(
    qdesigner_internal::PreviewManager *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_PreviewManager *>(self)->take(key, call);
}

//  bool qdesigner_internal::PreviewManager::eventFilter(QObject *watched,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal14PreviewManager11eventFilterEP7QObjectP6QEvent(
    qdesigner_internal::PreviewManager *self,
    QObject *watched,
    QEvent *event) {
  return self->qdesigner_internal::PreviewManager::eventFilter(
      watched,
      event);
}

//  Qt::WindowFlags
//      qdesigner_internal::PreviewManager::previewWindowFlags(const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14PreviewManager18previewWindowFlagsEPK7QWidget(
    const qdesigner_internal::PreviewManager *self,
    const QWidget *widget) {
  return static_cast<int>(
      self->qdesigner_internal::PreviewManager::previewWindowFlags(
          widget).toInt());
}

//  QWidget
//      *qdesigner_internal::PreviewManager::createDeviceSkinContainer(const
//      QDesignerFormWindowInterface *a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal14PreviewManager25createDeviceSkinContainerEPK28QDesignerFormWindowInterface(
    const qdesigner_internal::PreviewManager *self,
    const QDesignerFormWindowInterface *a0) {
  return self->qdesigner_internal::PreviewManager::createDeviceSkinContainer(
      a0);
}
