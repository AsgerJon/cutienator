//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickShaderEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickShaderEffect : QQuickShaderEffect {
  using QQuickShaderEffect::event;
  using QQuickShaderEffect::geometryChange;
  using QQuickShaderEffect::updatePaintNode;
  using QQuickShaderEffect::componentComplete;
  using QQuickShaderEffect::itemChange;
};

//  A QQuickShaderEffect that Python can take functions over in. Every QQuickShaderEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteQQuickShaderEffectCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectCall1)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQQuickShaderEffectCall2)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteQQuickShaderEffectCall5)(const void *, int *);
typedef const QRectF * (*CuteQQuickShaderEffectCall6)(const void *, int *);
typedef bool (*CuteQQuickShaderEffectCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickShaderEffectCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickShaderEffectCall9)(const void *, int *);
typedef void * (*CuteQQuickShaderEffectCall10)(const void *, int *);
typedef void (*CuteQQuickShaderEffectCall11)(const void *, int *);
typedef void (*CuteQQuickShaderEffectCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickShaderEffectCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickShaderEffectCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall21)(const void *, int *);
typedef void (*CuteQQuickShaderEffectCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShaderEffectCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShaderEffectCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickShaderEffectCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickShaderEffectCall33)(const void *, int *);
typedef void (*CuteQQuickShaderEffectCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShaderEffectCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShaderEffect : public QQuickShaderEffect {
public:
  using QQuickShaderEffect::QQuickShaderEffect;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShaderEffectCall0 call = reinterpret_cast<CuteQQuickShaderEffectCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickShaderEffect::event(e);
  }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShaderEffectCall1 call = reinterpret_cast<CuteQQuickShaderEffectCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShaderEffectCall2 call = reinterpret_cast<CuteQQuickShaderEffectCall2>(taken[2]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShaderEffect::updatePaintNode(oldNode, updatePaintNodeData);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShaderEffectCall3 call = reinterpret_cast<CuteQQuickShaderEffectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::componentComplete();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShaderEffectCall4 call = reinterpret_cast<CuteQQuickShaderEffectCall4>(taken[4]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShaderEffectCall5 call = reinterpret_cast<CuteQQuickShaderEffectCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShaderEffectCall6 call = reinterpret_cast<CuteQQuickShaderEffectCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShaderEffectCall7 call = reinterpret_cast<CuteQQuickShaderEffectCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShaderEffectCall8 call = reinterpret_cast<CuteQQuickShaderEffectCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickShaderEffectCall9 call = reinterpret_cast<CuteQQuickShaderEffectCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShaderEffectCall10 call = reinterpret_cast<CuteQQuickShaderEffectCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShaderEffectCall11 call = reinterpret_cast<CuteQQuickShaderEffectCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShaderEffectCall12 call = reinterpret_cast<CuteQQuickShaderEffectCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShaderEffectCall13 call = reinterpret_cast<CuteQQuickShaderEffectCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShaderEffectCall14 call = reinterpret_cast<CuteQQuickShaderEffectCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShaderEffectCall15 call = reinterpret_cast<CuteQQuickShaderEffectCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShaderEffectCall16 call = reinterpret_cast<CuteQQuickShaderEffectCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShaderEffectCall17 call = reinterpret_cast<CuteQQuickShaderEffectCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickShaderEffectCall18 call = reinterpret_cast<CuteQQuickShaderEffectCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickShaderEffectCall19 call = reinterpret_cast<CuteQQuickShaderEffectCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickShaderEffectCall20 call = reinterpret_cast<CuteQQuickShaderEffectCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickShaderEffectCall21 call = reinterpret_cast<CuteQQuickShaderEffectCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickShaderEffectCall22 call = reinterpret_cast<CuteQQuickShaderEffectCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickShaderEffectCall23 call = reinterpret_cast<CuteQQuickShaderEffectCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickShaderEffectCall24 call = reinterpret_cast<CuteQQuickShaderEffectCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickShaderEffectCall25 call = reinterpret_cast<CuteQQuickShaderEffectCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickShaderEffectCall26 call = reinterpret_cast<CuteQQuickShaderEffectCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickShaderEffectCall27 call = reinterpret_cast<CuteQQuickShaderEffectCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickShaderEffectCall28 call = reinterpret_cast<CuteQQuickShaderEffectCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickShaderEffectCall29 call = reinterpret_cast<CuteQQuickShaderEffectCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickShaderEffectCall30 call = reinterpret_cast<CuteQQuickShaderEffectCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickShaderEffectCall31 call = reinterpret_cast<CuteQQuickShaderEffectCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickShaderEffectCall32 call = reinterpret_cast<CuteQQuickShaderEffectCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickShaderEffectCall33 call = reinterpret_cast<CuteQQuickShaderEffectCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickShaderEffectCall34 call = reinterpret_cast<CuteQQuickShaderEffectCall34>(taken[34]);
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
      CuteQQuickShaderEffectCall35 call = reinterpret_cast<CuteQQuickShaderEffectCall35>(taken[35]);
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
      CuteQQuickShaderEffectCall36 call = reinterpret_cast<CuteQQuickShaderEffectCall36>(taken[36]);
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
      CuteQQuickShaderEffectCall37 call = reinterpret_cast<CuteQQuickShaderEffectCall37>(taken[37]);
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
      CuteQQuickShaderEffectCall38 call = reinterpret_cast<CuteQQuickShaderEffectCall38>(taken[38]);
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
      CuteQQuickShaderEffectCall39 call = reinterpret_cast<CuteQQuickShaderEffectCall39>(taken[39]);
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
      CuteQQuickShaderEffectCall40 call = reinterpret_cast<CuteQQuickShaderEffectCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShaderEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickShaderEffect10metaObjectEv(
    const QQuickShaderEffect *self) {
  return self->metaObject();
}

//  void *QQuickShaderEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickShaderEffect11qt_metacastEPKc(
    QQuickShaderEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickShaderEffect::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickShaderEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickShaderEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickShaderEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickShaderEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShaderEffect::tr(s, c, n));
}

//  QQuickShaderEffect::QQuickShaderEffect(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickShaderEffect *ritual_ZN18QQuickShaderEffectC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickShaderEffect(parent);
}

//  QQuickShaderEffect::~QQuickShaderEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffectD1Ev(QQuickShaderEffect *self) {
  delete self;
}

//  QUrl QQuickShaderEffect::fragmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickShaderEffect14fragmentShaderEv(
    const QQuickShaderEffect *self) {
  return new QUrl(self->fragmentShader());
}

//  void QQuickShaderEffect::setFragmentShader(const QUrl &fileUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect17setFragmentShaderERK4QUrl(
    QQuickShaderEffect *self,
    const QUrl *fileUrl) {
  self->setFragmentShader(*fileUrl);
}

//  QUrl QQuickShaderEffect::vertexShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickShaderEffect12vertexShaderEv(
    const QQuickShaderEffect *self) {
  return new QUrl(self->vertexShader());
}

//  void QQuickShaderEffect::setVertexShader(const QUrl &fileUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect15setVertexShaderERK4QUrl(
    QQuickShaderEffect *self,
    const QUrl *fileUrl) {
  self->setVertexShader(*fileUrl);
}

//  bool QQuickShaderEffect::blending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickShaderEffect8blendingEv(
    const QQuickShaderEffect *self) {
  return self->blending();
}

//  void QQuickShaderEffect::setBlending(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect11setBlendingEb(
    QQuickShaderEffect *self,
    bool enable) {
  self->setBlending(enable);
}

//  QVariant QQuickShaderEffect::mesh() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQuickShaderEffect4meshEv(
    const QQuickShaderEffect *self) {
  return new QVariant(self->mesh());
}

//  void QQuickShaderEffect::setMesh(const QVariant &mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect7setMeshERK8QVariant(
    QQuickShaderEffect *self,
    const QVariant *mesh) {
  self->setMesh(*mesh);
}

//  CullMode QQuickShaderEffect::cullMode() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffect::CullMode ritual_ZNK18QQuickShaderEffect8cullModeEv(
    const QQuickShaderEffect *self) {
  return self->cullMode();
}

//  void QQuickShaderEffect::setCullMode(CullMode face)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect11setCullModeENS_8CullModeE(
    QQuickShaderEffect *self,
    QQuickShaderEffect::CullMode face) {
  self->setCullMode(face);
}

//  bool QQuickShaderEffect::supportsAtlasTextures() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickShaderEffect21supportsAtlasTexturesEv(
    const QQuickShaderEffect *self) {
  return self->supportsAtlasTextures();
}

//  void QQuickShaderEffect::setSupportsAtlasTextures(bool supports)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect24setSupportsAtlasTexturesEb(
    QQuickShaderEffect *self,
    bool supports) {
  self->setSupportsAtlasTextures(supports);
}

//  QString QQuickShaderEffect::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickShaderEffect3logEv(
    const QQuickShaderEffect *self) {
  return new QString(self->log());
}

//  Status QQuickShaderEffect::status() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffect::Status ritual_ZNK18QQuickShaderEffect6statusEv(
    const QQuickShaderEffect *self) {
  return self->status();
}

//  bool QQuickShaderEffect::isComponentComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickShaderEffect19isComponentCompleteEv(
    const QQuickShaderEffect *self) {
  return self->isComponentComplete();
}

//  bool QQuickShaderEffect::updateUniformValue(const QByteArray &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickShaderEffect18updateUniformValueERK10QByteArrayRK8QVariant(
    QQuickShaderEffect *self,
    const QByteArray *name,
    const QVariant *value) {
  return self->updateUniformValue(*name, *value);
}

//  void QQuickShaderEffect::fragmentShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect21fragmentShaderChangedEv(
    QQuickShaderEffect *self) {
  self->fragmentShaderChanged();
}

//  void QQuickShaderEffect::vertexShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect19vertexShaderChangedEv(
    QQuickShaderEffect *self) {
  self->vertexShaderChanged();
}

//  void QQuickShaderEffect::blendingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect15blendingChangedEv(
    QQuickShaderEffect *self) {
  self->blendingChanged();
}

//  void QQuickShaderEffect::meshChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect11meshChangedEv(QQuickShaderEffect *self) {
  self->meshChanged();
}

//  void QQuickShaderEffect::cullModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect15cullModeChangedEv(
    QQuickShaderEffect *self) {
  self->cullModeChanged();
}

//  void QQuickShaderEffect::logChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect10logChangedEv(QQuickShaderEffect *self) {
  self->logChanged();
}

//  void QQuickShaderEffect::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect13statusChangedEv(
    QQuickShaderEffect *self) {
  self->statusChanged();
}

//  void QQuickShaderEffect::supportsAtlasTexturesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect28supportsAtlasTexturesChangedEv(
    QQuickShaderEffect *self) {
  self->supportsAtlasTexturesChanged();
}

//  bool QQuickShaderEffect::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickShaderEffect5eventEP6QEvent(
    QQuickShaderEffect *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickShaderEffect::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect14geometryChangeERK6QRectFS2_(
    QQuickShaderEffect *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN18QQuickShaderEffect15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShaderEffect *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return self->updatePaintNode(oldNode, updatePaintNodeData);
}

//  void QQuickShaderEffect::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect17componentCompleteEv(
    QQuickShaderEffect *self) {
  self->componentComplete();
}

//  void QQuickShaderEffect::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShaderEffect10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShaderEffect *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickShaderEffectPrivate *QQuickShaderEffect::d_func()
extern "C" Q_DECL_EXPORT
QQuickShaderEffectPrivate *ritual_ZN18QQuickShaderEffect6d_funcEv(
    QQuickShaderEffect *self) {
  return self->d_func();
}

//  const QQuickShaderEffectPrivate *QQuickShaderEffect::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickShaderEffectPrivate *ritual_ZNK18QQuickShaderEffect6d_funcEv(
    const QQuickShaderEffect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickShaderEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShaderEffect(
    QQuickShaderEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShaderEffect *>(self)->take(key, call);
}

//  bool QQuickShaderEffect::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickShaderEffect5eventEP6QEvent(
    QQuickShaderEffect *self,
    QEvent *e) {
  return static_cast<OwnQQuickShaderEffect *>(self)->OwnQQuickShaderEffect::event(
      e);
}

//  void QQuickShaderEffect::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickShaderEffect14geometryChangeERK6QRectFS2_(
    QQuickShaderEffect *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickShaderEffect *>(self)->OwnQQuickShaderEffect::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN18QQuickShaderEffect15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShaderEffect *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return static_cast<OwnQQuickShaderEffect *>(self)->OwnQQuickShaderEffect::updatePaintNode(
      oldNode,
      updatePaintNodeData);
}

//  void QQuickShaderEffect::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickShaderEffect17componentCompleteEv(
    QQuickShaderEffect *self) {
  static_cast<OwnQQuickShaderEffect *>(self)->OwnQQuickShaderEffect::componentComplete();
}

//  void QQuickShaderEffect::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickShaderEffect10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShaderEffect *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickShaderEffect *>(self)->OwnQQuickShaderEffect::itemChange(
      change,
      *value);
}

#endif  // QT_CONFIG(quick_shadereffect)
#endif  // QT_CONFIG(quick_shadereffect)
