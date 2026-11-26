//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickLayouts/qtquicklayoutsexports.h>
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#if !defined(Q_OS_INTEGRITY)
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickFlexboxLayout that Python can take functions over in. Every QQuickFlexboxLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFlexboxLayoutCall0)(const void *, int *);
typedef const QSizeF * (*CuteQQuickFlexboxLayoutCall1)(const void *, int, int *);
typedef void (*CuteQQuickFlexboxLayoutCall2)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickFlexboxLayoutCall3)(const void *, QQuickItem *, int, int, int *);
typedef void (*CuteQQuickFlexboxLayoutCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall5)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall6)(const void *, const QSizeF *, int *);
typedef void * (*CuteQQuickFlexboxLayoutCall7)(const void *, int, int *);
typedef int (*CuteQQuickFlexboxLayoutCall8)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall14)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall15)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall16)(const void *, int *);
typedef const QRectF * (*CuteQQuickFlexboxLayoutCall17)(const void *, int *);
typedef const QRectF * (*CuteQQuickFlexboxLayoutCall18)(const void *, int *);
typedef bool (*CuteQQuickFlexboxLayoutCall19)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickFlexboxLayoutCall20)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickFlexboxLayoutCall21)(const void *, int *);
typedef void * (*CuteQQuickFlexboxLayoutCall22)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlexboxLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall24)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall26)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickFlexboxLayoutCall27)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickFlexboxLayoutCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall30)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall34)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall35)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickFlexboxLayoutCall36)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickFlexboxLayoutCall37)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall38)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall40)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlexboxLayoutCall41)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlexboxLayoutCall42)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlexboxLayoutCall43)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlexboxLayoutCall44)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickFlexboxLayoutCall45)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickFlexboxLayoutCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall47)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall48)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall49)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall50)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall51)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall52)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall53)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall54)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall55)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickFlexboxLayoutCall56)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall57)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickFlexboxLayoutCall58)(const void *, int *);
typedef bool (*CuteQQuickFlexboxLayoutCall59)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickFlexboxLayoutCall60)(const void *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall61)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFlexboxLayoutCall62)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlexboxLayoutCall63)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall64)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall65)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall66)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall67)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlexboxLayoutCall68)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFlexboxLayout : public QQuickFlexboxLayout {
public:
  using QQuickFlexboxLayout::QQuickFlexboxLayout;
  void *taken[69] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout8sizeHintEN2Qt8SizeHintE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout10invalidateEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout17updateLayoutItemsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout9rearrangeERK6QSizeF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout6itemAtEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout9itemCountEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[40] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[62] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[63] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[64] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[65] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[66] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[67] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[68] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickFlexboxLayout::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall0 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::componentComplete();
  }

  //  QSizeF QQuickFlexboxLayout::sizeHint(Qt::SizeHint whichSizeHint)
  //      const
  QSizeF sizeHint(Qt::SizeHint whichSizeHint) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall1 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall1>(taken[1]);
      const QSizeF * given = call(this, static_cast<int>(whichSizeHint), &handled);
      if (handled && given) return *given;
    }
    return QQuickFlexboxLayout::sizeHint(whichSizeHint);
  }

  //  void QQuickFlexboxLayout::setAlignment(QQuickItem *a0, Qt::Alignment
  //      a1)
  void setAlignment(QQuickItem *a0, Qt::Alignment a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall2 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall2>(taken[2]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::setAlignment(a0, a1);
  }

  //  void QQuickFlexboxLayout::setStretchFactor(QQuickItem *a0, int a1,
  //      Qt::Orientation a2)
  void setStretchFactor(
      QQuickItem *a0,
      int a1,
      Qt::Orientation a2) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall3 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall3>(taken[3]);
      call(this, a0, a1, static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::setStretchFactor(a0, a1, a2);
  }

  //  void QQuickFlexboxLayout::invalidate(QQuickItem *childItem)
  void invalidate(QQuickItem *childItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall4 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall4>(taken[4]);
      call(this, childItem, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::invalidate(childItem);
  }

  //  void QQuickFlexboxLayout::updateLayoutItems()
  void updateLayoutItems() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall5 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::updateLayoutItems();
  }

  //  void QQuickFlexboxLayout::rearrange(const QSizeF &a0)
  void rearrange(const QSizeF &a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall6 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall6>(taken[6]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::rearrange(a0);
  }

  //  QQuickItem *QQuickFlexboxLayout::itemAt(int index) const
  QQuickItem *itemAt(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall7 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall7>(taken[7]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickFlexboxLayout::itemAt(index);
  }

  //  int QQuickFlexboxLayout::itemCount() const
  int itemCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall8 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlexboxLayout::itemCount();
  }

  //  void QQuickFlexboxLayout::itemSiblingOrderChanged(QQuickItem *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall9 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::itemSiblingOrderChanged(item);
  }

  //  void QQuickFlexboxLayout::itemVisibilityChanged(QQuickItem *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall10 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickFlexboxLayout::itemVisibilityChanged(item);
  }

  //  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall11 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall11>(taken[11]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickLayout::itemChange(change, value);
  }

  //  void QQuickLayout::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall12 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLayout::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall13 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall13>(taken[13]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitWidthChanged(item);
  }

  //  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall14 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall14>(taken[14]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitHeightChanged(item);
  }

  //  void QQuickLayout::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall15 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall15>(taken[15]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemDestroyed(item);
  }

  //  void QQuickLayout::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall16 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLayout::updatePolish();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall17 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall18 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall19 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall19>(taken[19]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall20 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall20>(taken[20]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall21 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall22 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall23 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall23>(taken[23]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall24 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall25 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall26 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall27 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall28 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall29 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall30 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall31 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall32 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall33 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall34 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall35 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall36 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall37 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall38 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall39 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall40 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall41 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall42 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall43 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall44 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall45 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall45>(taken[45]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall46 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall47 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall48 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall48>(taken[48]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall49 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall50 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall50>(taken[50]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall51 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall51>(taken[51]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall52 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall52>(taken[52]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall53 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall53>(taken[53]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall54 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall55 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall55>(taken[55]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall56 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall56>(taken[56]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall57 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall57>(taken[57]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall58 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall58>(taken[58]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall59 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall59>(taken[59]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall60 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall60>(taken[60]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickItemChangeListener::debugName();
  }

  //  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
  void addSourceItem(QQuickItem *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall61 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall62 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall63 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall63>(taken[63]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall64 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall64>(taken[64]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall65 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall65>(taken[65]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall66 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall66>(taken[66]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall67 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall67>(taken[67]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQuickFlexboxLayoutCall68 call = reinterpret_cast<CuteQQuickFlexboxLayoutCall68>(taken[68]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFlexboxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickFlexboxLayout10metaObjectEv(
    const QQuickFlexboxLayout *self) {
  return self->metaObject();
}

//  void *QQuickFlexboxLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickFlexboxLayout11qt_metacastEPKc(
    QQuickFlexboxLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFlexboxLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickFlexboxLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFlexboxLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFlexboxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickFlexboxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlexboxLayout::tr(s, c, n));
}

//  void QQuickFlexboxLayout::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout21qt_qmlMarker_attachedEv(
    QQuickFlexboxLayout *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickFlexboxLayout::QQuickFlexboxLayout(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout *ritual_ZN19QQuickFlexboxLayoutC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickFlexboxLayout(parent);
}

//  QQuickFlexboxLayout::~QQuickFlexboxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayoutD1Ev(QQuickFlexboxLayout *self) {
  delete self;
}

//  FlexboxDirection QQuickFlexboxLayout::direction() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxDirection ritual_ZNK19QQuickFlexboxLayout9directionEv(
    const QQuickFlexboxLayout *self) {
  return self->direction();
}

//  void QQuickFlexboxLayout::setDirection(FlexboxDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout12setDirectionENS_16FlexboxDirectionE(
    QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxDirection a0) {
  self->setDirection(a0);
}

//  FlexboxWrap QQuickFlexboxLayout::wrap() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxWrap ritual_ZNK19QQuickFlexboxLayout4wrapEv(
    const QQuickFlexboxLayout *self) {
  return self->wrap();
}

//  void QQuickFlexboxLayout::setWrap(FlexboxWrap a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout7setWrapENS_11FlexboxWrapE(
    QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxWrap a0) {
  self->setWrap(a0);
}

//  FlexboxAlignment QQuickFlexboxLayout::alignItems() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxAlignment ritual_ZNK19QQuickFlexboxLayout10alignItemsEv(
    const QQuickFlexboxLayout *self) {
  return self->alignItems();
}

//  void QQuickFlexboxLayout::setAlignItems(FlexboxAlignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout13setAlignItemsENS_16FlexboxAlignmentE(
    QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxAlignment a0) {
  self->setAlignItems(a0);
}

//  FlexboxJustify QQuickFlexboxLayout::justifyContent() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxJustify ritual_ZNK19QQuickFlexboxLayout14justifyContentEv(
    const QQuickFlexboxLayout *self) {
  return self->justifyContent();
}

//  void QQuickFlexboxLayout::setJustifyContent(FlexboxJustify a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout17setJustifyContentENS_14FlexboxJustifyE(
    QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxJustify a0) {
  self->setJustifyContent(a0);
}

//  FlexboxAlignment QQuickFlexboxLayout::alignContent() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxAlignment ritual_ZNK19QQuickFlexboxLayout12alignContentEv(
    const QQuickFlexboxLayout *self) {
  return self->alignContent();
}

//  void QQuickFlexboxLayout::setAlignContent(FlexboxAlignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout15setAlignContentENS_16FlexboxAlignmentE(
    QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxAlignment a0) {
  self->setAlignContent(a0);
}

//  qreal QQuickFlexboxLayout::gap() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFlexboxLayout3gapEv(
    const QQuickFlexboxLayout *self) {
  return self->gap();
}

//  void QQuickFlexboxLayout::setGap(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout6setGapEd(
    QQuickFlexboxLayout *self,
    qreal a0) {
  self->setGap(a0);
}

//  void QQuickFlexboxLayout::resetGap()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout8resetGapEv(QQuickFlexboxLayout *self) {
  self->resetGap();
}

//  qreal QQuickFlexboxLayout::rowGap() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFlexboxLayout6rowGapEv(
    const QQuickFlexboxLayout *self) {
  return self->rowGap();
}

//  void QQuickFlexboxLayout::setRowGap(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout9setRowGapEd(
    QQuickFlexboxLayout *self,
    qreal a0) {
  self->setRowGap(a0);
}

//  void QQuickFlexboxLayout::resetRowGap()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout11resetRowGapEv(
    QQuickFlexboxLayout *self) {
  self->resetRowGap();
}

//  qreal QQuickFlexboxLayout::columnGap() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFlexboxLayout9columnGapEv(
    const QQuickFlexboxLayout *self) {
  return self->columnGap();
}

//  void QQuickFlexboxLayout::setColumnGap(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout12setColumnGapEd(
    QQuickFlexboxLayout *self,
    qreal a0) {
  self->setColumnGap(a0);
}

//  void QQuickFlexboxLayout::resetColumnGap()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout14resetColumnGapEv(
    QQuickFlexboxLayout *self) {
  self->resetColumnGap();
}

//  void QQuickFlexboxLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout17componentCompleteEv(
    QQuickFlexboxLayout *self) {
  self->componentComplete();
}

//  QSizeF QQuickFlexboxLayout::sizeHint(Qt::SizeHint whichSizeHint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QQuickFlexboxLayout8sizeHintEN2Qt8SizeHintE(
    const QQuickFlexboxLayout *self,
    Qt::SizeHint whichSizeHint) {
  return new QSizeF(self->sizeHint(whichSizeHint));
}

//  void QQuickFlexboxLayout::setAlignment(QQuickItem *a0, Qt::Alignment a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickFlexboxLayout *self,
    QQuickItem *a0,
    int a1) {
  self->setAlignment(a0, QFlags<Qt::AlignmentFlag>::fromInt(a1));
}

//  void QQuickFlexboxLayout::setStretchFactor(QQuickItem *a0, int a1,
//      Qt::Orientation a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickFlexboxLayout *self,
    QQuickItem *a0,
    int a1,
    Qt::Orientation a2) {
  self->setStretchFactor(a0, a1, a2);
}

//  void QQuickFlexboxLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout10invalidateEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *childItem) {
  self->invalidate(childItem);
}

//  void QQuickFlexboxLayout::updateLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout17updateLayoutItemsEv(
    QQuickFlexboxLayout *self) {
  self->updateLayoutItems();
}

//  void QQuickFlexboxLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout9rearrangeERK6QSizeF(
    QQuickFlexboxLayout *self,
    const QSizeF *a0) {
  self->rearrange(*a0);
}

//  QQuickItem *QQuickFlexboxLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK19QQuickFlexboxLayout6itemAtEi(
    const QQuickFlexboxLayout *self,
    int index) {
  return self->itemAt(index);
}

//  int QQuickFlexboxLayout::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickFlexboxLayout9itemCountEv(
    const QQuickFlexboxLayout *self) {
  return self->itemCount();
}

//  void QQuickFlexboxLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *item) {
  self->itemSiblingOrderChanged(item);
}

//  void QQuickFlexboxLayout::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout21itemVisibilityChangedEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *item) {
  self->itemVisibilityChanged(item);
}

//  QQuickFlexboxLayoutAttached
//      *QQuickFlexboxLayout::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayoutAttached *ritual_ZN19QQuickFlexboxLayout21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickFlexboxLayout::qmlAttachedProperties(object);
}

//  bool QQuickFlexboxLayout::isGapBitSet(QQuickFlexboxLayout::FlexboxGap
//      gap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFlexboxLayout11isGapBitSetENS_10FlexboxGapE(
    const QQuickFlexboxLayout *self,
    QQuickFlexboxLayout::FlexboxGap gap) {
  return self->isGapBitSet(gap);
}

//  void QQuickFlexboxLayout::checkAnchors(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickFlexboxLayout12checkAnchorsEP10QQuickItem(
    const QQuickFlexboxLayout *self,
    QQuickItem *item) {
  self->checkAnchors(item);
}

//  void QQuickFlexboxLayout::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout12countChangedEv(
    QQuickFlexboxLayout *self) {
  self->countChanged();
}

//  void QQuickFlexboxLayout::directionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout16directionChangedEv(
    QQuickFlexboxLayout *self) {
  self->directionChanged();
}

//  void QQuickFlexboxLayout::wrapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout11wrapChangedEv(
    QQuickFlexboxLayout *self) {
  self->wrapChanged();
}

//  void QQuickFlexboxLayout::alignItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout17alignItemsChangedEv(
    QQuickFlexboxLayout *self) {
  self->alignItemsChanged();
}

//  void QQuickFlexboxLayout::alignContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout19alignContentChangedEv(
    QQuickFlexboxLayout *self) {
  self->alignContentChanged();
}

//  void QQuickFlexboxLayout::justifyContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout21justifyContentChangedEv(
    QQuickFlexboxLayout *self) {
  self->justifyContentChanged();
}

//  void QQuickFlexboxLayout::gapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout10gapChangedEv(
    QQuickFlexboxLayout *self) {
  self->gapChanged();
}

//  void QQuickFlexboxLayout::rowGapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout13rowGapChangedEv(
    QQuickFlexboxLayout *self) {
  self->rowGapChanged();
}

//  void QQuickFlexboxLayout::columnGapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout16columnGapChangedEv(
    QQuickFlexboxLayout *self) {
  self->columnGapChanged();
}

//  void QQuickFlexboxLayout::childItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFlexboxLayout17childItemsChangedEv(
    QQuickFlexboxLayout *self) {
  self->childItemsChanged();
}

//  QQuickFlexboxLayoutPrivate *QQuickFlexboxLayout::d_func()
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayoutPrivate *ritual_ZN19QQuickFlexboxLayout6d_funcEv(
    QQuickFlexboxLayout *self) {
  return self->d_func();
}

//  const QQuickFlexboxLayoutPrivate *QQuickFlexboxLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFlexboxLayoutPrivate *ritual_ZNK19QQuickFlexboxLayout6d_funcEv(
    const QQuickFlexboxLayout *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickFlexboxLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFlexboxLayout(
    QQuickFlexboxLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFlexboxLayout *>(self)->take(key, call);
}

//  void QQuickFlexboxLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout17componentCompleteEv(
    QQuickFlexboxLayout *self) {
  self->QQuickFlexboxLayout::componentComplete();
}

//  QSizeF QQuickFlexboxLayout::sizeHint(Qt::SizeHint whichSizeHint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK19QQuickFlexboxLayout8sizeHintEN2Qt8SizeHintE(
    const QQuickFlexboxLayout *self,
    Qt::SizeHint whichSizeHint) {
  return new QSizeF(self->QQuickFlexboxLayout::sizeHint(whichSizeHint));
}

//  void QQuickFlexboxLayout::setAlignment(QQuickItem *a0, Qt::Alignment a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickFlexboxLayout *self,
    QQuickItem *a0,
    int a1) {
  self->QQuickFlexboxLayout::setAlignment(
      a0,
      QFlags<Qt::AlignmentFlag>::fromInt(a1));
}

//  void QQuickFlexboxLayout::setStretchFactor(QQuickItem *a0, int a1,
//      Qt::Orientation a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickFlexboxLayout *self,
    QQuickItem *a0,
    int a1,
    Qt::Orientation a2) {
  self->QQuickFlexboxLayout::setStretchFactor(a0, a1, a2);
}

//  void QQuickFlexboxLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout10invalidateEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *childItem) {
  self->QQuickFlexboxLayout::invalidate(childItem);
}

//  void QQuickFlexboxLayout::updateLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout17updateLayoutItemsEv(
    QQuickFlexboxLayout *self) {
  self->QQuickFlexboxLayout::updateLayoutItems();
}

//  void QQuickFlexboxLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout9rearrangeERK6QSizeF(
    QQuickFlexboxLayout *self,
    const QSizeF *a0) {
  self->QQuickFlexboxLayout::rearrange(*a0);
}

//  QQuickItem *QQuickFlexboxLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZNK19QQuickFlexboxLayout6itemAtEi(
    const QQuickFlexboxLayout *self,
    int index) {
  return self->QQuickFlexboxLayout::itemAt(index);
}

//  int QQuickFlexboxLayout::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickFlexboxLayout9itemCountEv(
    const QQuickFlexboxLayout *self) {
  return self->QQuickFlexboxLayout::itemCount();
}

//  void QQuickFlexboxLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *item) {
  self->QQuickFlexboxLayout::itemSiblingOrderChanged(item);
}

//  void QQuickFlexboxLayout::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickFlexboxLayout21itemVisibilityChangedEP10QQuickItem(
    QQuickFlexboxLayout *self,
    QQuickItem *item) {
  self->QQuickFlexboxLayout::itemVisibilityChanged(item);
}

#endif  // !defined(Q_OS_INTEGRITY)
