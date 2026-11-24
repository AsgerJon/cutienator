//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobjectchangelistener_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobjectchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuick3DObjectChangeListener that Python can take functions over in. Every QQuick3DObjectChangeListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DObjectChangeListenerCall0)(const void *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall1)(const void *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall2)(const void *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall3)(const void *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall4)(const void *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall5)(const void *, QQuick3DObject *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall6)(const void *, QQuick3DObject *, QQuick3DObject *, int *);
typedef void (*CuteQQuick3DObjectChangeListenerCall7)(const void *, QQuick3DObject *, QQuick3DObject *, int *);
class CuteQQuick3DObjectChangeListener : public QQuick3DObjectChangeListener {
public:
  using QQuick3DObjectChangeListener::QQuick3DObjectChangeListener;
  CuteQQuick3DObjectChangeListener(const QQuick3DObjectChangeListener &other) : QQuick3DObjectChangeListener(other) {}
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener23itemSiblingOrderChangedEP14QQuick3DObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener21itemVisibilityChangedEP14QQuick3DObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener18itemEnabledChangedEP14QQuick3DObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener18itemOpacityChangedEP14QQuick3DObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQuick3DObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14QQuick3DObjectS1_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP14QQuick3DObjectS1_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQuick3DObjectChangeListener17itemParentChangedEP14QQuick3DObjectS1_")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void
  //      QQuick3DObjectChangeListener::itemSiblingOrderChanged(QQuick3DObj
  //      ect *a0)
  void itemSiblingOrderChanged(QQuick3DObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall0 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void
  //      QQuick3DObjectChangeListener::itemVisibilityChanged(QQuick3DObjec
  //      t *a0)
  void itemVisibilityChanged(QQuick3DObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall1 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuick3DObjectChangeListener::itemEnabledChanged(QQuick3DObject
  //      *a0)
  void itemEnabledChanged(QQuick3DObject *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall2 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuick3DObjectChangeListener::itemOpacityChanged(QQuick3DObject
  //      *a0)
  void itemOpacityChanged(QQuick3DObject *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall3 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuick3DObjectChangeListener::itemDestroyed(QQuick3DObject *a0)
  void itemDestroyed(QQuick3DObject *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall4 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemDestroyed(a0);
  }

  //  void QQuick3DObjectChangeListener::itemChildAdded(QQuick3DObject *a0,
  //      QQuick3DObject *a1)
  void itemChildAdded(QQuick3DObject *a0, QQuick3DObject *a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall5 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall5>(taken[5]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuick3DObjectChangeListener::itemChildRemoved(QQuick3DObject
  //      *a0, QQuick3DObject *a1)
  void itemChildRemoved(QQuick3DObject *a0, QQuick3DObject *a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall6 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall6>(taken[6]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuick3DObjectChangeListener::itemParentChanged(QQuick3DObject
  //      *a0, QQuick3DObject *a1)
  void itemParentChanged(QQuick3DObject *a0, QQuick3DObject *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DObjectChangeListenerCall7 call = reinterpret_cast<CuteQQuick3DObjectChangeListenerCall7>(taken[7]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuick3DObjectChangeListener::itemParentChanged(a0, a1);
  }
};

//  QQuick3DObjectChangeListener::~QQuick3DObjectChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListenerD1Ev(
    QQuick3DObjectChangeListener *self) {
  delete self;
}

//  void QQuick3DObjectChangeListener::itemSiblingOrderChanged(QQuick3DObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener23itemSiblingOrderChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->itemSiblingOrderChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemVisibilityChanged(QQuick3DObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener21itemVisibilityChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->itemVisibilityChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemEnabledChanged(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener18itemEnabledChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->itemEnabledChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemOpacityChanged(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener18itemOpacityChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->itemOpacityChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemDestroyed(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->itemDestroyed(a0);
}

//  void QQuick3DObjectChangeListener::itemChildAdded(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->itemChildAdded(a0, a1);
}

//  void QQuick3DObjectChangeListener::itemChildRemoved(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->itemChildRemoved(a0, a1);
}

//  void QQuick3DObjectChangeListener::itemParentChanged(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DObjectChangeListener17itemParentChangedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->itemParentChanged(a0, a1);
}

//  a Python function taken by a CuteQQuick3DObjectChangeListener, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DObjectChangeListener(
    QQuick3DObjectChangeListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DObjectChangeListener *>(self)->take(key, call);
}

//  void QQuick3DObjectChangeListener::itemSiblingOrderChanged(QQuick3DObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener23itemSiblingOrderChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->QQuick3DObjectChangeListener::itemSiblingOrderChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemVisibilityChanged(QQuick3DObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener21itemVisibilityChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->QQuick3DObjectChangeListener::itemVisibilityChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemEnabledChanged(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener18itemEnabledChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->QQuick3DObjectChangeListener::itemEnabledChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemOpacityChanged(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener18itemOpacityChangedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->QQuick3DObjectChangeListener::itemOpacityChanged(a0);
}

//  void QQuick3DObjectChangeListener::itemDestroyed(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQuick3DObject(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0) {
  self->QQuick3DObjectChangeListener::itemDestroyed(a0);
}

//  void QQuick3DObjectChangeListener::itemChildAdded(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->QQuick3DObjectChangeListener::itemChildAdded(a0, a1);
}

//  void QQuick3DObjectChangeListener::itemChildRemoved(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->QQuick3DObjectChangeListener::itemChildRemoved(a0, a1);
}

//  void QQuick3DObjectChangeListener::itemParentChanged(QQuick3DObject *a0,
//      QQuick3DObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DObjectChangeListener17itemParentChangedEP14QQuick3DObjectS1_(
    QQuick3DObjectChangeListener *self,
    QQuick3DObject *a0,
    QQuick3DObject *a1) {
  self->QQuick3DObjectChangeListener::itemParentChanged(a0, a1);
}
