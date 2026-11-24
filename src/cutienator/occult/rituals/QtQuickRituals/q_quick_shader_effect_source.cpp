//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffectsource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickShaderEffectSource may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickShaderEffectSource : QQuickShaderEffectSource {
  using QQuickShaderEffectSource::releaseResources;
  using QQuickShaderEffectSource::updatePaintNode;
  using QQuickShaderEffectSource::itemGeometryChanged;
  using QQuickShaderEffectSource::itemChange;
};

//  A QQuickShaderEffectSource that Python can take functions over in. Every QQuickShaderEffectSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteQQuickShaderEffectSourceCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQQuickShaderEffectSourceCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectSourceCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQQuickShaderEffectSourceCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectSourceCall4)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectSourceCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteQQuickShaderEffectSourceCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickShaderEffectSourceCall7)(const void *, int *);
typedef bool (*CuteQQuickShaderEffectSourceCall8)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickShaderEffectSourceCall9)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShaderEffectSourceCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall11)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall12)(const void *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall13)(const void *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickShaderEffectSourceCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickShaderEffectSourceCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall23)(const void *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShaderEffectSourceCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShaderEffectSourceCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectSourceCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectSourceCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectSourceCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShaderEffectSourceCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickShaderEffectSourceCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickShaderEffectSourceCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShaderEffectSourceCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectSourceCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShaderEffectSource : public QQuickShaderEffectSource {
public:
  using QQuickShaderEffectSource::QQuickShaderEffectSource;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffectSource::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall0 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShaderEffectSource::isTextureProvider();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QSGTextureProvider *QQuickShaderEffectSource::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall1 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickShaderEffectSource::textureProvider();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffectSource::releaseResources()
  void releaseResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall2 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShaderEffectSource::releaseResources();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QSGNode *QQuickShaderEffectSource::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall3 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShaderEffectSource::updatePaintNode(a0, a1);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffectSource::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall4 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall4>(taken[4]);
      call(this, item, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickShaderEffectSource::itemGeometryChanged(item, change, a2);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffectSource::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall5 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall5>(taken[5]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickShaderEffectSource::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall6 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall7 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall8 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall9 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall10 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall11 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall11>(taken[11]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall12 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall13 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall14 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall15 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall16 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall17 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall18 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall19 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall20 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall21 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall22 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall23 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall24 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall25 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall26 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall27 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall28 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall29 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall30 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall31 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall32 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall33 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall34 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall35 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall36 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall37 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall38 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall39 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall40 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickShaderEffectSourceCall41 call = reinterpret_cast<CuteQQuickShaderEffectSourceCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShaderEffectSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickShaderEffectSource10metaObjectEv(
    const QQuickShaderEffectSource *self) {
  return self->metaObject();
}

//  QString QQuickShaderEffectSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickShaderEffectSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShaderEffectSource::tr(s, c, n));
}

//  QQuickShaderEffectSource::QQuickShaderEffectSource(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource *ritual_ZN24QQuickShaderEffectSourceC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickShaderEffectSource(parent);
}

//  QQuickShaderEffectSource::~QQuickShaderEffectSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSourceD1Ev(
    QQuickShaderEffectSource *self) {
  delete self;
}

//  WrapMode QQuickShaderEffectSource::wrapMode() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::WrapMode ritual_ZNK24QQuickShaderEffectSource8wrapModeEv(
    const QQuickShaderEffectSource *self) {
  return self->wrapMode();
}

//  void QQuickShaderEffectSource::setWrapMode(WrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource11setWrapModeENS_8WrapModeE(
    QQuickShaderEffectSource *self,
    QQuickShaderEffectSource::WrapMode mode) {
  self->setWrapMode(mode);
}

//  QQuickItem *QQuickShaderEffectSource::sourceItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickShaderEffectSource10sourceItemEv(
    const QQuickShaderEffectSource *self) {
  return self->sourceItem();
}

//  void QQuickShaderEffectSource::setSourceItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource13setSourceItemEP10QQuickItem(
    QQuickShaderEffectSource *self,
    QQuickItem *item) {
  self->setSourceItem(item);
}

//  QRectF QQuickShaderEffectSource::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QQuickShaderEffectSource10sourceRectEv(
    const QQuickShaderEffectSource *self) {
  return new QRectF(self->sourceRect());
}

//  void QQuickShaderEffectSource::setSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource13setSourceRectERK6QRectF(
    QQuickShaderEffectSource *self,
    const QRectF *rect) {
  self->setSourceRect(*rect);
}

//  QSize QQuickShaderEffectSource::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QQuickShaderEffectSource11textureSizeEv(
    const QQuickShaderEffectSource *self) {
  return new QSize(self->textureSize());
}

//  void QQuickShaderEffectSource::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource14setTextureSizeERK5QSize(
    QQuickShaderEffectSource *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  Format QQuickShaderEffectSource::format() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::Format ritual_ZNK24QQuickShaderEffectSource6formatEv(
    const QQuickShaderEffectSource *self) {
  return self->format();
}

//  void QQuickShaderEffectSource::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource9setFormatENS_6FormatE(
    QQuickShaderEffectSource *self,
    QQuickShaderEffectSource::Format format) {
  self->setFormat(format);
}

//  bool QQuickShaderEffectSource::live() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickShaderEffectSource4liveEv(
    const QQuickShaderEffectSource *self) {
  return self->live();
}

//  void QQuickShaderEffectSource::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource7setLiveEb(
    QQuickShaderEffectSource *self,
    bool live) {
  self->setLive(live);
}

//  bool QQuickShaderEffectSource::hideSource() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickShaderEffectSource10hideSourceEv(
    const QQuickShaderEffectSource *self) {
  return self->hideSource();
}

//  void QQuickShaderEffectSource::setHideSource(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource13setHideSourceEb(
    QQuickShaderEffectSource *self,
    bool hide) {
  self->setHideSource(hide);
}

//  bool QQuickShaderEffectSource::mipmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickShaderEffectSource6mipmapEv(
    const QQuickShaderEffectSource *self) {
  return self->mipmap();
}

//  void QQuickShaderEffectSource::setMipmap(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource9setMipmapEb(
    QQuickShaderEffectSource *self,
    bool enabled) {
  self->setMipmap(enabled);
}

//  bool QQuickShaderEffectSource::recursive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickShaderEffectSource9recursiveEv(
    const QQuickShaderEffectSource *self) {
  return self->recursive();
}

//  void QQuickShaderEffectSource::setRecursive(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource12setRecursiveEb(
    QQuickShaderEffectSource *self,
    bool enabled) {
  self->setRecursive(enabled);
}

//  TextureMirroring QQuickShaderEffectSource::textureMirroring() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::TextureMirroring ritual_ZNK24QQuickShaderEffectSource16textureMirroringEv(
    const QQuickShaderEffectSource *self) {
  return self->textureMirroring();
}

//  void QQuickShaderEffectSource::setTextureMirroring(TextureMirroring
//      mirroring)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource19setTextureMirroringENS_16TextureMirroringE(
    QQuickShaderEffectSource *self,
    QQuickShaderEffectSource::TextureMirroring mirroring) {
  self->setTextureMirroring(mirroring);
}

//  bool QQuickShaderEffectSource::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickShaderEffectSource17isTextureProviderEv(
    const QQuickShaderEffectSource *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickShaderEffectSource::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK24QQuickShaderEffectSource15textureProviderEv(
    const QQuickShaderEffectSource *self) {
  return self->textureProvider();
}

//  void QQuickShaderEffectSource::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource14scheduleUpdateEv(
    QQuickShaderEffectSource *self) {
  self->scheduleUpdate();
}

//  int QQuickShaderEffectSource::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickShaderEffectSource7samplesEv(
    const QQuickShaderEffectSource *self) {
  return self->samples();
}

//  void QQuickShaderEffectSource::setSamples(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource10setSamplesEi(
    QQuickShaderEffectSource *self,
    int count) {
  self->setSamples(count);
}

//  void QQuickShaderEffectSource::sourceItemDestroyed(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource19sourceItemDestroyedEP7QObject(
    QQuickShaderEffectSource *self,
    QObject *item) {
  self->sourceItemDestroyed(item);
}

//  void QQuickShaderEffectSource::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource20invalidateSceneGraphEv(
    QQuickShaderEffectSource *self) {
  self->invalidateSceneGraph();
}

//  void QQuickShaderEffectSource::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource16releaseResourcesEv(
    QQuickShaderEffectSource *self) {
  self->releaseResources();
}

//  QSGNode *QQuickShaderEffectSource::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN24QQuickShaderEffectSource15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShaderEffectSource *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickShaderEffectSource::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickShaderEffectSource *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(item, *change, *a2);
}

//  void QQuickShaderEffectSource::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShaderEffectSource *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickShaderEffectSource::ensureTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShaderEffectSource13ensureTextureEv(
    QQuickShaderEffectSource *self) {
  self->ensureTexture();
}

//  a Python function taken by a CuteQQuickShaderEffectSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShaderEffectSource(
    QQuickShaderEffectSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShaderEffectSource *>(self)->take(key, call);
}

//  bool QQuickShaderEffectSource::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQuickShaderEffectSource17isTextureProviderEv(
    const QQuickShaderEffectSource *self) {
  return self->QQuickShaderEffectSource::isTextureProvider();
}

//  QSGTextureProvider *QQuickShaderEffectSource::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK24QQuickShaderEffectSource15textureProviderEv(
    const QQuickShaderEffectSource *self) {
  return self->QQuickShaderEffectSource::textureProvider();
}

//  void QQuickShaderEffectSource::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShaderEffectSource16releaseResourcesEv(
    QQuickShaderEffectSource *self) {
  static_cast<OwnQQuickShaderEffectSource *>(self)->OwnQQuickShaderEffectSource::releaseResources();
}

//  QSGNode *QQuickShaderEffectSource::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN24QQuickShaderEffectSource15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShaderEffectSource *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickShaderEffectSource *>(self)->OwnQQuickShaderEffectSource::updatePaintNode(
      a0,
      a1);
}

//  void QQuickShaderEffectSource::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickShaderEffectSource *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  static_cast<OwnQQuickShaderEffectSource *>(self)->OwnQQuickShaderEffectSource::itemGeometryChanged(
      item,
      *change,
      *a2);
}

//  void QQuickShaderEffectSource::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShaderEffectSource10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShaderEffectSource *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickShaderEffectSource *>(self)->OwnQQuickShaderEffectSource::itemChange(
      change,
      *value);
}

#endif  // QT_CONFIG(quick_shadereffect)
