//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQuickDragAttached that Python can take functions over in. Every QQuickDragAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickDragAttachedCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDragAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDragAttached : public QQuickDragAttached {
public:
  using QQuickDragAttached::QQuickDragAttached;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
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
#if QT_CONFIG(quick_draganddrop)
  //  bool QQuickDragAttached::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDragAttachedCall0 call = reinterpret_cast<CuteQQuickDragAttachedCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickDragAttached::event(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDragAttachedCall1 call = reinterpret_cast<CuteQQuickDragAttachedCall1>(taken[1]);
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
      CuteQQuickDragAttachedCall2 call = reinterpret_cast<CuteQQuickDragAttachedCall2>(taken[2]);
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
      CuteQQuickDragAttachedCall3 call = reinterpret_cast<CuteQQuickDragAttachedCall3>(taken[3]);
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
      CuteQQuickDragAttachedCall4 call = reinterpret_cast<CuteQQuickDragAttachedCall4>(taken[4]);
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
      CuteQQuickDragAttachedCall5 call = reinterpret_cast<CuteQQuickDragAttachedCall5>(taken[5]);
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
      CuteQQuickDragAttachedCall6 call = reinterpret_cast<CuteQQuickDragAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDragAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickDragAttached10metaObjectEv(
    const QQuickDragAttached *self) {
  return self->metaObject();
}

//  void *QQuickDragAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickDragAttached11qt_metacastEPKc(
    QQuickDragAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDragAttached::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDragAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDragAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDragAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickDragAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDragAttached::tr(s, c, n));
}

//  QQuickDragAttachedPrivate *QQuickDragAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickDragAttachedPrivate *ritual_ZN18QQuickDragAttached6d_funcEv(
    QQuickDragAttached *self) {
  return self->d_func();
}

//  const QQuickDragAttachedPrivate *QQuickDragAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDragAttachedPrivate *ritual_ZNK18QQuickDragAttached6d_funcEv(
    const QQuickDragAttached *self) {
  return self->d_func();
}

//  void QQuickDragAttached::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached22qt_qmlMarker_anonymousEv(
    QQuickDragAttached *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickDragAttached::QQuickDragAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDragAttached *ritual_ZN18QQuickDragAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickDragAttached(parent);
}

//  QQuickDragAttached::~QQuickDragAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttachedD1Ev(QQuickDragAttached *self) {
  delete self;
}

//  bool QQuickDragAttached::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickDragAttached8isActiveEv(
    const QQuickDragAttached *self) {
  return self->isActive();
}

//  void QQuickDragAttached::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached9setActiveEb(
    QQuickDragAttached *self,
    bool active) {
  self->setActive(active);
}

//  QObject *QQuickDragAttached::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQuickDragAttached6sourceEv(
    const QQuickDragAttached *self) {
  return self->source();
}

//  void QQuickDragAttached::setSource(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached9setSourceEP7QObject(
    QQuickDragAttached *self,
    QObject *item) {
  self->setSource(item);
}

//  void QQuickDragAttached::resetSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached11resetSourceEv(QQuickDragAttached *self) {
  self->resetSource();
}

//  QObject *QQuickDragAttached::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQuickDragAttached6targetEv(
    const QQuickDragAttached *self) {
  return self->target();
}

//  QPointF QQuickDragAttached::hotSpot() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickDragAttached7hotSpotEv(
    const QQuickDragAttached *self) {
  return new QPointF(self->hotSpot());
}

//  void QQuickDragAttached::setHotSpot(const QPointF &hotSpot)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached10setHotSpotERK7QPointF(
    QQuickDragAttached *self,
    const QPointF *hotSpot) {
  self->setHotSpot(*hotSpot);
}

//  QUrl QQuickDragAttached::imageSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickDragAttached11imageSourceEv(
    const QQuickDragAttached *self) {
  return new QUrl(self->imageSource());
}

//  void QQuickDragAttached::setImageSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached14setImageSourceERK4QUrl(
    QQuickDragAttached *self,
    const QUrl *url) {
  self->setImageSource(*url);
}

//  QSize QQuickDragAttached::imageSourceSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QQuickDragAttached15imageSourceSizeEv(
    const QQuickDragAttached *self) {
  return new QSize(self->imageSourceSize());
}

//  void QQuickDragAttached::setImageSourceSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached18setImageSourceSizeERK5QSize(
    QQuickDragAttached *self,
    const QSize *size) {
  self->setImageSourceSize(*size);
}

//  QStringList QQuickDragAttached::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QQuickDragAttached4keysEv(
    const QQuickDragAttached *self) {
  return new QList<QString>(self->keys());
}

//  void QQuickDragAttached::setKeys(const QStringList &keys)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached7setKeysERK5QListI7QStringE(
    QQuickDragAttached *self,
    const QList<QString> *keys) {
  self->setKeys(*keys);
}

//  QVariantMap QQuickDragAttached::mimeData() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK18QQuickDragAttached8mimeDataEv(
    const QQuickDragAttached *self) {
  return new QMap<QString, QVariant>(self->mimeData());
}

//  void QQuickDragAttached::setMimeData(const QVariantMap &mimeData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached11setMimeDataERK4QMapI7QString8QVariantE(
    QQuickDragAttached *self,
    const QMap<QString, QVariant> *mimeData) {
  self->setMimeData(*mimeData);
}

//  Qt::DropActions QQuickDragAttached::supportedActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickDragAttached16supportedActionsEv(
    const QQuickDragAttached *self) {
  return static_cast<int>(self->supportedActions().toInt());
}

//  void QQuickDragAttached::setSupportedActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached19setSupportedActionsE6QFlagsIN2Qt10DropActionEE(
    QQuickDragAttached *self,
    int actions) {
  self->setSupportedActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  Qt::DropAction QQuickDragAttached::proposedAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK18QQuickDragAttached14proposedActionEv(
    const QQuickDragAttached *self) {
  return self->proposedAction();
}

//  void QQuickDragAttached::setProposedAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached17setProposedActionEN2Qt10DropActionE(
    QQuickDragAttached *self,
    Qt::DropAction action) {
  self->setProposedAction(action);
}

//  QQuickDrag::DragType QQuickDragAttached::dragType() const
extern "C" Q_DECL_EXPORT
QQuickDrag::DragType ritual_ZNK18QQuickDragAttached8dragTypeEv(
    const QQuickDragAttached *self) {
  return self->dragType();
}

//  void QQuickDragAttached::setDragType(QQuickDrag::DragType dragType)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached11setDragTypeEN10QQuickDrag8DragTypeE(
    QQuickDragAttached *self,
    QQuickDrag::DragType dragType) {
  self->setDragType(dragType);
}

//  int QQuickDragAttached::drop()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDragAttached4dropEv(QQuickDragAttached *self) {
  return self->drop();
}

//  bool QQuickDragAttached::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickDragAttached5eventEP6QEvent(
    QQuickDragAttached *self,
    QEvent *event) {
  return self->event(event);
}

//  void QQuickDragAttached::start(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached5startEP14QQmlV4Function(
    QQuickDragAttached *self,
    QQmlV4FunctionPtr a0) {
  self->start(a0);
}

//  void QQuickDragAttached::startDrag(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached9startDragEP14QQmlV4Function(
    QQuickDragAttached *self,
    QQmlV4FunctionPtr a0) {
  self->startDrag(a0);
}

//  void QQuickDragAttached::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached6cancelEv(QQuickDragAttached *self) {
  self->cancel();
}

//  void QQuickDragAttached::dragStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached11dragStartedEv(QQuickDragAttached *self) {
  self->dragStarted();
}

//  void QQuickDragAttached::dragFinished(Qt::DropAction dropAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached12dragFinishedEN2Qt10DropActionE(
    QQuickDragAttached *self,
    Qt::DropAction dropAction) {
  self->dragFinished(dropAction);
}

//  void QQuickDragAttached::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached13activeChangedEv(
    QQuickDragAttached *self) {
  self->activeChanged();
}

//  void QQuickDragAttached::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached13sourceChangedEv(
    QQuickDragAttached *self) {
  self->sourceChanged();
}

//  void QQuickDragAttached::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached13targetChangedEv(
    QQuickDragAttached *self) {
  self->targetChanged();
}

//  void QQuickDragAttached::hotSpotChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached14hotSpotChangedEv(
    QQuickDragAttached *self) {
  self->hotSpotChanged();
}

//  void QQuickDragAttached::imageSourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached18imageSourceChangedEv(
    QQuickDragAttached *self) {
  self->imageSourceChanged();
}

//  void QQuickDragAttached::imageSourceSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached22imageSourceSizeChangedEv(
    QQuickDragAttached *self) {
  self->imageSourceSizeChanged();
}

//  void QQuickDragAttached::keysChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached11keysChangedEv(QQuickDragAttached *self) {
  self->keysChanged();
}

//  void QQuickDragAttached::mimeDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached15mimeDataChangedEv(
    QQuickDragAttached *self) {
  self->mimeDataChanged();
}

//  void QQuickDragAttached::supportedActionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached23supportedActionsChangedEv(
    QQuickDragAttached *self) {
  self->supportedActionsChanged();
}

//  void QQuickDragAttached::proposedActionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached21proposedActionChangedEv(
    QQuickDragAttached *self) {
  self->proposedActionChanged();
}

//  void QQuickDragAttached::dragTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDragAttached15dragTypeChangedEv(
    QQuickDragAttached *self) {
  self->dragTypeChanged();
}

//  a Python function taken by a CuteQQuickDragAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDragAttached(
    QQuickDragAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDragAttached *>(self)->take(key, call);
}

//  bool QQuickDragAttached::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickDragAttached5eventEP6QEvent(
    QQuickDragAttached *self,
    QEvent *event) {
  return self->QQuickDragAttached::event(event);
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
