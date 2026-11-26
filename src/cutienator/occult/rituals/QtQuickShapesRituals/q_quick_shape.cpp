//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  Only a class built on QQuickShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickShape : QQuickShape {
  using QQuickShape::updatePaintNode;
  using QQuickShape::updatePolish;
  using QQuickShape::itemChange;
  using QQuickShape::componentComplete;
  using QQuickShape::classBegin;
};

//  A QQuickShape that Python can take functions over in. Every QQuickShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQQuickShapeCall0)(const void *, int *);
typedef bool (*CuteQQuickShapeCall1)(const void *, const QPointF *, int *);
typedef void * (*CuteQQuickShapeCall2)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickShapeCall3)(const void *, int *);
typedef void (*CuteQQuickShapeCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickShapeCall5)(const void *, int *);
typedef void (*CuteQQuickShapeCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickShapeCall7)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickShapeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickShapeCall9)(const void *, int *);
typedef void * (*CuteQQuickShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickShapeCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickShapeCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickShapeCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickShapeCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShapeCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickShapeCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShapeCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShapeCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShapeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickShapeCall22)(const void *, int *);
typedef void (*CuteQQuickShapeCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShapeCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickShapeCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickShapeCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShapeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickShapeCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShapeCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShapeCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShapeCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickShapeCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickShapeCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickShapeCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShape : public QQuickShape {
public:
  using QQuickShape::QQuickShape;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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

  //  QRectF QQuickShape::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeCall0 call = reinterpret_cast<CuteQQuickShapeCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShape::boundingRect();
  }

  //  bool QQuickShape::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeCall1 call = reinterpret_cast<CuteQQuickShapeCall1>(taken[1]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickShape::contains(point);
  }

  //  QSGNode *QQuickShape::updatePaintNode(QSGNode *node,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *node,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeCall2 call = reinterpret_cast<CuteQQuickShapeCall2>(taken[2]);
      void * given = call(this, node, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShape::updatePaintNode(node, a1);
  }

  //  void QQuickShape::updatePolish()
  void updatePolish() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShapeCall3 call = reinterpret_cast<CuteQQuickShapeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::updatePolish();
  }

  //  void QQuickShape::itemChange(ItemChange change, const ItemChangeData
  //      &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShapeCall4 call = reinterpret_cast<CuteQQuickShapeCall4>(taken[4]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickShape::itemChange(change, data);
  }

  //  void QQuickShape::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShapeCall5 call = reinterpret_cast<CuteQQuickShapeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::componentComplete();
  }

  //  void QQuickShape::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShapeCall6 call = reinterpret_cast<CuteQQuickShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::classBegin();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShapeCall7 call = reinterpret_cast<CuteQQuickShapeCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShapeCall8 call = reinterpret_cast<CuteQQuickShapeCall8>(taken[8]);
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
      CuteQQuickShapeCall9 call = reinterpret_cast<CuteQQuickShapeCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShapeCall10 call = reinterpret_cast<CuteQQuickShapeCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShapeCall11 call = reinterpret_cast<CuteQQuickShapeCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShapeCall12 call = reinterpret_cast<CuteQQuickShapeCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShapeCall13 call = reinterpret_cast<CuteQQuickShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShapeCall14 call = reinterpret_cast<CuteQQuickShapeCall14>(taken[14]);
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
      CuteQQuickShapeCall15 call = reinterpret_cast<CuteQQuickShapeCall15>(taken[15]);
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
      CuteQQuickShapeCall16 call = reinterpret_cast<CuteQQuickShapeCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShapeCall17 call = reinterpret_cast<CuteQQuickShapeCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickShapeCall18 call = reinterpret_cast<CuteQQuickShapeCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickShapeCall19 call = reinterpret_cast<CuteQQuickShapeCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickShapeCall20 call = reinterpret_cast<CuteQQuickShapeCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickShapeCall21 call = reinterpret_cast<CuteQQuickShapeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickShapeCall22 call = reinterpret_cast<CuteQQuickShapeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickShapeCall23 call = reinterpret_cast<CuteQQuickShapeCall23>(taken[23]);
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
      CuteQQuickShapeCall24 call = reinterpret_cast<CuteQQuickShapeCall24>(taken[24]);
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
      CuteQQuickShapeCall25 call = reinterpret_cast<CuteQQuickShapeCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickShapeCall26 call = reinterpret_cast<CuteQQuickShapeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickShapeCall27 call = reinterpret_cast<CuteQQuickShapeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickShapeCall28 call = reinterpret_cast<CuteQQuickShapeCall28>(taken[28]);
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
      CuteQQuickShapeCall29 call = reinterpret_cast<CuteQQuickShapeCall29>(taken[29]);
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
      CuteQQuickShapeCall30 call = reinterpret_cast<CuteQQuickShapeCall30>(taken[30]);
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
      CuteQQuickShapeCall31 call = reinterpret_cast<CuteQQuickShapeCall31>(taken[31]);
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
      CuteQQuickShapeCall32 call = reinterpret_cast<CuteQQuickShapeCall32>(taken[32]);
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
      CuteQQuickShapeCall33 call = reinterpret_cast<CuteQQuickShapeCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickShapeCall34 call = reinterpret_cast<CuteQQuickShapeCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickShapeCall35 call = reinterpret_cast<CuteQQuickShapeCall35>(taken[35]);
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
      CuteQQuickShapeCall36 call = reinterpret_cast<CuteQQuickShapeCall36>(taken[36]);
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
      CuteQQuickShapeCall37 call = reinterpret_cast<CuteQQuickShapeCall37>(taken[37]);
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
      CuteQQuickShapeCall38 call = reinterpret_cast<CuteQQuickShapeCall38>(taken[38]);
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
      CuteQQuickShapeCall39 call = reinterpret_cast<CuteQQuickShapeCall39>(taken[39]);
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
      CuteQQuickShapeCall40 call = reinterpret_cast<CuteQQuickShapeCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickShape10metaObjectEv(
    const QQuickShape *self) {
  return self->metaObject();
}

//  void *QQuickShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QQuickShape11qt_metacastEPKc(
    QQuickShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickShape::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QQuickShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShape::tr(s, c, n));
}

//  QQuickShape::QQuickShape(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickShape *ritual_ZN11QQuickShapeC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickShape(parent);
}

//  QQuickShape::~QQuickShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShapeD1Ev(QQuickShape *self) {
  delete self;
}

//  RendererType QQuickShape::rendererType() const
extern "C" Q_DECL_EXPORT
QQuickShape::RendererType ritual_ZNK11QQuickShape12rendererTypeEv(
    const QQuickShape *self) {
  return self->rendererType();
}

//  bool QQuickShape::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickShape12asynchronousEv(const QQuickShape *self) {
  return self->asynchronous();
}

//  void QQuickShape::setAsynchronous(bool async)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape15setAsynchronousEb(
    QQuickShape *self,
    bool async) {
  self->setAsynchronous(async);
}

//  RendererType QQuickShape::preferredRendererType() const
extern "C" Q_DECL_EXPORT
QQuickShape::RendererType ritual_ZNK11QQuickShape21preferredRendererTypeEv(
    const QQuickShape *self) {
  return self->preferredRendererType();
}

//  void QQuickShape::setPreferredRendererType(RendererType preferredType)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape24setPreferredRendererTypeENS_12RendererTypeE(
    QQuickShape *self,
    QQuickShape::RendererType preferredType) {
  self->setPreferredRendererType(preferredType);
}

//  QRectF QQuickShape::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QQuickShape12boundingRectEv(const QQuickShape *self) {
  return new QRectF(self->boundingRect());
}

//  bool QQuickShape::vendorExtensionsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickShape23vendorExtensionsEnabledEv(
    const QQuickShape *self) {
  return self->vendorExtensionsEnabled();
}

//  void QQuickShape::setVendorExtensionsEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape26setVendorExtensionsEnabledEb(
    QQuickShape *self,
    bool enable) {
  self->setVendorExtensionsEnabled(enable);
}

//  Status QQuickShape::status() const
extern "C" Q_DECL_EXPORT
QQuickShape::Status ritual_ZNK11QQuickShape6statusEv(
    const QQuickShape *self) {
  return self->status();
}

//  ContainsMode QQuickShape::containsMode() const
extern "C" Q_DECL_EXPORT
QQuickShape::ContainsMode ritual_ZNK11QQuickShape12containsModeEv(
    const QQuickShape *self) {
  return self->containsMode();
}

//  void QQuickShape::setContainsMode(ContainsMode containsMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape15setContainsModeENS_12ContainsModeE(
    QQuickShape *self,
    QQuickShape::ContainsMode containsMode) {
  self->setContainsMode(containsMode);
}

//  bool QQuickShape::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickShape8containsERK7QPointF(
    const QQuickShape *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  QQmlListProperty<QObject> QQuickShape::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN11QQuickShape4dataEv(QQuickShape *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  FillMode QQuickShape::fillMode() const
extern "C" Q_DECL_EXPORT
QQuickShape::FillMode ritual_ZNK11QQuickShape8fillModeEv(
    const QQuickShape *self) {
  return self->fillMode();
}

//  void QQuickShape::setFillMode(FillMode newFillMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape11setFillModeENS_8FillModeE(
    QQuickShape *self,
    QQuickShape::FillMode newFillMode) {
  self->setFillMode(newFillMode);
}

//  HAlignment QQuickShape::horizontalAlignment() const
extern "C" Q_DECL_EXPORT
QQuickShape::HAlignment ritual_ZNK11QQuickShape19horizontalAlignmentEv(
    const QQuickShape *self) {
  return self->horizontalAlignment();
}

//  void QQuickShape::setHorizontalAlignment(HAlignment
//      newHorizontalAlignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape22setHorizontalAlignmentENS_10HAlignmentE(
    QQuickShape *self,
    QQuickShape::HAlignment newHorizontalAlignment) {
  self->setHorizontalAlignment(newHorizontalAlignment);
}

//  VAlignment QQuickShape::verticalAlignment() const
extern "C" Q_DECL_EXPORT
QQuickShape::VAlignment ritual_ZNK11QQuickShape17verticalAlignmentEv(
    const QQuickShape *self) {
  return self->verticalAlignment();
}

//  void QQuickShape::setVerticalAlignment(VAlignment newVerticalAlignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape20setVerticalAlignmentENS_10VAlignmentE(
    QQuickShape *self,
    QQuickShape::VAlignment newVerticalAlignment) {
  self->setVerticalAlignment(newVerticalAlignment);
}

//  QQuickShape::QQuickShape(QQuickShapePrivate &dd, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickShape *ritual_ZN11QQuickShapeC1ER18QQuickShapePrivateP10QQuickItem(
    QQuickShapePrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickShape(*dd, parent);
}

//  QSGNode *QQuickShape::updatePaintNode(QSGNode *node, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN11QQuickShape15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShape *self,
    QSGNode *node,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(node, a1);
}

//  void QQuickShape::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape12updatePolishEv(QQuickShape *self) {
  self->updatePolish();
}

//  void QQuickShape::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape17componentCompleteEv(QQuickShape *self) {
  self->componentComplete();
}

//  void QQuickShape::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape10classBeginEv(QQuickShape *self) {
  self->classBegin();
}

//  void QQuickShape::rendererChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape15rendererChangedEv(QQuickShape *self) {
  self->rendererChanged();
}

//  void QQuickShape::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape19asynchronousChangedEv(QQuickShape *self) {
  self->asynchronousChanged();
}

//  void QQuickShape::vendorExtensionsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape30vendorExtensionsEnabledChangedEv(
    QQuickShape *self) {
  self->vendorExtensionsEnabledChanged();
}

//  void QQuickShape::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape13statusChangedEv(QQuickShape *self) {
  self->statusChanged();
}

//  void QQuickShape::preferredRendererTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape28preferredRendererTypeChangedEv(
    QQuickShape *self) {
  self->preferredRendererTypeChanged();
}

//  void QQuickShape::boundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape19boundingRectChangedEv(QQuickShape *self) {
  self->boundingRectChanged();
}

//  void QQuickShape::containsModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape19containsModeChangedEv(QQuickShape *self) {
  self->containsModeChanged();
}

//  void QQuickShape::fillModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape15fillModeChangedEv(QQuickShape *self) {
  self->fillModeChanged();
}

//  void QQuickShape::horizontalAlignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape26horizontalAlignmentChangedEv(
    QQuickShape *self) {
  self->horizontalAlignmentChanged();
}

//  void QQuickShape::verticalAlignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShape24verticalAlignmentChangedEv(QQuickShape *self) {
  self->verticalAlignmentChanged();
}

//  QQuickShapePrivate *QQuickShape::d_func()
extern "C" Q_DECL_EXPORT
QQuickShapePrivate *ritual_ZN11QQuickShape6d_funcEv(QQuickShape *self) {
  return self->d_func();
}

//  const QQuickShapePrivate *QQuickShape::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickShapePrivate *ritual_ZNK11QQuickShape6d_funcEv(
    const QQuickShape *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickShape, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShape(
    QQuickShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShape *>(self)->take(key, call);
}

//  QRectF QQuickShape::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK11QQuickShape12boundingRectEv(
    const QQuickShape *self) {
  return new QRectF(self->QQuickShape::boundingRect());
}

//  bool QQuickShape::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QQuickShape8containsERK7QPointF(
    const QQuickShape *self,
    const QPointF *point) {
  return self->QQuickShape::contains(*point);
}

//  QSGNode *QQuickShape::updatePaintNode(QSGNode *node, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN11QQuickShape15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickShape *self,
    QSGNode *node,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickShape *>(self)->OwnQQuickShape::updatePaintNode(
      node,
      a1);
}

//  void QQuickShape::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickShape12updatePolishEv(QQuickShape *self) {
  static_cast<OwnQQuickShape *>(self)->OwnQQuickShape::updatePolish();
}

//  void QQuickShape::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickShape *>(self)->OwnQQuickShape::itemChange(
      change,
      *data);
}

//  void QQuickShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickShape17componentCompleteEv(QQuickShape *self) {
  static_cast<OwnQQuickShape *>(self)->OwnQQuickShape::componentComplete();
}

//  void QQuickShape::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickShape10classBeginEv(QQuickShape *self) {
  static_cast<OwnQQuickShape *>(self)->OwnQQuickShape::classBegin();
}

//  a QQmlListProperty<QObject> a ritual of QQuickShape gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickShape__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
