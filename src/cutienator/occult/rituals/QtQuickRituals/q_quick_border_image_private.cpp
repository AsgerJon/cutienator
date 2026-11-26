//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickborderimage_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickborderimage_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickborderimage_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickborderimage_p.h>
#include <QtQuick/private/qquickborderimage_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlengine.h>
#if QT_CONFIG(qml_network)
#include <QtNetwork/qnetworkreply.h>
#endif
#include <QtCore/qfile.h>
#include <QtCore/qmath.h>
#include <QtGui/qguiapplication.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickborderimage.cpp, line 465, as _ZN24QQuickBorderImagePrivate14calculateRectsEPK15QQuickScaleGridRK5QSizeRK6QSizeFiidP6QRectFSA_SA_SA_
inline void QQuickBorderImagePrivate::calculateRects(const QQuickScaleGrid *border,
                                              const QSize &sourceSize,
                                              const QSizeF &targetSize,
                                              int horizontalTileMode,
                                              int verticalTileMode,
                                              qreal devicePixelRatio,
                                              QRectF *targetRect,
                                              QRectF *innerTargetRect,
                                              QRectF *innerSourceRect,
                                              QRectF *subSourceRect)
{
    *innerSourceRect = QRectF(0, 0, 1, 1);
    *targetRect = QRectF(0, 0, targetSize.width(), targetSize.height());
    *innerTargetRect = *targetRect;

    if (border) {
        qreal borderLeft = border->left() * devicePixelRatio;
        qreal borderRight = border->right() * devicePixelRatio;
        qreal borderTop = border->top() * devicePixelRatio;
        qreal borderBottom = border->bottom() * devicePixelRatio;
        if (borderLeft + borderRight > sourceSize.width() && borderLeft < sourceSize.width())
            borderRight = sourceSize.width() - borderLeft;
        if (borderTop + borderBottom > sourceSize.height() && borderTop < sourceSize.height())
            borderBottom = sourceSize.height() - borderTop;
        *innerSourceRect = QRectF(QPointF(borderLeft / qreal(sourceSize.width()),
                                          borderTop / qreal(sourceSize.height())),
                                  QPointF((sourceSize.width() - borderRight) / qreal(sourceSize.width()),
                                          (sourceSize.height() - borderBottom) / qreal(sourceSize.height()))),
        *innerTargetRect = QRectF(border->left(),
                                  border->top(),
                                  qMax<qreal>(0, targetSize.width() - (border->right() + border->left())),
                                  qMax<qreal>(0, targetSize.height() - (border->bottom() + border->top())));
    }

    qreal hTiles = 1;
    qreal vTiles = 1;
    const QSizeF innerTargetSize = innerTargetRect->size() * devicePixelRatio;
    if (innerSourceRect->width() <= 0)
        hTiles = 0;
    else if (horizontalTileMode != QQuickBorderImage::Stretch) {
        hTiles = innerTargetSize.width() / qreal(innerSourceRect->width() * sourceSize.width());
        if (horizontalTileMode == QQuickBorderImage::Round)
            hTiles = qCeil(hTiles);
    }
    if (innerSourceRect->height() <= 0)
        vTiles = 0;
    else if (verticalTileMode != QQuickBorderImage::Stretch) {
        vTiles = innerTargetSize.height() / qreal(innerSourceRect->height() * sourceSize.height());
        if (verticalTileMode == QQuickBorderImage::Round)
            vTiles = qCeil(vTiles);
    }

    *subSourceRect = QRectF(0, 0, hTiles, vTiles);
}
//  -----------------------------------------------------------------------

//  A QQuickBorderImagePrivate that Python can take functions over in. Every QQuickBorderImagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickBorderImagePrivateCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickBorderImagePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickBorderImagePrivateCall3)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall4)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickBorderImagePrivateCall5)(const void *, int, int *);
typedef qreal (*CuteQQuickBorderImagePrivateCall6)(const void *, int *);
typedef qreal (*CuteQQuickBorderImagePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall8)(const void *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickBorderImagePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickBorderImagePrivateCall11)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickBorderImagePrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickBorderImagePrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickBorderImagePrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickBorderImagePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall17)(const void *, int *);
typedef void (*CuteQQuickBorderImagePrivateCall18)(const void *, int, int *);
class CuteQQuickBorderImagePrivate : public QQuickBorderImagePrivate {
public:
  using QQuickBorderImagePrivate::QQuickBorderImagePrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
  //      targetDevicePixelRatio)
  bool updateDevicePixelRatio(qreal targetDevicePixelRatio) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall0 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall0>(taken[0]);
      bool given = call(this, targetDevicePixelRatio, &handled);
      if (handled) return given;
    }
    return QQuickImageBasePrivate::updateDevicePixelRatio(targetDevicePixelRatio);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall1 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall2 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall3 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall3>(taken[3]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall4 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall4>(taken[4]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall5 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall6 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall7 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall8 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall9 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall10 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall11 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall11>(taken[11]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall12 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall12>(taken[12]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall13 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall14 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall15 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall16 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall17 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickBorderImagePrivateCall18 call = reinterpret_cast<CuteQQuickBorderImagePrivateCall18>(taken[18]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickBorderImage *QQuickBorderImagePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickBorderImage *ritual_ZN24QQuickBorderImagePrivate6q_funcEv(
    QQuickBorderImagePrivate *self) {
  return self->q_func();
}

//  const QQuickBorderImage *QQuickBorderImagePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickBorderImage *ritual_ZNK24QQuickBorderImagePrivate6q_funcEv(
    const QQuickBorderImagePrivate *self) {
  return self->q_func();
}

//  QQuickBorderImagePrivate::QQuickBorderImagePrivate()
extern "C" Q_DECL_EXPORT
QQuickBorderImagePrivate *ritual_ZN24QQuickBorderImagePrivateC1Ev() {
  return new CuteQQuickBorderImagePrivate();
}

//  QQuickBorderImagePrivate::~QQuickBorderImagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBorderImagePrivateD1Ev(
    QQuickBorderImagePrivate *self) {
  delete self;
}

//  QQuickScaleGrid *QQuickBorderImagePrivate::getScaleGrid()
extern "C" Q_DECL_EXPORT
QQuickScaleGrid *ritual_ZN24QQuickBorderImagePrivate12getScaleGridEv(
    QQuickBorderImagePrivate *self) {
  return self->getScaleGrid();
}

//  void QQuickBorderImagePrivate::calculateRects(const QQuickScaleGrid
//      *border, const QSize &sourceSize, const QSizeF &targetSize, int
//      horizontalTileMode, int verticalTileMode, qreal devicePixelRatio,
//      QRectF *targetRect, QRectF *innerTargetRect, QRectF *innerSourceRect,
//      QRectF *subSourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBorderImagePrivate14calculateRectsEPK15QQuickScaleGridRK5QSizeRK6QSizeFiidP6QRectFSA_SA_SA_(
    const QQuickScaleGrid *border,
    const QSize *sourceSize,
    const QSizeF *targetSize,
    int horizontalTileMode,
    int verticalTileMode,
    qreal devicePixelRatio,
    QRectF *targetRect,
    QRectF *innerTargetRect,
    QRectF *innerSourceRect,
    QRectF *subSourceRect) {
  QQuickBorderImagePrivate::calculateRects(
      border,
      *sourceSize,
      *targetSize,
      horizontalTileMode,
      verticalTileMode,
      devicePixelRatio,
      targetRect,
      innerTargetRect,
      innerSourceRect,
      subSourceRect);
}

//  a Python function taken by a CuteQQuickBorderImagePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBorderImagePrivate(
    QQuickBorderImagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBorderImagePrivate *>(self)->take(key, call);
}
