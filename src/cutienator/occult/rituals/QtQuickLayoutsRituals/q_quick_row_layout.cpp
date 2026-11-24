//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h>
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

//  A QQuickRowLayout that Python can take functions over in. Every QQuickRowLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRowLayoutCall0)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall1)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall2)(const void *, QQuickItem *, int *);
typedef const QSizeF * (*CuteQQuickRowLayoutCall3)(const void *, int, int *);
typedef void (*CuteQQuickRowLayoutCall4)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickRowLayoutCall5)(const void *, QQuickItem *, int, int, int *);
typedef void (*CuteQQuickRowLayoutCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall8)(const void *, int *);
typedef void * (*CuteQQuickRowLayoutCall9)(const void *, int, int *);
typedef int (*CuteQQuickRowLayoutCall10)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall11)(const void *, const QSizeF *, int *);
typedef void (*CuteQQuickRowLayoutCall12)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickRowLayoutCall13)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRowLayoutCall14)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall15)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall17)(const void *, int *);
typedef const QRectF * (*CuteQQuickRowLayoutCall18)(const void *, int *);
typedef const QRectF * (*CuteQQuickRowLayoutCall19)(const void *, int *);
typedef bool (*CuteQQuickRowLayoutCall20)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRowLayoutCall21)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRowLayoutCall22)(const void *, int *);
typedef void * (*CuteQQuickRowLayoutCall23)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRowLayoutCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall25)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall27)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRowLayoutCall28)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRowLayoutCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall34)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall35)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall36)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRowLayoutCall37)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRowLayoutCall38)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRowLayoutCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRowLayoutCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRowLayoutCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRowLayoutCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRowLayoutCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRowLayoutCall46)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickRowLayoutCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRowLayoutCall48)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall49)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickRowLayoutCall50)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall51)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall52)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall53)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall54)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall55)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall56)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickRowLayoutCall57)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall58)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickRowLayoutCall59)(const void *, int *);
typedef bool (*CuteQQuickRowLayoutCall60)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickRowLayoutCall61)(const void *, int *);
typedef void (*CuteQQuickRowLayoutCall62)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickRowLayoutCall63)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRowLayoutCall64)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall65)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall66)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall67)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall68)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRowLayoutCall69)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRowLayout : public QQuickRowLayout {
public:
  using QQuickRowLayout::QQuickRowLayout;
  void *taken[70] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickGridLayoutBase17insertLayoutItemsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout10invalidateEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout8sizeHintEN2Qt8SizeHintE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout17updateLayoutItemsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout6itemAtEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout9itemCountEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout9rearrangeERK6QSizeF")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[23] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[36] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[41] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[63] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[64] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[65] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[66] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[67] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[68] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[69] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickLinearLayout::insertLayoutItems()
  void insertLayoutItems() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRowLayoutCall0 call = reinterpret_cast<CuteQQuickRowLayoutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLinearLayout::insertLayoutItems();
  }

  //  void QQuickGridLayoutBase::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRowLayoutCall1 call = reinterpret_cast<CuteQQuickRowLayoutCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::componentComplete();
  }

  //  void QQuickGridLayoutBase::invalidate(QQuickItem *childItem)
  void invalidate(QQuickItem *childItem) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRowLayoutCall2 call = reinterpret_cast<CuteQQuickRowLayoutCall2>(taken[2]);
      call(this, childItem, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::invalidate(childItem);
  }

  //  QSizeF QQuickGridLayoutBase::sizeHint(Qt::SizeHint whichSizeHint)
  //      const
  QSizeF sizeHint(Qt::SizeHint whichSizeHint) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRowLayoutCall3 call = reinterpret_cast<CuteQQuickRowLayoutCall3>(taken[3]);
      const QSizeF * given = call(this, static_cast<int>(whichSizeHint), &handled);
      if (handled && given) return *given;
    }
    return QQuickGridLayoutBase::sizeHint(whichSizeHint);
  }

  //  void QQuickGridLayoutBase::setAlignment(QQuickItem *item,
  //      Qt::Alignment align)
  void setAlignment(QQuickItem *item, Qt::Alignment align) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRowLayoutCall4 call = reinterpret_cast<CuteQQuickRowLayoutCall4>(taken[4]);
      call(this, item, static_cast<int>(align.toInt()), &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::setAlignment(item, align);
  }

  //  void QQuickGridLayoutBase::setStretchFactor(QQuickItem *item, int
  //      stretchFactor, Qt::Orientation orient)
  void setStretchFactor(
      QQuickItem *item,
      int stretchFactor,
      Qt::Orientation orient) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRowLayoutCall5 call = reinterpret_cast<CuteQQuickRowLayoutCall5>(taken[5]);
      call(this, item, stretchFactor, static_cast<int>(orient), &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::setStretchFactor(item, stretchFactor, orient);
  }

  //  void QQuickGridLayoutBase::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRowLayoutCall6 call = reinterpret_cast<CuteQQuickRowLayoutCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::itemDestroyed(item);
  }

  //  void QQuickGridLayoutBase::itemVisibilityChanged(QQuickItem *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRowLayoutCall7 call = reinterpret_cast<CuteQQuickRowLayoutCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::itemVisibilityChanged(item);
  }

  //  void QQuickGridLayoutBase::updateLayoutItems()
  void updateLayoutItems() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRowLayoutCall8 call = reinterpret_cast<CuteQQuickRowLayoutCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::updateLayoutItems();
  }

  //  QQuickItem *QQuickGridLayoutBase::itemAt(int index) const
  QQuickItem *itemAt(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRowLayoutCall9 call = reinterpret_cast<CuteQQuickRowLayoutCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickGridLayoutBase::itemAt(index);
  }

  //  int QQuickGridLayoutBase::itemCount() const
  int itemCount() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRowLayoutCall10 call = reinterpret_cast<CuteQQuickRowLayoutCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGridLayoutBase::itemCount();
  }

  //  void QQuickGridLayoutBase::rearrange(const QSizeF &size)
  void rearrange(const QSizeF &size) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRowLayoutCall11 call = reinterpret_cast<CuteQQuickRowLayoutCall11>(taken[11]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QQuickGridLayoutBase::rearrange(size);
  }

  //  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRowLayoutCall12 call = reinterpret_cast<CuteQQuickRowLayoutCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRowLayoutCall13 call = reinterpret_cast<CuteQQuickRowLayoutCall13>(taken[13]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLayout::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickLayout::itemSiblingOrderChanged(QQuickItem *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRowLayoutCall14 call = reinterpret_cast<CuteQQuickRowLayoutCall14>(taken[14]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemSiblingOrderChanged(item);
  }

  //  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRowLayoutCall15 call = reinterpret_cast<CuteQQuickRowLayoutCall15>(taken[15]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitWidthChanged(item);
  }

  //  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRowLayoutCall16 call = reinterpret_cast<CuteQQuickRowLayoutCall16>(taken[16]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitHeightChanged(item);
  }

  //  void QQuickLayout::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRowLayoutCall17 call = reinterpret_cast<CuteQQuickRowLayoutCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLayout::updatePolish();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRowLayoutCall18 call = reinterpret_cast<CuteQQuickRowLayoutCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRowLayoutCall19 call = reinterpret_cast<CuteQQuickRowLayoutCall19>(taken[19]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRowLayoutCall20 call = reinterpret_cast<CuteQQuickRowLayoutCall20>(taken[20]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRowLayoutCall21 call = reinterpret_cast<CuteQQuickRowLayoutCall21>(taken[21]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRowLayoutCall22 call = reinterpret_cast<CuteQQuickRowLayoutCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRowLayoutCall23 call = reinterpret_cast<CuteQQuickRowLayoutCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickRowLayoutCall24 call = reinterpret_cast<CuteQQuickRowLayoutCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickRowLayoutCall25 call = reinterpret_cast<CuteQQuickRowLayoutCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRowLayoutCall26 call = reinterpret_cast<CuteQQuickRowLayoutCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRowLayoutCall27 call = reinterpret_cast<CuteQQuickRowLayoutCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRowLayoutCall28 call = reinterpret_cast<CuteQQuickRowLayoutCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickRowLayoutCall29 call = reinterpret_cast<CuteQQuickRowLayoutCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickRowLayoutCall30 call = reinterpret_cast<CuteQQuickRowLayoutCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickRowLayoutCall31 call = reinterpret_cast<CuteQQuickRowLayoutCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickRowLayoutCall32 call = reinterpret_cast<CuteQQuickRowLayoutCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickRowLayoutCall33 call = reinterpret_cast<CuteQQuickRowLayoutCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickRowLayoutCall34 call = reinterpret_cast<CuteQQuickRowLayoutCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickRowLayoutCall35 call = reinterpret_cast<CuteQQuickRowLayoutCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickRowLayoutCall36 call = reinterpret_cast<CuteQQuickRowLayoutCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickRowLayoutCall37 call = reinterpret_cast<CuteQQuickRowLayoutCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickRowLayoutCall38 call = reinterpret_cast<CuteQQuickRowLayoutCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickRowLayoutCall39 call = reinterpret_cast<CuteQQuickRowLayoutCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickRowLayoutCall40 call = reinterpret_cast<CuteQQuickRowLayoutCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickRowLayoutCall41 call = reinterpret_cast<CuteQQuickRowLayoutCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickRowLayoutCall42 call = reinterpret_cast<CuteQQuickRowLayoutCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickRowLayoutCall43 call = reinterpret_cast<CuteQQuickRowLayoutCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickRowLayoutCall44 call = reinterpret_cast<CuteQQuickRowLayoutCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickRowLayoutCall45 call = reinterpret_cast<CuteQQuickRowLayoutCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickRowLayoutCall46 call = reinterpret_cast<CuteQQuickRowLayoutCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQQuickRowLayoutCall47 call = reinterpret_cast<CuteQQuickRowLayoutCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickRowLayoutCall48 call = reinterpret_cast<CuteQQuickRowLayoutCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteQQuickRowLayoutCall49 call = reinterpret_cast<CuteQQuickRowLayoutCall49>(taken[49]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickRowLayoutCall50 call = reinterpret_cast<CuteQQuickRowLayoutCall50>(taken[50]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickRowLayoutCall51 call = reinterpret_cast<CuteQQuickRowLayoutCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickRowLayoutCall52 call = reinterpret_cast<CuteQQuickRowLayoutCall52>(taken[52]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickRowLayoutCall53 call = reinterpret_cast<CuteQQuickRowLayoutCall53>(taken[53]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickRowLayoutCall54 call = reinterpret_cast<CuteQQuickRowLayoutCall54>(taken[54]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickRowLayoutCall55 call = reinterpret_cast<CuteQQuickRowLayoutCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickRowLayoutCall56 call = reinterpret_cast<CuteQQuickRowLayoutCall56>(taken[56]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickRowLayoutCall57 call = reinterpret_cast<CuteQQuickRowLayoutCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickRowLayoutCall58 call = reinterpret_cast<CuteQQuickRowLayoutCall58>(taken[58]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickRowLayoutCall59 call = reinterpret_cast<CuteQQuickRowLayoutCall59>(taken[59]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickRowLayoutCall60 call = reinterpret_cast<CuteQQuickRowLayoutCall60>(taken[60]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickRowLayoutCall61 call = reinterpret_cast<CuteQQuickRowLayoutCall61>(taken[61]);
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
    if (taken[62]) {
      int handled = 0;
      CuteQQuickRowLayoutCall62 call = reinterpret_cast<CuteQQuickRowLayoutCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickRowLayoutCall63 call = reinterpret_cast<CuteQQuickRowLayoutCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickRowLayoutCall64 call = reinterpret_cast<CuteQQuickRowLayoutCall64>(taken[64]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickRowLayoutCall65 call = reinterpret_cast<CuteQQuickRowLayoutCall65>(taken[65]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickRowLayoutCall66 call = reinterpret_cast<CuteQQuickRowLayoutCall66>(taken[66]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickRowLayoutCall67 call = reinterpret_cast<CuteQQuickRowLayoutCall67>(taken[67]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQuickRowLayoutCall68 call = reinterpret_cast<CuteQQuickRowLayoutCall68>(taken[68]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQuickRowLayoutCall69 call = reinterpret_cast<CuteQQuickRowLayoutCall69>(taken[69]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRowLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickRowLayout10metaObjectEv(
    const QQuickRowLayout *self) {
  return self->metaObject();
}

//  QString QQuickRowLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickRowLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRowLayout::tr(s, c, n));
}

//  QQuickRowLayout::QQuickRowLayout(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRowLayout *ritual_ZN15QQuickRowLayoutC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRowLayout(parent);
}

//  a Python function taken by a CuteQQuickRowLayout, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRowLayout(
    QQuickRowLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRowLayout *>(self)->take(key, call);
}
