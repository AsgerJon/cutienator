//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainteritem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCanvasPainter/qtcanvaspainterglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if 1
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if 1
#include <QtCanvasPainter/QtCanvasPainter>
#include <QtCanvasPainter/qcanvaspainteritem.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainteritem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcanvaspainteritem_p.h>
#include <QtCanvasPainter/qcanvaspainteritemrenderer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaspainteritem.cpp, line 209, as _ZN25QCanvasPainterItemPrivate11updateDebugEv
inline void QCanvasPainterItemPrivate::updateDebug()
{
    Q_Q(QCanvasPainterItem);
    if (m_debugDataChanged) {
        Q_EMIT q->debugChanged();
        m_debugDataChanged = false;
        q->update();
    }
}
//  -----------------------------------------------------------------------

//  A QCanvasPainterItemPrivate that Python can take functions over in. Every QCanvasPainterItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCanvasPainterItemPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQCanvasPainterItemPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQCanvasPainterItemPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQCanvasPainterItemPrivateCall5)(const void *, int *);
typedef qreal (*CuteQCanvasPainterItemPrivateCall6)(const void *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall7)(const void *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQCanvasPainterItemPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQCanvasPainterItemPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQCanvasPainterItemPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQCanvasPainterItemPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQCanvasPainterItemPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQCanvasPainterItemPrivateCall14)(const void *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall15)(const void *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall16)(const void *, int *);
typedef void (*CuteQCanvasPainterItemPrivateCall17)(const void *, int, int *);
class CuteQCanvasPainterItemPrivate : public QCanvasPainterItemPrivate {
public:
  using QCanvasPainterItemPrivate::QCanvasPainterItemPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[11] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall0 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall1 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall2 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall2>(taken[2]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall3 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall4 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall5 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall6 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall7 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall8 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall9 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall10 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall10>(taken[10]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall11 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall11>(taken[11]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall12 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall13 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall14 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall15 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall16 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQCanvasPainterItemPrivateCall17 call = reinterpret_cast<CuteQCanvasPainterItemPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QCanvasPainterItem *QCanvasPainterItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCanvasPainterItem *ritual_ZN25QCanvasPainterItemPrivate6q_funcEv(
    QCanvasPainterItemPrivate *self) {
  return self->q_func();
}

//  const QCanvasPainterItem *QCanvasPainterItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCanvasPainterItem *ritual_ZNK25QCanvasPainterItemPrivate6q_funcEv(
    const QCanvasPainterItemPrivate *self) {
  return self->q_func();
}

//  void QCanvasPainterItemPrivate::updateDebug()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanvasPainterItemPrivate11updateDebugEv(
    QCanvasPainterItemPrivate *self) {
  self->updateDebug();
}

//  a Python function taken by a CuteQCanvasPainterItemPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasPainterItemPrivate(
    QCanvasPainterItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasPainterItemPrivate *>(self)->take(key, call);
}

#endif  // 1
