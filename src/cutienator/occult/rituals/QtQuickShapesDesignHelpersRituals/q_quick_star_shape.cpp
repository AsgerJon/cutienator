//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p.h>
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

//  Only a class built on QQuickStarShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickStarShape : QQuickStarShape {
  using QQuickStarShape::itemChange;
};

//  A QQuickStarShape that Python can take functions over in. Every QQuickStarShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickStarShapeCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickStarShapeCall1)(const void *, int *);
typedef bool (*CuteQQuickStarShapeCall2)(const void *, const QPointF *, int *);
typedef void * (*CuteQQuickStarShapeCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickStarShapeCall4)(const void *, int *);
typedef void (*CuteQQuickStarShapeCall5)(const void *, int *);
typedef void (*CuteQQuickStarShapeCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickStarShapeCall7)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickStarShapeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickStarShapeCall9)(const void *, int *);
typedef void * (*CuteQQuickStarShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStarShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickStarShapeCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickStarShapeCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickStarShapeCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickStarShapeCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickStarShapeCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickStarShapeCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStarShapeCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStarShapeCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStarShapeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStarShapeCall22)(const void *, int *);
typedef void (*CuteQQuickStarShapeCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickStarShapeCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickStarShapeCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickStarShapeCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickStarShapeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickStarShapeCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStarShapeCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStarShapeCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStarShapeCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStarShapeCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickStarShapeCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickStarShapeCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStarShapeCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStarShapeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStarShape : public QQuickStarShape {
public:
  using QQuickStarShape::QQuickStarShape;
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

  //  void QQuickStarShape::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStarShapeCall0 call = reinterpret_cast<CuteQQuickStarShapeCall0>(taken[0]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickStarShape::itemChange(change, value);
  }

  //  QRectF QQuickShape::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStarShapeCall1 call = reinterpret_cast<CuteQQuickStarShapeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShape::boundingRect();
  }

  //  bool QQuickShape::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStarShapeCall2 call = reinterpret_cast<CuteQQuickStarShapeCall2>(taken[2]);
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
      CuteQQuickStarShapeCall3 call = reinterpret_cast<CuteQQuickStarShapeCall3>(taken[3]);
      void * given = call(this, node, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShape::updatePaintNode(node, a1);
  }

  //  void QQuickShape::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStarShapeCall4 call = reinterpret_cast<CuteQQuickStarShapeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::updatePolish();
  }

  //  void QQuickShape::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStarShapeCall5 call = reinterpret_cast<CuteQQuickStarShapeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::componentComplete();
  }

  //  void QQuickShape::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickStarShapeCall6 call = reinterpret_cast<CuteQQuickStarShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::classBegin();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStarShapeCall7 call = reinterpret_cast<CuteQQuickStarShapeCall7>(taken[7]);
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
      CuteQQuickStarShapeCall8 call = reinterpret_cast<CuteQQuickStarShapeCall8>(taken[8]);
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
      CuteQQuickStarShapeCall9 call = reinterpret_cast<CuteQQuickStarShapeCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStarShapeCall10 call = reinterpret_cast<CuteQQuickStarShapeCall10>(taken[10]);
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
      CuteQQuickStarShapeCall11 call = reinterpret_cast<CuteQQuickStarShapeCall11>(taken[11]);
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
      CuteQQuickStarShapeCall12 call = reinterpret_cast<CuteQQuickStarShapeCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickStarShapeCall13 call = reinterpret_cast<CuteQQuickStarShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickStarShapeCall14 call = reinterpret_cast<CuteQQuickStarShapeCall14>(taken[14]);
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
      CuteQQuickStarShapeCall15 call = reinterpret_cast<CuteQQuickStarShapeCall15>(taken[15]);
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
      CuteQQuickStarShapeCall16 call = reinterpret_cast<CuteQQuickStarShapeCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickStarShapeCall17 call = reinterpret_cast<CuteQQuickStarShapeCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickStarShapeCall18 call = reinterpret_cast<CuteQQuickStarShapeCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickStarShapeCall19 call = reinterpret_cast<CuteQQuickStarShapeCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickStarShapeCall20 call = reinterpret_cast<CuteQQuickStarShapeCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickStarShapeCall21 call = reinterpret_cast<CuteQQuickStarShapeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickStarShapeCall22 call = reinterpret_cast<CuteQQuickStarShapeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickStarShapeCall23 call = reinterpret_cast<CuteQQuickStarShapeCall23>(taken[23]);
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
      CuteQQuickStarShapeCall24 call = reinterpret_cast<CuteQQuickStarShapeCall24>(taken[24]);
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
      CuteQQuickStarShapeCall25 call = reinterpret_cast<CuteQQuickStarShapeCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickStarShapeCall26 call = reinterpret_cast<CuteQQuickStarShapeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickStarShapeCall27 call = reinterpret_cast<CuteQQuickStarShapeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickStarShapeCall28 call = reinterpret_cast<CuteQQuickStarShapeCall28>(taken[28]);
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
      CuteQQuickStarShapeCall29 call = reinterpret_cast<CuteQQuickStarShapeCall29>(taken[29]);
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
      CuteQQuickStarShapeCall30 call = reinterpret_cast<CuteQQuickStarShapeCall30>(taken[30]);
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
      CuteQQuickStarShapeCall31 call = reinterpret_cast<CuteQQuickStarShapeCall31>(taken[31]);
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
      CuteQQuickStarShapeCall32 call = reinterpret_cast<CuteQQuickStarShapeCall32>(taken[32]);
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
      CuteQQuickStarShapeCall33 call = reinterpret_cast<CuteQQuickStarShapeCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickStarShapeCall34 call = reinterpret_cast<CuteQQuickStarShapeCall34>(taken[34]);
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
      CuteQQuickStarShapeCall35 call = reinterpret_cast<CuteQQuickStarShapeCall35>(taken[35]);
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
      CuteQQuickStarShapeCall36 call = reinterpret_cast<CuteQQuickStarShapeCall36>(taken[36]);
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
      CuteQQuickStarShapeCall37 call = reinterpret_cast<CuteQQuickStarShapeCall37>(taken[37]);
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
      CuteQQuickStarShapeCall38 call = reinterpret_cast<CuteQQuickStarShapeCall38>(taken[38]);
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
      CuteQQuickStarShapeCall39 call = reinterpret_cast<CuteQQuickStarShapeCall39>(taken[39]);
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
      CuteQQuickStarShapeCall40 call = reinterpret_cast<CuteQQuickStarShapeCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStarShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickStarShape10metaObjectEv(
    const QQuickStarShape *self) {
  return self->metaObject();
}

//  void *QQuickStarShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickStarShape11qt_metacastEPKc(
    QQuickStarShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickStarShape::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickStarShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickStarShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickStarShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickStarShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStarShape::tr(s, c, n));
}

//  QQuickStarShape::QQuickStarShape(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickStarShape *ritual_ZN15QQuickStarShapeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickStarShape(parent);
}

//  QQuickStarShape::~QQuickStarShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShapeD1Ev(QQuickStarShape *self) {
  delete self;
}

//  qreal QQuickStarShape::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickStarShape10dashOffsetEv(
    const QQuickStarShape *self) {
  return self->dashOffset();
}

//  void QQuickStarShape::setDashOffset(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape13setDashOffsetEd(
    QQuickStarShape *self,
    qreal a0) {
  self->setDashOffset(a0);
}

//  qreal QQuickStarShape::cornerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickStarShape12cornerRadiusEv(
    const QQuickStarShape *self) {
  return self->cornerRadius();
}

//  void QQuickStarShape::setCornerRadius(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape15setCornerRadiusEd(
    QQuickStarShape *self,
    qreal a0) {
  self->setCornerRadius(a0);
}

//  qreal QQuickStarShape::ratio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickStarShape5ratioEv(const QQuickStarShape *self) {
  return self->ratio();
}

//  void QQuickStarShape::setRatio(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape8setRatioEd(QQuickStarShape *self, qreal a0) {
  self->setRatio(a0);
}

//  int QQuickStarShape::pointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickStarShape10pointCountEv(const QQuickStarShape *self) {
  return self->pointCount();
}

//  void QQuickStarShape::setPointCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape13setPointCountEi(
    QQuickStarShape *self,
    int a0) {
  self->setPointCount(a0);
}

//  qreal QQuickStarShape::strokeWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickStarShape11strokeWidthEv(
    const QQuickStarShape *self) {
  return self->strokeWidth();
}

//  void QQuickStarShape::setStrokeWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape14setStrokeWidthEd(
    QQuickStarShape *self,
    qreal a0) {
  self->setStrokeWidth(a0);
}

//  QColor QQuickStarShape::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickStarShape9fillColorEv(
    const QQuickStarShape *self) {
  return new QColor(self->fillColor());
}

//  void QQuickStarShape::setFillColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape12setFillColorERK6QColor(
    QQuickStarShape *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QColor QQuickStarShape::strokeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickStarShape11strokeColorEv(
    const QQuickStarShape *self) {
  return new QColor(self->strokeColor());
}

//  void QQuickStarShape::setStrokeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape14setStrokeColorERK6QColor(
    QQuickStarShape *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  QQuickShapePath::CapStyle QQuickStarShape::capStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::CapStyle ritual_ZNK15QQuickStarShape8capStyleEv(
    const QQuickStarShape *self) {
  return self->capStyle();
}

//  void QQuickStarShape::setCapStyle(QQuickShapePath::CapStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape11setCapStyleEN15QQuickShapePath8CapStyleE(
    QQuickStarShape *self,
    QQuickShapePath::CapStyle style) {
  self->setCapStyle(style);
}

//  QQuickShapePath::JoinStyle QQuickStarShape::joinStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::JoinStyle ritual_ZNK15QQuickStarShape9joinStyleEv(
    const QQuickStarShape *self) {
  return self->joinStyle();
}

//  void QQuickStarShape::setJoinStyle(QQuickShapePath::JoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape12setJoinStyleEN15QQuickShapePath9JoinStyleE(
    QQuickStarShape *self,
    QQuickShapePath::JoinStyle style) {
  self->setJoinStyle(style);
}

//  QQuickShapePath::StrokeStyle QQuickStarShape::strokeStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::StrokeStyle ritual_ZNK15QQuickStarShape11strokeStyleEv(
    const QQuickStarShape *self) {
  return self->strokeStyle();
}

//  void QQuickStarShape::setStrokeStyle(QQuickShapePath::StrokeStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape14setStrokeStyleEN15QQuickShapePath11StrokeStyleE(
    QQuickStarShape *self,
    QQuickShapePath::StrokeStyle style) {
  self->setStrokeStyle(style);
}

//  QList<qreal> QQuickStarShape::dashPattern() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK15QQuickStarShape11dashPatternEv(
    const QQuickStarShape *self) {
  return new QList<qreal>(self->dashPattern());
}

//  void QQuickStarShape::setDashPattern(const QList<qreal> &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape14setDashPatternERK5QListIdE(
    QQuickStarShape *self,
    const QList<qreal> *array) {
  self->setDashPattern(*array);
}

//  QQuickShapeGradient *QQuickStarShape::fillGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK15QQuickStarShape12fillGradientEv(
    const QQuickStarShape *self) {
  return self->fillGradient();
}

//  void QQuickStarShape::setFillGradient(QQuickShapeGradient *fillGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape15setFillGradientEP19QQuickShapeGradient(
    QQuickStarShape *self,
    QQuickShapeGradient *fillGradient) {
  self->setFillGradient(fillGradient);
}

//  void QQuickStarShape::resetFillGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape17resetFillGradientEv(QQuickStarShape *self) {
  self->resetFillGradient();
}

//  QQuickItem *QQuickStarShape::fillItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickStarShape8fillItemEv(
    const QQuickStarShape *self) {
  return self->fillItem();
}

//  void QQuickStarShape::setFillItem(QQuickItem *newFillItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape11setFillItemEP10QQuickItem(
    QQuickStarShape *self,
    QQuickItem *newFillItem) {
  self->setFillItem(newFillItem);
}

//  void QQuickStarShape::cornerRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape19cornerRadiusChangedEv(
    QQuickStarShape *self) {
  self->cornerRadiusChanged();
}

//  void QQuickStarShape::ratioChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape12ratioChangedEv(QQuickStarShape *self) {
  self->ratioChanged();
}

//  void QQuickStarShape::pointCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape17pointCountChangedEv(QQuickStarShape *self) {
  self->pointCountChanged();
}

//  void QQuickStarShape::strokeColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape18strokeColorChangedEv(
    QQuickStarShape *self) {
  self->strokeColorChanged();
}

//  void QQuickStarShape::strokeWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape18strokeWidthChangedEv(
    QQuickStarShape *self) {
  self->strokeWidthChanged();
}

//  void QQuickStarShape::fillColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape16fillColorChangedEv(QQuickStarShape *self) {
  self->fillColorChanged();
}

//  void QQuickStarShape::joinStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape16joinStyleChangedEv(QQuickStarShape *self) {
  self->joinStyleChanged();
}

//  void QQuickStarShape::capStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape15capStyleChangedEv(QQuickStarShape *self) {
  self->capStyleChanged();
}

//  void QQuickStarShape::strokeStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape18strokeStyleChangedEv(
    QQuickStarShape *self) {
  self->strokeStyleChanged();
}

//  void QQuickStarShape::dashOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape17dashOffsetChangedEv(QQuickStarShape *self) {
  self->dashOffsetChanged();
}

//  void QQuickStarShape::dashPatternChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape18dashPatternChangedEv(
    QQuickStarShape *self) {
  self->dashPatternChanged();
}

//  void QQuickStarShape::fillGradientChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape19fillGradientChangedEv(
    QQuickStarShape *self) {
  self->fillGradientChanged();
}

//  void QQuickStarShape::fillItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape15fillItemChangedEv(QQuickStarShape *self) {
  self->fillItemChanged();
}

//  void QQuickStarShape::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStarShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickStarShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickStarShapePrivate *QQuickStarShape::d_func()
extern "C" Q_DECL_EXPORT
QQuickStarShapePrivate *ritual_ZN15QQuickStarShape6d_funcEv(
    QQuickStarShape *self) {
  return self->d_func();
}

//  const QQuickStarShapePrivate *QQuickStarShape::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickStarShapePrivate *ritual_ZNK15QQuickStarShape6d_funcEv(
    const QQuickStarShape *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickStarShape, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStarShape(
    QQuickStarShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStarShape *>(self)->take(key, call);
}

//  void QQuickStarShape::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickStarShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickStarShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickStarShape *>(self)->OwnQQuickStarShape::itemChange(
      change,
      *value);
}

//  a QList<qreal> a ritual of QQuickStarShape gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickStarShape__QList_qreal(QList<qreal> *self) {
  delete self;
}
