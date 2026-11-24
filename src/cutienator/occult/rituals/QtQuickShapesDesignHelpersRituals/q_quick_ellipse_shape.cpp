//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p.h>
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

//  Only a class built on QQuickEllipseShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickEllipseShape : QQuickEllipseShape {
  using QQuickEllipseShape::itemChange;
};

//  A QQuickEllipseShape that Python can take functions over in. Every QQuickEllipseShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickEllipseShapeCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickEllipseShapeCall1)(const void *, int *);
typedef bool (*CuteQQuickEllipseShapeCall2)(const void *, const QPointF *, int *);
typedef void * (*CuteQQuickEllipseShapeCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickEllipseShapeCall4)(const void *, int *);
typedef void (*CuteQQuickEllipseShapeCall5)(const void *, int *);
typedef void (*CuteQQuickEllipseShapeCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickEllipseShapeCall7)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickEllipseShapeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickEllipseShapeCall9)(const void *, int *);
typedef void * (*CuteQQuickEllipseShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickEllipseShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickEllipseShapeCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickEllipseShapeCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickEllipseShapeCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall22)(const void *, int *);
typedef void (*CuteQQuickEllipseShapeCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickEllipseShapeCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickEllipseShapeCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickEllipseShapeCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickEllipseShapeCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickEllipseShapeCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickEllipseShapeCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickEllipseShapeCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickEllipseShapeCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickEllipseShapeCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickEllipseShapeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickEllipseShape : public QQuickEllipseShape {
public:
  using QQuickEllipseShape::QQuickEllipseShape;
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

  //  void QQuickEllipseShape::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall0 call = reinterpret_cast<CuteQQuickEllipseShapeCall0>(taken[0]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickEllipseShape::itemChange(change, value);
  }

  //  QRectF QQuickShape::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall1 call = reinterpret_cast<CuteQQuickEllipseShapeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShape::boundingRect();
  }

  //  bool QQuickShape::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall2 call = reinterpret_cast<CuteQQuickEllipseShapeCall2>(taken[2]);
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
      CuteQQuickEllipseShapeCall3 call = reinterpret_cast<CuteQQuickEllipseShapeCall3>(taken[3]);
      void * given = call(this, node, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShape::updatePaintNode(node, a1);
  }

  //  void QQuickShape::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall4 call = reinterpret_cast<CuteQQuickEllipseShapeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::updatePolish();
  }

  //  void QQuickShape::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall5 call = reinterpret_cast<CuteQQuickEllipseShapeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::componentComplete();
  }

  //  void QQuickShape::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall6 call = reinterpret_cast<CuteQQuickEllipseShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::classBegin();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall7 call = reinterpret_cast<CuteQQuickEllipseShapeCall7>(taken[7]);
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
      CuteQQuickEllipseShapeCall8 call = reinterpret_cast<CuteQQuickEllipseShapeCall8>(taken[8]);
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
      CuteQQuickEllipseShapeCall9 call = reinterpret_cast<CuteQQuickEllipseShapeCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall10 call = reinterpret_cast<CuteQQuickEllipseShapeCall10>(taken[10]);
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
      CuteQQuickEllipseShapeCall11 call = reinterpret_cast<CuteQQuickEllipseShapeCall11>(taken[11]);
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
      CuteQQuickEllipseShapeCall12 call = reinterpret_cast<CuteQQuickEllipseShapeCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall13 call = reinterpret_cast<CuteQQuickEllipseShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall14 call = reinterpret_cast<CuteQQuickEllipseShapeCall14>(taken[14]);
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
      CuteQQuickEllipseShapeCall15 call = reinterpret_cast<CuteQQuickEllipseShapeCall15>(taken[15]);
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
      CuteQQuickEllipseShapeCall16 call = reinterpret_cast<CuteQQuickEllipseShapeCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall17 call = reinterpret_cast<CuteQQuickEllipseShapeCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall18 call = reinterpret_cast<CuteQQuickEllipseShapeCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall19 call = reinterpret_cast<CuteQQuickEllipseShapeCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall20 call = reinterpret_cast<CuteQQuickEllipseShapeCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall21 call = reinterpret_cast<CuteQQuickEllipseShapeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall22 call = reinterpret_cast<CuteQQuickEllipseShapeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall23 call = reinterpret_cast<CuteQQuickEllipseShapeCall23>(taken[23]);
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
      CuteQQuickEllipseShapeCall24 call = reinterpret_cast<CuteQQuickEllipseShapeCall24>(taken[24]);
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
      CuteQQuickEllipseShapeCall25 call = reinterpret_cast<CuteQQuickEllipseShapeCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall26 call = reinterpret_cast<CuteQQuickEllipseShapeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall27 call = reinterpret_cast<CuteQQuickEllipseShapeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall28 call = reinterpret_cast<CuteQQuickEllipseShapeCall28>(taken[28]);
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
      CuteQQuickEllipseShapeCall29 call = reinterpret_cast<CuteQQuickEllipseShapeCall29>(taken[29]);
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
      CuteQQuickEllipseShapeCall30 call = reinterpret_cast<CuteQQuickEllipseShapeCall30>(taken[30]);
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
      CuteQQuickEllipseShapeCall31 call = reinterpret_cast<CuteQQuickEllipseShapeCall31>(taken[31]);
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
      CuteQQuickEllipseShapeCall32 call = reinterpret_cast<CuteQQuickEllipseShapeCall32>(taken[32]);
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
      CuteQQuickEllipseShapeCall33 call = reinterpret_cast<CuteQQuickEllipseShapeCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickEllipseShapeCall34 call = reinterpret_cast<CuteQQuickEllipseShapeCall34>(taken[34]);
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
      CuteQQuickEllipseShapeCall35 call = reinterpret_cast<CuteQQuickEllipseShapeCall35>(taken[35]);
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
      CuteQQuickEllipseShapeCall36 call = reinterpret_cast<CuteQQuickEllipseShapeCall36>(taken[36]);
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
      CuteQQuickEllipseShapeCall37 call = reinterpret_cast<CuteQQuickEllipseShapeCall37>(taken[37]);
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
      CuteQQuickEllipseShapeCall38 call = reinterpret_cast<CuteQQuickEllipseShapeCall38>(taken[38]);
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
      CuteQQuickEllipseShapeCall39 call = reinterpret_cast<CuteQQuickEllipseShapeCall39>(taken[39]);
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
      CuteQQuickEllipseShapeCall40 call = reinterpret_cast<CuteQQuickEllipseShapeCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickEllipseShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickEllipseShape10metaObjectEv(
    const QQuickEllipseShape *self) {
  return self->metaObject();
}

//  QString QQuickEllipseShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickEllipseShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickEllipseShape::tr(s, c, n));
}

//  QQuickEllipseShape::QQuickEllipseShape(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickEllipseShape *ritual_ZN18QQuickEllipseShapeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickEllipseShape(parent);
}

//  QQuickEllipseShape::~QQuickEllipseShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShapeD1Ev(QQuickEllipseShape *self) {
  delete self;
}

//  qreal QQuickEllipseShape::sweepAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape10sweepAngleEv(
    const QQuickEllipseShape *self) {
  return self->sweepAngle();
}

//  void QQuickEllipseShape::setSweepAngle(qreal sweepAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape13setSweepAngleEd(
    QQuickEllipseShape *self,
    qreal sweepAngle) {
  self->setSweepAngle(sweepAngle);
}

//  qreal QQuickEllipseShape::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape10startAngleEv(
    const QQuickEllipseShape *self) {
  return self->startAngle();
}

//  void QQuickEllipseShape::setStartAngle(qreal startAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape13setStartAngleEd(
    QQuickEllipseShape *self,
    qreal startAngle) {
  self->setStartAngle(startAngle);
}

//  qreal QQuickEllipseShape::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape10dashOffsetEv(
    const QQuickEllipseShape *self) {
  return self->dashOffset();
}

//  void QQuickEllipseShape::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape13setDashOffsetEd(
    QQuickEllipseShape *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  qreal QQuickEllipseShape::innerArcRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape13innerArcRatioEv(
    const QQuickEllipseShape *self) {
  return self->innerArcRatio();
}

//  void QQuickEllipseShape::setInnerArcRatio(qreal innerArcRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape16setInnerArcRatioEd(
    QQuickEllipseShape *self,
    qreal innerArcRatio) {
  self->setInnerArcRatio(innerArcRatio);
}

//  qreal QQuickEllipseShape::cornerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape12cornerRadiusEv(
    const QQuickEllipseShape *self) {
  return self->cornerRadius();
}

//  void QQuickEllipseShape::setCornerRadius(qreal cornerRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape15setCornerRadiusEd(
    QQuickEllipseShape *self,
    qreal cornerRadius) {
  self->setCornerRadius(cornerRadius);
}

//  qreal QQuickEllipseShape::strokeWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickEllipseShape11strokeWidthEv(
    const QQuickEllipseShape *self) {
  return self->strokeWidth();
}

//  void QQuickEllipseShape::setStrokeWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape14setStrokeWidthEd(
    QQuickEllipseShape *self,
    qreal width) {
  self->setStrokeWidth(width);
}

//  QColor QQuickEllipseShape::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QQuickEllipseShape9fillColorEv(
    const QQuickEllipseShape *self) {
  return new QColor(self->fillColor());
}

//  void QQuickEllipseShape::setFillColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape12setFillColorERK6QColor(
    QQuickEllipseShape *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QColor QQuickEllipseShape::strokeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QQuickEllipseShape11strokeColorEv(
    const QQuickEllipseShape *self) {
  return new QColor(self->strokeColor());
}

//  void QQuickEllipseShape::setStrokeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape14setStrokeColorERK6QColor(
    QQuickEllipseShape *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  QQuickShapePath::CapStyle QQuickEllipseShape::capStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::CapStyle ritual_ZNK18QQuickEllipseShape8capStyleEv(
    const QQuickEllipseShape *self) {
  return self->capStyle();
}

//  void QQuickEllipseShape::setCapStyle(QQuickShapePath::CapStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape11setCapStyleEN15QQuickShapePath8CapStyleE(
    QQuickEllipseShape *self,
    QQuickShapePath::CapStyle style) {
  self->setCapStyle(style);
}

//  QQuickShapePath::JoinStyle QQuickEllipseShape::joinStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::JoinStyle ritual_ZNK18QQuickEllipseShape9joinStyleEv(
    const QQuickEllipseShape *self) {
  return self->joinStyle();
}

//  void QQuickEllipseShape::setJoinStyle(QQuickShapePath::JoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape12setJoinStyleEN15QQuickShapePath9JoinStyleE(
    QQuickEllipseShape *self,
    QQuickShapePath::JoinStyle style) {
  self->setJoinStyle(style);
}

//  QQuickShapePath::StrokeStyle QQuickEllipseShape::strokeStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::StrokeStyle ritual_ZNK18QQuickEllipseShape11strokeStyleEv(
    const QQuickEllipseShape *self) {
  return self->strokeStyle();
}

//  void QQuickEllipseShape::setStrokeStyle(QQuickShapePath::StrokeStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape14setStrokeStyleEN15QQuickShapePath11StrokeStyleE(
    QQuickEllipseShape *self,
    QQuickShapePath::StrokeStyle style) {
  self->setStrokeStyle(style);
}

//  QQuickShapePath::FillRule QQuickEllipseShape::fillRule() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::FillRule ritual_ZNK18QQuickEllipseShape8fillRuleEv(
    const QQuickEllipseShape *self) {
  return self->fillRule();
}

//  void QQuickEllipseShape::setFillRule(QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape11setFillRuleEN15QQuickShapePath8FillRuleE(
    QQuickEllipseShape *self,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  QQuickShapeGradient *QQuickEllipseShape::fillGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK18QQuickEllipseShape12fillGradientEv(
    const QQuickEllipseShape *self) {
  return self->fillGradient();
}

//  void QQuickEllipseShape::setFillGradient(QQuickShapeGradient
//      *fillGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape15setFillGradientEP19QQuickShapeGradient(
    QQuickEllipseShape *self,
    QQuickShapeGradient *fillGradient) {
  self->setFillGradient(fillGradient);
}

//  void QQuickEllipseShape::resetFillGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape17resetFillGradientEv(
    QQuickEllipseShape *self) {
  self->resetFillGradient();
}

//  BorderMode QQuickEllipseShape::borderMode() const
extern "C" Q_DECL_EXPORT
QQuickEllipseShape::BorderMode ritual_ZNK18QQuickEllipseShape10borderModeEv(
    const QQuickEllipseShape *self) {
  return self->borderMode();
}

//  void QQuickEllipseShape::setBorderMode(BorderMode borderMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape13setBorderModeENS_10BorderModeE(
    QQuickEllipseShape *self,
    QQuickEllipseShape::BorderMode borderMode) {
  self->setBorderMode(borderMode);
}

//  void QQuickEllipseShape::resetBorderMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape15resetBorderModeEv(
    QQuickEllipseShape *self) {
  self->resetBorderMode();
}

//  QQuickItem *QQuickEllipseShape::fillItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickEllipseShape8fillItemEv(
    const QQuickEllipseShape *self) {
  return self->fillItem();
}

//  void QQuickEllipseShape::setFillItem(QQuickItem *newFillItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape11setFillItemEP10QQuickItem(
    QQuickEllipseShape *self,
    QQuickItem *newFillItem) {
  self->setFillItem(newFillItem);
}

//  void QQuickEllipseShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickEllipseShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickEllipseShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickEllipseShapePrivate *QQuickEllipseShape::d_func()
extern "C" Q_DECL_EXPORT
QQuickEllipseShapePrivate *ritual_ZN18QQuickEllipseShape6d_funcEv(
    QQuickEllipseShape *self) {
  return self->d_func();
}

//  const QQuickEllipseShapePrivate *QQuickEllipseShape::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickEllipseShapePrivate *ritual_ZNK18QQuickEllipseShape6d_funcEv(
    const QQuickEllipseShape *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickEllipseShape, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickEllipseShape(
    QQuickEllipseShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickEllipseShape *>(self)->take(key, call);
}

//  void QQuickEllipseShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickEllipseShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickEllipseShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickEllipseShape *>(self)->OwnQQuickEllipseShape::itemChange(
      change,
      *value);
}
