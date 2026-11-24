//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickitemgroup_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickitemgroup_p.h>
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

//  Only a class built on QQuickItemGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemGroup : QQuickItemGroup {
  using QQuickItemGroup::itemChange;
  using QQuickItemGroup::geometryChange;
  using QQuickItemGroup::itemImplicitWidthChanged;
  using QQuickItemGroup::itemImplicitHeightChanged;
};

//  A QQuickItemGroup that Python can take functions over in. Every QQuickItemGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickItemGroupCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickItemGroupCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickItemGroupCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall3)(const void *, QQuickItem *, int *);
typedef const QRectF * (*CuteQQuickItemGroupCall4)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemGroupCall5)(const void *, int *);
typedef bool (*CuteQQuickItemGroupCall6)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickItemGroupCall7)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickItemGroupCall8)(const void *, int *);
typedef void * (*CuteQQuickItemGroupCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemGroupCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall11)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall12)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickItemGroupCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickItemGroupCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickItemGroupCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemGroupCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemGroupCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemGroupCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemGroupCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemGroupCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemGroupCall22)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemGroupCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemGroupCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickItemGroupCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemGroupCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemGroupCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemGroupCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemGroupCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemGroupCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemGroupCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickItemGroupCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickItemGroupCall34)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickItemGroupCall35)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall36)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall37)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickItemGroupCall38)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall39)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall40)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall41)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall42)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall43)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall44)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall45)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall46)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall47)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickItemGroupCall48)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall49)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickItemGroupCall50)(const void *, int *);
typedef bool (*CuteQQuickItemGroupCall51)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickItemGroupCall52)(const void *, int *);
typedef void (*CuteQQuickItemGroupCall53)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemGroupCall54)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemGroupCall55)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall56)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall57)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall58)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall59)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemGroupCall60)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItemGroup : public QQuickItemGroup {
public:
  using QQuickItemGroup::QQuickItemGroup;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[54] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[59] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[60] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickItemGroup::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemGroupCall0 call = reinterpret_cast<CuteQQuickItemGroupCall0>(taken[0]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickItemGroup::itemChange(change, data);
  }

  //  void QQuickItemGroup::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemGroupCall1 call = reinterpret_cast<CuteQQuickItemGroupCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItemGroup::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItemGroup::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemGroupCall2 call = reinterpret_cast<CuteQQuickItemGroupCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickItemGroup::itemImplicitWidthChanged(item);
  }

  //  void QQuickItemGroup::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemGroupCall3 call = reinterpret_cast<CuteQQuickItemGroupCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickItemGroup::itemImplicitHeightChanged(item);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemGroupCall4 call = reinterpret_cast<CuteQQuickItemGroupCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemGroupCall5 call = reinterpret_cast<CuteQQuickItemGroupCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemGroupCall6 call = reinterpret_cast<CuteQQuickItemGroupCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemGroupCall7 call = reinterpret_cast<CuteQQuickItemGroupCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemGroupCall8 call = reinterpret_cast<CuteQQuickItemGroupCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemGroupCall9 call = reinterpret_cast<CuteQQuickItemGroupCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemGroupCall10 call = reinterpret_cast<CuteQQuickItemGroupCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemGroupCall11 call = reinterpret_cast<CuteQQuickItemGroupCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemGroupCall12 call = reinterpret_cast<CuteQQuickItemGroupCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemGroupCall13 call = reinterpret_cast<CuteQQuickItemGroupCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemGroupCall14 call = reinterpret_cast<CuteQQuickItemGroupCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemGroupCall15 call = reinterpret_cast<CuteQQuickItemGroupCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemGroupCall16 call = reinterpret_cast<CuteQQuickItemGroupCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemGroupCall17 call = reinterpret_cast<CuteQQuickItemGroupCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemGroupCall18 call = reinterpret_cast<CuteQQuickItemGroupCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemGroupCall19 call = reinterpret_cast<CuteQQuickItemGroupCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemGroupCall20 call = reinterpret_cast<CuteQQuickItemGroupCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemGroupCall21 call = reinterpret_cast<CuteQQuickItemGroupCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickItemGroupCall22 call = reinterpret_cast<CuteQQuickItemGroupCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickItemGroupCall23 call = reinterpret_cast<CuteQQuickItemGroupCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickItemGroupCall24 call = reinterpret_cast<CuteQQuickItemGroupCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickItemGroupCall25 call = reinterpret_cast<CuteQQuickItemGroupCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemGroupCall26 call = reinterpret_cast<CuteQQuickItemGroupCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickItemGroupCall27 call = reinterpret_cast<CuteQQuickItemGroupCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickItemGroupCall28 call = reinterpret_cast<CuteQQuickItemGroupCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickItemGroupCall29 call = reinterpret_cast<CuteQQuickItemGroupCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickItemGroupCall30 call = reinterpret_cast<CuteQQuickItemGroupCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickItemGroupCall31 call = reinterpret_cast<CuteQQuickItemGroupCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickItemGroupCall32 call = reinterpret_cast<CuteQQuickItemGroupCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemGroupCall33 call = reinterpret_cast<CuteQQuickItemGroupCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemGroupCall34 call = reinterpret_cast<CuteQQuickItemGroupCall34>(taken[34]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickItemGroupCall35 call = reinterpret_cast<CuteQQuickItemGroupCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickItemGroupCall36 call = reinterpret_cast<CuteQQuickItemGroupCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickItemGroupCall37 call = reinterpret_cast<CuteQQuickItemGroupCall37>(taken[37]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickItemGroupCall38 call = reinterpret_cast<CuteQQuickItemGroupCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickItemGroupCall39 call = reinterpret_cast<CuteQQuickItemGroupCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickItemGroupCall40 call = reinterpret_cast<CuteQQuickItemGroupCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickItemGroupCall41 call = reinterpret_cast<CuteQQuickItemGroupCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickItemGroupCall42 call = reinterpret_cast<CuteQQuickItemGroupCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemDestroyed(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickItemGroupCall43 call = reinterpret_cast<CuteQQuickItemGroupCall43>(taken[43]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickItemGroupCall44 call = reinterpret_cast<CuteQQuickItemGroupCall44>(taken[44]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickItemGroupCall45 call = reinterpret_cast<CuteQQuickItemGroupCall45>(taken[45]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickItemGroupCall46 call = reinterpret_cast<CuteQQuickItemGroupCall46>(taken[46]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickItemGroupCall47 call = reinterpret_cast<CuteQQuickItemGroupCall47>(taken[47]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickItemGroupCall48 call = reinterpret_cast<CuteQQuickItemGroupCall48>(taken[48]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickItemGroupCall49 call = reinterpret_cast<CuteQQuickItemGroupCall49>(taken[49]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickItemGroupCall50 call = reinterpret_cast<CuteQQuickItemGroupCall50>(taken[50]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickItemGroupCall51 call = reinterpret_cast<CuteQQuickItemGroupCall51>(taken[51]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickItemGroupCall52 call = reinterpret_cast<CuteQQuickItemGroupCall52>(taken[52]);
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
    if (taken[53]) {
      int handled = 0;
      CuteQQuickItemGroupCall53 call = reinterpret_cast<CuteQQuickItemGroupCall53>(taken[53]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickItemGroupCall54 call = reinterpret_cast<CuteQQuickItemGroupCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickItemGroupCall55 call = reinterpret_cast<CuteQQuickItemGroupCall55>(taken[55]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickItemGroupCall56 call = reinterpret_cast<CuteQQuickItemGroupCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickItemGroupCall57 call = reinterpret_cast<CuteQQuickItemGroupCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickItemGroupCall58 call = reinterpret_cast<CuteQQuickItemGroupCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickItemGroupCall59 call = reinterpret_cast<CuteQQuickItemGroupCall59>(taken[59]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickItemGroupCall60 call = reinterpret_cast<CuteQQuickItemGroupCall60>(taken[60]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItemGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickItemGroup10metaObjectEv(
    const QQuickItemGroup *self) {
  return self->metaObject();
}

//  QString QQuickItemGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickItemGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemGroup::tr(s, c, n));
}

//  QQuickItemGroup::QQuickItemGroup(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickItemGroup *ritual_ZN15QQuickItemGroupC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickItemGroup(parent);
}

//  QQuickItemGroup::~QQuickItemGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroupD1Ev(QQuickItemGroup *self) {
  delete self;
}

//  void QQuickItemGroup::watch(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup5watchEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  self->watch(item);
}

//  void QQuickItemGroup::unwatch(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup7unwatchEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  self->unwatch(item);
}

//  QSizeF QQuickItemGroup::calculateImplicitSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QQuickItemGroup21calculateImplicitSizeEv(
    const QQuickItemGroup *self) {
  return new QSizeF(self->calculateImplicitSize());
}

//  void QQuickItemGroup::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup18updateImplicitSizeEv(
    QQuickItemGroup *self) {
  self->updateImplicitSize();
}

//  void QQuickItemGroup::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickItemGroup *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickItemGroup::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup14geometryChangeERK6QRectFS2_(
    QQuickItemGroup *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickItemGroup::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup24itemImplicitWidthChangedEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickItemGroup::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemGroup25itemImplicitHeightChangedEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  QQuickItemGroup as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickItemGroup_QQuickItemChangeListener(
    QQuickItemGroup *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickItemGroup, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemGroup(
    QQuickItemGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemGroup *>(self)->take(key, call);
}

//  void QQuickItemGroup::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemGroup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickItemGroup *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickItemGroup *>(self)->OwnQQuickItemGroup::itemChange(
      change,
      *data);
}

//  void QQuickItemGroup::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemGroup14geometryChangeERK6QRectFS2_(
    QQuickItemGroup *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickItemGroup *>(self)->OwnQQuickItemGroup::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickItemGroup::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemGroup24itemImplicitWidthChangedEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  static_cast<OwnQQuickItemGroup *>(self)->OwnQQuickItemGroup::itemImplicitWidthChanged(
      item);
}

//  void QQuickItemGroup::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemGroup25itemImplicitHeightChangedEP10QQuickItem(
    QQuickItemGroup *self,
    QQuickItem *item) {
  static_cast<OwnQQuickItemGroup *>(self)->OwnQQuickItemGroup::itemImplicitHeightChanged(
      item);
}
