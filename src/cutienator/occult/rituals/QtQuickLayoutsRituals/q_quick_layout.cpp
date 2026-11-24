//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayout_p.h>
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

//  Only a class built on QQuickLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLayout : QQuickLayout {
  using QQuickLayout::updatePolish;
};

//  A QQuickLayout that Python can take functions over in. Every QQuickLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLayoutCall0)(const void *, int *);
typedef const QSizeF * (*CuteQQuickLayoutCall1)(const void *, int, int *);
typedef void (*CuteQQuickLayoutCall2)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickLayoutCall3)(const void *, QQuickItem *, int, int, int *);
typedef void (*CuteQQuickLayoutCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall5)(const void *, int *);
typedef void * (*CuteQQuickLayoutCall6)(const void *, int, int *);
typedef int (*CuteQQuickLayoutCall7)(const void *, int *);
typedef void (*CuteQQuickLayoutCall8)(const void *, const QSizeF *, int *);
typedef void (*CuteQQuickLayoutCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickLayoutCall10)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickLayoutCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall12)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall14)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall15)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall16)(const void *, int *);
typedef const QRectF * (*CuteQQuickLayoutCall17)(const void *, int *);
typedef const QRectF * (*CuteQQuickLayoutCall18)(const void *, int *);
typedef bool (*CuteQQuickLayoutCall19)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickLayoutCall20)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickLayoutCall21)(const void *, int *);
typedef void * (*CuteQQuickLayoutCall22)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall24)(const void *, int *);
typedef void (*CuteQQuickLayoutCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickLayoutCall26)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickLayoutCall27)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickLayoutCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLayoutCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLayoutCall30)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutCall34)(const void *, int *);
typedef void (*CuteQQuickLayoutCall35)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLayoutCall36)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLayoutCall37)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickLayoutCall38)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLayoutCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLayoutCall40)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutCall41)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutCall42)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutCall43)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutCall44)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickLayoutCall45)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickLayoutCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickLayoutCall47)(const void *, int *);
typedef void (*CuteQQuickLayoutCall48)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickLayoutCall49)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall50)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall51)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall52)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall53)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall54)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall55)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickLayoutCall56)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall57)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickLayoutCall58)(const void *, int *);
typedef bool (*CuteQQuickLayoutCall59)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickLayoutCall60)(const void *, int *);
typedef void (*CuteQQuickLayoutCall61)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLayoutCall62)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutCall63)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall64)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall65)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall66)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall67)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutCall68)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLayout : public QQuickLayout {
public:
  using QQuickLayout::QQuickLayout;
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
    if (!std::strcmp(key, "_ZNK12QQuickLayout6itemAtEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QQuickLayout9itemCountEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQuickLayout9rearrangeERK6QSizeF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
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

  //  void QQuickLayout::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLayoutCall0 call = reinterpret_cast<CuteQQuickLayoutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLayout::componentComplete();
  }

  //  QSizeF QQuickLayout::sizeHint(Qt::SizeHint whichSizeHint) const
  QSizeF sizeHint(Qt::SizeHint whichSizeHint) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLayoutCall1 call = reinterpret_cast<CuteQQuickLayoutCall1>(taken[1]);
      const QSizeF * given = call(this, static_cast<int>(whichSizeHint), &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QQuickLayout::setAlignment(QQuickItem *item, Qt::Alignment
  //      align)
  void setAlignment(QQuickItem *item, Qt::Alignment align) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLayoutCall2 call = reinterpret_cast<CuteQQuickLayoutCall2>(taken[2]);
      call(this, item, static_cast<int>(align.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QQuickLayout::setStretchFactor(QQuickItem *item, int
  //      stretchFactor, Qt::Orientation orient)
  void setStretchFactor(
      QQuickItem *item,
      int stretchFactor,
      Qt::Orientation orient) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLayoutCall3 call = reinterpret_cast<CuteQQuickLayoutCall3>(taken[3]);
      call(this, item, stretchFactor, static_cast<int>(orient), &handled);
      if (handled) return;
    }
  }

  //  void QQuickLayout::invalidate(QQuickItem *childItem)
  void invalidate(QQuickItem *childItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLayoutCall4 call = reinterpret_cast<CuteQQuickLayoutCall4>(taken[4]);
      call(this, childItem, &handled);
      if (handled) return;
    }
    QQuickLayout::invalidate(childItem);
  }

  //  void QQuickLayout::updateLayoutItems()
  void updateLayoutItems() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLayoutCall5 call = reinterpret_cast<CuteQQuickLayoutCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QQuickItem *QQuickLayout::itemAt(int index) const
  QQuickItem *itemAt(int index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLayoutCall6 call = reinterpret_cast<CuteQQuickLayoutCall6>(taken[6]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return {};
  }

  //  int QQuickLayout::itemCount() const
  int itemCount() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLayoutCall7 call = reinterpret_cast<CuteQQuickLayoutCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQuickLayout::rearrange(const QSizeF &a0)
  void rearrange(const QSizeF &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLayoutCall8 call = reinterpret_cast<CuteQQuickLayoutCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickLayout::rearrange(a0);
  }

  //  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLayoutCall9 call = reinterpret_cast<CuteQQuickLayoutCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLayoutCall10 call = reinterpret_cast<CuteQQuickLayoutCall10>(taken[10]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLayout::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickLayout::itemSiblingOrderChanged(QQuickItem *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLayoutCall11 call = reinterpret_cast<CuteQQuickLayoutCall11>(taken[11]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemSiblingOrderChanged(item);
  }

  //  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLayoutCall12 call = reinterpret_cast<CuteQQuickLayoutCall12>(taken[12]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitWidthChanged(item);
  }

  //  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLayoutCall13 call = reinterpret_cast<CuteQQuickLayoutCall13>(taken[13]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemImplicitHeightChanged(item);
  }

  //  void QQuickLayout::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLayoutCall14 call = reinterpret_cast<CuteQQuickLayoutCall14>(taken[14]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemDestroyed(item);
  }

  //  void QQuickLayout::itemVisibilityChanged(QQuickItem *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLayoutCall15 call = reinterpret_cast<CuteQQuickLayoutCall15>(taken[15]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLayout::itemVisibilityChanged(item);
  }

  //  void QQuickLayout::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLayoutCall16 call = reinterpret_cast<CuteQQuickLayoutCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLayout::updatePolish();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLayoutCall17 call = reinterpret_cast<CuteQQuickLayoutCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLayoutCall18 call = reinterpret_cast<CuteQQuickLayoutCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLayoutCall19 call = reinterpret_cast<CuteQQuickLayoutCall19>(taken[19]);
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
      CuteQQuickLayoutCall20 call = reinterpret_cast<CuteQQuickLayoutCall20>(taken[20]);
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
      CuteQQuickLayoutCall21 call = reinterpret_cast<CuteQQuickLayoutCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickLayoutCall22 call = reinterpret_cast<CuteQQuickLayoutCall22>(taken[22]);
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
      CuteQQuickLayoutCall23 call = reinterpret_cast<CuteQQuickLayoutCall23>(taken[23]);
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
      CuteQQuickLayoutCall24 call = reinterpret_cast<CuteQQuickLayoutCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickLayoutCall25 call = reinterpret_cast<CuteQQuickLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickLayoutCall26 call = reinterpret_cast<CuteQQuickLayoutCall26>(taken[26]);
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
      CuteQQuickLayoutCall27 call = reinterpret_cast<CuteQQuickLayoutCall27>(taken[27]);
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
      CuteQQuickLayoutCall28 call = reinterpret_cast<CuteQQuickLayoutCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickLayoutCall29 call = reinterpret_cast<CuteQQuickLayoutCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickLayoutCall30 call = reinterpret_cast<CuteQQuickLayoutCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickLayoutCall31 call = reinterpret_cast<CuteQQuickLayoutCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickLayoutCall32 call = reinterpret_cast<CuteQQuickLayoutCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickLayoutCall33 call = reinterpret_cast<CuteQQuickLayoutCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickLayoutCall34 call = reinterpret_cast<CuteQQuickLayoutCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickLayoutCall35 call = reinterpret_cast<CuteQQuickLayoutCall35>(taken[35]);
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
      CuteQQuickLayoutCall36 call = reinterpret_cast<CuteQQuickLayoutCall36>(taken[36]);
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
      CuteQQuickLayoutCall37 call = reinterpret_cast<CuteQQuickLayoutCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickLayoutCall38 call = reinterpret_cast<CuteQQuickLayoutCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickLayoutCall39 call = reinterpret_cast<CuteQQuickLayoutCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickLayoutCall40 call = reinterpret_cast<CuteQQuickLayoutCall40>(taken[40]);
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
      CuteQQuickLayoutCall41 call = reinterpret_cast<CuteQQuickLayoutCall41>(taken[41]);
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
      CuteQQuickLayoutCall42 call = reinterpret_cast<CuteQQuickLayoutCall42>(taken[42]);
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
      CuteQQuickLayoutCall43 call = reinterpret_cast<CuteQQuickLayoutCall43>(taken[43]);
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
      CuteQQuickLayoutCall44 call = reinterpret_cast<CuteQQuickLayoutCall44>(taken[44]);
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
      CuteQQuickLayoutCall45 call = reinterpret_cast<CuteQQuickLayoutCall45>(taken[45]);
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
      CuteQQuickLayoutCall46 call = reinterpret_cast<CuteQQuickLayoutCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickLayoutCall47 call = reinterpret_cast<CuteQQuickLayoutCall47>(taken[47]);
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
      CuteQQuickLayoutCall48 call = reinterpret_cast<CuteQQuickLayoutCall48>(taken[48]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickLayoutCall49 call = reinterpret_cast<CuteQQuickLayoutCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickLayoutCall50 call = reinterpret_cast<CuteQQuickLayoutCall50>(taken[50]);
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
      CuteQQuickLayoutCall51 call = reinterpret_cast<CuteQQuickLayoutCall51>(taken[51]);
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
      CuteQQuickLayoutCall52 call = reinterpret_cast<CuteQQuickLayoutCall52>(taken[52]);
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
      CuteQQuickLayoutCall53 call = reinterpret_cast<CuteQQuickLayoutCall53>(taken[53]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickLayoutCall54 call = reinterpret_cast<CuteQQuickLayoutCall54>(taken[54]);
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
      CuteQQuickLayoutCall55 call = reinterpret_cast<CuteQQuickLayoutCall55>(taken[55]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickLayoutCall56 call = reinterpret_cast<CuteQQuickLayoutCall56>(taken[56]);
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
      CuteQQuickLayoutCall57 call = reinterpret_cast<CuteQQuickLayoutCall57>(taken[57]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickLayoutCall58 call = reinterpret_cast<CuteQQuickLayoutCall58>(taken[58]);
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
      CuteQQuickLayoutCall59 call = reinterpret_cast<CuteQQuickLayoutCall59>(taken[59]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickLayoutCall60 call = reinterpret_cast<CuteQQuickLayoutCall60>(taken[60]);
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
      CuteQQuickLayoutCall61 call = reinterpret_cast<CuteQQuickLayoutCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickLayoutCall62 call = reinterpret_cast<CuteQQuickLayoutCall62>(taken[62]);
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
      CuteQQuickLayoutCall63 call = reinterpret_cast<CuteQQuickLayoutCall63>(taken[63]);
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
      CuteQQuickLayoutCall64 call = reinterpret_cast<CuteQQuickLayoutCall64>(taken[64]);
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
      CuteQQuickLayoutCall65 call = reinterpret_cast<CuteQQuickLayoutCall65>(taken[65]);
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
      CuteQQuickLayoutCall66 call = reinterpret_cast<CuteQQuickLayoutCall66>(taken[66]);
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
      CuteQQuickLayoutCall67 call = reinterpret_cast<CuteQQuickLayoutCall67>(taken[67]);
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
      CuteQQuickLayoutCall68 call = reinterpret_cast<CuteQQuickLayoutCall68>(taken[68]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickLayout10metaObjectEv(
    const QQuickLayout *self) {
  return self->metaObject();
}

//  QString QQuickLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLayout::tr(s, c, n));
}

//  void QQuickLayout::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout24qt_qmlMarker_uncreatableEv(
    QQuickLayout *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickLayout::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout21qt_qmlMarker_attachedEv(QQuickLayout *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickLayout::~QQuickLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayoutD1Ev(QQuickLayout *self) {
  delete self;
}

//  QQuickLayoutAttached *QQuickLayout::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickLayoutAttached *ritual_ZN12QQuickLayout21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickLayout::qmlAttachedProperties(object);
}

//  void QQuickLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout17componentCompleteEv(QQuickLayout *self) {
  self->componentComplete();
}

//  QSizeF QQuickLayout::sizeHint(Qt::SizeHint whichSizeHint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK12QQuickLayout8sizeHintEN2Qt8SizeHintE(
    const QQuickLayout *self,
    Qt::SizeHint whichSizeHint) {
  return new QSizeF(self->sizeHint(whichSizeHint));
}

//  void QQuickLayout::setAlignment(QQuickItem *item, Qt::Alignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickLayout *self,
    QQuickItem *item,
    int align) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(align));
}

//  void QQuickLayout::setStretchFactor(QQuickItem *item, int stretchFactor,
//      Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickLayout *self,
    QQuickItem *item,
    int stretchFactor,
    Qt::Orientation orient) {
  self->setStretchFactor(item, stretchFactor, orient);
}

//  void QQuickLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout10invalidateEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *childItem) {
  self->invalidate(childItem);
}

//  void QQuickLayout::updateLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout17updateLayoutItemsEv(QQuickLayout *self) {
  self->updateLayoutItems();
}

//  void
//      QQuickLayout::ensureLayoutItemsUpdated(EnsureLayoutItemsUpdatedOption
//      s options) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QQuickLayout24ensureLayoutItemsUpdatedE6QFlagsINS_30EnsureLayoutItemsUpdatedOptionEE(
    const QQuickLayout *self,
    int options) {
  self->ensureLayoutItemsUpdated(
      QFlags<QQuickLayout::EnsureLayoutItemsUpdatedOption>::fromInt(options));
}

//  QQuickItem *QQuickLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickLayout6itemAtEi(
    const QQuickLayout *self,
    int index) {
  return self->itemAt(index);
}

//  int QQuickLayout::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickLayout9itemCountEv(const QQuickLayout *self) {
  return self->itemCount();
}

//  void QQuickLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout9rearrangeERK6QSizeF(
    QQuickLayout *self,
    const QSizeF *a0) {
  self->rearrange(*a0);
}

//  QLayoutPolicy::Policy QQuickLayout::effectiveSizePolicy_helper(QQuickItem
//      *item, Qt::Orientation orientation, QQuickLayoutAttached *info)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickLayout26effectiveSizePolicy_helperEP10QQuickItemN2Qt11OrientationEP20QQuickLayoutAttached(
    QQuickItem *item,
    Qt::Orientation orientation,
    QQuickLayoutAttached *info) {
  return static_cast<int>(
      QQuickLayout::effectiveSizePolicy_helper(
          item,
          orientation,
          info).toInt());
}

//  bool QQuickLayout::shouldIgnoreItem(QQuickItem *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLayout16shouldIgnoreItemEP10QQuickItem(
    const QQuickLayout *self,
    QQuickItem *child) {
  return self->shouldIgnoreItem(child);
}

//  void QQuickLayout::checkAnchors(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QQuickLayout12checkAnchorsEP10QQuickItem(
    const QQuickLayout *self,
    QQuickItem *item) {
  self->checkAnchors(item);
}

//  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLayout *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickLayout::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout14geometryChangeERK6QRectFS2_(
    QQuickLayout *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  bool QQuickLayout::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLayout7isReadyEv(const QQuickLayout *self) {
  return self->isReady();
}

//  void QQuickLayout::deactivateRecur()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout15deactivateRecurEv(QQuickLayout *self) {
  self->deactivateRecur();
}

//  bool QQuickLayout::invalidated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLayout11invalidatedEv(const QQuickLayout *self) {
  return self->invalidated();
}

//  bool QQuickLayout::invalidatedArrangement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLayout22invalidatedArrangementEv(
    const QQuickLayout *self) {
  return self->invalidatedArrangement();
}

//  bool QQuickLayout::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLayout10isMirroredEv(const QQuickLayout *self) {
  return self->isMirrored();
}

//  void QQuickLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->itemSiblingOrderChanged(item);
}

//  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickLayout::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout13itemDestroyedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickLayout::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout21itemVisibilityChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->itemVisibilityChanged(item);
}

//  void QQuickLayout::maybeSubscribeToBaseLineOffsetChanges(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout37maybeSubscribeToBaseLineOffsetChangesEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->maybeSubscribeToBaseLineOffsetChanges(item);
}

//  void QQuickLayout::_q_dumpLayoutTree() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QQuickLayout17_q_dumpLayoutTreeEv(
    const QQuickLayout *self) {
  self->_q_dumpLayoutTree();
}

//  void QQuickLayout::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout12updatePolishEv(QQuickLayout *self) {
  self->updatePolish();
}

//  void QQuickLayout::invalidateSenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLayout20invalidateSenderItemEv(QQuickLayout *self) {
  self->invalidateSenderItem();
}

//  QQuickLayoutPrivate *QQuickLayout::d_func()
extern "C" Q_DECL_EXPORT
QQuickLayoutPrivate *ritual_ZN12QQuickLayout6d_funcEv(QQuickLayout *self) {
  return self->d_func();
}

//  const QQuickLayoutPrivate *QQuickLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickLayoutPrivate *ritual_ZNK12QQuickLayout6d_funcEv(
    const QQuickLayout *self) {
  return self->d_func();
}

//  QQuickLayout as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickLayout_QQuickItemChangeListener(
    QQuickLayout *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLayout(
    QQuickLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLayout *>(self)->take(key, call);
}

//  void QQuickLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout17componentCompleteEv(QQuickLayout *self) {
  self->QQuickLayout::componentComplete();
}

//  void QQuickLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout10invalidateEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *childItem) {
  self->QQuickLayout::invalidate(childItem);
}

//  void QQuickLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout9rearrangeERK6QSizeF(
    QQuickLayout *self,
    const QSizeF *a0) {
  self->QQuickLayout::rearrange(*a0);
}

//  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLayout *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->QQuickLayout::itemChange(change, *value);
}

//  void QQuickLayout::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout14geometryChangeERK6QRectFS2_(
    QQuickLayout *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->QQuickLayout::geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->QQuickLayout::itemSiblingOrderChanged(item);
}

//  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->QQuickLayout::itemImplicitWidthChanged(item);
}

//  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->QQuickLayout::itemImplicitHeightChanged(item);
}

//  void QQuickLayout::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout13itemDestroyedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->QQuickLayout::itemDestroyed(item);
}

//  void QQuickLayout::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout21itemVisibilityChangedEP10QQuickItem(
    QQuickLayout *self,
    QQuickItem *item) {
  self->QQuickLayout::itemVisibilityChanged(item);
}

//  void QQuickLayout::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLayout12updatePolishEv(QQuickLayout *self) {
  static_cast<OwnQQuickLayout *>(self)->OwnQQuickLayout::updatePolish();
}
