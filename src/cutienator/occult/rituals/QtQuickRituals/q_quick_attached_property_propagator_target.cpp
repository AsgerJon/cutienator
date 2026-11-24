//  Written by dev_tooling.RitualGenerator from the records of QtQuick/6.12.0
//  /QtQuick/private/qquickattachedpropertypropagatortarget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagatortarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickAttachedPropertyPropagatorTarget that Python can take functions over in. Every QQuickAttachedPropertyPropagatorTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickAttachedPropertyPropagatorTargetCall0)(const void *, int *);
typedef void * (*CuteQQuickAttachedPropertyPropagatorTargetCall1)(const void *, const QMetaObject *, int *);
class CuteQQuickAttachedPropertyPropagatorTarget : public QQuickAttachedPropertyPropagatorTarget {
public:
  using QQuickAttachedPropertyPropagatorTarget::QQuickAttachedPropertyPropagatorTarget;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK11QMetaObject")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QQuickItem *QQuickAttachedPropertyPropagatorTarget::attacheeItem()
  //      const
  QQuickItem *attacheeItem() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorTargetCall0 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorTargetCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return {};
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickAttachedPropertyPropagatorTarget::attachedParent(const
  //      QMetaObject *attachedType) const
  QtPrivate::QQuickAttachedPropertyPropagator *attachedParent(
      const QMetaObject *attachedType) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorTargetCall1 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorTargetCall1>(taken[1]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return {};
  }
};

//  QQuickAttachedPropertyPropagatorTarget::~QQuickAttachedPropertyPropagator
//      Target()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickAttachedPropertyPropagatorTargetD1Ev(
    QQuickAttachedPropertyPropagatorTarget *self) {
  delete self;
}

//  QQuickItem *QQuickAttachedPropertyPropagatorTarget::attacheeItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv(
    const QQuickAttachedPropertyPropagatorTarget *self) {
  return self->attacheeItem();
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickAttachedPropertyPropagatorTarget::attachedParent(const
//      QMetaObject *attachedType) const
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK11QMetaObject(
    const QQuickAttachedPropertyPropagatorTarget *self,
    const QMetaObject *attachedType) {
  return self->attachedParent(attachedType);
}

//  a Python function taken by a CuteQQuickAttachedPropertyPropagatorTarget,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAttachedPropertyPropagatorTarget(
    QQuickAttachedPropertyPropagatorTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAttachedPropertyPropagatorTarget *>(self)->take(key, call);
}
