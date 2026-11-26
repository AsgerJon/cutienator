//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolyg
//  onshape_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolygonshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  Only a class built on QQuickRegularPolygonShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRegularPolygonShape : QQuickRegularPolygonShape {
  using QQuickRegularPolygonShape::itemChange;
};

//  A QQuickRegularPolygonShape that Python can take functions over in. Every QQuickRegularPolygonShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRegularPolygonShapeCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickRegularPolygonShapeCall1)(const void *, int *);
typedef bool (*CuteQQuickRegularPolygonShapeCall2)(const void *, const QPointF *, int *);
typedef void * (*CuteQQuickRegularPolygonShapeCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall4)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall5)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickRegularPolygonShapeCall7)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRegularPolygonShapeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRegularPolygonShapeCall9)(const void *, int *);
typedef void * (*CuteQQuickRegularPolygonShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRegularPolygonShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRegularPolygonShapeCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRegularPolygonShapeCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall22)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRegularPolygonShapeCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRegularPolygonShapeCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRegularPolygonShapeCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRegularPolygonShapeCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRegularPolygonShapeCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRegularPolygonShapeCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRegularPolygonShapeCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickRegularPolygonShapeCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRegularPolygonShapeCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRegularPolygonShapeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRegularPolygonShape : public QQuickRegularPolygonShape {
public:
  using QQuickRegularPolygonShape::QQuickRegularPolygonShape;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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

  //  void QQuickRegularPolygonShape::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall0 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall0>(taken[0]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickRegularPolygonShape::itemChange(change, value);
  }

  //  QRectF QQuickShape::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall1 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShape::boundingRect();
  }

  //  bool QQuickShape::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall2 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall3 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall3>(taken[3]);
      void * given = call(this, node, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShape::updatePaintNode(node, a1);
  }

  //  void QQuickShape::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall4 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::updatePolish();
  }

  //  void QQuickShape::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall5 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::componentComplete();
  }

  //  void QQuickShape::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall6 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::classBegin();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall7 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall7>(taken[7]);
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
      CuteQQuickRegularPolygonShapeCall8 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall8>(taken[8]);
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
      CuteQQuickRegularPolygonShapeCall9 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall10 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall10>(taken[10]);
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
      CuteQQuickRegularPolygonShapeCall11 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall11>(taken[11]);
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
      CuteQQuickRegularPolygonShapeCall12 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall13 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall14 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall14>(taken[14]);
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
      CuteQQuickRegularPolygonShapeCall15 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall15>(taken[15]);
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
      CuteQQuickRegularPolygonShapeCall16 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall17 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall18 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall19 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall20 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall21 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall22 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall23 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall23>(taken[23]);
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
      CuteQQuickRegularPolygonShapeCall24 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall24>(taken[24]);
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
      CuteQQuickRegularPolygonShapeCall25 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall26 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall27 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall28 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall28>(taken[28]);
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
      CuteQQuickRegularPolygonShapeCall29 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall29>(taken[29]);
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
      CuteQQuickRegularPolygonShapeCall30 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall30>(taken[30]);
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
      CuteQQuickRegularPolygonShapeCall31 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall31>(taken[31]);
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
      CuteQQuickRegularPolygonShapeCall32 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall32>(taken[32]);
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
      CuteQQuickRegularPolygonShapeCall33 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapeCall34 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall34>(taken[34]);
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
      CuteQQuickRegularPolygonShapeCall35 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall35>(taken[35]);
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
      CuteQQuickRegularPolygonShapeCall36 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall36>(taken[36]);
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
      CuteQQuickRegularPolygonShapeCall37 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall37>(taken[37]);
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
      CuteQQuickRegularPolygonShapeCall38 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall38>(taken[38]);
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
      CuteQQuickRegularPolygonShapeCall39 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall39>(taken[39]);
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
      CuteQQuickRegularPolygonShapeCall40 call = reinterpret_cast<CuteQQuickRegularPolygonShapeCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRegularPolygonShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickRegularPolygonShape10metaObjectEv(
    const QQuickRegularPolygonShape *self) {
  return self->metaObject();
}

//  void *QQuickRegularPolygonShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickRegularPolygonShape11qt_metacastEPKc(
    QQuickRegularPolygonShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRegularPolygonShape::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickRegularPolygonShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRegularPolygonShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRegularPolygonShape::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickRegularPolygonShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRegularPolygonShape::tr(s, c, n));
}

//  QQuickRegularPolygonShape::QQuickRegularPolygonShape(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRegularPolygonShape *ritual_ZN25QQuickRegularPolygonShapeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRegularPolygonShape(parent);
}

//  QQuickRegularPolygonShape::~QQuickRegularPolygonShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShapeD1Ev(
    QQuickRegularPolygonShape *self) {
  delete self;
}

//  qreal QQuickRegularPolygonShape::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickRegularPolygonShape10dashOffsetEv(
    const QQuickRegularPolygonShape *self) {
  return self->dashOffset();
}

//  void QQuickRegularPolygonShape::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape13setDashOffsetEd(
    QQuickRegularPolygonShape *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  qreal QQuickRegularPolygonShape::cornerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickRegularPolygonShape12cornerRadiusEv(
    const QQuickRegularPolygonShape *self) {
  return self->cornerRadius();
}

//  void QQuickRegularPolygonShape::setCornerRadius(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape15setCornerRadiusEd(
    QQuickRegularPolygonShape *self,
    qreal a0) {
  self->setCornerRadius(a0);
}

//  int QQuickRegularPolygonShape::sideCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuickRegularPolygonShape9sideCountEv(
    const QQuickRegularPolygonShape *self) {
  return self->sideCount();
}

//  void QQuickRegularPolygonShape::setSideCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape12setSideCountEi(
    QQuickRegularPolygonShape *self,
    int a0) {
  self->setSideCount(a0);
}

//  qreal QQuickRegularPolygonShape::strokeWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickRegularPolygonShape11strokeWidthEv(
    const QQuickRegularPolygonShape *self) {
  return self->strokeWidth();
}

//  void QQuickRegularPolygonShape::setStrokeWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape14setStrokeWidthEd(
    QQuickRegularPolygonShape *self,
    qreal width) {
  self->setStrokeWidth(width);
}

//  QColor QQuickRegularPolygonShape::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickRegularPolygonShape9fillColorEv(
    const QQuickRegularPolygonShape *self) {
  return new QColor(self->fillColor());
}

//  void QQuickRegularPolygonShape::setFillColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape12setFillColorERK6QColor(
    QQuickRegularPolygonShape *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QColor QQuickRegularPolygonShape::strokeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickRegularPolygonShape11strokeColorEv(
    const QQuickRegularPolygonShape *self) {
  return new QColor(self->strokeColor());
}

//  void QQuickRegularPolygonShape::setStrokeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape14setStrokeColorERK6QColor(
    QQuickRegularPolygonShape *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  QQuickShapePath::CapStyle QQuickRegularPolygonShape::capStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::CapStyle ritual_ZNK25QQuickRegularPolygonShape8capStyleEv(
    const QQuickRegularPolygonShape *self) {
  return self->capStyle();
}

//  void QQuickRegularPolygonShape::setCapStyle(QQuickShapePath::CapStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape11setCapStyleEN15QQuickShapePath8CapStyleE(
    QQuickRegularPolygonShape *self,
    QQuickShapePath::CapStyle style) {
  self->setCapStyle(style);
}

//  QQuickShapePath::JoinStyle QQuickRegularPolygonShape::joinStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::JoinStyle ritual_ZNK25QQuickRegularPolygonShape9joinStyleEv(
    const QQuickRegularPolygonShape *self) {
  return self->joinStyle();
}

//  void QQuickRegularPolygonShape::setJoinStyle(QQuickShapePath::JoinStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape12setJoinStyleEN15QQuickShapePath9JoinStyleE(
    QQuickRegularPolygonShape *self,
    QQuickShapePath::JoinStyle style) {
  self->setJoinStyle(style);
}

//  QQuickShapePath::StrokeStyle QQuickRegularPolygonShape::strokeStyle()
//      const
extern "C" Q_DECL_EXPORT
QQuickShapePath::StrokeStyle ritual_ZNK25QQuickRegularPolygonShape11strokeStyleEv(
    const QQuickRegularPolygonShape *self) {
  return self->strokeStyle();
}

//  void
//      QQuickRegularPolygonShape::setStrokeStyle(QQuickShapePath::StrokeStyl
//      e style)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape14setStrokeStyleEN15QQuickShapePath11StrokeStyleE(
    QQuickRegularPolygonShape *self,
    QQuickShapePath::StrokeStyle style) {
  self->setStrokeStyle(style);
}

//  QList<qreal> QQuickRegularPolygonShape::dashPattern() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK25QQuickRegularPolygonShape11dashPatternEv(
    const QQuickRegularPolygonShape *self) {
  return new QList<qreal>(self->dashPattern());
}

//  void QQuickRegularPolygonShape::setDashPattern(const QList<qreal> &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape14setDashPatternERK5QListIdE(
    QQuickRegularPolygonShape *self,
    const QList<qreal> *array) {
  self->setDashPattern(*array);
}

//  QQuickShapeGradient *QQuickRegularPolygonShape::fillGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK25QQuickRegularPolygonShape12fillGradientEv(
    const QQuickRegularPolygonShape *self) {
  return self->fillGradient();
}

//  void QQuickRegularPolygonShape::setFillGradient(QQuickShapeGradient
//      *fillGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape15setFillGradientEP19QQuickShapeGradient(
    QQuickRegularPolygonShape *self,
    QQuickShapeGradient *fillGradient) {
  self->setFillGradient(fillGradient);
}

//  void QQuickRegularPolygonShape::resetFillGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape17resetFillGradientEv(
    QQuickRegularPolygonShape *self) {
  self->resetFillGradient();
}

//  QQuickItem *QQuickRegularPolygonShape::fillItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK25QQuickRegularPolygonShape8fillItemEv(
    const QQuickRegularPolygonShape *self) {
  return self->fillItem();
}

//  void QQuickRegularPolygonShape::setFillItem(QQuickItem *newFillItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape11setFillItemEP10QQuickItem(
    QQuickRegularPolygonShape *self,
    QQuickItem *newFillItem) {
  self->setFillItem(newFillItem);
}

//  void QQuickRegularPolygonShape::cornerRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape19cornerRadiusChangedEv(
    QQuickRegularPolygonShape *self) {
  self->cornerRadiusChanged();
}

//  void QQuickRegularPolygonShape::sideCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape16sideCountChangedEv(
    QQuickRegularPolygonShape *self) {
  self->sideCountChanged();
}

//  void QQuickRegularPolygonShape::strokeColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape18strokeColorChangedEv(
    QQuickRegularPolygonShape *self) {
  self->strokeColorChanged();
}

//  void QQuickRegularPolygonShape::strokeWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape18strokeWidthChangedEv(
    QQuickRegularPolygonShape *self) {
  self->strokeWidthChanged();
}

//  void QQuickRegularPolygonShape::fillColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape16fillColorChangedEv(
    QQuickRegularPolygonShape *self) {
  self->fillColorChanged();
}

//  void QQuickRegularPolygonShape::joinStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape16joinStyleChangedEv(
    QQuickRegularPolygonShape *self) {
  self->joinStyleChanged();
}

//  void QQuickRegularPolygonShape::capStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape15capStyleChangedEv(
    QQuickRegularPolygonShape *self) {
  self->capStyleChanged();
}

//  void QQuickRegularPolygonShape::strokeStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape18strokeStyleChangedEv(
    QQuickRegularPolygonShape *self) {
  self->strokeStyleChanged();
}

//  void QQuickRegularPolygonShape::dashOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape17dashOffsetChangedEv(
    QQuickRegularPolygonShape *self) {
  self->dashOffsetChanged();
}

//  void QQuickRegularPolygonShape::dashPatternChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape18dashPatternChangedEv(
    QQuickRegularPolygonShape *self) {
  self->dashPatternChanged();
}

//  void QQuickRegularPolygonShape::fillGradientChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape19fillGradientChangedEv(
    QQuickRegularPolygonShape *self) {
  self->fillGradientChanged();
}

//  void QQuickRegularPolygonShape::fillItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape15fillItemChangedEv(
    QQuickRegularPolygonShape *self) {
  self->fillItemChanged();
}

//  void QQuickRegularPolygonShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRegularPolygonShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRegularPolygonShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickRegularPolygonShapePrivate *QQuickRegularPolygonShape::d_func()
extern "C" Q_DECL_EXPORT
QQuickRegularPolygonShapePrivate *ritual_ZN25QQuickRegularPolygonShape6d_funcEv(
    QQuickRegularPolygonShape *self) {
  return self->d_func();
}

//  const QQuickRegularPolygonShapePrivate
//      *QQuickRegularPolygonShape::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRegularPolygonShapePrivate *ritual_ZNK25QQuickRegularPolygonShape6d_funcEv(
    const QQuickRegularPolygonShape *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickRegularPolygonShape, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRegularPolygonShape(
    QQuickRegularPolygonShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRegularPolygonShape *>(self)->take(key, call);
}

//  void QQuickRegularPolygonShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickRegularPolygonShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRegularPolygonShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickRegularPolygonShape *>(self)->OwnQQuickRegularPolygonShape::itemChange(
      change,
      *value);
}

//  a QList<qreal> a ritual of QQuickRegularPolygonShape gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickRegularPolygonShape__QList_qreal(QList<qreal> *self) {
  delete self;
}
