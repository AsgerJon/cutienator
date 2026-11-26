//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickControls2/QtQuickControls2>
#include <QtQuickControls2/qquickattachedpropertypropagator.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QList>

//  A QtPrivate::QQuickAttachedPropertyPropagatorPrivate that Python can take functions over in. Every QtPrivate::QQuickAttachedPropertyPropagatorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivate : public QtPrivate::QQuickAttachedPropertyPropagatorPrivate {
public:
  using QtPrivate::QQuickAttachedPropertyPropagatorPrivate::QQuickAttachedPropertyPropagatorPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemParentChangedEP10QQuickItemS2_")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentCh
  //      anged(QQuickItem *item, QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivateCall0 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivateCall0>(taken[0]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChanged(item, parent);
  }
};

//  QQuickAttachedPropertyPropagator
//      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate6q_funcEv(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self) {
  return self->q_func();
}

//  const QQuickAttachedPropertyPropagator
//      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZNK9QtPrivate39QQuickAttachedPropertyPropagatorPrivate6q_funcEv(
    const QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self) {
  return self->q_func();
}

//  QQuickAttachedPropertyPropagatorPrivate *QtPrivate::QQuickAttachedPropert
//      yPropagatorPrivate::get(QQuickAttachedPropertyPropagator
//      *attachedObject)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagatorPrivate *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate3getEPNS_32QQuickAttachedPropertyPropagatorE(
    QtPrivate::QQuickAttachedPropertyPropagator *attachedObject) {
  return QtPrivate::QQuickAttachedPropertyPropagatorPrivate::get(
      attachedObject);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate4initEv(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self) {
  self->init();
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::attachTo(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate8attachToEP7QObject(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QObject *object) {
  self->attachTo(object);
}

//  void
//      QtPrivate::QQuickAttachedPropertyPropagatorPrivate::detachFrom(QObjec
//      t *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate10detachFromEP7QObject(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QObject *object) {
  self->detachFrom(object);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::setAttachedParen
//      t(QQuickAttachedPropertyPropagator *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17setAttachedParentEPNS_32QQuickAttachedPropertyPropagatorE(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QtPrivate::QQuickAttachedPropertyPropagator *parent) {
  self->setAttachedParent(parent);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemWindowChange
//      d(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemWindowChangedEP12QQuickWindow(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QQuickWindow *window) {
  self->itemWindowChanged(window);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::transientParentW
//      indowChanged(QWindow *newTransientParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate28transientParentWindowChangedEP7QWindow(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QWindow *newTransientParent) {
  self->transientParentWindowChanged(newTransientParent);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChange
//      d(QQuickItem *item, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemParentChangedEP10QQuickItemS2_(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->itemParentChanged(item, parent);
}

//  const QMetaObject *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::fi
//      rstCppMetaObject(QQuickAttachedPropertyPropagator *propagator)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate18firstCppMetaObjectEPNS_32QQuickAttachedPropertyPropagatorE(
    QtPrivate::QQuickAttachedPropertyPropagator *propagator) {
  return QtPrivate::QQuickAttachedPropertyPropagatorPrivate::firstCppMetaObject(
      propagator);
}

//  QQuickAttachedPropertyPropagator *QtPrivate::QQuickAttachedPropertyPropag
//      atorPrivate::findAttachedParent(const QMetaObject *attachedType,
//      QObject *attachee)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate18findAttachedParentEPK11QMetaObjectP7QObject(
    const QMetaObject *attachedType,
    QObject *attachee) {
  return QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedParent(
      attachedType,
      attachee);
}

//  QList<QQuickAttachedPropertyPropagator *> QtPrivate::QQuickAttachedProper
//      tyPropagatorPrivate::findAttachedChildren(const QMetaObject
//      *attachedType, QObject *object)
extern "C" Q_DECL_EXPORT
QList<QtPrivate::QQuickAttachedPropertyPropagator *> *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate20findAttachedChildrenEPK11QMetaObjectP7QObject(
    const QMetaObject *attachedType,
    QObject *object) {
  return new QList<QtPrivate::QQuickAttachedPropertyPropagator *>(
      QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedChildren(
          attachedType,
          object));
}

//  QQuickItem *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttac
//      hedItem(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate16findAttachedItemEP7QObject(
    QObject *object) {
  return QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedItem(
      object);
}

//  a Python function taken by a
//      CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtPrivate_QQuickAttachedPropertyPropagatorPrivate(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorPrivate *>(self)->take(key, call);
}

//  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChange
//      d(QQuickItem *item, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemParentChangedEP10QQuickItemS2_(
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChanged(
      item,
      parent);
}

//  a QList<QtPrivate::QQuickAttachedPropertyPropagator *> a ritual of
//      QtPrivate::QQuickAttachedPropertyPropagatorPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtPrivate_QQuickAttachedPropertyPropagatorPrivate__QList_QtPrivate_QQuickAttachedPropertyPropagator(
    QList<QtPrivate::QQuickAttachedPropertyPropagator *> *self) {
  delete self;
}
