//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickEffects/qtquickeffectsexports.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#include <QtQuickEffects/QtQuickEffects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickMultiEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMultiEffect : QQuickMultiEffect {
  using QQuickMultiEffect::componentComplete;
  using QQuickMultiEffect::geometryChange;
  using QQuickMultiEffect::itemChange;
};

//  A QQuickMultiEffect that Python can take functions over in. Every QQuickMultiEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickMultiEffectCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickMultiEffectCall1)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickMultiEffectCall2)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteQQuickMultiEffectCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickMultiEffectCall4)(const void *, int *);
typedef bool (*CuteQQuickMultiEffectCall5)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickMultiEffectCall6)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickMultiEffectCall7)(const void *, int *);
typedef void * (*CuteQQuickMultiEffectCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiEffectCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall10)(const void *, int *);
typedef void (*CuteQQuickMultiEffectCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickMultiEffectCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickMultiEffectCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall20)(const void *, int *);
typedef void (*CuteQQuickMultiEffectCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMultiEffectCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMultiEffectCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMultiEffectCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiEffectCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiEffectCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiEffectCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiEffectCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickMultiEffectCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickMultiEffectCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickMultiEffectCall33)(const void *, int *);
typedef void (*CuteQQuickMultiEffectCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiEffectCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiEffectCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMultiEffect : public QQuickMultiEffect {
public:
  using QQuickMultiEffect::QQuickMultiEffect;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickMultiEffect::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMultiEffectCall0 call = reinterpret_cast<CuteQQuickMultiEffectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMultiEffect::componentComplete();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickMultiEffect::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMultiEffectCall1 call = reinterpret_cast<CuteQQuickMultiEffectCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickMultiEffect::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickMultiEffect::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMultiEffectCall2 call = reinterpret_cast<CuteQQuickMultiEffectCall2>(taken[2]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickMultiEffect::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMultiEffectCall3 call = reinterpret_cast<CuteQQuickMultiEffectCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMultiEffectCall4 call = reinterpret_cast<CuteQQuickMultiEffectCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMultiEffectCall5 call = reinterpret_cast<CuteQQuickMultiEffectCall5>(taken[5]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMultiEffectCall6 call = reinterpret_cast<CuteQQuickMultiEffectCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMultiEffectCall7 call = reinterpret_cast<CuteQQuickMultiEffectCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMultiEffectCall8 call = reinterpret_cast<CuteQQuickMultiEffectCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMultiEffectCall9 call = reinterpret_cast<CuteQQuickMultiEffectCall9>(taken[9]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMultiEffectCall10 call = reinterpret_cast<CuteQQuickMultiEffectCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMultiEffectCall11 call = reinterpret_cast<CuteQQuickMultiEffectCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMultiEffectCall12 call = reinterpret_cast<CuteQQuickMultiEffectCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMultiEffectCall13 call = reinterpret_cast<CuteQQuickMultiEffectCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMultiEffectCall14 call = reinterpret_cast<CuteQQuickMultiEffectCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMultiEffectCall15 call = reinterpret_cast<CuteQQuickMultiEffectCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMultiEffectCall16 call = reinterpret_cast<CuteQQuickMultiEffectCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMultiEffectCall17 call = reinterpret_cast<CuteQQuickMultiEffectCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMultiEffectCall18 call = reinterpret_cast<CuteQQuickMultiEffectCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMultiEffectCall19 call = reinterpret_cast<CuteQQuickMultiEffectCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMultiEffectCall20 call = reinterpret_cast<CuteQQuickMultiEffectCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMultiEffectCall21 call = reinterpret_cast<CuteQQuickMultiEffectCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMultiEffectCall22 call = reinterpret_cast<CuteQQuickMultiEffectCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMultiEffectCall23 call = reinterpret_cast<CuteQQuickMultiEffectCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMultiEffectCall24 call = reinterpret_cast<CuteQQuickMultiEffectCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMultiEffectCall25 call = reinterpret_cast<CuteQQuickMultiEffectCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMultiEffectCall26 call = reinterpret_cast<CuteQQuickMultiEffectCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMultiEffectCall27 call = reinterpret_cast<CuteQQuickMultiEffectCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMultiEffectCall28 call = reinterpret_cast<CuteQQuickMultiEffectCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMultiEffectCall29 call = reinterpret_cast<CuteQQuickMultiEffectCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickMultiEffectCall30 call = reinterpret_cast<CuteQQuickMultiEffectCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickMultiEffectCall31 call = reinterpret_cast<CuteQQuickMultiEffectCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQQuickMultiEffectCall32 call = reinterpret_cast<CuteQQuickMultiEffectCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMultiEffectCall33 call = reinterpret_cast<CuteQQuickMultiEffectCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMultiEffectCall34 call = reinterpret_cast<CuteQQuickMultiEffectCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickMultiEffectCall35 call = reinterpret_cast<CuteQQuickMultiEffectCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickMultiEffectCall36 call = reinterpret_cast<CuteQQuickMultiEffectCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickMultiEffectCall37 call = reinterpret_cast<CuteQQuickMultiEffectCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickMultiEffectCall38 call = reinterpret_cast<CuteQQuickMultiEffectCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickMultiEffectCall39 call = reinterpret_cast<CuteQQuickMultiEffectCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickMultiEffectCall40 call = reinterpret_cast<CuteQQuickMultiEffectCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMultiEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickMultiEffect10metaObjectEv(
    const QQuickMultiEffect *self) {
  return self->metaObject();
}

//  void *QQuickMultiEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickMultiEffect11qt_metacastEPKc(
    QQuickMultiEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMultiEffect::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickMultiEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMultiEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMultiEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickMultiEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMultiEffect::tr(s, c, n));
}

//  QQuickMultiEffect::QQuickMultiEffect(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMultiEffect *ritual_ZN17QQuickMultiEffectC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickMultiEffect(parent);
}

//  QQuickMultiEffect::~QQuickMultiEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffectD1Ev(QQuickMultiEffect *self) {
  delete self;
}

//  QQuickItem *QQuickMultiEffect::source() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickMultiEffect6sourceEv(
    const QQuickMultiEffect *self) {
  return self->source();
}

//  void QQuickMultiEffect::setSource(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect9setSourceEP10QQuickItem(
    QQuickMultiEffect *self,
    QQuickItem *item) {
  self->setSource(item);
}

//  bool QQuickMultiEffect::autoPaddingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect18autoPaddingEnabledEv(
    const QQuickMultiEffect *self) {
  return self->autoPaddingEnabled();
}

//  void QQuickMultiEffect::setAutoPaddingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect21setAutoPaddingEnabledEb(
    QQuickMultiEffect *self,
    bool enabled) {
  self->setAutoPaddingEnabled(enabled);
}

//  QRectF QQuickMultiEffect::paddingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickMultiEffect11paddingRectEv(
    const QQuickMultiEffect *self) {
  return new QRectF(self->paddingRect());
}

//  void QQuickMultiEffect::setPaddingRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14setPaddingRectERK6QRectF(
    QQuickMultiEffect *self,
    const QRectF *rect) {
  self->setPaddingRect(*rect);
}

//  qreal QQuickMultiEffect::brightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect10brightnessEv(
    const QQuickMultiEffect *self) {
  return self->brightness();
}

//  void QQuickMultiEffect::setBrightness(qreal brightness)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13setBrightnessEd(
    QQuickMultiEffect *self,
    qreal brightness) {
  self->setBrightness(brightness);
}

//  qreal QQuickMultiEffect::contrast() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect8contrastEv(
    const QQuickMultiEffect *self) {
  return self->contrast();
}

//  void QQuickMultiEffect::setContrast(qreal contrast)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect11setContrastEd(
    QQuickMultiEffect *self,
    qreal contrast) {
  self->setContrast(contrast);
}

//  qreal QQuickMultiEffect::saturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect10saturationEv(
    const QQuickMultiEffect *self) {
  return self->saturation();
}

//  void QQuickMultiEffect::setSaturation(qreal saturation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13setSaturationEd(
    QQuickMultiEffect *self,
    qreal saturation) {
  self->setSaturation(saturation);
}

//  qreal QQuickMultiEffect::colorization() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect12colorizationEv(
    const QQuickMultiEffect *self) {
  return self->colorization();
}

//  void QQuickMultiEffect::setColorization(qreal colorization)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect15setColorizationEd(
    QQuickMultiEffect *self,
    qreal colorization) {
  self->setColorization(colorization);
}

//  QColor QQuickMultiEffect::colorizationColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickMultiEffect17colorizationColorEv(
    const QQuickMultiEffect *self) {
  return new QColor(self->colorizationColor());
}

//  void QQuickMultiEffect::setColorizationColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect20setColorizationColorERK6QColor(
    QQuickMultiEffect *self,
    const QColor *color) {
  self->setColorizationColor(*color);
}

//  bool QQuickMultiEffect::blurEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect11blurEnabledEv(
    const QQuickMultiEffect *self) {
  return self->blurEnabled();
}

//  void QQuickMultiEffect::setBlurEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14setBlurEnabledEb(
    QQuickMultiEffect *self,
    bool enabled) {
  self->setBlurEnabled(enabled);
}

//  qreal QQuickMultiEffect::blur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect4blurEv(const QQuickMultiEffect *self) {
  return self->blur();
}

//  void QQuickMultiEffect::setBlur(qreal blur)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect7setBlurEd(
    QQuickMultiEffect *self,
    qreal blur) {
  self->setBlur(blur);
}

//  int QQuickMultiEffect::blurMax() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickMultiEffect7blurMaxEv(const QQuickMultiEffect *self) {
  return self->blurMax();
}

//  void QQuickMultiEffect::setBlurMax(int blurMax)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect10setBlurMaxEi(
    QQuickMultiEffect *self,
    int blurMax) {
  self->setBlurMax(blurMax);
}

//  qreal QQuickMultiEffect::blurMultiplier() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect14blurMultiplierEv(
    const QQuickMultiEffect *self) {
  return self->blurMultiplier();
}

//  void QQuickMultiEffect::setBlurMultiplier(qreal blurMultiplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17setBlurMultiplierEd(
    QQuickMultiEffect *self,
    qreal blurMultiplier) {
  self->setBlurMultiplier(blurMultiplier);
}

//  bool QQuickMultiEffect::shadowEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect13shadowEnabledEv(
    const QQuickMultiEffect *self) {
  return self->shadowEnabled();
}

//  void QQuickMultiEffect::setShadowEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect16setShadowEnabledEb(
    QQuickMultiEffect *self,
    bool enabled) {
  self->setShadowEnabled(enabled);
}

//  qreal QQuickMultiEffect::shadowOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect13shadowOpacityEv(
    const QQuickMultiEffect *self) {
  return self->shadowOpacity();
}

//  void QQuickMultiEffect::setShadowOpacity(qreal shadowOpacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect16setShadowOpacityEd(
    QQuickMultiEffect *self,
    qreal shadowOpacity) {
  self->setShadowOpacity(shadowOpacity);
}

//  qreal QQuickMultiEffect::shadowBlur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect10shadowBlurEv(
    const QQuickMultiEffect *self) {
  return self->shadowBlur();
}

//  void QQuickMultiEffect::setShadowBlur(qreal shadowBlur)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13setShadowBlurEd(
    QQuickMultiEffect *self,
    qreal shadowBlur) {
  self->setShadowBlur(shadowBlur);
}

//  qreal QQuickMultiEffect::shadowHorizontalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect22shadowHorizontalOffsetEv(
    const QQuickMultiEffect *self) {
  return self->shadowHorizontalOffset();
}

//  void QQuickMultiEffect::setShadowHorizontalOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect25setShadowHorizontalOffsetEd(
    QQuickMultiEffect *self,
    qreal offset) {
  self->setShadowHorizontalOffset(offset);
}

//  qreal QQuickMultiEffect::shadowVerticalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect20shadowVerticalOffsetEv(
    const QQuickMultiEffect *self) {
  return self->shadowVerticalOffset();
}

//  void QQuickMultiEffect::setShadowVerticalOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect23setShadowVerticalOffsetEd(
    QQuickMultiEffect *self,
    qreal offset) {
  self->setShadowVerticalOffset(offset);
}

//  QColor QQuickMultiEffect::shadowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickMultiEffect11shadowColorEv(
    const QQuickMultiEffect *self) {
  return new QColor(self->shadowColor());
}

//  void QQuickMultiEffect::setShadowColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14setShadowColorERK6QColor(
    QQuickMultiEffect *self,
    const QColor *color) {
  self->setShadowColor(*color);
}

//  qreal QQuickMultiEffect::shadowScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect11shadowScaleEv(
    const QQuickMultiEffect *self) {
  return self->shadowScale();
}

//  void QQuickMultiEffect::setShadowScale(qreal shadowScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14setShadowScaleEd(
    QQuickMultiEffect *self,
    qreal shadowScale) {
  self->setShadowScale(shadowScale);
}

//  bool QQuickMultiEffect::maskEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect11maskEnabledEv(
    const QQuickMultiEffect *self) {
  return self->maskEnabled();
}

//  void QQuickMultiEffect::setMaskEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14setMaskEnabledEb(
    QQuickMultiEffect *self,
    bool enabled) {
  self->setMaskEnabled(enabled);
}

//  QQuickItem *QQuickMultiEffect::maskSource() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickMultiEffect10maskSourceEv(
    const QQuickMultiEffect *self) {
  return self->maskSource();
}

//  void QQuickMultiEffect::setMaskSource(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13setMaskSourceEP10QQuickItem(
    QQuickMultiEffect *self,
    QQuickItem *item) {
  self->setMaskSource(item);
}

//  qreal QQuickMultiEffect::maskThresholdMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect16maskThresholdMinEv(
    const QQuickMultiEffect *self) {
  return self->maskThresholdMin();
}

//  void QQuickMultiEffect::setMaskThresholdMin(qreal threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect19setMaskThresholdMinEd(
    QQuickMultiEffect *self,
    qreal threshold) {
  self->setMaskThresholdMin(threshold);
}

//  qreal QQuickMultiEffect::maskSpreadAtMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect15maskSpreadAtMinEv(
    const QQuickMultiEffect *self) {
  return self->maskSpreadAtMin();
}

//  void QQuickMultiEffect::setMaskSpreadAtMin(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18setMaskSpreadAtMinEd(
    QQuickMultiEffect *self,
    qreal spread) {
  self->setMaskSpreadAtMin(spread);
}

//  qreal QQuickMultiEffect::maskThresholdMax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect16maskThresholdMaxEv(
    const QQuickMultiEffect *self) {
  return self->maskThresholdMax();
}

//  void QQuickMultiEffect::setMaskThresholdMax(qreal threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect19setMaskThresholdMaxEd(
    QQuickMultiEffect *self,
    qreal threshold) {
  self->setMaskThresholdMax(threshold);
}

//  qreal QQuickMultiEffect::maskSpreadAtMax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickMultiEffect15maskSpreadAtMaxEv(
    const QQuickMultiEffect *self) {
  return self->maskSpreadAtMax();
}

//  void QQuickMultiEffect::setMaskSpreadAtMax(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18setMaskSpreadAtMaxEd(
    QQuickMultiEffect *self,
    qreal spread) {
  self->setMaskSpreadAtMax(spread);
}

//  bool QQuickMultiEffect::maskInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect12maskInvertedEv(
    const QQuickMultiEffect *self) {
  return self->maskInverted();
}

//  void QQuickMultiEffect::setMaskInverted(bool inverted)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect15setMaskInvertedEb(
    QQuickMultiEffect *self,
    bool inverted) {
  self->setMaskInverted(inverted);
}

//  QRectF QQuickMultiEffect::itemRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickMultiEffect8itemRectEv(
    const QQuickMultiEffect *self) {
  return new QRectF(self->itemRect());
}

//  QString QQuickMultiEffect::fragmentShader() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickMultiEffect14fragmentShaderEv(
    const QQuickMultiEffect *self) {
  return new QString(self->fragmentShader());
}

//  QString QQuickMultiEffect::vertexShader() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickMultiEffect12vertexShaderEv(
    const QQuickMultiEffect *self) {
  return new QString(self->vertexShader());
}

//  bool QQuickMultiEffect::hasProxySource() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMultiEffect14hasProxySourceEv(
    const QQuickMultiEffect *self) {
  return self->hasProxySource();
}

//  void QQuickMultiEffect::shaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13shaderChangedEv(QQuickMultiEffect *self) {
  self->shaderChanged();
}

//  void QQuickMultiEffect::itemSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect15itemSizeChangedEv(
    QQuickMultiEffect *self) {
  self->itemSizeChanged();
}

//  void QQuickMultiEffect::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect13sourceChangedEv(QQuickMultiEffect *self) {
  self->sourceChanged();
}

//  void QQuickMultiEffect::autoPaddingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect25autoPaddingEnabledChangedEv(
    QQuickMultiEffect *self) {
  self->autoPaddingEnabledChanged();
}

//  void QQuickMultiEffect::paddingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18paddingRectChangedEv(
    QQuickMultiEffect *self) {
  self->paddingRectChanged();
}

//  void QQuickMultiEffect::brightnessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17brightnessChangedEv(
    QQuickMultiEffect *self) {
  self->brightnessChanged();
}

//  void QQuickMultiEffect::contrastChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect15contrastChangedEv(
    QQuickMultiEffect *self) {
  self->contrastChanged();
}

//  void QQuickMultiEffect::saturationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17saturationChangedEv(
    QQuickMultiEffect *self) {
  self->saturationChanged();
}

//  void QQuickMultiEffect::colorizationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect19colorizationChangedEv(
    QQuickMultiEffect *self) {
  self->colorizationChanged();
}

//  void QQuickMultiEffect::colorizationColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect24colorizationColorChangedEv(
    QQuickMultiEffect *self) {
  self->colorizationColorChanged();
}

//  void QQuickMultiEffect::blurEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18blurEnabledChangedEv(
    QQuickMultiEffect *self) {
  self->blurEnabledChanged();
}

//  void QQuickMultiEffect::blurChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect11blurChangedEv(QQuickMultiEffect *self) {
  self->blurChanged();
}

//  void QQuickMultiEffect::blurMaxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14blurMaxChangedEv(
    QQuickMultiEffect *self) {
  self->blurMaxChanged();
}

//  void QQuickMultiEffect::blurMultiplierChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect21blurMultiplierChangedEv(
    QQuickMultiEffect *self) {
  self->blurMultiplierChanged();
}

//  void QQuickMultiEffect::shadowEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect20shadowEnabledChangedEv(
    QQuickMultiEffect *self) {
  self->shadowEnabledChanged();
}

//  void QQuickMultiEffect::shadowOpacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect20shadowOpacityChangedEv(
    QQuickMultiEffect *self) {
  self->shadowOpacityChanged();
}

//  void QQuickMultiEffect::shadowBlurChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17shadowBlurChangedEv(
    QQuickMultiEffect *self) {
  self->shadowBlurChanged();
}

//  void QQuickMultiEffect::shadowHorizontalOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect29shadowHorizontalOffsetChangedEv(
    QQuickMultiEffect *self) {
  self->shadowHorizontalOffsetChanged();
}

//  void QQuickMultiEffect::shadowVerticalOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect27shadowVerticalOffsetChangedEv(
    QQuickMultiEffect *self) {
  self->shadowVerticalOffsetChanged();
}

//  void QQuickMultiEffect::shadowColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18shadowColorChangedEv(
    QQuickMultiEffect *self) {
  self->shadowColorChanged();
}

//  void QQuickMultiEffect::shadowScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18shadowScaleChangedEv(
    QQuickMultiEffect *self) {
  self->shadowScaleChanged();
}

//  void QQuickMultiEffect::maskEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect18maskEnabledChangedEv(
    QQuickMultiEffect *self) {
  self->maskEnabledChanged();
}

//  void QQuickMultiEffect::maskSourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17maskSourceChangedEv(
    QQuickMultiEffect *self) {
  self->maskSourceChanged();
}

//  void QQuickMultiEffect::maskThresholdMinChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect23maskThresholdMinChangedEv(
    QQuickMultiEffect *self) {
  self->maskThresholdMinChanged();
}

//  void QQuickMultiEffect::maskSpreadAtMinChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect22maskSpreadAtMinChangedEv(
    QQuickMultiEffect *self) {
  self->maskSpreadAtMinChanged();
}

//  void QQuickMultiEffect::maskThresholdMaxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect23maskThresholdMaxChangedEv(
    QQuickMultiEffect *self) {
  self->maskThresholdMaxChanged();
}

//  void QQuickMultiEffect::maskSpreadAtMaxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect22maskSpreadAtMaxChangedEv(
    QQuickMultiEffect *self) {
  self->maskSpreadAtMaxChanged();
}

//  void QQuickMultiEffect::maskInvertedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect19maskInvertedChangedEv(
    QQuickMultiEffect *self) {
  self->maskInvertedChanged();
}

//  void QQuickMultiEffect::itemRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect15itemRectChangedEv(
    QQuickMultiEffect *self) {
  self->itemRectChanged();
}

//  void QQuickMultiEffect::fragmentShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect21fragmentShaderChangedEv(
    QQuickMultiEffect *self) {
  self->fragmentShaderChanged();
}

//  void QQuickMultiEffect::vertexShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect19vertexShaderChangedEv(
    QQuickMultiEffect *self) {
  self->vertexShaderChanged();
}

//  void QQuickMultiEffect::hasProxySourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect21hasProxySourceChangedEv(
    QQuickMultiEffect *self) {
  self->hasProxySourceChanged();
}

//  void QQuickMultiEffect::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect17componentCompleteEv(
    QQuickMultiEffect *self) {
  self->componentComplete();
}

//  void QQuickMultiEffect::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect14geometryChangeERK6QRectFS2_(
    QQuickMultiEffect *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickMultiEffect::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMultiEffect10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMultiEffect *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickMultiEffectPrivate *QQuickMultiEffect::d_func()
extern "C" Q_DECL_EXPORT
QQuickMultiEffectPrivate *ritual_ZN17QQuickMultiEffect6d_funcEv(
    QQuickMultiEffect *self) {
  return self->d_func();
}

//  const QQuickMultiEffectPrivate *QQuickMultiEffect::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMultiEffectPrivate *ritual_ZNK17QQuickMultiEffect6d_funcEv(
    const QQuickMultiEffect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMultiEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMultiEffect(
    QQuickMultiEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMultiEffect *>(self)->take(key, call);
}

//  void QQuickMultiEffect::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMultiEffect17componentCompleteEv(
    QQuickMultiEffect *self) {
  static_cast<OwnQQuickMultiEffect *>(self)->OwnQQuickMultiEffect::componentComplete();
}

//  void QQuickMultiEffect::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMultiEffect14geometryChangeERK6QRectFS2_(
    QQuickMultiEffect *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickMultiEffect *>(self)->OwnQQuickMultiEffect::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickMultiEffect::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMultiEffect10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMultiEffect *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickMultiEffect *>(self)->OwnQQuickMultiEffect::itemChange(
      change,
      *value);
}

#endif  // QT_CONFIG(quick_shadereffect)
